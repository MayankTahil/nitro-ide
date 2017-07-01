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
Configuration for SLA Virtual server config on NetScaler resource
'''

class ns_sla_config(base_resource):
	_appflowlog= ""
	_acceptancethreshold= ""
	_is_active_policy= ""
	_rule= ""
	_appflowaction= ""
	_is_response_time_set= ""
	_policy_action= ""
	_ns_ip_address= ""
	_hits= ""
	_maxtransactionthreshold= ""
	_DOI= ""
	_vserver_ip_address= ""
	_bind_priority= ""
	_bind_type= ""
	_mintransactionthreshold= ""
	_time_window_interval= ""
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
			return "ns_sla_config"
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
			return "ns_sla_configs"
		except Exception as e :
			raise e


	'''
	Appflow log
	'''
	@property
	def appflowlog(self):
		try:
			return self._appflowlog
		except Exception as e :
			raise e
	'''
	Appflow log
	'''
	@appflowlog.setter
	def appflowlog(self,appflowlog):
		try :
			if not isinstance(appflowlog,str):
				raise TypeError("appflowlog must be set to str value")
			self._appflowlog = appflowlog
		except Exception as e :
			raise e

	'''
	Tells whether bind type virtual server type
	'''
	@property
	def acceptancethreshold(self):
		try:
			return self._acceptancethreshold
		except Exception as e :
			raise e
	'''
	Tells whether bind type virtual server type
	'''
	@acceptancethreshold.setter
	def acceptancethreshold(self,acceptancethreshold):
		try :
			if not isinstance(acceptancethreshold,str):
				raise TypeError("acceptancethreshold must be set to str value")
			self._acceptancethreshold = acceptancethreshold
		except Exception as e :
			raise e

	'''
	 Policy is Active or Not
	'''
	@property
	def is_active_policy(self):
		try:
			return self._is_active_policy
		except Exception as e :
			raise e
	'''
	 Policy is Active or Not
	'''
	@is_active_policy.setter
	def is_active_policy(self,is_active_policy):
		try :
			if not isinstance(is_active_policy,int):
				raise TypeError("is_active_policy must be set to int value")
			self._is_active_policy = is_active_policy
		except Exception as e :
			raise e

	'''
	Responder policy rule
	'''
	@property
	def rule(self):
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	Responder policy rule
	'''
	@rule.setter
	def rule(self,rule):
		try :
			if not isinstance(rule,str):
				raise TypeError("rule must be set to str value")
			self._rule = rule
		except Exception as e :
			raise e

	'''
	appflowaction
	'''
	@property
	def appflowaction(self):
		try:
			return self._appflowaction
		except Exception as e :
			raise e
	'''
	appflowaction
	'''
	@appflowaction.setter
	def appflowaction(self,appflowaction):
		try :
			if not isinstance(appflowaction,str):
				raise TypeError("appflowaction must be set to str value")
			self._appflowaction = appflowaction
		except Exception as e :
			raise e

	'''
	 is_response_time_set
	'''
	@property
	def is_response_time_set(self):
		try:
			return self._is_response_time_set
		except Exception as e :
			raise e
	'''
	 is_response_time_set
	'''
	@is_response_time_set.setter
	def is_response_time_set(self,is_response_time_set):
		try :
			if not isinstance(is_response_time_set,int):
				raise TypeError("is_response_time_set must be set to int value")
			self._is_response_time_set = is_response_time_set
		except Exception as e :
			raise e

	'''
	policy_action NOOP
	'''
	@property
	def policy_action(self):
		try:
			return self._policy_action
		except Exception as e :
			raise e
	'''
	policy_action NOOP
	'''
	@policy_action.setter
	def policy_action(self,policy_action):
		try :
			if not isinstance(policy_action,str):
				raise TypeError("policy_action must be set to str value")
			self._policy_action = policy_action
		except Exception as e :
			raise e

	'''
	NS IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NS IP Address
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
	Hits of Responder Policy
	'''
	@property
	def hits(self):
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	Hits of Responder Policy
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,str):
				raise TypeError("hits must be set to str value")
			self._hits = hits
		except Exception as e :
			raise e

	'''
	rt_max_threshold 
	'''
	@property
	def maxtransactionthreshold(self):
		try:
			return self._maxtransactionthreshold
		except Exception as e :
			raise e
	'''
	rt_max_threshold 
	'''
	@maxtransactionthreshold.setter
	def maxtransactionthreshold(self,maxtransactionthreshold):
		try :
			if not isinstance(maxtransactionthreshold,str):
				raise TypeError("maxtransactionthreshold must be set to str value")
			self._maxtransactionthreshold = maxtransactionthreshold
		except Exception as e :
			raise e

	'''
	DOI name
	'''
	@property
	def DOI(self):
		try:
			return self._DOI
		except Exception as e :
			raise e
	'''
	DOI name
	'''
	@DOI.setter
	def DOI(self,DOI):
		try :
			if not isinstance(DOI,str):
				raise TypeError("DOI must be set to str value")
			self._DOI = DOI
		except Exception as e :
			raise e

	'''
	NetScaler IP Address
	'''
	@property
	def vserver_ip_address(self):
		try:
			return self._vserver_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
	'''
	@vserver_ip_address.setter
	def vserver_ip_address(self,vserver_ip_address):
		try :
			if not isinstance(vserver_ip_address,str):
				raise TypeError("vserver_ip_address must be set to str value")
			self._vserver_ip_address = vserver_ip_address
		except Exception as e :
			raise e

	'''
	bind_priority 1 to 2147483647
	'''
	@property
	def bind_priority(self):
		try:
			return self._bind_priority
		except Exception as e :
			raise e
	'''
	bind_priority 1 to 2147483647
	'''
	@bind_priority.setter
	def bind_priority(self,bind_priority):
		try :
			if not isinstance(bind_priority,str):
				raise TypeError("bind_priority must be set to str value")
			self._bind_priority = bind_priority
		except Exception as e :
			raise e

	'''
	Tells whether bind type virtual server type
	'''
	@property
	def bind_type(self):
		try:
			return self._bind_type
		except Exception as e :
			raise e
	'''
	Tells whether bind type virtual server type
	'''
	@bind_type.setter
	def bind_type(self,bind_type):
		try :
			if not isinstance(bind_type,str):
				raise TypeError("bind_type must be set to str value")
			self._bind_type = bind_type
		except Exception as e :
			raise e

	'''
	rt_min_threshold 
	'''
	@property
	def mintransactionthreshold(self):
		try:
			return self._mintransactionthreshold
		except Exception as e :
			raise e
	'''
	rt_min_threshold 
	'''
	@mintransactionthreshold.setter
	def mintransactionthreshold(self,mintransactionthreshold):
		try :
			if not isinstance(mintransactionthreshold,str):
				raise TypeError("mintransactionthreshold must be set to str value")
			self._mintransactionthreshold = mintransactionthreshold
		except Exception as e :
			raise e

	'''
	time_window_interval 1 min to 1440 mins 
	'''
	@property
	def time_window_interval(self):
		try:
			return self._time_window_interval
		except Exception as e :
			raise e
	'''
	time_window_interval 1 min to 1440 mins 
	'''
	@time_window_interval.setter
	def time_window_interval(self,time_window_interval):
		try :
			if not isinstance(time_window_interval,str):
				raise TypeError("time_window_interval must be set to str value")
			self._time_window_interval = time_window_interval
		except Exception as e :
			raise e

	'''
	Add SLA NS Responder Policy Config.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_sla_config_obj= ns_sla_config()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_sla_config_obj)
		except Exception as e :
			raise e

	'''
	delete SLA NS Responder Policy Config.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_sla_config_obj=ns_sla_config()
					return cls.delete_bulk_request(client,resource,ns_sla_config_obj)
		except Exception as e :
			raise e

	'''
	get SLA NS Responder Policy Config.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_sla_config_obj=ns_sla_config()
				response = ns_sla_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify SLA NS Responder Policy Config.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_sla_config_obj=ns_sla_config()
				return cls.update_bulk_request(client,resource,ns_sla_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_sla_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_sla_config_obj = ns_sla_config()
			option_ = options()
			option_._filter=filter_
			return ns_sla_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_sla_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_sla_config_obj = ns_sla_config()
			option_ = options()
			option_._count=True
			response = ns_sla_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_sla_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_sla_config_obj = ns_sla_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_sla_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_sla_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sla_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sla_config_responses, response, "ns_sla_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sla_config_response_array
				i=0
				error = [ns_sla_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sla_config_response_array
			i=0
			ns_sla_config_objs = [ns_sla_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sla_config'):
					for props in obj._ns_sla_config:
						result = service.payload_formatter.string_to_bulk_resource(ns_sla_config_response,self.__class__.__name__,props)
						ns_sla_config_objs[i] = result.ns_sla_config
						i=i+1
			return ns_sla_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sla_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sla_config_response(base_response):
	def __init__(self,length=1) :
		self.ns_sla_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sla_config= [ ns_sla_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sla_config_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sla_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sla_config_response_array = [ ns_sla_config() for _ in range(length)]
