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
Configuration for OpenStack Cloud configuration resource
'''

class tenant(base_resource):
	_openstack_tenant_name= ""
	_nsm_tenant_id= ""
	_openstack_tenant_id= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/oca/v1/tenants"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "tenants"
		except Exception as e :
			raise e

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
			return self._openstack_tenant_id
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
	get Name of openstack tenant.
	'''
	@property
	def openstack_tenant_name(self) :
		try:
			return self._openstack_tenant_name
		except Exception as e :
			raise e


	'''
	get Tenant Id in ControlCenter corresponds to OpenStack Tenant
	'''
	@property
	def nsm_tenant_id(self) :
		try:
			return self._nsm_tenant_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for openstack Tenant
	'''
	@property
	def openstack_tenant_id(self) :
		try:
			return self._openstack_tenant_id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for openstack Tenant
	'''
	@openstack_tenant_id.setter
	def openstack_tenant_id(self,openstack_tenant_id):
		try :
			if not isinstance(openstack_tenant_id,str):
				raise TypeError("openstack_tenant_id must be set to str value")
			self._openstack_tenant_id = openstack_tenant_id
		except Exception as e :
			raise e

	'''
	Use this operation to add a OpenStack Tenant details.
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
	Use this operation to delete OpenStack tenant.
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
	Use this operation to get OpenStack Tenant details.
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
			result=service.payload_formatter.string_to_resource(tenant_response, response, self.__class__.__name__,class_name=self.__class__)
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
			result=service.payload_formatter.string_to_resource(tenant_responses, response, "tenant_response_array", class_name=self.__class__)
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
			return response
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
