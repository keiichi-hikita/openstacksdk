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

from openstack.micro_internet_gateway import micro_internet_gateway_service
from openstack import resource


class Size(resource.Resource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "sizes"
    # resource_key = "size"

    service = micro_internet_gateway_service.\
        MicroInternetGatewayService("v1.0")

    # TODO 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/micro_internet_gateway_plans'

    # Json-Server用
    base_path = '/sizes'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_fetch = True

    # _query_mapping = resource.QueryParameters("details")
    # TBD

    # Properties
    #: It identifies connection resource uniquely.
    id = resource.Body('id')
    #: Name of virtual network appliance plan.
    name = resource.Body('name')
    #: Description of virtual network appliance plan.
    description = resource.Body('description')
    #: Flavor of virtual network appliance plan.
    flavor = resource.Body('flavor')
    #: Image ID of micro internet gateway plan
    image_id = resource.Body('image_id')
    #: Date / Time when resource was created.
    created_at = resource.Body('created_at')
    #: Date / Time when resource was updated.
    updated_at = resource.Body('updated_at')
    #: Date / Time when resource was updated.
    deleted_at = resource.Body('deleted_at')