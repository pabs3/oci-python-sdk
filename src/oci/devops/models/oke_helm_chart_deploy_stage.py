# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage import DeployStage
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OkeHelmChartDeployStage(DeployStage):
    """
    Specifies the OKE cluster deployment stage using helm charts.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OkeHelmChartDeployStage object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.OkeHelmChartDeployStage.deploy_stage_type` attribute
        of this class is ``OKE_HELM_CHART_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OkeHelmChartDeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this OkeHelmChartDeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this OkeHelmChartDeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this OkeHelmChartDeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this OkeHelmChartDeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OkeHelmChartDeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this OkeHelmChartDeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT", "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT", "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL", "OKE_BLUE_GREEN_DEPLOYMENT", "OKE_BLUE_GREEN_TRAFFIC_SHIFT", "OKE_CANARY_DEPLOYMENT", "OKE_CANARY_TRAFFIC_SHIFT", "OKE_CANARY_APPROVAL", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", "OKE_HELM_CHART_DEPLOYMENT", "SHELL"
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this OkeHelmChartDeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OkeHelmChartDeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OkeHelmChartDeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OkeHelmChartDeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this OkeHelmChartDeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OkeHelmChartDeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OkeHelmChartDeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OkeHelmChartDeployStage.
        :type system_tags: dict(str, dict(str, object))

        :param oke_cluster_deploy_environment_id:
            The value to assign to the oke_cluster_deploy_environment_id property of this OkeHelmChartDeployStage.
        :type oke_cluster_deploy_environment_id: str

        :param helm_chart_deploy_artifact_id:
            The value to assign to the helm_chart_deploy_artifact_id property of this OkeHelmChartDeployStage.
        :type helm_chart_deploy_artifact_id: str

        :param values_artifact_ids:
            The value to assign to the values_artifact_ids property of this OkeHelmChartDeployStage.
        :type values_artifact_ids: list[str]

        :param release_name:
            The value to assign to the release_name property of this OkeHelmChartDeployStage.
        :type release_name: str

        :param namespace:
            The value to assign to the namespace property of this OkeHelmChartDeployStage.
        :type namespace: str

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this OkeHelmChartDeployStage.
        :type timeout_in_seconds: int

        :param rollback_policy:
            The value to assign to the rollback_policy property of this OkeHelmChartDeployStage.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'oke_cluster_deploy_environment_id': 'str',
            'helm_chart_deploy_artifact_id': 'str',
            'values_artifact_ids': 'list[str]',
            'release_name': 'str',
            'namespace': 'str',
            'timeout_in_seconds': 'int',
            'rollback_policy': 'DeployStageRollbackPolicy'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'oke_cluster_deploy_environment_id': 'okeClusterDeployEnvironmentId',
            'helm_chart_deploy_artifact_id': 'helmChartDeployArtifactId',
            'values_artifact_ids': 'valuesArtifactIds',
            'release_name': 'releaseName',
            'namespace': 'namespace',
            'timeout_in_seconds': 'timeoutInSeconds',
            'rollback_policy': 'rollbackPolicy'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._oke_cluster_deploy_environment_id = None
        self._helm_chart_deploy_artifact_id = None
        self._values_artifact_ids = None
        self._release_name = None
        self._namespace = None
        self._timeout_in_seconds = None
        self._rollback_policy = None
        self._deploy_stage_type = 'OKE_HELM_CHART_DEPLOYMENT'

    @property
    def oke_cluster_deploy_environment_id(self):
        """
        **[Required]** Gets the oke_cluster_deploy_environment_id of this OkeHelmChartDeployStage.
        Kubernetes cluster environment OCID for deployment.


        :return: The oke_cluster_deploy_environment_id of this OkeHelmChartDeployStage.
        :rtype: str
        """
        return self._oke_cluster_deploy_environment_id

    @oke_cluster_deploy_environment_id.setter
    def oke_cluster_deploy_environment_id(self, oke_cluster_deploy_environment_id):
        """
        Sets the oke_cluster_deploy_environment_id of this OkeHelmChartDeployStage.
        Kubernetes cluster environment OCID for deployment.


        :param oke_cluster_deploy_environment_id: The oke_cluster_deploy_environment_id of this OkeHelmChartDeployStage.
        :type: str
        """
        self._oke_cluster_deploy_environment_id = oke_cluster_deploy_environment_id

    @property
    def helm_chart_deploy_artifact_id(self):
        """
        **[Required]** Gets the helm_chart_deploy_artifact_id of this OkeHelmChartDeployStage.
        Helm chart artifact OCID.


        :return: The helm_chart_deploy_artifact_id of this OkeHelmChartDeployStage.
        :rtype: str
        """
        return self._helm_chart_deploy_artifact_id

    @helm_chart_deploy_artifact_id.setter
    def helm_chart_deploy_artifact_id(self, helm_chart_deploy_artifact_id):
        """
        Sets the helm_chart_deploy_artifact_id of this OkeHelmChartDeployStage.
        Helm chart artifact OCID.


        :param helm_chart_deploy_artifact_id: The helm_chart_deploy_artifact_id of this OkeHelmChartDeployStage.
        :type: str
        """
        self._helm_chart_deploy_artifact_id = helm_chart_deploy_artifact_id

    @property
    def values_artifact_ids(self):
        """
        Gets the values_artifact_ids of this OkeHelmChartDeployStage.
        List of values.yaml file artifact OCIDs.


        :return: The values_artifact_ids of this OkeHelmChartDeployStage.
        :rtype: list[str]
        """
        return self._values_artifact_ids

    @values_artifact_ids.setter
    def values_artifact_ids(self, values_artifact_ids):
        """
        Sets the values_artifact_ids of this OkeHelmChartDeployStage.
        List of values.yaml file artifact OCIDs.


        :param values_artifact_ids: The values_artifact_ids of this OkeHelmChartDeployStage.
        :type: list[str]
        """
        self._values_artifact_ids = values_artifact_ids

    @property
    def release_name(self):
        """
        **[Required]** Gets the release_name of this OkeHelmChartDeployStage.
        Release name of the Helm chart.


        :return: The release_name of this OkeHelmChartDeployStage.
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """
        Sets the release_name of this OkeHelmChartDeployStage.
        Release name of the Helm chart.


        :param release_name: The release_name of this OkeHelmChartDeployStage.
        :type: str
        """
        self._release_name = release_name

    @property
    def namespace(self):
        """
        Gets the namespace of this OkeHelmChartDeployStage.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :return: The namespace of this OkeHelmChartDeployStage.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OkeHelmChartDeployStage.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :param namespace: The namespace of this OkeHelmChartDeployStage.
        :type: str
        """
        self._namespace = namespace

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this OkeHelmChartDeployStage.
        Time to wait for execution of a helm stage. Defaults to 300 seconds.


        :return: The timeout_in_seconds of this OkeHelmChartDeployStage.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this OkeHelmChartDeployStage.
        Time to wait for execution of a helm stage. Defaults to 300 seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this OkeHelmChartDeployStage.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this OkeHelmChartDeployStage.

        :return: The rollback_policy of this OkeHelmChartDeployStage.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this OkeHelmChartDeployStage.

        :param rollback_policy: The rollback_policy of this OkeHelmChartDeployStage.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
