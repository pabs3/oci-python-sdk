# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .ingress_gateway_traffic_route_rule_details import IngressGatewayTrafficRouteRuleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TcpIngressGatewayTrafficRouteRuleDetails(IngressGatewayTrafficRouteRuleDetails):
    """
    Rule for routing incoming ingress gateway traffic with TCP protocol.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TcpIngressGatewayTrafficRouteRuleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.TcpIngressGatewayTrafficRouteRuleDetails.type` attribute
        of this class is ``TCP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TcpIngressGatewayTrafficRouteRuleDetails.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP"
        :type type: str

        :param ingress_gateway_host:
            The value to assign to the ingress_gateway_host property of this TcpIngressGatewayTrafficRouteRuleDetails.
        :type ingress_gateway_host: oci.service_mesh.models.IngressGatewayHostRef

        :param destinations:
            The value to assign to the destinations property of this TcpIngressGatewayTrafficRouteRuleDetails.
        :type destinations: list[oci.service_mesh.models.VirtualServiceTrafficRuleTargetDetails]

        """
        self.swagger_types = {
            'type': 'str',
            'ingress_gateway_host': 'IngressGatewayHostRef',
            'destinations': 'list[VirtualServiceTrafficRuleTargetDetails]'
        }

        self.attribute_map = {
            'type': 'type',
            'ingress_gateway_host': 'ingressGatewayHost',
            'destinations': 'destinations'
        }

        self._type = None
        self._ingress_gateway_host = None
        self._destinations = None
        self._type = 'TCP'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
