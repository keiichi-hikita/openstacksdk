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

from openstack import exceptions

from openstack import resource
from openstack.micro_internet_gateway import micro_internet_gateway_service
from openstack import utils


class Configuration(resource.Resource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "configurations"
    # resource_key = "configuration"

    service = micro_internet_gateway_service. \
        MicroInternetGatewayService("v1.0")

    # 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/ecl/micro_internet_gateways'

    # Json-Server用
    base_path = '/configurations'

    # Capabilities
    allow_list = True
    # allow_get = True
    # allow_fetch = True

    _query_mapping = resource.QueryParameters('cell_id', 'type')

    # Properties
    #: It identifies connection resource uniquely.
    cell_id = resource.Body('cell_id', alternate_id=True)
    #: Name of cell
    configurations = resource.Body('configurations')

    # def fetch(self, session, requires_id=True, error_message=None):
    #     """Get a configurations based on this cell.
    #
    #     :param session: The session to use for making this request.
    #     :type session: :class:`~keystoneauth1.adapter.Adapter`
    #     :param boolean requires_id: A boolean indicating whether resource ID
    #                                 should be part of the requested URI.
    #     :return: This :class:`Resource` instance.
    #     :raises: :exc:`~openstack.exceptions.MethodNotSupported` if
    #              :data:`Resource.allow_fetch` is not set to ``True``.
    #     """
    #     # if not self.allow_fetch:
    #     #     raise exceptions.MethodNotSupported(self, "fetch")
    #
    #     request = self._prepare_request(requires_id=False)
    #
    #     request.url =
    #     session = self._get_session(session)
    #     microversion = self._get_microversion_for(session, 'fetch')
    #     response = session.get(request.url, microversion=microversion)
    #     kwargs = {}
    #
    #     if error_message:
    #         kwargs['error_message'] = error_message
    #
    #     self.microversion = microversion
    #     self._translate_response(response, **kwargs)
    #     return self
