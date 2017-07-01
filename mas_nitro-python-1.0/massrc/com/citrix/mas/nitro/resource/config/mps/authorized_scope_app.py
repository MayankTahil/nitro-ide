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
Configuration for Authorized applications resource
'''

class authorized_scope_app(base_resource):
	_parent_name= ""
	_app_state= ""
	_parent_id= ""
	_device_ip_address= ""
	_app_protocol= ""
	_appname= ""
	_app_ip_address= ""
	_entity_id= ""
	_app_type= ""
	_id= ""
	_config_path= ""
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
			return "authorized_scope_app"
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
			return "authorized_scope_apps"
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
	get App state
	'''
	@property
	def app_state(self) :
		try:
			return self._app_state
		except Exception as e :
			raise e
	'''
	set App state
	'''
	@app_state.setter
	def app_state(self,app_state):
		try :
			if not isinstance(app_state,str):
				raise TypeError("app_state must be set to str value")
			self._app_state = app_state
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
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
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
	get App Protocol
	'''
	@property
	def app_protocol(self) :
		try:
			return self._app_protocol
		except Exception as e :
			raise e
	'''
	set App Protocol
	'''
	@app_protocol.setter
	def app_protocol(self,app_protocol):
		try :
			if not isinstance(app_protocol,str):
				raise TypeError("app_protocol must be set to str value")
			self._app_protocol = app_protocol
		except Exception as e :
			raise e


	'''
	get Property key
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set Property key
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get Application IP Address
	'''
	@property
	def app_ip_address(self) :
		try:
			return self._app_ip_address
		except Exception as e :
			raise e
	'''
	set Application IP Address
	'''
	@app_ip_address.setter
	def app_ip_address(self,app_ip_address):
		try :
			if not isinstance(app_ip_address,str):
				raise TypeError("app_ip_address must be set to str value")
			self._app_ip_address = app_ip_address
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def entity_id(self) :
		try:
			return self._entity_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@entity_id.setter
	def entity_id(self,entity_id):
		try :
			if not isinstance(entity_id,str):
				raise TypeError("entity_id must be set to str value")
			self._entity_id = entity_id
		except Exception as e :
			raise e


	'''
	get Application type ( CS/LB/GSLB etc.)
	'''
	@property
	def app_type(self) :
		try:
			return self._app_type
		except Exception as e :
			raise e
	'''
	set Application type ( CS/LB/GSLB etc.)
	'''
	@app_type.setter
	def app_type(self,app_type):
		try :
			if not isinstance(app_type,str):
				raise TypeError("app_type must be set to str value")
			self._app_type = app_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	def config_path(self) :
		try:
			return self._config_path
		except Exception as e :
			raise e
	'''
	set 
	'''
	@config_path.setter
	def config_path(self,config_path):
		try :
			if not isinstance(config_path,str):
				raise TypeError("config_path must be set to str value")
			self._config_path = config_path
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(authorized_scope_app_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authorized_scope_app
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(authorized_scope_app_responses, response, "authorized_scope_app_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.authorized_scope_app_response_array
				i=0
				error = [authorized_scope_app() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.authorized_scope_app_response_array
			i=0
			authorized_scope_app_objs = [authorized_scope_app() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_authorized_scope_app'):
					for props in obj._authorized_scope_app:
						result = service.payload_formatter.string_to_bulk_resource(authorized_scope_app_response,self.__class__.__name__,props)
						authorized_scope_app_objs[i] = result.authorized_scope_app
						i=i+1
			return authorized_scope_app_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(authorized_scope_app,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class authorized_scope_app_response(base_response):
	def __init__(self,length=1) :
		self.authorized_scope_app= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.authorized_scope_app= [ authorized_scope_app() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class authorized_scope_app_responses(base_response):
	def __init__(self,length=1) :
		self.authorized_scope_app_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.authorized_scope_app_response_array = [ authorized_scope_app() for _ in range(length)]
