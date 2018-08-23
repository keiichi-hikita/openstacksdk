# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import base

from openstack import resource
from openstack.micro_internet_gateway import micro_internet_gateway_service
from openstack import utils


class Cell(base.MicroInternetGatewayBaseResource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "cells"
    # resource_key = "cell"

    service = micro_internet_gateway_service. \
        MicroInternetGatewayService("v1.0")

    # 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/ecl/micro_internet_gateways'

    # Json-Server用
    base_path = '/cells'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_fetch = True
    allow_create = True
    allow_update = True
    allow_delete = True

    # _query_mapping = resource.QueryParameters()
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource.Body('id')
    #: Name of cell
    name = resource.Body('name')
    #: Description of cell
    description = resource.Body('description')
    #: Status of cell
    status = resource.Body('status')
    #: Utilization of cell
    utilization = resource.Body('utilization')
    #: Region of cell
    region_id = resource.Body('region_id')
    #: Firewall policy type of cell
    firewall_policy_type_id = resource.Body('firewall_policy_type_id')
    #: Alert e-mail address for cell.
    alert_email = resource.Body('alert_email')
    #: Plan ID of cell
    size_id = resource.Body('size_id')
    #: VPN N Number of cell
    n_number = resource.Body('n_number')
    #: VPN V Number of cell
    v_number = resource.Body('v_number')
    #: vThunder connectivity address
    vthunder_connectivity_cidr = resource.Body('vthunder_connectivity_cidr')
    #: Date / Time when resource was created.
    created_at = resource.Body('created_at')
    #: Date / Time when resource was updated.
    updated_at = resource.Body('updated_at')
    #: Date / Time when resource was updated.
    deleted_at = resource.Body('deleted_at')

    # ---temporally implemented---
    # def _configurations(self, session, config_type=None):
    #     """Preform getting configurations of specified cell"""
    #     url = utils.urljoin(Cell.base_path,
    #                         self.id,
    #                         'configurations?type=%s' % config_type)
    #     return session.get(url, endpoint_filter=self.service)
    #
    # def firewall_configurations(self, session):
    #     return self._configurations(session, 'firewall')
    #
    # def gslb_configurations(self, session):
    #     return self._configurations(session, 'gslb')
    #

    # def _action(self, session, body, postfix='action'):
    #     """Preform virtual network appliance actions given the message body"""
    #     url = utils.urljoin(Cell.base_path,
    #                         self.id, postfix)
    #     headers = {'Accept': ''}
    #     return session.post(
    #         url, endpoint_filter=self.service, json=body, headers=headers)
    #
    # def start(self, session):
    #     """Start virtual network appliance"""
    #     body = {"os-start": None}
    #     return self._action(session, body)
    #
    # def stop(self, session):
    #     """Stop virtual network appliance"""
    #     body = {"os-stop": None}
    #     return self._action(session, body)
    #
    # def restart(self, session):
    #     """Restart virtual network appliance"""
    #     body = {'os-restart': None}
    #     self._action(session, body)
    #
    # def reset_password(self, session):
    #     """Reset virtual network appliance password."""
    #     body = {}
    #     resp = self._action(session, body, postfix='reset-password')
    #     self._translate_response(resp, has_body=True)
    #     return self
