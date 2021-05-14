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


class V1alpha1FileWatchStatus(object):
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
        'file_events': 'list[V1alpha1FileEvent]',
        'last_event_time': 'datetime',
        'monitor_start_time': 'datetime'
    }

    attribute_map = {
        'error': 'error',
        'file_events': 'fileEvents',
        'last_event_time': 'lastEventTime',
        'monitor_start_time': 'monitorStartTime'
    }

    def __init__(self, error=None, file_events=None, last_event_time=None, monitor_start_time=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1FileWatchStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._file_events = None
        self._last_event_time = None
        self._monitor_start_time = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if file_events is not None:
            self.file_events = file_events
        if last_event_time is not None:
            self.last_event_time = last_event_time
        if monitor_start_time is not None:
            self.monitor_start_time = monitor_start_time

    @property
    def error(self):
        """Gets the error of this V1alpha1FileWatchStatus.  # noqa: E501

        Error is set if there is a problem with the filesystem watch. If non-empty, consumers should assume that no filesystem events will be seen and that the file watcher is in a failed state.  # noqa: E501

        :return: The error of this V1alpha1FileWatchStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1alpha1FileWatchStatus.

        Error is set if there is a problem with the filesystem watch. If non-empty, consumers should assume that no filesystem events will be seen and that the file watcher is in a failed state.  # noqa: E501

        :param error: The error of this V1alpha1FileWatchStatus.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def file_events(self):
        """Gets the file_events of this V1alpha1FileWatchStatus.  # noqa: E501

        FileEvents summarizes batches of file changes (create, modify, or delete) that have been seen in ascending chronological order. Only the most recent 20 events are included.  # noqa: E501

        :return: The file_events of this V1alpha1FileWatchStatus.  # noqa: E501
        :rtype: list[V1alpha1FileEvent]
        """
        return self._file_events

    @file_events.setter
    def file_events(self, file_events):
        """Sets the file_events of this V1alpha1FileWatchStatus.

        FileEvents summarizes batches of file changes (create, modify, or delete) that have been seen in ascending chronological order. Only the most recent 20 events are included.  # noqa: E501

        :param file_events: The file_events of this V1alpha1FileWatchStatus.  # noqa: E501
        :type: list[V1alpha1FileEvent]
        """

        self._file_events = file_events

    @property
    def last_event_time(self):
        """Gets the last_event_time of this V1alpha1FileWatchStatus.  # noqa: E501

        LastEventTime is the timestamp of the most recent file event. It is zero if no events have been seen yet.  If the specifics of which files changed are not important, this field can be used as a watermark without needing to inspect FileEvents.  # noqa: E501

        :return: The last_event_time of this V1alpha1FileWatchStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this V1alpha1FileWatchStatus.

        LastEventTime is the timestamp of the most recent file event. It is zero if no events have been seen yet.  If the specifics of which files changed are not important, this field can be used as a watermark without needing to inspect FileEvents.  # noqa: E501

        :param last_event_time: The last_event_time of this V1alpha1FileWatchStatus.  # noqa: E501
        :type: datetime
        """

        self._last_event_time = last_event_time

    @property
    def monitor_start_time(self):
        """Gets the monitor_start_time of this V1alpha1FileWatchStatus.  # noqa: E501

        MonitorStartTime is the timestamp of when filesystem monitor was started. It is zero if the monitor has not been started yet.  # noqa: E501

        :return: The monitor_start_time of this V1alpha1FileWatchStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._monitor_start_time

    @monitor_start_time.setter
    def monitor_start_time(self, monitor_start_time):
        """Sets the monitor_start_time of this V1alpha1FileWatchStatus.

        MonitorStartTime is the timestamp of when filesystem monitor was started. It is zero if the monitor has not been started yet.  # noqa: E501

        :param monitor_start_time: The monitor_start_time of this V1alpha1FileWatchStatus.  # noqa: E501
        :type: datetime
        """

        self._monitor_start_time = monitor_start_time

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
        if not isinstance(other, V1alpha1FileWatchStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1FileWatchStatus):
            return True

        return self.to_dict() != other.to_dict()
