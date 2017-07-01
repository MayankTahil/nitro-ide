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

from massrc.com.citrix.mas.nitro.resource.config.mps.sb_info import sb_info

'''
Configuration for Single Bundle File Info For Clean Install resource
'''

class clean_install_info(sb_info):
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
			return "clean_install_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(clean_install_info,self).get_object_id()
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
			return "clean_install_infos"
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(clean_install_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clean_install_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(clean_install_info_responses, response, "clean_install_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.clean_install_info_response_array
				i=0
				error = [clean_install_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.clean_install_info_response_array
			i=0
			clean_install_info_objs = [clean_install_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_clean_install_info'):
					for props in obj._clean_install_info:
						result = service.payload_formatter.string_to_bulk_resource(clean_install_info_response,self.__class__.__name__,props)
						clean_install_info_objs[i] = result.clean_install_info
						i=i+1
			return clean_install_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(clean_install_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class clean_install_info_response(base_response):
	def __init__(self,length=1) :
		self.clean_install_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.clean_install_info= [ clean_install_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class clean_install_info_responses(base_response):
	def __init__(self,length=1) :
		self.clean_install_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.clean_install_info_response_array = [ clean_install_info() for _ in range(length)]
