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


class TiltChecker(threading.Thread):
    def __init__(self, starting_seconds=0, is_running=True, active=True):
        self.starting_seconds = starting_seconds
        self.is_running = is_running
        self.active = active

        self.start_time = None
        self.time_passed = None

        super().__init__(daemon=True)

    def run(self):
        self.start_time = time.time()
        self.time_passed = self.starting_seconds

        while self.active:
            if self.is_running:
                self.time_passed = (self.starting_seconds
                                    + int(time.time() - self.start_time))

            time.sleep(0.5)

    def is_div5(self):
        _, seconds = divmod(self.time_passed, 60)
        return seconds % 5 == 0


if __name__ == "__main__":
    cfg = clientlib.Configuration()

    config.load_kube_config(TILT_API_CONFIG_PATH, TILT_API_CONTEXT,
                            client_configuration=cfg)

    with clientlib.ApiClient(cfg) as api_client:
        api_instance = clientlib.TiltDevV1alpha1Api(api_client)

        # Bearer Auth doesn't work right with Python codegen, sigh, so just add auth
        # info to all request headers.
        # https://github.com/OpenAPITools/openapi-generator/issues/8865
        api_instance.api_client.default_headers['Authorization'] = cfg.get_api_key_with_prefix('authorization')

        try:
            api_response = api_instance.list_session()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TiltDevV1alpha1Api->list_session: %s\n" % e)
