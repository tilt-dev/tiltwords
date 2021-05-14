from __future__ import print_function

import threading
import time
import tilt_dev.python_client as clientlib
from tilt_dev.python_client.exceptions import ApiException
from pprint import pprint
from kubernetes import config

# TODO: get the dir correctly
TILT_API_CONFIG_PATH = "/Users/maia/.windmill/config"
TILT_API_CONTEXT = "tilt-default"

# type alias
Session = clientlib.models.v1alpha1_session.V1alpha1Session
Target = clientlib.models.v1alpha1_target.V1alpha1Target


def _any_targets_red(session: Session) -> bool:
    return any([_target_is_red(target) for target in session.status.targets])


def _target_is_red(target: Target) -> bool:
    return target.state.terminated and target.state.terminated.error


class TiltChecker(threading.Thread):
    def __init__(self, sleep_secs=0.5, debug=False):
        self.any_red = False
        self.sleep_secs = sleep_secs
        self.debug = debug

        # TODO: error handling
        cfg = clientlib.Configuration()
        config.load_kube_config(TILT_API_CONFIG_PATH, TILT_API_CONTEXT,
                                client_configuration=cfg)

        # TODO: client should be initialized in a `with` so cleanup happens automatically
        api_client = clientlib.ApiClient(cfg)
        api_instance = clientlib.TiltDevV1alpha1Api(api_client)

        # Bearer Auth doesn't work right with Python codegen, sigh, so just add auth
        # info to all request headers.
        # https://github.com/OpenAPITools/openapi-generator/issues/8865
        api_instance.api_client.default_headers['Authorization'] = cfg.get_api_key_with_prefix('authorization')

        self.cli = api_instance

        super().__init__(daemon=True)

    def check_any_red(self):
        try:
            session = self.cli.read_session("Tiltfile")
            # no error = tilt is running
            self.any_red = _any_targets_red(session)
        except ApiException as e:
            print("Exception when getting Tilt session: Tiltfile")
            raise e

    def run(self):
        try:
            while True:
                self.check_any_red()
                time.sleep(self.sleep_secs)
        finally:
            self.cli.api_client.close()  # is there a slicker way to do this teardown automatically?
