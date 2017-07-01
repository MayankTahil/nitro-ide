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
Configuration for SSL certificate on NetScaler resource
'''

class ns_ssl_certkey(base_resource):
	_serial_number= ""
	_signature_algorithm= ""
	_valid_from= ""
	_status= ""
	_hostname= ""
	_issuer= ""
	_no_domain_check= ""
	_ns_ip_address= ""
	_certkeypair_name= ""
	_public_key_size= ""
	_device_name= ""
	_ssl_key= ""
	_id= ""
	_key_data= ""
	_valid_to= ""
	_subject= ""
	_version= ""
	_public_key_algorithm= ""
	_days_to_expiry= ""
	_poll_time= ""
	_display_name= ""
	_no_of_bound_entities= ""
	_ssl_certificate= ""
	_certificate_data= ""
	_file_location_path= ""
	_partition_name= ""
	_cert_format= ""
	_certchainbinding=[]
	_save_config= ""
	_password= ""
	_csr= ""
	_ns_ip_address_arr=[]
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
			return "ns_ssl_certkey"
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
			return self._file_location_path
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "ns_ssl_certkeys"
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
	get Host Name of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
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
	get Specify this option to override the check for matching domain names during certificate update operation
	'''
	@property
	def no_domain_check(self) :
		try:
			return self._no_domain_check
		except Exception as e :
			raise e
	'''
	set Specify this option to override the check for matching domain names during certificate update operation
	'''
	@no_domain_check.setter
	def no_domain_check(self,no_domain_check):
		try :
			if not isinstance(no_domain_check,bool):
				raise TypeError("no_domain_check must be set to bool value")
			self._no_domain_check = no_domain_check
		except Exception as e :
			raise e


	'''
	get List of NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set List of NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get Cert Key Pair Name
	'''
	@property
	def certkeypair_name(self) :
		try:
			return self._certkeypair_name
		except Exception as e :
			raise e
	'''
	set Cert Key Pair Name
	'''
	@certkeypair_name.setter
	def certkeypair_name(self,certkeypair_name):
		try :
			if not isinstance(certkeypair_name,str):
				raise TypeError("certkeypair_name must be set to str value")
			self._certkeypair_name = certkeypair_name
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
	get Name of the device
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
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
	get Id is system generated key for all ssl cert-keys entries. For download operation "id" must be provided in the format <ns_ip_address>_<certkeypair_name>.tgz
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all ssl cert-keys entries. For download operation "id" must be provided in the format <ns_ip_address>_<certkeypair_name>.tgz
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
	get Key Data
	'''
	@property
	def key_data(self) :
		try:
			return self._key_data
		except Exception as e :
			raise e
	'''
	set Key Data
	'''
	@key_data.setter
	def key_data(self,key_data):
		try :
			if not isinstance(key_data,str):
				raise TypeError("key_data must be set to str value")
			self._key_data = key_data
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
	get Subject
	'''
	@property
	def subject(self) :
		try:
			return self._subject
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
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get Display Name of the device
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get no_of_bound_entities
	'''
	@property
	def no_of_bound_entities(self) :
		try:
			return self._no_of_bound_entities
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
	get Certificate Data
	'''
	@property
	def certificate_data(self) :
		try:
			return self._certificate_data
		except Exception as e :
			raise e
	'''
	set Certificate Data
	'''
	@certificate_data.setter
	def certificate_data(self,certificate_data):
		try :
			if not isinstance(certificate_data,str):
				raise TypeError("certificate_data must be set to str value")
			self._certificate_data = certificate_data
		except Exception as e :
			raise e


	'''
	get File Location on Client for download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for download
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
	get Name of Admin Partition. Blank means Default Partition
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Certificate Format
	'''
	@property
	def cert_format(self) :
		try:
			return self._cert_format
		except Exception as e :
			raise e
	'''
	set Certificate Format
	'''
	@cert_format.setter
	def cert_format(self,cert_format):
		try :
			if not isinstance(cert_format,str):
				raise TypeError("cert_format must be set to str value")
			self._cert_format = cert_format
		except Exception as e :
			raise e

	'''
	Certificate Chain binding.
	'''
	@property
	def certchainbinding(self) :
		try:
			return self._certchainbinding
		except Exception as e :
			raise e
	'''
	Certificate Chain binding.
	'''
	@certchainbinding.setter
	def certchainbinding(self,certchainbinding) :
		try :
			if not isinstance(certchainbinding,list):
				raise TypeError("certchainbinding must be set to array of str value")
			for item in certchainbinding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._certchainbinding = certchainbinding
		except Exception as e :
			raise e

	'''
	true, if save config is required
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	true, if save config is required
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e

	'''
	The pass-phrase that was used to encrypt the private-key.
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	The pass-phrase that was used to encrypt the private-key.
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
	Certificate Signing Request
	'''
	@property
	def csr(self):
		try:
			return self._csr
		except Exception as e :
			raise e

	'''
	List of NetScaler IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	List of NetScaler IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e

	'''
	Use this operation to install certificates on NetScaler Instance(s).
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete certificates on NetScaler Instance(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_ssl_certkey_obj=ns_ssl_certkey()
					return cls.delete_bulk_request(client,resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get certificates on NetScaler Instance(s).
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_ssl_certkey_obj=ns_ssl_certkey()
				response = ns_ssl_certkey_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify certificates on NetScaler Instance(s).
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_ssl_certkey_obj=ns_ssl_certkey()
				return cls.update_bulk_request(client,resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download certificates.
	'''

	'''
	Use this operation to download certificates.
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
	Use this operation to generate CSR for the certificate.
	'''

	'''
	Use this operation to generate CSR for the certificate.
	'''
	@classmethod
	def gen_csr(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"gen_csr")
			else : 
				ns_ssl_certkey_obj= ns_ssl_certkey()
				return cls.perform_operation_bulk_request(service,"gen_csr", resource,ns_ssl_certkey_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_certkey_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_certkey resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._count=True
			response = ns_ssl_certkey_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_certkey resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_certkey_obj = ns_ssl_certkey()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_certkey_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_certkey
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_responses, response, "ns_ssl_certkey_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_certkey_response_array
				i=0
				error = [ns_ssl_certkey() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_certkey_response_array
			i=0
			ns_ssl_certkey_objs = [ns_ssl_certkey() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_certkey'):
					for props in obj._ns_ssl_certkey:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_certkey_response,self.__class__.__name__,props)
						ns_ssl_certkey_objs[i] = result.ns_ssl_certkey
						i=i+1
			return ns_ssl_certkey_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_certkey,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_certkey_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_certkey= [ ns_ssl_certkey() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_certkey_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_certkey_response_array = [ ns_ssl_certkey() for _ in range(length)]
