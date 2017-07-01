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
Configuration for Details of the device used by managed app resource
'''

class app_device(base_resource):
	_device_id= ""
	_parent_name= ""
	_device_mgmt_ip= ""
	_id= ""
	_parent_id= ""
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
			return "app_device"
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
			return "app_devices"
		except Exception as e :
			raise e



	'''
	get Instance ID for the device
	'''
	@property
	def device_id(self) :
		try:
			return self._device_id
		except Exception as e :
			raise e
	'''
	set Instance ID for the device
	'''
	@device_id.setter
	def device_id(self,device_id):
		try :
			if not isinstance(device_id,str):
				raise TypeError("device_id must be set to str value")
			self._device_id = device_id
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
	get IPv4 or IPv6 Address assigned to the device
	'''
	@property
	def device_mgmt_ip(self) :
		try:
			return self._device_mgmt_ip
		except Exception as e :
			raise e
	'''
	set IPv4 or IPv6 Address assigned to the device
	'''
	@device_mgmt_ip.setter
	def device_mgmt_ip(self,device_mgmt_ip):
		try :
			if not isinstance(device_mgmt_ip,str):
				raise TypeError("device_mgmt_ip must be set to str value")
			self._device_mgmt_ip = device_mgmt_ip
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the app-device mapping
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the app-device mapping
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_device_responses, response, "app_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_device_response_array
				i=0
				error = [app_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_device_response_array
			i=0
			app_device_objs = [app_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_device'):
					for props in obj._app_device:
						result = service.payload_formatter.string_to_bulk_resource(app_device_response,self.__class__.__name__,props)
						app_device_objs[i] = result.app_device
						i=i+1
			return app_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_device_response(base_response):
	def __init__(self,length=1) :
		self.app_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_device= [ app_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_device_responses(base_response):
	def __init__(self,length=1) :
		self.app_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_device_response_array = [ app_device() for _ in range(length)]
