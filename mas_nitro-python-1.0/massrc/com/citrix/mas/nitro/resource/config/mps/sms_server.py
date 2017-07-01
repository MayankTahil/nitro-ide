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
Configuration for SMS server properties  resource
'''

class sms_server(base_resource):
	_optional2_val1= ""
	_optional1_val= ""
	_to_seperater= ""
	_username_val= ""
	_to_key= ""
	_tenant_id= ""
	_optional3_key= ""
	_id= ""
	_is_ssl= ""
	_optional3_val= ""
	_base_url= ""
	_username_key= ""
	_optional2_key= ""
	_optional1_key= ""
	_message_key= ""
	_message_word_sperater= ""
	_type= ""
	_password_val= ""
	_password_key= ""
	_server_name= ""
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
			return "sms_server"
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
			return "sms_servers"
		except Exception as e :
			raise e



	'''
	get Optional2 Val for the sms server
	'''
	@property
	def optional2_val1(self) :
		try:
			return self._optional2_val1
		except Exception as e :
			raise e


	'''
	get Optional1 Val for the sms server
	'''
	@property
	def optional1_val(self) :
		try:
			return self._optional1_val
		except Exception as e :
			raise e
	'''
	set Optional1 Val for the sms server
	'''
	@optional1_val.setter
	def optional1_val(self,optional1_val):
		try :
			if not isinstance(optional1_val,str):
				raise TypeError("optional1_val must be set to str value")
			self._optional1_val = optional1_val
		except Exception as e :
			raise e


	'''
	get To list seperater for the sms server
	'''
	@property
	def to_seperater(self) :
		try:
			return self._to_seperater
		except Exception as e :
			raise e
	'''
	set To list seperater for the sms server
	'''
	@to_seperater.setter
	def to_seperater(self,to_seperater):
		try :
			if not isinstance(to_seperater,str):
				raise TypeError("to_seperater must be set to str value")
			self._to_seperater = to_seperater
		except Exception as e :
			raise e


	'''
	get Username val for the sms server
	'''
	@property
	def username_val(self) :
		try:
			return self._username_val
		except Exception as e :
			raise e
	'''
	set Username val for the sms server
	'''
	@username_val.setter
	def username_val(self,username_val):
		try :
			if not isinstance(username_val,str):
				raise TypeError("username_val must be set to str value")
			self._username_val = username_val
		except Exception as e :
			raise e


	'''
	get To key for the sms server
	'''
	@property
	def to_key(self) :
		try:
			return self._to_key
		except Exception as e :
			raise e
	'''
	set To key for the sms server
	'''
	@to_key.setter
	def to_key(self,to_key):
		try :
			if not isinstance(to_key,str):
				raise TypeError("to_key must be set to str value")
			self._to_key = to_key
		except Exception as e :
			raise e


	'''
	get Tenant Id of the Config Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Optional3 key for the sms server
	'''
	@property
	def optional3_key(self) :
		try:
			return self._optional3_key
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the sms server
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sms server
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
	get Is SSL support configured.
	'''
	@property
	def is_ssl(self) :
		try:
			return self._is_ssl
		except Exception as e :
			raise e
	'''
	set Is SSL support configured.
	'''
	@is_ssl.setter
	def is_ssl(self,is_ssl):
		try :
			if not isinstance(is_ssl,bool):
				raise TypeError("is_ssl must be set to bool value")
			self._is_ssl = is_ssl
		except Exception as e :
			raise e


	'''
	get Optional3 Val for the sms server
	'''
	@property
	def optional3_val(self) :
		try:
			return self._optional3_val
		except Exception as e :
			raise e


	'''
	get Base URL for the sms server, without payload
	'''
	@property
	def base_url(self) :
		try:
			return self._base_url
		except Exception as e :
			raise e
	'''
	set Base URL for the sms server, without payload
	'''
	@base_url.setter
	def base_url(self,base_url):
		try :
			if not isinstance(base_url,str):
				raise TypeError("base_url must be set to str value")
			self._base_url = base_url
		except Exception as e :
			raise e


	'''
	get Username key for the sms server
	'''
	@property
	def username_key(self) :
		try:
			return self._username_key
		except Exception as e :
			raise e
	'''
	set Username key for the sms server
	'''
	@username_key.setter
	def username_key(self,username_key):
		try :
			if not isinstance(username_key,str):
				raise TypeError("username_key must be set to str value")
			self._username_key = username_key
		except Exception as e :
			raise e


	'''
	get Optional2 key for the sms server
	'''
	@property
	def optional2_key(self) :
		try:
			return self._optional2_key
		except Exception as e :
			raise e


	'''
	get Optional1 key for the sms server
	'''
	@property
	def optional1_key(self) :
		try:
			return self._optional1_key
		except Exception as e :
			raise e
	'''
	set Optional1 key for the sms server
	'''
	@optional1_key.setter
	def optional1_key(self,optional1_key):
		try :
			if not isinstance(optional1_key,str):
				raise TypeError("optional1_key must be set to str value")
			self._optional1_key = optional1_key
		except Exception as e :
			raise e


	'''
	get Message key for the sms server
	'''
	@property
	def message_key(self) :
		try:
			return self._message_key
		except Exception as e :
			raise e
	'''
	set Message key for the sms server
	'''
	@message_key.setter
	def message_key(self,message_key):
		try :
			if not isinstance(message_key,str):
				raise TypeError("message_key must be set to str value")
			self._message_key = message_key
		except Exception as e :
			raise e


	'''
	get Message Word Seperater for the sms server
	'''
	@property
	def message_word_sperater(self) :
		try:
			return self._message_word_sperater
		except Exception as e :
			raise e
	'''
	set Message Word Seperater for the sms server
	'''
	@message_word_sperater.setter
	def message_word_sperater(self,message_word_sperater):
		try :
			if not isinstance(message_word_sperater,str):
				raise TypeError("message_word_sperater must be set to str value")
			self._message_word_sperater = message_word_sperater
		except Exception as e :
			raise e


	'''
	get HTTP type supported for the sms server
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set HTTP type supported for the sms server
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Password Val for the sms server
	'''
	@property
	def password_val(self) :
		try:
			return self._password_val
		except Exception as e :
			raise e
	'''
	set Password Val for the sms server
	'''
	@password_val.setter
	def password_val(self,password_val):
		try :
			if not isinstance(password_val,str):
				raise TypeError("password_val must be set to str value")
			self._password_val = password_val
		except Exception as e :
			raise e


	'''
	get Password key for the sms server
	'''
	@property
	def password_key(self) :
		try:
			return self._password_key
		except Exception as e :
			raise e
	'''
	set Password key for the sms server
	'''
	@password_key.setter
	def password_key(self,password_key):
		try :
			if not isinstance(password_key,str):
				raise TypeError("password_key must be set to str value")
			self._password_key = password_key
		except Exception as e :
			raise e


	'''
	get SMS server name
	'''
	@property
	def server_name(self) :
		try:
			return self._server_name
		except Exception as e :
			raise e
	'''
	set SMS server name
	'''
	@server_name.setter
	def server_name(self,server_name):
		try :
			if not isinstance(server_name,str):
				raise TypeError("server_name must be set to str value")
			self._server_name = server_name
		except Exception as e :
			raise e

	'''
	Use this operation to add sms server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				sms_server_obj= sms_server()
				return cls.perform_operation_bulk_request(service,"add", resource,sms_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete sms server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					sms_server_obj=sms_server()
					return cls.delete_bulk_request(client,resource,sms_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get sms server details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sms_server_obj=sms_server()
				response = sms_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify sms server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				sms_server_obj=sms_server()
				return cls.update_bulk_request(client,resource,sms_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sms_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sms_server_obj = sms_server()
			option_ = options()
			option_._filter=filter_
			return sms_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sms_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sms_server_obj = sms_server()
			option_ = options()
			option_._count=True
			response = sms_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sms_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sms_server_obj = sms_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sms_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sms_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sms_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sms_server_responses, response, "sms_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sms_server_response_array
				i=0
				error = [sms_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sms_server_response_array
			i=0
			sms_server_objs = [sms_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sms_server'):
					for props in obj._sms_server:
						result = service.payload_formatter.string_to_bulk_resource(sms_server_response,self.__class__.__name__,props)
						sms_server_objs[i] = result.sms_server
						i=i+1
			return sms_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sms_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sms_server_response(base_response):
	def __init__(self,length=1) :
		self.sms_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sms_server= [ sms_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sms_server_responses(base_response):
	def __init__(self,length=1) :
		self.sms_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sms_server_response_array = [ sms_server() for _ in range(length)]
