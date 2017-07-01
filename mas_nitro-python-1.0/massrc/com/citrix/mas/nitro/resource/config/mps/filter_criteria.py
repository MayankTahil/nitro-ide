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
Configuration for event filter criteria properties resource
'''

class filter_criteria(base_resource):
	_source= ""
	_cmd_exec_status= ""
	_device_family= ""
	_parent_name= ""
	_message= ""
	_parent_id= ""
	_cmd_auth_status= ""
	_config_cmd= ""
	_id= ""
	_category= ""
	_severity= ""
	_failureobj= ""
	_category_array=[]
	_failureobj_array=[]
	_source_array=[]
	_severity_array=[]
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
			return "filter_criteria"
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
			return "filter_criterias"
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
	get Command Execution Status
	'''
	@property
	def cmd_exec_status(self) :
		try:
			return self._cmd_exec_status
		except Exception as e :
			raise e
	'''
	set Command Execution Status
	'''
	@cmd_exec_status.setter
	def cmd_exec_status(self,cmd_exec_status):
		try :
			if not isinstance(cmd_exec_status,str):
				raise TypeError("cmd_exec_status must be set to str value")
			self._cmd_exec_status = cmd_exec_status
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
	get Event Message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Event Message
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
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
	get Command Authorization status
	'''
	@property
	def cmd_auth_status(self) :
		try:
			return self._cmd_auth_status
		except Exception as e :
			raise e
	'''
	set Command Authorization status
	'''
	@cmd_auth_status.setter
	def cmd_auth_status(self,cmd_auth_status):
		try :
			if not isinstance(cmd_auth_status,str):
				raise TypeError("cmd_auth_status must be set to str value")
			self._cmd_auth_status = cmd_auth_status
		except Exception as e :
			raise e


	'''
	get Configuration Command
	'''
	@property
	def config_cmd(self) :
		try:
			return self._config_cmd
		except Exception as e :
			raise e
	'''
	set Configuration Command
	'''
	@config_cmd.setter
	def config_cmd(self,config_cmd):
		try :
			if not isinstance(config_cmd,str):
				raise TypeError("config_cmd must be set to str value")
			self._config_cmd = config_cmd
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
	get Category of Event
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	set Category of Event
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
	get Severity of Event
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity of Event
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,str):
				raise TypeError("severity must be set to str value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Failure Object
	'''
	@property
	def failureobj(self) :
		try:
			return self._failureobj
		except Exception as e :
			raise e
	'''
	set Failure Object
	'''
	@failureobj.setter
	def failureobj(self,failureobj):
		try :
			if not isinstance(failureobj,str):
				raise TypeError("failureobj must be set to str value")
			self._failureobj = failureobj
		except Exception as e :
			raise e

	'''
	Category list
	'''
	@property
	def category_array(self) :
		try:
			return self._category_array
		except Exception as e :
			raise e
	'''
	Category list
	'''
	@category_array.setter
	def category_array(self,category_array) :
		try :
			if not isinstance(category_array,list):
				raise TypeError("category_array must be set to array of str value")
			for item in category_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._category_array = category_array
		except Exception as e :
			raise e

	'''
	Failure Object list
	'''
	@property
	def failureobj_array(self) :
		try:
			return self._failureobj_array
		except Exception as e :
			raise e
	'''
	Failure Object list
	'''
	@failureobj_array.setter
	def failureobj_array(self,failureobj_array) :
		try :
			if not isinstance(failureobj_array,list):
				raise TypeError("failureobj_array must be set to array of str value")
			for item in failureobj_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._failureobj_array = failureobj_array
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
	Severity list
	'''
	@property
	def severity_array(self) :
		try:
			return self._severity_array
		except Exception as e :
			raise e
	'''
	Severity list
	'''
	@severity_array.setter
	def severity_array(self,severity_array) :
		try :
			if not isinstance(severity_array,list):
				raise TypeError("severity_array must be set to array of str value")
			for item in severity_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._severity_array = severity_array
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_criteria_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filter_criteria
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_criteria_responses, response, "filter_criteria_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.filter_criteria_response_array
				i=0
				error = [filter_criteria() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.filter_criteria_response_array
			i=0
			filter_criteria_objs = [filter_criteria() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_filter_criteria'):
					for props in obj._filter_criteria:
						result = service.payload_formatter.string_to_bulk_resource(filter_criteria_response,self.__class__.__name__,props)
						filter_criteria_objs[i] = result.filter_criteria
						i=i+1
			return filter_criteria_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(filter_criteria,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class filter_criteria_response(base_response):
	def __init__(self,length=1) :
		self.filter_criteria= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.filter_criteria= [ filter_criteria() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class filter_criteria_responses(base_response):
	def __init__(self,length=1) :
		self.filter_criteria_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.filter_criteria_response_array = [ filter_criteria() for _ in range(length)]
