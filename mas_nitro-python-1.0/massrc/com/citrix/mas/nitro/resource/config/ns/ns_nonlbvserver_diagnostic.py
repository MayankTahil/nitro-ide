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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_appflow_policies_diagnostic import ns_appflow_policies_diagnostic


'''
Configuration for NON LBVServer Diagnostic resource
'''

class ns_nonlbvserver_diagnostic(base_resource):
	_appflowlog= ""
	_name= ""
	_appflow_policies=[]
	_state= ""
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
			return "ns_nonlbvserver_diagnostic"
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
			return "ns_nonlbvserver_diagnostics"
		except Exception as e :
			raise e



	'''
	get AppFlow is enabled at Vserver
	'''
	@property
	def appflowlog(self) :
		try:
			return self._appflowlog
		except Exception as e :
			raise e
	'''
	set AppFlow is enabled at Vserver
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
	get Virtual server name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Virtual server name
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
	get Appflow policies bind to the vserver
	'''
	@property
	def appflow_policies(self) :
		try:
			return self._appflow_policies
		except Exception as e :
			raise e
	'''
	set Appflow policies bind to the vserver
	'''
	@appflow_policies.setter
	def appflow_policies(self,appflow_policies) :
		try :
			if not isinstance(appflow_policies,list):
				raise TypeError("appflow_policies must be set to array of ns_appflow_policies_diagnostic value")
			for item in appflow_policies :
				if not isinstance(item,ns_appflow_policies_diagnostic):
					raise TypeError("item must be set to ns_appflow_policies_diagnostic value")
			self._appflow_policies = appflow_policies
		except Exception as e :
			raise e


	'''
	get Tells whether virtual server up/down
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Tells whether virtual server up/down
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
	Use this method to diagnose NetScaler.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_nonlbvserver_diagnostic_obj=ns_nonlbvserver_diagnostic()
				response = ns_nonlbvserver_diagnostic_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_nonlbvserver_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_nonlbvserver_diagnostic_obj = ns_nonlbvserver_diagnostic()
			option_ = options()
			option_._filter=filter_
			return ns_nonlbvserver_diagnostic_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_nonlbvserver_diagnostic resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_nonlbvserver_diagnostic_obj = ns_nonlbvserver_diagnostic()
			option_ = options()
			option_._count=True
			response = ns_nonlbvserver_diagnostic_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_nonlbvserver_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_nonlbvserver_diagnostic_obj = ns_nonlbvserver_diagnostic()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_nonlbvserver_diagnostic_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_nonlbvserver_diagnostic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_nonlbvserver_diagnostic
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_nonlbvserver_diagnostic_responses, response, "ns_nonlbvserver_diagnostic_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_nonlbvserver_diagnostic_response_array
				i=0
				error = [ns_nonlbvserver_diagnostic() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_nonlbvserver_diagnostic_response_array
			i=0
			ns_nonlbvserver_diagnostic_objs = [ns_nonlbvserver_diagnostic() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_nonlbvserver_diagnostic'):
					for props in obj._ns_nonlbvserver_diagnostic:
						result = service.payload_formatter.string_to_bulk_resource(ns_nonlbvserver_diagnostic_response,self.__class__.__name__,props)
						ns_nonlbvserver_diagnostic_objs[i] = result.ns_nonlbvserver_diagnostic
						i=i+1
			return ns_nonlbvserver_diagnostic_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_nonlbvserver_diagnostic,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_nonlbvserver_diagnostic_response(base_response):
	def __init__(self,length=1) :
		self.ns_nonlbvserver_diagnostic= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_nonlbvserver_diagnostic= [ ns_nonlbvserver_diagnostic() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_nonlbvserver_diagnostic_responses(base_response):
	def __init__(self,length=1) :
		self.ns_nonlbvserver_diagnostic_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_nonlbvserver_diagnostic_response_array = [ ns_nonlbvserver_diagnostic() for _ in range(length)]
