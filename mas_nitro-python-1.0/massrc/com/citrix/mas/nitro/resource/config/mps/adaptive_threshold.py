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
Configuration for Af report sys log for adaptive threshold resource
'''

class adaptive_threshold(base_resource):
	_threshold_value= ""
	_monitor_duration= ""
	_id= ""
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
			return "adaptive_threshold"
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
			return "adaptive_thresholds"
		except Exception as e :
			raise e



	'''
	get threshold value in percentage
	'''
	@property
	def threshold_value(self) :
		try:
			return self._threshold_value
		except Exception as e :
			raise e
	'''
	set threshold value in percentage
	'''
	@threshold_value.setter
	def threshold_value(self,threshold_value):
		try :
			if not isinstance(threshold_value,int):
				raise TypeError("threshold_value must be set to int value")
			self._threshold_value = threshold_value
		except Exception as e :
			raise e


	'''
	get threshold monitoring duration.
	'''
	@property
	def monitor_duration(self) :
		try:
			return self._monitor_duration
		except Exception as e :
			raise e
	'''
	set threshold monitoring duration.
	'''
	@monitor_duration.setter
	def monitor_duration(self,monitor_duration):
		try :
			if not isinstance(monitor_duration,str):
				raise TypeError("monitor_duration must be set to str value")
			self._monitor_duration = monitor_duration
		except Exception as e :
			raise e


	'''
	get Id is Adaptive threshold ID
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is Adaptive threshold ID
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
	Use this operation to add threshold.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				adaptive_threshold_obj= adaptive_threshold()
				return cls.perform_operation_bulk_request(service,"add", resource,adaptive_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete threshold.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					adaptive_threshold_obj=adaptive_threshold()
					return cls.delete_bulk_request(client,resource,adaptive_threshold_obj)
		except Exception as e :
			raise e

	'''
	Af Report for Adaptive Threshold Monitoring..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				adaptive_threshold_obj=adaptive_threshold()
				response = adaptive_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify threshold.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				adaptive_threshold_obj=adaptive_threshold()
				return cls.update_bulk_request(client,resource,adaptive_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of adaptive_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			adaptive_threshold_obj = adaptive_threshold()
			option_ = options()
			option_._filter=filter_
			return adaptive_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the adaptive_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			adaptive_threshold_obj = adaptive_threshold()
			option_ = options()
			option_._count=True
			response = adaptive_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of adaptive_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			adaptive_threshold_obj = adaptive_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = adaptive_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(adaptive_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.adaptive_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(adaptive_threshold_responses, response, "adaptive_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.adaptive_threshold_response_array
				i=0
				error = [adaptive_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.adaptive_threshold_response_array
			i=0
			adaptive_threshold_objs = [adaptive_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_adaptive_threshold'):
					for props in obj._adaptive_threshold:
						result = service.payload_formatter.string_to_bulk_resource(adaptive_threshold_response,self.__class__.__name__,props)
						adaptive_threshold_objs[i] = result.adaptive_threshold
						i=i+1
			return adaptive_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(adaptive_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class adaptive_threshold_response(base_response):
	def __init__(self,length=1) :
		self.adaptive_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.adaptive_threshold= [ adaptive_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class adaptive_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.adaptive_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.adaptive_threshold_response_array = [ adaptive_threshold() for _ in range(length)]
