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
Configuration for RBA Role resource
'''

class rba_role(base_resource):
	_tenant_id= ""
	_name= ""
	_id= ""
	_description= ""
	_resourcegroups=[]
	_groups=[]
	_policies=[]
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
			return "rba_role"
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
			return "rba_roles"
		except Exception as e :
			raise e



	'''
	get Tenant Id of the RBA roles
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the RBA roles
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
	get Role Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Role Name
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
	get Id is system generated key for all the RBA roles
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the RBA roles
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
	get Description of Role
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of Role
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e

	'''
	Resourcegroups attached to this role.
	'''
	@property
	def resourcegroups(self) :
		try:
			return self._resourcegroups
		except Exception as e :
			raise e
	'''
	Resourcegroups attached to this role.
	'''
	@resourcegroups.setter
	def resourcegroups(self,resourcegroups) :
		try :
			if not isinstance(resourcegroups,list):
				raise TypeError("resourcegroups must be set to array of str value")
			for item in resourcegroups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._resourcegroups = resourcegroups
		except Exception as e :
			raise e

	'''
	Groups to which this role is assigned
	'''
	@property
	def groups(self) :
		try:
			return self._groups
		except Exception as e :
			raise e
	'''
	Groups to which this role is assigned
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
	Policies attached to this role.
	'''
	@property
	def policies(self) :
		try:
			return self._policies
		except Exception as e :
			raise e
	'''
	Policies attached to this role.
	'''
	@policies.setter
	def policies(self,policies) :
		try :
			if not isinstance(policies,list):
				raise TypeError("policies must be set to array of str value")
			for item in policies :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._policies = policies
		except Exception as e :
			raise e

	'''
	Use this operation to add RBA role.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				rba_role_obj= rba_role()
				return cls.perform_operation_bulk_request(service,"add", resource,rba_role_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete RBA role(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					rba_role_obj=rba_role()
					return cls.delete_bulk_request(client,resource,rba_role_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get RBA roles.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				rba_role_obj=rba_role()
				response = rba_role_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify RBA role.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				rba_role_obj=rba_role()
				return cls.update_bulk_request(client,resource,rba_role_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of rba_role resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			rba_role_obj = rba_role()
			option_ = options()
			option_._filter=filter_
			return rba_role_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the rba_role resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			rba_role_obj = rba_role()
			option_ = options()
			option_._count=True
			response = rba_role_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of rba_role resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			rba_role_obj = rba_role()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = rba_role_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(rba_role_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_role
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_role_responses, response, "rba_role_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_role_response_array
				i=0
				error = [rba_role() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_role_response_array
			i=0
			rba_role_objs = [rba_role() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_role'):
					for props in obj._rba_role:
						result = service.payload_formatter.string_to_bulk_resource(rba_role_response,self.__class__.__name__,props)
						rba_role_objs[i] = result.rba_role
						i=i+1
			return rba_role_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_role,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_role_response(base_response):
	def __init__(self,length=1) :
		self.rba_role= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_role= [ rba_role() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_role_responses(base_response):
	def __init__(self,length=1) :
		self.rba_role_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_role_response_array = [ rba_role() for _ in range(length)]
