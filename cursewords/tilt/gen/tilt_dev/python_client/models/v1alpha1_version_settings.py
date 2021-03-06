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


class V1alpha1VersionSettings(object):
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
        'check_updates': 'bool'
    }

    attribute_map = {
        'check_updates': 'checkUpdates'
    }

    def __init__(self, check_updates=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1VersionSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_updates = None
        self.discriminator = None

        self.check_updates = check_updates

    @property
    def check_updates(self):
        """Gets the check_updates of this V1alpha1VersionSettings.  # noqa: E501

        Whether version updates have been enabled/disabled from the Tiltfile.  # noqa: E501

        :return: The check_updates of this V1alpha1VersionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._check_updates

    @check_updates.setter
    def check_updates(self, check_updates):
        """Sets the check_updates of this V1alpha1VersionSettings.

        Whether version updates have been enabled/disabled from the Tiltfile.  # noqa: E501

        :param check_updates: The check_updates of this V1alpha1VersionSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and check_updates is None:  # noqa: E501
            raise ValueError("Invalid value for `check_updates`, must not be `None`")  # noqa: E501

        self._check_updates = check_updates

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
        if not isinstance(other, V1alpha1VersionSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1VersionSettings):
            return True

        return self.to_dict() != other.to_dict()
