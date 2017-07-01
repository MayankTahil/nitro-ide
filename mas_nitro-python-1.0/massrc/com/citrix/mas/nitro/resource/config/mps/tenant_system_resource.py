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
Configuration for System Resources available for a tenant resource
'''

class tenant_system_resource(base_resource):
	_available_disk_size= ""
	_max_plt_bw= ""
	_max_pps= ""
	_available_std_bw= ""
	_max_cpu_cores= ""
	_parent_id= ""
	_available_pps= ""
	_tenant_id= ""
	_max_disk_size= ""
	_available_throughput= ""
	_max_instances= ""
	_id= ""
	_parent_name= ""
	_available_instances= ""
	_max_throughput= ""
	_max_std_bw= ""
	_available_ent_bw= ""
	_max_memory= ""
	_max_ent_bw= ""
	_available_ssl_cards= ""
	_available_memory= ""
	_max_ssl_cards= ""
	_available_plt_bw= ""
	_available_cpu_cores= ""
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
			return "tenant_system_resource"
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
			return "tenant_system_resources"
		except Exception as e :
			raise e



	'''
	get Available disk size
	'''
	@property
	def available_disk_size(self) :
		try:
			return self._available_disk_size
		except Exception as e :
			raise e
	'''
	set Available disk size
	'''
	@available_disk_size.setter
	def available_disk_size(self,available_disk_size):
		try :
			if not isinstance(available_disk_size,float):
				raise TypeError("available_disk_size must be set to float value")
			self._available_disk_size = available_disk_size
		except Exception as e :
			raise e


	'''
	get Max Allowed Platinum bandwidth Mbps
	'''
	@property
	def max_plt_bw(self) :
		try:
			return self._max_plt_bw
		except Exception as e :
			raise e
	'''
	set Max Allowed Platinum bandwidth Mbps
	'''
	@max_plt_bw.setter
	def max_plt_bw(self,max_plt_bw):
		try :
			if not isinstance(max_plt_bw,int):
				raise TypeError("max_plt_bw must be set to int value")
			self._max_plt_bw = max_plt_bw
		except Exception as e :
			raise e


	'''
	get Maximum PPS 
	'''
	@property
	def max_pps(self) :
		try:
			return self._max_pps
		except Exception as e :
			raise e


	'''
	get Available Standard bandwidth in Mbps
	'''
	@property
	def available_std_bw(self) :
		try:
			return self._available_std_bw
		except Exception as e :
			raise e


	'''
	get Maximum number of CPU Cores
	'''
	@property
	def max_cpu_cores(self) :
		try:
			return self._max_cpu_cores
		except Exception as e :
			raise e
	'''
	set Maximum number of CPU Cores
	'''
	@max_cpu_cores.setter
	def max_cpu_cores(self,max_cpu_cores):
		try :
			if not isinstance(max_cpu_cores,int):
				raise TypeError("max_cpu_cores must be set to int value")
			self._max_cpu_cores = max_cpu_cores
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
	get Available PPS
	'''
	@property
	def available_pps(self) :
		try:
			return self._available_pps
		except Exception as e :
			raise e


	'''
	get Id of the parent tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of the parent tenant
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Maximum Disk Space
	'''
	@property
	def max_disk_size(self) :
		try:
			return self._max_disk_size
		except Exception as e :
			raise e
	'''
	set Maximum Disk Space
	'''
	@max_disk_size.setter
	def max_disk_size(self,max_disk_size):
		try :
			if not isinstance(max_disk_size,float):
				raise TypeError("max_disk_size must be set to float value")
			self._max_disk_size = max_disk_size
		except Exception as e :
			raise e


	'''
	get Available Throughput in Mbps
	'''
	@property
	def available_throughput(self) :
		try:
			return self._available_throughput
		except Exception as e :
			raise e


	'''
	get Maximum number of Instances
	'''
	@property
	def max_instances(self) :
		try:
			return self._max_instances
		except Exception as e :
			raise e
	'''
	set Maximum number of Instances
	'''
	@max_instances.setter
	def max_instances(self,max_instances):
		try :
			if not isinstance(max_instances,int):
				raise TypeError("max_instances must be set to int value")
			self._max_instances = max_instances
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
	get Available number of CPU Cores
	'''
	@property
	def available_instances(self) :
		try:
			return self._available_instances
		except Exception as e :
			raise e
	'''
	set Available number of CPU Cores
	'''
	@available_instances.setter
	def available_instances(self,available_instances):
		try :
			if not isinstance(available_instances,int):
				raise TypeError("available_instances must be set to int value")
			self._available_instances = available_instances
		except Exception as e :
			raise e


	'''
	get Maximum Throughput in Mbps
	'''
	@property
	def max_throughput(self) :
		try:
			return self._max_throughput
		except Exception as e :
			raise e


	'''
	get Max Allowed Standard bandwidth Mbps
	'''
	@property
	def max_std_bw(self) :
		try:
			return self._max_std_bw
		except Exception as e :
			raise e
	'''
	set Max Allowed Standard bandwidth Mbps
	'''
	@max_std_bw.setter
	def max_std_bw(self,max_std_bw):
		try :
			if not isinstance(max_std_bw,int):
				raise TypeError("max_std_bw must be set to int value")
			self._max_std_bw = max_std_bw
		except Exception as e :
			raise e


	'''
	get Available Enterprise bandwidth in Mbps
	'''
	@property
	def available_ent_bw(self) :
		try:
			return self._available_ent_bw
		except Exception as e :
			raise e


	'''
	get Maximum Memory
	'''
	@property
	def max_memory(self) :
		try:
			return self._max_memory
		except Exception as e :
			raise e
	'''
	set Maximum Memory
	'''
	@max_memory.setter
	def max_memory(self,max_memory):
		try :
			if not isinstance(max_memory,float):
				raise TypeError("max_memory must be set to float value")
			self._max_memory = max_memory
		except Exception as e :
			raise e


	'''
	get Max Allowed Enterprise bandwidth Mbps
	'''
	@property
	def max_ent_bw(self) :
		try:
			return self._max_ent_bw
		except Exception as e :
			raise e
	'''
	set Max Allowed Enterprise bandwidth Mbps
	'''
	@max_ent_bw.setter
	def max_ent_bw(self,max_ent_bw):
		try :
			if not isinstance(max_ent_bw,int):
				raise TypeError("max_ent_bw must be set to int value")
			self._max_ent_bw = max_ent_bw
		except Exception as e :
			raise e


	'''
	get Available number of SSL Cores
	'''
	@property
	def available_ssl_cards(self) :
		try:
			return self._available_ssl_cards
		except Exception as e :
			raise e
	'''
	set Available number of SSL Cores
	'''
	@available_ssl_cards.setter
	def available_ssl_cards(self,available_ssl_cards):
		try :
			if not isinstance(available_ssl_cards,int):
				raise TypeError("available_ssl_cards must be set to int value")
			self._available_ssl_cards = available_ssl_cards
		except Exception as e :
			raise e


	'''
	get Available number of CPU Cores
	'''
	@property
	def available_memory(self) :
		try:
			return self._available_memory
		except Exception as e :
			raise e
	'''
	set Available number of CPU Cores
	'''
	@available_memory.setter
	def available_memory(self,available_memory):
		try :
			if not isinstance(available_memory,float):
				raise TypeError("available_memory must be set to float value")
			self._available_memory = available_memory
		except Exception as e :
			raise e


	'''
	get Available number of CPU Cores
	'''
	@property
	def max_ssl_cards(self) :
		try:
			return self._max_ssl_cards
		except Exception as e :
			raise e
	'''
	set Available number of CPU Cores
	'''
	@max_ssl_cards.setter
	def max_ssl_cards(self,max_ssl_cards):
		try :
			if not isinstance(max_ssl_cards,int):
				raise TypeError("max_ssl_cards must be set to int value")
			self._max_ssl_cards = max_ssl_cards
		except Exception as e :
			raise e


	'''
	get Available Platinum bandwidth in Mbps
	'''
	@property
	def available_plt_bw(self) :
		try:
			return self._available_plt_bw
		except Exception as e :
			raise e


	'''
	get Available number of CPU Cores
	'''
	@property
	def available_cpu_cores(self) :
		try:
			return self._available_cpu_cores
		except Exception as e :
			raise e
	'''
	set Available number of CPU Cores
	'''
	@available_cpu_cores.setter
	def available_cpu_cores(self,available_cpu_cores):
		try :
			if not isinstance(available_cpu_cores,int):
				raise TypeError("available_cpu_cores must be set to int value")
			self._available_cpu_cores = available_cpu_cores
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_system_resource_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_system_resource
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_system_resource_responses, response, "tenant_system_resource_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_system_resource_response_array
				i=0
				error = [tenant_system_resource() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_system_resource_response_array
			i=0
			tenant_system_resource_objs = [tenant_system_resource() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_system_resource'):
					for props in obj._tenant_system_resource:
						result = service.payload_formatter.string_to_bulk_resource(tenant_system_resource_response,self.__class__.__name__,props)
						tenant_system_resource_objs[i] = result.tenant_system_resource
						i=i+1
			return tenant_system_resource_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_system_resource,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_system_resource_response(base_response):
	def __init__(self,length=1) :
		self.tenant_system_resource= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_system_resource= [ tenant_system_resource() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_system_resource_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_system_resource_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_system_resource_response_array = [ tenant_system_resource() for _ in range(length)]
