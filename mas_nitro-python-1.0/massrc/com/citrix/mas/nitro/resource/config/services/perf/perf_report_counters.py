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
Configuration for Perf Report Counters resource
'''

class perf_report_counters(base_resource):
	_report_name= ""
	_counter_name= ""
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
			return "perf_report_counters"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._report_name
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
			return "perf_report_counterss"
		except Exception as e :
			raise e



	'''
	get Name of Report
	'''
	@property
	def report_name(self) :
		try:
			return self._report_name
		except Exception as e :
			raise e
	'''
	set Name of Report
	'''
	@report_name.setter
	def report_name(self,report_name):
		try :
			if not isinstance(report_name,str):
				raise TypeError("report_name must be set to str value")
			self._report_name = report_name
		except Exception as e :
			raise e


	'''
	get Counter name
	'''
	@property
	def counter_name(self) :
		try:
			return self._counter_name
		except Exception as e :
			raise e
	'''
	set Counter name
	'''
	@counter_name.setter
	def counter_name(self,counter_name):
		try :
			if not isinstance(counter_name,str):
				raise TypeError("counter_name must be set to str value")
			self._counter_name = counter_name
		except Exception as e :
			raise e

	'''
	Use this operation to get the perf counter name for the given report name.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_report_counters_obj=perf_report_counters()
				response = perf_report_counters_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_report_counters resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_report_counters_obj = perf_report_counters()
			option_ = options()
			option_._filter=filter_
			return perf_report_counters_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_report_counters resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_report_counters_obj = perf_report_counters()
			option_ = options()
			option_._count=True
			response = perf_report_counters_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_report_counters resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_report_counters_obj = perf_report_counters()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_report_counters_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_report_counters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_report_counters
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_report_counters_responses, response, "perf_report_counters_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_report_counters_response_array
				i=0
				error = [perf_report_counters() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_report_counters_response_array
			i=0
			perf_report_counters_objs = [perf_report_counters() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_report_counters'):
					for props in obj._perf_report_counters:
						result = service.payload_formatter.string_to_bulk_resource(perf_report_counters_response,self.__class__.__name__,props)
						perf_report_counters_objs[i] = result.perf_report_counters
						i=i+1
			return perf_report_counters_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_report_counters,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_report_counters_response(base_response):
	def __init__(self,length=1) :
		self.perf_report_counters= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_report_counters= [ perf_report_counters() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_report_counters_responses(base_response):
	def __init__(self,length=1) :
		self.perf_report_counters_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_report_counters_response_array = [ perf_report_counters() for _ in range(length)]
