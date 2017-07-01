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
Configuration for Activity Status resource
'''

class activity_status(base_resource):
	_status= ""
	_reboot_now= ""
	_activity= ""
	_message= ""
	_act_id= ""
	_is_last= ""
	_starttime= ""
	_id= ""
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
			return "activity_status"
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
			return "activity_statuss"
		except Exception as e :
			raise e



	'''
	get Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get if true then the system is about to reboot
	'''
	@property
	def reboot_now(self) :
		try:
			return self._reboot_now
		except Exception as e :
			raise e


	'''
	get Activity
	'''
	@property
	def activity(self) :
		try:
			return self._activity
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
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get is_last
	'''
	@property
	def is_last(self) :
		try:
			return self._is_last
		except Exception as e :
			raise e


	'''
	get Start Time
	'''
	@property
	def starttime(self) :
		try:
			return self._starttime
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the task logs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the task logs
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
	Use this operation to get activity status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				activity_status_obj=activity_status()
				response = activity_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of activity_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			activity_status_obj = activity_status()
			option_ = options()
			option_._filter=filter_
			return activity_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the activity_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			activity_status_obj = activity_status()
			option_ = options()
			option_._count=True
			response = activity_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of activity_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			activity_status_obj = activity_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = activity_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(activity_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.activity_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(activity_status_responses, response, "activity_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.activity_status_response_array
				i=0
				error = [activity_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.activity_status_response_array
			i=0
			activity_status_objs = [activity_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_activity_status'):
					for props in obj._activity_status:
						result = service.payload_formatter.string_to_bulk_resource(activity_status_response,self.__class__.__name__,props)
						activity_status_objs[i] = result.activity_status
						i=i+1
			return activity_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(activity_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class activity_status_response(base_response):
	def __init__(self,length=1) :
		self.activity_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.activity_status= [ activity_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class activity_status_responses(base_response):
	def __init__(self,length=1) :
		self.activity_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.activity_status_response_array = [ activity_status() for _ in range(length)]
