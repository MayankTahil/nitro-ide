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
Configuration for CLI Prompt string resource
'''

class cli_prompt(base_resource):
	_promptString= ""
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
			return "cli_prompt"
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
			return "cli_prompts"
		except Exception as e :
			raise e


	'''
	The prompt string.  The following special values are allowed:
		%! - will be replaced by the history event number
		%u - will be replaced by the NetScaler SVM user name
		%h - will be replaced by the NetScaler SVM hostname
		%t - will be replaced by the current time (12 hr)
		%T - will be replaced by the current time (24 hr)
		%d - will be replaced by the current date (yy/mm/dd)
This is a mandatory argument.
	'''
	@property
	def promptString(self):
		try:
			return self._promptString
		except Exception as e :
			raise e
	'''
	The prompt string.  The following special values are allowed:
		%! - will be replaced by the history event number
		%u - will be replaced by the NetScaler SVM user name
		%h - will be replaced by the NetScaler SVM hostname
		%t - will be replaced by the current time (12 hr)
		%T - will be replaced by the current time (24 hr)
		%d - will be replaced by the current date (yy/mm/dd)
This is a mandatory argument.
	'''
	@promptString.setter
	def promptString(self,promptString):
		try :
			if not isinstance(promptString,str):
				raise TypeError("promptString must be set to str value")
			self._promptString = promptString
		except Exception as e :
			raise e

	'''
	Use this operation to set CLI prompt.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				cli_prompt_obj=cli_prompt()
				return cls.update_bulk_request(client,resource,cli_prompt_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cli_prompt_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cli_prompt
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cli_prompt_responses, response, "cli_prompt_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cli_prompt_response_array
				i=0
				error = [cli_prompt() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cli_prompt_response_array
			i=0
			cli_prompt_objs = [cli_prompt() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cli_prompt'):
					for props in obj._cli_prompt:
						result = service.payload_formatter.string_to_bulk_resource(cli_prompt_response,self.__class__.__name__,props)
						cli_prompt_objs[i] = result.cli_prompt
						i=i+1
			return cli_prompt_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cli_prompt,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cli_prompt_response(base_response):
	def __init__(self,length=1) :
		self.cli_prompt= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cli_prompt= [ cli_prompt() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cli_prompt_responses(base_response):
	def __init__(self,length=1) :
		self.cli_prompt_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cli_prompt_response_array = [ cli_prompt() for _ in range(length)]
