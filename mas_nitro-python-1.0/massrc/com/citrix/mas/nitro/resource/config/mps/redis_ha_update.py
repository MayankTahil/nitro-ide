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
Configuration for Redis Publishing resource
'''

class redis_ha_update(base_resource):
	_tenant_name= ""
	_device_ids=[]
	_device_names=[]
	_operation= ""
	_device_ip_addresses=[]
	_group_list=[]
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
			return "redis_ha_update"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "redis_ha_updates"
		except Exception as e :
			raise e



	'''
	get Tenant Name of user who has added/removed a device
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name of user who has added/removed a device
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get Array of device ids to be updated
	'''
	@property
	def device_ids(self) :
		try:
			return self._device_ids
		except Exception as e :
			raise e
	'''
	set Array of device ids to be updated
	'''
	@device_ids.setter
	def device_ids(self,device_ids) :
		try :
			if not isinstance(device_ids,list):
				raise TypeError("device_ids must be set to array of str value")
			for item in device_ids :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_ids = device_ids
		except Exception as e :
			raise e


	'''
	get Array of device names to be updated
	'''
	@property
	def device_names(self) :
		try:
			return self._device_names
		except Exception as e :
			raise e
	'''
	set Array of device names to be updated
	'''
	@device_names.setter
	def device_names(self,device_names) :
		try :
			if not isinstance(device_names,list):
				raise TypeError("device_names must be set to array of str value")
			for item in device_names :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_names = device_names
		except Exception as e :
			raise e


	'''
	get Whether to add or remove a device
	'''
	@property
	def operation(self) :
		try:
			return self._operation
		except Exception as e :
			raise e
	'''
	set Whether to add or remove a device
	'''
	@operation.setter
	def operation(self,operation):
		try :
			if not isinstance(operation,str):
				raise TypeError("operation must be set to str value")
			self._operation = operation
		except Exception as e :
			raise e


	'''
	get Array of device ip addresses to be updated
	'''
	@property
	def device_ip_addresses(self) :
		try:
			return self._device_ip_addresses
		except Exception as e :
			raise e
	'''
	set Array of device ip addresses to be updated
	'''
	@device_ip_addresses.setter
	def device_ip_addresses(self,device_ip_addresses) :
		try :
			if not isinstance(device_ip_addresses,list):
				raise TypeError("device_ip_addresses must be set to array of str value")
			for item in device_ip_addresses :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_ip_addresses = device_ip_addresses
		except Exception as e :
			raise e


	'''
	get Array of groups to which the user belongs
	'''
	@property
	def group_list(self) :
		try:
			return self._group_list
		except Exception as e :
			raise e
	'''
	set Array of groups to which the user belongs
	'''
	@group_list.setter
	def group_list(self,group_list) :
		try :
			if not isinstance(group_list,list):
				raise TypeError("group_list must be set to array of str value")
			for item in group_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._group_list = group_list
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(redis_ha_update_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.redis_ha_update
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(redis_ha_update_responses, response, "redis_ha_update_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.redis_ha_update_response_array
				i=0
				error = [redis_ha_update() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.redis_ha_update_response_array
			i=0
			redis_ha_update_objs = [redis_ha_update() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_redis_ha_update'):
					for props in obj._redis_ha_update:
						result = service.payload_formatter.string_to_bulk_resource(redis_ha_update_response,self.__class__.__name__,props)
						redis_ha_update_objs[i] = result.redis_ha_update
						i=i+1
			return redis_ha_update_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(redis_ha_update,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class redis_ha_update_response(base_response):
	def __init__(self,length=1) :
		self.redis_ha_update= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.redis_ha_update= [ redis_ha_update() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class redis_ha_update_responses(base_response):
	def __init__(self,length=1) :
		self.redis_ha_update_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.redis_ha_update_response_array = [ redis_ha_update() for _ in range(length)]
