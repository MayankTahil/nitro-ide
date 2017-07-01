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
from massrc.com.citrix.mas.nitro.resource.config.ns.managed_vserver import managed_vserver


'''
Configuration for Managed Vserver Information resource
'''

class user_managed_vserver(base_resource):
	_managed_vserver_list=[]
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
			return "user_managed_vserver"
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
			return "user_managed_vservers"
		except Exception as e :
			raise e



	'''
	get Managed/Unmanaged Vserver list
	'''
	@property
	def managed_vserver_list(self) :
		try:
			return self._managed_vserver_list
		except Exception as e :
			raise e
	'''
	set Managed/Unmanaged Vserver list
	'''
	@managed_vserver_list.setter
	def managed_vserver_list(self,managed_vserver_list) :
		try :
			if not isinstance(managed_vserver_list,list):
				raise TypeError("managed_vserver_list must be set to array of managed_vserver value")
			for item in managed_vserver_list :
				if not isinstance(item,managed_vserver):
					raise TypeError("item must be set to managed_vserver value")
			self._managed_vserver_list = managed_vserver_list
		except Exception as e :
			raise e

	'''
	Use this operation to manage/unmanage vservers.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				user_managed_vserver_obj= user_managed_vserver()
				return cls.perform_operation_bulk_request(service,"add", resource,user_managed_vserver_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(user_managed_vserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.user_managed_vserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(user_managed_vserver_responses, response, "user_managed_vserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.user_managed_vserver_response_array
				i=0
				error = [user_managed_vserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.user_managed_vserver_response_array
			i=0
			user_managed_vserver_objs = [user_managed_vserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_user_managed_vserver'):
					for props in obj._user_managed_vserver:
						result = service.payload_formatter.string_to_bulk_resource(user_managed_vserver_response,self.__class__.__name__,props)
						user_managed_vserver_objs[i] = result.user_managed_vserver
						i=i+1
			return user_managed_vserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(user_managed_vserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class user_managed_vserver_response(base_response):
	def __init__(self,length=1) :
		self.user_managed_vserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.user_managed_vserver= [ user_managed_vserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class user_managed_vserver_responses(base_response):
	def __init__(self,length=1) :
		self.user_managed_vserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.user_managed_vserver_response_array = [ user_managed_vserver() for _ in range(length)]
