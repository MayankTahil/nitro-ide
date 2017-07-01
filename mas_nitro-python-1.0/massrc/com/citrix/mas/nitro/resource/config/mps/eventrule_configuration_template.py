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
from massrc.com.citrix.mas.nitro.resource.config.mps.eventrule_config_command import eventrule_config_command
from massrc.com.citrix.mas.nitro.resource.config.mps.eventrule_config_variable import eventrule_config_variable


'''
Configuration for eventruleConfiguration Template resource
'''

class eventrule_configuration_template(base_resource):
	_device_family= ""
	_parent_name= ""
	_commands=[]
	_name= ""
	_variables=[]
	_description= ""
	_parent_id= ""
	_is_visible= ""
	_tenant_id= ""
	_id= ""
	_is_inbuilt= ""
	_category= ""
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
			return "eventrule_configuration_template"
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
			return "eventrule_configuration_templates"
		except Exception as e :
			raise e



	'''
	get Family of Devices for which config template is defined.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of Devices for which config template is defined.
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
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
	get Array of commands part of the configuration template
	'''
	@property
	def commands(self) :
		try:
			return self._commands
		except Exception as e :
			raise e
	'''
	set Array of commands part of the configuration template
	'''
	@commands.setter
	def commands(self,commands) :
		try :
			if not isinstance(commands,list):
				raise TypeError("commands must be set to array of eventrule_config_command value")
			for item in commands :
				if not isinstance(item,eventrule_config_command):
					raise TypeError("item must be set to eventrule_config_command value")
			self._commands = commands
		except Exception as e :
			raise e


	'''
	get Name of configuration template
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of configuration template
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
	get Array of variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Array of variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of eventrule_config_variable value")
			for item in variables :
				if not isinstance(item,eventrule_config_variable):
					raise TypeError("item must be set to eventrule_config_variable value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get Description of configuration template
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of configuration template
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
	get true, if this template is visible
	'''
	@property
	def is_visible(self) :
		try:
			return self._is_visible
		except Exception as e :
			raise e


	'''
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the configuration templates
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the configuration templates
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
	get true, if this template is in built
	'''
	@property
	def is_inbuilt(self) :
		try:
			return self._is_inbuilt
		except Exception as e :
			raise e


	'''
	get Category of configuration template
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	set Category of configuration template
	'''
	@category.setter
	def category(self,category):
		try :
			if not isinstance(category,str):
				raise TypeError("category must be set to str value")
			self._category = category
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(eventrule_configuration_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.eventrule_configuration_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(eventrule_configuration_template_responses, response, "eventrule_configuration_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.eventrule_configuration_template_response_array
				i=0
				error = [eventrule_configuration_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.eventrule_configuration_template_response_array
			i=0
			eventrule_configuration_template_objs = [eventrule_configuration_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_eventrule_configuration_template'):
					for props in obj._eventrule_configuration_template:
						result = service.payload_formatter.string_to_bulk_resource(eventrule_configuration_template_response,self.__class__.__name__,props)
						eventrule_configuration_template_objs[i] = result.eventrule_configuration_template
						i=i+1
			return eventrule_configuration_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(eventrule_configuration_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class eventrule_configuration_template_response(base_response):
	def __init__(self,length=1) :
		self.eventrule_configuration_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.eventrule_configuration_template= [ eventrule_configuration_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class eventrule_configuration_template_responses(base_response):
	def __init__(self,length=1) :
		self.eventrule_configuration_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.eventrule_configuration_template_response_array = [ eventrule_configuration_template() for _ in range(length)]
