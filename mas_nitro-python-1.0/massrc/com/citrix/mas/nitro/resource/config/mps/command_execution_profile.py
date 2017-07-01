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
Configuration for Command Execution Profile resource
'''

class command_execution_profile(base_resource):
	_tenant_id= ""
	_append_errors= ""
	_id= ""
	_append_output= ""
	_command_text= ""
	_profile_name= ""
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
			return "command_execution_profile"
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
			return "command_execution_profiles"
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
	get Append Errors
	'''
	@property
	def append_errors(self) :
		try:
			return self._append_errors
		except Exception as e :
			raise e
	'''
	set Append Errors
	'''
	@append_errors.setter
	def append_errors(self,append_errors):
		try :
			if not isinstance(append_errors,bool):
				raise TypeError("append_errors must be set to bool value")
			self._append_errors = append_errors
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the run command profile.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the run command profile.
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
	get Append Output
	'''
	@property
	def append_output(self) :
		try:
			return self._append_output
		except Exception as e :
			raise e
	'''
	set Append Output
	'''
	@append_output.setter
	def append_output(self,append_output):
		try :
			if not isinstance(append_output,bool):
				raise TypeError("append_output must be set to bool value")
			self._append_output = append_output
		except Exception as e :
			raise e


	'''
	get Run Command Text
	'''
	@property
	def command_text(self) :
		try:
			return self._command_text
		except Exception as e :
			raise e
	'''
	set Run Command Text
	'''
	@command_text.setter
	def command_text(self,command_text):
		try :
			if not isinstance(command_text,str):
				raise TypeError("command_text must be set to str value")
			self._command_text = command_text
		except Exception as e :
			raise e


	'''
	get Profile name for the run command setting.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name for the run command setting.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Use this operation to add command execution profile..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				command_execution_profile_obj= command_execution_profile()
				return cls.perform_operation_bulk_request(service,"add", resource,command_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete command execution profile..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					command_execution_profile_obj=command_execution_profile()
					return cls.delete_bulk_request(client,resource,command_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get command execution profile..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				command_execution_profile_obj=command_execution_profile()
				response = command_execution_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify command execution profile..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				command_execution_profile_obj=command_execution_profile()
				return cls.update_bulk_request(client,resource,command_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of command_execution_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			command_execution_profile_obj = command_execution_profile()
			option_ = options()
			option_._filter=filter_
			return command_execution_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the command_execution_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			command_execution_profile_obj = command_execution_profile()
			option_ = options()
			option_._count=True
			response = command_execution_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of command_execution_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			command_execution_profile_obj = command_execution_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = command_execution_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(command_execution_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.command_execution_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(command_execution_profile_responses, response, "command_execution_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.command_execution_profile_response_array
				i=0
				error = [command_execution_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.command_execution_profile_response_array
			i=0
			command_execution_profile_objs = [command_execution_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_command_execution_profile'):
					for props in obj._command_execution_profile:
						result = service.payload_formatter.string_to_bulk_resource(command_execution_profile_response,self.__class__.__name__,props)
						command_execution_profile_objs[i] = result.command_execution_profile
						i=i+1
			return command_execution_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(command_execution_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class command_execution_profile_response(base_response):
	def __init__(self,length=1) :
		self.command_execution_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.command_execution_profile= [ command_execution_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class command_execution_profile_responses(base_response):
	def __init__(self,length=1) :
		self.command_execution_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.command_execution_profile_response_array = [ command_execution_profile() for _ in range(length)]
