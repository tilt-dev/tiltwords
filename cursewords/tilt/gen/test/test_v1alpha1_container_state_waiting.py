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
from tilt-dev/python-kubernetes.client.models.v1alpha1_container_state_waiting import V1alpha1ContainerStateWaiting  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException

class TestV1alpha1ContainerStateWaiting(unittest.TestCase):
    """V1alpha1ContainerStateWaiting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ContainerStateWaiting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tilt-dev/python-kubernetes.client.models.v1alpha1_container_state_waiting.V1alpha1ContainerStateWaiting()  # noqa: E501
        if include_optional :
            return V1alpha1ContainerStateWaiting(
                reason = '0'
            )
        else :
            return V1alpha1ContainerStateWaiting(
                reason = '0',
        )

    def testV1alpha1ContainerStateWaiting(self):
        """Test V1alpha1ContainerStateWaiting"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
