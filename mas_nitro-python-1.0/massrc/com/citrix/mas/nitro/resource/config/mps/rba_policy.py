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
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_statement import rba_statement
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_ui import rba_ui


'''
Configuration for RBA Policy resource
'''

class rba_policy(base_resource):
	_tenant_id= ""
	_statement=[]
	_ui=[]
	_name= ""
	_id= ""
	_description= ""
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
			return "rba_policy"
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
			return "rba_policys"
		except Exception as e :
			raise e



	'''
	get Tenant Id of the system policys
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the system policys
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
	get RBA statement
	'''
	@property
	def statement(self) :
		try:
			return self._statement
		except Exception as e :
			raise e
	'''
	set RBA statement
	'''
	@statement.setter
	def statement(self,statement) :
		try :
			if not isinstance(statement,list):
				raise TypeError("statement must be set to array of rba_statement value")
			for item in statement :
				if not isinstance(item,rba_statement):
					raise TypeError("item must be set to rba_statement value")
			self._statement = statement
		except Exception as e :
			raise e


	'''
	get RBA for UI components
	'''
	@property
	def ui(self) :
		try:
			return self._ui
		except Exception as e :
			raise e
	'''
	set RBA for UI components
	'''
	@ui.setter
	def ui(self,ui) :
		try :
			if not isinstance(ui,list):
				raise TypeError("ui must be set to array of rba_ui value")
			for item in ui :
				if not isinstance(item,rba_ui):
					raise TypeError("item must be set to rba_ui value")
			self._ui = ui
		except Exception as e :
			raise e


	'''
	get Policy Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Policy Name
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
	get Id is system generated key for all the system policys
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system policys
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
	get Description of Policy
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of Policy
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
	Roles to which this policy attached
	'''
	@property
	def roles(self) :
		try:
			return self._roles
		except Exception as e :
			raise e
	'''
	Roles to which this policy attached
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
	Use this operation to add system policy.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				rba_policy_obj= rba_policy()
				return cls.perform_operation_bulk_request(service,"add", resource,rba_policy_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete system policy(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					rba_policy_obj=rba_policy()
					return cls.delete_bulk_request(client,resource,rba_policy_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get system policies.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				rba_policy_obj=rba_policy()
				response = rba_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify system policy.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				rba_policy_obj=rba_policy()
				return cls.update_bulk_request(client,resource,rba_policy_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of rba_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			rba_policy_obj = rba_policy()
			option_ = options()
			option_._filter=filter_
			return rba_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the rba_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			rba_policy_obj = rba_policy()
			option_ = options()
			option_._count=True
			response = rba_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of rba_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			rba_policy_obj = rba_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = rba_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(rba_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_policy_responses, response, "rba_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_policy_response_array
				i=0
				error = [rba_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_policy_response_array
			i=0
			rba_policy_objs = [rba_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_policy'):
					for props in obj._rba_policy:
						result = service.payload_formatter.string_to_bulk_resource(rba_policy_response,self.__class__.__name__,props)
						rba_policy_objs[i] = result.rba_policy
						i=i+1
			return rba_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_policy_response(base_response):
	def __init__(self,length=1) :
		self.rba_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_policy= [ rba_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_policy_responses(base_response):
	def __init__(self,length=1) :
		self.rba_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_policy_response_array = [ rba_policy() for _ in range(length)]
