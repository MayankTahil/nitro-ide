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
Configuration for Formation Template resource
'''

class formation_template(base_resource):
	_file_name= ""
	_version= ""
	_name= ""
	_author= ""
	_schema_version= ""
	_description= ""
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
			return "formation_template"
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
			return "formation_templates"
		except Exception as e :
			raise e



	'''
	get Formation template filename
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Formation template filename
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
	get Template version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Template version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Formation Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Formation Name
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
	get author
	'''
	@property
	def author(self) :
		try:
			return self._author
		except Exception as e :
			raise e
	'''
	set author
	'''
	@author.setter
	def author(self,author):
		try :
			if not isinstance(author,str):
				raise TypeError("author must be set to str value")
			self._author = author
		except Exception as e :
			raise e


	'''
	get Schema version
	'''
	@property
	def schema_version(self) :
		try:
			return self._schema_version
		except Exception as e :
			raise e
	'''
	set Schema version
	'''
	@schema_version.setter
	def schema_version(self,schema_version):
		try :
			if not isinstance(schema_version,str):
				raise TypeError("schema_version must be set to str value")
			self._schema_version = schema_version
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
	Use this operation to delete the formation templates.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					formation_template_obj=formation_template()
					return cls.delete_bulk_request(client,resource,formation_template_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get the formation templates.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				formation_template_obj=formation_template()
				response = formation_template_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of formation_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			formation_template_obj = formation_template()
			option_ = options()
			option_._filter=filter_
			return formation_template_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the formation_template resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			formation_template_obj = formation_template()
			option_ = options()
			option_._count=True
			response = formation_template_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of formation_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			formation_template_obj = formation_template()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = formation_template_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(formation_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.formation_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(formation_template_responses, response, "formation_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.formation_template_response_array
				i=0
				error = [formation_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.formation_template_response_array
			i=0
			formation_template_objs = [formation_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_formation_template'):
					for props in obj._formation_template:
						result = service.payload_formatter.string_to_bulk_resource(formation_template_response,self.__class__.__name__,props)
						formation_template_objs[i] = result.formation_template
						i=i+1
			return formation_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(formation_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class formation_template_response(base_response):
	def __init__(self,length=1) :
		self.formation_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.formation_template= [ formation_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class formation_template_responses(base_response):
	def __init__(self,length=1) :
		self.formation_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.formation_template_response_array = [ formation_template() for _ in range(length)]
