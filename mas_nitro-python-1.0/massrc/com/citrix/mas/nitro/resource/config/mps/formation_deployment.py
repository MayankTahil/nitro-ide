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
Configuration for Formation Deployment resource
'''

class formation_deployment(base_resource):
	_template_version= ""
	_template_name= ""
	_file_name= ""
	_platform_id= ""
	_description= ""
	_template_schema_version= ""
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
			return "formation_deployment"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "formation_deployments"
		except Exception as e :
			raise e



	'''
	get Formation Template version
	'''
	@property
	def template_version(self) :
		try:
			return self._template_version
		except Exception as e :
			raise e
	'''
	set Formation Template version
	'''
	@template_version.setter
	def template_version(self,template_version):
		try :
			if not isinstance(template_version,str):
				raise TypeError("template_version must be set to str value")
			self._template_version = template_version
		except Exception as e :
			raise e


	'''
	get Formation Template Name
	'''
	@property
	def template_name(self) :
		try:
			return self._template_name
		except Exception as e :
			raise e
	'''
	set Formation Template Name
	'''
	@template_name.setter
	def template_name(self,template_name):
		try :
			if not isinstance(template_name,str):
				raise TypeError("template_name must be set to str value")
			self._template_name = template_name
		except Exception as e :
			raise e


	'''
	get Formation Deployment filename
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Formation Deployment filename
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Platform ID
	'''
	@property
	def platform_id(self) :
		try:
			return self._platform_id
		except Exception as e :
			raise e
	'''
	set Platform ID
	'''
	@platform_id.setter
	def platform_id(self,platform_id):
		try :
			if not isinstance(platform_id,str):
				raise TypeError("platform_id must be set to str value")
			self._platform_id = platform_id
		except Exception as e :
			raise e


	'''
	get description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set description
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
	get Template Schema version
	'''
	@property
	def template_schema_version(self) :
		try:
			return self._template_schema_version
		except Exception as e :
			raise e
	'''
	set Template Schema version
	'''
	@template_schema_version.setter
	def template_schema_version(self,template_schema_version):
		try :
			if not isinstance(template_schema_version,str):
				raise TypeError("template_schema_version must be set to str value")
			self._template_schema_version = template_schema_version
		except Exception as e :
			raise e

	'''
	Use this operation to delete the formation Deployments.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					formation_deployment_obj=formation_deployment()
					return cls.delete_bulk_request(client,resource,formation_deployment_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get the formation Deployments.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				formation_deployment_obj=formation_deployment()
				response = formation_deployment_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of formation_deployment resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			formation_deployment_obj = formation_deployment()
			option_ = options()
			option_._filter=filter_
			return formation_deployment_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the formation_deployment resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			formation_deployment_obj = formation_deployment()
			option_ = options()
			option_._count=True
			response = formation_deployment_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of formation_deployment resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			formation_deployment_obj = formation_deployment()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = formation_deployment_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(formation_deployment_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.formation_deployment
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(formation_deployment_responses, response, "formation_deployment_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.formation_deployment_response_array
				i=0
				error = [formation_deployment() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.formation_deployment_response_array
			i=0
			formation_deployment_objs = [formation_deployment() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_formation_deployment'):
					for props in obj._formation_deployment:
						result = service.payload_formatter.string_to_bulk_resource(formation_deployment_response,self.__class__.__name__,props)
						formation_deployment_objs[i] = result.formation_deployment
						i=i+1
			return formation_deployment_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(formation_deployment,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class formation_deployment_response(base_response):
	def __init__(self,length=1) :
		self.formation_deployment= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.formation_deployment= [ formation_deployment() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class formation_deployment_responses(base_response):
	def __init__(self,length=1) :
		self.formation_deployment_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.formation_deployment_response_array = [ formation_deployment() for _ in range(length)]
