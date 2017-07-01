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
Configuration for Marathon params used in triton config resource
'''

class marathon_param(base_resource):
	_marathon_username= ""
	_marathon_url= ""
	_parent_name= ""
	_marathon_password= ""
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
			return "marathon_param"
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
			return "marathon_params"
		except Exception as e :
			raise e



	'''
	get User Name for Marathon connection
	'''
	@property
	def marathon_username(self) :
		try:
			return self._marathon_username
		except Exception as e :
			raise e
	'''
	set User Name for Marathon connection
	'''
	@marathon_username.setter
	def marathon_username(self,marathon_username):
		try :
			if not isinstance(marathon_username,str):
				raise TypeError("marathon_username must be set to str value")
			self._marathon_username = marathon_username
		except Exception as e :
			raise e


	'''
	get URL to be used to connect to Marathon
	'''
	@property
	def marathon_url(self) :
		try:
			return self._marathon_url
		except Exception as e :
			raise e
	'''
	set URL to be used to connect to Marathon
	'''
	@marathon_url.setter
	def marathon_url(self,marathon_url):
		try :
			if not isinstance(marathon_url,str):
				raise TypeError("marathon_url must be set to str value")
			self._marathon_url = marathon_url
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
	get Password for marathon connection
	'''
	@property
	def marathon_password(self) :
		try:
			return self._marathon_password
		except Exception as e :
			raise e
	'''
	set Password for marathon connection
	'''
	@marathon_password.setter
	def marathon_password(self,marathon_password):
		try :
			if not isinstance(marathon_password,str):
				raise TypeError("marathon_password must be set to str value")
			self._marathon_password = marathon_password
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
			result=service.payload_formatter.string_to_resource(marathon_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.marathon_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(marathon_param_responses, response, "marathon_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.marathon_param_response_array
				i=0
				error = [marathon_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.marathon_param_response_array
			i=0
			marathon_param_objs = [marathon_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_marathon_param'):
					for props in obj._marathon_param:
						result = service.payload_formatter.string_to_bulk_resource(marathon_param_response,self.__class__.__name__,props)
						marathon_param_objs[i] = result.marathon_param
						i=i+1
			return marathon_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(marathon_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class marathon_param_response(base_response):
	def __init__(self,length=1) :
		self.marathon_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.marathon_param= [ marathon_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class marathon_param_responses(base_response):
	def __init__(self,length=1) :
		self.marathon_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.marathon_param_response_array = [ marathon_param() for _ in range(length)]
