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
Configuration for event category resource
'''

class event_category(base_resource):
	_product_type= ""
	_action= ""
	_category= ""
	_display_name= ""
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
			return "event_category"
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
			return "event_categorys"
		except Exception as e :
			raise e


	'''
	Product type
	'''
	@property
	def product_type(self):
		try:
			return self._product_type
		except Exception as e :
			raise e

	'''
	Event category action
	'''
	@property
	def action(self):
		try:
			return self._action
		except Exception as e :
			raise e
	'''
	Event category action
	'''
	@action.setter
	def action(self,action):
		try :
			if not isinstance(action,str):
				raise TypeError("action must be set to str value")
			self._action = action
		except Exception as e :
			raise e

	'''
	Event category
	'''
	@property
	def category(self):
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	Event category
	'''
	@category.setter
	def category(self,category):
		try :
			if not isinstance(category,str):
				raise TypeError("category must be set to str value")
			self._category = category
		except Exception as e :
			raise e

	'''
	Event category display name
	'''
	@property
	def display_name(self):
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	Event category display name
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e

	'''
	Get event category.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				event_category_obj=event_category()
				response = event_category_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of event_category resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			event_category_obj = event_category()
			option_ = options()
			option_._filter=filter_
			return event_category_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the event_category resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			event_category_obj = event_category()
			option_ = options()
			option_._count=True
			response = event_category_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of event_category resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			event_category_obj = event_category()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = event_category_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(event_category_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.event_category
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(event_category_responses, response, "event_category_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.event_category_response_array
				i=0
				error = [event_category() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.event_category_response_array
			i=0
			event_category_objs = [event_category() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_event_category'):
					for props in obj._event_category:
						result = service.payload_formatter.string_to_bulk_resource(event_category_response,self.__class__.__name__,props)
						event_category_objs[i] = result.event_category
						i=i+1
			return event_category_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(event_category,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class event_category_response(base_response):
	def __init__(self,length=1) :
		self.event_category= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.event_category= [ event_category() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class event_category_responses(base_response):
	def __init__(self,length=1) :
		self.event_category_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.event_category_response_array = [ event_category() for _ in range(length)]
