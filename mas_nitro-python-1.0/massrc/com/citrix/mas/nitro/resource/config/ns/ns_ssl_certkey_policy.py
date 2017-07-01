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
Configuration for NetScaler SSL Cert-Key Polling Policy resource
'''

class ns_ssl_certkey_policy(base_resource):
	_interval_unit= ""
	_polling_interval= ""
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
			return "ns_ssl_certkey_policy"
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
			return "ns_ssl_certkey_policys"
		except Exception as e :
			raise e



	'''
	This property is deprecated, polling interval will be provided in minutes only
	get Frequency unit (Minutes)
	'''
	@property
	def interval_unit(self) :
		try:
			return self._interval_unit
		except Exception as e :
			raise e
	'''
	This property is deprecated, polling interval will be provided in minutes only
	set Frequency unit (Minutes)
	'''
	@interval_unit.setter
	def interval_unit(self,interval_unit):
		try :
			if not isinstance(interval_unit,str):
				raise TypeError("interval_unit must be set to str value")
			self._interval_unit = interval_unit
		except Exception as e :
			raise e


	'''
	get Frequency of polling in minutes
	'''
	@property
	def polling_interval(self) :
		try:
			return self._polling_interval
		except Exception as e :
			raise e
	'''
	set Frequency of polling in minutes
	'''
	@polling_interval.setter
	def polling_interval(self,polling_interval):
		try :
			if not isinstance(polling_interval,int):
				raise TypeError("polling_interval must be set to int value")
			self._polling_interval = polling_interval
		except Exception as e :
			raise e

	'''
	Use this operation to poll all SSL certificates from all NetScalers and update the database.
	'''
	@classmethod
	def do_poll(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"do_poll")
		except Exception as e :
			raise e

	'''
	Use this operation to get the polling frequency of the NetScaler SSL certificates.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_ssl_certkey_policy_obj=ns_ssl_certkey_policy()
				response = ns_ssl_certkey_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to set the polling frequency of the NetScaler SSL certificates.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ssl_certkey_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ssl_certkey_policy_obj = ns_ssl_certkey_policy()
			option_ = options()
			option_._filter=filter_
			return ns_ssl_certkey_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ssl_certkey_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ssl_certkey_policy_obj = ns_ssl_certkey_policy()
			option_ = options()
			option_._count=True
			response = ns_ssl_certkey_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ssl_certkey_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ssl_certkey_policy_obj = ns_ssl_certkey_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ssl_certkey_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ssl_certkey_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ssl_certkey_policy_responses, response, "ns_ssl_certkey_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ssl_certkey_policy_response_array
				i=0
				error = [ns_ssl_certkey_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ssl_certkey_policy_response_array
			i=0
			ns_ssl_certkey_policy_objs = [ns_ssl_certkey_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ssl_certkey_policy'):
					for props in obj._ns_ssl_certkey_policy:
						result = service.payload_formatter.string_to_bulk_resource(ns_ssl_certkey_policy_response,self.__class__.__name__,props)
						ns_ssl_certkey_policy_objs[i] = result.ns_ssl_certkey_policy
						i=i+1
			return ns_ssl_certkey_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ssl_certkey_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ssl_certkey_policy_response(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ssl_certkey_policy= [ ns_ssl_certkey_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ssl_certkey_policy_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ssl_certkey_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ssl_certkey_policy_response_array = [ ns_ssl_certkey_policy() for _ in range(length)]
