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
Configuration for License User Information resource
'''

class license_user_detail(base_resource):
	_no_of_license= ""
	_parent_name= ""
	_time= ""
	_name= ""
	_id= ""
	_node= ""
	_display= ""
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
			return "license_user_detail"
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
			return "license_user_details"
		except Exception as e :
			raise e



	'''
	get No of licenses
	'''
	@property
	def no_of_license(self) :
		try:
			return self._no_of_license
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
	get Time
	'''
	@property
	def time(self) :
		try:
			return self._time
		except Exception as e :
			raise e


	'''
	get Name
	'''
	@property
	def name(self) :
		try:
			return self._name
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
	get Node
	'''
	@property
	def node(self) :
		try:
			return self._node
		except Exception as e :
			raise e


	'''
	get display
	'''
	@property
	def display(self) :
		try:
			return self._display
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_user_detail_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_user_detail
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_user_detail_responses, response, "license_user_detail_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_user_detail_response_array
				i=0
				error = [license_user_detail() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_user_detail_response_array
			i=0
			license_user_detail_objs = [license_user_detail() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_user_detail'):
					for props in obj._license_user_detail:
						result = service.payload_formatter.string_to_bulk_resource(license_user_detail_response,self.__class__.__name__,props)
						license_user_detail_objs[i] = result.license_user_detail
						i=i+1
			return license_user_detail_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_user_detail,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_user_detail_response(base_response):
	def __init__(self,length=1) :
		self.license_user_detail= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_user_detail= [ license_user_detail() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_user_detail_responses(base_response):
	def __init__(self,length=1) :
		self.license_user_detail_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_user_detail_response_array = [ license_user_detail() for _ in range(length)]
