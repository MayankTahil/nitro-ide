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
Configuration for Task Command Log resource
'''

class task_command_log(base_resource):
	_protocol= ""
	_status= ""
	_index= ""
	_starttime= ""
	_id= ""
	_task_device_id= ""
	_endtime= ""
	_ip_address= ""
	_statusmessage= ""
	_command= ""
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
			return "task_command_log"
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
			return "task_command_logs"
		except Exception as e :
			raise e



	'''
	get Protocol
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e


	'''
	get Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Stores the order of the command.
	'''
	@property
	def index(self) :
		try:
			return self._index
		except Exception as e :
			raise e
	'''
	set Stores the order of the command.
	'''
	@index.setter
	def index(self,index):
		try :
			if not isinstance(index,int):
				raise TypeError("index must be set to int value")
			self._index = index
		except Exception as e :
			raise e


	'''
	get Start Time
	'''
	@property
	def starttime(self) :
		try:
			return self._starttime
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the task command logs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the task command logs
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
	get Task Device ID
	'''
	@property
	def task_device_id(self) :
		try:
			return self._task_device_id
		except Exception as e :
			raise e


	'''
	get End Time
	'''
	@property
	def endtime(self) :
		try:
			return self._endtime
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Status Message
	'''
	@property
	def statusmessage(self) :
		try:
			return self._statusmessage
		except Exception as e :
			raise e


	'''
	get Command
	'''
	@property
	def command(self) :
		try:
			return self._command
		except Exception as e :
			raise e

	'''
	Use this operation to get task log for each command.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				task_command_log_obj=task_command_log()
				response = task_command_log_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of task_command_log resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			task_command_log_obj = task_command_log()
			option_ = options()
			option_._filter=filter_
			return task_command_log_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the task_command_log resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			task_command_log_obj = task_command_log()
			option_ = options()
			option_._count=True
			response = task_command_log_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of task_command_log resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			task_command_log_obj = task_command_log()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = task_command_log_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(task_command_log_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.task_command_log
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(task_command_log_responses, response, "task_command_log_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.task_command_log_response_array
				i=0
				error = [task_command_log() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.task_command_log_response_array
			i=0
			task_command_log_objs = [task_command_log() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_task_command_log'):
					for props in obj._task_command_log:
						result = service.payload_formatter.string_to_bulk_resource(task_command_log_response,self.__class__.__name__,props)
						task_command_log_objs[i] = result.task_command_log
						i=i+1
			return task_command_log_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(task_command_log,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class task_command_log_response(base_response):
	def __init__(self,length=1) :
		self.task_command_log= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.task_command_log= [ task_command_log() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class task_command_log_responses(base_response):
	def __init__(self,length=1) :
		self.task_command_log_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.task_command_log_response_array = [ task_command_log() for _ in range(length)]
