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


'''
Configuration for VM device network interface resource
'''

class network_interface(base_resource):
	_device_channel_name= ""
	_is_mgmt_ifc= ""
	_name_server= ""
	_vrid_list_ipv6= ""
	_gateway= ""
	_xen_vf_index= ""
	_parent_id= ""
	_vrid_list_ipv4= ""
	_is_member_ifc= ""
	_mac_address= ""
	_l2_enabled= ""
	_id= ""
	_ip_address= ""
	_netmask= ""
	_port_name= ""
	_parent_name= ""
	_mac_mode= ""
	_managed_device_id= ""
	_vlan= ""
	_receiveuntagged= ""
	_sdx_formation_network_id= ""
	_vlan_whitelist= ""
	_interface_name= ""
	_vrid_list_ipv4_array=[]
	_vrid_list_ipv6_array=[]
	_vlan_whitelist_array=[]
	_is_vlan_applied= ""
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
			return "network_interface"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "network_interfaces"
		except Exception as e :
			raise e



	'''
	get LA Name on the actual VM
	'''
	@property
	def device_channel_name(self) :
		try:
			return self._device_channel_name
		except Exception as e :
			raise e


	'''
	get True if this is the management interface
	'''
	@property
	def is_mgmt_ifc(self) :
		try:
			return self._is_mgmt_ifc
		except Exception as e :
			raise e
	'''
	set True if this is the management interface
	'''
	@is_mgmt_ifc.setter
	def is_mgmt_ifc(self,is_mgmt_ifc):
		try :
			if not isinstance(is_mgmt_ifc,bool):
				raise TypeError("is_mgmt_ifc must be set to bool value")
			self._is_mgmt_ifc = is_mgmt_ifc
		except Exception as e :
			raise e


	'''
	get Name Server
	'''
	@property
	def name_server(self) :
		try:
			return self._name_server
		except Exception as e :
			raise e
	'''
	set Name Server
	'''
	@name_server.setter
	def name_server(self,name_server):
		try :
			if not isinstance(name_server,str):
				raise TypeError("name_server must be set to str value")
			self._name_server = name_server
		except Exception as e :
			raise e


	'''
	get VRID List for Interface/Channel for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6(self) :
		try:
			return self._vrid_list_ipv6
		except Exception as e :
			raise e
	'''
	set VRID List for Interface/Channel for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6.setter
	def vrid_list_ipv6(self,vrid_list_ipv6):
		try :
			if not isinstance(vrid_list_ipv6,str):
				raise TypeError("vrid_list_ipv6 must be set to str value")
			self._vrid_list_ipv6 = vrid_list_ipv6
		except Exception as e :
			raise e


	'''
	get gateway
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set gateway
	'''
	@gateway.setter
	def gateway(self,gateway):
		try :
			if not isinstance(gateway,str):
				raise TypeError("gateway must be set to str value")
			self._gateway = gateway
		except Exception as e :
			raise e


	'''
	get Index given by Xen when assigning free virtual function
	'''
	@property
	def xen_vf_index(self) :
		try:
			return self._xen_vf_index
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get VRID List for Interface/Channel for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4(self) :
		try:
			return self._vrid_list_ipv4
		except Exception as e :
			raise e
	'''
	set VRID List for Interface/Channel for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4.setter
	def vrid_list_ipv4(self,vrid_list_ipv4):
		try :
			if not isinstance(vrid_list_ipv4,str):
				raise TypeError("vrid_list_ipv4 must be set to str value")
			self._vrid_list_ipv4 = vrid_list_ipv4
		except Exception as e :
			raise e


	'''
	get True if this interface is member of a channel
	'''
	@property
	def is_member_ifc(self) :
		try:
			return self._is_member_ifc
		except Exception as e :
			raise e
	'''
	set True if this interface is member of a channel
	'''
	@is_member_ifc.setter
	def is_member_ifc(self,is_member_ifc):
		try :
			if not isinstance(is_member_ifc,bool):
				raise TypeError("is_member_ifc must be set to bool value")
			self._is_member_ifc = is_member_ifc
		except Exception as e :
			raise e


	'''
	get Mac Address
	'''
	@property
	def mac_address(self) :
		try:
			return self._mac_address
		except Exception as e :
			raise e
	'''
	set Mac Address
	'''
	@mac_address.setter
	def mac_address(self,mac_address):
		try :
			if not isinstance(mac_address,str):
				raise TypeError("mac_address must be set to str value")
			self._mac_address = mac_address
		except Exception as e :
			raise e


	'''
	get L2 mode status of Interface
	'''
	@property
	def l2_enabled(self) :
		try:
			return self._l2_enabled
		except Exception as e :
			raise e
	'''
	set L2 mode status of Interface
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
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get netmask
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set netmask
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Port name of the interface on the host machine
	'''
	@property
	def port_name(self) :
		try:
			return self._port_name
		except Exception as e :
			raise e
	'''
	set Port name of the interface on the host machine
	'''
	@port_name.setter
	def port_name(self,port_name):
		try :
			if not isinstance(port_name,str):
				raise TypeError("port_name must be set to str value")
			self._port_name = port_name
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Mac Mode, default for XenServer generated, generated for SVM generated, custom for User assigned
	'''
	@property
	def mac_mode(self) :
		try:
			return self._mac_mode
		except Exception as e :
			raise e
	'''
	set Mac Mode, default for XenServer generated, generated for SVM generated, custom for User assigned
	'''
	@mac_mode.setter
	def mac_mode(self,mac_mode):
		try :
			if not isinstance(mac_mode,str):
				raise TypeError("mac_mode must be set to str value")
			self._mac_mode = mac_mode
		except Exception as e :
			raise e


	'''
	get managed_device_id
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e
	'''
	set managed_device_id
	'''
	@managed_device_id.setter
	def managed_device_id(self,managed_device_id):
		try :
			if not isinstance(managed_device_id,str):
				raise TypeError("managed_device_id must be set to str value")
			self._managed_device_id = managed_device_id
		except Exception as e :
			raise e


	'''
	This property is not supported.Use vlan_whitelist for vlan configuration
	get VLAN Id
	'''
	@property
	def vlan(self) :
		try:
			return self._vlan
		except Exception as e :
			raise e
	'''
	This property is not supported.Use vlan_whitelist for vlan configuration
	set VLAN Id
	'''
	@vlan.setter
	def vlan(self,vlan):
		try :
			if not isinstance(vlan,int):
				raise TypeError("vlan must be set to int value")
			self._vlan = vlan
		except Exception as e :
			raise e


	'''
	get Receive Untagged Packets on Interface/Channel
	'''
	@property
	def receiveuntagged(self) :
		try:
			return self._receiveuntagged
		except Exception as e :
			raise e
	'''
	set Receive Untagged Packets on Interface/Channel
	'''
	@receiveuntagged.setter
	def receiveuntagged(self,receiveuntagged):
		try :
			if not isinstance(receiveuntagged,bool):
				raise TypeError("receiveuntagged must be set to bool value")
			self._receiveuntagged = receiveuntagged
		except Exception as e :
			raise e


	'''
	get SDX Formation Network Id of which this Interface is part of
	'''
	@property
	def sdx_formation_network_id(self) :
		try:
			return self._sdx_formation_network_id
		except Exception as e :
			raise e
	'''
	set SDX Formation Network Id of which this Interface is part of
	'''
	@sdx_formation_network_id.setter
	def sdx_formation_network_id(self,sdx_formation_network_id):
		try :
			if not isinstance(sdx_formation_network_id,str):
				raise TypeError("sdx_formation_network_id must be set to str value")
			self._sdx_formation_network_id = sdx_formation_network_id
		except Exception as e :
			raise e


	'''
	get VLAN Whitelist for Interface/Channel on VM Instance
	'''
	@property
	def vlan_whitelist(self) :
		try:
			return self._vlan_whitelist
		except Exception as e :
			raise e
	'''
	set VLAN Whitelist for Interface/Channel on VM Instance
	'''
	@vlan_whitelist.setter
	def vlan_whitelist(self,vlan_whitelist):
		try :
			if not isinstance(vlan_whitelist,str):
				raise TypeError("vlan_whitelist must be set to str value")
			self._vlan_whitelist = vlan_whitelist
		except Exception as e :
			raise e

	'''
	Name of this interface
	'''
	@property
	def interface_name(self):
		try:
			return self._interface_name
		except Exception as e :
			raise e
	'''
	Name of this interface
	'''
	@interface_name.setter
	def interface_name(self,interface_name):
		try :
			if not isinstance(interface_name,str):
				raise TypeError("interface_name must be set to str value")
			self._interface_name = interface_name
		except Exception as e :
			raise e

	'''
	VRID List for Interface for IPV4 VMAC Generation
	'''
	@property
	def vrid_list_ipv4_array(self) :
		try:
			return self._vrid_list_ipv4_array
		except Exception as e :
			raise e
	'''
	VRID List for Interface for IPV4 VMAC Generation
	'''
	@vrid_list_ipv4_array.setter
	def vrid_list_ipv4_array(self,vrid_list_ipv4_array) :
		try :
			if not isinstance(vrid_list_ipv4_array,list):
				raise TypeError("vrid_list_ipv4_array must be set to array of str value")
			for item in vrid_list_ipv4_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv4_array = vrid_list_ipv4_array
		except Exception as e :
			raise e

	'''
	VRID List for Interface for IPV6 VMAC Generation
	'''
	@property
	def vrid_list_ipv6_array(self) :
		try:
			return self._vrid_list_ipv6_array
		except Exception as e :
			raise e
	'''
	VRID List for Interface for IPV6 VMAC Generation
	'''
	@vrid_list_ipv6_array.setter
	def vrid_list_ipv6_array(self,vrid_list_ipv6_array) :
		try :
			if not isinstance(vrid_list_ipv6_array,list):
				raise TypeError("vrid_list_ipv6_array must be set to array of str value")
			for item in vrid_list_ipv6_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vrid_list_ipv6_array = vrid_list_ipv6_array
		except Exception as e :
			raise e

	'''
	VLAN Whitelist for Interface on VM Instance
	'''
	@property
	def vlan_whitelist_array(self) :
		try:
			return self._vlan_whitelist_array
		except Exception as e :
			raise e
	'''
	VLAN Whitelist for Interface on VM Instance
	'''
	@vlan_whitelist_array.setter
	def vlan_whitelist_array(self,vlan_whitelist_array) :
		try :
			if not isinstance(vlan_whitelist_array,list):
				raise TypeError("vlan_whitelist_array must be set to array of str value")
			for item in vlan_whitelist_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vlan_whitelist_array = vlan_whitelist_array
		except Exception as e :
			raise e

	'''
	Is VLAN added on NetworkInterface of VM Instance
	'''
	@property
	def is_vlan_applied(self):
		try:
			return self._is_vlan_applied
		except Exception as e :
			raise e
	'''
	Is VLAN added on NetworkInterface of VM Instance
	'''
	@is_vlan_applied.setter
	def is_vlan_applied(self,is_vlan_applied):
		try :
			if not isinstance(is_vlan_applied,bool):
				raise TypeError("is_vlan_applied must be set to bool value")
			self._is_vlan_applied = is_vlan_applied
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_interface_obj = network_interface()
			option_ = options()
			option_._filter=filter_
			return network_interface_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_interface resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_interface_obj = network_interface()
			option_ = options()
			option_._count=True
			response = network_interface_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_interface_obj = network_interface()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_interface_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_interface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_interface
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_interface_responses, response, "network_interface_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_interface_response_array
				i=0
				error = [network_interface() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_interface_response_array
			i=0
			network_interface_objs = [network_interface() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_interface'):
					for props in obj._network_interface:
						result = service.payload_formatter.string_to_bulk_resource(network_interface_response,self.__class__.__name__,props)
						network_interface_objs[i] = result.network_interface
						i=i+1
			return network_interface_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_interface,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_interface_response(base_response):
	def __init__(self,length=1) :
		self.network_interface= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_interface= [ network_interface() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_interface_responses(base_response):
	def __init__(self,length=1) :
		self.network_interface_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_interface_response_array = [ network_interface() for _ in range(length)]
