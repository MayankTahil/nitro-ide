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
from massrc.com.citrix.mas.nitro.resource.config.mps.device_values_map import device_values_map


'''
Configuration for Variable Values required for config template execution resource
'''

class variable_values(base_resource):
	_parent_name= ""
	_value= ""
	_name= ""
	_display_name= ""
	_description= ""
	_device_values=[]
	_parent_id= ""
	_default_value= ""
	_id= ""
	_type= ""
	_values_enum_db= ""
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
			return "variable_values"
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
			return "variable_valuess"
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
	get Value of the Variable to be used for all device ips/groups
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set Value of the Variable to be used for all device ips/groups
	'''
	@value.setter
	def value(self,value):
		try :
			if not isinstance(value,str):
				raise TypeError("value must be set to str value")
			self._value = value
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
	get Values of variables used in commands of the configuration template for individual devices
	'''
	@property
	def device_values(self) :
		try:
			return self._device_values
		except Exception as e :
			raise e
	'''
	set Values of variables used in commands of the configuration template for individual devices
	'''
	@device_values.setter
	def device_values(self,device_values) :
		try :
			if not isinstance(device_values,list):
				raise TypeError("device_values must be set to array of device_values_map value")
			for item in device_values :
				if not isinstance(item,device_values_map):
					raise TypeError("item must be set to device_values_map value")
			self._device_values = device_values
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
	Use this operation to get configuration templates.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				variable_values_obj=variable_values()
				response = variable_values_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of variable_values resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			variable_values_obj = variable_values()
			option_ = options()
			option_._filter=filter_
			return variable_values_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the variable_values resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			variable_values_obj = variable_values()
			option_ = options()
			option_._count=True
			response = variable_values_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of variable_values resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			variable_values_obj = variable_values()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = variable_values_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(variable_values_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.variable_values
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(variable_values_responses, response, "variable_values_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.variable_values_response_array
				i=0
				error = [variable_values() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.variable_values_response_array
			i=0
			variable_values_objs = [variable_values() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_variable_values'):
					for props in obj._variable_values:
						result = service.payload_formatter.string_to_bulk_resource(variable_values_response,self.__class__.__name__,props)
						variable_values_objs[i] = result.variable_values
						i=i+1
			return variable_values_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(variable_values,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class variable_values_response(base_response):
	def __init__(self,length=1) :
		self.variable_values= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.variable_values= [ variable_values() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class variable_values_responses(base_response):
	def __init__(self,length=1) :
		self.variable_values_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.variable_values_response_array = [ variable_values() for _ in range(length)]
