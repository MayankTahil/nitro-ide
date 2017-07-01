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
from massrc.com.citrix.mas.nitro.resource.config.mps.eventHistory import eventHistory


'''
Configuration for Event resource
'''

class event(base_resource):
	_counter_threshold_value= ""
	_source= ""
	_cmd_exec_status= ""
	_device_entity_type= ""
	_trap_id= ""
	_entity= ""
	_device_type= ""
	_timestamp= ""
	_operation_type= ""
	_id= ""
	_category= ""
	_severity= ""
	_failureobj= ""
	_source_event_id= ""
	_event_history=[]
	_history= ""
	_device_family= ""
	_rpt_sample_time= ""
	_message= ""
	_user_name= ""
	_device_entity_name= ""
	_config_cmd= ""
	_cmd_auth_status= ""
	_counter_actual_value= ""
	_current_value= ""
	_threshold_value= ""
	_entity_type= ""
	_hostname= ""
	_matched_filters= ""
	_managed_device_id= ""
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
			return "event"
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
			return "events"
		except Exception as e :
			raise e



	'''
	get device threshold value for any threadhold violated traps
	'''
	@property
	def counter_threshold_value(self) :
		try:
			return self._counter_threshold_value
		except Exception as e :
			raise e
	'''
	set device threshold value for any threadhold violated traps
	'''
	@counter_threshold_value.setter
	def counter_threshold_value(self,counter_threshold_value):
		try :
			if not isinstance(counter_threshold_value,str):
				raise TypeError("counter_threshold_value must be set to str value")
			self._counter_threshold_value = counter_threshold_value
		except Exception as e :
			raise e


	'''
	get Source
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e


	'''
	get Command Execution Status
	'''
	@property
	def cmd_exec_status(self) :
		try:
			return self._cmd_exec_status
		except Exception as e :
			raise e
	'''
	set Command Execution Status
	'''
	@cmd_exec_status.setter
	def cmd_exec_status(self,cmd_exec_status):
		try :
			if not isinstance(cmd_exec_status,str):
				raise TypeError("cmd_exec_status must be set to str value")
			self._cmd_exec_status = cmd_exec_status
		except Exception as e :
			raise e


	'''
	get Device Entity Type
	'''
	@property
	def device_entity_type(self) :
		try:
			return self._device_entity_type
		except Exception as e :
			raise e
	'''
	set Device Entity Type
	'''
	@device_entity_type.setter
	def device_entity_type(self,device_entity_type):
		try :
			if not isinstance(device_entity_type,str):
				raise TypeError("device_entity_type must be set to str value")
			self._device_entity_type = device_entity_type
		except Exception as e :
			raise e


	'''
	get Last Octet of SNMP Trap OID
	'''
	@property
	def trap_id(self) :
		try:
			return self._trap_id
		except Exception as e :
			raise e


	'''
	get Entity of Event
	'''
	@property
	def entity(self) :
		try:
			return self._entity
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
	get Event Time
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Operation Type
	'''
	@property
	def operation_type(self) :
		try:
			return self._operation_type
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
	get Category of Event
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e


	'''
	get Severity of Event
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e


	'''
	get Failure Object
	'''
	@property
	def failureobj(self) :
		try:
			return self._failureobj
		except Exception as e :
			raise e


	'''
	get Internal Event ID used in the source device.
	'''
	@property
	def source_event_id(self) :
		try:
			return self._source_event_id
		except Exception as e :
			raise e


	'''
	get previous status of event
	'''
	@property
	def event_history(self) :
		try:
			return self._event_history
		except Exception as e :
			raise e
	'''
	set previous status of event
	'''
	@event_history.setter
	def event_history(self,event_history) :
		try :
			if not isinstance(event_history,list):
				raise TypeError("event_history must be set to array of eventHistory value")
			for item in event_history :
				if not isinstance(item,eventHistory):
					raise TypeError("item must be set to eventHistory value")
			self._event_history = event_history
		except Exception as e :
			raise e


	'''
	get History of the Event with same entity
	'''
	@property
	def history(self) :
		try:
			return self._history
		except Exception as e :
			raise e


	'''
	get Device Family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family
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
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Event Message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e


	'''
	get Username
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set Username
	'''
	@user_name.setter
	def user_name(self,user_name):
		try :
			if not isinstance(user_name,str):
				raise TypeError("user_name must be set to str value")
			self._user_name = user_name
		except Exception as e :
			raise e


	'''
	get Device Entity Name
	'''
	@property
	def device_entity_name(self) :
		try:
			return self._device_entity_name
		except Exception as e :
			raise e
	'''
	set Device Entity Name
	'''
	@device_entity_name.setter
	def device_entity_name(self,device_entity_name):
		try :
			if not isinstance(device_entity_name,str):
				raise TypeError("device_entity_name must be set to str value")
			self._device_entity_name = device_entity_name
		except Exception as e :
			raise e


	'''
	get Config Command
	'''
	@property
	def config_cmd(self) :
		try:
			return self._config_cmd
		except Exception as e :
			raise e
	'''
	set Config Command
	'''
	@config_cmd.setter
	def config_cmd(self,config_cmd):
		try :
			if not isinstance(config_cmd,str):
				raise TypeError("config_cmd must be set to str value")
			self._config_cmd = config_cmd
		except Exception as e :
			raise e


	'''
	get Command Authorization Status
	'''
	@property
	def cmd_auth_status(self) :
		try:
			return self._cmd_auth_status
		except Exception as e :
			raise e
	'''
	set Command Authorization Status
	'''
	@cmd_auth_status.setter
	def cmd_auth_status(self,cmd_auth_status):
		try :
			if not isinstance(cmd_auth_status,str):
				raise TypeError("cmd_auth_status must be set to str value")
			self._cmd_auth_status = cmd_auth_status
		except Exception as e :
			raise e


	'''
	get device actual value for any threadhold violated traps
	'''
	@property
	def counter_actual_value(self) :
		try:
			return self._counter_actual_value
		except Exception as e :
			raise e
	'''
	set device actual value for any threadhold violated traps
	'''
	@counter_actual_value.setter
	def counter_actual_value(self,counter_actual_value):
		try :
			if not isinstance(counter_actual_value,str):
				raise TypeError("counter_actual_value must be set to str value")
			self._counter_actual_value = counter_actual_value
		except Exception as e :
			raise e

	'''
	Current Value, cab be used while sending traps
	'''
	@property
	def current_value(self):
		try:
			return self._current_value
		except Exception as e :
			raise e

	'''
	Threshold Value, cab be used while sending traps
	'''
	@property
	def threshold_value(self):
		try:
			return self._threshold_value
		except Exception as e :
			raise e

	'''
	Entity Type
	'''
	@property
	def entity_type(self):
		try:
			return self._entity_type
		except Exception as e :
			raise e

	'''
	Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def hostname(self):
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e

	'''
	Matched Event Filter Ids separated by comma
	'''
	@property
	def matched_filters(self):
		try:
			return self._matched_filters
		except Exception as e :
			raise e

	'''
	Managed Device ID
	'''
	@property
	def managed_device_id(self):
		try:
			return self._managed_device_id
		except Exception as e :
			raise e

	'''
	Use this operation to delete events.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					event_obj=event()
					return cls.delete_bulk_request(client,resource,event_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get events.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				event_obj=event()
				response = event_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of event resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			event_obj = event()
			option_ = options()
			option_._filter=filter_
			return event_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the event resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			event_obj = event()
			option_ = options()
			option_._count=True
			response = event_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of event resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			event_obj = event()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = event_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(event_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.event
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(event_responses, response, "event_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.event_response_array
				i=0
				error = [event() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.event_response_array
			i=0
			event_objs = [event() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_event'):
					for props in obj._event:
						result = service.payload_formatter.string_to_bulk_resource(event_response,self.__class__.__name__,props)
						event_objs[i] = result.event
						i=i+1
			return event_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(event,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class event_response(base_response):
	def __init__(self,length=1) :
		self.event= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.event= [ event() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class event_responses(base_response):
	def __init__(self,length=1) :
		self.event_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.event_response_array = [ event() for _ in range(length)]