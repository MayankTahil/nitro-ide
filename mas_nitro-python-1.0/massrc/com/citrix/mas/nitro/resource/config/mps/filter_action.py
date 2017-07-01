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
Configuration for event filter action properties resource
'''

class filter_action(base_resource):
	_parent_name= ""
	_type= ""
	_id= ""
	_suppress_time= ""
	_parent_id= ""
	_repeat_email_notification_threshold= ""
	_profile_name= ""
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
			return "filter_action"
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
			return "filter_actions"
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
	get Action Type e.g. SENDMAIL,SENDSMS
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Action Type e.g. SENDMAIL,SENDSMS
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get 
	'''
	@property
	def suppress_time(self) :
		try:
			return self._suppress_time
		except Exception as e :
			raise e
	'''
	set 
	'''
	@suppress_time.setter
	def suppress_time(self,suppress_time):
		try :
			if not isinstance(suppress_time,int):
				raise TypeError("suppress_time must be set to int value")
			self._suppress_time = suppress_time
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
	get RepeatEmailNotificationThreshold
	'''
	@property
	def repeat_email_notification_threshold(self) :
		try:
			return self._repeat_email_notification_threshold
		except Exception as e :
			raise e
	'''
	set RepeatEmailNotificationThreshold
	'''
	@repeat_email_notification_threshold.setter
	def repeat_email_notification_threshold(self,repeat_email_notification_threshold):
		try :
			if not isinstance(repeat_email_notification_threshold,int):
				raise TypeError("repeat_email_notification_threshold must be set to int value")
			self._repeat_email_notification_threshold = repeat_email_notification_threshold
		except Exception as e :
			raise e

	'''
	Mail or SMS profile name
	'''
	@property
	def profile_name(self):
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	Mail or SMS profile name
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_action_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filter_action
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(filter_action_responses, response, "filter_action_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.filter_action_response_array
				i=0
				error = [filter_action() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.filter_action_response_array
			i=0
			filter_action_objs = [filter_action() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_filter_action'):
					for props in obj._filter_action:
						result = service.payload_formatter.string_to_bulk_resource(filter_action_response,self.__class__.__name__,props)
						filter_action_objs[i] = result.filter_action
						i=i+1
			return filter_action_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(filter_action,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class filter_action_response(base_response):
	def __init__(self,length=1) :
		self.filter_action= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.filter_action= [ filter_action() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class filter_action_responses(base_response):
	def __init__(self,length=1) :
		self.filter_action_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.filter_action_response_array = [ filter_action() for _ in range(length)]
