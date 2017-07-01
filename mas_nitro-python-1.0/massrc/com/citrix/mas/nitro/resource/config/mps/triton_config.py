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
from massrc.com.citrix.mas.nitro.resource.config.mps.marathon_param import marathon_param
from massrc.com.citrix.mas.nitro.resource.config.mps.dns_param import dns_param
from massrc.com.citrix.mas.nitro.resource.config.mps.kubernetes_param import kubernetes_param
from massrc.com.citrix.mas.nitro.resource.config.mps.networking_param import networking_param


'''
Configuration for Configuration details for Triton module resource
'''

class triton_config(base_resource):
	_active_framework= ""
	_marathon_params= ""
	_netmode= ""
	_dns_params= ""
	_framework_healthcheck= ""
	_kube_params= ""
	_loopback_disabled= ""
	_id= ""
	_networking_params= ""
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
			return "triton_config"
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
			return "triton_configs"
		except Exception as e :
			raise e



	'''
	get Currently active container orchestration framework (Kubernetes or Marathon)
	'''
	@property
	def active_framework(self) :
		try:
			return self._active_framework
		except Exception as e :
			raise e
	'''
	set Currently active container orchestration framework (Kubernetes or Marathon)
	'''
	@active_framework.setter
	def active_framework(self,active_framework):
		try :
			if not isinstance(active_framework,str):
				raise TypeError("active_framework must be set to str value")
			self._active_framework = active_framework
		except Exception as e :
			raise e


	'''
	get Marathon parameters
	'''
	@property
	def marathon_params(self) :
		try:
			return self._marathon_params
		except Exception as e :
			raise e
	'''
	set Marathon parameters
	'''
	@marathon_params.setter
	def marathon_params(self,marathon_params):
		try :
			if not isinstance(marathon_params,marathon_param):
				raise TypeError("marathon_params must be set to marathon_param value")
			self._marathon_params = marathon_params
		except Exception as e :
			raise e


	'''
	get Network mode of the operation: IP per container or CPX per host
	'''
	@property
	def netmode(self) :
		try:
			return self._netmode
		except Exception as e :
			raise e
	'''
	set Network mode of the operation: IP per container or CPX per host
	'''
	@netmode.setter
	def netmode(self,netmode):
		try :
			if not isinstance(netmode,str):
				raise TypeError("netmode must be set to str value")
			self._netmode = netmode
		except Exception as e :
			raise e


	'''
	get DNS Parameters
	'''
	@property
	def dns_params(self) :
		try:
			return self._dns_params
		except Exception as e :
			raise e
	'''
	set DNS Parameters
	'''
	@dns_params.setter
	def dns_params(self,dns_params):
		try :
			if not isinstance(dns_params,dns_param):
				raise TypeError("dns_params must be set to dns_param value")
			self._dns_params = dns_params
		except Exception as e :
			raise e


	'''
	get This indicates default monitor is enabled on this app or not
	'''
	@property
	def framework_healthcheck(self) :
		try:
			return self._framework_healthcheck
		except Exception as e :
			raise e
	'''
	set This indicates default monitor is enabled on this app or not
	'''
	@framework_healthcheck.setter
	def framework_healthcheck(self,framework_healthcheck):
		try :
			if not isinstance(framework_healthcheck,bool):
				raise TypeError("framework_healthcheck must be set to bool value")
			self._framework_healthcheck = framework_healthcheck
		except Exception as e :
			raise e


	'''
	get Kubernetes parameters
	'''
	@property
	def kube_params(self) :
		try:
			return self._kube_params
		except Exception as e :
			raise e
	'''
	set Kubernetes parameters
	'''
	@kube_params.setter
	def kube_params(self,kube_params):
		try :
			if not isinstance(kube_params,kubernetes_param):
				raise TypeError("kube_params must be set to kubernetes_param value")
			self._kube_params = kube_params
		except Exception as e :
			raise e


	'''
	get This indicates default monitor is enabled on this app or not
	'''
	@property
	def loopback_disabled(self) :
		try:
			return self._loopback_disabled
		except Exception as e :
			raise e
	'''
	set This indicates default monitor is enabled on this app or not
	'''
	@loopback_disabled.setter
	def loopback_disabled(self,loopback_disabled):
		try :
			if not isinstance(loopback_disabled,bool):
				raise TypeError("loopback_disabled must be set to bool value")
			self._loopback_disabled = loopback_disabled
		except Exception as e :
			raise e


	'''
	get Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id
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
	get Networking parameters
	'''
	@property
	def networking_params(self) :
		try:
			return self._networking_params
		except Exception as e :
			raise e
	'''
	set Networking parameters
	'''
	@networking_params.setter
	def networking_params(self,networking_params):
		try :
			if not isinstance(networking_params,networking_param):
				raise TypeError("networking_params must be set to networking_param value")
			self._networking_params = networking_params
		except Exception as e :
			raise e

	'''
	Use this operation to add an managed application.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				triton_config_obj= triton_config()
				return cls.perform_operation_bulk_request(service,"add", resource,triton_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get an managed application.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				triton_config_obj=triton_config()
				response = triton_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update managed application.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				triton_config_obj=triton_config()
				return cls.update_bulk_request(client,resource,triton_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of triton_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			triton_config_obj = triton_config()
			option_ = options()
			option_._filter=filter_
			return triton_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the triton_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			triton_config_obj = triton_config()
			option_ = options()
			option_._count=True
			response = triton_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of triton_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			triton_config_obj = triton_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = triton_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(triton_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.triton_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(triton_config_responses, response, "triton_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.triton_config_response_array
				i=0
				error = [triton_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.triton_config_response_array
			i=0
			triton_config_objs = [triton_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_triton_config'):
					for props in obj._triton_config:
						result = service.payload_formatter.string_to_bulk_resource(triton_config_response,self.__class__.__name__,props)
						triton_config_objs[i] = result.triton_config
						i=i+1
			return triton_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(triton_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class triton_config_response(base_response):
	def __init__(self,length=1) :
		self.triton_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.triton_config= [ triton_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class triton_config_responses(base_response):
	def __init__(self,length=1) :
		self.triton_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.triton_config_response_array = [ triton_config() for _ in range(length)]
