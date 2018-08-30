# Copyright 2018 Red Hat, Inc.
#
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

import os_service_types

# Add your original service type here.
ADDITIONAL_SERVICE_TYPES = [
    {
        'project': 'micro-internet-gateway',
        'service_type': 'micro-internet-gateway',
        'api-reference': '',
        'aliases': ['micro_internet_gateway']
    }
]


class ServiceTypes(os_service_types.ServiceTypes):

    @property
    def services(self):
        "Full service-type data listing."
        services = super(ServiceTypes, self).services
        return services + ADDITIONAL_SERVICE_TYPES
