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
Configuration for trap severities resource
'''

class trap_settings(base_resource):
	_source= ""
	_default_severity= ""
	_device_family= ""
	_oid= ""
	_user_defined_severity= ""
	_trap_description= ""
	_trap_category= ""
	_is_suppress= ""
	_id= ""
	_source_array=[]
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
			return "trap_settings"
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
			return "trap_settingss"
		except Exception as e :
			raise e



	'''
	get Source
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e


	'''
	get default severity of trap
	'''
	@property
	def default_severity(self) :
		try:
			return self._default_severity
		except Exception as e :
			raise e
	'''
	set default severity of trap
	'''
	@default_severity.setter
	def default_severity(self,default_severity):
		try :
			if not isinstance(default_severity,str):
				raise TypeError("default_severity must be set to str value")
			self._default_severity = default_severity
		except Exception as e :
			raise e


	'''
	get Device Family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family
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
	get Trap OID
	'''
	@property
	def oid(self) :
		try:
			return self._oid
		except Exception as e :
			raise e
	'''
	set Trap OID
	'''
	@oid.setter
	def oid(self,oid):
		try :
			if not isinstance(oid,str):
				raise TypeError("oid must be set to str value")
			self._oid = oid
		except Exception as e :
			raise e


	'''
	get user defined severity of trap
	'''
	@property
	def user_defined_severity(self) :
		try:
			return self._user_defined_severity
		except Exception as e :
			raise e
	'''
	set user defined severity of trap
	'''
	@user_defined_severity.setter
	def user_defined_severity(self,user_defined_severity):
		try :
			if not isinstance(user_defined_severity,str):
				raise TypeError("user_defined_severity must be set to str value")
			self._user_defined_severity = user_defined_severity
		except Exception as e :
			raise e


	'''
	get Trap Description
	'''
	@property
	def trap_description(self) :
		try:
			return self._trap_description
		except Exception as e :
			raise e
	'''
	set Trap Description
	'''
	@trap_description.setter
	def trap_description(self,trap_description):
		try :
			if not isinstance(trap_description,str):
				raise TypeError("trap_description must be set to str value")
			self._trap_description = trap_description
		except Exception as e :
			raise e


	'''
	get Trap Category
	'''
	@property
	def trap_category(self) :
		try:
			return self._trap_category
		except Exception as e :
			raise e
	'''
	set Trap Category
	'''
	@trap_category.setter
	def trap_category(self,trap_category):
		try :
			if not isinstance(trap_category,str):
				raise TypeError("trap_category must be set to str value")
			self._trap_category = trap_category
		except Exception as e :
			raise e


	'''
	get if trap needs to be suppressed or not
	'''
	@property
	def is_suppress(self) :
		try:
			return self._is_suppress
		except Exception as e :
			raise e
	'''
	set if trap needs to be suppressed or not
	'''
	@is_suppress.setter
	def is_suppress(self,is_suppress):
		try :
			if not isinstance(is_suppress,bool):
				raise TypeError("is_suppress must be set to bool value")
			self._is_suppress = is_suppress
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	Source list
	'''
	@property
	def source_array(self) :
		try:
			return self._source_array
		except Exception as e :
			raise e
	'''
	Source list
	'''
	@source_array.setter
	def source_array(self,source_array) :
		try :
			if not isinstance(source_array,list):
				raise TypeError("source_array must be set to array of str value")
			for item in source_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._source_array = source_array
		except Exception as e :
			raise e

	'''
	Use this operation to get trap severities.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				trap_settings_obj=trap_settings()
				response = trap_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify trap severities.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				trap_settings_obj=trap_settings()
				return cls.update_bulk_request(client,resource,trap_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of trap_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			trap_settings_obj = trap_settings()
			option_ = options()
			option_._filter=filter_
			return trap_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the trap_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			trap_settings_obj = trap_settings()
			option_ = options()
			option_._count=True
			response = trap_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of trap_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			trap_settings_obj = trap_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = trap_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(trap_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.trap_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(trap_settings_responses, response, "trap_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.trap_settings_response_array
				i=0
				error = [trap_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.trap_settings_response_array
			i=0
			trap_settings_objs = [trap_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_trap_settings'):
					for props in obj._trap_settings:
						result = service.payload_formatter.string_to_bulk_resource(trap_settings_response,self.__class__.__name__,props)
						trap_settings_objs[i] = result.trap_settings
						i=i+1
			return trap_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(trap_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class trap_settings_response(base_response):
	def __init__(self,length=1) :
		self.trap_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.trap_settings= [ trap_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class trap_settings_responses(base_response):
	def __init__(self,length=1) :
		self.trap_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.trap_settings_response_array = [ trap_settings() for _ in range(length)]
