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


class V1alpha1Pod(object):
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
        'ancestor_uid': 'str',
        'baseline_restart_count': 'int',
        'conditions': 'list[V1alpha1PodCondition]',
        'containers': 'list[V1alpha1Container]',
        'created_at': 'datetime',
        'deleting': 'bool',
        'errors': 'list[str]',
        'init_containers': 'list[V1alpha1Container]',
        'name': 'str',
        'namespace': 'str',
        'phase': 'str',
        'pod_template_spec_hash': 'str',
        'status': 'str',
        'uid': 'str',
        'update_started_at': 'datetime'
    }

    attribute_map = {
        'ancestor_uid': 'ancestorUID',
        'baseline_restart_count': 'baselineRestartCount',
        'conditions': 'conditions',
        'containers': 'containers',
        'created_at': 'createdAt',
        'deleting': 'deleting',
        'errors': 'errors',
        'init_containers': 'initContainers',
        'name': 'name',
        'namespace': 'namespace',
        'phase': 'phase',
        'pod_template_spec_hash': 'podTemplateSpecHash',
        'status': 'status',
        'uid': 'uid',
        'update_started_at': 'updateStartedAt'
    }

    def __init__(self, ancestor_uid=None, baseline_restart_count=None, conditions=None, containers=None, created_at=None, deleting=None, errors=None, init_containers=None, name=None, namespace=None, phase=None, pod_template_spec_hash=None, status=None, uid=None, update_started_at=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Pod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ancestor_uid = None
        self._baseline_restart_count = None
        self._conditions = None
        self._containers = None
        self._created_at = None
        self._deleting = None
        self._errors = None
        self._init_containers = None
        self._name = None
        self._namespace = None
        self._phase = None
        self._pod_template_spec_hash = None
        self._status = None
        self._uid = None
        self._update_started_at = None
        self.discriminator = None

        if ancestor_uid is not None:
            self.ancestor_uid = ancestor_uid
        self.baseline_restart_count = baseline_restart_count
        if conditions is not None:
            self.conditions = conditions
        self.containers = containers
        self.created_at = created_at
        self.deleting = deleting
        self.errors = errors
        if init_containers is not None:
            self.init_containers = init_containers
        self.name = name
        self.namespace = namespace
        self.phase = phase
        if pod_template_spec_hash is not None:
            self.pod_template_spec_hash = pod_template_spec_hash
        self.status = status
        self.uid = uid
        if update_started_at is not None:
            self.update_started_at = update_started_at

    @property
    def ancestor_uid(self):
        """Gets the ancestor_uid of this V1alpha1Pod.  # noqa: E501

        AncestorUID is the UID from the WatchRef that matched this Pod.  If the Pod matched based on extra label selectors, this will be empty.  # noqa: E501

        :return: The ancestor_uid of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._ancestor_uid

    @ancestor_uid.setter
    def ancestor_uid(self, ancestor_uid):
        """Sets the ancestor_uid of this V1alpha1Pod.

        AncestorUID is the UID from the WatchRef that matched this Pod.  If the Pod matched based on extra label selectors, this will be empty.  # noqa: E501

        :param ancestor_uid: The ancestor_uid of this V1alpha1Pod.  # noqa: E501
        :type: str
        """

        self._ancestor_uid = ancestor_uid

    @property
    def baseline_restart_count(self):
        """Gets the baseline_restart_count of this V1alpha1Pod.  # noqa: E501

        BaselineRestartCount is the number of restarts across all containers before Tilt started observing the Pod.  This is used to ignore restarts for a Pod that was already executing before the Tilt daemon started.  # noqa: E501

        :return: The baseline_restart_count of this V1alpha1Pod.  # noqa: E501
        :rtype: int
        """
        return self._baseline_restart_count

    @baseline_restart_count.setter
    def baseline_restart_count(self, baseline_restart_count):
        """Sets the baseline_restart_count of this V1alpha1Pod.

        BaselineRestartCount is the number of restarts across all containers before Tilt started observing the Pod.  This is used to ignore restarts for a Pod that was already executing before the Tilt daemon started.  # noqa: E501

        :param baseline_restart_count: The baseline_restart_count of this V1alpha1Pod.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and baseline_restart_count is None:  # noqa: E501
            raise ValueError("Invalid value for `baseline_restart_count`, must not be `None`")  # noqa: E501

        self._baseline_restart_count = baseline_restart_count

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1Pod.  # noqa: E501

        Conditions are various lifecycle conditions for this Pod.  See also v1.PodCondition in the Kubernetes API.  # noqa: E501

        :return: The conditions of this V1alpha1Pod.  # noqa: E501
        :rtype: list[V1alpha1PodCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1Pod.

        Conditions are various lifecycle conditions for this Pod.  See also v1.PodCondition in the Kubernetes API.  # noqa: E501

        :param conditions: The conditions of this V1alpha1Pod.  # noqa: E501
        :type: list[V1alpha1PodCondition]
        """

        self._conditions = conditions

    @property
    def containers(self):
        """Gets the containers of this V1alpha1Pod.  # noqa: E501

        Containers are the containers belonging to the Pod.  # noqa: E501

        :return: The containers of this V1alpha1Pod.  # noqa: E501
        :rtype: list[V1alpha1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this V1alpha1Pod.

        Containers are the containers belonging to the Pod.  # noqa: E501

        :param containers: The containers of this V1alpha1Pod.  # noqa: E501
        :type: list[V1alpha1Container]
        """
        if self.local_vars_configuration.client_side_validation and containers is None:  # noqa: E501
            raise ValueError("Invalid value for `containers`, must not be `None`")  # noqa: E501

        self._containers = containers

    @property
    def created_at(self):
        """Gets the created_at of this V1alpha1Pod.  # noqa: E501

        CreatedAt is when the Pod was created.  # noqa: E501

        :return: The created_at of this V1alpha1Pod.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1alpha1Pod.

        CreatedAt is when the Pod was created.  # noqa: E501

        :param created_at: The created_at of this V1alpha1Pod.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def deleting(self):
        """Gets the deleting of this V1alpha1Pod.  # noqa: E501

        Deleting indicates that the Pod is in the process of being removed.  # noqa: E501

        :return: The deleting of this V1alpha1Pod.  # noqa: E501
        :rtype: bool
        """
        return self._deleting

    @deleting.setter
    def deleting(self, deleting):
        """Sets the deleting of this V1alpha1Pod.

        Deleting indicates that the Pod is in the process of being removed.  # noqa: E501

        :param deleting: The deleting of this V1alpha1Pod.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and deleting is None:  # noqa: E501
            raise ValueError("Invalid value for `deleting`, must not be `None`")  # noqa: E501

        self._deleting = deleting

    @property
    def errors(self):
        """Gets the errors of this V1alpha1Pod.  # noqa: E501

        Errors are aggregated error messages for the Pod and its containers.  # noqa: E501

        :return: The errors of this V1alpha1Pod.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this V1alpha1Pod.

        Errors are aggregated error messages for the Pod and its containers.  # noqa: E501

        :param errors: The errors of this V1alpha1Pod.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def init_containers(self):
        """Gets the init_containers of this V1alpha1Pod.  # noqa: E501

        InitContainers are containers executed prior to the Pod containers being executed.  # noqa: E501

        :return: The init_containers of this V1alpha1Pod.  # noqa: E501
        :rtype: list[V1alpha1Container]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """Sets the init_containers of this V1alpha1Pod.

        InitContainers are containers executed prior to the Pod containers being executed.  # noqa: E501

        :param init_containers: The init_containers of this V1alpha1Pod.  # noqa: E501
        :type: list[V1alpha1Container]
        """

        self._init_containers = init_containers

    @property
    def name(self):
        """Gets the name of this V1alpha1Pod.  # noqa: E501

        Name is the Pod name within the K8s cluster.  # noqa: E501

        :return: The name of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Pod.

        Name is the Pod name within the K8s cluster.  # noqa: E501

        :param name: The name of this V1alpha1Pod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1Pod.  # noqa: E501

        Namespace is the Pod namespace within the K8s cluster.  # noqa: E501

        :return: The namespace of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1Pod.

        Namespace is the Pod namespace within the K8s cluster.  # noqa: E501

        :param namespace: The namespace of this V1alpha1Pod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def phase(self):
        """Gets the phase of this V1alpha1Pod.  # noqa: E501

        Phase is where the Pod is at in its current lifecycle.  Valid values for this are v1.PodPhase values from the Kubernetes API.  # noqa: E501

        :return: The phase of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1alpha1Pod.

        Phase is where the Pod is at in its current lifecycle.  Valid values for this are v1.PodPhase values from the Kubernetes API.  # noqa: E501

        :param phase: The phase of this V1alpha1Pod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phase is None:  # noqa: E501
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def pod_template_spec_hash(self):
        """Gets the pod_template_spec_hash of this V1alpha1Pod.  # noqa: E501

        PodTemplateSpecHash is a hash of the Pod template spec.  Tilt uses this to associate Pods with the build that triggered them.  # noqa: E501

        :return: The pod_template_spec_hash of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._pod_template_spec_hash

    @pod_template_spec_hash.setter
    def pod_template_spec_hash(self, pod_template_spec_hash):
        """Sets the pod_template_spec_hash of this V1alpha1Pod.

        PodTemplateSpecHash is a hash of the Pod template spec.  Tilt uses this to associate Pods with the build that triggered them.  # noqa: E501

        :param pod_template_spec_hash: The pod_template_spec_hash of this V1alpha1Pod.  # noqa: E501
        :type: str
        """

        self._pod_template_spec_hash = pod_template_spec_hash

    @property
    def status(self):
        """Gets the status of this V1alpha1Pod.  # noqa: E501

        Status is a concise description for the Pod's current state.  This is based off the status output from `kubectl get pod` and is not an \"enum-like\" value.  # noqa: E501

        :return: The status of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1Pod.

        Status is a concise description for the Pod's current state.  This is based off the status output from `kubectl get pod` and is not an \"enum-like\" value.  # noqa: E501

        :param status: The status of this V1alpha1Pod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this V1alpha1Pod.  # noqa: E501

        UID is the unique Pod UID within the K8s cluster.  # noqa: E501

        :return: The uid of this V1alpha1Pod.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1alpha1Pod.

        UID is the unique Pod UID within the K8s cluster.  # noqa: E501

        :param uid: The uid of this V1alpha1Pod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def update_started_at(self):
        """Gets the update_started_at of this V1alpha1Pod.  # noqa: E501

        UpdateStartedAt is when Tilt started a deployment update for this Pod.  # noqa: E501

        :return: The update_started_at of this V1alpha1Pod.  # noqa: E501
        :rtype: datetime
        """
        return self._update_started_at

    @update_started_at.setter
    def update_started_at(self, update_started_at):
        """Sets the update_started_at of this V1alpha1Pod.

        UpdateStartedAt is when Tilt started a deployment update for this Pod.  # noqa: E501

        :param update_started_at: The update_started_at of this V1alpha1Pod.  # noqa: E501
        :type: datetime
        """

        self._update_started_at = update_started_at

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
        if not isinstance(other, V1alpha1Pod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Pod):
            return True

        return self.to_dict() != other.to_dict()
