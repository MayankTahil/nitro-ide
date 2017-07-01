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
Configuration for SDX Formation Network resource
'''

class sdx_formation_network(base_resource):
	_network_iprange= ""
	_port_name= ""
	_name= ""
	_network_type= ""
	_description= ""
	_vlan= ""
	_interface_type= ""
	_traffic_load= ""
	_traffic_type= ""
	_formation_instance_id= ""
	_id= ""
	_networkpool= ""
	_vlan_whitelist= ""
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
			return "sdx_formation_network"
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
			return "sdx_formation_networks"
		except Exception as e :
			raise e



	'''
	get Network IP Range (In X.Y.*.* or StartIP-EndIP Format)
	'''
	@property
	def network_iprange(self) :
		try:
			return self._network_iprange
		except Exception as e :
			raise e
	'''
	set Network IP Range (In X.Y.*.* or StartIP-EndIP Format)
	'''
	@network_iprange.setter
	def network_iprange(self,network_iprange):
		try :
			if not isinstance(network_iprange,str):
				raise TypeError("network_iprange must be set to str value")
			self._network_iprange = network_iprange
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
	get SDX Formation Network Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set SDX Formation Network Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Network Type (External / Internal)
	'''
	@property
	def network_type(self) :
		try:
			return self._network_type
		except Exception as e :
			raise e
	'''
	set Network Type (External / Internal)
	'''
	@network_type.setter
	def network_type(self,network_type):
		try :
			if not isinstance(network_type,str):
				raise TypeError("network_type must be set to str value")
			self._network_type = network_type
		except Exception as e :
			raise e


	'''
	get Description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get VLAN Id of this Network
	'''
	@property
	def vlan(self) :
		try:
			return self._vlan
		except Exception as e :
			raise e
	'''
	set VLAN Id of this Network
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
	get Interface Type, SRIOV or PV
	'''
	@property
	def interface_type(self) :
		try:
			return self._interface_type
		except Exception as e :
			raise e
	'''
	set Interface Type, SRIOV or PV
	'''
	@interface_type.setter
	def interface_type(self,interface_type):
		try :
			if not isinstance(interface_type,int):
				raise TypeError("interface_type must be set to int value")
			self._interface_type = interface_type
		except Exception as e :
			raise e


	'''
	get Traffic Load (low / high)
	'''
	@property
	def traffic_load(self) :
		try:
			return self._traffic_load
		except Exception as e :
			raise e
	'''
	set Traffic Load (low / high)
	'''
	@traffic_load.setter
	def traffic_load(self,traffic_load):
		try :
			if not isinstance(traffic_load,str):
				raise TypeError("traffic_load must be set to str value")
			self._traffic_load = traffic_load
		except Exception as e :
			raise e


	'''
	get Traffic Type (Data / Management)
	'''
	@property
	def traffic_type(self) :
		try:
			return self._traffic_type
		except Exception as e :
			raise e
	'''
	set Traffic Type (Data / Management)
	'''
	@traffic_type.setter
	def traffic_type(self,traffic_type):
		try :
			if not isinstance(traffic_type,str):
				raise TypeError("traffic_type must be set to str value")
			self._traffic_type = traffic_type
		except Exception as e :
			raise e


	'''
	get Formation Instance Id that this Network is Part of
	'''
	@property
	def formation_instance_id(self) :
		try:
			return self._formation_instance_id
		except Exception as e :
			raise e
	'''
	set Formation Instance Id that this Network is Part of
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
	get Id is system generated key for all the sdx formation networks
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sdx formation networks
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
	get SDX Formation Network Name
	'''
	@property
	def networkpool(self) :
		try:
			return self._networkpool
		except Exception as e :
			raise e
	'''
	set SDX Formation Network Name
	'''
	@networkpool.setter
	def networkpool(self,networkpool):
		try :
			if not isinstance(networkpool,str):
				raise TypeError("networkpool must be set to str value")
			self._networkpool = networkpool
		except Exception as e :
			raise e


	'''
	get VLAN Whitelist for SDX Formation Network
	'''
	@property
	def vlan_whitelist(self) :
		try:
			return self._vlan_whitelist
		except Exception as e :
			raise e
	'''
	set VLAN Whitelist for SDX Formation Network
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
	Use this operation to get the network pool.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_formation_network_obj=sdx_formation_network()
				response = sdx_formation_network_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_formation_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_formation_network_obj = sdx_formation_network()
			option_ = options()
			option_._filter=filter_
			return sdx_formation_network_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_formation_network resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_formation_network_obj = sdx_formation_network()
			option_ = options()
			option_._count=True
			response = sdx_formation_network_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_formation_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_formation_network_obj = sdx_formation_network()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_formation_network_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_formation_network_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_formation_network
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_formation_network_responses, response, "sdx_formation_network_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_formation_network_response_array
				i=0
				error = [sdx_formation_network() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_formation_network_response_array
			i=0
			sdx_formation_network_objs = [sdx_formation_network() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_formation_network'):
					for props in obj._sdx_formation_network:
						result = service.payload_formatter.string_to_bulk_resource(sdx_formation_network_response,self.__class__.__name__,props)
						sdx_formation_network_objs[i] = result.sdx_formation_network
						i=i+1
			return sdx_formation_network_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_formation_network,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_formation_network_response(base_response):
	def __init__(self,length=1) :
		self.sdx_formation_network= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_formation_network= [ sdx_formation_network() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_formation_network_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_formation_network_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_formation_network_response_array = [ sdx_formation_network() for _ in range(length)]
