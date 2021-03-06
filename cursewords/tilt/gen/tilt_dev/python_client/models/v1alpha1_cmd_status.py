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


class V1alpha1CmdStatus(object):
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
        'ready': 'bool',
        'running': 'V1alpha1CmdStateRunning',
        'terminated': 'V1alpha1CmdStateTerminated',
        'waiting': 'V1alpha1CmdStateWaiting'
    }

    attribute_map = {
        'ready': 'ready',
        'running': 'running',
        'terminated': 'terminated',
        'waiting': 'waiting'
    }

    def __init__(self, ready=None, running=None, terminated=None, waiting=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CmdStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ready = None
        self._running = None
        self._terminated = None
        self._waiting = None
        self.discriminator = None

        if ready is not None:
            self.ready = ready
        if running is not None:
            self.running = running
        if terminated is not None:
            self.terminated = terminated
        if waiting is not None:
            self.waiting = waiting

    @property
    def ready(self):
        """Gets the ready of this V1alpha1CmdStatus.  # noqa: E501

        Specifies whether the command has passed its readiness probe.  Terminating the command does not change its Ready state.  Is always true when no readiness probe is defined.  # noqa: E501

        :return: The ready of this V1alpha1CmdStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1alpha1CmdStatus.

        Specifies whether the command has passed its readiness probe.  Terminating the command does not change its Ready state.  Is always true when no readiness probe is defined.  # noqa: E501

        :param ready: The ready of this V1alpha1CmdStatus.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def running(self):
        """Gets the running of this V1alpha1CmdStatus.  # noqa: E501


        :return: The running of this V1alpha1CmdStatus.  # noqa: E501
        :rtype: V1alpha1CmdStateRunning
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this V1alpha1CmdStatus.


        :param running: The running of this V1alpha1CmdStatus.  # noqa: E501
        :type: V1alpha1CmdStateRunning
        """

        self._running = running

    @property
    def terminated(self):
        """Gets the terminated of this V1alpha1CmdStatus.  # noqa: E501


        :return: The terminated of this V1alpha1CmdStatus.  # noqa: E501
        :rtype: V1alpha1CmdStateTerminated
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this V1alpha1CmdStatus.


        :param terminated: The terminated of this V1alpha1CmdStatus.  # noqa: E501
        :type: V1alpha1CmdStateTerminated
        """

        self._terminated = terminated

    @property
    def waiting(self):
        """Gets the waiting of this V1alpha1CmdStatus.  # noqa: E501


        :return: The waiting of this V1alpha1CmdStatus.  # noqa: E501
        :rtype: V1alpha1CmdStateWaiting
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this V1alpha1CmdStatus.


        :param waiting: The waiting of this V1alpha1CmdStatus.  # noqa: E501
        :type: V1alpha1CmdStateWaiting
        """

        self._waiting = waiting

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
        if not isinstance(other, V1alpha1CmdStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CmdStatus):
            return True

        return self.to_dict() != other.to_dict()
