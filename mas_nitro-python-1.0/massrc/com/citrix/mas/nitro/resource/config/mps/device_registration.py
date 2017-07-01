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
Configuration for Register Device resource
'''

class device_registration(base_resource):
	_device_type= ""
	_device_ip_address= ""
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
			return "device_registration"
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
			return "device_registrations"
		except Exception as e :
			raise e



	'''
	get Device Type of the device to be registered for discovery
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set Device Type of the device to be registered for discovery
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
		except Exception as e :
			raise e


	'''
	get Device to be registered for discovery.
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device to be registered for discovery.
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to register devices.
	'''
	@classmethod
	def update(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"update")
			else : 
				device_registration_obj= device_registration()
				return cls.perform_operation_bulk_request(service,"update", resource,device_registration_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_registration_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_registration
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_registration_responses, response, "device_registration_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_registration_response_array
				i=0
				error = [device_registration() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_registration_response_array
			i=0
			device_registration_objs = [device_registration() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_registration'):
					for props in obj._device_registration:
						result = service.payload_formatter.string_to_bulk_resource(device_registration_response,self.__class__.__name__,props)
						device_registration_objs[i] = result.device_registration
						i=i+1
			return device_registration_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_registration,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_registration_response(base_response):
	def __init__(self,length=1) :
		self.device_registration= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_registration= [ device_registration() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_registration_responses(base_response):
	def __init__(self,length=1) :
		self.device_registration_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_registration_response_array = [ device_registration() for _ in range(length)]
