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
Configuration for Appflow Policies resource
'''

class ns_appflow_policies_diagnostic(base_resource):
	_hits= ""
	_name= ""
	_rule= ""
	_traffic_flow= ""
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
			return "ns_appflow_policies_diagnostic"
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
			return "ns_appflow_policies_diagnostics"
		except Exception as e :
			raise e



	'''
	get  Hits more than 0 signifies traffic is flowing
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	set  Hits more than 0 signifies traffic is flowing
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,long):
				raise TypeError("hits must be set to long value")
			self._hits = hits
		except Exception as e :
			raise e


	'''
	get Policy name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Policy name
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
	get Policy Rule
	'''
	@property
	def rule(self) :
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	set Policy Rule
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
	get true if hit increases
	'''
	@property
	def traffic_flow(self) :
		try:
			return self._traffic_flow
		except Exception as e :
			raise e
	'''
	set true if hit increases
	'''
	@traffic_flow.setter
	def traffic_flow(self,traffic_flow):
		try :
			if not isinstance(traffic_flow,bool):
				raise TypeError("traffic_flow must be set to bool value")
			self._traffic_flow = traffic_flow
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
				ns_appflow_policies_diagnostic_obj=ns_appflow_policies_diagnostic()
				response = ns_appflow_policies_diagnostic_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_appflow_policies_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_appflow_policies_diagnostic_obj = ns_appflow_policies_diagnostic()
			option_ = options()
			option_._filter=filter_
			return ns_appflow_policies_diagnostic_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_appflow_policies_diagnostic resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_appflow_policies_diagnostic_obj = ns_appflow_policies_diagnostic()
			option_ = options()
			option_._count=True
			response = ns_appflow_policies_diagnostic_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_appflow_policies_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_appflow_policies_diagnostic_obj = ns_appflow_policies_diagnostic()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_appflow_policies_diagnostic_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_appflow_policies_diagnostic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_appflow_policies_diagnostic
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_appflow_policies_diagnostic_responses, response, "ns_appflow_policies_diagnostic_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_appflow_policies_diagnostic_response_array
				i=0
				error = [ns_appflow_policies_diagnostic() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_appflow_policies_diagnostic_response_array
			i=0
			ns_appflow_policies_diagnostic_objs = [ns_appflow_policies_diagnostic() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_appflow_policies_diagnostic'):
					for props in obj._ns_appflow_policies_diagnostic:
						result = service.payload_formatter.string_to_bulk_resource(ns_appflow_policies_diagnostic_response,self.__class__.__name__,props)
						ns_appflow_policies_diagnostic_objs[i] = result.ns_appflow_policies_diagnostic
						i=i+1
			return ns_appflow_policies_diagnostic_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_appflow_policies_diagnostic,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_appflow_policies_diagnostic_response(base_response):
	def __init__(self,length=1) :
		self.ns_appflow_policies_diagnostic= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_appflow_policies_diagnostic= [ ns_appflow_policies_diagnostic() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_appflow_policies_diagnostic_responses(base_response):
	def __init__(self,length=1) :
		self.ns_appflow_policies_diagnostic_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_appflow_policies_diagnostic_response_array = [ ns_appflow_policies_diagnostic() for _ in range(length)]
