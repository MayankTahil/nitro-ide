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
Configuration for Network Service Resource Profile resource
'''

class network_service_resource_profile(base_resource):
	_parent_name= ""
	_name= ""
	_number_of_vcpu= ""
	_parent_id= ""
	_memory= ""
	_formation_template_id= ""
	_number_of_ssl_cores= ""
	_memory_unit= ""
	_storage_unit= ""
	_id= ""
	_storage= ""
	_storage_type= ""
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
			return "network_service_resource_profile"
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
			return "network_service_resource_profiles"
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
	get Number of Virtual CPUs/Cores
	'''
	@property
	def number_of_vcpu(self) :
		try:
			return self._number_of_vcpu
		except Exception as e :
			raise e
	'''
	set Number of Virtual CPUs/Cores
	'''
	@number_of_vcpu.setter
	def number_of_vcpu(self,number_of_vcpu):
		try :
			if not isinstance(number_of_vcpu,int):
				raise TypeError("number_of_vcpu must be set to int value")
			self._number_of_vcpu = number_of_vcpu
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
	get memory
	'''
	@property
	def memory(self) :
		try:
			return self._memory
		except Exception as e :
			raise e
	'''
	set memory
	'''
	@memory.setter
	def memory(self,memory):
		try :
			if not isinstance(memory,int):
				raise TypeError("memory must be set to int value")
			self._memory = memory
		except Exception as e :
			raise e


	'''
	get Formation Template ID
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set Formation Template ID
	'''
	@formation_template_id.setter
	def formation_template_id(self,formation_template_id):
		try :
			if not isinstance(formation_template_id,str):
				raise TypeError("formation_template_id must be set to str value")
			self._formation_template_id = formation_template_id
		except Exception as e :
			raise e


	'''
	get number_of_ssl_cores
	'''
	@property
	def number_of_ssl_cores(self) :
		try:
			return self._number_of_ssl_cores
		except Exception as e :
			raise e
	'''
	set number_of_ssl_cores
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
	get memory unit
	'''
	@property
	def memory_unit(self) :
		try:
			return self._memory_unit
		except Exception as e :
			raise e
	'''
	set memory unit
	'''
	@memory_unit.setter
	def memory_unit(self,memory_unit):
		try :
			if not isinstance(memory_unit,str):
				raise TypeError("memory_unit must be set to str value")
			self._memory_unit = memory_unit
		except Exception as e :
			raise e


	'''
	get storage unit
	'''
	@property
	def storage_unit(self) :
		try:
			return self._storage_unit
		except Exception as e :
			raise e
	'''
	set storage unit
	'''
	@storage_unit.setter
	def storage_unit(self,storage_unit):
		try :
			if not isinstance(storage_unit,str):
				raise TypeError("storage_unit must be set to str value")
			self._storage_unit = storage_unit
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the resource profile
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the resource profile
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
	get storage, comma separated
	'''
	@property
	def storage(self) :
		try:
			return self._storage
		except Exception as e :
			raise e
	'''
	set storage, comma separated
	'''
	@storage.setter
	def storage(self,storage):
		try :
			if not isinstance(storage,str):
				raise TypeError("storage must be set to str value")
			self._storage = storage
		except Exception as e :
			raise e


	'''
	get storage type HDD/SSD
	'''
	@property
	def storage_type(self) :
		try:
			return self._storage_type
		except Exception as e :
			raise e
	'''
	set storage type HDD/SSD
	'''
	@storage_type.setter
	def storage_type(self,storage_type):
		try :
			if not isinstance(storage_type,str):
				raise TypeError("storage_type must be set to str value")
			self._storage_type = storage_type
		except Exception as e :
			raise e

	'''
	Use this operation to get the network service resource profiles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_service_resource_profile_obj=network_service_resource_profile()
				response = network_service_resource_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_service_resource_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_service_resource_profile_obj = network_service_resource_profile()
			option_ = options()
			option_._filter=filter_
			return network_service_resource_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_service_resource_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_service_resource_profile_obj = network_service_resource_profile()
			option_ = options()
			option_._count=True
			response = network_service_resource_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_service_resource_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_service_resource_profile_obj = network_service_resource_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_service_resource_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_service_resource_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_service_resource_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_service_resource_profile_responses, response, "network_service_resource_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_service_resource_profile_response_array
				i=0
				error = [network_service_resource_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_service_resource_profile_response_array
			i=0
			network_service_resource_profile_objs = [network_service_resource_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_service_resource_profile'):
					for props in obj._network_service_resource_profile:
						result = service.payload_formatter.string_to_bulk_resource(network_service_resource_profile_response,self.__class__.__name__,props)
						network_service_resource_profile_objs[i] = result.network_service_resource_profile
						i=i+1
			return network_service_resource_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_service_resource_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_service_resource_profile_response(base_response):
	def __init__(self,length=1) :
		self.network_service_resource_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_service_resource_profile= [ network_service_resource_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_service_resource_profile_responses(base_response):
	def __init__(self,length=1) :
		self.network_service_resource_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_service_resource_profile_response_array = [ network_service_resource_profile() for _ in range(length)]
