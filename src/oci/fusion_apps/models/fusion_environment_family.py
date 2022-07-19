# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FusionEnvironmentFamily(object):
    """
    Details of a Fusion environment family. An environment family is a logical grouping of environments. The environment family defines a set of characteristics that are shared across the environments to allow consistent management and maintenance across your production, test, and development environments. For more information, see `Planning an Environment Family`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm
    """

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironmentFamily.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FusionEnvironmentFamily object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FusionEnvironmentFamily.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FusionEnvironmentFamily.
        :type display_name: str

        :param family_maintenance_policy:
            The value to assign to the family_maintenance_policy property of this FusionEnvironmentFamily.
        :type family_maintenance_policy: oci.fusion_apps.models.FamilyMaintenancePolicy

        :param compartment_id:
            The value to assign to the compartment_id property of this FusionEnvironmentFamily.
        :type compartment_id: str

        :param subscription_ids:
            The value to assign to the subscription_ids property of this FusionEnvironmentFamily.
        :type subscription_ids: list[str]

        :param is_subscription_update_needed:
            The value to assign to the is_subscription_update_needed property of this FusionEnvironmentFamily.
        :type is_subscription_update_needed: bool

        :param time_created:
            The value to assign to the time_created property of this FusionEnvironmentFamily.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FusionEnvironmentFamily.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FusionEnvironmentFamily.
        :type lifecycle_details: str

        :param system_name:
            The value to assign to the system_name property of this FusionEnvironmentFamily.
        :type system_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FusionEnvironmentFamily.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FusionEnvironmentFamily.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'family_maintenance_policy': 'FamilyMaintenancePolicy',
            'compartment_id': 'str',
            'subscription_ids': 'list[str]',
            'is_subscription_update_needed': 'bool',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'system_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'family_maintenance_policy': 'familyMaintenancePolicy',
            'compartment_id': 'compartmentId',
            'subscription_ids': 'subscriptionIds',
            'is_subscription_update_needed': 'isSubscriptionUpdateNeeded',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'system_name': 'systemName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._family_maintenance_policy = None
        self._compartment_id = None
        self._subscription_ids = None
        self._is_subscription_update_needed = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._system_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FusionEnvironmentFamily.
        The unique identifier (OCID) of the environment family. Can't be changed after creation.


        :return: The id of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FusionEnvironmentFamily.
        The unique identifier (OCID) of the environment family. Can't be changed after creation.


        :param id: The id of this FusionEnvironmentFamily.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FusionEnvironmentFamily.
        A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.


        :return: The display_name of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FusionEnvironmentFamily.
        A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.


        :param display_name: The display_name of this FusionEnvironmentFamily.
        :type: str
        """
        self._display_name = display_name

    @property
    def family_maintenance_policy(self):
        """
        Gets the family_maintenance_policy of this FusionEnvironmentFamily.

        :return: The family_maintenance_policy of this FusionEnvironmentFamily.
        :rtype: oci.fusion_apps.models.FamilyMaintenancePolicy
        """
        return self._family_maintenance_policy

    @family_maintenance_policy.setter
    def family_maintenance_policy(self, family_maintenance_policy):
        """
        Sets the family_maintenance_policy of this FusionEnvironmentFamily.

        :param family_maintenance_policy: The family_maintenance_policy of this FusionEnvironmentFamily.
        :type: oci.fusion_apps.models.FamilyMaintenancePolicy
        """
        self._family_maintenance_policy = family_maintenance_policy

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FusionEnvironmentFamily.
        The OCID of the compartment where the environment family is located.


        :return: The compartment_id of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FusionEnvironmentFamily.
        The OCID of the compartment where the environment family is located.


        :param compartment_id: The compartment_id of this FusionEnvironmentFamily.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subscription_ids(self):
        """
        **[Required]** Gets the subscription_ids of this FusionEnvironmentFamily.
        The list of the IDs of the applications subscriptions that are associated with the environment family.


        :return: The subscription_ids of this FusionEnvironmentFamily.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this FusionEnvironmentFamily.
        The list of the IDs of the applications subscriptions that are associated with the environment family.


        :param subscription_ids: The subscription_ids of this FusionEnvironmentFamily.
        :type: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def is_subscription_update_needed(self):
        """
        Gets the is_subscription_update_needed of this FusionEnvironmentFamily.
        When set to True, a subscription update is required for the environment family.


        :return: The is_subscription_update_needed of this FusionEnvironmentFamily.
        :rtype: bool
        """
        return self._is_subscription_update_needed

    @is_subscription_update_needed.setter
    def is_subscription_update_needed(self, is_subscription_update_needed):
        """
        Sets the is_subscription_update_needed of this FusionEnvironmentFamily.
        When set to True, a subscription update is required for the environment family.


        :param is_subscription_update_needed: The is_subscription_update_needed of this FusionEnvironmentFamily.
        :type: bool
        """
        self._is_subscription_update_needed = is_subscription_update_needed

    @property
    def time_created(self):
        """
        Gets the time_created of this FusionEnvironmentFamily.
        The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.


        :return: The time_created of this FusionEnvironmentFamily.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FusionEnvironmentFamily.
        The time the the FusionEnvironmentFamily was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this FusionEnvironmentFamily.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FusionEnvironmentFamily.
        The current state of the FusionEnvironmentFamily.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FusionEnvironmentFamily.
        The current state of the FusionEnvironmentFamily.


        :param lifecycle_state: The lifecycle_state of this FusionEnvironmentFamily.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FusionEnvironmentFamily.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FusionEnvironmentFamily.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FusionEnvironmentFamily.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def system_name(self):
        """
        Gets the system_name of this FusionEnvironmentFamily.
        Environment Specific Guid/ System Name


        :return: The system_name of this FusionEnvironmentFamily.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """
        Sets the system_name of this FusionEnvironmentFamily.
        Environment Specific Guid/ System Name


        :param system_name: The system_name of this FusionEnvironmentFamily.
        :type: str
        """
        self._system_name = system_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FusionEnvironmentFamily.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FusionEnvironmentFamily.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FusionEnvironmentFamily.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FusionEnvironmentFamily.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FusionEnvironmentFamily.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FusionEnvironmentFamily.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FusionEnvironmentFamily.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FusionEnvironmentFamily.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
