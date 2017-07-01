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
Configuration for AF CPX Support resource
'''

class af_cpx_support(base_resource):
	_enable= ""
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
			return "af_cpx_support"
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
			return "af_cpx_supports"
		except Exception as e :
			raise e



	'''
	get AF CPX Support enable value
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set AF CPX Support enable value
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e

	'''
	To get the AF CPX Support enable value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_cpx_support_obj=af_cpx_support()
				response = af_cpx_support_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set the AF URL Support enable value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				af_cpx_support_obj=af_cpx_support()
				return cls.update_bulk_request(client,resource,af_cpx_support_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_cpx_support resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_cpx_support_obj = af_cpx_support()
			option_ = options()
			option_._filter=filter_
			return af_cpx_support_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_cpx_support resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_cpx_support_obj = af_cpx_support()
			option_ = options()
			option_._count=True
			response = af_cpx_support_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_cpx_support resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_cpx_support_obj = af_cpx_support()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_cpx_support_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_cpx_support_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_cpx_support
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_cpx_support_responses, response, "af_cpx_support_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_cpx_support_response_array
				i=0
				error = [af_cpx_support() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_cpx_support_response_array
			i=0
			af_cpx_support_objs = [af_cpx_support() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_af_cpx_support'):
					for props in obj._af_cpx_support:
						result = service.payload_formatter.string_to_bulk_resource(af_cpx_support_response,self.__class__.__name__,props)
						af_cpx_support_objs[i] = result.af_cpx_support
						i=i+1
			return af_cpx_support_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_cpx_support,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_cpx_support_response(base_response):
	def __init__(self,length=1) :
		self.af_cpx_support= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_cpx_support= [ af_cpx_support() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_cpx_support_responses(base_response):
	def __init__(self,length=1) :
		self.af_cpx_support_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_cpx_support_response_array = [ af_cpx_support() for _ in range(length)]
