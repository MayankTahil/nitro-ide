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


'''
Configuration for SDX Network Service resource
'''

class sdx_network_service(base_resource):
	_gateway= ""
	_network_interfaces=[]
	_uuid= ""
	_vm_memory_total= ""
	_disk_allocation= ""
	_id= ""
	_ip_address= ""
	_netmask= ""
	_instance_state= ""
	_number_of_cores= ""
	_name= ""
	_disk_space= ""
	_description= ""
	_formation_instance_id= ""
	_number_of_ssl_cores= ""
	_type= ""
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
			return "sdx_network_service"
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
			return "sdx_network_services"
		except Exception as e :
			raise e



	'''
	get Default Gateway of managed device
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set Default Gateway of managed device
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
	get Disk allocation for VM Instance
	'''
	@property
	def disk_allocation(self) :
		try:
			return self._disk_allocation
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the SDX Network Services
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the SDX Network Services
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
	get IP Address for this managed device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for this managed device
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
	get Netmask of managed device
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set Netmask of managed device
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
	get State of device, UP only if device accessible
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
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
	get Network Service Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Network Service Name
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
	get Show Disk Space (GB) available to VM Instance
	'''
	@property
	def disk_space(self) :
		try:
			return self._disk_space
		except Exception as e :
			raise e


	'''
	get description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set description
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
	get Formation Instance Id
	'''
	@property
	def formation_instance_id(self) :
		try:
			return self._formation_instance_id
		except Exception as e :
			raise e
	'''
	set Formation Instance Id
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
	get Service Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Service Type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e

	'''
	Use this operation to get the SDX Network Services.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_network_service_obj=sdx_network_service()
				response = sdx_network_service_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_network_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_network_service_obj = sdx_network_service()
			option_ = options()
			option_._filter=filter_
			return sdx_network_service_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_network_service resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_network_service_obj = sdx_network_service()
			option_ = options()
			option_._count=True
			response = sdx_network_service_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_network_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_network_service_obj = sdx_network_service()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_network_service_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_network_service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_network_service
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_network_service_responses, response, "sdx_network_service_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_network_service_response_array
				i=0
				error = [sdx_network_service() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_network_service_response_array
			i=0
			sdx_network_service_objs = [sdx_network_service() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_network_service'):
					for props in obj._sdx_network_service:
						result = service.payload_formatter.string_to_bulk_resource(sdx_network_service_response,self.__class__.__name__,props)
						sdx_network_service_objs[i] = result.sdx_network_service
						i=i+1
			return sdx_network_service_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_network_service,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_network_service_response(base_response):
	def __init__(self,length=1) :
		self.sdx_network_service= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_network_service= [ sdx_network_service() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_network_service_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_network_service_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_network_service_response_array = [ sdx_network_service() for _ in range(length)]
