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
Configuration for Af URL Parameter remove resource
'''

class url_parameter(base_resource):
	_remove= ""
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
			return "url_parameter"
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
			return "url_parameters"
		except Exception as e :
			raise e



	'''
	get Remove URL Parameter value
	'''
	@property
	def remove(self) :
		try:
			return self._remove
		except Exception as e :
			raise e
	'''
	set Remove URL Parameter value
	'''
	@remove.setter
	def remove(self,remove):
		try :
			if not isinstance(remove,bool):
				raise TypeError("remove must be set to bool value")
			self._remove = remove
		except Exception as e :
			raise e

	'''
	To set URL Parameter value.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				url_parameter_obj= url_parameter()
				return cls.perform_operation_bulk_request(service,"add", resource,url_parameter_obj)
		except Exception as e :
			raise e

	'''
	To get URL Parameter value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				url_parameter_obj=url_parameter()
				response = url_parameter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set URL Parameter value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				url_parameter_obj=url_parameter()
				return cls.update_bulk_request(client,resource,url_parameter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of url_parameter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			url_parameter_obj = url_parameter()
			option_ = options()
			option_._filter=filter_
			return url_parameter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the url_parameter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			url_parameter_obj = url_parameter()
			option_ = options()
			option_._count=True
			response = url_parameter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of url_parameter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			url_parameter_obj = url_parameter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = url_parameter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(url_parameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.url_parameter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(url_parameter_responses, response, "url_parameter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.url_parameter_response_array
				i=0
				error = [url_parameter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.url_parameter_response_array
			i=0
			url_parameter_objs = [url_parameter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_url_parameter'):
					for props in obj._url_parameter:
						result = service.payload_formatter.string_to_bulk_resource(url_parameter_response,self.__class__.__name__,props)
						url_parameter_objs[i] = result.url_parameter
						i=i+1
			return url_parameter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(url_parameter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class url_parameter_response(base_response):
	def __init__(self,length=1) :
		self.url_parameter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.url_parameter= [ url_parameter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class url_parameter_responses(base_response):
	def __init__(self,length=1) :
		self.url_parameter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.url_parameter_response_array = [ url_parameter() for _ in range(length)]
