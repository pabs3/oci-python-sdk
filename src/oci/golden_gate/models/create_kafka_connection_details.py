# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateKafkaConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Kafka Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateKafkaConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateKafkaConnectionDetails.connection_type` attribute
        of this class is ``KAFKA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateKafkaConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateKafkaConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateKafkaConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateKafkaConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateKafkaConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateKafkaConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateKafkaConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateKafkaConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateKafkaConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateKafkaConnectionDetails.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this CreateKafkaConnectionDetails.
        :type technology_type: str

        :param stream_pool_id:
            The value to assign to the stream_pool_id property of this CreateKafkaConnectionDetails.
        :type stream_pool_id: str

        :param bootstrap_servers:
            The value to assign to the bootstrap_servers property of this CreateKafkaConnectionDetails.
        :type bootstrap_servers: list[oci.golden_gate.models.KafkaBootstrapServer]

        :param security_protocol:
            The value to assign to the security_protocol property of this CreateKafkaConnectionDetails.
        :type security_protocol: str

        :param username:
            The value to assign to the username property of this CreateKafkaConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateKafkaConnectionDetails.
        :type password: str

        :param trust_store:
            The value to assign to the trust_store property of this CreateKafkaConnectionDetails.
        :type trust_store: str

        :param trust_store_password:
            The value to assign to the trust_store_password property of this CreateKafkaConnectionDetails.
        :type trust_store_password: str

        :param key_store:
            The value to assign to the key_store property of this CreateKafkaConnectionDetails.
        :type key_store: str

        :param key_store_password:
            The value to assign to the key_store_password property of this CreateKafkaConnectionDetails.
        :type key_store_password: str

        :param ssl_key_password:
            The value to assign to the ssl_key_password property of this CreateKafkaConnectionDetails.
        :type ssl_key_password: str

        :param consumer_properties:
            The value to assign to the consumer_properties property of this CreateKafkaConnectionDetails.
        :type consumer_properties: str

        :param producer_properties:
            The value to assign to the producer_properties property of this CreateKafkaConnectionDetails.
        :type producer_properties: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'stream_pool_id': 'str',
            'bootstrap_servers': 'list[KafkaBootstrapServer]',
            'security_protocol': 'str',
            'username': 'str',
            'password': 'str',
            'trust_store': 'str',
            'trust_store_password': 'str',
            'key_store': 'str',
            'key_store_password': 'str',
            'ssl_key_password': 'str',
            'consumer_properties': 'str',
            'producer_properties': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'stream_pool_id': 'streamPoolId',
            'bootstrap_servers': 'bootstrapServers',
            'security_protocol': 'securityProtocol',
            'username': 'username',
            'password': 'password',
            'trust_store': 'trustStore',
            'trust_store_password': 'trustStorePassword',
            'key_store': 'keyStore',
            'key_store_password': 'keyStorePassword',
            'ssl_key_password': 'sslKeyPassword',
            'consumer_properties': 'consumerProperties',
            'producer_properties': 'producerProperties'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._technology_type = None
        self._stream_pool_id = None
        self._bootstrap_servers = None
        self._security_protocol = None
        self._username = None
        self._password = None
        self._trust_store = None
        self._trust_store_password = None
        self._key_store = None
        self._key_store_password = None
        self._ssl_key_password = None
        self._consumer_properties = None
        self._producer_properties = None
        self._connection_type = 'KAFKA'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateKafkaConnectionDetails.
        The Kafka technology type.


        :return: The technology_type of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateKafkaConnectionDetails.
        The Kafka technology type.


        :param technology_type: The technology_type of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def stream_pool_id(self):
        """
        Gets the stream_pool_id of this CreateKafkaConnectionDetails.
        The `OCID`__ of the stream pool being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The stream_pool_id of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._stream_pool_id

    @stream_pool_id.setter
    def stream_pool_id(self, stream_pool_id):
        """
        Sets the stream_pool_id of this CreateKafkaConnectionDetails.
        The `OCID`__ of the stream pool being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param stream_pool_id: The stream_pool_id of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._stream_pool_id = stream_pool_id

    @property
    def bootstrap_servers(self):
        """
        Gets the bootstrap_servers of this CreateKafkaConnectionDetails.
        Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
        list of KafkaBootstrapServer objects specified by host/port.
        Used for establishing the initial connection to the Kafka cluster.
        Example: `\"server1.example.com:9092,server2.example.com:9092\"`


        :return: The bootstrap_servers of this CreateKafkaConnectionDetails.
        :rtype: list[oci.golden_gate.models.KafkaBootstrapServer]
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """
        Sets the bootstrap_servers of this CreateKafkaConnectionDetails.
        Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
        list of KafkaBootstrapServer objects specified by host/port.
        Used for establishing the initial connection to the Kafka cluster.
        Example: `\"server1.example.com:9092,server2.example.com:9092\"`


        :param bootstrap_servers: The bootstrap_servers of this CreateKafkaConnectionDetails.
        :type: list[oci.golden_gate.models.KafkaBootstrapServer]
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this CreateKafkaConnectionDetails.
        Security Type for Kafka.


        :return: The security_protocol of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this CreateKafkaConnectionDetails.
        Security Type for Kafka.


        :param security_protocol: The security_protocol of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def username(self):
        """
        Gets the username of this CreateKafkaConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :return: The username of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateKafkaConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :param username: The username of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this CreateKafkaConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the
        specific security requirements implemented by the database including length, case
        sensitivity, and so on.


        :return: The password of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateKafkaConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the
        specific security requirements implemented by the database including length, case
        sensitivity, and so on.


        :param password: The password of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def trust_store(self):
        """
        Gets the trust_store of this CreateKafkaConnectionDetails.
        The base64 encoded content of the TrustStore file.


        :return: The trust_store of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._trust_store

    @trust_store.setter
    def trust_store(self, trust_store):
        """
        Sets the trust_store of this CreateKafkaConnectionDetails.
        The base64 encoded content of the TrustStore file.


        :param trust_store: The trust_store of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._trust_store = trust_store

    @property
    def trust_store_password(self):
        """
        Gets the trust_store_password of this CreateKafkaConnectionDetails.
        The TrustStore password.


        :return: The trust_store_password of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """
        Sets the trust_store_password of this CreateKafkaConnectionDetails.
        The TrustStore password.


        :param trust_store_password: The trust_store_password of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._trust_store_password = trust_store_password

    @property
    def key_store(self):
        """
        Gets the key_store of this CreateKafkaConnectionDetails.
        The base64 encoded content of the KeyStore file.


        :return: The key_store of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._key_store

    @key_store.setter
    def key_store(self, key_store):
        """
        Sets the key_store of this CreateKafkaConnectionDetails.
        The base64 encoded content of the KeyStore file.


        :param key_store: The key_store of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._key_store = key_store

    @property
    def key_store_password(self):
        """
        Gets the key_store_password of this CreateKafkaConnectionDetails.
        The KeyStore password.


        :return: The key_store_password of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """
        Sets the key_store_password of this CreateKafkaConnectionDetails.
        The KeyStore password.


        :param key_store_password: The key_store_password of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._key_store_password = key_store_password

    @property
    def ssl_key_password(self):
        """
        Gets the ssl_key_password of this CreateKafkaConnectionDetails.
        The password for the cert inside of the KeyStore.
        In case it differs from the KeyStore password, it should be provided.


        :return: The ssl_key_password of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._ssl_key_password

    @ssl_key_password.setter
    def ssl_key_password(self, ssl_key_password):
        """
        Sets the ssl_key_password of this CreateKafkaConnectionDetails.
        The password for the cert inside of the KeyStore.
        In case it differs from the KeyStore password, it should be provided.


        :param ssl_key_password: The ssl_key_password of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._ssl_key_password = ssl_key_password

    @property
    def consumer_properties(self):
        """
        Gets the consumer_properties of this CreateKafkaConnectionDetails.
        The base64 encoded content of the consumer.properties file.


        :return: The consumer_properties of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._consumer_properties

    @consumer_properties.setter
    def consumer_properties(self, consumer_properties):
        """
        Sets the consumer_properties of this CreateKafkaConnectionDetails.
        The base64 encoded content of the consumer.properties file.


        :param consumer_properties: The consumer_properties of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._consumer_properties = consumer_properties

    @property
    def producer_properties(self):
        """
        Gets the producer_properties of this CreateKafkaConnectionDetails.
        The base64 encoded content of the producer.properties file.


        :return: The producer_properties of this CreateKafkaConnectionDetails.
        :rtype: str
        """
        return self._producer_properties

    @producer_properties.setter
    def producer_properties(self, producer_properties):
        """
        Sets the producer_properties of this CreateKafkaConnectionDetails.
        The base64 encoded content of the producer.properties file.


        :param producer_properties: The producer_properties of this CreateKafkaConnectionDetails.
        :type: str
        """
        self._producer_properties = producer_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
