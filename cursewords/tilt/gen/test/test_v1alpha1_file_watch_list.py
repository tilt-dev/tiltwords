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
from tilt-dev/python-kubernetes.client.models.v1alpha1_file_watch_list import V1alpha1FileWatchList  # noqa: E501
from tilt-dev/python-kubernetes.client.rest import ApiException

class TestV1alpha1FileWatchList(unittest.TestCase):
    """V1alpha1FileWatchList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1FileWatchList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tilt-dev/python-kubernetes.client.models.v1alpha1_file_watch_list.V1alpha1FileWatchList()  # noqa: E501
        if include_optional :
            return V1alpha1FileWatchList(
                api_version = '0',
                items = [
                    tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch.v1alpha1.FileWatch(
                        api_version = '0',
                        kind = '0',
                        metadata = tilt-dev/python-kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                },
                            cluster_name = '0',
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            deletion_grace_period_seconds = 56,
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            finalizers = [
                                '0'
                                ],
                            generate_name = '0',
                            generation = 56,
                            labels = {
                                'key' : '0'
                                },
                            managed_fields = [
                                tilt-dev/python-kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0',
                                    fields_type = '0',
                                    fields_v1 = tilt-dev/python-kubernetes.client.models.fields_v1.fieldsV1(),
                                    manager = '0',
                                    operation = '0',
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ],
                            name = '0',
                            namespace = '0',
                            owner_references = [
                                tilt-dev/python-kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0',
                                    block_owner_deletion = True,
                                    controller = True,
                                    kind = '0',
                                    name = '0',
                                    uid = '0', )
                                ],
                            resource_version = '0',
                            self_link = '0',
                            uid = '0', ),
                        spec = tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch_spec.v1alpha1.FileWatchSpec(
                            ignores = [
                                tilt-dev/python-kubernetes.client.models.v1alpha1/ignore_def.v1alpha1.IgnoreDef(
                                    base_path = '0',
                                    patterns = [
                                        '0'
                                        ], )
                                ],
                            watched_paths = [
                                '0'
                                ], ),
                        status = tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch_status.v1alpha1.FileWatchStatus(
                            error = '0',
                            file_events = [
                                tilt-dev/python-kubernetes.client.models.v1alpha1/file_event.v1alpha1.FileEvent(
                                    seen_files = [
                                        '0'
                                        ],
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ],
                            last_event_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            monitor_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
                kind = '0',
                metadata = tilt-dev/python-kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0',
                    remaining_item_count = 56,
                    resource_version = '0',
                    self_link = '0', )
            )
        else :
            return V1alpha1FileWatchList(
                items = [
                    tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch.v1alpha1.FileWatch(
                        api_version = '0',
                        kind = '0',
                        metadata = tilt-dev/python-kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                },
                            cluster_name = '0',
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            deletion_grace_period_seconds = 56,
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            finalizers = [
                                '0'
                                ],
                            generate_name = '0',
                            generation = 56,
                            labels = {
                                'key' : '0'
                                },
                            managed_fields = [
                                tilt-dev/python-kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0',
                                    fields_type = '0',
                                    fields_v1 = tilt-dev/python-kubernetes.client.models.fields_v1.fieldsV1(),
                                    manager = '0',
                                    operation = '0',
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ],
                            name = '0',
                            namespace = '0',
                            owner_references = [
                                tilt-dev/python-kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0',
                                    block_owner_deletion = True,
                                    controller = True,
                                    kind = '0',
                                    name = '0',
                                    uid = '0', )
                                ],
                            resource_version = '0',
                            self_link = '0',
                            uid = '0', ),
                        spec = tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch_spec.v1alpha1.FileWatchSpec(
                            ignores = [
                                tilt-dev/python-kubernetes.client.models.v1alpha1/ignore_def.v1alpha1.IgnoreDef(
                                    base_path = '0',
                                    patterns = [
                                        '0'
                                        ], )
                                ],
                            watched_paths = [
                                '0'
                                ], ),
                        status = tilt-dev/python-kubernetes.client.models.v1alpha1/file_watch_status.v1alpha1.FileWatchStatus(
                            error = '0',
                            file_events = [
                                tilt-dev/python-kubernetes.client.models.v1alpha1/file_event.v1alpha1.FileEvent(
                                    seen_files = [
                                        '0'
                                        ],
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ],
                            last_event_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                            monitor_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ],
        )

    def testV1alpha1FileWatchList(self):
        """Test V1alpha1FileWatchList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()