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
from massrc.com.citrix.mas.nitro.resource.config.admin.platformspecs import platformspecs


'''
Configuration for Rescources in a device resource
'''

class spec(base_resource):
	_platformspec= ""
	_ha= ""
	_model= ""
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
			return "/admin/v1/specs"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "specs"
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
			return "spec"
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
			return "specs"
		except Exception as e :
			raise e



	'''
	get platform spec
	'''
	@property
	def platformspec(self) :
		try:
			return self._platformspec
		except Exception as e :
			raise e
	'''
	set platform spec
	'''
	@platformspec.setter
	def platformspec(self,platformspec):
		try :
			if not isinstance(platformspec,platformspecs):
				raise TypeError("platformspec must be set to platformspecs value")
			self._platformspec = platformspec
		except Exception as e :
			raise e


	'''
	get HA
	'''
	@property
	def ha(self) :
		try:
			return self._ha
		except Exception as e :
			raise e
	'''
	set HA
	'''
	@ha.setter
	def ha(self,ha):
		try :
			if not isinstance(ha,bool):
				raise TypeError("ha must be set to bool value")
			self._ha = ha
		except Exception as e :
			raise e


	'''
	get Model
	'''
	@property
	def model(self) :
		try:
			return self._model
		except Exception as e :
			raise e
	'''
	set Model
	'''
	@model.setter
	def model(self,model):
		try :
			if not isinstance(model,str):
				raise TypeError("model must be set to str value")
			self._model = model
		except Exception as e :
			raise e


	'''
	get Id is system generated key for partition specs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for partition specs
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
	Use this operation to add tenantgroups.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				spec_obj= spec()
				return cls.perform_operation_bulk_request(service,"add", resource,spec_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a tenantgroup.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					spec_obj=spec()
					return cls.delete_bulk_request(client,resource,spec_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get tenantgroups' details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				spec_obj=spec()
				response = spec_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify tenantgroup details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				spec_obj=resource[0]
				return cls.update_bulk_request(client,resource,spec_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of spec resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			spec_obj = spec()
			option_ = options()
			option_._filter=filter_
			return spec_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the spec resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			spec_obj = spec()
			option_ = options()
			option_._count=True
			response = spec_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of spec resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			spec_obj = spec()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = spec_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(spec_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.spec
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(spec_responses, response, "spec_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.spec_response_array
				i=0
				error = [spec() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.spec_response_array
			i=0
			spec_objs = [spec() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_spec'):
					for props in obj._spec:
						result = service.payload_formatter.string_to_bulk_resource(spec_response,self.__class__.__name__,props)
						spec_objs[i] = result.spec
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(spec,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class spec_response(base_response):
	def __init__(self,length=1) :
		self.spec= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.spec= [ spec() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class spec_responses(base_response):
	def __init__(self,length=1) :
		self.spec_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.spec_response_array = [ spec() for _ in range(length)]
