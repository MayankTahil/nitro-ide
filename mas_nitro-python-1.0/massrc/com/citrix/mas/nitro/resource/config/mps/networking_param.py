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
Configuration for Networking params used in triton config resource
'''

class networking_param(base_resource):
	_networking_type= ""
	_parent_name= ""
	_networking_username= ""
	_networking_vip_subnet= ""
	_networking_password= ""
	_parent_id= ""
	_networking_enterprise= ""
	_networking_api_url= ""
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
			return "networking_param"
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
			return "networking_params"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def networking_type(self) :
		try:
			return self._networking_type
		except Exception as e :
			raise e
	'''
	set 
	'''
	@networking_type.setter
	def networking_type(self,networking_type):
		try :
			if not isinstance(networking_type,str):
				raise TypeError("networking_type must be set to str value")
			self._networking_type = networking_type
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
	get User Name for Networking connection
	'''
	@property
	def networking_username(self) :
		try:
			return self._networking_username
		except Exception as e :
			raise e
	'''
	set User Name for Networking connection
	'''
	@networking_username.setter
	def networking_username(self,networking_username):
		try :
			if not isinstance(networking_username,str):
				raise TypeError("networking_username must be set to str value")
			self._networking_username = networking_username
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def networking_vip_subnet(self) :
		try:
			return self._networking_vip_subnet
		except Exception as e :
			raise e
	'''
	set 
	'''
	@networking_vip_subnet.setter
	def networking_vip_subnet(self,networking_vip_subnet):
		try :
			if not isinstance(networking_vip_subnet,str):
				raise TypeError("networking_vip_subnet must be set to str value")
			self._networking_vip_subnet = networking_vip_subnet
		except Exception as e :
			raise e


	'''
	get Password for networking connection
	'''
	@property
	def networking_password(self) :
		try:
			return self._networking_password
		except Exception as e :
			raise e
	'''
	set Password for networking connection
	'''
	@networking_password.setter
	def networking_password(self,networking_password):
		try :
			if not isinstance(networking_password,str):
				raise TypeError("networking_password must be set to str value")
			self._networking_password = networking_password
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
	get 
	'''
	@property
	def networking_enterprise(self) :
		try:
			return self._networking_enterprise
		except Exception as e :
			raise e
	'''
	set 
	'''
	@networking_enterprise.setter
	def networking_enterprise(self,networking_enterprise):
		try :
			if not isinstance(networking_enterprise,str):
				raise TypeError("networking_enterprise must be set to str value")
			self._networking_enterprise = networking_enterprise
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def networking_api_url(self) :
		try:
			return self._networking_api_url
		except Exception as e :
			raise e
	'''
	set 
	'''
	@networking_api_url.setter
	def networking_api_url(self,networking_api_url):
		try :
			if not isinstance(networking_api_url,str):
				raise TypeError("networking_api_url must be set to str value")
			self._networking_api_url = networking_api_url
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(networking_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.networking_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(networking_param_responses, response, "networking_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.networking_param_response_array
				i=0
				error = [networking_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.networking_param_response_array
			i=0
			networking_param_objs = [networking_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_networking_param'):
					for props in obj._networking_param:
						result = service.payload_formatter.string_to_bulk_resource(networking_param_response,self.__class__.__name__,props)
						networking_param_objs[i] = result.networking_param
						i=i+1
			return networking_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(networking_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class networking_param_response(base_response):
	def __init__(self,length=1) :
		self.networking_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.networking_param= [ networking_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class networking_param_responses(base_response):
	def __init__(self,length=1) :
		self.networking_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.networking_param_response_array = [ networking_param() for _ in range(length)]
