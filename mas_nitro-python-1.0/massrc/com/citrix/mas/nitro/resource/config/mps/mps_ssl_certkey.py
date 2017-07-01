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
Configuration for Install SSL certificate on Management Service resource
'''

class mps_ssl_certkey(base_resource):
	_serial_number= ""
	_signature_algorithm= ""
	_valid_from= ""
	_status= ""
	_issuer= ""
	_public_key_size= ""
	_password= ""
	_ssl_key= ""
	_valid_to= ""
	_version= ""
	_subject= ""
	_public_key_algorithm= ""
	_days_to_expiry= ""
	_ssl_certificate= ""
	_fingerprint= ""
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
			return "mps_ssl_certkey"
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
			return "mps_ssl_certkeys"
		except Exception as e :
			raise e



	'''
	get Serial Number
	'''
	@property
	def serial_number(self) :
		try:
			return self._serial_number
		except Exception as e :
			raise e


	'''
	get Signature Algorithm
	'''
	@property
	def signature_algorithm(self) :
		try:
			return self._signature_algorithm
		except Exception as e :
			raise e


	'''
	get Valid From
	'''
	@property
	def valid_from(self) :
		try:
			return self._valid_from
		except Exception as e :
			raise e


	'''
	get Tells whether the certificate is still valid or not
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Issuer
	'''
	@property
	def issuer(self) :
		try:
			return self._issuer
		except Exception as e :
			raise e


	'''
	get Public Key Size
	'''
	@property
	def public_key_size(self) :
		try:
			return self._public_key_size
		except Exception as e :
			raise e


	'''
	get The pass-phrase that was used to encrypt the private-key.
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set The pass-phrase that was used to encrypt the private-key.
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
	get Key
	'''
	@property
	def ssl_key(self) :
		try:
			return self._ssl_key
		except Exception as e :
			raise e
	'''
	set Key
	'''
	@ssl_key.setter
	def ssl_key(self,ssl_key):
		try :
			if not isinstance(ssl_key,str):
				raise TypeError("ssl_key must be set to str value")
			self._ssl_key = ssl_key
		except Exception as e :
			raise e


	'''
	get Valid To
	'''
	@property
	def valid_to(self) :
		try:
			return self._valid_to
		except Exception as e :
			raise e


	'''
	get Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get Subject
	'''
	@property
	def subject(self) :
		try:
			return self._subject
		except Exception as e :
			raise e


	'''
	get Public Key Algorithm
	'''
	@property
	def public_key_algorithm(self) :
		try:
			return self._public_key_algorithm
		except Exception as e :
			raise e


	'''
	get Days before SSL certificate expires
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e


	'''
	get Certificate
	'''
	@property
	def ssl_certificate(self) :
		try:
			return self._ssl_certificate
		except Exception as e :
			raise e
	'''
	set Certificate
	'''
	@ssl_certificate.setter
	def ssl_certificate(self,ssl_certificate):
		try :
			if not isinstance(ssl_certificate,str):
				raise TypeError("ssl_certificate must be set to str value")
			self._ssl_certificate = ssl_certificate
		except Exception as e :
			raise e

	'''
	SHA-1 Fingerprint of MAS SSL Certificate
	'''
	@property
	def fingerprint(self):
		try:
			return self._fingerprint
		except Exception as e :
			raise e
	'''
	SHA-1 Fingerprint of MAS SSL Certificate
	'''
	@fingerprint.setter
	def fingerprint(self,fingerprint):
		try :
			if not isinstance(fingerprint,str):
				raise TypeError("fingerprint must be set to str value")
			self._fingerprint = fingerprint
		except Exception as e :
			raise e

	'''
	Use this operation to install certificate on Management Service.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				mps_ssl_certkey_obj= mps_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"add", resource,mps_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get certificate on Management Service.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_ssl_certkey_obj=mps_ssl_certkey()
				response = mps_ssl_certkey_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_ssl_certkey_obj = mps_ssl_certkey()
			option_ = options()
			option_._filter=filter_
			return mps_ssl_certkey_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_ssl_certkey resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_ssl_certkey_obj = mps_ssl_certkey()
			option_ = options()
			option_._count=True
			response = mps_ssl_certkey_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_ssl_certkey_obj = mps_ssl_certkey()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_ssl_certkey_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_ssl_certkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_ssl_certkey
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_ssl_certkey_responses, response, "mps_ssl_certkey_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_ssl_certkey_response_array
				i=0
				error = [mps_ssl_certkey() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_ssl_certkey_response_array
			i=0
			mps_ssl_certkey_objs = [mps_ssl_certkey() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_ssl_certkey'):
					for props in obj._mps_ssl_certkey:
						result = service.payload_formatter.string_to_bulk_resource(mps_ssl_certkey_response,self.__class__.__name__,props)
						mps_ssl_certkey_objs[i] = result.mps_ssl_certkey
						i=i+1
			return mps_ssl_certkey_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_ssl_certkey,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_ssl_certkey_response(base_response):
	def __init__(self,length=1) :
		self.mps_ssl_certkey= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_ssl_certkey= [ mps_ssl_certkey() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_ssl_certkey_responses(base_response):
	def __init__(self,length=1) :
		self.mps_ssl_certkey_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_ssl_certkey_response_array = [ mps_ssl_certkey() for _ in range(length)]
