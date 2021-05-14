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


class V1alpha1TargetStateTerminated(object):
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
        'error': 'str',
        'finish_time': 'datetime',
        'start_time': 'datetime'
    }

    attribute_map = {
        'error': 'error',
        'finish_time': 'finishTime',
        'start_time': 'startTime'
    }

    def __init__(self, error=None, finish_time=None, start_time=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1TargetStateTerminated - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._finish_time = None
        self._start_time = None
        self.discriminator = None

        if error is not None:
            self.error = error
        self.finish_time = finish_time
        self.start_time = start_time

    @property
    def error(self):
        """Gets the error of this V1alpha1TargetStateTerminated.  # noqa: E501

        Error is a non-empty string if the target encountered a failure during execution that caused it to stop.  For targets of type TargetTypeServer, this is always populated, as the target is expected to run indefinitely, and thus any termination is an error.  # noqa: E501

        :return: The error of this V1alpha1TargetStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1alpha1TargetStateTerminated.

        Error is a non-empty string if the target encountered a failure during execution that caused it to stop.  For targets of type TargetTypeServer, this is always populated, as the target is expected to run indefinitely, and thus any termination is an error.  # noqa: E501

        :param error: The error of this V1alpha1TargetStateTerminated.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def finish_time(self):
        """Gets the finish_time of this V1alpha1TargetStateTerminated.  # noqa: E501

        FinishTime is when the target stopped executing.  # noqa: E501

        :return: The finish_time of this V1alpha1TargetStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this V1alpha1TargetStateTerminated.

        FinishTime is when the target stopped executing.  # noqa: E501

        :param finish_time: The finish_time of this V1alpha1TargetStateTerminated.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and finish_time is None:  # noqa: E501
            raise ValueError("Invalid value for `finish_time`, must not be `None`")  # noqa: E501

        self._finish_time = finish_time

    @property
    def start_time(self):
        """Gets the start_time of this V1alpha1TargetStateTerminated.  # noqa: E501

        StartTime is when the target began executing.  # noqa: E501

        :return: The start_time of this V1alpha1TargetStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1alpha1TargetStateTerminated.

        StartTime is when the target began executing.  # noqa: E501

        :param start_time: The start_time of this V1alpha1TargetStateTerminated.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

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
        if not isinstance(other, V1alpha1TargetStateTerminated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1TargetStateTerminated):
            return True

        return self.to_dict() != other.to_dict()
