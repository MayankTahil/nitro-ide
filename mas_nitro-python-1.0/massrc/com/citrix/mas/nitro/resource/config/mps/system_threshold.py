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

from massrc.com.citrix.mas.nitro.resource.config.mps.threshold import threshold

'''
Configuration for System Thresholds resource
'''

class system_threshold(threshold):
	_category_list=[]
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
			return "system_threshold"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(system_threshold,self).get_object_id()
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
			return "system_thresholds"
		except Exception as e :
			raise e


	'''
	List of selected event category.
	'''
	@property
	def category_list(self) :
		try:
			return self._category_list
		except Exception as e :
			raise e
	'''
	List of selected event category.
	'''
	@category_list.setter
	def category_list(self,category_list) :
		try :
			if not isinstance(category_list,list):
				raise TypeError("category_list must be set to array of str value")
			for item in category_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._category_list = category_list
		except Exception as e :
			raise e

	'''
	Get system threshold configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				system_threshold_obj=system_threshold()
				response = system_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Modify system threshold configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				system_threshold_obj=system_threshold()
				return cls.update_bulk_request(client,resource,system_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of system_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			system_threshold_obj = system_threshold()
			option_ = options()
			option_._filter=filter_
			return system_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the system_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			system_threshold_obj = system_threshold()
			option_ = options()
			option_._count=True
			response = system_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of system_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			system_threshold_obj = system_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = system_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(system_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.system_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(system_threshold_responses, response, "system_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.system_threshold_response_array
				i=0
				error = [system_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.system_threshold_response_array
			i=0
			system_threshold_objs = [system_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_system_threshold'):
					for props in obj._system_threshold:
						result = service.payload_formatter.string_to_bulk_resource(system_threshold_response,self.__class__.__name__,props)
						system_threshold_objs[i] = result.system_threshold
						i=i+1
			return system_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(system_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class system_threshold_response(base_response):
	def __init__(self,length=1) :
		self.system_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.system_threshold= [ system_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class system_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.system_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.system_threshold_response_array = [ system_threshold() for _ in range(length)]
