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
Configuration for Syslog Purge Setting Details resource
'''

class syslog_purge_setting_details(base_resource):
	_syslog_detail_type_desc= ""
	_parent_name= ""
	_syslog_type= ""
	_syslog_module= ""
	_id= ""
	_syslog_detail_purge_interval= ""
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
			return "syslog_purge_setting_details"
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
			return "syslog_purge_setting_detailss"
		except Exception as e :
			raise e



	'''
	get syslog groups
	'''
	@property
	def syslog_detail_type_desc(self) :
		try:
			return self._syslog_detail_type_desc
		except Exception as e :
			raise e
	'''
	set syslog groups
	'''
	@syslog_detail_type_desc.setter
	def syslog_detail_type_desc(self,syslog_detail_type_desc):
		try :
			if not isinstance(syslog_detail_type_desc,str):
				raise TypeError("syslog_detail_type_desc must be set to str value")
			self._syslog_detail_type_desc = syslog_detail_type_desc
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
	get syslog groups
	'''
	@property
	def syslog_type(self) :
		try:
			return self._syslog_type
		except Exception as e :
			raise e
	'''
	set syslog groups
	'''
	@syslog_type.setter
	def syslog_type(self,syslog_type):
		try :
			if not isinstance(syslog_type,str):
				raise TypeError("syslog_type must be set to str value")
			self._syslog_type = syslog_type
		except Exception as e :
			raise e


	'''
	get syslog modulename
	'''
	@property
	def syslog_module(self) :
		try:
			return self._syslog_module
		except Exception as e :
			raise e
	'''
	set syslog modulename
	'''
	@syslog_module.setter
	def syslog_module(self,syslog_module):
		try :
			if not isinstance(syslog_module,str):
				raise TypeError("syslog_module must be set to str value")
			self._syslog_module = syslog_module
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
	get Purge interval for syslog groups.
	'''
	@property
	def syslog_detail_purge_interval(self) :
		try:
			return self._syslog_detail_purge_interval
		except Exception as e :
			raise e
	'''
	set Purge interval for syslog groups.
	'''
	@syslog_detail_purge_interval.setter
	def syslog_detail_purge_interval(self,syslog_detail_purge_interval):
		try :
			if not isinstance(syslog_detail_purge_interval,int):
				raise TypeError("syslog_detail_purge_interval must be set to int value")
			self._syslog_detail_purge_interval = syslog_detail_purge_interval
		except Exception as e :
			raise e


	'''
	get ID of syslog_purge_setting_details
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set ID of syslog_purge_setting_details
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
			result=service.payload_formatter.string_to_resource(syslog_purge_setting_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_purge_setting_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_purge_setting_details_responses, response, "syslog_purge_setting_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_purge_setting_details_response_array
				i=0
				error = [syslog_purge_setting_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_purge_setting_details_response_array
			i=0
			syslog_purge_setting_details_objs = [syslog_purge_setting_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_purge_setting_details'):
					for props in obj._syslog_purge_setting_details:
						result = service.payload_formatter.string_to_bulk_resource(syslog_purge_setting_details_response,self.__class__.__name__,props)
						syslog_purge_setting_details_objs[i] = result.syslog_purge_setting_details
						i=i+1
			return syslog_purge_setting_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_purge_setting_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_purge_setting_details_response(base_response):
	def __init__(self,length=1) :
		self.syslog_purge_setting_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_purge_setting_details= [ syslog_purge_setting_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_purge_setting_details_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_purge_setting_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_purge_setting_details_response_array = [ syslog_purge_setting_details() for _ in range(length)]
