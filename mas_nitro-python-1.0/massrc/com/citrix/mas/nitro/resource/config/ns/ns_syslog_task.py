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


'''
Configuration for NS Syslog Configure Task resource
'''

class ns_syslog_task(base_resource):
	_scheduleTimesEpoch= ""
	_device_family= ""
	_device_groups=[]
	_scheduleTimes= ""
	_variables=[]
	_on_error= ""
	_port= ""
	_execute_sequentially= ""
	_tz_offset= ""
	_scheduleOptions= ""
	_devices=[]
	_scheduleType= ""
	_ip_address= ""
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
			return "ns_syslog_task"
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
			return "ns_syslog_tasks"
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
	get Device Group Array on which for which template is applied
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	set Device Group Array on which for which template is applied
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
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
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
	get Syslog server port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Syslog server port
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
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
	get Device IP Address Array on which template is applied
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Device IP Address Array on which template is applied
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
	get Syslog server IP address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Syslog server IP address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to add device profile.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_syslog_task_obj= ns_syslog_task()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_syslog_task_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete device profile(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_syslog_task_obj=ns_syslog_task()
					return cls.delete_bulk_request(client,resource,ns_syslog_task_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get device profiles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_syslog_task_obj=ns_syslog_task()
				response = ns_syslog_task_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_syslog_task resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_syslog_task_obj = ns_syslog_task()
			option_ = options()
			option_._filter=filter_
			return ns_syslog_task_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_syslog_task resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_syslog_task_obj = ns_syslog_task()
			option_ = options()
			option_._count=True
			response = ns_syslog_task_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_syslog_task resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_syslog_task_obj = ns_syslog_task()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_syslog_task_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_syslog_task_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_syslog_task
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_syslog_task_responses, response, "ns_syslog_task_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_syslog_task_response_array
				i=0
				error = [ns_syslog_task() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_syslog_task_response_array
			i=0
			ns_syslog_task_objs = [ns_syslog_task() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_syslog_task'):
					for props in obj._ns_syslog_task:
						result = service.payload_formatter.string_to_bulk_resource(ns_syslog_task_response,self.__class__.__name__,props)
						ns_syslog_task_objs[i] = result.ns_syslog_task
						i=i+1
			return ns_syslog_task_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_syslog_task,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_syslog_task_response(base_response):
	def __init__(self,length=1) :
		self.ns_syslog_task= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_syslog_task= [ ns_syslog_task() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_syslog_task_responses(base_response):
	def __init__(self,length=1) :
		self.ns_syslog_task_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_syslog_task_response_array = [ ns_syslog_task() for _ in range(length)]
