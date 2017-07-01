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
Configuration for System Log Message resource
'''

class syslog_messages(base_resource):
	_source= ""
	_event_type= ""
	_system_gmt_time= ""
	_message= ""
	_app_name= ""
	_system_time= ""
	_id= ""
	_instance_ip= ""
	_severity= ""
	_module= ""
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
			return "syslog_messages"
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
			return "syslog_messagess"
		except Exception as e :
			raise e



	'''
	get Source IP Address
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e
	'''
	set Source IP Address
	'''
	@source.setter
	def source(self,source):
		try :
			if not isinstance(source,str):
				raise TypeError("source must be set to str value")
			self._source = source
		except Exception as e :
			raise e


	'''
	get Event type
	'''
	@property
	def event_type(self) :
		try:
			return self._event_type
		except Exception as e :
			raise e
	'''
	set Event type
	'''
	@event_type.setter
	def event_type(self,event_type):
		try :
			if not isinstance(event_type,str):
				raise TypeError("event_type must be set to str value")
			self._event_type = event_type
		except Exception as e :
			raise e


	'''
	get System Time in GMT timezone
	'''
	@property
	def system_gmt_time(self) :
		try:
			return self._system_gmt_time
		except Exception as e :
			raise e


	'''
	get Message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Message
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def app_name(self) :
		try:
			return self._app_name
		except Exception as e :
			raise e
	'''
	set Application Name
	'''
	@app_name.setter
	def app_name(self,app_name):
		try :
			if not isinstance(app_name,str):
				raise TypeError("app_name must be set to str value")
			self._app_name = app_name
		except Exception as e :
			raise e


	'''
	get System Time in local timezone
	'''
	@property
	def system_time(self) :
		try:
			return self._system_time
		except Exception as e :
			raise e
	'''
	set System Time in local timezone
	'''
	@system_time.setter
	def system_time(self,system_time):
		try :
			if not isinstance(system_time,str):
				raise TypeError("system_time must be set to str value")
			self._system_time = system_time
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system log entries
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system log entries
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
	get Instance IP Address
	'''
	@property
	def instance_ip(self) :
		try:
			return self._instance_ip
		except Exception as e :
			raise e
	'''
	set Instance IP Address
	'''
	@instance_ip.setter
	def instance_ip(self,instance_ip):
		try :
			if not isinstance(instance_ip,str):
				raise TypeError("instance_ip must be set to str value")
			self._instance_ip = instance_ip
		except Exception as e :
			raise e


	'''
	get Severity of the message
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity of the message
	'''
	@severity.setter
	def severity(self,severity):
		try :
			if not isinstance(severity,str):
				raise TypeError("severity must be set to str value")
			self._severity = severity
		except Exception as e :
			raise e


	'''
	get Module name
	'''
	@property
	def module(self) :
		try:
			return self._module
		except Exception as e :
			raise e
	'''
	set Module name
	'''
	@module.setter
	def module(self,module):
		try :
			if not isinstance(module,str):
				raise TypeError("module must be set to str value")
			self._module = module
		except Exception as e :
			raise e

	'''
	Use this operation to get system log messages.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				syslog_messages_obj=syslog_messages()
				response = syslog_messages_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_messages resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_messages_obj = syslog_messages()
			option_ = options()
			option_._filter=filter_
			return syslog_messages_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_messages resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_messages_obj = syslog_messages()
			option_ = options()
			option_._count=True
			response = syslog_messages_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_messages resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_messages_obj = syslog_messages()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_messages_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_messages_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_messages
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_messages_responses, response, "syslog_messages_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_messages_response_array
				i=0
				error = [syslog_messages() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_messages_response_array
			i=0
			syslog_messages_objs = [syslog_messages() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_messages'):
					for props in obj._syslog_messages:
						result = service.payload_formatter.string_to_bulk_resource(syslog_messages_response,self.__class__.__name__,props)
						syslog_messages_objs[i] = result.syslog_messages
						i=i+1
			return syslog_messages_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_messages,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_messages_response(base_response):
	def __init__(self,length=1) :
		self.syslog_messages= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_messages= [ syslog_messages() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_messages_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_messages_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_messages_response_array = [ syslog_messages() for _ in range(length)]
