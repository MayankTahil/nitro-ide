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
Configuration for Device Counter Table resource
'''

class perf_device_counters(base_resource):
	_device_family= ""
	_counter_group= ""
	_is_tabular= ""
	_min_ver_supported= ""
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
			return "perf_device_counters"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._counter_group
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
			return "perf_device_counterss"
		except Exception as e :
			raise e



	'''
	get Device Family of which the counter belongs to
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family of which the counter belongs to
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Counter Group of which the counter belongs to
	'''
	@property
	def counter_group(self) :
		try:
			return self._counter_group
		except Exception as e :
			raise e
	'''
	set Counter Group of which the counter belongs to
	'''
	@counter_group.setter
	def counter_group(self,counter_group):
		try :
			if not isinstance(counter_group,str):
				raise TypeError("counter_group must be set to str value")
			self._counter_group = counter_group
		except Exception as e :
			raise e


	'''
	get Is Tabular
	'''
	@property
	def is_tabular(self) :
		try:
			return self._is_tabular
		except Exception as e :
			raise e
	'''
	set Is Tabular
	'''
	@is_tabular.setter
	def is_tabular(self,is_tabular):
		try :
			if not isinstance(is_tabular,bool):
				raise TypeError("is_tabular must be set to bool value")
			self._is_tabular = is_tabular
		except Exception as e :
			raise e


	'''
	get Minimum Version supported by the counter Group
	'''
	@property
	def min_ver_supported(self) :
		try:
			return self._min_ver_supported
		except Exception as e :
			raise e
	'''
	set Minimum Version supported by the counter Group
	'''
	@min_ver_supported.setter
	def min_ver_supported(self,min_ver_supported):
		try :
			if not isinstance(min_ver_supported,str):
				raise TypeError("min_ver_supported must be set to str value")
			self._min_ver_supported = min_ver_supported
		except Exception as e :
			raise e


	'''
	get Counter Name
	'''
	@property
	def counter_name(self) :
		try:
			return self._counter_name
		except Exception as e :
			raise e
	'''
	set Counter Name
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
	Get all the counter groups/counters.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_device_counters_obj=perf_device_counters()
				response = perf_device_counters_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_device_counters resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_device_counters_obj = perf_device_counters()
			option_ = options()
			option_._filter=filter_
			return perf_device_counters_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_device_counters resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_device_counters_obj = perf_device_counters()
			option_ = options()
			option_._count=True
			response = perf_device_counters_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_device_counters resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_device_counters_obj = perf_device_counters()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_device_counters_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_device_counters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_device_counters
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_device_counters_responses, response, "perf_device_counters_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_device_counters_response_array
				i=0
				error = [perf_device_counters() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_device_counters_response_array
			i=0
			perf_device_counters_objs = [perf_device_counters() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_device_counters'):
					for props in obj._perf_device_counters:
						result = service.payload_formatter.string_to_bulk_resource(perf_device_counters_response,self.__class__.__name__,props)
						perf_device_counters_objs[i] = result.perf_device_counters
						i=i+1
			return perf_device_counters_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_device_counters,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_device_counters_response(base_response):
	def __init__(self,length=1) :
		self.perf_device_counters= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_device_counters= [ perf_device_counters() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_device_counters_responses(base_response):
	def __init__(self,length=1) :
		self.perf_device_counters_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_device_counters_response_array = [ perf_device_counters() for _ in range(length)]
