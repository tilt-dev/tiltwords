# coding: utf-8

"""
    tilt

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.20.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tilt_dev.python_client.configuration import Configuration


class V1alpha1KubernetesDiscoveryStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'monitor_start_time': 'datetime',
        'pods': 'list[V1alpha1Pod]'
    }

    attribute_map = {
        'monitor_start_time': 'monitorStartTime',
        'pods': 'pods'
    }

    def __init__(self, monitor_start_time=None, pods=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1KubernetesDiscoveryStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._monitor_start_time = None
        self._pods = None
        self.discriminator = None

        if monitor_start_time is not None:
            self.monitor_start_time = monitor_start_time
        self.pods = pods

    @property
    def monitor_start_time(self):
        """Gets the monitor_start_time of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501

        MonitorStartTime is the timestamp of when Kubernetes resource discovery was started.  It is zero if discovery has not been started yet.  # noqa: E501

        :return: The monitor_start_time of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._monitor_start_time

    @monitor_start_time.setter
    def monitor_start_time(self, monitor_start_time):
        """Sets the monitor_start_time of this V1alpha1KubernetesDiscoveryStatus.

        MonitorStartTime is the timestamp of when Kubernetes resource discovery was started.  It is zero if discovery has not been started yet.  # noqa: E501

        :param monitor_start_time: The monitor_start_time of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501
        :type: datetime
        """

        self._monitor_start_time = monitor_start_time

    @property
    def pods(self):
        """Gets the pods of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501

        Pods that have been discovered based on the criteria in the spec.  # noqa: E501

        :return: The pods of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501
        :rtype: list[V1alpha1Pod]
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this V1alpha1KubernetesDiscoveryStatus.

        Pods that have been discovered based on the criteria in the spec.  # noqa: E501

        :param pods: The pods of this V1alpha1KubernetesDiscoveryStatus.  # noqa: E501
        :type: list[V1alpha1Pod]
        """
        if self.local_vars_configuration.client_side_validation and pods is None:  # noqa: E501
            raise ValueError("Invalid value for `pods`, must not be `None`")  # noqa: E501

        self._pods = pods

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1KubernetesDiscoveryStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1KubernetesDiscoveryStatus):
            return True

        return self.to_dict() != other.to_dict()