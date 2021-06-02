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


class V1alpha1CmdStateTerminated(object):
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
        'exit_code': 'int',
        'finished_at': 'datetime',
        'pid': 'int',
        'reason': 'str',
        'started_at': 'datetime'
    }

    attribute_map = {
        'exit_code': 'exitCode',
        'finished_at': 'finishedAt',
        'pid': 'pid',
        'reason': 'reason',
        'started_at': 'startedAt'
    }

    def __init__(self, exit_code=None, finished_at=None, pid=None, reason=None, started_at=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CmdStateTerminated - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exit_code = None
        self._finished_at = None
        self._pid = None
        self._reason = None
        self._started_at = None
        self.discriminator = None

        self.exit_code = exit_code
        if finished_at is not None:
            self.finished_at = finished_at
        self.pid = pid
        if reason is not None:
            self.reason = reason
        if started_at is not None:
            self.started_at = started_at

    @property
    def exit_code(self):
        """Gets the exit_code of this V1alpha1CmdStateTerminated.  # noqa: E501

        Exit status from the last termination of the command  # noqa: E501

        :return: The exit_code of this V1alpha1CmdStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this V1alpha1CmdStateTerminated.

        Exit status from the last termination of the command  # noqa: E501

        :param exit_code: The exit_code of this V1alpha1CmdStateTerminated.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and exit_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exit_code`, must not be `None`")  # noqa: E501

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """Gets the finished_at of this V1alpha1CmdStateTerminated.  # noqa: E501

        Time at which the command last terminated  # noqa: E501

        :return: The finished_at of this V1alpha1CmdStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1alpha1CmdStateTerminated.

        Time at which the command last terminated  # noqa: E501

        :param finished_at: The finished_at of this V1alpha1CmdStateTerminated.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def pid(self):
        """Gets the pid of this V1alpha1CmdStateTerminated.  # noqa: E501

        The process id of the command.  # noqa: E501

        :return: The pid of this V1alpha1CmdStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this V1alpha1CmdStateTerminated.

        The process id of the command.  # noqa: E501

        :param pid: The pid of this V1alpha1CmdStateTerminated.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pid is None:  # noqa: E501
            raise ValueError("Invalid value for `pid`, must not be `None`")  # noqa: E501

        self._pid = pid

    @property
    def reason(self):
        """Gets the reason of this V1alpha1CmdStateTerminated.  # noqa: E501

        (brief) reason the process is terminated  # noqa: E501

        :return: The reason of this V1alpha1CmdStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1alpha1CmdStateTerminated.

        (brief) reason the process is terminated  # noqa: E501

        :param reason: The reason of this V1alpha1CmdStateTerminated.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def started_at(self):
        """Gets the started_at of this V1alpha1CmdStateTerminated.  # noqa: E501

        Time at which previous execution of the command started  # noqa: E501

        :return: The started_at of this V1alpha1CmdStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1alpha1CmdStateTerminated.

        Time at which previous execution of the command started  # noqa: E501

        :param started_at: The started_at of this V1alpha1CmdStateTerminated.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

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
        if not isinstance(other, V1alpha1CmdStateTerminated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CmdStateTerminated):
            return True

        return self.to_dict() != other.to_dict()