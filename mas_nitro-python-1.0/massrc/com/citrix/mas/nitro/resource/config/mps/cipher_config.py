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
Configuration for SSL Cipher Config resource
'''

class cipher_config(base_resource):
	_cipher_group_name= ""
	_config_mode= ""
	_cipher_name_list_array=[]
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
			return "cipher_config"
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
			return "cipher_configs"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def cipher_group_name(self) :
		try:
			return self._cipher_group_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@cipher_group_name.setter
	def cipher_group_name(self,cipher_group_name):
		try :
			if not isinstance(cipher_group_name,str):
				raise TypeError("cipher_group_name must be set to str value")
			self._cipher_group_name = cipher_group_name
		except Exception as e :
			raise e


	'''
	get SSL Ciphers Config Mode [CipherGroup, CipherSuites]
	'''
	@property
	def config_mode(self) :
		try:
			return self._config_mode
		except Exception as e :
			raise e
	'''
	set SSL Ciphers Config Mode [CipherGroup, CipherSuites]
	'''
	@config_mode.setter
	def config_mode(self,config_mode):
		try :
			if not isinstance(config_mode,str):
				raise TypeError("config_mode must be set to str value")
			self._config_mode = config_mode
		except Exception as e :
			raise e


	'''
	get list of cipher suites in form of array of strings
	'''
	@property
	def cipher_name_list_array(self) :
		try:
			return self._cipher_name_list_array
		except Exception as e :
			raise e
	'''
	set list of cipher suites in form of array of strings
	'''
	@cipher_name_list_array.setter
	def cipher_name_list_array(self,cipher_name_list_array) :
		try :
			if not isinstance(cipher_name_list_array,list):
				raise TypeError("cipher_name_list_array must be set to array of str value")
			for item in cipher_name_list_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._cipher_name_list_array = cipher_name_list_array
		except Exception as e :
			raise e

	'''
	Use this operation to get Cipher Group details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cipher_config_obj=cipher_config()
				response = cipher_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a Cipher Group.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				cipher_config_obj=cipher_config()
				return cls.update_bulk_request(client,resource,cipher_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cipher_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cipher_config_obj = cipher_config()
			option_ = options()
			option_._filter=filter_
			return cipher_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cipher_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cipher_config_obj = cipher_config()
			option_ = options()
			option_._count=True
			response = cipher_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cipher_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cipher_config_obj = cipher_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cipher_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cipher_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cipher_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cipher_config_responses, response, "cipher_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cipher_config_response_array
				i=0
				error = [cipher_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cipher_config_response_array
			i=0
			cipher_config_objs = [cipher_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cipher_config'):
					for props in obj._cipher_config:
						result = service.payload_formatter.string_to_bulk_resource(cipher_config_response,self.__class__.__name__,props)
						cipher_config_objs[i] = result.cipher_config
						i=i+1
			return cipher_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cipher_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cipher_config_response(base_response):
	def __init__(self,length=1) :
		self.cipher_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cipher_config= [ cipher_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cipher_config_responses(base_response):
	def __init__(self,length=1) :
		self.cipher_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cipher_config_response_array = [ cipher_config() for _ in range(length)]
