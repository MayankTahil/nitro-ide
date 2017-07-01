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

class openstack(base_resource):
	_keystone_uri= ""
	_name= ""
	_glance_uri= ""
	_neutron_uri= ""
	_username= ""
	_keystone_admin_uri= ""
	_nova_uri= ""
	_password= ""
	_driver_username= ""
	_admin_tenant_id= ""
	_admin_tenant_name= ""
	_id= ""
	_driver_password= ""
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
			return "/oca/v1/openstacks"
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
			return "openstack"
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
			return "openstacks"
		except Exception as e :
			raise e



	'''
	get URI of keystone service in openstack
	'''
	@property
	def keystone_uri(self) :
		try:
			return self._keystone_uri
		except Exception as e :
			raise e
	'''
	set URI of keystone service in openstack
	'''
	@keystone_uri.setter
	def keystone_uri(self,keystone_uri):
		try :
			if not isinstance(keystone_uri,str):
				raise TypeError("keystone_uri must be set to str value")
			self._keystone_uri = keystone_uri
		except Exception as e :
			raise e


	'''
	get Name of openstack.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of openstack.
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
	get URI of glance service in openstack
	'''
	@property
	def glance_uri(self) :
		try:
			return self._glance_uri
		except Exception as e :
			raise e
	'''
	set URI of glance service in openstack
	'''
	@glance_uri.setter
	def glance_uri(self,glance_uri):
		try :
			if not isinstance(glance_uri,str):
				raise TypeError("glance_uri must be set to str value")
			self._glance_uri = glance_uri
		except Exception as e :
			raise e


	'''
	get URI of neutron service in openstack
	'''
	@property
	def neutron_uri(self) :
		try:
			return self._neutron_uri
		except Exception as e :
			raise e
	'''
	set URI of neutron service in openstack
	'''
	@neutron_uri.setter
	def neutron_uri(self,neutron_uri):
		try :
			if not isinstance(neutron_uri,str):
				raise TypeError("neutron_uri must be set to str value")
			self._neutron_uri = neutron_uri
		except Exception as e :
			raise e


	'''
	get Username of admin tenant in openstack
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Username of admin tenant in openstack
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get Admin URI of Keystone in OpenStack
	'''
	@property
	def keystone_admin_uri(self) :
		try:
			return self._keystone_admin_uri
		except Exception as e :
			raise e
	'''
	set Admin URI of Keystone in OpenStack
	'''
	@keystone_admin_uri.setter
	def keystone_admin_uri(self,keystone_admin_uri):
		try :
			if not isinstance(keystone_admin_uri,str):
				raise TypeError("keystone_admin_uri must be set to str value")
			self._keystone_admin_uri = keystone_admin_uri
		except Exception as e :
			raise e


	'''
	get URI of nova service in openstack
	'''
	@property
	def nova_uri(self) :
		try:
			return self._nova_uri
		except Exception as e :
			raise e
	'''
	set URI of nova service in openstack
	'''
	@nova_uri.setter
	def nova_uri(self,nova_uri):
		try :
			if not isinstance(nova_uri,str):
				raise TypeError("nova_uri must be set to str value")
			self._nova_uri = nova_uri
		except Exception as e :
			raise e


	'''
	get Password of admin tenant in openstack
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password of admin tenant in openstack
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
	get Username of netscaler driver account created in controlcenter.
	'''
	@property
	def driver_username(self) :
		try:
			return self._driver_username
		except Exception as e :
			raise e
	'''
	set Username of netscaler driver account created in controlcenter.
	'''
	@driver_username.setter
	def driver_username(self,driver_username):
		try :
			if not isinstance(driver_username,str):
				raise TypeError("driver_username must be set to str value")
			self._driver_username = driver_username
		except Exception as e :
			raise e


	'''
	get Admin Tenant Id in OpenStack
	'''
	@property
	def admin_tenant_id(self) :
		try:
			return self._admin_tenant_id
		except Exception as e :
			raise e
	'''
	set Admin Tenant Id in OpenStack
	'''
	@admin_tenant_id.setter
	def admin_tenant_id(self,admin_tenant_id):
		try :
			if not isinstance(admin_tenant_id,str):
				raise TypeError("admin_tenant_id must be set to str value")
			self._admin_tenant_id = admin_tenant_id
		except Exception as e :
			raise e


	'''
	get Admin Tenant Name in OpenStack
	'''
	@property
	def admin_tenant_name(self) :
		try:
			return self._admin_tenant_name
		except Exception as e :
			raise e
	'''
	set Admin Tenant Name in OpenStack
	'''
	@admin_tenant_name.setter
	def admin_tenant_name(self,admin_tenant_name):
		try :
			if not isinstance(admin_tenant_name,str):
				raise TypeError("admin_tenant_name must be set to str value")
			self._admin_tenant_name = admin_tenant_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for openstack cloud
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for openstack cloud
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
	get Password of netscaler driver account created in controlcenter.
	'''
	@property
	def driver_password(self) :
		try:
			return self._driver_password
		except Exception as e :
			raise e
	'''
	set Password of netscaler driver account created in controlcenter.
	'''
	@driver_password.setter
	def driver_password(self,driver_password):
		try :
			if not isinstance(driver_password,str):
				raise TypeError("driver_password must be set to str value")
			self._driver_password = driver_password
		except Exception as e :
			raise e

	'''
	Use this operation to add a OpenStack details.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				openstack_obj= openstack()
				return cls.perform_operation_bulk_request(service,"add", resource,openstack_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to OpenStack cloud details.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					openstack_obj=openstack()
					return cls.delete_bulk_request(client,resource,openstack_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get OpenStack cloud details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				openstack_obj=openstack()
				response = openstack_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify OpenStack cloud details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				openstack_obj=openstack()
				return cls.update_bulk_request(client,resource,openstack_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of openstack resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			openstack_obj = openstack()
			option_ = options()
			option_._filter=filter_
			return openstack_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the openstack resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			openstack_obj = openstack()
			option_ = options()
			option_._count=True
			response = openstack_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of openstack resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			openstack_obj = openstack()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = openstack_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(openstack_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.openstack
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(openstack_responses, response, "openstack_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.openstack_response_array
				i=0
				error = [openstack() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.openstack_response_array
			i=0
			openstack_objs = [openstack() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_openstack'):
					for props in obj._openstack:
						result = service.payload_formatter.string_to_bulk_resource(openstack_response,self.__class__.__name__,props)
						openstack_objs[i] = result.openstack
						i=i+1
			return openstack_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(openstack,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class openstack_response(base_response):
	def __init__(self,length=1) :
		self.openstack= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.openstack= [ openstack() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class openstack_responses(base_response):
	def __init__(self,length=1) :
		self.openstack_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.openstack_response_array = [ openstack() for _ in range(length)]
