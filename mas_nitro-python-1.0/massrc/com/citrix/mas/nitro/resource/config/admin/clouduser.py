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
from massrc.com.citrix.mas.nitro.resource.config.admin.resource import resource


'''
Configuration for A cloud user resource represents a tenant in the cloud. Tenants are the unit of accounting: Resources (such as devices, network services, etc.) are always associated with tenants based on configured policies. resource
'''

class clouduser(base_resource):
	_resources= ""
	_parent= ""
	_status= ""
	_name= ""
	_id= ""
	_description= ""
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
			return "/admin/v1/cloudusers"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "cloudusers"
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
			return "clouduser"
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
			return "cloudusers"
		except Exception as e :
			raise e



	'''
	get Resources allocated to this tenant
	'''
	@property
	def resources(self) :
		try:
			return self._resources
		except Exception as e :
			raise e


	'''
	get parent tenant ID - default: None
	'''
	@property
	def parent(self) :
		try:
			return self._parent
		except Exception as e :
			raise e
	'''
	set parent tenant ID - default: None
	'''
	@parent.setter
	def parent(self,parent):
		try :
			if not isinstance(parent,str):
				raise TypeError("parent must be set to str value")
			self._parent = parent
		except Exception as e :
			raise e


	'''
	get Status of the tenant - ACTIVE or DOWN
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of the tenant - ACTIVE or DOWN
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Name of tenant.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of tenant.
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
	get ID of the tenant
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID of the tenant
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
	get Textual description of the tenant
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Textual description of the tenant
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
	Use this operation to add a cloud user.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				clouduser_obj= clouduser()
				return cls.perform_operation_bulk_request(service,"add", resource,clouduser_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete  cloud user.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					clouduser_obj=clouduser()
					return cls.delete_bulk_request(client,resource,clouduser_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get cloud user details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				clouduser_obj=clouduser()
				response = clouduser_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of clouduser resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			clouduser_obj = clouduser()
			option_ = options()
			option_._filter=filter_
			return clouduser_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the clouduser resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			clouduser_obj = clouduser()
			option_ = options()
			option_._count=True
			response = clouduser_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of clouduser resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			clouduser_obj = clouduser()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = clouduser_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(clouduser_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clouduser
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(clouduser_responses, response, "clouduser_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.clouduser_response_array
				i=0
				error = [clouduser() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.clouduser_response_array
			i=0
			clouduser_objs = [clouduser() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_clouduser'):
					for props in obj._clouduser:
						result = service.payload_formatter.string_to_bulk_resource(clouduser_response,self.__class__.__name__,props)
						clouduser_objs[i] = result.clouduser
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(clouduser,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class clouduser_response(base_response):
	def __init__(self,length=1) :
		self.clouduser= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.clouduser= [ clouduser() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class clouduser_responses(base_response):
	def __init__(self,length=1) :
		self.clouduser_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.clouduser_response_array = [ clouduser() for _ in range(length)]
