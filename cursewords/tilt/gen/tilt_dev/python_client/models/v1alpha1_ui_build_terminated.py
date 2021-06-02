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


class V1alpha1UIBuildTerminated(object):
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
        'is_crash_rebuild': 'bool',
        'span_id': 'str',
        'start_time': 'datetime',
        'warnings': 'list[str]'
    }

    attribute_map = {
        'error': 'error',
        'finish_time': 'finishTime',
        'is_crash_rebuild': 'isCrashRebuild',
        'span_id': 'spanID',
        'start_time': 'startTime',
        'warnings': 'warnings'
    }

    def __init__(self, error=None, finish_time=None, is_crash_rebuild=None, span_id=None, start_time=None, warnings=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1UIBuildTerminated - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._finish_time = None
        self._is_crash_rebuild = None
        self._span_id = None
        self._start_time = None
        self._warnings = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if finish_time is not None:
            self.finish_time = finish_time
        if is_crash_rebuild is not None:
            self.is_crash_rebuild = is_crash_rebuild
        if span_id is not None:
            self.span_id = span_id
        if start_time is not None:
            self.start_time = start_time
        if warnings is not None:
            self.warnings = warnings

    @property
    def error(self):
        """Gets the error of this V1alpha1UIBuildTerminated.  # noqa: E501

        A non-empty string if the build failed with an error.  # noqa: E501

        :return: The error of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V1alpha1UIBuildTerminated.

        A non-empty string if the build failed with an error.  # noqa: E501

        :param error: The error of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def finish_time(self):
        """Gets the finish_time of this V1alpha1UIBuildTerminated.  # noqa: E501

        The time when the build finished.  # noqa: E501

        :return: The finish_time of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this V1alpha1UIBuildTerminated.

        The time when the build finished.  # noqa: E501

        :param finish_time: The finish_time of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: datetime
        """

        self._finish_time = finish_time

    @property
    def is_crash_rebuild(self):
        """Gets the is_crash_rebuild of this V1alpha1UIBuildTerminated.  # noqa: E501

        A crash rebuild happens when Tilt live-updated a container, then the pod crashed, wiping out the live-updates. Tilt does a full build+deploy to reset the pod state to what's on disk.  # noqa: E501

        :return: The is_crash_rebuild of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: bool
        """
        return self._is_crash_rebuild

    @is_crash_rebuild.setter
    def is_crash_rebuild(self, is_crash_rebuild):
        """Sets the is_crash_rebuild of this V1alpha1UIBuildTerminated.

        A crash rebuild happens when Tilt live-updated a container, then the pod crashed, wiping out the live-updates. Tilt does a full build+deploy to reset the pod state to what's on disk.  # noqa: E501

        :param is_crash_rebuild: The is_crash_rebuild of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: bool
        """

        self._is_crash_rebuild = is_crash_rebuild

    @property
    def span_id(self):
        """Gets the span_id of this V1alpha1UIBuildTerminated.  # noqa: E501

        The log span where the build logs are stored in the logstore.  # noqa: E501

        :return: The span_id of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        """Sets the span_id of this V1alpha1UIBuildTerminated.

        The log span where the build logs are stored in the logstore.  # noqa: E501

        :param span_id: The span_id of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: str
        """

        self._span_id = span_id

    @property
    def start_time(self):
        """Gets the start_time of this V1alpha1UIBuildTerminated.  # noqa: E501

        The time when the build started.  # noqa: E501

        :return: The start_time of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1alpha1UIBuildTerminated.

        The time when the build started.  # noqa: E501

        :param start_time: The start_time of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def warnings(self):
        """Gets the warnings of this V1alpha1UIBuildTerminated.  # noqa: E501

        A list of warnings encountered while running the build. These warnings will also be printed to the build's log.  # noqa: E501

        :return: The warnings of this V1alpha1UIBuildTerminated.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this V1alpha1UIBuildTerminated.

        A list of warnings encountered while running the build. These warnings will also be printed to the build's log.  # noqa: E501

        :param warnings: The warnings of this V1alpha1UIBuildTerminated.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

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
        if not isinstance(other, V1alpha1UIBuildTerminated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1UIBuildTerminated):
            return True

        return self.to_dict() != other.to_dict()