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
from massrc.com.citrix.mas.nitro.resource.config.mps.filter_schedule_details import filter_schedule_details


'''
Configuration for Filter Scheduler resource
'''

class filter_scheduler(base_resource):
	_details=[]
	_recurrence_type= ""
	_tz_offset= ""
	_activity_log= ""
	_filter_job_name= ""
	_recurrenceOptions= ""
	_activity_status= ""
	_id= ""
	_filter_status= ""
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
			return "filter_scheduler"
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
			return "filter_schedulers"
		except Exception as e :
			raise e



	'''
	get Filter Schedule Details
	'''
	@property
	def details(self) :
		try:
			return self._details
		except Exception as e :
			raise e
	'''
	set Filter Schedule Details
	'''
	@details.setter
	def details(self,details) :
		try :
			if not isinstance(details,list):
				raise TypeError("details must be set to array of filter_schedule_details value")
			for item in details :
				if not isinstance(item,filter_schedule_details):
					raise TypeError("item must be set to filter_schedule_details value")
			self._details = details
		except Exception as e :
			raise e


	'''
	get Tenant
	'''
	@property
	def recurrence_type(self) :
		try:
			return self._recurrence_type
		except Exception as e :
			raise e
	'''
	set Tenant
	'''
	@recurrence_type.setter
	def recurrence_type(self,recurrence_type):
		try :
			if not isinstance(recurrence_type,str):
				raise TypeError("recurrence_type must be set to str value")
			self._recurrence_type = recurrence_type
		except Exception as e :
			raise e


	'''
	get Time zone offset.
	'''
	@property
	def tz_offset(self) :
		try:
			return self._tz_offset
		except Exception as e :
			raise e
	'''
	set Time zone offset.
	'''
	@tz_offset.setter
	def tz_offset(self,tz_offset):
		try :
			if not isinstance(tz_offset,int):
				raise TypeError("tz_offset must be set to int value")
			self._tz_offset = tz_offset
		except Exception as e :
			raise e


	'''
	get Device Group Criteria
	'''
	@property
	def activity_log(self) :
		try:
			return self._activity_log
		except Exception as e :
			raise e


	'''
	get Filter Job Name
	'''
	@property
	def filter_job_name(self) :
		try:
			return self._filter_job_name
		except Exception as e :
			raise e
	'''
	set Filter Job Name
	'''
	@filter_job_name.setter
	def filter_job_name(self,filter_job_name):
		try :
			if not isinstance(filter_job_name,str):
				raise TypeError("filter_job_name must be set to str value")
			self._filter_job_name = filter_job_name
		except Exception as e :
			raise e


	'''
	get Comma Seperated recurrence options of job that is scheduled
	'''
	@property
	def recurrenceOptions(self) :
		try:
			return self._recurrenceOptions
		except Exception as e :
			raise e
	'''
	set Comma Seperated recurrence options of job that is scheduled
	'''
	@recurrenceOptions.setter
	def recurrenceOptions(self,recurrenceOptions):
		try :
			if not isinstance(recurrenceOptions,str):
				raise TypeError("recurrenceOptions must be set to str value")
			self._recurrenceOptions = recurrenceOptions
		except Exception as e :
			raise e


	'''
	get Activity Status
	'''
	@property
	def activity_status(self) :
		try:
			return self._activity_status
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the events
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the events
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
	get Device Group Criteria
	'''
	@property
	def filter_status(self) :
		try:
			return self._filter_status
		except Exception as e :
			raise e
	'''
	set Device Group Criteria
	'''
	@filter_status.setter
	def filter_status(self,filter_status):
		try :
			if not isinstance(filter_status,str):
				raise TypeError("filter_status must be set to str value")
			self._filter_status = filter_status
		except Exception as e :
			raise e

	'''
	Use this operation to add filter_scheduler.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				filter_scheduler_obj= filter_scheduler()
				return cls.perform_operation_bulk_request(service,"add", resource,filter_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete filter_scheduler.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					filter_scheduler_obj=filter_scheduler()
					return cls.delete_bulk_request(client,resource,filter_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to device group.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				filter_scheduler_obj=filter_scheduler()
				response = filter_scheduler_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify filter_scheduler.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				filter_scheduler_obj=filter_scheduler()
				return cls.update_bulk_request(client,resource,filter_scheduler_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of filter_scheduler resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			filter_scheduler_obj = filter_scheduler()
			option_ = options()
			option_._filter=filter_
			return filter_scheduler_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the filter_scheduler resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			filter_scheduler_obj = filter_scheduler()
			option_ = options()
			option_._count=True
			response = filter_scheduler_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of filter_scheduler resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			filter_scheduler_obj = filter_scheduler()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = filter_scheduler_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(filter_scheduler_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filter_scheduler
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_scheduler_responses, response, "filter_scheduler_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.filter_scheduler_response_array
				i=0
				error = [filter_scheduler() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.filter_scheduler_response_array
			i=0
			filter_scheduler_objs = [filter_scheduler() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_filter_scheduler'):
					for props in obj._filter_scheduler:
						result = service.payload_formatter.string_to_bulk_resource(filter_scheduler_response,self.__class__.__name__,props)
						filter_scheduler_objs[i] = result.filter_scheduler
						i=i+1
			return filter_scheduler_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(filter_scheduler,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class filter_scheduler_response(base_response):
	def __init__(self,length=1) :
		self.filter_scheduler= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.filter_scheduler= [ filter_scheduler() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class filter_scheduler_responses(base_response):
	def __init__(self,length=1) :
		self.filter_scheduler_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.filter_scheduler_response_array = [ filter_scheduler() for _ in range(length)]
