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


class V1alpha1UISessionStatus(object):
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
        'fatal_error': 'str',
        'feature_flags': 'list[V1alpha1UIFeatureFlag]',
        'needs_analytics_nudge': 'bool',
        'running_tilt_build': 'V1alpha1TiltBuild',
        'suggested_tilt_version': 'str',
        'tilt_cloud_scheme_host': 'str',
        'tilt_cloud_team_id': 'str',
        'tilt_cloud_team_name': 'str',
        'tilt_cloud_username': 'str',
        'tilt_start_time': 'datetime',
        'tiltfile_key': 'str',
        'version_settings': 'V1alpha1VersionSettings'
    }

    attribute_map = {
        'fatal_error': 'fatalError',
        'feature_flags': 'featureFlags',
        'needs_analytics_nudge': 'needsAnalyticsNudge',
        'running_tilt_build': 'runningTiltBuild',
        'suggested_tilt_version': 'suggestedTiltVersion',
        'tilt_cloud_scheme_host': 'tiltCloudSchemeHost',
        'tilt_cloud_team_id': 'tiltCloudTeamID',
        'tilt_cloud_team_name': 'tiltCloudTeamName',
        'tilt_cloud_username': 'tiltCloudUsername',
        'tilt_start_time': 'tiltStartTime',
        'tiltfile_key': 'tiltfileKey',
        'version_settings': 'versionSettings'
    }

    def __init__(self, fatal_error=None, feature_flags=None, needs_analytics_nudge=None, running_tilt_build=None, suggested_tilt_version=None, tilt_cloud_scheme_host=None, tilt_cloud_team_id=None, tilt_cloud_team_name=None, tilt_cloud_username=None, tilt_start_time=None, tiltfile_key=None, version_settings=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1UISessionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fatal_error = None
        self._feature_flags = None
        self._needs_analytics_nudge = None
        self._running_tilt_build = None
        self._suggested_tilt_version = None
        self._tilt_cloud_scheme_host = None
        self._tilt_cloud_team_id = None
        self._tilt_cloud_team_name = None
        self._tilt_cloud_username = None
        self._tilt_start_time = None
        self._tiltfile_key = None
        self._version_settings = None
        self.discriminator = None

        self.fatal_error = fatal_error
        self.feature_flags = feature_flags
        self.needs_analytics_nudge = needs_analytics_nudge
        self.running_tilt_build = running_tilt_build
        self.suggested_tilt_version = suggested_tilt_version
        self.tilt_cloud_scheme_host = tilt_cloud_scheme_host
        self.tilt_cloud_team_id = tilt_cloud_team_id
        self.tilt_cloud_team_name = tilt_cloud_team_name
        self.tilt_cloud_username = tilt_cloud_username
        self.tilt_start_time = tilt_start_time
        self.tiltfile_key = tiltfile_key
        self.version_settings = version_settings

    @property
    def fatal_error(self):
        """Gets the fatal_error of this V1alpha1UISessionStatus.  # noqa: E501

        A FatalError is an error that forces Tilt to stop its control loop. The API server will stay up and continue to serve the UI, but no further builds will happen.  # noqa: E501

        :return: The fatal_error of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._fatal_error

    @fatal_error.setter
    def fatal_error(self, fatal_error):
        """Sets the fatal_error of this V1alpha1UISessionStatus.

        A FatalError is an error that forces Tilt to stop its control loop. The API server will stay up and continue to serve the UI, but no further builds will happen.  # noqa: E501

        :param fatal_error: The fatal_error of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fatal_error is None:  # noqa: E501
            raise ValueError("Invalid value for `fatal_error`, must not be `None`")  # noqa: E501

        self._fatal_error = fatal_error

    @property
    def feature_flags(self):
        """Gets the feature_flags of this V1alpha1UISessionStatus.  # noqa: E501

        FeatureFlags reports a list of experimental features that have been enabled.  # noqa: E501

        :return: The feature_flags of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: list[V1alpha1UIFeatureFlag]
        """
        return self._feature_flags

    @feature_flags.setter
    def feature_flags(self, feature_flags):
        """Sets the feature_flags of this V1alpha1UISessionStatus.

        FeatureFlags reports a list of experimental features that have been enabled.  # noqa: E501

        :param feature_flags: The feature_flags of this V1alpha1UISessionStatus.  # noqa: E501
        :type: list[V1alpha1UIFeatureFlag]
        """
        if self.local_vars_configuration.client_side_validation and feature_flags is None:  # noqa: E501
            raise ValueError("Invalid value for `feature_flags`, must not be `None`")  # noqa: E501

        self._feature_flags = feature_flags

    @property
    def needs_analytics_nudge(self):
        """Gets the needs_analytics_nudge of this V1alpha1UISessionStatus.  # noqa: E501

        NeedsAnalyticsNudge reports whether the UI hasn't opted in or out of analytics, and the UI should nudge them to do so.  # noqa: E501

        :return: The needs_analytics_nudge of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: bool
        """
        return self._needs_analytics_nudge

    @needs_analytics_nudge.setter
    def needs_analytics_nudge(self, needs_analytics_nudge):
        """Sets the needs_analytics_nudge of this V1alpha1UISessionStatus.

        NeedsAnalyticsNudge reports whether the UI hasn't opted in or out of analytics, and the UI should nudge them to do so.  # noqa: E501

        :param needs_analytics_nudge: The needs_analytics_nudge of this V1alpha1UISessionStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and needs_analytics_nudge is None:  # noqa: E501
            raise ValueError("Invalid value for `needs_analytics_nudge`, must not be `None`")  # noqa: E501

        self._needs_analytics_nudge = needs_analytics_nudge

    @property
    def running_tilt_build(self):
        """Gets the running_tilt_build of this V1alpha1UISessionStatus.  # noqa: E501


        :return: The running_tilt_build of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: V1alpha1TiltBuild
        """
        return self._running_tilt_build

    @running_tilt_build.setter
    def running_tilt_build(self, running_tilt_build):
        """Sets the running_tilt_build of this V1alpha1UISessionStatus.


        :param running_tilt_build: The running_tilt_build of this V1alpha1UISessionStatus.  # noqa: E501
        :type: V1alpha1TiltBuild
        """
        if self.local_vars_configuration.client_side_validation and running_tilt_build is None:  # noqa: E501
            raise ValueError("Invalid value for `running_tilt_build`, must not be `None`")  # noqa: E501

        self._running_tilt_build = running_tilt_build

    @property
    def suggested_tilt_version(self):
        """Gets the suggested_tilt_version of this V1alpha1UISessionStatus.  # noqa: E501

        SuggestedTiltVersion tells the UI the recommended version for this user. If the version is different than what's running, the UI may display a prompt to upgrade.  # noqa: E501

        :return: The suggested_tilt_version of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._suggested_tilt_version

    @suggested_tilt_version.setter
    def suggested_tilt_version(self, suggested_tilt_version):
        """Sets the suggested_tilt_version of this V1alpha1UISessionStatus.

        SuggestedTiltVersion tells the UI the recommended version for this user. If the version is different than what's running, the UI may display a prompt to upgrade.  # noqa: E501

        :param suggested_tilt_version: The suggested_tilt_version of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and suggested_tilt_version is None:  # noqa: E501
            raise ValueError("Invalid value for `suggested_tilt_version`, must not be `None`")  # noqa: E501

        self._suggested_tilt_version = suggested_tilt_version

    @property
    def tilt_cloud_scheme_host(self):
        """Gets the tilt_cloud_scheme_host of this V1alpha1UISessionStatus.  # noqa: E501

        TiltCloudSchemeHost reports the base URL of the Tilt Cloud instance associated with this Tilt process. Usually https://cloud.tilt.dev  # noqa: E501

        :return: The tilt_cloud_scheme_host of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._tilt_cloud_scheme_host

    @tilt_cloud_scheme_host.setter
    def tilt_cloud_scheme_host(self, tilt_cloud_scheme_host):
        """Sets the tilt_cloud_scheme_host of this V1alpha1UISessionStatus.

        TiltCloudSchemeHost reports the base URL of the Tilt Cloud instance associated with this Tilt process. Usually https://cloud.tilt.dev  # noqa: E501

        :param tilt_cloud_scheme_host: The tilt_cloud_scheme_host of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tilt_cloud_scheme_host is None:  # noqa: E501
            raise ValueError("Invalid value for `tilt_cloud_scheme_host`, must not be `None`")  # noqa: E501

        self._tilt_cloud_scheme_host = tilt_cloud_scheme_host

    @property
    def tilt_cloud_team_id(self):
        """Gets the tilt_cloud_team_id of this V1alpha1UISessionStatus.  # noqa: E501

        TiltCloudTeamID reports the unique team id if the user is signed into TiltCloud and the Tiltfile declares a team.  # noqa: E501

        :return: The tilt_cloud_team_id of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._tilt_cloud_team_id

    @tilt_cloud_team_id.setter
    def tilt_cloud_team_id(self, tilt_cloud_team_id):
        """Sets the tilt_cloud_team_id of this V1alpha1UISessionStatus.

        TiltCloudTeamID reports the unique team id if the user is signed into TiltCloud and the Tiltfile declares a team.  # noqa: E501

        :param tilt_cloud_team_id: The tilt_cloud_team_id of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tilt_cloud_team_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tilt_cloud_team_id`, must not be `None`")  # noqa: E501

        self._tilt_cloud_team_id = tilt_cloud_team_id

    @property
    def tilt_cloud_team_name(self):
        """Gets the tilt_cloud_team_name of this V1alpha1UISessionStatus.  # noqa: E501

        TiltCloudUsername reports the human-readable team name if the user is signed into TiltCloud and the Tiltfile declares a team.  # noqa: E501

        :return: The tilt_cloud_team_name of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._tilt_cloud_team_name

    @tilt_cloud_team_name.setter
    def tilt_cloud_team_name(self, tilt_cloud_team_name):
        """Sets the tilt_cloud_team_name of this V1alpha1UISessionStatus.

        TiltCloudUsername reports the human-readable team name if the user is signed into TiltCloud and the Tiltfile declares a team.  # noqa: E501

        :param tilt_cloud_team_name: The tilt_cloud_team_name of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tilt_cloud_team_name is None:  # noqa: E501
            raise ValueError("Invalid value for `tilt_cloud_team_name`, must not be `None`")  # noqa: E501

        self._tilt_cloud_team_name = tilt_cloud_team_name

    @property
    def tilt_cloud_username(self):
        """Gets the tilt_cloud_username of this V1alpha1UISessionStatus.  # noqa: E501

        TiltCloudUsername reports the username if the user is signed into TiltCloud.  # noqa: E501

        :return: The tilt_cloud_username of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._tilt_cloud_username

    @tilt_cloud_username.setter
    def tilt_cloud_username(self, tilt_cloud_username):
        """Sets the tilt_cloud_username of this V1alpha1UISessionStatus.

        TiltCloudUsername reports the username if the user is signed into TiltCloud.  # noqa: E501

        :param tilt_cloud_username: The tilt_cloud_username of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tilt_cloud_username is None:  # noqa: E501
            raise ValueError("Invalid value for `tilt_cloud_username`, must not be `None`")  # noqa: E501

        self._tilt_cloud_username = tilt_cloud_username

    @property
    def tilt_start_time(self):
        """Gets the tilt_start_time of this V1alpha1UISessionStatus.  # noqa: E501

        The time that this instance of tilt started. Clients can use this to determine if the API server has restarted and all the objects need to be refreshed.  # noqa: E501

        :return: The tilt_start_time of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._tilt_start_time

    @tilt_start_time.setter
    def tilt_start_time(self, tilt_start_time):
        """Sets the tilt_start_time of this V1alpha1UISessionStatus.

        The time that this instance of tilt started. Clients can use this to determine if the API server has restarted and all the objects need to be refreshed.  # noqa: E501

        :param tilt_start_time: The tilt_start_time of this V1alpha1UISessionStatus.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and tilt_start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `tilt_start_time`, must not be `None`")  # noqa: E501

        self._tilt_start_time = tilt_start_time

    @property
    def tiltfile_key(self):
        """Gets the tiltfile_key of this V1alpha1UISessionStatus.  # noqa: E501

        An identifier for the Tiltfile that is running. Clients can use this to store data associated with a particular project in LocalStorage or other persistent storage.  # noqa: E501

        :return: The tiltfile_key of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: str
        """
        return self._tiltfile_key

    @tiltfile_key.setter
    def tiltfile_key(self, tiltfile_key):
        """Sets the tiltfile_key of this V1alpha1UISessionStatus.

        An identifier for the Tiltfile that is running. Clients can use this to store data associated with a particular project in LocalStorage or other persistent storage.  # noqa: E501

        :param tiltfile_key: The tiltfile_key of this V1alpha1UISessionStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tiltfile_key is None:  # noqa: E501
            raise ValueError("Invalid value for `tiltfile_key`, must not be `None`")  # noqa: E501

        self._tiltfile_key = tiltfile_key

    @property
    def version_settings(self):
        """Gets the version_settings of this V1alpha1UISessionStatus.  # noqa: E501


        :return: The version_settings of this V1alpha1UISessionStatus.  # noqa: E501
        :rtype: V1alpha1VersionSettings
        """
        return self._version_settings

    @version_settings.setter
    def version_settings(self, version_settings):
        """Sets the version_settings of this V1alpha1UISessionStatus.


        :param version_settings: The version_settings of this V1alpha1UISessionStatus.  # noqa: E501
        :type: V1alpha1VersionSettings
        """
        if self.local_vars_configuration.client_side_validation and version_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `version_settings`, must not be `None`")  # noqa: E501

        self._version_settings = version_settings

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
        if not isinstance(other, V1alpha1UISessionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1UISessionStatus):
            return True

        return self.to_dict() != other.to_dict()
