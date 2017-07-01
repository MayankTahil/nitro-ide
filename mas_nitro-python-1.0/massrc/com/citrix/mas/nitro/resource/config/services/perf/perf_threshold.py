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
Configuration for PerfThreshold resource
'''

class perf_threshold(base_resource):
	_sms_profile= ""
	_clear_message= ""
	_threshold_type= ""
	_clear_event= ""
	_id= ""
	_report_name= ""
	_severity= ""
	_mail_profile= ""
	_tenant_name= ""
	_is_enabled= ""
	_device_family= ""
	_instances= ""
	_threshold_value= ""
	_name= ""
	_duration= ""
	_counter_name= ""
	_devices= ""
	_message= ""
	_clear_value= ""
	_devices_array=[]
	_instances_array=[]
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
			return "perf_threshold"
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
			return "perf_thresholds"
		except Exception as e :
			raise e



	'''
	get SMS Profile
	'''
	@property
	def sms_profile(self) :
		try:
			return self._sms_profile
		except Exception as e :
			raise e
	'''
	set SMS Profile
	'''
	@sms_profile.setter
	def sms_profile(self,sms_profile):
		try :
			if not isinstance(sms_profile,str):
				raise TypeError("sms_profile must be set to str value")
			self._sms_profile = sms_profile
		except Exception as e :
			raise e


	'''
	get Clear Message
	'''
	@property
	def clear_message(self) :
		try:
			return self._clear_message
		except Exception as e :
			raise e
	'''
	set Clear Message
	'''
	@clear_message.setter
	def clear_message(self,clear_message):
		try :
			if not isinstance(clear_message,str):
				raise TypeError("clear_message must be set to str value")
			self._clear_message = clear_message
		except Exception as e :
			raise e


	'''
	get Threshold Type
	'''
	@property
	def threshold_type(self) :
		try:
			return self._threshold_type
		except Exception as e :
			raise e
	'''
	set Threshold Type
	'''
	@threshold_type.setter
	def threshold_type(self,threshold_type):
		try :
			if not isinstance(threshold_type,str):
				raise TypeError("threshold_type must be set to str value")
			self._threshold_type = threshold_type
		except Exception as e :
			raise e


	'''
	get set to true if the event needs to be cleared
	'''
	@property
	def clear_event(self) :
		try:
			return self._clear_event
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the perf thresholds configuration 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the perf thresholds configuration 
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
	get Report Name for which the threshold is configured
	'''
	@property
	def report_name(self) :
		try:
			return self._report_name
		except Exception as e :
			raise e
	'''
	set Report Name for which the threshold is configured
	'''
	@report_name.setter
	def report_name(self,report_name):
		try :
			if not isinstance(report_name,str):
				raise TypeError("report_name must be set to str value")
			self._report_name = report_name
		except Exception as e :
			raise e


	'''
	get Severity
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e
	'''
	set Severity
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
	get Mail Profile
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail Profile
	'''
	@mail_profile.setter
	def mail_profile(self,mail_profile):
		try :
			if not isinstance(mail_profile,str):
				raise TypeError("mail_profile must be set to str value")
			self._mail_profile = mail_profile
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
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
	get Device Family of which this threshold belongs to
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family of which this threshold belongs to
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
	get counter instances
	'''
	@property
	def instances(self) :
		try:
			return self._instances
		except Exception as e :
			raise e
	'''
	set counter instances
	'''
	@instances.setter
	def instances(self,instances):
		try :
			if not isinstance(instances,str):
				raise TypeError("instances must be set to str value")
			self._instances = instances
		except Exception as e :
			raise e


	'''
	get Threshold Value
	'''
	@property
	def threshold_value(self) :
		try:
			return self._threshold_value
		except Exception as e :
			raise e
	'''
	set Threshold Value
	'''
	@threshold_value.setter
	def threshold_value(self,threshold_value):
		try :
			if not isinstance(threshold_value,float):
				raise TypeError("threshold_value must be set to float value")
			self._threshold_value = threshold_value
		except Exception as e :
			raise e


	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get duration of metric to be checked against threshold
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set duration of metric to be checked against threshold
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Counter Name for which the threshold is configured
	'''
	@property
	def counter_name(self) :
		try:
			return self._counter_name
		except Exception as e :
			raise e
	'''
	set Counter Name for which the threshold is configured
	'''
	@counter_name.setter
	def counter_name(self,counter_name):
		try :
			if not isinstance(counter_name,str):
				raise TypeError("counter_name must be set to str value")
			self._counter_name = counter_name
		except Exception as e :
			raise e


	'''
	get On which devices the threshold is enabled
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set On which devices the threshold is enabled
	'''
	@devices.setter
	def devices(self,devices):
		try :
			if not isinstance(devices,str):
				raise TypeError("devices must be set to str value")
			self._devices = devices
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
	get Clear Value
	'''
	@property
	def clear_value(self) :
		try:
			return self._clear_value
		except Exception as e :
			raise e
	'''
	set Clear Value
	'''
	@clear_value.setter
	def clear_value(self,clear_value):
		try :
			if not isinstance(clear_value,float):
				raise TypeError("clear_value must be set to float value")
			self._clear_value = clear_value
		except Exception as e :
			raise e

	'''
	Devices list
	'''
	@property
	def devices_array(self) :
		try:
			return self._devices_array
		except Exception as e :
			raise e
	'''
	Devices list
	'''
	@devices_array.setter
	def devices_array(self,devices_array) :
		try :
			if not isinstance(devices_array,list):
				raise TypeError("devices_array must be set to array of str value")
			for item in devices_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices_array = devices_array
		except Exception as e :
			raise e

	'''
	Instances list
	'''
	@property
	def instances_array(self) :
		try:
			return self._instances_array
		except Exception as e :
			raise e
	'''
	Instances list
	'''
	@instances_array.setter
	def instances_array(self,instances_array) :
		try :
			if not isinstance(instances_array,list):
				raise TypeError("instances_array must be set to array of str value")
			for item in instances_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._instances_array = instances_array
		except Exception as e :
			raise e

	'''
	add perf threshold configuration.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				perf_threshold_obj= perf_threshold()
				return cls.perform_operation_bulk_request(service,"add", resource,perf_threshold_obj)
		except Exception as e :
			raise e

	'''
	Delete perf threshold configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					perf_threshold_obj=perf_threshold()
					return cls.delete_bulk_request(client,resource,perf_threshold_obj)
		except Exception as e :
			raise e

	'''
	get perf threshold configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_threshold_obj=perf_threshold()
				response = perf_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify perf threshold configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				perf_threshold_obj=perf_threshold()
				return cls.update_bulk_request(client,resource,perf_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_threshold_obj = perf_threshold()
			option_ = options()
			option_._filter=filter_
			return perf_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_threshold_obj = perf_threshold()
			option_ = options()
			option_._count=True
			response = perf_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_threshold_obj = perf_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_threshold_responses, response, "perf_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_threshold_response_array
				i=0
				error = [perf_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_threshold_response_array
			i=0
			perf_threshold_objs = [perf_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_threshold'):
					for props in obj._perf_threshold:
						result = service.payload_formatter.string_to_bulk_resource(perf_threshold_response,self.__class__.__name__,props)
						perf_threshold_objs[i] = result.perf_threshold
						i=i+1
			return perf_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_threshold_response(base_response):
	def __init__(self,length=1) :
		self.perf_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_threshold= [ perf_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.perf_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_threshold_response_array = [ perf_threshold() for _ in range(length)]
