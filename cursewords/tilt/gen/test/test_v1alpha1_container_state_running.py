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
from tilt-dev/python-kubernetes.client.models.v1alpha1_container_state_running import V1alpha1ContainerStateRunning  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException

class TestV1alpha1ContainerStateRunning(unittest.TestCase):
    """V1alpha1ContainerStateRunning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ContainerStateRunning
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tilt-dev/python-kubernetes.client.models.v1alpha1_container_state_running.V1alpha1ContainerStateRunning()  # noqa: E501
        if include_optional :
            return V1alpha1ContainerStateRunning(
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return V1alpha1ContainerStateRunning(
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testV1alpha1ContainerStateRunning(self):
        """Test V1alpha1ContainerStateRunning"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
