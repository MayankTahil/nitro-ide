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
Configuration for System Groups resource
'''

class mpsgroup(base_resource):
	_allow_application_only= ""
	_session_timeout= ""
	_permission= ""
	_name= ""
	_session_timeout_unit= ""
	_assign_all_apps= ""
	_enable_session_timeout= ""
	_tenant_id= ""
	_assign_all_devices= ""
	_id= ""
	_role= ""
	_roles=[]
	_application_names=[]
	_standalone_instances_id=[]
	_users=[]
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
			return "mpsgroup"
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
			return "mpsgroups"
		except Exception as e :
			raise e



	'''
	get Checks if only application centic page is needed
	'''
	@property
	def allow_application_only(self) :
		try:
			return self._allow_application_only
		except Exception as e :
			raise e
	'''
	set Checks if only application centic page is needed
	'''
	@allow_application_only.setter
	def allow_application_only(self,allow_application_only):
		try :
			if not isinstance(allow_application_only,bool):
				raise TypeError("allow_application_only must be set to bool value")
			self._allow_application_only = allow_application_only
		except Exception as e :
			raise e


	'''
	get Session timeout for the Group
	'''
	@property
	def session_timeout(self) :
		try:
			return self._session_timeout
		except Exception as e :
			raise e
	'''
	set Session timeout for the Group
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
	get Permission for the group (admin/read-only)
	'''
	@property
	def permission(self) :
		try:
			return self._permission
		except Exception as e :
			raise e
	'''
	set Permission for the group (admin/read-only)
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
	get Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Group Name
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
	get Session timeout unit for the Group
	'''
	@property
	def session_timeout_unit(self) :
		try:
			return self._session_timeout_unit
		except Exception as e :
			raise e
	'''
	set Session timeout unit for the Group
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
	get Assign All Applications (YES|NO)
	'''
	@property
	def assign_all_apps(self) :
		try:
			return self._assign_all_apps
		except Exception as e :
			raise e
	'''
	set Assign All Applications (YES|NO)
	'''
	@assign_all_apps.setter
	def assign_all_apps(self,assign_all_apps):
		try :
			if not isinstance(assign_all_apps,bool):
				raise TypeError("assign_all_apps must be set to bool value")
			self._assign_all_apps = assign_all_apps
		except Exception as e :
			raise e


	'''
	get Enables session timeout for group
	'''
	@property
	def enable_session_timeout(self) :
		try:
			return self._enable_session_timeout
		except Exception as e :
			raise e
	'''
	set Enables session timeout for group
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
	get Id of the tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of the tenant
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
	get Assign All Instances (YES|NO)
	'''
	@property
	def assign_all_devices(self) :
		try:
			return self._assign_all_devices
		except Exception as e :
			raise e
	'''
	set Assign All Instances (YES|NO)
	'''
	@assign_all_devices.setter
	def assign_all_devices(self,assign_all_devices):
		try :
			if not isinstance(assign_all_devices,bool):
				raise TypeError("assign_all_devices must be set to bool value")
			self._assign_all_devices = assign_all_devices
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system groups
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system groups
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
	get Role (admin|nonadmin)
	'''
	@property
	def role(self) :
		try:
			return self._role
		except Exception as e :
			raise e
	'''
	set Role (admin|nonadmin)
	'''
	@role.setter
	def role(self,role):
		try :
			if not isinstance(role,str):
				raise TypeError("role must be set to str value")
			self._role = role
		except Exception as e :
			raise e

	'''
	Roles assigned to the group
	'''
	@property
	def roles(self) :
		try:
			return self._roles
		except Exception as e :
			raise e
	'''
	Roles assigned to the group
	'''
	@roles.setter
	def roles(self,roles) :
		try :
			if not isinstance(roles,list):
				raise TypeError("roles must be set to array of str value")
			for item in roles :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._roles = roles
		except Exception as e :
			raise e

	'''
	Application names that are part of this group
	'''
	@property
	def application_names(self) :
		try:
			return self._application_names
		except Exception as e :
			raise e
	'''
	Application names that are part of this group
	'''
	@application_names.setter
	def application_names(self,application_names) :
		try :
			if not isinstance(application_names,list):
				raise TypeError("application_names must be set to array of str value")
			for item in application_names :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._application_names = application_names
		except Exception as e :
			raise e

	'''
	Stand alone instances belong to this groupp
	'''
	@property
	def standalone_instances_id(self) :
		try:
			return self._standalone_instances_id
		except Exception as e :
			raise e
	'''
	Stand alone instances belong to this groupp
	'''
	@standalone_instances_id.setter
	def standalone_instances_id(self,standalone_instances_id) :
		try :
			if not isinstance(standalone_instances_id,list):
				raise TypeError("standalone_instances_id must be set to array of str value")
			for item in standalone_instances_id :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._standalone_instances_id = standalone_instances_id
		except Exception as e :
			raise e

	'''
	Users belong to the group
	'''
	@property
	def users(self) :
		try:
			return self._users
		except Exception as e :
			raise e
	'''
	Users belong to the group
	'''
	@users.setter
	def users(self,users) :
		try :
			if not isinstance(users,list):
				raise TypeError("users must be set to array of str value")
			for item in users :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._users = users
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
				mpsgroup_obj= mpsgroup()
				return cls.perform_operation_bulk_request(service,"add", resource,mpsgroup_obj)
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
					mpsgroup_obj=mpsgroup()
					return cls.delete_bulk_request(client,resource,mpsgroup_obj)
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
				mpsgroup_obj=mpsgroup()
				response = mpsgroup_obj.get_resources(client,option_)
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
				mpsgroup_obj=mpsgroup()
				return cls.update_bulk_request(client,resource,mpsgroup_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mpsgroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mpsgroup_obj = mpsgroup()
			option_ = options()
			option_._filter=filter_
			return mpsgroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mpsgroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mpsgroup_obj = mpsgroup()
			option_ = options()
			option_._count=True
			response = mpsgroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mpsgroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mpsgroup_obj = mpsgroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mpsgroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mpsgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mpsgroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mpsgroup_responses, response, "mpsgroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mpsgroup_response_array
				i=0
				error = [mpsgroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mpsgroup_response_array
			i=0
			mpsgroup_objs = [mpsgroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mpsgroup'):
					for props in obj._mpsgroup:
						result = service.payload_formatter.string_to_bulk_resource(mpsgroup_response,self.__class__.__name__,props)
						mpsgroup_objs[i] = result.mpsgroup
						i=i+1
			return mpsgroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mpsgroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mpsgroup_response(base_response):
	def __init__(self,length=1) :
		self.mpsgroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mpsgroup= [ mpsgroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mpsgroup_responses(base_response):
	def __init__(self,length=1) :
		self.mpsgroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mpsgroup_response_array = [ mpsgroup() for _ in range(length)]
