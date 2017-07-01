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
from massrc.com.citrix.mas.nitro.resource.config.mps.config_advice_result import config_advice_result


'''
Configuration for Config Advice resource
'''

class config_advice(base_resource):
	_is_xendesktop= ""
	_output_file= ""
	_is_pci= ""
	_config_advice_results=[]
	_ip_address= ""
	_id= ""
	_command= ""
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
			return "config_advice"
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
			return "config_advices"
		except Exception as e :
			raise e



	'''
	get Enables search for Xen Desktop properties 
	'''
	@property
	def is_xendesktop(self) :
		try:
			return self._is_xendesktop
		except Exception as e :
			raise e
	'''
	set Enables search for Xen Desktop properties 
	'''
	@is_xendesktop.setter
	def is_xendesktop(self,is_xendesktop):
		try :
			if not isinstance(is_xendesktop,bool):
				raise TypeError("is_xendesktop must be set to bool value")
			self._is_xendesktop = is_xendesktop
		except Exception as e :
			raise e


	'''
	get File Path
	'''
	@property
	def output_file(self) :
		try:
			return self._output_file
		except Exception as e :
			raise e
	'''
	set File Path
	'''
	@output_file.setter
	def output_file(self,output_file):
		try :
			if not isinstance(output_file,str):
				raise TypeError("output_file must be set to str value")
			self._output_file = output_file
		except Exception as e :
			raise e


	'''
	get Enables search for PCI properties
	'''
	@property
	def is_pci(self) :
		try:
			return self._is_pci
		except Exception as e :
			raise e
	'''
	set Enables search for PCI properties
	'''
	@is_pci.setter
	def is_pci(self,is_pci):
		try :
			if not isinstance(is_pci,bool):
				raise TypeError("is_pci must be set to bool value")
			self._is_pci = is_pci
		except Exception as e :
			raise e


	'''
	get config advice result
	'''
	@property
	def config_advice_results(self) :
		try:
			return self._config_advice_results
		except Exception as e :
			raise e
	'''
	set config advice result
	'''
	@config_advice_results.setter
	def config_advice_results(self,config_advice_results) :
		try :
			if not isinstance(config_advice_results,list):
				raise TypeError("config_advice_results must be set to array of config_advice_result value")
			for item in config_advice_results :
				if not isinstance(item,config_advice_result):
					raise TypeError("item must be set to config_advice_result value")
			self._config_advice_results = config_advice_results
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
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
	get Commands
	'''
	@property
	def command(self) :
		try:
			return self._command
		except Exception as e :
			raise e
	'''
	set Commands
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
	Use this operation to get config advice.
	'''
	@classmethod
	def custom(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"custom")
			else : 
				config_advice_obj= config_advice()
				return cls.perform_operation_bulk_request(service,"custom", resource,config_advice_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get config advice.
	'''
	@classmethod
	def download(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"download")
			else : 
				config_advice_obj= config_advice()
				return cls.perform_operation_bulk_request(service,"download", resource,config_advice_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_advice_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_advice
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_advice_responses, response, "config_advice_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_advice_response_array
				i=0
				error = [config_advice() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_advice_response_array
			i=0
			config_advice_objs = [config_advice() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_advice'):
					for props in obj._config_advice:
						result = service.payload_formatter.string_to_bulk_resource(config_advice_response,self.__class__.__name__,props)
						config_advice_objs[i] = result.config_advice
						i=i+1
			return config_advice_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_advice,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_advice_response(base_response):
	def __init__(self,length=1) :
		self.config_advice= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_advice= [ config_advice() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_advice_responses(base_response):
	def __init__(self,length=1) :
		self.config_advice_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_advice_response_array = [ config_advice() for _ in range(length)]
