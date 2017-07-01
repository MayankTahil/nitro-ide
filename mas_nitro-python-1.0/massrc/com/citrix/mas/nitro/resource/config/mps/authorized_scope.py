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
Configuration for Authorized Scope resource
'''

class authorized_scope(base_resource):
	_formation_device_id= ""
	_group_id= ""
	_id= ""
	_managed_device_id= ""
	_managed_device_id_array=[]
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
			return "authorized_scope"
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
			return "authorized_scopes"
		except Exception as e :
			raise e



	'''
	get formation device id
	'''
	@property
	def formation_device_id(self) :
		try:
			return self._formation_device_id
		except Exception as e :
			raise e
	'''
	set formation device id
	'''
	@formation_device_id.setter
	def formation_device_id(self,formation_device_id):
		try :
			if not isinstance(formation_device_id,str):
				raise TypeError("formation_device_id must be set to str value")
			self._formation_device_id = formation_device_id
		except Exception as e :
			raise e


	'''
	get Id of the group
	'''
	@property
	def group_id(self) :
		try:
			return self._group_id
		except Exception as e :
			raise e
	'''
	set Id of the group
	'''
	@group_id.setter
	def group_id(self,group_id):
		try :
			if not isinstance(group_id,str):
				raise TypeError("group_id must be set to str value")
			self._group_id = group_id
		except Exception as e :
			raise e


	'''
	get Auto generated ID.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Auto generated ID.
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
	get managed device id
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e
	'''
	set managed device id
	'''
	@managed_device_id.setter
	def managed_device_id(self,managed_device_id):
		try :
			if not isinstance(managed_device_id,str):
				raise TypeError("managed_device_id must be set to str value")
			self._managed_device_id = managed_device_id
		except Exception as e :
			raise e

	'''
	Array for formation device
	'''
	@property
	def formation_device_id_array(self) :
		try:
			return self._formation_device_id_array
		except Exception as e :
			raise e
	'''
	Array for formation device
	'''
	@formation_device_id_array.setter
	def formation_device_id_array(self,formation_device_id_array) :
		try :
			if not isinstance(formation_device_id_array,list):
				raise TypeError("formation_device_id_array must be set to array of str value")
			for item in formation_device_id_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._formation_device_id_array = formation_device_id_array
		except Exception as e :
			raise e

	'''
	Applications
	'''
	@property
	def auth_application_list(self) :
		try:
			return self._auth_application_list
		except Exception as e :
			raise e
	'''
	Applications
	'''
	@auth_application_list.setter
	def auth_application_list(self,auth_application_list) :
		try :
			if not isinstance(auth_application_list,list):
				raise TypeError("auth_application_list must be set to array of authorized_application value")
			for item in auth_application_list :
				if not isinstance(item,authorized_application):
					raise TypeError("item must be set to authorized_application value")
			self._auth_application_list = auth_application_list
		except Exception as e :
			raise e

	'''
	Array for managed device
	'''
	@property
	def managed_device_id_array(self) :
		try:
			return self._managed_device_id_array
		except Exception as e :
			raise e
	'''
	Array for managed device
	'''
	@managed_device_id_array.setter
	def managed_device_id_array(self,managed_device_id_array) :
		try :
			if not isinstance(managed_device_id_array,list):
				raise TypeError("managed_device_id_array must be set to array of str value")
			for item in managed_device_id_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._managed_device_id_array = managed_device_id_array
		except Exception as e :
			raise e

	'''
	Use this operation to add system group.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				authorized_scope_obj= authorized_scope()
				return cls.perform_operation_bulk_request(service,"add", resource,authorized_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete system group(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					authorized_scope_obj=authorized_scope()
					return cls.delete_bulk_request(client,resource,authorized_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get system groups.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				authorized_scope_obj=authorized_scope()
				response = authorized_scope_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system group.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				authorized_scope_obj=authorized_scope()
				return cls.update_bulk_request(client,resource,authorized_scope_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of authorized_scope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			authorized_scope_obj = authorized_scope()
			option_ = options()
			option_._filter=filter_
			return authorized_scope_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the authorized_scope resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			authorized_scope_obj = authorized_scope()
			option_ = options()
			option_._count=True
			response = authorized_scope_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of authorized_scope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			authorized_scope_obj = authorized_scope()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = authorized_scope_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(authorized_scope_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authorized_scope
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(authorized_scope_responses, response, "authorized_scope_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.authorized_scope_response_array
				i=0
				error = [authorized_scope() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.authorized_scope_response_array
			i=0
			authorized_scope_objs = [authorized_scope() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_authorized_scope'):
					for props in obj._authorized_scope:
						result = service.payload_formatter.string_to_bulk_resource(authorized_scope_response,self.__class__.__name__,props)
						authorized_scope_objs[i] = result.authorized_scope
						i=i+1
			return authorized_scope_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(authorized_scope,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class authorized_scope_response(base_response):
	def __init__(self,length=1) :
		self.authorized_scope= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.authorized_scope= [ authorized_scope() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class authorized_scope_responses(base_response):
	def __init__(self,length=1) :
		self.authorized_scope_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.authorized_scope_response_array = [ authorized_scope() for _ in range(length)]
