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
from massrc.com.citrix.mas.nitro.resource.config.mps.filter_action import filter_action
from massrc.com.citrix.mas.nitro.resource.config.mps.filter_criteria import filter_criteria


'''
Configuration for event filter criteria properties resource
'''

class event_filter(base_resource):
	_is_enabled= ""
	_actions=[]
	_event_age_threshold= ""
	_name= ""
	_id= ""
	_criteria= ""
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
			return "event_filter"
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
			return "event_filters"
		except Exception as e :
			raise e



	'''
	get enabled or disabled
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set enabled or disabled
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,bool):
				raise TypeError("is_enabled must be set to bool value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get Filter actions
	'''
	@property
	def actions(self) :
		try:
			return self._actions
		except Exception as e :
			raise e
	'''
	set Filter actions
	'''
	@actions.setter
	def actions(self,actions) :
		try :
			if not isinstance(actions,list):
				raise TypeError("actions must be set to array of filter_action value")
			for item in actions :
				if not isinstance(item,filter_action):
					raise TypeError("item must be set to filter_action value")
			self._actions = actions
		except Exception as e :
			raise e


	'''
	get Event Age Threshold
	'''
	@property
	def event_age_threshold(self) :
		try:
			return self._event_age_threshold
		except Exception as e :
			raise e
	'''
	set Event Age Threshold
	'''
	@event_age_threshold.setter
	def event_age_threshold(self,event_age_threshold):
		try :
			if not isinstance(event_age_threshold,int):
				raise TypeError("event_age_threshold must be set to int value")
			self._event_age_threshold = event_age_threshold
		except Exception as e :
			raise e


	'''
	get Filter Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Filter Name
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
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Filter criteria props
	'''
	@property
	def criteria(self) :
		try:
			return self._criteria
		except Exception as e :
			raise e
	'''
	set Filter criteria props
	'''
	@criteria.setter
	def criteria(self,criteria):
		try :
			if not isinstance(criteria,filter_criteria):
				raise TypeError("criteria must be set to filter_criteria value")
			self._criteria = criteria
		except Exception as e :
			raise e

	'''
	add event filter.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				event_filter_obj= event_filter()
				return cls.perform_operation_bulk_request(service,"add", resource,event_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete event filters.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					event_filter_obj=event_filter()
					return cls.delete_bulk_request(client,resource,event_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get filters.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				event_filter_obj=event_filter()
				response = event_filter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify event filter.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				event_filter_obj=event_filter()
				return cls.update_bulk_request(client,resource,event_filter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of event_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			event_filter_obj = event_filter()
			option_ = options()
			option_._filter=filter_
			return event_filter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the event_filter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			event_filter_obj = event_filter()
			option_ = options()
			option_._count=True
			response = event_filter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of event_filter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			event_filter_obj = event_filter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = event_filter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(event_filter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.event_filter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(event_filter_responses, response, "event_filter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.event_filter_response_array
				i=0
				error = [event_filter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.event_filter_response_array
			i=0
			event_filter_objs = [event_filter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_event_filter'):
					for props in obj._event_filter:
						result = service.payload_formatter.string_to_bulk_resource(event_filter_response,self.__class__.__name__,props)
						event_filter_objs[i] = result.event_filter
						i=i+1
			return event_filter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(event_filter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class event_filter_response(base_response):
	def __init__(self,length=1) :
		self.event_filter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.event_filter= [ event_filter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class event_filter_responses(base_response):
	def __init__(self,length=1) :
		self.event_filter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.event_filter_response_array = [ event_filter() for _ in range(length)]
