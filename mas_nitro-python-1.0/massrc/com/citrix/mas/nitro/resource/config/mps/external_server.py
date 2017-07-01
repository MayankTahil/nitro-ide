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
Configuration for External Server configuration resource
'''

class external_server(base_resource):
	_priority= ""
	_parent_name= ""
	_external_server_type= ""
	_external_server_name= ""
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
			return "external_server"
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
			return "external_servers"
		except Exception as e :
			raise e



	'''
	get Priority of external server
	'''
	@property
	def priority(self) :
		try:
			return self._priority
		except Exception as e :
			raise e
	'''
	set Priority of external server
	'''
	@priority.setter
	def priority(self,priority):
		try :
			if not isinstance(priority,int):
				raise TypeError("priority must be set to int value")
			self._priority = priority
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
	get Type of external server. Supported types 1.RADIUS 2.LDAP 3.TACACS 4.KEYSTONE
	'''
	@property
	def external_server_type(self) :
		try:
			return self._external_server_type
		except Exception as e :
			raise e
	'''
	set Type of external server. Supported types 1.RADIUS 2.LDAP 3.TACACS 4.KEYSTONE
	'''
	@external_server_type.setter
	def external_server_type(self,external_server_type):
		try :
			if not isinstance(external_server_type,str):
				raise TypeError("external_server_type must be set to str value")
			self._external_server_type = external_server_type
		except Exception as e :
			raise e


	'''
	get Name of external server
	'''
	@property
	def external_server_name(self) :
		try:
			return self._external_server_name
		except Exception as e :
			raise e
	'''
	set Name of external server
	'''
	@external_server_name.setter
	def external_server_name(self,external_server_name):
		try :
			if not isinstance(external_server_name,str):
				raise TypeError("external_server_name must be set to str value")
			self._external_server_name = external_server_name
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
			result=service.payload_formatter.string_to_resource(external_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.external_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(external_server_responses, response, "external_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.external_server_response_array
				i=0
				error = [external_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.external_server_response_array
			i=0
			external_server_objs = [external_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_external_server'):
					for props in obj._external_server:
						result = service.payload_formatter.string_to_bulk_resource(external_server_response,self.__class__.__name__,props)
						external_server_objs[i] = result.external_server
						i=i+1
			return external_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(external_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class external_server_response(base_response):
	def __init__(self,length=1) :
		self.external_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.external_server= [ external_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class external_server_responses(base_response):
	def __init__(self,length=1) :
		self.external_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.external_server_response_array = [ external_server() for _ in range(length)]
