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
Configuration for Managed Device Summary resource
'''

class managed_device_summary(base_resource):
	_category_type= ""
	_device_type= ""
	_device_family= ""
	_value= ""
	_subcategory_type= ""
	_category_name= ""
	_subcategory_name= ""
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
			return "managed_device_summary"
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
			return "managed_device_summarys"
		except Exception as e :
			raise e



	'''
	get Type of Category
	'''
	@property
	def category_type(self) :
		try:
			return self._category_type
		except Exception as e :
			raise e
	'''
	set Type of Category
	'''
	@category_type.setter
	def category_type(self,category_type):
		try :
			if not isinstance(category_type,str):
				raise TypeError("category_type must be set to str value")
			self._category_type = category_type
		except Exception as e :
			raise e


	'''
	get Device Type
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set Device Type
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
		except Exception as e :
			raise e


	'''
	get Device family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device family
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
	get Value of category
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set Value of category
	'''
	@value.setter
	def value(self,value):
		try :
			if not isinstance(value,float):
				raise TypeError("value must be set to float value")
			self._value = value
		except Exception as e :
			raise e


	'''
	get Type of Subcategory
	'''
	@property
	def subcategory_type(self) :
		try:
			return self._subcategory_type
		except Exception as e :
			raise e
	'''
	set Type of Subcategory
	'''
	@subcategory_type.setter
	def subcategory_type(self,subcategory_type):
		try :
			if not isinstance(subcategory_type,str):
				raise TypeError("subcategory_type must be set to str value")
			self._subcategory_type = subcategory_type
		except Exception as e :
			raise e


	'''
	get Name of Category
	'''
	@property
	def category_name(self) :
		try:
			return self._category_name
		except Exception as e :
			raise e
	'''
	set Name of Category
	'''
	@category_name.setter
	def category_name(self,category_name):
		try :
			if not isinstance(category_name,str):
				raise TypeError("category_name must be set to str value")
			self._category_name = category_name
		except Exception as e :
			raise e


	'''
	get Name of Subcategory
	'''
	@property
	def subcategory_name(self) :
		try:
			return self._subcategory_name
		except Exception as e :
			raise e
	'''
	set Name of Subcategory
	'''
	@subcategory_name.setter
	def subcategory_name(self,subcategory_name):
		try :
			if not isinstance(subcategory_name,str):
				raise TypeError("subcategory_name must be set to str value")
			self._subcategory_name = subcategory_name
		except Exception as e :
			raise e

	'''
	Use this operation to get managed device summary.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				managed_device_summary_obj=managed_device_summary()
				response = managed_device_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of managed_device_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			managed_device_summary_obj = managed_device_summary()
			option_ = options()
			option_._filter=filter_
			return managed_device_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the managed_device_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			managed_device_summary_obj = managed_device_summary()
			option_ = options()
			option_._count=True
			response = managed_device_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of managed_device_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			managed_device_summary_obj = managed_device_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = managed_device_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(managed_device_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.managed_device_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_device_summary_responses, response, "managed_device_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.managed_device_summary_response_array
				i=0
				error = [managed_device_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.managed_device_summary_response_array
			i=0
			managed_device_summary_objs = [managed_device_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_managed_device_summary'):
					for props in obj._managed_device_summary:
						result = service.payload_formatter.string_to_bulk_resource(managed_device_summary_response,self.__class__.__name__,props)
						managed_device_summary_objs[i] = result.managed_device_summary
						i=i+1
			return managed_device_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(managed_device_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class managed_device_summary_response(base_response):
	def __init__(self,length=1) :
		self.managed_device_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.managed_device_summary= [ managed_device_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class managed_device_summary_responses(base_response):
	def __init__(self,length=1) :
		self.managed_device_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.managed_device_summary_response_array = [ managed_device_summary() for _ in range(length)]
