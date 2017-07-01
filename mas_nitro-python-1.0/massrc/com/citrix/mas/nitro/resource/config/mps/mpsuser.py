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
Configuration for System User resource
'''

class mpsuser(base_resource):
	_session_timeout= ""
	_permission= ""
	_name= ""
	_session_timeout_unit= ""
	_external_authentication= ""
	_enable_session_timeout= ""
	_tenant_id= ""
	_password= ""
	_id= ""
	_groups=[]
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
			return "mpsuser"
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
			return "mpsusers"
		except Exception as e :
			raise e



	'''
	get Session timeout for the user
	'''
	@property
	def session_timeout(self) :
		try:
			return self._session_timeout
		except Exception as e :
			raise e
	'''
	set Session timeout for the user
	'''
	@session_timeout.setter
	def session_timeout(self,session_timeout):
		try :
			if not isinstance(session_timeout,int):
				raise TypeError("session_timeout must be set to int value")
			self._session_timeout = session_timeout
		except Exception as e :
			raise e


	'''
	This property is not supported, permission will be taken from groups only
	get Actions that this user is authorized to perform
	'''
	@property
	def permission(self) :
		try:
			return self._permission
		except Exception as e :
			raise e
	'''
	This property is not supported, permission will be taken from groups only
	set Actions that this user is authorized to perform
	'''
	@permission.setter
	def permission(self,permission):
		try :
			if not isinstance(permission,str):
				raise TypeError("permission must be set to str value")
			self._permission = permission
		except Exception as e :
			raise e


	'''
	get User Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set User Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Session timeout unit for the user
	'''
	@property
	def session_timeout_unit(self) :
		try:
			return self._session_timeout_unit
		except Exception as e :
			raise e
	'''
	set Session timeout unit for the user
	'''
	@session_timeout_unit.setter
	def session_timeout_unit(self,session_timeout_unit):
		try :
			if not isinstance(session_timeout_unit,str):
				raise TypeError("session_timeout_unit must be set to str value")
			self._session_timeout_unit = session_timeout_unit
		except Exception as e :
			raise e


	'''
	get Enable external authentication
	'''
	@property
	def external_authentication(self) :
		try:
			return self._external_authentication
		except Exception as e :
			raise e
	'''
	set Enable external authentication
	'''
	@external_authentication.setter
	def external_authentication(self,external_authentication):
		try :
			if not isinstance(external_authentication,bool):
				raise TypeError("external_authentication must be set to bool value")
			self._external_authentication = external_authentication
		except Exception as e :
			raise e


	'''
	get Enables session timeout for user
	'''
	@property
	def enable_session_timeout(self) :
		try:
			return self._enable_session_timeout
		except Exception as e :
			raise e
	'''
	set Enables session timeout for user
	'''
	@enable_session_timeout.setter
	def enable_session_timeout(self,enable_session_timeout):
		try :
			if not isinstance(enable_session_timeout,bool):
				raise TypeError("enable_session_timeout must be set to bool value")
			self._enable_session_timeout = enable_session_timeout
		except Exception as e :
			raise e


	'''
	get Tenant Id of the system users
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the system users
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system users
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system users
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
	Groups to which user belongs
	'''
	@property
	def groups(self) :
		try:
			return self._groups
		except Exception as e :
			raise e
	'''
	Groups to which user belongs
	'''
	@groups.setter
	def groups(self,groups) :
		try :
			if not isinstance(groups,list):
				raise TypeError("groups must be set to array of str value")
			for item in groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._groups = groups
		except Exception as e :
			raise e

	'''
	Use this operation to add system user.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				mpsuser_obj= mpsuser()
				return cls.perform_operation_bulk_request(service,"add", resource,mpsuser_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete system user(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					mpsuser_obj=mpsuser()
					return cls.delete_bulk_request(client,resource,mpsuser_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get system users.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mpsuser_obj=mpsuser()
				response = mpsuser_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system user.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				mpsuser_obj=mpsuser()
				return cls.update_bulk_request(client,resource,mpsuser_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mpsuser resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mpsuser_obj = mpsuser()
			option_ = options()
			option_._filter=filter_
			return mpsuser_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mpsuser resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mpsuser_obj = mpsuser()
			option_ = options()
			option_._count=True
			response = mpsuser_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mpsuser resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mpsuser_obj = mpsuser()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mpsuser_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mpsuser_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mpsuser
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mpsuser_responses, response, "mpsuser_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mpsuser_response_array
				i=0
				error = [mpsuser() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mpsuser_response_array
			i=0
			mpsuser_objs = [mpsuser() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mpsuser'):
					for props in obj._mpsuser:
						result = service.payload_formatter.string_to_bulk_resource(mpsuser_response,self.__class__.__name__,props)
						mpsuser_objs[i] = result.mpsuser
						i=i+1
			return mpsuser_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mpsuser,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mpsuser_response(base_response):
	def __init__(self,length=1) :
		self.mpsuser= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mpsuser= [ mpsuser() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mpsuser_responses(base_response):
	def __init__(self,length=1) :
		self.mpsuser_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mpsuser_response_array = [ mpsuser() for _ in range(length)]
