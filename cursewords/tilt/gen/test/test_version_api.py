# coding: utf-8

"""
    tilt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.20.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import tilt_dev.python-kubernetes.client
from tilt-dev/python-kubernetes.client.api.version_api import VersionApi  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""

    def setUp(self):
        self.api = tilt-dev/python-kubernetes.client.api.version_api.VersionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_code(self):
        """Test case for get_code

        """
        pass


if __name__ == '__main__':
    unittest.main()