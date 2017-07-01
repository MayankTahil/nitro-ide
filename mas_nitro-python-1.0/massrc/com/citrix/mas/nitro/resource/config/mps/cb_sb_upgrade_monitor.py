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
Configuration for CBSDX Single Bundle Upgrade Status resource
'''

class cb_sb_upgrade_monitor(base_resource):
	_time_remaining= ""
	_component_name= ""
	_reboot_required= ""
	_status_message= ""
	_error_code= ""
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
			return "cb_sb_upgrade_monitor"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._component_name
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
			return "cb_sb_upgrade_monitors"
		except Exception as e :
			raise e



	'''
	get Remaining Time
	'''
	@property
	def time_remaining(self) :
		try:
			return self._time_remaining
		except Exception as e :
			raise e


	'''
	get Component Name
	'''
	@property
	def component_name(self) :
		try:
			return self._component_name
		except Exception as e :
			raise e
	'''
	set Component Name
	'''
	@component_name.setter
	def component_name(self,component_name):
		try :
			if not isinstance(component_name,str):
				raise TypeError("component_name must be set to str value")
			self._component_name = component_name
		except Exception as e :
			raise e


	'''
	get Reboot Required
	'''
	@property
	def reboot_required(self) :
		try:
			return self._reboot_required
		except Exception as e :
			raise e


	'''
	get Upgrade Status Message
	'''
	@property
	def status_message(self) :
		try:
			return self._status_message
		except Exception as e :
			raise e


	'''
	get Error Code
	'''
	@property
	def error_code(self) :
		try:
			return self._error_code
		except Exception as e :
			raise e

	'''
	Use this operation to get single bundle upgrade status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cb_sb_upgrade_monitor_obj=cb_sb_upgrade_monitor()
				response = cb_sb_upgrade_monitor_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cb_sb_upgrade_monitor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cb_sb_upgrade_monitor_obj = cb_sb_upgrade_monitor()
			option_ = options()
			option_._filter=filter_
			return cb_sb_upgrade_monitor_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cb_sb_upgrade_monitor resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cb_sb_upgrade_monitor_obj = cb_sb_upgrade_monitor()
			option_ = options()
			option_._count=True
			response = cb_sb_upgrade_monitor_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cb_sb_upgrade_monitor resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cb_sb_upgrade_monitor_obj = cb_sb_upgrade_monitor()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cb_sb_upgrade_monitor_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cb_sb_upgrade_monitor_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cb_sb_upgrade_monitor
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cb_sb_upgrade_monitor_responses, response, "cb_sb_upgrade_monitor_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cb_sb_upgrade_monitor_response_array
				i=0
				error = [cb_sb_upgrade_monitor() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cb_sb_upgrade_monitor_response_array
			i=0
			cb_sb_upgrade_monitor_objs = [cb_sb_upgrade_monitor() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cb_sb_upgrade_monitor'):
					for props in obj._cb_sb_upgrade_monitor:
						result = service.payload_formatter.string_to_bulk_resource(cb_sb_upgrade_monitor_response,self.__class__.__name__,props)
						cb_sb_upgrade_monitor_objs[i] = result.cb_sb_upgrade_monitor
						i=i+1
			return cb_sb_upgrade_monitor_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cb_sb_upgrade_monitor,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cb_sb_upgrade_monitor_response(base_response):
	def __init__(self,length=1) :
		self.cb_sb_upgrade_monitor= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cb_sb_upgrade_monitor= [ cb_sb_upgrade_monitor() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cb_sb_upgrade_monitor_responses(base_response):
	def __init__(self,length=1) :
		self.cb_sb_upgrade_monitor_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cb_sb_upgrade_monitor_response_array = [ cb_sb_upgrade_monitor() for _ in range(length)]
