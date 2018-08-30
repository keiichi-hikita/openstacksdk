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


class FirewallConfiguration(resource.Resource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "sizes"
    # resource_key = "size"

    service = micro_internet_gateway_service.\
        MicroInternetGatewayService("v1.0")

    # TODO 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/micro_internet_gateway_plans'

    # Json-Server用
    base_path = '/firewall_configurations'

    # Capabilities
    allow_list = True
    allow_get = True
    allow_fetch = True

    # _query_mapping = resource.QueryParameters("details")
    # TBD

    # Properties

    #: It identifies connection resource uniquely.
    id = resource.Body('id')

    #: Description of firewall configuration.
    description = resource.Body('description')

    #: Priority of firewall configuration.
    priority = resource.Body('priority')

    #: Direction(ingress/egress) of firewall configuration.
    direction = resource.Body('direction')

    #: Source IP address of firewall configuration.
    source_ip = resource.Body('source_ip')

    #: Destination IP address of firewall configuration.
    destination_ip = resource.Body('destination_ip')

    #: Application Filter of firewall configuration.(Impl later)
    application_filter = resource.Body('application_filter')

    #: Protocol / Port of firewall configuration.
    protocol_port = resource.Body('protocol_port')

    #: Log enable settings for configuration.
    log = resource.Body('log')

    #: IDS/IPS settings for configuration.
    ids_ips = resource.Body('ids_ips')

    #: Anti-Virus settings for configuration.
    anti_virus = resource.Body('anti_virus')

    #: Anti-Spyware settings for configuration.
    anti_spyware = resource.Body('anti_spyware')

    #: URL filtering for configuration.
    url_filtering = resource.Body('url_filtering')

    #: Rule enable/disable settings for configuration.
    enabled = resource.Body('enabled')
