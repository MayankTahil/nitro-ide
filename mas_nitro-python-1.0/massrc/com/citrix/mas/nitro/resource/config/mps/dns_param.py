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
Configuration for Dns params used in triton config resource
'''

class dns_param(base_resource):
	_parent_name= ""
	_dns_suffix= ""
	_dns_type= ""
	_dns_api_url= ""
	_dns_password= ""
	_dns_username= ""
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
			return "dns_param"
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
			return "dns_params"
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
	get 
	'''
	@property
	def dns_suffix(self) :
		try:
			return self._dns_suffix
		except Exception as e :
			raise e
	'''
	set 
	'''
	@dns_suffix.setter
	def dns_suffix(self,dns_suffix):
		try :
			if not isinstance(dns_suffix,str):
				raise TypeError("dns_suffix must be set to str value")
			self._dns_suffix = dns_suffix
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def dns_type(self) :
		try:
			return self._dns_type
		except Exception as e :
			raise e
	'''
	set 
	'''
	@dns_type.setter
	def dns_type(self,dns_type):
		try :
			if not isinstance(dns_type,str):
				raise TypeError("dns_type must be set to str value")
			self._dns_type = dns_type
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def dns_api_url(self) :
		try:
			return self._dns_api_url
		except Exception as e :
			raise e
	'''
	set 
	'''
	@dns_api_url.setter
	def dns_api_url(self,dns_api_url):
		try :
			if not isinstance(dns_api_url,str):
				raise TypeError("dns_api_url must be set to str value")
			self._dns_api_url = dns_api_url
		except Exception as e :
			raise e


	'''
	get Password for dns connection
	'''
	@property
	def dns_password(self) :
		try:
			return self._dns_password
		except Exception as e :
			raise e
	'''
	set Password for dns connection
	'''
	@dns_password.setter
	def dns_password(self,dns_password):
		try :
			if not isinstance(dns_password,str):
				raise TypeError("dns_password must be set to str value")
			self._dns_password = dns_password
		except Exception as e :
			raise e


	'''
	get User Name for Dns connection
	'''
	@property
	def dns_username(self) :
		try:
			return self._dns_username
		except Exception as e :
			raise e
	'''
	set User Name for Dns connection
	'''
	@dns_username.setter
	def dns_username(self,dns_username):
		try :
			if not isinstance(dns_username,str):
				raise TypeError("dns_username must be set to str value")
			self._dns_username = dns_username
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
			result=service.payload_formatter.string_to_resource(dns_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dns_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(dns_param_responses, response, "dns_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.dns_param_response_array
				i=0
				error = [dns_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.dns_param_response_array
			i=0
			dns_param_objs = [dns_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_dns_param'):
					for props in obj._dns_param:
						result = service.payload_formatter.string_to_bulk_resource(dns_param_response,self.__class__.__name__,props)
						dns_param_objs[i] = result.dns_param
						i=i+1
			return dns_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(dns_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class dns_param_response(base_response):
	def __init__(self,length=1) :
		self.dns_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.dns_param= [ dns_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class dns_param_responses(base_response):
	def __init__(self,length=1) :
		self.dns_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.dns_param_response_array = [ dns_param() for _ in range(length)]
