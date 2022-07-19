# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ingest_stream_distribution_channel_details import IngestStreamDistributionChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssetMetadataEntryDetails(IngestStreamDistributionChannelDetails):
    """
    Asset Metadata entry information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssetMetadataEntryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.AssetMetadataEntryDetails.ingest_payload_type` attribute
        of this class is ``ASSET_METADATA_MEDIA_ASSET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ingest_payload_type:
            The value to assign to the ingest_payload_type property of this AssetMetadataEntryDetails.
            Allowed values for this property are: "ASSET_METADATA_MEDIA_ASSET"
        :type ingest_payload_type: str

        :param media_asset_id:
            The value to assign to the media_asset_id property of this AssetMetadataEntryDetails.
        :type media_asset_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssetMetadataEntryDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'ingest_payload_type': 'str',
            'media_asset_id': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'ingest_payload_type': 'ingestPayloadType',
            'media_asset_id': 'mediaAssetId',
            'compartment_id': 'compartmentId'
        }

        self._ingest_payload_type = None
        self._media_asset_id = None
        self._compartment_id = None
        self._ingest_payload_type = 'ASSET_METADATA_MEDIA_ASSET'

    @property
    def media_asset_id(self):
        """
        **[Required]** Gets the media_asset_id of this AssetMetadataEntryDetails.
        The Media Asset ID to ingest into the Distribution Channel.


        :return: The media_asset_id of this AssetMetadataEntryDetails.
        :rtype: str
        """
        return self._media_asset_id

    @media_asset_id.setter
    def media_asset_id(self, media_asset_id):
        """
        Sets the media_asset_id of this AssetMetadataEntryDetails.
        The Media Asset ID to ingest into the Distribution Channel.


        :param media_asset_id: The media_asset_id of this AssetMetadataEntryDetails.
        :type: str
        """
        self._media_asset_id = media_asset_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AssetMetadataEntryDetails.
        The compartment ID where the Ingest Workflow Job will be run.


        :return: The compartment_id of this AssetMetadataEntryDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssetMetadataEntryDetails.
        The compartment ID where the Ingest Workflow Job will be run.


        :param compartment_id: The compartment_id of this AssetMetadataEntryDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
