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
Configuration for backup components resource
'''

class backup_component(base_resource):
	_component_message= ""
	_component_minimum_version= ""
	_component_name= ""
	_component= ""
	_backup_file_name= ""
	_component_versions= ""
	_component_ip= ""
	_component_error_severity= ""
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
			return "backup_component"
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
			return "backup_components"
		except Exception as e :
			raise e



	'''
	get Information about the componenet
	'''
	@property
	def component_message(self) :
		try:
			return self._component_message
		except Exception as e :
			raise e
	'''
	set Information about the componenet
	'''
	@component_message.setter
	def component_message(self,component_message):
		try :
			if not isinstance(component_message,str):
				raise TypeError("component_message must be set to str value")
			self._component_message = component_message
		except Exception as e :
			raise e


	'''
	get Minimum version supported by the NetScaler
	'''
	@property
	def component_minimum_version(self) :
		try:
			return self._component_minimum_version
		except Exception as e :
			raise e
	'''
	set Minimum version supported by the NetScaler
	'''
	@component_minimum_version.setter
	def component_minimum_version(self,component_minimum_version):
		try :
			if not isinstance(component_minimum_version,str):
				raise TypeError("component_minimum_version must be set to str value")
			self._component_minimum_version = component_minimum_version
		except Exception as e :
			raise e


	'''
	get Backup component Name
	'''
	@property
	def component_name(self) :
		try:
			return self._component_name
		except Exception as e :
			raise e
	'''
	set Backup component Name
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
	get Backup component
	'''
	@property
	def component(self) :
		try:
			return self._component
		except Exception as e :
			raise e
	'''
	set Backup component
	'''
	@component.setter
	def component(self,component):
		try :
			if not isinstance(component,str):
				raise TypeError("component must be set to str value")
			self._component = component
		except Exception as e :
			raise e


	'''
	get Backup file name
	'''
	@property
	def backup_file_name(self) :
		try:
			return self._backup_file_name
		except Exception as e :
			raise e
	'''
	set Backup file name
	'''
	@backup_file_name.setter
	def backup_file_name(self,backup_file_name):
		try :
			if not isinstance(backup_file_name,str):
				raise TypeError("backup_file_name must be set to str value")
			self._backup_file_name = backup_file_name
		except Exception as e :
			raise e


	'''
	get Backup component version
	'''
	@property
	def component_versions(self) :
		try:
			return self._component_versions
		except Exception as e :
			raise e
	'''
	set Backup component version
	'''
	@component_versions.setter
	def component_versions(self,component_versions):
		try :
			if not isinstance(component_versions,str):
				raise TypeError("component_versions must be set to str value")
			self._component_versions = component_versions
		except Exception as e :
			raise e


	'''
	get Backup component IPaddress
	'''
	@property
	def component_ip(self) :
		try:
			return self._component_ip
		except Exception as e :
			raise e
	'''
	set Backup component IPaddress
	'''
	@component_ip.setter
	def component_ip(self,component_ip):
		try :
			if not isinstance(component_ip,str):
				raise TypeError("component_ip must be set to str value")
			self._component_ip = component_ip
		except Exception as e :
			raise e


	'''
	get Severity of error for the component
	'''
	@property
	def component_error_severity(self) :
		try:
			return self._component_error_severity
		except Exception as e :
			raise e
	'''
	set Severity of error for the component
	'''
	@component_error_severity.setter
	def component_error_severity(self,component_error_severity):
		try :
			if not isinstance(component_error_severity,int):
				raise TypeError("component_error_severity must be set to int value")
			self._component_error_severity = component_error_severity
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(backup_component_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.backup_component
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(backup_component_responses, response, "backup_component_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.backup_component_response_array
				i=0
				error = [backup_component() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.backup_component_response_array
			i=0
			backup_component_objs = [backup_component() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_backup_component'):
					for props in obj._backup_component:
						result = service.payload_formatter.string_to_bulk_resource(backup_component_response,self.__class__.__name__,props)
						backup_component_objs[i] = result.backup_component
						i=i+1
			return backup_component_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(backup_component,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class backup_component_response(base_response):
	def __init__(self,length=1) :
		self.backup_component= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.backup_component= [ backup_component() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class backup_component_responses(base_response):
	def __init__(self,length=1) :
		self.backup_component_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.backup_component_response_array = [ backup_component() for _ in range(length)]
