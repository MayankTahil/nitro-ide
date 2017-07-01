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
Configuration for Administrative Domain Information resource
'''

class tenant_info(base_resource):
	_ability_to_create_domain= ""
	_level= ""
	_parent_name= ""
	_name= ""
	_is_pooled_license= ""
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
			return "tenant_info"
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
			return "tenant_infos"
		except Exception as e :
			raise e



	'''
	get Ability to create sub administrative domain
	'''
	@property
	def ability_to_create_domain(self) :
		try:
			return self._ability_to_create_domain
		except Exception as e :
			raise e
	'''
	set Ability to create sub administrative domain
	'''
	@ability_to_create_domain.setter
	def ability_to_create_domain(self,ability_to_create_domain):
		try :
			if not isinstance(ability_to_create_domain,bool):
				raise TypeError("ability_to_create_domain must be set to bool value")
			self._ability_to_create_domain = ability_to_create_domain
		except Exception as e :
			raise e


	'''
	get Level of Administrative Domain
	'''
	@property
	def level(self) :
		try:
			return self._level
		except Exception as e :
			raise e
	'''
	set Level of Administrative Domain
	'''
	@level.setter
	def level(self,level):
		try :
			if not isinstance(level,int):
				raise TypeError("level must be set to int value")
			self._level = level
		except Exception as e :
			raise e


	'''
	get Parent Administrative Domain Name
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e


	'''
	get Administrative Domain Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e

	'''
	Platform is licensed for Triscaler feature
	'''
	@property
	def is_pooled_license(self):
		try:
			return self._is_pooled_license
		except Exception as e :
			raise e

	'''
	Use this operation to get administrative domain info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tenant_info_obj=tenant_info()
				response = tenant_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_info_obj = tenant_info()
			option_ = options()
			option_._filter=filter_
			return tenant_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_info_obj = tenant_info()
			option_ = options()
			option_._count=True
			response = tenant_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_info_obj = tenant_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_info_responses, response, "tenant_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_info_response_array
				i=0
				error = [tenant_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_info_response_array
			i=0
			tenant_info_objs = [tenant_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_info'):
					for props in obj._tenant_info:
						result = service.payload_formatter.string_to_bulk_resource(tenant_info_response,self.__class__.__name__,props)
						tenant_info_objs[i] = result.tenant_info
						i=i+1
			return tenant_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_info_response(base_response):
	def __init__(self,length=1) :
		self.tenant_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_info= [ tenant_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_info_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_info_response_array = [ tenant_info() for _ in range(length)]
