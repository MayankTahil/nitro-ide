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
from massrc.com.citrix.mas.nitro.resource.config.mps.task_device_log import task_device_log
from massrc.com.citrix.mas.nitro.resource.config.mps.config_command import config_command

from massrc.com.citrix.mas.nitro.resource.config.mps.config_job import config_job

'''
Configuration for Configuration Job Details resource
'''

class config_job_details(config_job):
	_devices_info=[]
	_commands_count= ""
	_variables_count= ""
	_device_family= ""
	_commands=[]
	_nextScheduleTimeEpoch= ""
	_filename= ""
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
			return "config_job_details"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(config_job_details,self).get_object_id()
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
			return "config_job_detailss"
		except Exception as e :
			raise e



	'''
	get Array of device task logs
	'''
	@property
	def devices_info(self) :
		try:
			return self._devices_info
		except Exception as e :
			raise e
	'''
	set Array of device task logs
	'''
	@devices_info.setter
	def devices_info(self,devices_info) :
		try :
			if not isinstance(devices_info,list):
				raise TypeError("devices_info must be set to array of task_device_log value")
			for item in devices_info :
				if not isinstance(item,task_device_log):
					raise TypeError("item must be set to task_device_log value")
			self._devices_info = devices_info
		except Exception as e :
			raise e


	'''
	get Number of Commands to be executed on each device
	'''
	@property
	def commands_count(self) :
		try:
			return self._commands_count
		except Exception as e :
			raise e


	'''
	get Number of Variables used in config commands
	'''
	@property
	def variables_count(self) :
		try:
			return self._variables_count
		except Exception as e :
			raise e


	'''
	get Family of Devices for which config template is defined.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of Devices for which config template is defined.
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
	get Array of commands part of the configuration template
	'''
	@property
	def commands(self) :
		try:
			return self._commands
		except Exception as e :
			raise e
	'''
	set Array of commands part of the configuration template
	'''
	@commands.setter
	def commands(self,commands) :
		try :
			if not isinstance(commands,list):
				raise TypeError("commands must be set to array of config_command value")
			for item in commands :
				if not isinstance(item,config_command):
					raise TypeError("item must be set to config_command value")
			self._commands = commands
		except Exception as e :
			raise e


	'''
	get Next Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def nextScheduleTimeEpoch(self) :
		try:
			return self._nextScheduleTimeEpoch
		except Exception as e :
			raise e
	'''
	set Next Schedule time epoch (string representation of 11 digit numbers).
	'''
	@nextScheduleTimeEpoch.setter
	def nextScheduleTimeEpoch(self,nextScheduleTimeEpoch):
		try :
			if not isinstance(nextScheduleTimeEpoch,str):
				raise TypeError("nextScheduleTimeEpoch must be set to str value")
			self._nextScheduleTimeEpoch = nextScheduleTimeEpoch
		except Exception as e :
			raise e

	'''
	Output Filename
	'''
	@property
	def filename(self):
		try:
			return self._filename
		except Exception as e :
			raise e
	'''
	Output Filename
	'''
	@filename.setter
	def filename(self,filename):
		try :
			if not isinstance(filename,str):
				raise TypeError("filename must be set to str value")
			self._filename = filename
		except Exception as e :
			raise e

	'''
	Use this operation to get details of configuration job.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				config_job_details_obj=config_job_details()
				response = config_job_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of config_job_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			config_job_details_obj = config_job_details()
			option_ = options()
			option_._filter=filter_
			return config_job_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the config_job_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			config_job_details_obj = config_job_details()
			option_ = options()
			option_._count=True
			response = config_job_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of config_job_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			config_job_details_obj = config_job_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = config_job_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(config_job_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_job_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_job_details_responses, response, "config_job_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_job_details_response_array
				i=0
				error = [config_job_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_job_details_response_array
			i=0
			config_job_details_objs = [config_job_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_job_details'):
					for props in obj._config_job_details:
						result = service.payload_formatter.string_to_bulk_resource(config_job_details_response,self.__class__.__name__,props)
						config_job_details_objs[i] = result.config_job_details
						i=i+1
			return config_job_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_job_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_job_details_response(base_response):
	def __init__(self,length=1) :
		self.config_job_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_job_details= [ config_job_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_job_details_responses(base_response):
	def __init__(self,length=1) :
		self.config_job_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_job_details_response_array = [ config_job_details() for _ in range(length)]
