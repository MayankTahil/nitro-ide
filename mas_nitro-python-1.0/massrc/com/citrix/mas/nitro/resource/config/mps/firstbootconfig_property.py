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
Configuration for Service First Boot Config Property resource
'''

class firstbootconfig_property(base_resource):
	_value_reference= ""
	_parent_name= ""
	_value= ""
	_name= ""
	_network_service_id= ""
	_description= ""
	_parent_id= ""
	_formation_template_id= ""
	_id= ""
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
			return "firstbootconfig_property"
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
			return "firstbootconfig_propertys"
		except Exception as e :
			raise e



	'''
	get Reference to obtain value
	'''
	@property
	def value_reference(self) :
		try:
			return self._value_reference
		except Exception as e :
			raise e
	'''
	set Reference to obtain value
	'''
	@value_reference.setter
	def value_reference(self,value_reference):
		try :
			if not isinstance(value_reference,str):
				raise TypeError("value_reference must be set to str value")
			self._value_reference = value_reference
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
	get The value of the property
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set The value of the property
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
	get Property Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Property Name
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
	get Network Service ID
	'''
	@property
	def network_service_id(self) :
		try:
			return self._network_service_id
		except Exception as e :
			raise e
	'''
	set Network Service ID
	'''
	@network_service_id.setter
	def network_service_id(self,network_service_id):
		try :
			if not isinstance(network_service_id,str):
				raise TypeError("network_service_id must be set to str value")
			self._network_service_id = network_service_id
		except Exception as e :
			raise e


	'''
	get Property description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Property description
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
	get description
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set description
	'''
	@formation_template_id.setter
	def formation_template_id(self,formation_template_id):
		try :
			if not isinstance(formation_template_id,str):
				raise TypeError("formation_template_id must be set to str value")
			self._formation_template_id = formation_template_id
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
	Use this operation to get the network service firstbootconfig property.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				firstbootconfig_property_obj=firstbootconfig_property()
				response = firstbootconfig_property_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of firstbootconfig_property resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			firstbootconfig_property_obj = firstbootconfig_property()
			option_ = options()
			option_._filter=filter_
			return firstbootconfig_property_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the firstbootconfig_property resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			firstbootconfig_property_obj = firstbootconfig_property()
			option_ = options()
			option_._count=True
			response = firstbootconfig_property_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of firstbootconfig_property resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			firstbootconfig_property_obj = firstbootconfig_property()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = firstbootconfig_property_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(firstbootconfig_property_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.firstbootconfig_property
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(firstbootconfig_property_responses, response, "firstbootconfig_property_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.firstbootconfig_property_response_array
				i=0
				error = [firstbootconfig_property() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.firstbootconfig_property_response_array
			i=0
			firstbootconfig_property_objs = [firstbootconfig_property() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_firstbootconfig_property'):
					for props in obj._firstbootconfig_property:
						result = service.payload_formatter.string_to_bulk_resource(firstbootconfig_property_response,self.__class__.__name__,props)
						firstbootconfig_property_objs[i] = result.firstbootconfig_property
						i=i+1
			return firstbootconfig_property_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(firstbootconfig_property,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class firstbootconfig_property_response(base_response):
	def __init__(self,length=1) :
		self.firstbootconfig_property= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.firstbootconfig_property= [ firstbootconfig_property() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class firstbootconfig_property_responses(base_response):
	def __init__(self,length=1) :
		self.firstbootconfig_property_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.firstbootconfig_property_response_array = [ firstbootconfig_property() for _ in range(length)]
