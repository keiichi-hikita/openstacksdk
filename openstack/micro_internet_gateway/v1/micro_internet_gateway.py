# -*- coding: utf-8 -*-

import base

from openstack import resource
from openstack.micro_internet_gateway import micro_internet_gateway_service
from openstack import utils


class MicroInternetGateway(base.MicroInternetGatewayBaseResource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "micro_internet_gateways"
    # resource_key = "micro_internet_gateway"

    service = micro_internet_gateway_service. \
        MicroInternetGatewayService("v1.0")

    # 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/ecl/micro_internet_gateways'

    # Json-Server用
    base_path = '/micro_internet_gateways'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # _query_mapping = resource.QueryParameters()
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource.Body('id')
    #: Name of micro internet gateway
    name = resource.Body('name')
    #: Description of micro internet gateway
    description = resource.Body('description')
    #: Description of micro internet gateway
    instance_id = resource.Body('instance_id')
    #: Status of micro internet gateway
    status = resource.Body('status')
    #: Zone of micro internet gateway
    availability_zone = resource.Body('availability_zone')
    user_id = resource.Body('user_id')
    #: Password of micro internet gateway.
    password = resource.Body('password')
    #: Password(after reset) of micro internet gateway.
    #: Plan ID of micro internet gateway
    micro_internet_gateway_plan_id = \
        resource.Body('micro_internet_gateway_plan_id')
    #: Date / Time when resource was created.
    created_at = resource.Body('created_at')
    #: Date / Time when resource was updated.
    updated_at = resource.Body('updated_at')
    #: Date / Time when resource was updated.
    deleted_at = resource.Body('deleted_at')
    #: Interface information f internet gateway
    interfaces = resource.Body('interfaces')

    def _action(self, session, body, postfix='action'):
        """Preform virtual network appliance actions given the message body"""
        url = utils.urljoin(MicroInternetGateway.base_path,
                            self.id, postfix)
        headers = {'Accept': ''}
        return session.post(
            url, endpoint_filter=self.service, json=body, headers=headers)

    def start(self, session):
        """Start virtual network appliance"""
        body = {"os-start": None}
        return self._action(session, body)

    def stop(self, session):
        """Stop virtual network appliance"""
        body = {"os-stop": None}
        return self._action(session, body)

    def restart(self, session):
        """Restart virtual network appliance"""
        body = {'os-restart': None}
        self._action(session, body)

    def reset_password(self, session):
        """Reset virtual network appliance password."""
        body = {}
        resp = self._action(session, body, postfix='reset-password')
        self._translate_response(resp, has_body=True)
        return self
