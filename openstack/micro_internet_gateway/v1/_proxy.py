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

from openstack import proxy

from openstack.micro_internet_gateway.v1 \
    import micro_internet_gateway as _micro_internet_gateway
from openstack.micro_internet_gateway.v1 \
    import micro_internet_gateway_plan as _micro_internet_gateway_plan
from openstack.micro_internet_gateway.v1 import operation as _operation


class Proxy(proxy.Proxy):

    def micro_internet_gateway_plans(self, **params):
        """List micro internet gateway plans.

        :param params: The parameters as query string format
            to get network appliance plans.
        :returns: A list of network appliance plans.
        :rtype: list of :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway_plan.MicroInternetGatewayPlan`
        """
        return list(self._list(
            _micro_internet_gateway_plan.MicroInternetGatewayPlan,
            paginated=False, **params))

    def get_micro_internet_gateway_plan(
            self, micro_internet_gateway_plan_id):
        """Show micro internet gateway plan.

        :param string micro_internet_gateway_plan_id:
            ID of specified micro internet gateway plan.
        :return: :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway_plan.MicroInternetGatewayPlan`
        """
        return self._get(
            _micro_internet_gateway_plan.MicroInternetGatewayPlan,
            micro_internet_gateway_plan_id)

    def micro_internet_gateways(self, **params):
        """List micro internet gateways.

        :param params: The parameters as query string format
            to get list of network appliance.
        :returns: A list of network appliance.
        :rtype: list of :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway.MicroInternetGateway`
        """
        return list(self._list(
            _micro_internet_gateway.MicroInternetGateway,
            paginated=False, **params))

    def get_micro_internet_gateway(self, micro_internet_gateway_id):
        """Show micro internet gateway.

        :param string micro_internet_gateway_id:
            ID of specified micro internet gateway.
        :return: :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway.MicroInternetGateway`
        """
        return self._get(_micro_internet_gateway.MicroInternetGateway,
                         micro_internet_gateway_id)

    def update_micro_internet_gateway(self, micro_internet_gateway,
                                      **body):
        """Update a micro internet gateway.

        :param micro_internet_gateway:
            ID of specified micro internet gateway.
        :param :attrs \*\*params: Parameters for updating
            specified micro internet gateway.
        :returns: :class:`~ecl.micro_internet_gateway.
            v1.micro_internet_gateway.MicroInternetGateway`
        """
        return self._update(_micro_internet_gateway.MicroInternetGateway,
                            micro_internet_gateway, **body)

    def find_micro_internet_gateway(self, name_or_id, ignore_missing=False):
        """Find a single micro internet gateway.

        :param name_or_id: The name or ID of a micro internet gateway.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway.MicroInternetGateway` or None
        """
        return self._find(_micro_internet_gateway.MicroInternetGateway,
                          name_or_id,
                          ignore_missing=ignore_missing)

    def delete_micro_internet_gateway(self, micro_internet_gateway_id,
                                      ignore_missing=False):
        """Delete micro internet gateway.

        :param micro_internet_gateway_id:
            The ID of a micro internet gateway.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the port does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent port.
        :returns: ``None``
        """
        self._delete(_micro_internet_gateway.MicroInternetGateway,
                     micro_internet_gateway_id,
                     ignore_missing=ignore_missing)

    def create_micro_internet_gateway(
            self,
            micro_internet_gateway_plan_id,
            interfaces,
            name=None,
            description=None,
            # default_gateway=None,
            availability_zone=None):
        """Create micro internet gateway.

        :param string micro_internet_gateway_plan_id:
            Plan ID for micro internet gateway.
        :param dict interfaces: Interface definition dictionary.
        :param string name: Name of micro internet gateway.
        :param string description: Description of micro internet gateway.
        :param string availability_zone: Availability Zone
            for micro internet gateway.
        :returns: :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway.MicroInternetGateway`
        """
        body = {}
        body["micro_internet_gateway_plan_id"] = \
            micro_internet_gateway_plan_id
        body["interfaces"] = interfaces
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        # if default_gateway:
        #     body["default_gateway"] = default_gateway
        if availability_zone:
            body["availability_zone"] = availability_zone
        return self._create(_micro_internet_gateway.MicroInternetGateway,
                            **body)

    def start_micro_internet_gateway(self, micro_internet_gateway):
        """Start the micro internet gateway.

        :param micro_internet_gateway:
            The ID of a micro internet gateway.
        :return: <Response 200>
        """
        micro_internet_gateway = \
            self.get_micro_internet_gateway(micro_internet_gateway)
        return micro_internet_gateway.start(self.session)

    def get_micro_internet_gateway_console(self,
                                           micro_internet_gateway,
                                           vnc_type):
        """Get console information for the micro internet gateway.

        :param micro_internet_gateway: Either the ID of a server or a
            :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway.MicroInternetGateway` instance.
        :param vnc_type: should be `~string "novnc"`
        :return: <Response 200>
        """
        micro_internet_gateway = \
            self.get_micro_internet_gateway(micro_internet_gateway)
        return micro_internet_gateway.get_console(self.session, vnc_type)

    def stop_micro_internet_gateway(self, micro_internet_gateway):
        """Stop the micro internet gateway.

        :param micro_internet_gateway:
            The ID of a micro internet gateway.
        :return: <Response 200>
        """
        micro_internet_gateway = \
            self.get_micro_internet_gateway(micro_internet_gateway)
        return micro_internet_gateway.stop(self.session)

    def restart_micro_internet_gateway(self, micro_internet_gateway):
        """Restart the micro internet gateway.

        :param micro_internet_gateway:
            The ID of a micro internet gateway.
        :return: <Response 200>
        """
        micro_internet_gateway = \
            self.get_micro_internet_gateway(micro_internet_gateway)
        return micro_internet_gateway.restart(self.session)

    def reset_password_micro_internet_gateway(self, micro_internet_gateway):
        """Reset the password of micro internet gateway.

        :param micro_internet_gateway:
            The ID of a micro internet gateway.
        :return: <Response 200>
        """
        micro_internet_gateway = \
            self.get_micro_internet_gateway(micro_internet_gateway)
        return micro_internet_gateway.reset_password(self.session)

    def operations(self, **params):
        """List operations.

        :param kwargs \*\*params: Optional query parameters to be sent to limit
                                  the resources being returned.

        :returns: A list of operation objects
        :rtype: list of :class:`~ecl.micro_internet_gateway.v1.
            operation.Operation`
        """
        return list(self._list(_operation.Operation,
                               paginated=False, **params))

    def get_operation(
            self, operation_id):
        """Show operation.

        :param string operation_id: ID of specified operation.
        :return: :class:`~ecl.micro_internet_gateway.v1.
            operation.Operation`
        """
        return self._get(_operation.Operation, operation_id)

    def find_micro_internet_gateway_plan(self, name_or_id,
                                         ignore_missing=False):
        """Find a single micro internet gateway plan.

        :param name_or_id: The name or ID of a micro internet gateway plan.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.micro_internet_gateway.v1.
            micro_internet_gateway_plan.MicroInternetGatewayPlan`
            or None
        """
        return self._find(
            _micro_internet_gateway_plan.MicroInternetGatewayPlan,
            name_or_id,
            ignore_missing=ignore_missing)
