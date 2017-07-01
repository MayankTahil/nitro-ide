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
Configuration for Notification Digest Settings resource
'''

class notification_digest_settings(base_resource):
	_WeeklyFeaturesList= ""
	_scheduleTimesEpoch= ""
	_tz_offset= ""
	_scheduleOptions= ""
	_ImmediateFeaturesList= ""
	_MonthlyFeaturesList= ""
	_tenant_id= ""
	_nextScheduleTimeEpoch= ""
	_id= ""
	_DailyFeaturesList= ""
	_notification_period= ""
	_mail_profile= ""
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
			return "notification_digest_settings"
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
			return "notification_digest_settingss"
		except Exception as e :
			raise e



	'''
	get List of events for which notification is to be generated weekly.
	'''
	@property
	def WeeklyFeaturesList(self) :
		try:
			return self._WeeklyFeaturesList
		except Exception as e :
			raise e
	'''
	set List of events for which notification is to be generated weekly.
	'''
	@WeeklyFeaturesList.setter
	def WeeklyFeaturesList(self,WeeklyFeaturesList):
		try :
			if not isinstance(WeeklyFeaturesList,str):
				raise TypeError("WeeklyFeaturesList must be set to str value")
			self._WeeklyFeaturesList = WeeklyFeaturesList
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
	get List of events for which notification is to be generated immediately.
	'''
	@property
	def ImmediateFeaturesList(self) :
		try:
			return self._ImmediateFeaturesList
		except Exception as e :
			raise e
	'''
	set List of events for which notification is to be generated immediately.
	'''
	@ImmediateFeaturesList.setter
	def ImmediateFeaturesList(self,ImmediateFeaturesList):
		try :
			if not isinstance(ImmediateFeaturesList,str):
				raise TypeError("ImmediateFeaturesList must be set to str value")
			self._ImmediateFeaturesList = ImmediateFeaturesList
		except Exception as e :
			raise e


	'''
	get List of events for which notification is to be generated monthly.
	'''
	@property
	def MonthlyFeaturesList(self) :
		try:
			return self._MonthlyFeaturesList
		except Exception as e :
			raise e
	'''
	set List of events for which notification is to be generated monthly.
	'''
	@MonthlyFeaturesList.setter
	def MonthlyFeaturesList(self,MonthlyFeaturesList):
		try :
			if not isinstance(MonthlyFeaturesList,str):
				raise TypeError("MonthlyFeaturesList must be set to str value")
			self._MonthlyFeaturesList = MonthlyFeaturesList
		except Exception as e :
			raise e


	'''
	get Tenant Id of the Notification Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
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
	get Id is system generated for each setting
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated for each setting
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
	get List of events for which notification is to be generated daily.
	'''
	@property
	def DailyFeaturesList(self) :
		try:
			return self._DailyFeaturesList
		except Exception as e :
			raise e
	'''
	set List of events for which notification is to be generated daily.
	'''
	@DailyFeaturesList.setter
	def DailyFeaturesList(self,DailyFeaturesList):
		try :
			if not isinstance(DailyFeaturesList,str):
				raise TypeError("DailyFeaturesList must be set to str value")
			self._DailyFeaturesList = DailyFeaturesList
		except Exception as e :
			raise e


	'''
	get notification_period
	'''
	@property
	def notification_period(self) :
		try:
			return self._notification_period
		except Exception as e :
			raise e
	'''
	set notification_period
	'''
	@notification_period.setter
	def notification_period(self,notification_period):
		try :
			if not isinstance(notification_period,str):
				raise TypeError("notification_period must be set to str value")
			self._notification_period = notification_period
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
	Use this operation to add system user.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				notification_digest_settings_obj= notification_digest_settings()
				return cls.perform_operation_bulk_request(service,"add", resource,notification_digest_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete system user(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					notification_digest_settings_obj=notification_digest_settings()
					return cls.delete_bulk_request(client,resource,notification_digest_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get system users.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				notification_digest_settings_obj=notification_digest_settings()
				response = notification_digest_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system user.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				notification_digest_settings_obj=notification_digest_settings()
				return cls.update_bulk_request(client,resource,notification_digest_settings_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of notification_digest_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			notification_digest_settings_obj = notification_digest_settings()
			option_ = options()
			option_._filter=filter_
			return notification_digest_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the notification_digest_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			notification_digest_settings_obj = notification_digest_settings()
			option_ = options()
			option_._count=True
			response = notification_digest_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of notification_digest_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			notification_digest_settings_obj = notification_digest_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = notification_digest_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(notification_digest_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.notification_digest_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(notification_digest_settings_responses, response, "notification_digest_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.notification_digest_settings_response_array
				i=0
				error = [notification_digest_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.notification_digest_settings_response_array
			i=0
			notification_digest_settings_objs = [notification_digest_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_notification_digest_settings'):
					for props in obj._notification_digest_settings:
						result = service.payload_formatter.string_to_bulk_resource(notification_digest_settings_response,self.__class__.__name__,props)
						notification_digest_settings_objs[i] = result.notification_digest_settings
						i=i+1
			return notification_digest_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(notification_digest_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class notification_digest_settings_response(base_response):
	def __init__(self,length=1) :
		self.notification_digest_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.notification_digest_settings= [ notification_digest_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class notification_digest_settings_responses(base_response):
	def __init__(self,length=1) :
		self.notification_digest_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.notification_digest_settings_response_array = [ notification_digest_settings() for _ in range(length)]
