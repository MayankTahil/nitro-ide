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
Configuration for Configuration Commands for use in configuration template resource
'''

class eventrule_config_command(base_resource):
	_protocol= ""
	_index= ""
	_parent_name= ""
	_timeout= ""
	_nitro_payload= ""
	_nitro_resource= ""
	_id= ""
	_nitro_method= ""
	_command= ""
	_parent_id= ""
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
			return "eventrule_config_command"
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
			return "eventrule_config_commands"
		except Exception as e :
			raise e



	'''
	get Protocol used by Configuration Command: SSH|SCP|SFTP|NITRO
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set Protocol used by Configuration Command: SSH|SCP|SFTP|NITRO
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,str):
				raise TypeError("protocol must be set to str value")
			self._protocol = protocol
		except Exception as e :
			raise e


	'''
	get Index that stores the position of the command in a command array
	'''
	@property
	def index(self) :
		try:
			return self._index
		except Exception as e :
			raise e
	'''
	set Index that stores the position of the command in a command array
	'''
	@index.setter
	def index(self,index):
		try :
			if not isinstance(index,int):
				raise TypeError("index must be set to int value")
			self._index = index
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
	get Command Timeout in secs
	'''
	@property
	def timeout(self) :
		try:
			return self._timeout
		except Exception as e :
			raise e
	'''
	set Command Timeout in secs
	'''
	@timeout.setter
	def timeout(self,timeout):
		try :
			if not isinstance(timeout,int):
				raise TypeError("timeout must be set to int value")
			self._timeout = timeout
		except Exception as e :
			raise e


	'''
	get NITRO Request Payload
	'''
	@property
	def nitro_payload(self) :
		try:
			return self._nitro_payload
		except Exception as e :
			raise e
	'''
	set NITRO Request Payload
	'''
	@nitro_payload.setter
	def nitro_payload(self,nitro_payload):
		try :
			if not isinstance(nitro_payload,str):
				raise TypeError("nitro_payload must be set to str value")
			self._nitro_payload = nitro_payload
		except Exception as e :
			raise e


	'''
	get NITRO Resource Name
	'''
	@property
	def nitro_resource(self) :
		try:
			return self._nitro_resource
		except Exception as e :
			raise e
	'''
	set NITRO Resource Name
	'''
	@nitro_resource.setter
	def nitro_resource(self,nitro_resource):
		try :
			if not isinstance(nitro_resource,str):
				raise TypeError("nitro_resource must be set to str value")
			self._nitro_resource = nitro_resource
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
	get NITRO Request Method: POST|PUT|DELETE
	'''
	@property
	def nitro_method(self) :
		try:
			return self._nitro_method
		except Exception as e :
			raise e
	'''
	set NITRO Request Method: POST|PUT|DELETE
	'''
	@nitro_method.setter
	def nitro_method(self,nitro_method):
		try :
			if not isinstance(nitro_method,str):
				raise TypeError("nitro_method must be set to str value")
			self._nitro_method = nitro_method
		except Exception as e :
			raise e


	'''
	get Command String for Protocols SSH|SCP|SFTP
	'''
	@property
	def command(self) :
		try:
			return self._command
		except Exception as e :
			raise e
	'''
	set Command String for Protocols SSH|SCP|SFTP
	'''
	@command.setter
	def command(self,command):
		try :
			if not isinstance(command,str):
				raise TypeError("command must be set to str value")
			self._command = command
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
	Use this API to fetch filtered set of eventrule_config_command resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			eventrule_config_command_obj = eventrule_config_command()
			option_ = options()
			option_._filter=filter_
			return eventrule_config_command_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the eventrule_config_command resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			eventrule_config_command_obj = eventrule_config_command()
			option_ = options()
			option_._count=True
			response = eventrule_config_command_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of eventrule_config_command resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			eventrule_config_command_obj = eventrule_config_command()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = eventrule_config_command_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(eventrule_config_command_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.eventrule_config_command
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(eventrule_config_command_responses, response, "eventrule_config_command_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.eventrule_config_command_response_array
				i=0
				error = [eventrule_config_command() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.eventrule_config_command_response_array
			i=0
			eventrule_config_command_objs = [eventrule_config_command() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_eventrule_config_command'):
					for props in obj._eventrule_config_command:
						result = service.payload_formatter.string_to_bulk_resource(eventrule_config_command_response,self.__class__.__name__,props)
						eventrule_config_command_objs[i] = result.eventrule_config_command
						i=i+1
			return eventrule_config_command_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(eventrule_config_command,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class eventrule_config_command_response(base_response):
	def __init__(self,length=1) :
		self.eventrule_config_command= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.eventrule_config_command= [ eventrule_config_command() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class eventrule_config_command_responses(base_response):
	def __init__(self,length=1) :
		self.eventrule_config_command_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.eventrule_config_command_response_array = [ eventrule_config_command() for _ in range(length)]
