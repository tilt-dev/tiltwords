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
from tilt-dev/python-kubernetes.client.models.v1alpha1_ui_session_status import V1alpha1UISessionStatus  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException

class TestV1alpha1UISessionStatus(unittest.TestCase):
    """V1alpha1UISessionStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1UISessionStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tilt-dev/python-kubernetes.client.models.v1alpha1_ui_session_status.V1alpha1UISessionStatus()  # noqa: E501
        if include_optional :
            return V1alpha1UISessionStatus(
                fatal_error = '0',
                feature_flags = [
                    tilt-dev/python-kubernetes.client.models.v1alpha1/ui_feature_flag.v1alpha1.UIFeatureFlag(
                        name = '0',
                        value = True, )
                    ],
                needs_analytics_nudge = True,
                running_tilt_build = tilt-dev/python-kubernetes.client.models.v1alpha1/tilt_build.v1alpha1.TiltBuild(
                    commit_sha = '0',
                    date = '0',
                    dev = True,
                    version = '0', ),
                suggested_tilt_version = '0',
                tilt_cloud_scheme_host = '0',
                tilt_cloud_team_id = '0',
                tilt_cloud_team_name = '0',
                tilt_cloud_username = '0',
                tilt_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tiltfile_key = '0',
                version_settings = tilt-dev/python-kubernetes.client.models.v1alpha1/version_settings.v1alpha1.VersionSettings(
                    check_updates = True, )
            )
        else :
            return V1alpha1UISessionStatus(
                fatal_error = '0',
                feature_flags = [
                    tilt-dev/python-kubernetes.client.models.v1alpha1/ui_feature_flag.v1alpha1.UIFeatureFlag(
                        name = '0',
                        value = True, )
                    ],
                needs_analytics_nudge = True,
                running_tilt_build = tilt-dev/python-kubernetes.client.models.v1alpha1/tilt_build.v1alpha1.TiltBuild(
                    commit_sha = '0',
                    date = '0',
                    dev = True,
                    version = '0', ),
                suggested_tilt_version = '0',
                tilt_cloud_scheme_host = '0',
                tilt_cloud_team_id = '0',
                tilt_cloud_team_name = '0',
                tilt_cloud_username = '0',
                tilt_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tiltfile_key = '0',
                version_settings = tilt-dev/python-kubernetes.client.models.v1alpha1/version_settings.v1alpha1.VersionSettings(
                    check_updates = True, ),
        )

    def testV1alpha1UISessionStatus(self):
        """Test V1alpha1UISessionStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
