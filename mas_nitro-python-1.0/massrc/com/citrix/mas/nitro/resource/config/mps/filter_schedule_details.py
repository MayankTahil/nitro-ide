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
Configuration for Filter Schedule Details resource
'''

class filter_schedule_details(base_resource):
	_scheduleEndTimesEpoch= ""
	_scheduleStartTimesEpoch= ""
	_parent_name= ""
	_endRecurrenceTimes= ""
	_id= ""
	_startRecurrenceTimes= ""
	_parent_id= ""
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
			return "filter_schedule_details"
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
			return "filter_schedule_detailss"
		except Exception as e :
			raise e



	'''
	get Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def scheduleEndTimesEpoch(self) :
		try:
			return self._scheduleEndTimesEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch (string representation of 11 digit numbers).
	'''
	@scheduleEndTimesEpoch.setter
	def scheduleEndTimesEpoch(self,scheduleEndTimesEpoch):
		try :
			if not isinstance(scheduleEndTimesEpoch,str):
				raise TypeError("scheduleEndTimesEpoch must be set to str value")
			self._scheduleEndTimesEpoch = scheduleEndTimesEpoch
		except Exception as e :
			raise e


	'''
	get Schedule time epoch (string representation of 11 digit numbers).
	'''
	@property
	def scheduleStartTimesEpoch(self) :
		try:
			return self._scheduleStartTimesEpoch
		except Exception as e :
			raise e
	'''
	set Schedule time epoch (string representation of 11 digit numbers).
	'''
	@scheduleStartTimesEpoch.setter
	def scheduleStartTimesEpoch(self,scheduleStartTimesEpoch):
		try :
			if not isinstance(scheduleStartTimesEpoch,str):
				raise TypeError("scheduleStartTimesEpoch must be set to str value")
			self._scheduleStartTimesEpoch = scheduleStartTimesEpoch
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
	get Comma Seperated recurrence epoch times at which job is to be executed
	'''
	@property
	def endRecurrenceTimes(self) :
		try:
			return self._endRecurrenceTimes
		except Exception as e :
			raise e
	'''
	set Comma Seperated recurrence epoch times at which job is to be executed
	'''
	@endRecurrenceTimes.setter
	def endRecurrenceTimes(self,endRecurrenceTimes):
		try :
			if not isinstance(endRecurrenceTimes,str):
				raise TypeError("endRecurrenceTimes must be set to str value")
			self._endRecurrenceTimes = endRecurrenceTimes
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
	get Comma Seperated recurrence epoch times at which job is to be executed
	'''
	@property
	def startRecurrenceTimes(self) :
		try:
			return self._startRecurrenceTimes
		except Exception as e :
			raise e
	'''
	set Comma Seperated recurrence epoch times at which job is to be executed
	'''
	@startRecurrenceTimes.setter
	def startRecurrenceTimes(self,startRecurrenceTimes):
		try :
			if not isinstance(startRecurrenceTimes,str):
				raise TypeError("startRecurrenceTimes must be set to str value")
			self._startRecurrenceTimes = startRecurrenceTimes
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the events
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the events
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_schedule_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filter_schedule_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_schedule_details_responses, response, "filter_schedule_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.filter_schedule_details_response_array
				i=0
				error = [filter_schedule_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.filter_schedule_details_response_array
			i=0
			filter_schedule_details_objs = [filter_schedule_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_filter_schedule_details'):
					for props in obj._filter_schedule_details:
						result = service.payload_formatter.string_to_bulk_resource(filter_schedule_details_response,self.__class__.__name__,props)
						filter_schedule_details_objs[i] = result.filter_schedule_details
						i=i+1
			return filter_schedule_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(filter_schedule_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class filter_schedule_details_response(base_response):
	def __init__(self,length=1) :
		self.filter_schedule_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.filter_schedule_details= [ filter_schedule_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class filter_schedule_details_responses(base_response):
	def __init__(self,length=1) :
		self.filter_schedule_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.filter_schedule_details_response_array = [ filter_schedule_details() for _ in range(length)]
