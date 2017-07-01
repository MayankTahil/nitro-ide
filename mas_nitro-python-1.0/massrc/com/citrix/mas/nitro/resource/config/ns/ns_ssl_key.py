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
Configuration for NS SSL key File resource
'''

class ns_ssl_key(base_resource):
	_tenant_name= ""
	_keysize= ""
	_file_size= ""
	_file_last_modified= ""
	_keyform= ""
	_des_type= ""
	_file_location_path= ""
	_password= ""
	_algo= ""
	_file_name= ""
	_exponent= ""
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
			return "ns_ssl_key"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "ns_ssl_keys"
		except Exception as e :
			raise e



	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get Key Size in bits
	'''
	@property
	def keysize(self) :
		try:
			return self._keysize
		except Exception as e :
			raise e
	'''
	set Key Size in bits
	'''
	@keysize.setter
	def keysize(self,keysize):
		try :
			if not isinstance(keysize,int):
				raise TypeError("keysize must be set to int value")
			self._keysize = keysize
		except Exception as e :
			raise e


	'''
	get file_size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get Last Modified
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get Key Form
	'''
	@property
	def keyform(self) :
		try:
			return self._keyform
		except Exception as e :
			raise e
	'''
	set Key Form
	'''
	@keyform.setter
	def keyform(self,keyform):
		try :
			if not isinstance(keyform,str):
				raise TypeError("keyform must be set to str value")
			self._keyform = keyform
		except Exception as e :
			raise e


	'''
	get DES Encryption type possible values des|des3.
	'''
	@property
	def des_type(self) :
		try:
			return self._des_type
		except Exception as e :
			raise e
	'''
	set DES Encryption type possible values des|des3.
	'''
	@des_type.setter
	def des_type(self,des_type):
		try :
			if not isinstance(des_type,str):
				raise TypeError("des_type must be set to str value")
			self._des_type = des_type
		except Exception as e :
			raise e


	'''
	get File Location on Client for upload/download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Encryption Algorithm supported RSA and DSA.
	'''
	@property
	def algo(self) :
		try:
			return self._algo
		except Exception as e :
			raise e
	'''
	set Encryption Algorithm supported RSA and DSA.
	'''
	@algo.setter
	def algo(self,algo):
		try :
			if not isinstance(algo,str):
				raise TypeError("algo must be set to str value")
			self._algo = algo
		except Exception as e :
			raise e


	'''
	get Key File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Key File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Exponent
	'''
	@property
	def exponent(self) :
		try:
			return self._exponent
		except Exception as e :
			raise e
	'''
	set Exponent
	'''
	@exponent.setter
	def exponent(self,exponent):
		try :
			if not isinstance(exponent,str):
				raise TypeError("exponent must be set to str value")
			self._exponent = exponent
		except Exception as e :
			raise e

	'''
	Use this operation to create ns ssl key file.
	'''
	@classmethod
	def create(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"create")
			else : 
				ns_ssl_key_obj= ns_ssl_key()
				return cls.perform_operation_bulk_request(service,"create", resource,ns_ssl_key_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload ns ssl key file.
	'''

	'''
	Use this operation to upload ns ssl key file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to delete ns ssl key file.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_ssl_key_obj=ns_ssl_key()
					return cls.delete_bulk_request(client,resource,ns_ssl_key_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get ns ssl key file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_ssl_key_obj=ns_ssl_key()
				response = ns_ssl_key_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to download ns ssl key file.
	'''

	'''
	Use this operation to download ns ssl key file.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_key resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_key_obj = ns_ssl_key()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_key_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_key resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_key_obj = ns_ssl_key()
			option_ = options()
			option_._count=True
			response = ns_ssl_key_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_key resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_key_obj = ns_ssl_key()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_key_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_key_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_key
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_key_responses, response, "ns_ssl_key_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_key_response_array
				i=0
				error = [ns_ssl_key() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_key_response_array
			i=0
			ns_ssl_key_objs = [ns_ssl_key() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_key'):
					for props in obj._ns_ssl_key:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_key_response,self.__class__.__name__,props)
						ns_ssl_key_objs[i] = result.ns_ssl_key
						i=i+1
			return ns_ssl_key_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_key,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_key_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_key= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_key= [ ns_ssl_key() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_key_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_key_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_key_response_array = [ ns_ssl_key() for _ in range(length)]
