# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BitbucketCloudAppPasswordConnectionSummary(ConnectionSummary):
    """
    Summary information for a connection of the type `BITBUCKET_CLOUD_APP_PASSWORD`.
    This type corresponds to a connection in Bitbucket Cloud that is authenticated with a username and app password.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BitbucketCloudAppPasswordConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.BitbucketCloudAppPasswordConnectionSummary.connection_type` attribute
        of this class is ``BITBUCKET_CLOUD_APP_PASSWORD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BitbucketCloudAppPasswordConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BitbucketCloudAppPasswordConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this BitbucketCloudAppPasswordConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BitbucketCloudAppPasswordConnectionSummary.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this BitbucketCloudAppPasswordConnectionSummary.
        :type project_id: str

        :param connection_type:
            The value to assign to the connection_type property of this BitbucketCloudAppPasswordConnectionSummary.
        :type connection_type: str

        :param time_created:
            The value to assign to the time_created property of this BitbucketCloudAppPasswordConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BitbucketCloudAppPasswordConnectionSummary.
        :type time_updated: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BitbucketCloudAppPasswordConnectionSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BitbucketCloudAppPasswordConnectionSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BitbucketCloudAppPasswordConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BitbucketCloudAppPasswordConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BitbucketCloudAppPasswordConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param username:
            The value to assign to the username property of this BitbucketCloudAppPasswordConnectionSummary.
        :type username: str

        :param app_password:
            The value to assign to the app_password property of this BitbucketCloudAppPasswordConnectionSummary.
        :type app_password: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'connection_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'username': 'str',
            'app_password': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'connection_type': 'connectionType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'username': 'username',
            'app_password': 'appPassword'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._project_id = None
        self._connection_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._username = None
        self._app_password = None
        self._connection_type = 'BITBUCKET_CLOUD_APP_PASSWORD'

    @property
    def username(self):
        """
        **[Required]** Gets the username of this BitbucketCloudAppPasswordConnectionSummary.
        Public Bitbucket Cloud Username in plain text


        :return: The username of this BitbucketCloudAppPasswordConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this BitbucketCloudAppPasswordConnectionSummary.
        Public Bitbucket Cloud Username in plain text


        :param username: The username of this BitbucketCloudAppPasswordConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def app_password(self):
        """
        **[Required]** Gets the app_password of this BitbucketCloudAppPasswordConnectionSummary.
        OCID of personal Bitbucket Cloud AppPassword saved in secret store


        :return: The app_password of this BitbucketCloudAppPasswordConnectionSummary.
        :rtype: str
        """
        return self._app_password

    @app_password.setter
    def app_password(self, app_password):
        """
        Sets the app_password of this BitbucketCloudAppPasswordConnectionSummary.
        OCID of personal Bitbucket Cloud AppPassword saved in secret store


        :param app_password: The app_password of this BitbucketCloudAppPasswordConnectionSummary.
        :type: str
        """
        self._app_password = app_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
