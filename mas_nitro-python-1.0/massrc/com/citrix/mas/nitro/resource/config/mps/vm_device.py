'''
Copyright (c) 2008-2015 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response
from massrc.com.citrix.mas.nitro.resource.config.mps.network_interface import network_interface

from massrc.com.citrix.mas.nitro.resource.config.mps.managed_device import managed_device

'''
Configuration for VM Device resource
'''

class vm_device(managed_device):
	_image_name= ""
	_network_interfaces=[]
	_vm_state= ""
	_uuid= ""
	_vm_memory_total= ""
	_cpu_core_mgmt= ""
	_ssl_virtual_functions= ""
	_throughput_limit= ""
	_sdxtools_http_port= ""
	_host_ip_address= ""
	_vlan_id_0_1= ""
	_provision_with_xva= ""
	_disk_space= ""
	_virtual_functions= ""
	_la_mgmt= ""
	_assigned_cpu_socket= ""
	_vlan_id_0_2= ""
	_number_of_ssl_cores= ""
	_throughput= ""
	_fips_partition_name= ""
	_sdxtools_public_key= ""
	_template_name= ""
	_domid= ""
	_cpu_core_pe= ""
	_vm_description= ""
	_http_port= ""
	_max_burst_throughput= ""
	_ssh_port= ""
	_mac_eth0= ""
	_vm_rx= ""
	_disk_allocation= ""
	_burst_priority= ""
	_preferred_cpu_socket= ""
	_vm_tx= ""
	_routable= ""
	_throughput_allocation_mode= ""
	_number_of_cores= ""
	_lb_role= ""
	_has_sdxtools= ""
	_vm_memory_used= ""
	_https_port= ""
	_number_of_cpu= ""
	_domain_name= ""
	_vm_memory_free= ""
	_formation_instance_id= ""
	_vm_memory_usage= ""
	_sdxtools_version= ""
	_vm_cpu_usage= ""
	_snmp_port= ""
	_vlan_1_2= ""
	_vrid_list_ipv4_1_2=[]
	_vlan_1_7= ""
	_vrid_list_ipv6_1_2=[]
	_vrid_list_ipv4_1_4=[]
	_vrid_list_ipv6_10_6=[]
	_if_10_4= ""
	_vlan_10_5= ""
	_vrid_list_ipv6_10_3=[]
	_vrid_list_ipv6_1_1=[]
	_if_1_5= ""
	_receiveuntagged_1_4= ""
	_vrid_list_ipv6_10_4=[]
	_vrid_list_ipv6_1_3=[]
	_if_10_3= ""
	_vrid_list_ipv6_10_5=[]
	_receiveuntagged_10_4= ""
	_vrid_list_ipv6_1_8=[]
	_vlan_10_6= ""
	_if_10_5= ""
	_vrid_list_ipv6_1_6=[]
	_if_10_7= ""
	_receiveuntagged_10_8= ""
	_vrid_list_ipv6_1_4=[]
	_receiveuntagged_1_6= ""
	_vlan_1_4= ""
	_if_1_2= ""
	_receiveuntagged_1_5= ""
	_receiveuntagged_10_6= ""
	_receiveuntagged_10_1= ""
	_vrid_list_ipv6_1_5=[]
	_vrid_list_ipv4_1_6=[]
	_vrid_list_ipv6_10_8=[]
	_vrid_list_ipv4_1_7=[]
	_receiveuntagged_10_2= ""
	_vrid_list_ipv4_1_5=[]
	_receiveuntagged_1_7= ""
	_vlan_10_4= ""
	_if_1_7= ""
	_receiveuntagged_1_1= ""
	_vrid_list_ipv6_1_7=[]
	_if_10_1= ""
	_if_10_8= ""
	_l2_enabled= ""
	_vlan_10_7= ""
	_vlan_10_1= ""
	_receiveuntagged_1_2= ""
	_reboot_vm_on_cpu_change= ""
	_vlan_1_6= ""
	_vrid_list_ipv4_1_3=[]
	_receiveuntagged_10_7= ""
	_vrid_list_ipv4_1_1=[]
	_vlan_1_1= ""
	_vrid_list_ipv6_10_7=[]
	_vlan_1_8= ""
	_vlan_10_2= ""
	_receiveuntagged_10_5= ""
	_vrid_list_ipv4_10_3=[]
	_receiveuntagged_1_8= ""
	_vrid_list_ipv4_1_8=[]
	_vrid_list_ipv4_10_6=[]
	_vlan_1_3= ""
	_vrid_list_ipv4_10_4=[]
	_if_1_6= ""
	_if_10_6= ""
	_receiveuntagged_10_3= ""
	_vlan_10_3= ""
	_vlan_1_5= ""
	_if_1_3= ""
	_if_1_4= ""
	_vrid_list_ipv4_10_5=[]
	_vrid_list_ipv4_10_8=[]
	_if_1_1= ""
	_vlan_10_8= ""
	_vrid_list_ipv4_10_7=[]
	_receiveuntagged_1_3= ""
	_vrid_list_ipv4_10_2=[]
	_if_1_8= ""
	_vrid_list_ipv4_10_1=[]
	_vrid_list_ipv6_10_2=[]
	_if_10_2= ""
	_vrid_list_ipv6_10_1=[]
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "vm_device"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(vm_device,self).get_object_id()
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "vm_devices"
		except Exception as e :
			raise e



	'''
	get Image Name, This parameter is used while provisioning VM Instance with XVA image, template_name is given priority if provided along with image_name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set Image Name, This parameter is used while provisioning VM Instance with XVA image, template_name is given priority if provided along with image_name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get Network Interfaces
	'''
	@property
	def network_interfaces(self) :
		try:
			return self._network_interfaces
		except Exception as e :
			raise e
	'''
	set Network Interfaces
	'''
	@network_interfaces.setter
	def network_interfaces(self,network_interfaces) :
		try :
			if not isinstance(network_interfaces,list):
				raise TypeError("network_interfaces must be set to array of network_interface value")
			for item in network_interfaces :
				if not isinstance(item,network_interface):
					raise TypeError("item must be set to network_interface value")
			self._network_interfaces = network_interfaces
		except Exception as e :
			raise e


	'''
	get State of Virtual Machine (Running | Halted)
	'''
	@property
	def vm_state(self) :
		try:
			return self._vm_state
		except Exception as e :
			raise e


	'''
	get UUID of VM Instance
	'''
	@property
	def uuid(self) :
		try:
			return self._uuid
		except Exception as e :
			raise e


	'''
	get Total Memory of VM Instance in MB
	'''
	@property
	def vm_memory_total(self) :
		try:
			return self._vm_memory_total
		except Exception as e :
			raise e
	'''
	set Total Memory of VM Instance in MB
	'''
	@vm_memory_total.setter
	def vm_memory_total(self,vm_memory_total):
		try :
			if not isinstance(vm_memory_total,float):
				raise TypeError("vm_memory_total must be set to float value")
			self._vm_memory_total = vm_memory_total
		except Exception as e :
			raise e


	'''
	get Management CPU cores assigned to VM Instance
	'''
	@property
	def cpu_core_mgmt(self) :
		try:
			return self._cpu_core_mgmt
		except Exception as e :
			raise e


	'''
	get SSL Virtual Functions assigned to VM Instance
	'''
	@property
	def ssl_virtual_functions(self) :
		try:
			return self._ssl_virtual_functions
		except Exception as e :
			raise e


	'''
	get Throughput Limit in Mbps set for VM Instance
	'''
	@property
	def throughput_limit(self) :
		try:
			return self._throughput_limit
		except Exception as e :
			raise e
	'''
	set Throughput Limit in Mbps set for VM Instance
	'''
	@throughput_limit.setter
	def throughput_limit(self,throughput_limit):
		try :
			if not isinstance(throughput_limit,float):
				raise TypeError("throughput_limit must be set to float value")
			self._throughput_limit = throughput_limit
		except Exception as e :
			raise e


	'''
	get Http Port number to communicate to SDXTools
	'''
	@property
	def sdxtools_http_port(self) :
		try:
			return self._sdxtools_http_port
		except Exception as e :
			raise e


	'''
	get Host IPAddress where VM is provisioned
	'''
	@property
	def host_ip_address(self) :
		try:
			return self._host_ip_address
		except Exception as e :
			raise e
	'''
	set Host IPAddress where VM is provisioned
	'''
	@host_ip_address.setter
	def host_ip_address(self,host_ip_address):
		try :
			if not isinstance(host_ip_address,str):
				raise TypeError("host_ip_address must be set to str value")
			self._host_ip_address = host_ip_address
		except Exception as e :
			raise e


	'''
	get VLAN id for the management interface 0/1
	'''
	@property
	def vlan_id_0_1(self) :
		try:
			return self._vlan_id_0_1
		except Exception as e :
			raise e
	'''
	set VLAN id for the management interface 0/1
	'''
	@vlan_id_0_1.setter
	def vlan_id_0_1(self,vlan_id_0_1):
		try :
			if not isinstance(vlan_id_0_1,int):
				raise TypeError("vlan_id_0_1 must be set to int value")
			self._vlan_id_0_1 = vlan_id_0_1
		except Exception as e :
			raise e


	'''
	get True if provision through XVA, false if provision through template
	'''
	@property
	def provision_with_xva(self) :
		try:
			return self._provision_with_xva
		except Exception as e :
			raise e
	'''
	set True if provision through XVA, false if provision through template
	'''
	@provision_with_xva.setter
	def provision_with_xva(self,provision_with_xva):
		try :
			if not isinstance(provision_with_xva,bool):
				raise TypeError("provision_with_xva must be set to bool value")
			self._provision_with_xva = provision_with_xva
		except Exception as e :
			raise e


	'''
	get Show Disk Space (GB) available to VM Instance
	'''
	@property
	def disk_space(self) :
		try:
			return self._disk_space
		except Exception as e :
			raise e
	'''
	set Show Disk Space (GB) available to VM Instance
	'''
	@disk_space.setter
	def disk_space(self,disk_space):
		try :
			if not isinstance(disk_space,float):
				raise TypeError("disk_space must be set to float value")
			self._disk_space = disk_space
		except Exception as e :
			raise e


	'''
	get Virtual Functions assigned to VM Instance
	'''
	@property
	def virtual_functions(self) :
		try:
			return self._virtual_functions
		except Exception as e :
			raise e


	'''
	get Bond consisting of management ports on VM Instance
	'''
	@property
	def la_mgmt(self) :
		try:
			return self._la_mgmt
		except Exception as e :
			raise e
	'''
	set Bond consisting of management ports on VM Instance
	'''
	@la_mgmt.setter
	def la_mgmt(self,la_mgmt):
		try :
			if not isinstance(la_mgmt,bool):
				raise TypeError("la_mgmt must be set to bool value")
			self._la_mgmt = la_mgmt
		except Exception as e :
			raise e


	'''
	get Assigned CPU Socket
	'''
	@property
	def assigned_cpu_socket(self) :
		try:
			return self._assigned_cpu_socket
		except Exception as e :
			raise e


	'''
	get VLAN id for the management interface 0/2
	'''
	@property
	def vlan_id_0_2(self) :
		try:
			return self._vlan_id_0_2
		except Exception as e :
			raise e
	'''
	set VLAN id for the management interface 0/2
	'''
	@vlan_id_0_2.setter
	def vlan_id_0_2(self,vlan_id_0_2):
		try :
			if not isinstance(vlan_id_0_2,int):
				raise TypeError("vlan_id_0_2 must be set to int value")
			self._vlan_id_0_2 = vlan_id_0_2
		except Exception as e :
			raise e


	'''
	get Assign number of ssl virtual functions to VM Instance
	'''
	@property
	def number_of_ssl_cores(self) :
		try:
			return self._number_of_ssl_cores
		except Exception as e :
			raise e
	'''
	set Assign number of ssl virtual functions to VM Instance
	'''
	@number_of_ssl_cores.setter
	def number_of_ssl_cores(self,number_of_ssl_cores):
		try :
			if not isinstance(number_of_ssl_cores,int):
				raise TypeError("number_of_ssl_cores must be set to int value")
			self._number_of_ssl_cores = number_of_ssl_cores
		except Exception as e :
			raise e


	'''
	get Assign throughput in Mbps to VM Instance
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set Assign throughput in Mbps to VM Instance
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,float):
				raise TypeError("throughput must be set to float value")
			self._throughput = throughput
		except Exception as e :
			raise e


	'''
	get FIPS Partition Name
	'''
	@property
	def fips_partition_name(self) :
		try:
			return self._fips_partition_name
		except Exception as e :
			raise e
	'''
	set FIPS Partition Name
	'''
	@fips_partition_name.setter
	def fips_partition_name(self,fips_partition_name):
		try :
			if not isinstance(fips_partition_name,str):
				raise TypeError("fips_partition_name must be set to str value")
			self._fips_partition_name = fips_partition_name
		except Exception as e :
			raise e


	'''
	get SDXTools HTTPS Public Key
	'''
	@property
	def sdxtools_public_key(self) :
		try:
			return self._sdxtools_public_key
		except Exception as e :
			raise e


	'''
	get Template Name, This parameter is used while provisioning VM Instance with template, template_name is given priority if provided along with image_name
	'''
	@property
	def template_name(self) :
		try:
			return self._template_name
		except Exception as e :
			raise e
	'''
	set Template Name, This parameter is used while provisioning VM Instance with template, template_name is given priority if provided along with image_name
	'''
	@template_name.setter
	def template_name(self,template_name):
		try :
			if not isinstance(template_name,str):
				raise TypeError("template_name must be set to str value")
			self._template_name = template_name
		except Exception as e :
			raise e


	'''
	get DOM Id assigned to VM Instance
	'''
	@property
	def domid(self) :
		try:
			return self._domid
		except Exception as e :
			raise e


	'''
	get Packet Engine cores assigned to VM Instance
	'''
	@property
	def cpu_core_pe(self) :
		try:
			return self._cpu_core_pe
		except Exception as e :
			raise e


	'''
	get Description
	'''
	@property
	def vm_description(self) :
		try:
			return self._vm_description
		except Exception as e :
			raise e


	'''
	get HTTP port of the container.
	'''
	@property
	def http_port(self) :
		try:
			return self._http_port
		except Exception as e :
			raise e
	'''
	set HTTP port of the container.
	'''
	@http_port.setter
	def http_port(self,http_port):
		try :
			if not isinstance(http_port,int):
				raise TypeError("http_port must be set to int value")
			self._http_port = http_port
		except Exception as e :
			raise e


	'''
	get Maximum burst throughput in Mbps of VM Instance
	'''
	@property
	def max_burst_throughput(self) :
		try:
			return self._max_burst_throughput
		except Exception as e :
			raise e
	'''
	set Maximum burst throughput in Mbps of VM Instance
	'''
	@max_burst_throughput.setter
	def max_burst_throughput(self,max_burst_throughput):
		try :
			if not isinstance(max_burst_throughput,float):
				raise TypeError("max_burst_throughput must be set to float value")
			self._max_burst_throughput = max_burst_throughput
		except Exception as e :
			raise e


	'''
	get SSH port of the container.
	'''
	@property
	def ssh_port(self) :
		try:
			return self._ssh_port
		except Exception as e :
			raise e
	'''
	set SSH port of the container.
	'''
	@ssh_port.setter
	def ssh_port(self,ssh_port):
		try :
			if not isinstance(ssh_port,int):
				raise TypeError("ssh_port must be set to int value")
			self._ssh_port = ssh_port
		except Exception as e :
			raise e


	'''
	get MAC Address of eth0 on VM Instance
	'''
	@property
	def mac_eth0(self) :
		try:
			return self._mac_eth0
		except Exception as e :
			raise e


	'''
	get In Throughput of VM Instance in Mbps
	'''
	@property
	def vm_rx(self) :
		try:
			return self._vm_rx
		except Exception as e :
			raise e


	'''
	get Disk allocation for VM Instance
	'''
	@property
	def disk_allocation(self) :
		try:
			return self._disk_allocation
		except Exception as e :
			raise e


	'''
	get Burst Priority of the VM Instance.
	'''
	@property
	def burst_priority(self) :
		try:
			return self._burst_priority
		except Exception as e :
			raise e
	'''
	set Burst Priority of the VM Instance.
	'''
	@burst_priority.setter
	def burst_priority(self,burst_priority):
		try :
			if not isinstance(burst_priority,int):
				raise TypeError("burst_priority must be set to int value")
			self._burst_priority = burst_priority
		except Exception as e :
			raise e


	'''
	get Preferred CPU Socket
	'''
	@property
	def preferred_cpu_socket(self) :
		try:
			return self._preferred_cpu_socket
		except Exception as e :
			raise e


	'''
	get Out Throughput of VM Instance in Mbps
	'''
	@property
	def vm_tx(self) :
		try:
			return self._vm_tx
		except Exception as e :
			raise e


	'''
	get Whether the device is reachable or not
	'''
	@property
	def routable(self) :
		try:
			return self._routable
		except Exception as e :
			raise e
	'''
	set Whether the device is reachable or not
	'''
	@routable.setter
	def routable(self,routable):
		try :
			if not isinstance(routable,bool):
				raise TypeError("routable must be set to bool value")
			self._routable = routable
		except Exception as e :
			raise e


	'''
	get Throughput Allocation Mode: 0-Fixed, 1-Burst-able
	'''
	@property
	def throughput_allocation_mode(self) :
		try:
			return self._throughput_allocation_mode
		except Exception as e :
			raise e
	'''
	set Throughput Allocation Mode: 0-Fixed, 1-Burst-able
	'''
	@throughput_allocation_mode.setter
	def throughput_allocation_mode(self,throughput_allocation_mode):
		try :
			if not isinstance(throughput_allocation_mode,int):
				raise TypeError("throughput_allocation_mode must be set to int value")
			self._throughput_allocation_mode = throughput_allocation_mode
		except Exception as e :
			raise e


	'''
	get Number of cores that are assigned to VM Instance
	'''
	@property
	def number_of_cores(self) :
		try:
			return self._number_of_cores
		except Exception as e :
			raise e
	'''
	set Number of cores that are assigned to VM Instance
	'''
	@number_of_cores.setter
	def number_of_cores(self,number_of_cores):
		try :
			if not isinstance(number_of_cores,int):
				raise TypeError("number_of_cores must be set to int value")
			self._number_of_cores = number_of_cores
		except Exception as e :
			raise e


	'''
	get LB role performed by the device: North-South (Ingress or server), or East-West (client)
	'''
	@property
	def lb_role(self) :
		try:
			return self._lb_role
		except Exception as e :
			raise e
	'''
	set LB role performed by the device: North-South (Ingress or server), or East-West (client)
	'''
	@lb_role.setter
	def lb_role(self,lb_role):
		try :
			if not isinstance(lb_role,str):
				raise TypeError("lb_role must be set to str value")
			self._lb_role = lb_role
		except Exception as e :
			raise e


	'''
	get True if SDX Tools are installed on this VM
	'''
	@property
	def has_sdxtools(self) :
		try:
			return self._has_sdxtools
		except Exception as e :
			raise e


	'''
	get Memory Used (MB) by VM Instance
	'''
	@property
	def vm_memory_used(self) :
		try:
			return self._vm_memory_used
		except Exception as e :
			raise e


	'''
	get HTTPS port of the container.
	'''
	@property
	def https_port(self) :
		try:
			return self._https_port
		except Exception as e :
			raise e
	'''
	set HTTPS port of the container.
	'''
	@https_port.setter
	def https_port(self,https_port):
		try :
			if not isinstance(https_port,int):
				raise TypeError("https_port must be set to int value")
			self._https_port = https_port
		except Exception as e :
			raise e


	'''
	get Number of CPU that is assigned to VM Instance
	'''
	@property
	def number_of_cpu(self) :
		try:
			return self._number_of_cpu
		except Exception as e :
			raise e
	'''
	set Number of CPU that is assigned to VM Instance
	'''
	@number_of_cpu.setter
	def number_of_cpu(self,number_of_cpu):
		try :
			if not isinstance(number_of_cpu,int):
				raise TypeError("number_of_cpu must be set to int value")
			self._number_of_cpu = number_of_cpu
		except Exception as e :
			raise e


	'''
	get Domain name of VM Device
	'''
	@property
	def domain_name(self) :
		try:
			return self._domain_name
		except Exception as e :
			raise e
	'''
	set Domain name of VM Device
	'''
	@domain_name.setter
	def domain_name(self,domain_name):
		try :
			if not isinstance(domain_name,str):
				raise TypeError("domain_name must be set to str value")
			self._domain_name = domain_name
		except Exception as e :
			raise e


	'''
	get Free Memory (MB) available in VM Instance
	'''
	@property
	def vm_memory_free(self) :
		try:
			return self._vm_memory_free
		except Exception as e :
			raise e


	'''
	get Formation Instance Id that this VM is Part of
	'''
	@property
	def formation_instance_id(self) :
		try:
			return self._formation_instance_id
		except Exception as e :
			raise e
	'''
	set Formation Instance Id that this VM is Part of
	'''
	@formation_instance_id.setter
	def formation_instance_id(self,formation_instance_id):
		try :
			if not isinstance(formation_instance_id,str):
				raise TypeError("formation_instance_id must be set to str value")
			self._formation_instance_id = formation_instance_id
		except Exception as e :
			raise e


	'''
	get Memory Usage (%) of VM Instance
	'''
	@property
	def vm_memory_usage(self) :
		try:
			return self._vm_memory_usage
		except Exception as e :
			raise e


	'''
	get SDXTools version running on VM Instance
	'''
	@property
	def sdxtools_version(self) :
		try:
			return self._sdxtools_version
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of VM Instance
	'''
	@property
	def vm_cpu_usage(self) :
		try:
			return self._vm_cpu_usage
		except Exception as e :
			raise e


	'''
	get SNMP port of the container.
	'''
	@property
	def snmp_port(self) :
		try:
			return self._snmp_port
		except Exception as e :
			raise e
	'''
	set SNMP port of the container.
	'''
	@snmp_port.setter
	def snmp_port(self,snmp_port):
		try :
			if not isinstance(snmp_port,int):
				raise TypeError("snmp_port must be set to int value")
			self._snmp_port = snmp_port
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/2 on VM Instance
	'''
	@property
	def vlan_1_2(self):
		try:
			return self._vlan_1_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/2 on VM Instance
	'''
	@vlan_1_2.setter
	def vlan_1_2(self,vlan_1_2):
		try :
			if not isinstance(vlan_1_2,int):
				raise TypeError("vlan_1_2 must be set to int value")
			self._vlan_1_2 = vlan_1_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/2 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_2(self) :
		try:
			return self._vrid_list_ipv4_1_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/2 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_2.setter
	def vrid_list_ipv4_1_2(self,vrid_list_ipv4_1_2) :
		try :
			if not isinstance(vrid_list_ipv4_1_2,list):
				raise TypeError("vrid_list_ipv4_1_2 must be set to array of str value")
			for item in vrid_list_ipv4_1_2 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_2 = vrid_list_ipv4_1_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/7 on VM Instance
	'''
	@property
	def vlan_1_7(self):
		try:
			return self._vlan_1_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/7 on VM Instance
	'''
	@vlan_1_7.setter
	def vlan_1_7(self,vlan_1_7):
		try :
			if not isinstance(vlan_1_7,int):
				raise TypeError("vlan_1_7 must be set to int value")
			self._vlan_1_7 = vlan_1_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/2 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_2(self) :
		try:
			return self._vrid_list_ipv6_1_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/2 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_2.setter
	def vrid_list_ipv6_1_2(self,vrid_list_ipv6_1_2) :
		try :
			if not isinstance(vrid_list_ipv6_1_2,list):
				raise TypeError("vrid_list_ipv6_1_2 must be set to array of str value")
			for item in vrid_list_ipv6_1_2 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_2 = vrid_list_ipv6_1_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/4 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_4(self) :
		try:
			return self._vrid_list_ipv4_1_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/4 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_4.setter
	def vrid_list_ipv4_1_4(self,vrid_list_ipv4_1_4) :
		try :
			if not isinstance(vrid_list_ipv4_1_4,list):
				raise TypeError("vrid_list_ipv4_1_4 must be set to array of str value")
			for item in vrid_list_ipv4_1_4 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_4 = vrid_list_ipv4_1_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/6 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_6(self) :
		try:
			return self._vrid_list_ipv6_10_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/6 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_6.setter
	def vrid_list_ipv6_10_6(self,vrid_list_ipv6_10_6) :
		try :
			if not isinstance(vrid_list_ipv6_10_6,list):
				raise TypeError("vrid_list_ipv6_10_6 must be set to array of str value")
			for item in vrid_list_ipv6_10_6 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_6 = vrid_list_ipv6_10_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/4 on VM Instance
	'''
	@property
	def if_10_4(self):
		try:
			return self._if_10_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/4 on VM Instance
	'''
	@if_10_4.setter
	def if_10_4(self,if_10_4):
		try :
			if not isinstance(if_10_4,bool):
				raise TypeError("if_10_4 must be set to bool value")
			self._if_10_4 = if_10_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/5 on VM Instance
	'''
	@property
	def vlan_10_5(self):
		try:
			return self._vlan_10_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/5 on VM Instance
	'''
	@vlan_10_5.setter
	def vlan_10_5(self,vlan_10_5):
		try :
			if not isinstance(vlan_10_5,int):
				raise TypeError("vlan_10_5 must be set to int value")
			self._vlan_10_5 = vlan_10_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/3 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_3(self) :
		try:
			return self._vrid_list_ipv6_10_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/3 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_3.setter
	def vrid_list_ipv6_10_3(self,vrid_list_ipv6_10_3) :
		try :
			if not isinstance(vrid_list_ipv6_10_3,list):
				raise TypeError("vrid_list_ipv6_10_3 must be set to array of str value")
			for item in vrid_list_ipv6_10_3 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_3 = vrid_list_ipv6_10_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/1 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_1(self) :
		try:
			return self._vrid_list_ipv6_1_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/1 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_1.setter
	def vrid_list_ipv6_1_1(self,vrid_list_ipv6_1_1) :
		try :
			if not isinstance(vrid_list_ipv6_1_1,list):
				raise TypeError("vrid_list_ipv6_1_1 must be set to array of str value")
			for item in vrid_list_ipv6_1_1 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_1 = vrid_list_ipv6_1_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/5 on VM Instance
	'''
	@property
	def if_1_5(self):
		try:
			return self._if_1_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/5 on VM Instance
	'''
	@if_1_5.setter
	def if_1_5(self,if_1_5):
		try :
			if not isinstance(if_1_5,bool):
				raise TypeError("if_1_5 must be set to bool value")
			self._if_1_5 = if_1_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/4 on VM Instance
	'''
	@property
	def receiveuntagged_1_4(self):
		try:
			return self._receiveuntagged_1_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/4 on VM Instance
	'''
	@receiveuntagged_1_4.setter
	def receiveuntagged_1_4(self,receiveuntagged_1_4):
		try :
			if not isinstance(receiveuntagged_1_4,bool):
				raise TypeError("receiveuntagged_1_4 must be set to bool value")
			self._receiveuntagged_1_4 = receiveuntagged_1_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/4 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_4(self) :
		try:
			return self._vrid_list_ipv6_10_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/4 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_4.setter
	def vrid_list_ipv6_10_4(self,vrid_list_ipv6_10_4) :
		try :
			if not isinstance(vrid_list_ipv6_10_4,list):
				raise TypeError("vrid_list_ipv6_10_4 must be set to array of str value")
			for item in vrid_list_ipv6_10_4 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_4 = vrid_list_ipv6_10_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/3for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_3(self) :
		try:
			return self._vrid_list_ipv6_1_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/3for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_3.setter
	def vrid_list_ipv6_1_3(self,vrid_list_ipv6_1_3) :
		try :
			if not isinstance(vrid_list_ipv6_1_3,list):
				raise TypeError("vrid_list_ipv6_1_3 must be set to array of str value")
			for item in vrid_list_ipv6_1_3 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_3 = vrid_list_ipv6_1_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/3 on VM Instance
	'''
	@property
	def if_10_3(self):
		try:
			return self._if_10_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/3 on VM Instance
	'''
	@if_10_3.setter
	def if_10_3(self,if_10_3):
		try :
			if not isinstance(if_10_3,bool):
				raise TypeError("if_10_3 must be set to bool value")
			self._if_10_3 = if_10_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/5 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_5(self) :
		try:
			return self._vrid_list_ipv6_10_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/5 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_5.setter
	def vrid_list_ipv6_10_5(self,vrid_list_ipv6_10_5) :
		try :
			if not isinstance(vrid_list_ipv6_10_5,list):
				raise TypeError("vrid_list_ipv6_10_5 must be set to array of str value")
			for item in vrid_list_ipv6_10_5 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_5 = vrid_list_ipv6_10_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/4 on VM Instance
	'''
	@property
	def receiveuntagged_10_4(self):
		try:
			return self._receiveuntagged_10_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/4 on VM Instance
	'''
	@receiveuntagged_10_4.setter
	def receiveuntagged_10_4(self,receiveuntagged_10_4):
		try :
			if not isinstance(receiveuntagged_10_4,bool):
				raise TypeError("receiveuntagged_10_4 must be set to bool value")
			self._receiveuntagged_10_4 = receiveuntagged_10_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/8 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_8(self) :
		try:
			return self._vrid_list_ipv6_1_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/8 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_8.setter
	def vrid_list_ipv6_1_8(self,vrid_list_ipv6_1_8) :
		try :
			if not isinstance(vrid_list_ipv6_1_8,list):
				raise TypeError("vrid_list_ipv6_1_8 must be set to array of str value")
			for item in vrid_list_ipv6_1_8 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_8 = vrid_list_ipv6_1_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/6 on VM Instance
	'''
	@property
	def vlan_10_6(self):
		try:
			return self._vlan_10_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/6 on VM Instance
	'''
	@vlan_10_6.setter
	def vlan_10_6(self,vlan_10_6):
		try :
			if not isinstance(vlan_10_6,int):
				raise TypeError("vlan_10_6 must be set to int value")
			self._vlan_10_6 = vlan_10_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/5 on VM Instance
	'''
	@property
	def if_10_5(self):
		try:
			return self._if_10_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/5 on VM Instance
	'''
	@if_10_5.setter
	def if_10_5(self,if_10_5):
		try :
			if not isinstance(if_10_5,bool):
				raise TypeError("if_10_5 must be set to bool value")
			self._if_10_5 = if_10_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/6 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_6(self) :
		try:
			return self._vrid_list_ipv6_1_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/6 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_6.setter
	def vrid_list_ipv6_1_6(self,vrid_list_ipv6_1_6) :
		try :
			if not isinstance(vrid_list_ipv6_1_6,list):
				raise TypeError("vrid_list_ipv6_1_6 must be set to array of str value")
			for item in vrid_list_ipv6_1_6 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_6 = vrid_list_ipv6_1_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/7 on VM Instance
	'''
	@property
	def if_10_7(self):
		try:
			return self._if_10_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/7 on VM Instance
	'''
	@if_10_7.setter
	def if_10_7(self,if_10_7):
		try :
			if not isinstance(if_10_7,bool):
				raise TypeError("if_10_7 must be set to bool value")
			self._if_10_7 = if_10_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/8 on VM Instance
	'''
	@property
	def receiveuntagged_10_8(self):
		try:
			return self._receiveuntagged_10_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/8 on VM Instance
	'''
	@receiveuntagged_10_8.setter
	def receiveuntagged_10_8(self,receiveuntagged_10_8):
		try :
			if not isinstance(receiveuntagged_10_8,bool):
				raise TypeError("receiveuntagged_10_8 must be set to bool value")
			self._receiveuntagged_10_8 = receiveuntagged_10_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/4 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_4(self) :
		try:
			return self._vrid_list_ipv6_1_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/4 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_4.setter
	def vrid_list_ipv6_1_4(self,vrid_list_ipv6_1_4) :
		try :
			if not isinstance(vrid_list_ipv6_1_4,list):
				raise TypeError("vrid_list_ipv6_1_4 must be set to array of str value")
			for item in vrid_list_ipv6_1_4 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_4 = vrid_list_ipv6_1_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/6 on VM Instance
	'''
	@property
	def receiveuntagged_1_6(self):
		try:
			return self._receiveuntagged_1_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/6 on VM Instance
	'''
	@receiveuntagged_1_6.setter
	def receiveuntagged_1_6(self,receiveuntagged_1_6):
		try :
			if not isinstance(receiveuntagged_1_6,bool):
				raise TypeError("receiveuntagged_1_6 must be set to bool value")
			self._receiveuntagged_1_6 = receiveuntagged_1_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/4 on VM Instance
	'''
	@property
	def vlan_1_4(self):
		try:
			return self._vlan_1_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/4 on VM Instance
	'''
	@vlan_1_4.setter
	def vlan_1_4(self,vlan_1_4):
		try :
			if not isinstance(vlan_1_4,int):
				raise TypeError("vlan_1_4 must be set to int value")
			self._vlan_1_4 = vlan_1_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/2 on VM Instance
	'''
	@property
	def if_1_2(self):
		try:
			return self._if_1_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/2 on VM Instance
	'''
	@if_1_2.setter
	def if_1_2(self,if_1_2):
		try :
			if not isinstance(if_1_2,bool):
				raise TypeError("if_1_2 must be set to bool value")
			self._if_1_2 = if_1_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/5 on VM Instance
	'''
	@property
	def receiveuntagged_1_5(self):
		try:
			return self._receiveuntagged_1_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/5 on VM Instance
	'''
	@receiveuntagged_1_5.setter
	def receiveuntagged_1_5(self,receiveuntagged_1_5):
		try :
			if not isinstance(receiveuntagged_1_5,bool):
				raise TypeError("receiveuntagged_1_5 must be set to bool value")
			self._receiveuntagged_1_5 = receiveuntagged_1_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/6 on VM Instance
	'''
	@property
	def receiveuntagged_10_6(self):
		try:
			return self._receiveuntagged_10_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/6 on VM Instance
	'''
	@receiveuntagged_10_6.setter
	def receiveuntagged_10_6(self,receiveuntagged_10_6):
		try :
			if not isinstance(receiveuntagged_10_6,bool):
				raise TypeError("receiveuntagged_10_6 must be set to bool value")
			self._receiveuntagged_10_6 = receiveuntagged_10_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/1 on VM Instance
	'''
	@property
	def receiveuntagged_10_1(self):
		try:
			return self._receiveuntagged_10_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/1 on VM Instance
	'''
	@receiveuntagged_10_1.setter
	def receiveuntagged_10_1(self,receiveuntagged_10_1):
		try :
			if not isinstance(receiveuntagged_10_1,bool):
				raise TypeError("receiveuntagged_10_1 must be set to bool value")
			self._receiveuntagged_10_1 = receiveuntagged_10_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/5 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_5(self) :
		try:
			return self._vrid_list_ipv6_1_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/5 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_5.setter
	def vrid_list_ipv6_1_5(self,vrid_list_ipv6_1_5) :
		try :
			if not isinstance(vrid_list_ipv6_1_5,list):
				raise TypeError("vrid_list_ipv6_1_5 must be set to array of str value")
			for item in vrid_list_ipv6_1_5 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_5 = vrid_list_ipv6_1_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/6 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_6(self) :
		try:
			return self._vrid_list_ipv4_1_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/6 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_6.setter
	def vrid_list_ipv4_1_6(self,vrid_list_ipv4_1_6) :
		try :
			if not isinstance(vrid_list_ipv4_1_6,list):
				raise TypeError("vrid_list_ipv4_1_6 must be set to array of str value")
			for item in vrid_list_ipv4_1_6 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_6 = vrid_list_ipv4_1_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/8 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_8(self) :
		try:
			return self._vrid_list_ipv6_10_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/8 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_8.setter
	def vrid_list_ipv6_10_8(self,vrid_list_ipv6_10_8) :
		try :
			if not isinstance(vrid_list_ipv6_10_8,list):
				raise TypeError("vrid_list_ipv6_10_8 must be set to array of str value")
			for item in vrid_list_ipv6_10_8 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_8 = vrid_list_ipv6_10_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/7 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_7(self) :
		try:
			return self._vrid_list_ipv4_1_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/7 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_7.setter
	def vrid_list_ipv4_1_7(self,vrid_list_ipv4_1_7) :
		try :
			if not isinstance(vrid_list_ipv4_1_7,list):
				raise TypeError("vrid_list_ipv4_1_7 must be set to array of str value")
			for item in vrid_list_ipv4_1_7 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_7 = vrid_list_ipv4_1_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/2 on VM Instance
	'''
	@property
	def receiveuntagged_10_2(self):
		try:
			return self._receiveuntagged_10_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/2 on VM Instance
	'''
	@receiveuntagged_10_2.setter
	def receiveuntagged_10_2(self,receiveuntagged_10_2):
		try :
			if not isinstance(receiveuntagged_10_2,bool):
				raise TypeError("receiveuntagged_10_2 must be set to bool value")
			self._receiveuntagged_10_2 = receiveuntagged_10_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/5 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_5(self) :
		try:
			return self._vrid_list_ipv4_1_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/5 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_5.setter
	def vrid_list_ipv4_1_5(self,vrid_list_ipv4_1_5) :
		try :
			if not isinstance(vrid_list_ipv4_1_5,list):
				raise TypeError("vrid_list_ipv4_1_5 must be set to array of str value")
			for item in vrid_list_ipv4_1_5 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_5 = vrid_list_ipv4_1_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/7 on VM Instance
	'''
	@property
	def receiveuntagged_1_7(self):
		try:
			return self._receiveuntagged_1_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/7 on VM Instance
	'''
	@receiveuntagged_1_7.setter
	def receiveuntagged_1_7(self,receiveuntagged_1_7):
		try :
			if not isinstance(receiveuntagged_1_7,bool):
				raise TypeError("receiveuntagged_1_7 must be set to bool value")
			self._receiveuntagged_1_7 = receiveuntagged_1_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/4 on VM Instance
	'''
	@property
	def vlan_10_4(self):
		try:
			return self._vlan_10_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/4 on VM Instance
	'''
	@vlan_10_4.setter
	def vlan_10_4(self,vlan_10_4):
		try :
			if not isinstance(vlan_10_4,int):
				raise TypeError("vlan_10_4 must be set to int value")
			self._vlan_10_4 = vlan_10_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/7 on VM Instance
	'''
	@property
	def if_1_7(self):
		try:
			return self._if_1_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/7 on VM Instance
	'''
	@if_1_7.setter
	def if_1_7(self,if_1_7):
		try :
			if not isinstance(if_1_7,bool):
				raise TypeError("if_1_7 must be set to bool value")
			self._if_1_7 = if_1_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/1 on VM Instance
	'''
	@property
	def receiveuntagged_1_1(self):
		try:
			return self._receiveuntagged_1_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/1 on VM Instance
	'''
	@receiveuntagged_1_1.setter
	def receiveuntagged_1_1(self,receiveuntagged_1_1):
		try :
			if not isinstance(receiveuntagged_1_1,bool):
				raise TypeError("receiveuntagged_1_1 must be set to bool value")
			self._receiveuntagged_1_1 = receiveuntagged_1_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/7 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_1_7(self) :
		try:
			return self._vrid_list_ipv6_1_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/7 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_1_7.setter
	def vrid_list_ipv6_1_7(self,vrid_list_ipv6_1_7) :
		try :
			if not isinstance(vrid_list_ipv6_1_7,list):
				raise TypeError("vrid_list_ipv6_1_7 must be set to array of str value")
			for item in vrid_list_ipv6_1_7 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_1_7 = vrid_list_ipv6_1_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/1 on VM Instance
	'''
	@property
	def if_10_1(self):
		try:
			return self._if_10_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/1 on VM Instance
	'''
	@if_10_1.setter
	def if_10_1(self,if_10_1):
		try :
			if not isinstance(if_10_1,bool):
				raise TypeError("if_10_1 must be set to bool value")
			self._if_10_1 = if_10_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/8 on VM Instance
	'''
	@property
	def if_10_8(self):
		try:
			return self._if_10_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/8 on VM Instance
	'''
	@if_10_8.setter
	def if_10_8(self,if_10_8):
		try :
			if not isinstance(if_10_8,bool):
				raise TypeError("if_10_8 must be set to bool value")
			self._if_10_8 = if_10_8
		except Exception as e :
			raise e

	'''
	L2mode status of VM Instance
	'''
	@property
	def l2_enabled(self):
		try:
			return self._l2_enabled
		except Exception as e :
			raise e
	'''
	L2mode status of VM Instance
	'''
	@l2_enabled.setter
	def l2_enabled(self,l2_enabled):
		try :
			if not isinstance(l2_enabled,bool):
				raise TypeError("l2_enabled must be set to bool value")
			self._l2_enabled = l2_enabled
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/7 on VM Instance
	'''
	@property
	def vlan_10_7(self):
		try:
			return self._vlan_10_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/7 on VM Instance
	'''
	@vlan_10_7.setter
	def vlan_10_7(self,vlan_10_7):
		try :
			if not isinstance(vlan_10_7,int):
				raise TypeError("vlan_10_7 must be set to int value")
			self._vlan_10_7 = vlan_10_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/1 on VM Instance
	'''
	@property
	def vlan_10_1(self):
		try:
			return self._vlan_10_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/1 on VM Instance
	'''
	@vlan_10_1.setter
	def vlan_10_1(self,vlan_10_1):
		try :
			if not isinstance(vlan_10_1,int):
				raise TypeError("vlan_10_1 must be set to int value")
			self._vlan_10_1 = vlan_10_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/2 on VM Instance
	'''
	@property
	def receiveuntagged_1_2(self):
		try:
			return self._receiveuntagged_1_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/2 on VM Instance
	'''
	@receiveuntagged_1_2.setter
	def receiveuntagged_1_2(self,receiveuntagged_1_2):
		try :
			if not isinstance(receiveuntagged_1_2,bool):
				raise TypeError("receiveuntagged_1_2 must be set to bool value")
			self._receiveuntagged_1_2 = receiveuntagged_1_2
		except Exception as e :
			raise e

	'''
	Reboot VMs on CPU change during resource allocation
	'''
	@property
	def reboot_vm_on_cpu_change(self):
		try:
			return self._reboot_vm_on_cpu_change
		except Exception as e :
			raise e
	'''
	Reboot VMs on CPU change during resource allocation
	'''
	@reboot_vm_on_cpu_change.setter
	def reboot_vm_on_cpu_change(self,reboot_vm_on_cpu_change):
		try :
			if not isinstance(reboot_vm_on_cpu_change,bool):
				raise TypeError("reboot_vm_on_cpu_change must be set to bool value")
			self._reboot_vm_on_cpu_change = reboot_vm_on_cpu_change
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/6 on VM Instance
	'''
	@property
	def vlan_1_6(self):
		try:
			return self._vlan_1_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/6 on VM Instance
	'''
	@vlan_1_6.setter
	def vlan_1_6(self,vlan_1_6):
		try :
			if not isinstance(vlan_1_6,int):
				raise TypeError("vlan_1_6 must be set to int value")
			self._vlan_1_6 = vlan_1_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/3for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_3(self) :
		try:
			return self._vrid_list_ipv4_1_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/3for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_3.setter
	def vrid_list_ipv4_1_3(self,vrid_list_ipv4_1_3) :
		try :
			if not isinstance(vrid_list_ipv4_1_3,list):
				raise TypeError("vrid_list_ipv4_1_3 must be set to array of str value")
			for item in vrid_list_ipv4_1_3 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_3 = vrid_list_ipv4_1_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/7 on VM Instance
	'''
	@property
	def receiveuntagged_10_7(self):
		try:
			return self._receiveuntagged_10_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/7 on VM Instance
	'''
	@receiveuntagged_10_7.setter
	def receiveuntagged_10_7(self,receiveuntagged_10_7):
		try :
			if not isinstance(receiveuntagged_10_7,bool):
				raise TypeError("receiveuntagged_10_7 must be set to bool value")
			self._receiveuntagged_10_7 = receiveuntagged_10_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/1 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_1(self) :
		try:
			return self._vrid_list_ipv4_1_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/1 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_1.setter
	def vrid_list_ipv4_1_1(self,vrid_list_ipv4_1_1) :
		try :
			if not isinstance(vrid_list_ipv4_1_1,list):
				raise TypeError("vrid_list_ipv4_1_1 must be set to array of str value")
			for item in vrid_list_ipv4_1_1 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_1 = vrid_list_ipv4_1_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/1 on VM Instance
	'''
	@property
	def vlan_1_1(self):
		try:
			return self._vlan_1_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/1 on VM Instance
	'''
	@vlan_1_1.setter
	def vlan_1_1(self,vlan_1_1):
		try :
			if not isinstance(vlan_1_1,int):
				raise TypeError("vlan_1_1 must be set to int value")
			self._vlan_1_1 = vlan_1_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/7 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_7(self) :
		try:
			return self._vrid_list_ipv6_10_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/7 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_7.setter
	def vrid_list_ipv6_10_7(self,vrid_list_ipv6_10_7) :
		try :
			if not isinstance(vrid_list_ipv6_10_7,list):
				raise TypeError("vrid_list_ipv6_10_7 must be set to array of str value")
			for item in vrid_list_ipv6_10_7 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_7 = vrid_list_ipv6_10_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/8 on VM Instance
	'''
	@property
	def vlan_1_8(self):
		try:
			return self._vlan_1_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/8 on VM Instance
	'''
	@vlan_1_8.setter
	def vlan_1_8(self,vlan_1_8):
		try :
			if not isinstance(vlan_1_8,int):
				raise TypeError("vlan_1_8 must be set to int value")
			self._vlan_1_8 = vlan_1_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/2 on VM Instance
	'''
	@property
	def vlan_10_2(self):
		try:
			return self._vlan_10_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/2 on VM Instance
	'''
	@vlan_10_2.setter
	def vlan_10_2(self,vlan_10_2):
		try :
			if not isinstance(vlan_10_2,int):
				raise TypeError("vlan_10_2 must be set to int value")
			self._vlan_10_2 = vlan_10_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/5 on VM Instance
	'''
	@property
	def receiveuntagged_10_5(self):
		try:
			return self._receiveuntagged_10_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/5 on VM Instance
	'''
	@receiveuntagged_10_5.setter
	def receiveuntagged_10_5(self,receiveuntagged_10_5):
		try :
			if not isinstance(receiveuntagged_10_5,bool):
				raise TypeError("receiveuntagged_10_5 must be set to bool value")
			self._receiveuntagged_10_5 = receiveuntagged_10_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/3 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_3(self) :
		try:
			return self._vrid_list_ipv4_10_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/3 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_3.setter
	def vrid_list_ipv4_10_3(self,vrid_list_ipv4_10_3) :
		try :
			if not isinstance(vrid_list_ipv4_10_3,list):
				raise TypeError("vrid_list_ipv4_10_3 must be set to array of str value")
			for item in vrid_list_ipv4_10_3 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_3 = vrid_list_ipv4_10_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/8 on VM Instance
	'''
	@property
	def receiveuntagged_1_8(self):
		try:
			return self._receiveuntagged_1_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/8 on VM Instance
	'''
	@receiveuntagged_1_8.setter
	def receiveuntagged_1_8(self,receiveuntagged_1_8):
		try :
			if not isinstance(receiveuntagged_1_8,bool):
				raise TypeError("receiveuntagged_1_8 must be set to bool value")
			self._receiveuntagged_1_8 = receiveuntagged_1_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/8 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_1_8(self) :
		try:
			return self._vrid_list_ipv4_1_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 1/8 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_1_8.setter
	def vrid_list_ipv4_1_8(self,vrid_list_ipv4_1_8) :
		try :
			if not isinstance(vrid_list_ipv4_1_8,list):
				raise TypeError("vrid_list_ipv4_1_8 must be set to array of str value")
			for item in vrid_list_ipv4_1_8 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_1_8 = vrid_list_ipv4_1_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/6 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_6(self) :
		try:
			return self._vrid_list_ipv4_10_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/6 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_6.setter
	def vrid_list_ipv4_10_6(self,vrid_list_ipv4_10_6) :
		try :
			if not isinstance(vrid_list_ipv4_10_6,list):
				raise TypeError("vrid_list_ipv4_10_6 must be set to array of str value")
			for item in vrid_list_ipv4_10_6 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_6 = vrid_list_ipv4_10_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/3 on VM Instance
	'''
	@property
	def vlan_1_3(self):
		try:
			return self._vlan_1_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/3 on VM Instance
	'''
	@vlan_1_3.setter
	def vlan_1_3(self,vlan_1_3):
		try :
			if not isinstance(vlan_1_3,int):
				raise TypeError("vlan_1_3 must be set to int value")
			self._vlan_1_3 = vlan_1_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/4 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_4(self) :
		try:
			return self._vrid_list_ipv4_10_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/4 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_4.setter
	def vrid_list_ipv4_10_4(self,vrid_list_ipv4_10_4) :
		try :
			if not isinstance(vrid_list_ipv4_10_4,list):
				raise TypeError("vrid_list_ipv4_10_4 must be set to array of str value")
			for item in vrid_list_ipv4_10_4 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_4 = vrid_list_ipv4_10_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/6 on VM Instance
	'''
	@property
	def if_1_6(self):
		try:
			return self._if_1_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/6 on VM Instance
	'''
	@if_1_6.setter
	def if_1_6(self,if_1_6):
		try :
			if not isinstance(if_1_6,bool):
				raise TypeError("if_1_6 must be set to bool value")
			self._if_1_6 = if_1_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/6 on VM Instance
	'''
	@property
	def if_10_6(self):
		try:
			return self._if_10_6
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/6 on VM Instance
	'''
	@if_10_6.setter
	def if_10_6(self,if_10_6):
		try :
			if not isinstance(if_10_6,bool):
				raise TypeError("if_10_6 must be set to bool value")
			self._if_10_6 = if_10_6
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/3 on VM Instance
	'''
	@property
	def receiveuntagged_10_3(self):
		try:
			return self._receiveuntagged_10_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 10/3 on VM Instance
	'''
	@receiveuntagged_10_3.setter
	def receiveuntagged_10_3(self,receiveuntagged_10_3):
		try :
			if not isinstance(receiveuntagged_10_3,bool):
				raise TypeError("receiveuntagged_10_3 must be set to bool value")
			self._receiveuntagged_10_3 = receiveuntagged_10_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/3 on VM Instance
	'''
	@property
	def vlan_10_3(self):
		try:
			return self._vlan_10_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/3 on VM Instance
	'''
	@vlan_10_3.setter
	def vlan_10_3(self,vlan_10_3):
		try :
			if not isinstance(vlan_10_3,int):
				raise TypeError("vlan_10_3 must be set to int value")
			self._vlan_10_3 = vlan_10_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/5 on VM Instance
	'''
	@property
	def vlan_1_5(self):
		try:
			return self._vlan_1_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 1/5 on VM Instance
	'''
	@vlan_1_5.setter
	def vlan_1_5(self,vlan_1_5):
		try :
			if not isinstance(vlan_1_5,int):
				raise TypeError("vlan_1_5 must be set to int value")
			self._vlan_1_5 = vlan_1_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/3 on VM Instance
	'''
	@property
	def if_1_3(self):
		try:
			return self._if_1_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/3 on VM Instance
	'''
	@if_1_3.setter
	def if_1_3(self,if_1_3):
		try :
			if not isinstance(if_1_3,bool):
				raise TypeError("if_1_3 must be set to bool value")
			self._if_1_3 = if_1_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/4 on VM Instance
	'''
	@property
	def if_1_4(self):
		try:
			return self._if_1_4
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/4 on VM Instance
	'''
	@if_1_4.setter
	def if_1_4(self,if_1_4):
		try :
			if not isinstance(if_1_4,bool):
				raise TypeError("if_1_4 must be set to bool value")
			self._if_1_4 = if_1_4
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/5 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_5(self) :
		try:
			return self._vrid_list_ipv4_10_5
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/5 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_5.setter
	def vrid_list_ipv4_10_5(self,vrid_list_ipv4_10_5) :
		try :
			if not isinstance(vrid_list_ipv4_10_5,list):
				raise TypeError("vrid_list_ipv4_10_5 must be set to array of str value")
			for item in vrid_list_ipv4_10_5 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_5 = vrid_list_ipv4_10_5
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/8 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_8(self) :
		try:
			return self._vrid_list_ipv4_10_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/8 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_8.setter
	def vrid_list_ipv4_10_8(self,vrid_list_ipv4_10_8) :
		try :
			if not isinstance(vrid_list_ipv4_10_8,list):
				raise TypeError("vrid_list_ipv4_10_8 must be set to array of str value")
			for item in vrid_list_ipv4_10_8 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_8 = vrid_list_ipv4_10_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/1 on VM Instance
	'''
	@property
	def if_1_1(self):
		try:
			return self._if_1_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/1 on VM Instance
	'''
	@if_1_1.setter
	def if_1_1(self,if_1_1):
		try :
			if not isinstance(if_1_1,bool):
				raise TypeError("if_1_1 must be set to bool value")
			self._if_1_1 = if_1_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/8 on VM Instance
	'''
	@property
	def vlan_10_8(self):
		try:
			return self._vlan_10_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VLAN for Network 10/8 on VM Instance
	'''
	@vlan_10_8.setter
	def vlan_10_8(self,vlan_10_8):
		try :
			if not isinstance(vlan_10_8,int):
				raise TypeError("vlan_10_8 must be set to int value")
			self._vlan_10_8 = vlan_10_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/7 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_7(self) :
		try:
			return self._vrid_list_ipv4_10_7
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/7 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_7.setter
	def vrid_list_ipv4_10_7(self,vrid_list_ipv4_10_7) :
		try :
			if not isinstance(vrid_list_ipv4_10_7,list):
				raise TypeError("vrid_list_ipv4_10_7 must be set to array of str value")
			for item in vrid_list_ipv4_10_7 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_7 = vrid_list_ipv4_10_7
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/3 on VM Instance
	'''
	@property
	def receiveuntagged_1_3(self):
		try:
			return self._receiveuntagged_1_3
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Receive Untagged Packets on 1/3 on VM Instance
	'''
	@receiveuntagged_1_3.setter
	def receiveuntagged_1_3(self,receiveuntagged_1_3):
		try :
			if not isinstance(receiveuntagged_1_3,bool):
				raise TypeError("receiveuntagged_1_3 must be set to bool value")
			self._receiveuntagged_1_3 = receiveuntagged_1_3
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/2 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_2(self) :
		try:
			return self._vrid_list_ipv4_10_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/2 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_2.setter
	def vrid_list_ipv4_10_2(self,vrid_list_ipv4_10_2) :
		try :
			if not isinstance(vrid_list_ipv4_10_2,list):
				raise TypeError("vrid_list_ipv4_10_2 must be set to array of str value")
			for item in vrid_list_ipv4_10_2 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_2 = vrid_list_ipv4_10_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 1/8 on VM Instance
	'''
	@property
	def if_1_8(self):
		try:
			return self._if_1_8
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 1/8 on VM Instance
	'''
	@if_1_8.setter
	def if_1_8(self,if_1_8):
		try :
			if not isinstance(if_1_8,bool):
				raise TypeError("if_1_8 must be set to bool value")
			self._if_1_8 = if_1_8
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/1 for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_10_1(self) :
		try:
			return self._vrid_list_ipv4_10_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/1 for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_10_1.setter
	def vrid_list_ipv4_10_1(self,vrid_list_ipv4_10_1) :
		try :
			if not isinstance(vrid_list_ipv4_10_1,list):
				raise TypeError("vrid_list_ipv4_10_1 must be set to array of str value")
			for item in vrid_list_ipv4_10_1 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_10_1 = vrid_list_ipv4_10_1
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/2 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_2(self) :
		try:
			return self._vrid_list_ipv6_10_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/2 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_2.setter
	def vrid_list_ipv6_10_2(self,vrid_list_ipv6_10_2) :
		try :
			if not isinstance(vrid_list_ipv6_10_2,list):
				raise TypeError("vrid_list_ipv6_10_2 must be set to array of str value")
			for item in vrid_list_ipv6_10_2 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_2 = vrid_list_ipv6_10_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	Network 10/2 on VM Instance
	'''
	@property
	def if_10_2(self):
		try:
			return self._if_10_2
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	Network 10/2 on VM Instance
	'''
	@if_10_2.setter
	def if_10_2(self,if_10_2):
		try :
			if not isinstance(if_10_2,bool):
				raise TypeError("if_10_2 must be set to bool value")
			self._if_10_2 = if_10_2
		except Exception as e :
			raise e

	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/1 for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_10_1(self) :
		try:
			return self._vrid_list_ipv6_10_1
		except Exception as e :
			raise e
	'''
	This property is deprecated by network_interfaces
	VRID List for Interface 10/1 for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_10_1.setter
	def vrid_list_ipv6_10_1(self,vrid_list_ipv6_10_1) :
		try :
			if not isinstance(vrid_list_ipv6_10_1,list):
				raise TypeError("vrid_list_ipv6_10_1 must be set to array of str value")
			for item in vrid_list_ipv6_10_1 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_10_1 = vrid_list_ipv6_10_1
		except Exception as e :
			raise e

	'''
	Use this operation to get VM Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vm_device_obj=vm_device()
				response = vm_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vm_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._filter=filter_
			return vm_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vm_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._count=True
			response = vm_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vm_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vm_device_obj = vm_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vm_device_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vm_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vm_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vm_device_responses, response, "vm_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vm_device_response_array
				i=0
				error = [vm_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vm_device_response_array
			i=0
			vm_device_objs = [vm_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vm_device'):
					for props in obj._vm_device:
						result = service.payload_formatter.string_to_bulk_resource(vm_device_response,self.__class__.__name__,props)
						vm_device_objs[i] = result.vm_device
						i=i+1
			return vm_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vm_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vm_device_response(base_response):
	def __init__(self,length=1) :
		self.vm_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vm_device= [ vm_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vm_device_responses(base_response):
	def __init__(self,length=1) :
		self.vm_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vm_device_response_array = [ vm_device() for _ in range(length)]
