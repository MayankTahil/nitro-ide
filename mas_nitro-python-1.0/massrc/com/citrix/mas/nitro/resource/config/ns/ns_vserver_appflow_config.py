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
Configuration for Virtual server appflow config on NetScaler resource
'''

class ns_vserver_appflow_config(base_resource):
	_export_option=[]
	_appflow_policy_rule= ""
	_appflowlog= ""
	_es4nslog= ""
	_name= ""
	_export_list=[]
	_state= ""
	_ns_ip_address= ""
	_agent_list=[]
	_ip_address= ""
	_type= ""
	_icalog= ""
	_servicetype= ""
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
			return "ns_vserver_appflow_config"
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
			return "ns_vserver_appflow_configs"
		except Exception as e :
			raise e


	'''
	Export Options: TCP, ICA
	'''
	@property
	def export_option(self) :
		try:
			return self._export_option
		except Exception as e :
			raise e
	'''
	Export Options: TCP, ICA
	'''
	@export_option.setter
	def export_option(self,export_option) :
		try :
			if not isinstance(export_option,list):
				raise TypeError("export_option must be set to array of str value")
			for item in export_option :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._export_option = export_option
		except Exception as e :
			raise e

	'''
	Appflow policy rule
	'''
	@property
	def appflow_policy_rule(self):
		try:
			return self._appflow_policy_rule
		except Exception as e :
			raise e
	'''
	Appflow policy rule
	'''
	@appflow_policy_rule.setter
	def appflow_policy_rule(self,appflow_policy_rule):
		try :
			if not isinstance(appflow_policy_rule,str):
				raise TypeError("appflow_policy_rule must be set to str value")
			self._appflow_policy_rule = appflow_policy_rule
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
	ESNS enable
	'''
	@property
	def es4nslog(self):
		try:
			return self._es4nslog
		except Exception as e :
			raise e
	'''
	ESNS enable
	'''
	@es4nslog.setter
	def es4nslog(self,es4nslog):
		try :
			if not isinstance(es4nslog,str):
				raise TypeError("es4nslog must be set to str value")
			self._es4nslog = es4nslog
		except Exception as e :
			raise e

	'''
	Virtual server name
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Virtual server name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e

	'''
	Export List: WebInsight, SecurityInsight
	'''
	@property
	def export_list(self) :
		try:
			return self._export_list
		except Exception as e :
			raise e
	'''
	Export List: WebInsight, SecurityInsight
	'''
	@export_list.setter
	def export_list(self,export_list) :
		try :
			if not isinstance(export_list,list):
				raise TypeError("export_list must be set to array of str value")
			for item in export_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._export_list = export_list
		except Exception as e :
			raise e

	'''
	Tells whether virtual server up/down
	'''
	@property
	def state(self):
		try:
			return self._state
		except Exception as e :
			raise e

	'''
	NetScaler IP Address
	'''
	@property
	def ns_ip_address(self):
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	NetScaler IP Address
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
	Agent List, on which traffic will flow
	'''
	@property
	def agent_list(self) :
		try:
			return self._agent_list
		except Exception as e :
			raise e
	'''
	Agent List, on which traffic will flow
	'''
	@agent_list.setter
	def agent_list(self,agent_list) :
		try :
			if not isinstance(agent_list,list):
				raise TypeError("agent_list must be set to array of str value")
			for item in agent_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._agent_list = agent_list
		except Exception as e :
			raise e

	'''
	Virtual server IP Address
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	Virtual server IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Tells whether virtual server type
	'''
	@property
	def type(self):
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	Tells whether virtual server type
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
	ICA log
	'''
	@property
	def icalog(self):
		try:
			return self._icalog
		except Exception as e :
			raise e
	'''
	ICA log
	'''
	@icalog.setter
	def icalog(self,icalog):
		try :
			if not isinstance(icalog,str):
				raise TypeError("icalog must be set to str value")
			self._icalog = icalog
		except Exception as e :
			raise e

	'''
	servicetype
	'''
	@property
	def servicetype(self):
		try:
			return self._servicetype
		except Exception as e :
			raise e
	'''
	servicetype
	'''
	@servicetype.setter
	def servicetype(self,servicetype):
		try :
			if not isinstance(servicetype,str):
				raise TypeError("servicetype must be set to str value")
			self._servicetype = servicetype
		except Exception as e :
			raise e

	'''
	Add virtual server policy.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_vserver_appflow_config_obj= ns_vserver_appflow_config()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	delete virtual server policy.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_vserver_appflow_config_obj=ns_vserver_appflow_config()
					return cls.delete_bulk_request(client,resource,ns_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	get virtual server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_vserver_appflow_config_obj=ns_vserver_appflow_config()
				response = ns_vserver_appflow_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify virtual server policy.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_vserver_appflow_config_obj=ns_vserver_appflow_config()
				return cls.update_bulk_request(client,resource,ns_vserver_appflow_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_vserver_appflow_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_vserver_appflow_config_obj = ns_vserver_appflow_config()
			option_ = options()
			option_._filter=filter_
			return ns_vserver_appflow_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_vserver_appflow_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_vserver_appflow_config_obj = ns_vserver_appflow_config()
			option_ = options()
			option_._count=True
			response = ns_vserver_appflow_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_vserver_appflow_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_vserver_appflow_config_obj = ns_vserver_appflow_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_vserver_appflow_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_vserver_appflow_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_vserver_appflow_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_vserver_appflow_config_responses, response, "ns_vserver_appflow_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_vserver_appflow_config_response_array
				i=0
				error = [ns_vserver_appflow_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_vserver_appflow_config_response_array
			i=0
			ns_vserver_appflow_config_objs = [ns_vserver_appflow_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_vserver_appflow_config'):
					for props in obj._ns_vserver_appflow_config:
						result = service.payload_formatter.string_to_bulk_resource(ns_vserver_appflow_config_response,self.__class__.__name__,props)
						ns_vserver_appflow_config_objs[i] = result.ns_vserver_appflow_config
						i=i+1
			return ns_vserver_appflow_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_vserver_appflow_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_vserver_appflow_config_response(base_response):
	def __init__(self,length=1) :
		self.ns_vserver_appflow_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_vserver_appflow_config= [ ns_vserver_appflow_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_vserver_appflow_config_responses(base_response):
	def __init__(self,length=1) :
		self.ns_vserver_appflow_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_vserver_appflow_config_response_array = [ ns_vserver_appflow_config() for _ in range(length)]
