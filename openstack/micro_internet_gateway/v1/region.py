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

from openstack import resource

from openstack.micro_internet_gateway import micro_internet_gateway_service


class Region(resource.Resource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "cells"
    # resource_key = "cell"

    service = micro_internet_gateway_service. \
        MicroInternetGatewayService("v1.0")

    # 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/ecl/micro_internet_gateways'

    # Json-Server用
    base_path = '/regions'

    # Capabilities
    allow_list = True
    # allow_get = True
    # allow_fetch = True
    # allow_create = True
    # allow_update = True
    # allow_delete = True

    # _query_mapping = resource.QueryParameters()
    # TBD

    # Properties
    #: It identifies region resource uniquely.
    id = resource.Body('id')
    #: Name of region
    name = resource.Body('name')
    #: Availability of region
    available = resource.Body('available')
