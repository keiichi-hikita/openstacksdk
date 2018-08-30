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


class MicroInternetGatewayBaseResource(resource.Resource):

    @property
    def name_or_id(self):
        try:
            return (self._body.get('name') or
                    '(%s)' % self._body['id'][:13])
        except KeyError:
            pass

    def set_id_as_name_if_empty(self, length=8):
        try:
            if not self._body.get('name'):
                id = self._body['id']
                if length:
                    id = id[:length]
                setattr(self, 'name', '(%s)' % id)
        except KeyError:
            pass

    #: The ID of the project this resource is associated with.
    tenant_id = resource.Body('tenant_id')
