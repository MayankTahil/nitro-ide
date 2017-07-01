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
Configuration for Save configuration on NetScaler resource
'''

class ns_save_config(base_resource):
	_ns_ip_address_arr=[]
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
			return "ns_save_config"
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
			return "ns_save_configs"
		except Exception as e :
			raise e



	'''
	get List of NS IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of NS IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e

	'''
	Use this operation to save configuration on NS Instance(s).
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_save_config_obj= ns_save_config()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_save_config_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_save_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_save_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_save_config_responses, response, "ns_save_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_save_config_response_array
				i=0
				error = [ns_save_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_save_config_response_array
			i=0
			ns_save_config_objs = [ns_save_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_save_config'):
					for props in obj._ns_save_config:
						result = service.payload_formatter.string_to_bulk_resource(ns_save_config_response,self.__class__.__name__,props)
						ns_save_config_objs[i] = result.ns_save_config
						i=i+1
			return ns_save_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_save_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_save_config_response(base_response):
	def __init__(self,length=1) :
		self.ns_save_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_save_config= [ ns_save_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_save_config_responses(base_response):
	def __init__(self,length=1) :
		self.ns_save_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_save_config_response_array = [ ns_save_config() for _ in range(length)]
