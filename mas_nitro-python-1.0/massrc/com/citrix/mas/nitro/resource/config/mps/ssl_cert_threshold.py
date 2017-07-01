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

from massrc.com.citrix.mas.nitro.resource.config.mps.threshold import threshold

'''
Configuration for SSL certificate Threshold configuration resource
'''

class ssl_cert_threshold(threshold):
	_days_to_expiry= ""
	_approved_key_strength_list=[]
	_approved_signature_algo_list=[]
	_approved_issuers_list=[]
	_approved_ssl_protocol_list=[]
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
			return "ssl_cert_threshold"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ssl_cert_threshold,self).get_object_id()
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
			return "ssl_cert_thresholds"
		except Exception as e :
			raise e



	'''
	get Days remaining for expiry
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e
	'''
	set Days remaining for expiry
	'''
	@days_to_expiry.setter
	def days_to_expiry(self,days_to_expiry):
		try :
			if not isinstance(days_to_expiry,int):
				raise TypeError("days_to_expiry must be set to int value")
			self._days_to_expiry = days_to_expiry
		except Exception as e :
			raise e

	'''
	Key Strength List
	'''
	@property
	def approved_key_strength_list(self) :
		try:
			return self._approved_key_strength_list
		except Exception as e :
			raise e
	'''
	Key Strength List
	'''
	@approved_key_strength_list.setter
	def approved_key_strength_list(self,approved_key_strength_list) :
		try :
			if not isinstance(approved_key_strength_list,list):
				raise TypeError("approved_key_strength_list must be set to array of str value")
			for item in approved_key_strength_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._approved_key_strength_list = approved_key_strength_list
		except Exception as e :
			raise e

	'''
	Signature Algorithm List
	'''
	@property
	def approved_signature_algo_list(self) :
		try:
			return self._approved_signature_algo_list
		except Exception as e :
			raise e
	'''
	Signature Algorithm List
	'''
	@approved_signature_algo_list.setter
	def approved_signature_algo_list(self,approved_signature_algo_list) :
		try :
			if not isinstance(approved_signature_algo_list,list):
				raise TypeError("approved_signature_algo_list must be set to array of str value")
			for item in approved_signature_algo_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._approved_signature_algo_list = approved_signature_algo_list
		except Exception as e :
			raise e

	'''
	Issuers List
	'''
	@property
	def approved_issuers_list(self) :
		try:
			return self._approved_issuers_list
		except Exception as e :
			raise e
	'''
	Issuers List
	'''
	@approved_issuers_list.setter
	def approved_issuers_list(self,approved_issuers_list) :
		try :
			if not isinstance(approved_issuers_list,list):
				raise TypeError("approved_issuers_list must be set to array of str value")
			for item in approved_issuers_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._approved_issuers_list = approved_issuers_list
		except Exception as e :
			raise e

	'''
	SSL Protocols List
	'''
	@property
	def approved_ssl_protocol_list(self) :
		try:
			return self._approved_ssl_protocol_list
		except Exception as e :
			raise e
	'''
	SSL Protocols List
	'''
	@approved_ssl_protocol_list.setter
	def approved_ssl_protocol_list(self,approved_ssl_protocol_list) :
		try :
			if not isinstance(approved_ssl_protocol_list,list):
				raise TypeError("approved_ssl_protocol_list must be set to array of str value")
			for item in approved_ssl_protocol_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._approved_ssl_protocol_list = approved_ssl_protocol_list
		except Exception as e :
			raise e

	'''
	Use this operation to get ssl certificate policy.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ssl_cert_threshold_obj=ssl_cert_threshold()
				response = ssl_cert_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify ssl certificate policy.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ssl_cert_threshold_obj=ssl_cert_threshold()
				return cls.update_bulk_request(client,resource,ssl_cert_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ssl_cert_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ssl_cert_threshold_obj = ssl_cert_threshold()
			option_ = options()
			option_._filter=filter_
			return ssl_cert_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ssl_cert_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ssl_cert_threshold_obj = ssl_cert_threshold()
			option_ = options()
			option_._count=True
			response = ssl_cert_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ssl_cert_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ssl_cert_threshold_obj = ssl_cert_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ssl_cert_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ssl_cert_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssl_cert_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ssl_cert_threshold_responses, response, "ssl_cert_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ssl_cert_threshold_response_array
				i=0
				error = [ssl_cert_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ssl_cert_threshold_response_array
			i=0
			ssl_cert_threshold_objs = [ssl_cert_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ssl_cert_threshold'):
					for props in obj._ssl_cert_threshold:
						result = service.payload_formatter.string_to_bulk_resource(ssl_cert_threshold_response,self.__class__.__name__,props)
						ssl_cert_threshold_objs[i] = result.ssl_cert_threshold
						i=i+1
			return ssl_cert_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ssl_cert_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ssl_cert_threshold_response(base_response):
	def __init__(self,length=1) :
		self.ssl_cert_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ssl_cert_threshold= [ ssl_cert_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ssl_cert_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.ssl_cert_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ssl_cert_threshold_response_array = [ ssl_cert_threshold() for _ in range(length)]
