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
from massrc.com.citrix.mas.nitro.resource.config.mps.tenant_system_resource import tenant_system_resource
from massrc.com.citrix.mas.nitro.resource.config.mps.tenant_company_info import tenant_company_info


'''
Configuration for Tenants resource
'''

class tenant(base_resource):
	_system_resource= ""
	_name= ""
	_company_info= ""
	_user_name= ""
	_parent_id= ""
	_password= ""
	_preauthtoken= ""
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
			return "tenant"
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
			return "tenants"
		except Exception as e :
			raise e



	'''
	get Tenant System Resource
	'''
	@property
	def system_resource(self) :
		try:
			return self._system_resource
		except Exception as e :
			raise e
	'''
	set Tenant System Resource
	'''
	@system_resource.setter
	def system_resource(self,system_resource):
		try :
			if not isinstance(system_resource,tenant_system_resource):
				raise TypeError("system_resource must be set to tenant_system_resource value")
			self._system_resource = system_resource
		except Exception as e :
			raise e


	'''
	get Name of the Tenant
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the Tenant
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
	get Tenant Company Information
	'''
	@property
	def company_info(self) :
		try:
			return self._company_info
		except Exception as e :
			raise e
	'''
	set Tenant Company Information
	'''
	@company_info.setter
	def company_info(self,company_info):
		try :
			if not isinstance(company_info,tenant_company_info):
				raise TypeError("company_info must be set to tenant_company_info value")
			self._company_info = company_info
		except Exception as e :
			raise e


	'''
	get User Name for tenant
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set User Name for tenant
	'''
	@user_name.setter
	def user_name(self,user_name):
		try :
			if not isinstance(user_name,str):
				raise TypeError("user_name must be set to str value")
			self._user_name = user_name
		except Exception as e :
			raise e


	'''
	get Tenant ID of the parent Tenant.
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set Tenant ID of the parent Tenant.
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
	get Preauth token for a tenant
	'''
	@property
	def preauthtoken(self) :
		try:
			return self._preauthtoken
		except Exception as e :
			raise e
	'''
	set Preauth token for a tenant
	'''
	@preauthtoken.setter
	def preauthtoken(self,preauthtoken):
		try :
			if not isinstance(preauthtoken,str):
				raise TypeError("preauthtoken must be set to str value")
			self._preauthtoken = preauthtoken
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the Tenants
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Tenants
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
	Use this operation to add a tenant..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				tenant_obj= tenant()
				return cls.perform_operation_bulk_request(service,"add", resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a tenant..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					tenant_obj=tenant()
					return cls.delete_bulk_request(client,resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get tenants..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tenant_obj=tenant()
				response = tenant_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a tenant..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				tenant_obj=tenant()
				return cls.update_bulk_request(client,resource,tenant_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._filter=filter_
			return tenant_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._count=True
			response = tenant_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_obj = tenant()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_responses, response, "tenant_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_response_array
				i=0
				error = [tenant() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_response_array
			i=0
			tenant_objs = [tenant() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant'):
					for props in obj._tenant:
						result = service.payload_formatter.string_to_bulk_resource(tenant_response,self.__class__.__name__,props)
						tenant_objs[i] = result.tenant
						i=i+1
			return tenant_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_response(base_response):
	def __init__(self,length=1) :
		self.tenant= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant= [ tenant() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_response_array = [ tenant() for _ in range(length)]
