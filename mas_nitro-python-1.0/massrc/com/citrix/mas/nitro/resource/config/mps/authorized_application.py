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
Configuration for Authorized applications resource
'''

class authorized_application(base_resource):
	_application_name= ""
	_authorized_scope_id= ""
	_id= ""
	_application_id= ""
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
			return "authorized_application"
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
			return "authorized_applications"
		except Exception as e :
			raise e



	'''
	get Application Name
	'''
	@property
	def application_name(self) :
		try:
			return self._application_name
		except Exception as e :
			raise e
	'''
	set Application Name
	'''
	@application_name.setter
	def application_name(self,application_name):
		try :
			if not isinstance(application_name,str):
				raise TypeError("application_name must be set to str value")
			self._application_name = application_name
		except Exception as e :
			raise e


	'''
	get authorized_scope ID
	'''
	@property
	def authorized_scope_id(self) :
		try:
			return self._authorized_scope_id
		except Exception as e :
			raise e
	'''
	set authorized_scope ID
	'''
	@authorized_scope_id.setter
	def authorized_scope_id(self,authorized_scope_id):
		try :
			if not isinstance(authorized_scope_id,str):
				raise TypeError("authorized_scope_id must be set to str value")
			self._authorized_scope_id = authorized_scope_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	get ID of the application
	'''
	@property
	def application_id(self) :
		try:
			return self._application_id
		except Exception as e :
			raise e
	'''
	set ID of the application
	'''
	@application_id.setter
	def application_id(self,application_id):
		try :
			if not isinstance(application_id,str):
				raise TypeError("application_id must be set to str value")
			self._application_id = application_id
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(authorized_application_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authorized_application
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(authorized_application_responses, response, "authorized_application_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.authorized_application_response_array
				i=0
				error = [authorized_application() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.authorized_application_response_array
			i=0
			authorized_application_objs = [authorized_application() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_authorized_application'):
					for props in obj._authorized_application:
						result = service.payload_formatter.string_to_bulk_resource(authorized_application_response,self.__class__.__name__,props)
						authorized_application_objs[i] = result.authorized_application
						i=i+1
			return authorized_application_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(authorized_application,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class authorized_application_response(base_response):
	def __init__(self,length=1) :
		self.authorized_application= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.authorized_application= [ authorized_application() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class authorized_application_responses(base_response):
	def __init__(self,length=1) :
		self.authorized_application_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.authorized_application_response_array = [ authorized_application() for _ in range(length)]
