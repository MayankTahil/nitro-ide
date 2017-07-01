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
Configuration for Single Bundle File Info resource
'''

class sb_info(base_resource):
	_component_info=[]
	_error_message= ""
	_file_name= ""
	_total_approx_time= ""
	_reboot_message= ""
	_selected_sb_version= ""
	_current_sb_version= ""
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
			return "sb_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "sb_infos"
		except Exception as e :
			raise e



	'''
	get Component Info
	'''
	@property
	def component_info(self) :
		try:
			return self._component_info
		except Exception as e :
			raise e


	'''
	get Error Message in case the Single Bundle cannot be applied
	'''
	@property
	def error_message(self) :
		try:
			return self._error_message
		except Exception as e :
			raise e


	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Total approximate time that the upgrade will take
	'''
	@property
	def total_approx_time(self) :
		try:
			return self._total_approx_time
		except Exception as e :
			raise e


	'''
	get Reboot Message
	'''
	@property
	def reboot_message(self) :
		try:
			return self._reboot_message
		except Exception as e :
			raise e


	'''
	get Selected Single Bundle Version
	'''
	@property
	def selected_sb_version(self) :
		try:
			return self._selected_sb_version
		except Exception as e :
			raise e


	'''
	get Current Single Bundle Version
	'''
	@property
	def current_sb_version(self) :
		try:
			return self._current_sb_version
		except Exception as e :
			raise e

	'''
	Use this operation to get build file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sb_info_obj=sb_info()
				response = sb_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sb_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sb_info_obj = sb_info()
			option_ = options()
			option_._filter=filter_
			return sb_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sb_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sb_info_obj = sb_info()
			option_ = options()
			option_._count=True
			response = sb_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sb_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sb_info_obj = sb_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sb_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sb_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sb_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sb_info_responses, response, "sb_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sb_info_response_array
				i=0
				error = [sb_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sb_info_response_array
			i=0
			sb_info_objs = [sb_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sb_info'):
					for props in obj._sb_info:
						result = service.payload_formatter.string_to_bulk_resource(sb_info_response,self.__class__.__name__,props)
						sb_info_objs[i] = result.sb_info
						i=i+1
			return sb_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sb_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sb_info_response(base_response):
	def __init__(self,length=1) :
		self.sb_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sb_info= [ sb_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sb_info_responses(base_response):
	def __init__(self,length=1) :
		self.sb_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sb_info_response_array = [ sb_info() for _ in range(length)]
