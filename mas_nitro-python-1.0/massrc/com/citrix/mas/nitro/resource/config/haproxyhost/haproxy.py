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

from massrc.com.citrix.mas.nitro.resource.config.mps.vm_device import vm_device

'''
Configuration for HAProxy Instance resource
'''

class haproxy(vm_device):
	_stat_password= ""
	_stat_username= ""
	_stat_port= ""
	_stat_uri= ""
	_configuration_path= ""
	_config= ""
	_no_of_frontend= ""
	_no_of_backend= ""
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
			return "haproxy"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(haproxy,self).get_object_id()
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
			return "haproxys"
		except Exception as e :
			raise e



	'''
	get Password to access haproxy stat.
	'''
	@property
	def stat_password(self) :
		try:
			return self._stat_password
		except Exception as e :
			raise e
	'''
	set Password to access haproxy stat.
	'''
	@stat_password.setter
	def stat_password(self,stat_password):
		try :
			if not isinstance(stat_password,str):
				raise TypeError("stat_password must be set to str value")
			self._stat_password = stat_password
		except Exception as e :
			raise e


	'''
	get Username for accessing haproxy stat.
	'''
	@property
	def stat_username(self) :
		try:
			return self._stat_username
		except Exception as e :
			raise e
	'''
	set Username for accessing haproxy stat.
	'''
	@stat_username.setter
	def stat_username(self,stat_username):
		try :
			if not isinstance(stat_username,str):
				raise TypeError("stat_username must be set to str value")
			self._stat_username = stat_username
		except Exception as e :
			raise e


	'''
	get Port at wich haproxy stat is configured.
	'''
	@property
	def stat_port(self) :
		try:
			return self._stat_port
		except Exception as e :
			raise e
	'''
	set Port at wich haproxy stat is configured.
	'''
	@stat_port.setter
	def stat_port(self,stat_port):
		try :
			if not isinstance(stat_port,str):
				raise TypeError("stat_port must be set to str value")
			self._stat_port = stat_port
		except Exception as e :
			raise e


	'''
	get URL at which haproxy stat is configured.
	'''
	@property
	def stat_uri(self) :
		try:
			return self._stat_uri
		except Exception as e :
			raise e
	'''
	set URL at which haproxy stat is configured.
	'''
	@stat_uri.setter
	def stat_uri(self,stat_uri):
		try :
			if not isinstance(stat_uri,str):
				raise TypeError("stat_uri must be set to str value")
			self._stat_uri = stat_uri
		except Exception as e :
			raise e


	'''
	get Config Path of HA Proxy Instance.
	'''
	@property
	def configuration_path(self) :
		try:
			return self._configuration_path
		except Exception as e :
			raise e

	'''
	Config Paths of HA Proxies on this HAPRoxy Host.
	'''
	@property
	def config(self):
		try:
			return self._config
		except Exception as e :
			raise e

	'''
	No of frontend in haproxy instance
	'''
	@property
	def no_of_frontend(self):
		try:
			return self._no_of_frontend
		except Exception as e :
			raise e
	'''
	No of frontend in haproxy instance
	'''
	@no_of_frontend.setter
	def no_of_frontend(self,no_of_frontend):
		try :
			if not isinstance(no_of_frontend,int):
				raise TypeError("no_of_frontend must be set to int value")
			self._no_of_frontend = no_of_frontend
		except Exception as e :
			raise e

	'''
	No of backend in haproxy instance
	'''
	@property
	def no_of_backend(self):
		try:
			return self._no_of_backend
		except Exception as e :
			raise e
	'''
	No of backend in haproxy instance
	'''
	@no_of_backend.setter
	def no_of_backend(self,no_of_backend):
		try :
			if not isinstance(no_of_backend,int):
				raise TypeError("no_of_backend must be set to int value")
			self._no_of_backend = no_of_backend
		except Exception as e :
			raise e

	'''
	Use this operation to add a HAProxy.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				haproxy_obj= haproxy()
				return cls.perform_operation_bulk_request(service,"add", resource,haproxy_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get HAProxy.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				haproxy_obj=haproxy()
				response = haproxy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of haproxy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			haproxy_obj = haproxy()
			option_ = options()
			option_._filter=filter_
			return haproxy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the haproxy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			haproxy_obj = haproxy()
			option_ = options()
			option_._count=True
			response = haproxy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of haproxy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			haproxy_obj = haproxy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = haproxy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(haproxy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.haproxy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxy_responses, response, "haproxy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.haproxy_response_array
				i=0
				error = [haproxy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.haproxy_response_array
			i=0
			haproxy_objs = [haproxy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_haproxy'):
					for props in obj._haproxy:
						result = service.payload_formatter.string_to_bulk_resource(haproxy_response,self.__class__.__name__,props)
						haproxy_objs[i] = result.haproxy
						i=i+1
			return haproxy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(haproxy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class haproxy_response(base_response):
	def __init__(self,length=1) :
		self.haproxy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.haproxy= [ haproxy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class haproxy_responses(base_response):
	def __init__(self,length=1) :
		self.haproxy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.haproxy_response_array = [ haproxy() for _ in range(length)]
