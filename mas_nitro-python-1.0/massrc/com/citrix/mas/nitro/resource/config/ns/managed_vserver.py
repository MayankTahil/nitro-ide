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
Configuration for Managed Vserver Information resource
'''

class managed_vserver(base_resource):
	_managed= ""
	_type= ""
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
			return "managed_vserver"
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
			return "managed_vservers"
		except Exception as e :
			raise e



	'''
	get Managed
	'''
	@property
	def managed(self) :
		try:
			return self._managed
		except Exception as e :
			raise e
	'''
	set Managed
	'''
	@managed.setter
	def managed(self,managed):
		try :
			if not isinstance(managed,bool):
				raise TypeError("managed must be set to bool value")
			self._managed = managed
		except Exception as e :
			raise e


	'''
	get Vserver Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Vserver Type
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
	get Id of the Vserver
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id of the Vserver
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_vserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.managed_vserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_vserver_responses, response, "managed_vserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.managed_vserver_response_array
				i=0
				error = [managed_vserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.managed_vserver_response_array
			i=0
			managed_vserver_objs = [managed_vserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_managed_vserver'):
					for props in obj._managed_vserver:
						result = service.payload_formatter.string_to_bulk_resource(managed_vserver_response,self.__class__.__name__,props)
						managed_vserver_objs[i] = result.managed_vserver
						i=i+1
			return managed_vserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(managed_vserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class managed_vserver_response(base_response):
	def __init__(self,length=1) :
		self.managed_vserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.managed_vserver= [ managed_vserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class managed_vserver_responses(base_response):
	def __init__(self,length=1) :
		self.managed_vserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.managed_vserver_response_array = [ managed_vserver() for _ in range(length)]
