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
Configuration for Cipher Suite resource
'''

class cipher_suite(base_resource):
	_protocol= ""
	_message_auth_code= ""
	_encryption= ""
	_cipher_suite_openssl_name= ""
	_authentication= ""
	_cipher_suite_description= ""
	_is_supported= ""
	_preference= ""
	_cipher_suite_name= ""
	_hexcode= ""
	_key_exchange= ""
	_cipher_group_list=[]
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
			return "cipher_suite"
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
			return "cipher_suites"
		except Exception as e :
			raise e


	'''
	
	'''
	@property
	def protocol(self):
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	
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
	
	'''
	@property
	def message_auth_code(self):
		try:
			return self._message_auth_code
		except Exception as e :
			raise e
	'''
	
	'''
	@message_auth_code.setter
	def message_auth_code(self,message_auth_code):
		try :
			if not isinstance(message_auth_code,str):
				raise TypeError("message_auth_code must be set to str value")
			self._message_auth_code = message_auth_code
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def encryption(self):
		try:
			return self._encryption
		except Exception as e :
			raise e
	'''
	
	'''
	@encryption.setter
	def encryption(self,encryption):
		try :
			if not isinstance(encryption,str):
				raise TypeError("encryption must be set to str value")
			self._encryption = encryption
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def cipher_suite_openssl_name(self):
		try:
			return self._cipher_suite_openssl_name
		except Exception as e :
			raise e
	'''
	
	'''
	@cipher_suite_openssl_name.setter
	def cipher_suite_openssl_name(self,cipher_suite_openssl_name):
		try :
			if not isinstance(cipher_suite_openssl_name,str):
				raise TypeError("cipher_suite_openssl_name must be set to str value")
			self._cipher_suite_openssl_name = cipher_suite_openssl_name
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def authentication(self):
		try:
			return self._authentication
		except Exception as e :
			raise e
	'''
	
	'''
	@authentication.setter
	def authentication(self,authentication):
		try :
			if not isinstance(authentication,str):
				raise TypeError("authentication must be set to str value")
			self._authentication = authentication
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def cipher_suite_description(self):
		try:
			return self._cipher_suite_description
		except Exception as e :
			raise e
	'''
	
	'''
	@cipher_suite_description.setter
	def cipher_suite_description(self,cipher_suite_description):
		try :
			if not isinstance(cipher_suite_description,str):
				raise TypeError("cipher_suite_description must be set to str value")
			self._cipher_suite_description = cipher_suite_description
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def is_supported(self):
		try:
			return self._is_supported
		except Exception as e :
			raise e
	'''
	
	'''
	@is_supported.setter
	def is_supported(self,is_supported):
		try :
			if not isinstance(is_supported,bool):
				raise TypeError("is_supported must be set to bool value")
			self._is_supported = is_supported
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def preference(self):
		try:
			return self._preference
		except Exception as e :
			raise e
	'''
	
	'''
	@preference.setter
	def preference(self,preference):
		try :
			if not isinstance(preference,int):
				raise TypeError("preference must be set to int value")
			self._preference = preference
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def cipher_suite_name(self):
		try:
			return self._cipher_suite_name
		except Exception as e :
			raise e
	'''
	
	'''
	@cipher_suite_name.setter
	def cipher_suite_name(self,cipher_suite_name):
		try :
			if not isinstance(cipher_suite_name,str):
				raise TypeError("cipher_suite_name must be set to str value")
			self._cipher_suite_name = cipher_suite_name
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def hexcode(self):
		try:
			return self._hexcode
		except Exception as e :
			raise e
	'''
	
	'''
	@hexcode.setter
	def hexcode(self,hexcode):
		try :
			if not isinstance(hexcode,str):
				raise TypeError("hexcode must be set to str value")
			self._hexcode = hexcode
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def key_exchange(self):
		try:
			return self._key_exchange
		except Exception as e :
			raise e
	'''
	
	'''
	@key_exchange.setter
	def key_exchange(self,key_exchange):
		try :
			if not isinstance(key_exchange,str):
				raise TypeError("key_exchange must be set to str value")
			self._key_exchange = key_exchange
		except Exception as e :
			raise e

	'''
	
	'''
	@property
	def cipher_group_list(self) :
		try:
			return self._cipher_group_list
		except Exception as e :
			raise e
	'''
	
	'''
	@cipher_group_list.setter
	def cipher_group_list(self,cipher_group_list) :
		try :
			if not isinstance(cipher_group_list,list):
				raise TypeError("cipher_group_list must be set to array of str value")
			for item in cipher_group_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._cipher_group_list = cipher_group_list
		except Exception as e :
			raise e

	'''
	Use this operation to get AAA server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cipher_suite_obj=cipher_suite()
				response = cipher_suite_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cipher_suite resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cipher_suite_obj = cipher_suite()
			option_ = options()
			option_._filter=filter_
			return cipher_suite_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cipher_suite resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cipher_suite_obj = cipher_suite()
			option_ = options()
			option_._count=True
			response = cipher_suite_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cipher_suite resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cipher_suite_obj = cipher_suite()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cipher_suite_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cipher_suite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cipher_suite
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cipher_suite_responses, response, "cipher_suite_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cipher_suite_response_array
				i=0
				error = [cipher_suite() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cipher_suite_response_array
			i=0
			cipher_suite_objs = [cipher_suite() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cipher_suite'):
					for props in obj._cipher_suite:
						result = service.payload_formatter.string_to_bulk_resource(cipher_suite_response,self.__class__.__name__,props)
						cipher_suite_objs[i] = result.cipher_suite
						i=i+1
			return cipher_suite_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cipher_suite,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cipher_suite_response(base_response):
	def __init__(self,length=1) :
		self.cipher_suite= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cipher_suite= [ cipher_suite() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cipher_suite_responses(base_response):
	def __init__(self,length=1) :
		self.cipher_suite_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cipher_suite_response_array = [ cipher_suite() for _ in range(length)]
