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
Configuration for ns_sla conf file on NetScaler resource
'''

class ns_sla_appflow_action(base_resource):
	_appflowaction_name= ""
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
			return "ns_sla_appflow_action"
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
			return "ns_sla_appflow_actions"
		except Exception as e :
			raise e


	'''
	appflowaction names
	'''
	@property
	def appflowaction_name(self):
		try:
			return self._appflowaction_name
		except Exception as e :
			raise e
	'''
	appflowaction names
	'''
	@appflowaction_name.setter
	def appflowaction_name(self,appflowaction_name):
		try :
			if not isinstance(appflowaction_name,str):
				raise TypeError("appflowaction_name must be set to str value")
			self._appflowaction_name = appflowaction_name
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
	get SLA NS Responder Policy Config.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_sla_appflow_action_obj=ns_sla_appflow_action()
				response = ns_sla_appflow_action_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_sla_appflow_action resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_sla_appflow_action_obj = ns_sla_appflow_action()
			option_ = options()
			option_._filter=filter_
			return ns_sla_appflow_action_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_sla_appflow_action resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_sla_appflow_action_obj = ns_sla_appflow_action()
			option_ = options()
			option_._count=True
			response = ns_sla_appflow_action_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_sla_appflow_action resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_sla_appflow_action_obj = ns_sla_appflow_action()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_sla_appflow_action_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_sla_appflow_action_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sla_appflow_action
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sla_appflow_action_responses, response, "ns_sla_appflow_action_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sla_appflow_action_response_array
				i=0
				error = [ns_sla_appflow_action() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sla_appflow_action_response_array
			i=0
			ns_sla_appflow_action_objs = [ns_sla_appflow_action() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sla_appflow_action'):
					for props in obj._ns_sla_appflow_action:
						result = service.payload_formatter.string_to_bulk_resource(ns_sla_appflow_action_response,self.__class__.__name__,props)
						ns_sla_appflow_action_objs[i] = result.ns_sla_appflow_action
						i=i+1
			return ns_sla_appflow_action_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sla_appflow_action,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sla_appflow_action_response(base_response):
	def __init__(self,length=1) :
		self.ns_sla_appflow_action= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sla_appflow_action= [ ns_sla_appflow_action() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sla_appflow_action_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sla_appflow_action_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sla_appflow_action_response_array = [ ns_sla_appflow_action() for _ in range(length)]
