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
Configuration for JournalTask configuration resource
'''

class journaltask(base_resource):
	_rollback_instruction= ""
	_status= ""
	_name= ""
	_start_time= ""
	_end_time= ""
	_service_name= ""
	_error_message= ""
	_context_id= ""
	_rollback_method= ""
	_id= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/admin/v1/journalcontexts/{context_id}/journaltasks"
		except Exception as e :
			raise e

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
			return "journaltask"
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
			return "journaltasks"
		except Exception as e :
			raise e



	'''
	get Rollback instruction for the journal task
	'''
	@property
	def rollback_instruction(self) :
		try:
			return self._rollback_instruction
		except Exception as e :
			raise e
	'''
	set Rollback instruction for the journal task
	'''
	@rollback_instruction.setter
	def rollback_instruction(self,rollback_instruction):
		try :
			if not isinstance(rollback_instruction,str):
				raise TypeError("rollback_instruction must be set to str value")
			self._rollback_instruction = rollback_instruction
		except Exception as e :
			raise e


	'''
	get Status of context could be attempted/finished/Error/Rollback in progress/Rollback Completed
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of context could be attempted/finished/Error/Rollback in progress/Rollback Completed
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Name of the context
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the context
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
	get Start time of request.
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e
	'''
	set Start time of request.
	'''
	@start_time.setter
	def start_time(self,start_time):
		try :
			if not isinstance(start_time,str):
				raise TypeError("start_time must be set to str value")
			self._start_time = start_time
		except Exception as e :
			raise e


	'''
	get End time of request
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set End time of request
	'''
	@end_time.setter
	def end_time(self,end_time):
		try :
			if not isinstance(end_time,str):
				raise TypeError("end_time must be set to str value")
			self._end_time = end_time
		except Exception as e :
			raise e


	'''
	get Name of service-request which started the context
	'''
	@property
	def service_name(self) :
		try:
			return self._service_name
		except Exception as e :
			raise e
	'''
	set Name of service-request which started the context
	'''
	@service_name.setter
	def service_name(self,service_name):
		try :
			if not isinstance(service_name,str):
				raise TypeError("service_name must be set to str value")
			self._service_name = service_name
		except Exception as e :
			raise e


	'''
	get message to be displayed if there is some error in processing journal task
	'''
	@property
	def error_message(self) :
		try:
			return self._error_message
		except Exception as e :
			raise e
	'''
	set message to be displayed if there is some error in processing journal task
	'''
	@error_message.setter
	def error_message(self,error_message):
		try :
			if not isinstance(error_message,str):
				raise TypeError("error_message must be set to str value")
			self._error_message = error_message
		except Exception as e :
			raise e


	'''
	get Request/Context id of the task
	'''
	@property
	def context_id(self) :
		try:
			return self._context_id
		except Exception as e :
			raise e
	'''
	set Request/Context id of the task
	'''
	@context_id.setter
	def context_id(self,context_id):
		try :
			if not isinstance(context_id,str):
				raise TypeError("context_id must be set to str value")
			self._context_id = context_id
		except Exception as e :
			raise e


	'''
	get Rollback method for the journal task
	'''
	@property
	def rollback_method(self) :
		try:
			return self._rollback_method
		except Exception as e :
			raise e
	'''
	set Rollback method for the journal task
	'''
	@rollback_method.setter
	def rollback_method(self,rollback_method):
		try :
			if not isinstance(rollback_method,str):
				raise TypeError("rollback_method must be set to str value")
			self._rollback_method = rollback_method
		except Exception as e :
			raise e


	'''
	get Id is sequential number identifying Journal Task
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is sequential number identifying Journal Task
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
	Use this operation to get context details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				journaltask_obj=journaltask()
				response = journaltask_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of journaltask resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			journaltask_obj = journaltask()
			option_ = options()
			option_._filter=filter_
			return journaltask_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the journaltask resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			journaltask_obj = journaltask()
			option_ = options()
			option_._count=True
			response = journaltask_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of journaltask resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			journaltask_obj = journaltask()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = journaltask_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(journaltask_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.journaltask
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(journaltask_responses, response, "journaltask_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.journaltask_response_array
				i=0
				error = [journaltask() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.journaltask_response_array
			i=0
			journaltask_objs = [journaltask() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_journaltask'):
					for props in obj._journaltask:
						result = service.payload_formatter.string_to_bulk_resource(journaltask_response,self.__class__.__name__,props)
						journaltask_objs[i] = result.journaltask
						i=i+1
			return journaltask_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(journaltask,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class journaltask_response(base_response):
	def __init__(self,length=1) :
		self.journaltask= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.journaltask= [ journaltask() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class journaltask_responses(base_response):
	def __init__(self,length=1) :
		self.journaltask_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.journaltask_response_array = [ journaltask() for _ in range(length)]
