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

from openstack.micro_internet_gateway.v1 import cell as _cell
from openstack.micro_internet_gateway.v1 import configuration as _config
from openstack.micro_internet_gateway.v1 \
    import firewall_policy_types as _firewall_policy_type
from openstack.micro_internet_gateway.v1 \
    import firewall_configuration as _firewall_configuration
from openstack.micro_internet_gateway.v1 import size as _size
from openstack.micro_internet_gateway.v1 import region as _region


class Proxy(proxy.Proxy):

    def create_firewall_configuration(self,
                                      source_ip,
                                      destination_ip,
                                      ids_ips,
                                      anti_virus,
                                      anti_spyware,
                                      enabled=False,
                                      description="",
                                      priority=0,
                                      application_filter="",
                                      log=False,
                                      url_filtering="",
                                      protocol_port="",
                                      protocol_port_pattern=""):
        """Create Firewall Configuration.

        :param string source_ip: Source ip address for configuration.
        :param string destination_ip: 
            Destination ip address for configuration.
        :param string ids_ips: IDS/IPS settings for configuration.
        :param string anti_virus: Anti-Virus settings for configuration.
        :param string anti_spyware: Anti-Spyware settings for configuration.
        :param string enabled: Rule enable/disable settings for configuration.
        :param string description: Description for configuration.
        :param string priority: Priority for configuration.
        :param string application_filter: Application filter for configuration.
        :param string log: Log enable/disable settings for configuration.
        :param string url_filtering: URL filtering settings for configuration.
        :param string protocol_port: Allowed protocol/port for configuration.
        :param string protocol_port_pattern: 
            Settings if permit all traffic or use protocol/port pattern.
        :returns:
            :class:`~openstack.micro_internet_gateway.v1.
            firewall_configuration.FirewallConfiguration`
        """
        body = {}

        # required params
        body["source_ip"] = source_ip
        body["destination_ip"] = destination_ip
        body["ids_ips"] = ids_ips
        body["anti_virus"] = anti_virus
        body["anti_spyware"] = anti_spyware

        body["description"] = description
        body["priority"] = priority
        body["application_filter"] = application_filter
        body["log"] = log if log else False
        body["url_filtering"] = url_filtering
        body["enabled"] = True if enabled else False

        if protocol_port_pattern == "any":
            body["protocol_port"] = None
        else:
            body["protocol_port"] = protocol_port

        return self._create(_firewall_configuration.FirewallConfiguration, 
                            **body)

    def delete_firewall_configuration(self, config_id, ignore_missing=False):
        """Delete firewall configuration.

        :param cell_id:
            The ID of a firewall configuration.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the port does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent port.
        :returns: ``None``
        """
        self._delete(_firewall_configuration.FirewallConfiguration,
                     config_id, ignore_missing=ignore_missing)

    def firewall_configurations(self, **params):
        """List firewall configurations

        :param params: 
            The parameters as query string format 
            to get firewall configurations.
        :returns: A list of firewall configurations.
        :rtype: list of
            :class:`~openstack.micro_internet_gateway.v1.
                   firewall_configuration.FirewallConfiguration`
        """
        return list(self._list(_firewall_configuration.FirewallConfiguration, 
                               paginated=False, **params))

    def get_firewall_configuration(self, firewall_configuration):
        """Show firewall configuration.

        :param size: The value can be the ID of a firewall configuration or a
                     :class:`~openstack.micro_internet_gateway.v1.
                     firewall_configuration.FirewallConfiguration`
        :return: :class:`~openstack.micro_internet_gateway.v1.
                     firewall_configuration.FirewallConfiguration`
        """
        return self._get(_firewall_configuration.FirewallConfiguration, 
                         firewall_configuration)

    def regions(self, **params):
        """List regions

        :param params: The parameters as query string format to get region.
        :returns: A list of regions.
        :rtype: list of
            :class:`~openstack.micro_internet_gateway.v1.region.Region`
        """
        return list(self._list(_region.Region, paginated=False, **params))

    def firewall_policy_types(self, **params):
        """List firewall policy types

        :param params: 
            The parameters as query string format 
            to get firewall policy types.
        :returns: A list of firewall policy types.
        :rtype: list of
            :class:`~openstack.micro_internet_gateway.v1.size.Size`
        """
        return list(self._list(_firewall_policy_type.FirewallPoicyTypes,
                    paginated=False, **params))

    def sizes(self, **params):
        """List sizes

        :param params: The parameters as query string format to get size.
        :returns: A list of sizes.
        :rtype: list of
            :class:`~openstack.micro_internet_gateway.v1.size.Size`
        """
        return list(self._list(_size.Size, paginated=False, **params))

    def get_size(self, size):
        """Show size.

        :param size: The value can be the ID of a size or a
                     :class:`~openstack.micro_internet_gateway.v1.size.Size`
        :return: :class:`~openstack.micro_internet_gateway.v1.size.Size`
        """
        return self._get(_size.Size, size)

    def find_size(self, name_or_id, ignore_missing=False):
        """Find a size.

        :param name_or_id: The name or ID of a size.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.micro_internet_gateway.v1.
            cell_plan.Size`
            or None
        """
        return self._find(_size.Size, name_or_id,
                          ignore_missing=ignore_missing)

    def cells(self, **params):
        """List cells.

        :param params: The parameters as query string format
            to get list of cells.
        :returns: A list of cells.
        :rtype: list of :class:`~openstack.micro_internet_gateway.v1.
            cell.Cell`
        """
        return list(self._list(_cell.Cell, paginated=False, **params))

    def get_cell(self, cell):
        """Show cell.

        :param size: The value can be the ID of a cell or a
                     :class:`~openstack.micro_internet_gateway.v1.cell.Cell`
        :return: :class:`~openstack.micro_internet_gateway.v1.cell.Cell`
        """
        return self._get(_cell.Cell, cell)

    # def update_cell(self, cell, **body):
    #     """Update a cell.

    #     :param cell: ID of specified cell.
    #     :param :attrs \*\*params: Parameters for updating specified cell.
    #     :returns: :class:`~ecl.cell.v1.cell.Cell`
    #     """
    #     return self._update(_cell.Cell, cell, **body)

    def find_cell(self, name_or_id, ignore_missing=False):
        """Find a single cell.

        :param name_or_id: The name or ID of a cell.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.micro_internet_gateway.v1.
            cell.Cell` or None
        """
        return self._find(_cell.Cell, name_or_id,
                          ignore_missing=ignore_missing)

    def delete_cell(self, cell_id, ignore_missing=False):
        """Delete cell.

        :param cell_id:
            The ID of a micro internet gateway.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the port does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent port.
        :returns: ``None``
        """
        self._delete(_cell.Cell, cell_id, ignore_missing=ignore_missing)

    def create_cell(self,
                    name,
                    size_id,
                    firewall_policy_type_id,
                    n_number,
                    v_number,
                    api_key,
                    vthunder_connectivity_cidr,
                    description=None,
                    region_id=None,
                    alert_email=None):
        """Create Cell.

        :param string name: Name for cell.
        :param string size: Size for cell.
        :param string firewall_policy_type_id: Firewall policy type for cell.
        :param string n_number: UNO contract N Number.
        :param string v_number: UNO contract V Number.
        :param string api_key: API key.
        :param string vthunder_connectivity_cidr:
            CIDR for VPN connection segments.
        :param string description: Description for cell.
        :param string region: Region for cell.
        :param string alert_email: Alert e-mail address for cell.
        :returns: :class:`~openstack.micro_internet_gateway.v1.cell.Cell`
        """
        body = {}

        # required params
        body["name"] = name
        body["size_id"] = size_id
        body["firewall_policy_type_id"] = firewall_policy_type_id
        body["n_number"] = n_number
        body["v_number"] = v_number
        body["api_key"] = api_key
        body["vthunder_connectivity_cidr"] = vthunder_connectivity_cidr

        if description:
            body["description"] = description
        if region_id:
            body["region_id"] = region_id
        if alert_email:
            body["alert_email"] = alert_email

        return self._create(_cell.Cell, **body)

    def configurations(self, **params):
        """Show configuration.

        :param cell: The value can be the ID of a size or a
                     :class:`~openstack.micro_internet_gateway.v1.cell.Cell`
        :param params:
            The parameters as query string format to get configuration.
        :return:
            :class:`~openstack.micro_internet_gateway.v1._config.Configuration`
        """
        return list(self._list(_config.Configuration,
                               paginated=False, **params))[0]

    def activate_cell(self, cell):
        """Activate specified cell.

        :param cell: The ID of Cell.
        :return: <Response 200>
        """
        cell = self.get_cell(cell)
        return cell.activate(self.session)

    # def get_cell_console(self,
    #                                        cell,
    #                                        vnc_type):
    #     """Get console information for the micro internet gateway.
    #
    #     :param cell: Either the ID of a server or a
    #         :class:`~openstack.micro_internet_gateway.v1.
    #         cell.MicroInternetGateway` instance.
    #     :param vnc_type: should be `~string "novnc"`
    #     :return: <Response 200>
    #     """
    #     cell = \
    #         self.get_cell(cell)
    #     return cell.get_console(self.session, vnc_type)
    #    # def restart_cell(self, cell):
    #     """Restart the micro internet gateway.
    #
    #     :param cell:
    #         The ID of a micro internet gateway.
    #     :return: <Response 200>
    #     """
    #     cell = \
    #         self.get_cell(cell)
    #     return cell.restart(self.session)
    #
    # def reset_password_cell(self, cell):
    #     """Reset the password of micro internet gateway.
    #
    #     :param cell:
    #         The ID of a micro internet gateway.
    #     :return: <Response 200>
    #     """
    #     cell = \
    #         self.get_cell(cell)
    #     return cell.reset_password(self.session)

    # def operations(self, **params):
    #     """List operations.

    #     :param kwargs \*\*params: Optional query parameters to be sent to limit
    #                               the resources being returned.

    #     :returns: A list of operation objects
    #     :rtype: list of :class:`~openstack.micro_internet_gateway.v1.
    #         operation.Operation`
    #     """
    #     return list(self._list(_operation.Operation,
    #                            paginated=False, **params))

    # def get_operation(
    #         self, operation_id):
    #     """Show operation.

    #     :param string operation_id: ID of specified operation.
    #     :return: :class:`~openstack.micro_internet_gateway.v1.
    #         operation.Operation`
    #     """
    #     return self._get(_operation.Operation, operation_id)

