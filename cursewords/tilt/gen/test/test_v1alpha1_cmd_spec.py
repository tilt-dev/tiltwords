# coding: utf-8

"""
    tilt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.20.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tilt_dev.python-kubernetes.client
from tilt-dev/python-kubernetes.client.models.v1alpha1_cmd_spec import V1alpha1CmdSpec  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException

class TestV1alpha1CmdSpec(unittest.TestCase):
    """V1alpha1CmdSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1CmdSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tilt-dev/python-kubernetes.client.models.v1alpha1_cmd_spec.V1alpha1CmdSpec()  # noqa: E501
        if include_optional :
            return V1alpha1CmdSpec(
                args = [
                    '0'
                    ],
                dir = '0',
                env = [
                    '0'
                    ],
                readiness_probe = tilt-dev/python-kubernetes.client.models.v1alpha1/probe.v1alpha1.Probe(
                    exec = tilt-dev/python-kubernetes.client.models.v1alpha1/exec_action.v1alpha1.ExecAction(
                        command = [
                            '0'
                            ], ),
                    failure_threshold = 56,
                    http_get = tilt-dev/python-kubernetes.client.models.v1alpha1/http_get_action.v1alpha1.HTTPGetAction(
                        host = '0',
                        http_headers = [
                            tilt-dev/python-kubernetes.client.models.v1alpha1/http_header.v1alpha1.HTTPHeader(
                                name = '0',
                                value = '0', )
                            ],
                        path = '0',
                        port = 56,
                        scheme = '0', ),
                    initial_delay_seconds = 56,
                    period_seconds = 56,
                    success_threshold = 56,
                    tcp_socket = tilt-dev/python-kubernetes.client.models.v1alpha1/tcp_socket_action.v1alpha1.TCPSocketAction(
                        host = '0',
                        port = 56, ),
                    timeout_seconds = 56, ),
                restart_on = tilt-dev/python-kubernetes.client.models.v1alpha1/restart_on_spec.v1alpha1.RestartOnSpec(
                    file_watches = [
                        '0'
                        ], )
            )
        else :
            return V1alpha1CmdSpec(
        )

    def testV1alpha1CmdSpec(self):
        """Test V1alpha1CmdSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
