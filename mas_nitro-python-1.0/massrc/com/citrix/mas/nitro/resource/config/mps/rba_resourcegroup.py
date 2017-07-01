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
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_resourcegroup_props import rba_resourcegroup_props


'''
Configuration for RBA Resource Group resource
'''

class rba_resourcegroup(base_resource):
	_tenant_id= ""
	_props=[]
	_name= ""
	_id= ""
	_roles=[]
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
			return "rba_resourcegroup"
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
			return "rba_resourcegroups"
		except Exception as e :
			raise e



	'''
	get Tenant Id of the RBA resource group
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the RBA resource group
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
	get RBA Resource Group Props
	'''
	@property
	def props(self) :
		try:
			return self._props
		except Exception as e :
			raise e
	'''
	set RBA Resource Group Props
	'''
	@props.setter
	def props(self,props) :
		try :
			if not isinstance(props,list):
				raise TypeError("props must be set to array of rba_resourcegroup_props value")
			for item in props :
				if not isinstance(item,rba_resourcegroup_props):
					raise TypeError("item must be set to rba_resourcegroup_props value")
			self._props = props
		except Exception as e :
			raise e


	'''
	get Resource Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Resource Group Name
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
	get Id is system generated key for RBA resource group
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for RBA resource group
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
	Roles to which this resourcegroup is assigned
	'''
	@property
	def roles(self) :
		try:
			return self._roles
		except Exception as e :
			raise e
	'''
	Roles to which this resourcegroup is assigned
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
	Use this operation to add RBA resource groups.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				rba_resourcegroup_obj= rba_resourcegroup()
				return cls.perform_operation_bulk_request(service,"add", resource,rba_resourcegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete RBA resource groups.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					rba_resourcegroup_obj=rba_resourcegroup()
					return cls.delete_bulk_request(client,resource,rba_resourcegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get RBA resource groups.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				rba_resourcegroup_obj=rba_resourcegroup()
				response = rba_resourcegroup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify RBA resource groups.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				rba_resourcegroup_obj=rba_resourcegroup()
				return cls.update_bulk_request(client,resource,rba_resourcegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of rba_resourcegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			rba_resourcegroup_obj = rba_resourcegroup()
			option_ = options()
			option_._filter=filter_
			return rba_resourcegroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the rba_resourcegroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			rba_resourcegroup_obj = rba_resourcegroup()
			option_ = options()
			option_._count=True
			response = rba_resourcegroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of rba_resourcegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			rba_resourcegroup_obj = rba_resourcegroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = rba_resourcegroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(rba_resourcegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_resourcegroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_resourcegroup_responses, response, "rba_resourcegroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_resourcegroup_response_array
				i=0
				error = [rba_resourcegroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_resourcegroup_response_array
			i=0
			rba_resourcegroup_objs = [rba_resourcegroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_resourcegroup'):
					for props in obj._rba_resourcegroup:
						result = service.payload_formatter.string_to_bulk_resource(rba_resourcegroup_response,self.__class__.__name__,props)
						rba_resourcegroup_objs[i] = result.rba_resourcegroup
						i=i+1
			return rba_resourcegroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_resourcegroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_resourcegroup_response(base_response):
	def __init__(self,length=1) :
		self.rba_resourcegroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_resourcegroup= [ rba_resourcegroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_resourcegroup_responses(base_response):
	def __init__(self,length=1) :
		self.rba_resourcegroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_resourcegroup_response_array = [ rba_resourcegroup() for _ in range(length)]
