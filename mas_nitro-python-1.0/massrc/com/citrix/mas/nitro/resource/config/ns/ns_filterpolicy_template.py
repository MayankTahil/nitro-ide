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
from massrc.com.citrix.mas.nitro.resource.config.mps.variable_values import variable_values


'''
Configuration for NS Filter Policy Configure Task resource
'''

class ns_filterpolicy_template(base_resource):
	_priority= ""
	_device_groups=[]
	_name= ""
	_variables=[]
	_state= ""
	_devices=[]
	_actionType= ""
	_actionName= ""
	_expression= ""
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
			return "ns_filterpolicy_template"
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
			return "ns_filterpolicy_templates"
		except Exception as e :
			raise e



	'''
	get Policy Priority
	'''
	@property
	def priority(self) :
		try:
			return self._priority
		except Exception as e :
			raise e
	'''
	set Policy Priority
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
	get Device Group Array on which for which template is applied
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	set Device Group Array on which for which template is applied
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e


	'''
	get Name of Policy
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of Policy
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
	get Values of Variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of variable_values value")
			for item in variables :
				if not isinstance(item,variable_values):
					raise TypeError("item must be set to variable_values value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get State of the Policy: enabled/disabled
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of the Policy: enabled/disabled
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get Device IP Address Array on which template is applied
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Device IP Address Array on which template is applied
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e


	'''
	get Action Type of the Policy
	'''
	@property
	def actionType(self) :
		try:
			return self._actionType
		except Exception as e :
			raise e
	'''
	set Action Type of the Policy
	'''
	@actionType.setter
	def actionType(self,actionType):
		try :
			if not isinstance(actionType,str):
				raise TypeError("actionType must be set to str value")
			self._actionType = actionType
		except Exception as e :
			raise e


	'''
	get Action Name of the Policy
	'''
	@property
	def actionName(self) :
		try:
			return self._actionName
		except Exception as e :
			raise e
	'''
	set Action Name of the Policy
	'''
	@actionName.setter
	def actionName(self,actionName):
		try :
			if not isinstance(actionName,str):
				raise TypeError("actionName must be set to str value")
			self._actionName = actionName
		except Exception as e :
			raise e


	'''
	get Expression of the Policy
	'''
	@property
	def expression(self) :
		try:
			return self._expression
		except Exception as e :
			raise e
	'''
	set Expression of the Policy
	'''
	@expression.setter
	def expression(self,expression):
		try :
			if not isinstance(expression,str):
				raise TypeError("expression must be set to str value")
			self._expression = expression
		except Exception as e :
			raise e

	'''
	Use this operation to add device profile.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_filterpolicy_template_obj= ns_filterpolicy_template()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_filterpolicy_template_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get device profiles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_filterpolicy_template_obj=ns_filterpolicy_template()
				response = ns_filterpolicy_template_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_filterpolicy_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_filterpolicy_template_obj = ns_filterpolicy_template()
			option_ = options()
			option_._filter=filter_
			return ns_filterpolicy_template_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_filterpolicy_template resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_filterpolicy_template_obj = ns_filterpolicy_template()
			option_ = options()
			option_._count=True
			response = ns_filterpolicy_template_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_filterpolicy_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_filterpolicy_template_obj = ns_filterpolicy_template()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_filterpolicy_template_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_filterpolicy_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_filterpolicy_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_filterpolicy_template_responses, response, "ns_filterpolicy_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_filterpolicy_template_response_array
				i=0
				error = [ns_filterpolicy_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_filterpolicy_template_response_array
			i=0
			ns_filterpolicy_template_objs = [ns_filterpolicy_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_filterpolicy_template'):
					for props in obj._ns_filterpolicy_template:
						result = service.payload_formatter.string_to_bulk_resource(ns_filterpolicy_template_response,self.__class__.__name__,props)
						ns_filterpolicy_template_objs[i] = result.ns_filterpolicy_template
						i=i+1
			return ns_filterpolicy_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_filterpolicy_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_filterpolicy_template_response(base_response):
	def __init__(self,length=1) :
		self.ns_filterpolicy_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_filterpolicy_template= [ ns_filterpolicy_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_filterpolicy_template_responses(base_response):
	def __init__(self,length=1) :
		self.ns_filterpolicy_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_filterpolicy_template_response_array = [ ns_filterpolicy_template() for _ in range(length)]
