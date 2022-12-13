# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualServiceTrafficRouteRuleDetails(object):
    """
    Rule for routing incoming virtual service traffic to a version.
    """

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRuleDetails.
    #: This constant has a value of "HTTP"
    TYPE_HTTP = "HTTP"

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRuleDetails.
    #: This constant has a value of "TLS_PASSTHROUGH"
    TYPE_TLS_PASSTHROUGH = "TLS_PASSTHROUGH"

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRuleDetails.
    #: This constant has a value of "TCP"
    TYPE_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualServiceTrafficRouteRuleDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.TcpVirtualServiceTrafficRouteRuleDetails`
        * :class:`~oci.service_mesh.models.TlsPassthroughVirtualServiceTrafficRouteRuleDetails`
        * :class:`~oci.service_mesh.models.HttpVirtualServiceTrafficRouteRuleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VirtualServiceTrafficRouteRuleDetails.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP"
        :type type: str

        :param destinations:
            The value to assign to the destinations property of this VirtualServiceTrafficRouteRuleDetails.
        :type destinations: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTargetDetails]

        """
        self.swagger_types = {
            'type': 'str',
            'destinations': 'list[VirtualDeploymentTrafficRuleTargetDetails]'
        }

        self.attribute_map = {
            'type': 'type',
            'destinations': 'destinations'
        }

        self._type = None
        self._destinations = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'TCP':
            return 'TcpVirtualServiceTrafficRouteRuleDetails'

        if type == 'TLS_PASSTHROUGH':
            return 'TlsPassthroughVirtualServiceTrafficRouteRuleDetails'

        if type == 'HTTP':
            return 'HttpVirtualServiceTrafficRouteRuleDetails'
        else:
            return 'VirtualServiceTrafficRouteRuleDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this VirtualServiceTrafficRouteRuleDetails.
        Type of protocol.

        Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP"


        :return: The type of this VirtualServiceTrafficRouteRuleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VirtualServiceTrafficRouteRuleDetails.
        Type of protocol.


        :param type: The type of this VirtualServiceTrafficRouteRuleDetails.
        :type: str
        """
        allowed_values = ["HTTP", "TLS_PASSTHROUGH", "TCP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def destinations(self):
        """
        **[Required]** Gets the destinations of this VirtualServiceTrafficRouteRuleDetails.
        The destination of the request.


        :return: The destinations of this VirtualServiceTrafficRouteRuleDetails.
        :rtype: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTargetDetails]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this VirtualServiceTrafficRouteRuleDetails.
        The destination of the request.


        :param destinations: The destinations of this VirtualServiceTrafficRouteRuleDetails.
        :type: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTargetDetails]
        """
        self._destinations = destinations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
