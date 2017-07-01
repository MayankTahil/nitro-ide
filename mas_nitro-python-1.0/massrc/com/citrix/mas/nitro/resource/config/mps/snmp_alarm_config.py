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
Configuration for SNMP Alarm Configurations resource
'''

class snmp_alarm_config(base_resource):
	_enable= ""
	_threshold= ""
	_clear_alarm_oid= ""
	_time= ""
	_name= ""
	_severity= ""
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
			return "snmp_alarm_config"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "snmp_alarm_configs"
		except Exception as e :
			raise e



	'''
	get Enable Alarm
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set Enable Alarm
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e


	'''
	get Threshold Value for the alarm
	'''
	@property
	def threshold(self) :
		try:
			return self._threshold
		except Exception as e :
			raise e
	'''
	set Threshold Value for the alarm
	'''
	@threshold.setter
	def threshold(self,threshold):
		try :
			if not isinstance(threshold,int):
				raise TypeError("threshold must be set to int value")
			self._threshold = threshold
		except Exception as e :
			raise e


	'''
	get Clear alarm Oid
	'''
	@property
	def clear_alarm_oid(self) :
		try:
			return self._clear_alarm_oid
		except Exception as e :
			raise e


	'''
	get Frequency of the alarm
	'''
	@property
	def time(self) :
		try:
			return self._time
		except Exception as e :
			raise e
	'''
	set Frequency of the alarm
	'''
	@time.setter
	def time(self,time):
		try :
			if not isinstance(time,int):
				raise TypeError("time must be set to int value")
			self._time = time
		except Exception as e :
			raise e


	'''
	get Alarm Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Alarm Name
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
	get Alarm severity. Supported values: Critical, Major, Minor, Warning, Informational 
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Alarm severity. Supported values: Critical, Major, Minor, Warning, Informational 
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
	Use this operation to get snmp alarm configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_alarm_config_obj=snmp_alarm_config()
				response = snmp_alarm_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp alarm configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_alarm_config_obj=snmp_alarm_config()
				return cls.update_bulk_request(client,resource,snmp_alarm_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_alarm_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_alarm_config_obj = snmp_alarm_config()
			option_ = options()
			option_._filter=filter_
			return snmp_alarm_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_alarm_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_alarm_config_obj = snmp_alarm_config()
			option_ = options()
			option_._count=True
			response = snmp_alarm_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_alarm_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_alarm_config_obj = snmp_alarm_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_alarm_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_alarm_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_alarm_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_alarm_config_responses, response, "snmp_alarm_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_alarm_config_response_array
				i=0
				error = [snmp_alarm_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_alarm_config_response_array
			i=0
			snmp_alarm_config_objs = [snmp_alarm_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_alarm_config'):
					for props in obj._snmp_alarm_config:
						result = service.payload_formatter.string_to_bulk_resource(snmp_alarm_config_response,self.__class__.__name__,props)
						snmp_alarm_config_objs[i] = result.snmp_alarm_config
						i=i+1
			return snmp_alarm_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_alarm_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_alarm_config_response(base_response):
	def __init__(self,length=1) :
		self.snmp_alarm_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_alarm_config= [ snmp_alarm_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_alarm_config_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_alarm_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_alarm_config_response_array = [ snmp_alarm_config() for _ in range(length)]
