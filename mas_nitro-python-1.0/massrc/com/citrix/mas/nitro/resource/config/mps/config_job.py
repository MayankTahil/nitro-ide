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
from massrc.com.citrix.mas.nitro.resource.config.mps.variable_values import variable_values
from massrc.com.citrix.mas.nitro.resource.config.mps.configuration_template import configuration_template


'''
Configuration for Configuration Job resource
'''

class config_job(base_resource):
	_status= ""
	_scheduleTimes= ""
	_sms_profiles= ""
	_variables=[]
	_execute_sequentially= ""
	_lastExecutedTimeEpoch= ""
	_tenant_id= ""
	_execute_password= ""
	_node_id= ""
	_timestamp= ""
	_devices_db= ""
	_id= ""
	_lastExecutionStatus= ""
	_scheduleTimesEpoch= ""
	_credentials_required= ""
	_device_family= ""
	_device_groups=[]
	_tasklog_id= ""
	_name= ""
	_template_info= ""
	_on_error= ""
	_devices=[]
	_scheduleOptions= ""
	_tz_offset= ""
	_username= ""
	_mail_profiles= ""
	_device_groups_db= ""
	_scheduleType= ""
	_nextScheduleTimeEpoch= ""
	_execute_username= ""
	_preview_commands=[]
	_devices_count= ""
	_devices_completed_count= ""
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
			return "config_job"
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
			return "config_jobs"
		except Exception as e :
			raise e



	'''
	get Status of Config Job
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Comma Seperated times of the day(HH:MM) on which Configuration Template is scheduled
	'''
	@property
	def scheduleTimes(self) :
		try:
			return self._scheduleTimes
		except Exception as e :
			raise e
	'''
	set Comma Seperated times of the day(HH:MM) on which Configuration Template is scheduled
	'''
	@scheduleTimes.setter
	def scheduleTimes(self,scheduleTimes):
		try :
			if not isinstance(scheduleTimes,str):
				raise TypeError("scheduleTimes must be set to str value")
			self._scheduleTimes = scheduleTimes
		except Exception as e :
			raise e


	'''
	get Comma seperated list of SMS profiles
	'''
	@property
	def sms_profiles(self) :
		try:
			return self._sms_profiles
		except Exception as e :
			raise e
	'''
	set Comma seperated list of SMS profiles
	'''
	@sms_profiles.setter
	def sms_profiles(self,sms_profiles):
		try :
			if not isinstance(sms_profiles,str):
				raise TypeError("sms_profiles must be set to str value")
			self._sms_profiles = sms_profiles
		except Exception as e :
			raise e


	'''
	get Values of Variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of variable_values value")
			for item in variables :
				if not isinstance(item,variable_values):
					raise TypeError("item must be set to variable_values value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get True if configuration template is to be applied to devices sequentially
	'''
	@property
	def execute_sequentially(self) :
		try:
			return self._execute_sequentially
		except Exception as e :
			raise e
	'''
	set True if configuration template is to be applied to devices sequentially
	'''
	@execute_sequentially.setter
	def execute_sequentially(self,execute_sequentially):
		try :
			if not isinstance(execute_sequentially,bool):
				raise TypeError("execute_sequentially must be set to bool value")
			self._execute_sequentially = execute_sequentially
		except Exception as e :
			raise e


	'''
	get Schedule time epoch at which job was last executed.
	'''
	@property
	def lastExecutedTimeEpoch(self) :
		try:
			return self._lastExecutedTimeEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch at which job was last executed.
	'''
	@lastExecutedTimeEpoch.setter
	def lastExecutedTimeEpoch(self,lastExecutedTimeEpoch):
		try :
			if not isinstance(lastExecutedTimeEpoch,str):
				raise TypeError("lastExecutedTimeEpoch must be set to str value")
			self._lastExecutedTimeEpoch = lastExecutedTimeEpoch
		except Exception as e :
			raise e


	'''
	get Tenant Id of the Config Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Execute Password for job
	'''
	@property
	def execute_password(self) :
		try:
			return self._execute_password
		except Exception as e :
			raise e
	'''
	set Execute Password for job
	'''
	@execute_password.setter
	def execute_password(self,execute_password):
		try :
			if not isinstance(execute_password,str):
				raise TypeError("execute_password must be set to str value")
			self._execute_password = execute_password
		except Exception as e :
			raise e


	'''
	get Node id of the node executing the task in a Multinode / HA deployment
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Node id of the node executing the task in a Multinode / HA deployment
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e


	'''
	get Time of Creation of Configuration Job
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Device IP Address List Comma Seperated on which job is run
	'''
	@property
	def devices_db(self) :
		try:
			return self._devices_db
		except Exception as e :
			raise e
	'''
	set Device IP Address List Comma Seperated on which job is run
	'''
	@devices_db.setter
	def devices_db(self,devices_db):
		try :
			if not isinstance(devices_db,str):
				raise TypeError("devices_db must be set to str value")
			self._devices_db = devices_db
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the configuration jobs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the configuration jobs
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
	get Status of last Execution of Config Job
	'''
	@property
	def lastExecutionStatus(self) :
		try:
			return self._lastExecutionStatus
		except Exception as e :
			raise e


	'''
	get Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def scheduleTimesEpoch(self) :
		try:
			return self._scheduleTimesEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch (string representation of 11 digit numbers).
	'''
	@scheduleTimesEpoch.setter
	def scheduleTimesEpoch(self,scheduleTimesEpoch):
		try :
			if not isinstance(scheduleTimesEpoch,str):
				raise TypeError("scheduleTimesEpoch must be set to str value")
			self._scheduleTimesEpoch = scheduleTimesEpoch
		except Exception as e :
			raise e


	'''
	get True if username/password need to be asked before configuration template is to applied on devices
	'''
	@property
	def credentials_required(self) :
		try:
			return self._credentials_required
		except Exception as e :
			raise e
	'''
	set True if username/password need to be asked before configuration template is to applied on devices
	'''
	@credentials_required.setter
	def credentials_required(self,credentials_required):
		try :
			if not isinstance(credentials_required,bool):
				raise TypeError("credentials_required must be set to bool value")
			self._credentials_required = credentials_required
		except Exception as e :
			raise e


	'''
	get Family of Devices for which config job was executed
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Family of Devices for which config job was executed
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
	get Device Group Array on which for which job is run
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	set Device Group Array on which for which job is run
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e


	'''
	get Task Log Id of the Config Job
	'''
	@property
	def tasklog_id(self) :
		try:
			return self._tasklog_id
		except Exception as e :
			raise e
	'''
	set Task Log Id of the Config Job
	'''
	@tasklog_id.setter
	def tasklog_id(self,tasklog_id):
		try :
			if not isinstance(tasklog_id,str):
				raise TypeError("tasklog_id must be set to str value")
			self._tasklog_id = tasklog_id
		except Exception as e :
			raise e


	'''
	get Name of configuration job
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of configuration job
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
	get Configuration Template to be executed/scheduled
	'''
	@property
	def template_info(self) :
		try:
			return self._template_info
		except Exception as e :
			raise e
	'''
	set Configuration Template to be executed/scheduled
	'''
	@template_info.setter
	def template_info(self,template_info):
		try :
			if not isinstance(template_info,configuration_template):
				raise TypeError("template_info must be set to configuration_template value")
			self._template_info = template_info
		except Exception as e :
			raise e


	'''
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@on_error.setter
	def on_error(self,on_error):
		try :
			if not isinstance(on_error,str):
				raise TypeError("on_error must be set to str value")
			self._on_error = on_error
		except Exception as e :
			raise e


	'''
	get Device IP Address Array on which job is run
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Device IP Address Array on which job is run
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e


	'''
	get Comma Seperated Options for scheduling Configuration Template
	'''
	@property
	def scheduleOptions(self) :
		try:
			return self._scheduleOptions
		except Exception as e :
			raise e
	'''
	set Comma Seperated Options for scheduling Configuration Template
	'''
	@scheduleOptions.setter
	def scheduleOptions(self,scheduleOptions):
		try :
			if not isinstance(scheduleOptions,str):
				raise TypeError("scheduleOptions must be set to str value")
			self._scheduleOptions = scheduleOptions
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
	get Name of user who created configuration job
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Comma seperated list of Mail profiles
	'''
	@property
	def mail_profiles(self) :
		try:
			return self._mail_profiles
		except Exception as e :
			raise e
	'''
	set Comma seperated list of Mail profiles
	'''
	@mail_profiles.setter
	def mail_profiles(self,mail_profiles):
		try :
			if not isinstance(mail_profiles,str):
				raise TypeError("mail_profiles must be set to str value")
			self._mail_profiles = mail_profiles
		except Exception as e :
			raise e


	'''
	get Device Groups List Comma Seperated on which job is run
	'''
	@property
	def device_groups_db(self) :
		try:
			return self._device_groups_db
		except Exception as e :
			raise e
	'''
	set Device Groups List Comma Seperated on which job is run
	'''
	@device_groups_db.setter
	def device_groups_db(self,device_groups_db):
		try :
			if not isinstance(device_groups_db,str):
				raise TypeError("device_groups_db must be set to str value")
			self._device_groups_db = device_groups_db
		except Exception as e :
			raise e


	'''
	get Schedule Type of Configuration Template that is scheduled
	'''
	@property
	def scheduleType(self) :
		try:
			return self._scheduleType
		except Exception as e :
			raise e
	'''
	set Schedule Type of Configuration Template that is scheduled
	'''
	@scheduleType.setter
	def scheduleType(self,scheduleType):
		try :
			if not isinstance(scheduleType,str):
				raise TypeError("scheduleType must be set to str value")
			self._scheduleType = scheduleType
		except Exception as e :
			raise e


	'''
	get Schedule time epoch at which job is scheduled to be run next.
	'''
	@property
	def nextScheduleTimeEpoch(self) :
		try:
			return self._nextScheduleTimeEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch at which job is scheduled to be run next.
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
	get Execute User Name for job
	'''
	@property
	def execute_username(self) :
		try:
			return self._execute_username
		except Exception as e :
			raise e
	'''
	set Execute User Name for job
	'''
	@execute_username.setter
	def execute_username(self,execute_username):
		try :
			if not isinstance(execute_username,str):
				raise TypeError("execute_username must be set to str value")
			self._execute_username = execute_username
		except Exception as e :
			raise e

	'''
	Preview of list of commands
	'''
	@property
	def preview_commands(self) :
		try:
			return self._preview_commands
		except Exception as e :
			raise e
	'''
	Preview of list of commands
	'''
	@preview_commands.setter
	def preview_commands(self,preview_commands) :
		try :
			if not isinstance(preview_commands,list):
				raise TypeError("preview_commands must be set to array of str value")
			for item in preview_commands :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._preview_commands = preview_commands
		except Exception as e :
			raise e

	'''
	Number of Devices on which commands executed
	'''
	@property
	def devices_count(self):
		try:
			return self._devices_count
		except Exception as e :
			raise e

	'''
	Devices Completed Count
	'''
	@property
	def devices_completed_count(self):
		try:
			return self._devices_completed_count
		except Exception as e :
			raise e

	'''
	Use this operation to run config job.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				config_job_obj= config_job()
				return cls.perform_operation_bulk_request(service,"add", resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete config job.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					config_job_obj=config_job()
					return cls.delete_bulk_request(client,resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get config job.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				config_job_obj=config_job()
				response = config_job_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update config job.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				config_job_obj=config_job()
				return cls.update_bulk_request(client,resource,config_job_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of config_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._filter=filter_
			return config_job_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the config_job resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._count=True
			response = config_job_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of config_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			config_job_obj = config_job()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = config_job_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(config_job_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.config_job
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(config_job_responses, response, "config_job_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.config_job_response_array
				i=0
				error = [config_job() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.config_job_response_array
			i=0
			config_job_objs = [config_job() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_config_job'):
					for props in obj._config_job:
						result = service.payload_formatter.string_to_bulk_resource(config_job_response,self.__class__.__name__,props)
						config_job_objs[i] = result.config_job
						i=i+1
			return config_job_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(config_job,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class config_job_response(base_response):
	def __init__(self,length=1) :
		self.config_job= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.config_job= [ config_job() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class config_job_responses(base_response):
	def __init__(self,length=1) :
		self.config_job_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.config_job_response_array = [ config_job() for _ in range(length)]
