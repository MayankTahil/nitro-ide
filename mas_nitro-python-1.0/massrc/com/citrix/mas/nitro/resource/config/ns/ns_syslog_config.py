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
Configuration for NetScaler Syslog Config resource
'''

class ns_syslog_config(base_resource):
	_destination_ip= ""
	_state= ""
	_ns_ip_address= ""
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
			return "ns_syslog_config"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._ns_ip_address
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
			return "ns_syslog_configs"
		except Exception as e :
			raise e



	'''
	get Syslog Destination IP Address
	'''
	@property
	def destination_ip(self) :
		try:
			return self._destination_ip
		except Exception as e :
			raise e
	'''
	set Syslog Destination IP Address
	'''
	@destination_ip.setter
	def destination_ip(self,destination_ip):
		try :
			if not isinstance(destination_ip,str):
				raise TypeError("destination_ip must be set to str value")
			self._destination_ip = destination_ip
		except Exception as e :
			raise e


	'''
	get Syslog Status
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Syslog Status
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get Netscaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set Netscaler IP Address
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
	Get the syslog server configuration for NS.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_syslog_config_obj=ns_syslog_config()
				response = ns_syslog_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify syslog server configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_syslog_config_obj=ns_syslog_config()
				return cls.update_bulk_request(client,resource,ns_syslog_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_syslog_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_syslog_config_obj = ns_syslog_config()
			option_ = options()
			option_._filter=filter_
			return ns_syslog_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_syslog_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_syslog_config_obj = ns_syslog_config()
			option_ = options()
			option_._count=True
			response = ns_syslog_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_syslog_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_syslog_config_obj = ns_syslog_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_syslog_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_syslog_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_syslog_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_syslog_config_responses, response, "ns_syslog_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_syslog_config_response_array
				i=0
				error = [ns_syslog_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_syslog_config_response_array
			i=0
			ns_syslog_config_objs = [ns_syslog_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_syslog_config'):
					for props in obj._ns_syslog_config:
						result = service.payload_formatter.string_to_bulk_resource(ns_syslog_config_response,self.__class__.__name__,props)
						ns_syslog_config_objs[i] = result.ns_syslog_config
						i=i+1
			return ns_syslog_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_syslog_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_syslog_config_response(base_response):
	def __init__(self,length=1) :
		self.ns_syslog_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_syslog_config= [ ns_syslog_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_syslog_config_responses(base_response):
	def __init__(self,length=1) :
		self.ns_syslog_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_syslog_config_response_array = [ ns_syslog_config() for _ in range(length)]
