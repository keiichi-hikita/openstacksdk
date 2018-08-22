# -*- coding: utf-8 -*-

import base
from openstack.micro_internet_gateway import micro_internet_gateway_service
from openstack import resource


class MicroInternetGatewayPlan(base.MicroInternetGatewayBaseResource):

    # TODO Json-server適合させるために、一時的にコメントアウト
    # resources_key = "micro_internet_gateway_plans"
    # resource_key = "micro_internet_gateway_plan"

    service = micro_internet_gateway_service.\
        MicroInternetGatewayService("v1.0")

    # TODO 最後にはこうなる↓が、まずはjson-server用にコメントアウト
    # base_path = '/' + service.version + '/micro_internet_gateway_plans'

    # Json-Server用
    base_path = '/micro_internet_gateway_plans'

    # Capabilities
    allow_list = True
    allow_get = True

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
