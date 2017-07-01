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
Configuration for Configuration Variables for use in configuration template resource
'''

class config_variable(base_resource):
	_parent_name= ""
	_name= ""
	_display_name= ""
	_description= ""
	_parent_id= ""
	_required= ""
	_default_value= ""
	_id= ""
	_type= ""
	_values_enum_db= ""
	_values_enum=[]
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
			return "config_variable"
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
			return "config_variables"
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
	get Variable name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Variable name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Display name of configuration variable
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Display name of configuration variable
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get Description of configuration variable
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of configuration variable
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
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
	get If it is required argument for command then true else false.
	'''
	@property
	def required(self) :
		try:
			return self._required
		except Exception as e :
			raise e
	'''
	set If it is required argument for command then true else false.
	'''
	@required.setter
	def required(self,required):
		try :
			if not isinstance(required,bool):
				raise TypeError("required must be set to bool value")
			self._required = required
		except Exception as e :
			raise e


	'''
	get Default Value of configuration variable
	'''
	@property
	def default_value(self) :
		try:
			return self._default_value
		except Exception as e :
			raise e
	'''
	set Default Value of configuration variable
	'''
	@default_value.setter
	def default_value(self,default_value):
		try :
			if not isinstance(default_value,str):
				raise TypeError("default_value must be set to str value")
			self._default_value = default_value
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
	get Type of Variable
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of Variable
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Comma seperated list of possible values of variable
	'''
	@property
	def values_enum_db(self) :
		try:
			return self._values_enum_db
		except Exception as e :
			raise e
	'''
	set Comma seperated list of possible values of variable
	'''
	@values_enum_db.setter
	def values_enum_db(self,values_enum_db):
		try :
			if not isinstance(values_enum_db,str):
				raise TypeError("values_enum_db must be set to str value")
			self._values_enum_db = values_enum_db
		except Exception as e :
			raise e


	'''
	get Possible Values Enum for the configuration variable
	'''
	@property
	def values_enum(self) :
		try:
			return self._values_enum
		except Exception as e :
			raise e
	'''
	set Possible Values Enum for the configuration variable
	'''
	@values_enum.setter
	def values_enum(self,values_enum) :
		try :
			if not isinstance(values_enum,list):
				raise TypeError("values_enum must be set to array of str value")
			for item in values_enum :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._values_enum = values_enum
		except Exception as e :
			raise e

	'''
	Use this operation to add config variable..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				config_variable_obj= config_variable()
				return cls.perform_operation_bulk_request(service,"add", resource,config_variable_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_variable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_variable
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_variable_responses, response, "config_variable_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_variable_response_array
				i=0
				error = [config_variable() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_variable_response_array
			i=0
			config_variable_objs = [config_variable() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_variable'):
					for props in obj._config_variable:
						result = service.payload_formatter.string_to_bulk_resource(config_variable_response,self.__class__.__name__,props)
						config_variable_objs[i] = result.config_variable
						i=i+1
			return config_variable_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_variable,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_variable_response(base_response):
	def __init__(self,length=1) :
		self.config_variable= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_variable= [ config_variable() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_variable_responses(base_response):
	def __init__(self,length=1) :
		self.config_variable_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_variable_response_array = [ config_variable() for _ in range(length)]
