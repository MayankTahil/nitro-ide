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
Configuration for Activity Status resource
'''

class config_advice_result(base_resource):
	_parent_name= ""
	_modification_status_message= ""
	_issue= ""
	_parent_id= ""
	_modification_status= ""
	_corrective_command= ""
	_id= ""
	_category= ""
	_severity= ""
	_advice= ""
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
			return "config_advice_result"
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
			return "config_advice_results"
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
	get Command Deployment message
	'''
	@property
	def modification_status_message(self) :
		try:
			return self._modification_status_message
		except Exception as e :
			raise e
	'''
	set Command Deployment message
	'''
	@modification_status_message.setter
	def modification_status_message(self,modification_status_message):
		try :
			if not isinstance(modification_status_message,str):
				raise TypeError("modification_status_message must be set to str value")
			self._modification_status_message = modification_status_message
		except Exception as e :
			raise e


	'''
	get Issue
	'''
	@property
	def issue(self) :
		try:
			return self._issue
		except Exception as e :
			raise e
	'''
	set Issue
	'''
	@issue.setter
	def issue(self,issue):
		try :
			if not isinstance(issue,str):
				raise TypeError("issue must be set to str value")
			self._issue = issue
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
	get Command Deployment Status
	'''
	@property
	def modification_status(self) :
		try:
			return self._modification_status
		except Exception as e :
			raise e
	'''
	set Command Deployment Status
	'''
	@modification_status.setter
	def modification_status(self,modification_status):
		try :
			if not isinstance(modification_status,bool):
				raise TypeError("modification_status must be set to bool value")
			self._modification_status = modification_status
		except Exception as e :
			raise e


	'''
	get Command
	'''
	@property
	def corrective_command(self) :
		try:
			return self._corrective_command
		except Exception as e :
			raise e
	'''
	set Command
	'''
	@corrective_command.setter
	def corrective_command(self,corrective_command):
		try :
			if not isinstance(corrective_command,str):
				raise TypeError("corrective_command must be set to str value")
			self._corrective_command = corrective_command
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
	get Category
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	set Category
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
	get Severity
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity
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
	get Advice
	'''
	@property
	def advice(self) :
		try:
			return self._advice
		except Exception as e :
			raise e
	'''
	set Advice
	'''
	@advice.setter
	def advice(self,advice):
		try :
			if not isinstance(advice,str):
				raise TypeError("advice must be set to str value")
			self._advice = advice
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_advice_result_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_advice_result
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_advice_result_responses, response, "config_advice_result_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_advice_result_response_array
				i=0
				error = [config_advice_result() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_advice_result_response_array
			i=0
			config_advice_result_objs = [config_advice_result() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_advice_result'):
					for props in obj._config_advice_result:
						result = service.payload_formatter.string_to_bulk_resource(config_advice_result_response,self.__class__.__name__,props)
						config_advice_result_objs[i] = result.config_advice_result
						i=i+1
			return config_advice_result_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_advice_result,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_advice_result_response(base_response):
	def __init__(self,length=1) :
		self.config_advice_result= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_advice_result= [ config_advice_result() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_advice_result_responses(base_response):
	def __init__(self,length=1) :
		self.config_advice_result_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_advice_result_response_array = [ config_advice_result() for _ in range(length)]
