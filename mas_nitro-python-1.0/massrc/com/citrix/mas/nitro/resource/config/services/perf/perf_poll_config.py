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
Configuration for Perf Poll Configuration resource
'''

class perf_poll_config(base_resource):
	_polling_interval= ""
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
			return "perf_poll_config"
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
			return "perf_poll_configs"
		except Exception as e :
			raise e



	'''
	get Polling interval in minutes
	'''
	@property
	def polling_interval(self) :
		try:
			return self._polling_interval
		except Exception as e :
			raise e
	'''
	set Polling interval in minutes
	'''
	@polling_interval.setter
	def polling_interval(self,polling_interval):
		try :
			if not isinstance(polling_interval,int):
				raise TypeError("polling_interval must be set to int value")
			self._polling_interval = polling_interval
		except Exception as e :
			raise e

	'''
	Use this operation to get the poll interval in minutes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_poll_config_obj=perf_poll_config()
				response = perf_poll_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify the poll interval in minutes.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_poll_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_poll_config_obj = perf_poll_config()
			option_ = options()
			option_._filter=filter_
			return perf_poll_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_poll_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_poll_config_obj = perf_poll_config()
			option_ = options()
			option_._count=True
			response = perf_poll_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_poll_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_poll_config_obj = perf_poll_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_poll_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_poll_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_poll_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_poll_config_responses, response, "perf_poll_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_poll_config_response_array
				i=0
				error = [perf_poll_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_poll_config_response_array
			i=0
			perf_poll_config_objs = [perf_poll_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_poll_config'):
					for props in obj._perf_poll_config:
						result = service.payload_formatter.string_to_bulk_resource(perf_poll_config_response,self.__class__.__name__,props)
						perf_poll_config_objs[i] = result.perf_poll_config
						i=i+1
			return perf_poll_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_poll_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_poll_config_response(base_response):
	def __init__(self,length=1) :
		self.perf_poll_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_poll_config= [ perf_poll_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_poll_config_responses(base_response):
	def __init__(self,length=1) :
		self.perf_poll_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_poll_config_response_array = [ perf_poll_config() for _ in range(length)]
