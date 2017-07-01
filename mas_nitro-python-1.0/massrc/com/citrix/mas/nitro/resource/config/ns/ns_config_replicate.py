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
Configuration for NetScaler Configuration Replicate resource
'''

class ns_config_replicate(base_resource):
	_source_device= ""
	_target_device=[]
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
			return "ns_config_replicate"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._source_device
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
			return "ns_config_replicates"
		except Exception as e :
			raise e



	'''
	get Source NS IP Address
	'''
	@property
	def source_device(self) :
		try:
			return self._source_device
		except Exception as e :
			raise e
	'''
	set Source NS IP Address
	'''
	@source_device.setter
	def source_device(self,source_device):
		try :
			if not isinstance(source_device,str):
				raise TypeError("source_device must be set to str value")
			self._source_device = source_device
		except Exception as e :
			raise e


	'''
	get Target device IP Address Array on which replicate config from source device
	'''
	@property
	def target_device(self) :
		try:
			return self._target_device
		except Exception as e :
			raise e
	'''
	set Target device IP Address Array on which replicate config from source device
	'''
	@target_device.setter
	def target_device(self,target_device) :
		try :
			if not isinstance(target_device,list):
				raise TypeError("target_device must be set to array of str value")
			for item in target_device :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._target_device = target_device
		except Exception as e :
			raise e

	'''
	 Use this operation to replicate source ns device configuration to one or more target ns devices.
	'''
	@classmethod
	def replicate(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"replicate")
			else : 
				ns_config_replicate_obj= ns_config_replicate()
				return cls.perform_operation_bulk_request(service,"replicate", resource,ns_config_replicate_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_config_replicate_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_config_replicate
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_config_replicate_responses, response, "ns_config_replicate_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_config_replicate_response_array
				i=0
				error = [ns_config_replicate() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_config_replicate_response_array
			i=0
			ns_config_replicate_objs = [ns_config_replicate() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_config_replicate'):
					for props in obj._ns_config_replicate:
						result = service.payload_formatter.string_to_bulk_resource(ns_config_replicate_response,self.__class__.__name__,props)
						ns_config_replicate_objs[i] = result.ns_config_replicate
						i=i+1
			return ns_config_replicate_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_config_replicate,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_config_replicate_response(base_response):
	def __init__(self,length=1) :
		self.ns_config_replicate= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_config_replicate= [ ns_config_replicate() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_config_replicate_responses(base_response):
	def __init__(self,length=1) :
		self.ns_config_replicate_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_config_replicate_response_array = [ ns_config_replicate() for _ in range(length)]
