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
Configuration for Trigger Detail resource
'''

class trigger_detail(base_resource):
	_expiry= ""
	_parent_name= ""
	_daily_time= ""
	_trigger_type= ""
	_recur_hr= ""
	_duration= ""
	_description= ""
	_parent_id= ""
	_monthday_time= ""
	_id= ""
	_weekday_time= ""
	_recur_min= ""
	_start= ""
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
			return "trigger_detail"
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
			return "trigger_details"
		except Exception as e :
			raise e



	'''
	get Time at which the trigger should end.Format:YY:MM:DD:HH:MM.Applicable for trigger of type fixed
	'''
	@property
	def expiry(self) :
		try:
			return self._expiry
		except Exception as e :
			raise e
	'''
	set Time at which the trigger should end.Format:YY:MM:DD:HH:MM.Applicable for trigger of type fixed
	'''
	@expiry.setter
	def expiry(self,expiry):
		try :
			if not isinstance(expiry,str):
				raise TypeError("expiry must be set to str value")
			self._expiry = expiry
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Time of the day.Format is HH:MM where HH is hours and MM is minutes.Applicable for trigger of type daily
	'''
	@property
	def daily_time(self) :
		try:
			return self._daily_time
		except Exception as e :
			raise e
	'''
	set Time of the day.Format is HH:MM where HH is hours and MM is minutes.Applicable for trigger of type daily
	'''
	@daily_time.setter
	def daily_time(self,daily_time):
		try :
			if not isinstance(daily_time,str):
				raise TypeError("daily_time must be set to str value")
			self._daily_time = daily_time
		except Exception as e :
			raise e


	'''
	get Trigger type.Possible values: fixed,daily,weekly,monthly
	'''
	@property
	def trigger_type(self) :
		try:
			return self._trigger_type
		except Exception as e :
			raise e
	'''
	set Trigger type.Possible values: fixed,daily,weekly,monthly
	'''
	@trigger_type.setter
	def trigger_type(self,trigger_type):
		try :
			if not isinstance(trigger_type,str):
				raise TypeError("trigger_type must be set to str value")
			self._trigger_type = trigger_type
		except Exception as e :
			raise e


	'''
	get Recur interval in hours. Applicable for trigger of type fixed
	'''
	@property
	def recur_hr(self) :
		try:
			return self._recur_hr
		except Exception as e :
			raise e
	'''
	set Recur interval in hours. Applicable for trigger of type fixed
	'''
	@recur_hr.setter
	def recur_hr(self,recur_hr):
		try :
			if not isinstance(recur_hr,str):
				raise TypeError("recur_hr must be set to str value")
			self._recur_hr = recur_hr
		except Exception as e :
			raise e


	'''
	get Duration in days for which the trigger should last. Applicable for trigger of type fixed
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Duration in days for which the trigger should last. Applicable for trigger of type fixed
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
	get Trigger description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Trigger description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Days of the month.Format is DD:HH:MM where DD is either 1-31 or "last" for days of the month,HH is hours and MM is minutes.Applicable for trigger of type monthly.
	'''
	@property
	def monthday_time(self) :
		try:
			return self._monthday_time
		except Exception as e :
			raise e
	'''
	set Days of the month.Format is DD:HH:MM where DD is either 1-31 or "last" for days of the month,HH is hours and MM is minutes.Applicable for trigger of type monthly.
	'''
	@monthday_time.setter
	def monthday_time(self,monthday_time):
		try :
			if not isinstance(monthday_time,str):
				raise TypeError("monthday_time must be set to str value")
			self._monthday_time = monthday_time
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get Days of the week.Format is Day:HH:MM where Day is 0-6 for sunday-saturday,HH is hours and MM is minutes.Applicable for trigger of type weekly
	'''
	@property
	def weekday_time(self) :
		try:
			return self._weekday_time
		except Exception as e :
			raise e
	'''
	set Days of the week.Format is Day:HH:MM where Day is 0-6 for sunday-saturday,HH is hours and MM is minutes.Applicable for trigger of type weekly
	'''
	@weekday_time.setter
	def weekday_time(self,weekday_time):
		try :
			if not isinstance(weekday_time,str):
				raise TypeError("weekday_time must be set to str value")
			self._weekday_time = weekday_time
		except Exception as e :
			raise e


	'''
	get Recur interval in minutes. Applicable for trigger of type fixed
	'''
	@property
	def recur_min(self) :
		try:
			return self._recur_min
		except Exception as e :
			raise e
	'''
	set Recur interval in minutes. Applicable for trigger of type fixed
	'''
	@recur_min.setter
	def recur_min(self,recur_min):
		try :
			if not isinstance(recur_min,str):
				raise TypeError("recur_min must be set to str value")
			self._recur_min = recur_min
		except Exception as e :
			raise e


	'''
	get Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@property
	def start(self) :
		try:
			return self._start
		except Exception as e :
			raise e
	'''
	set Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@start.setter
	def start(self,start):
		try :
			if not isinstance(start,str):
				raise TypeError("start must be set to str value")
			self._start = start
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(trigger_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.trigger_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(trigger_detail_responses, response, "trigger_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.trigger_detail_response_array
				i=0
				error = [trigger_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.trigger_detail_response_array
			i=0
			trigger_detail_objs = [trigger_detail() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_trigger_detail'):
					for props in obj._trigger_detail:
						result = service.payload_formatter.string_to_bulk_resource(trigger_detail_response,self.__class__.__name__,props)
						trigger_detail_objs[i] = result.trigger_detail
						i=i+1
			return trigger_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(trigger_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class trigger_detail_response(base_response):
	def __init__(self,length=1) :
		self.trigger_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.trigger_detail= [ trigger_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class trigger_detail_responses(base_response):
	def __init__(self,length=1) :
		self.trigger_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.trigger_detail_response_array = [ trigger_detail() for _ in range(length)]
