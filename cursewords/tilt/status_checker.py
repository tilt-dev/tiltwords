from __future__ import print_function

import threading
import time
import tilt_dev.python_client as clientlib
from tilt_dev.python_client.exceptions import ApiException
from kubernetes import config

CONFIG_PATH = "~/.tilt-dev/config"
CONTEXT = "tilt-default"

Session = clientlib.models.v1alpha1_session.V1alpha1Session
Target = clientlib.models.v1alpha1_target.V1alpha1Target

class StatusChecker(threading.Thread):
    def __init__(self):
        self.any_red = False
        self.any_in_progress = True
        cfg = clientlib.Configuration()
        config.load_kube_config(CONFIG_PATH, CONTEXT, client_configuration=cfg)
        api_instance = clientlib.TiltDevV1alpha1Api(clientlib.ApiClient(cfg))
        api_instance.api_client.default_headers['Authorization'] = cfg.get_api_key_with_prefix('authorization')
        self.cli = api_instance
        super().__init__(daemon=True)

    def can_play(self):
        return not self.any_red and self.any_in_progress

    def run(self):
        try:
            while True:
                try:
                    session = self.cli.read_session("Tiltfile")
                    self.any_red = _any_targets_red(session)
                    self.any_in_progress = _any_targets_in_progress(session)
                    time.sleep(0.5)
                except ApiException as e:
                    print("tilt session exception")
                    raise e
        finally:
            self.cli.api_client.close()

def _target_is_red(target: Target) -> bool:
    return target.state.terminated and target.state.terminated.error

def _any_targets_red(session: Session) -> bool:
    return any([_target_is_red(target) for target in session.status.targets])

def _target_is_in_progress(target: Target) -> bool:
    state = target.state
    if not (state.waiting or state.active or state.terminated):
        return False
    if target.type == "server":
        return not state.waiting or (state.active and not state.active.ready)
    elif target.type == "job":
        return not state.terminated
    else:
        raise Exception("target bad on {}: {}".format(target.name, target.type))

def _any_targets_in_progress(session: Session) -> bool:
    return any([_target_is_in_progress(target) for target in session.status.targets])

# def _target_is_in_progress(target: Target) -> bool:
#     state = target.state
#     if not (state.waiting or state.active or state.terminated):
#         # target has not been requested to run (e.g. auto_init = false)
#         # so it's certainly not "in progress"
#         return False

#     if target.type == "server":
#         # case 1: server -- if it's waiting to build, or if it's active but not
#         # ready, then it's "in progress"
#         return not state.waiting or (state.active and not state.active.ready)
#     elif target.type == "job":
#         # case 2: job -- if it hasn't finished running, it's "in progress"
#         return not state.terminated
#     else:
#         raise Exception("Unrecognized target type for target {}: {}".format(
#             target.name, target.type
#         ))

# class StatusChecker(threading.Thread):
#     def __init__(self, sleep_secs=0.5, debug=False):
#         self.any_red = False
#         self.any_in_progress = True

#         self.sleep_secs = sleep_secs
#         self.debug = debug

#         # TODO: error handling
#         cfg = clientlib.Configuration()
#         config.load_kube_config(CONFIG_PATH, CONTEXT,
#                                 client_configuration=cfg)

#         # TODO: client should be initialized in a `with` so cleanup happens automatically
#         api_client = clientlib.ApiClient(cfg)
#         api_instance = clientlib.TiltDevV1alpha1Api(api_client)

#         # Bearer Auth doesn't work right with Python codegen, sigh, so just add auth
#         # info to all request headers.
#         # https://github.com/OpenAPITools/openapi-generator/issues/8865
#         api_instance.api_client.default_headers['Authorization'] = cfg.get_api_key_with_prefix('authorization')

#         self.cli = api_instance

#         super().__init__(daemon=True)

#     def can_play(self):
#         # Go play your crossword puzzle if:
#         # - at least one resource is still in progress (i.e. running a build/update)
#         # - no resources are red
#         return not self.any_red and self.any_in_progress

#     def run(self):
#         try:
#             while True:
#                 try:
#                     session = self.cli.read_session("Tiltfile")

#                     self.any_red = _any_targets_red(session)
#                     self.any_in_progress = _any_targets_in_progress(session)
#                     time.sleep(self.sleep_secs)
#                 except ApiException as e:
#                     print("Exception when getting Tilt session: Tiltfile")
#                     raise e

#         finally:
#             # is there a slicker way to do this teardown automatically?
#             self.cli.api_client.close()
