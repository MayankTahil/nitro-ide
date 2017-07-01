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
Configuration for Application Category resource
'''

class app_category(base_resource):
	_tenant_id= ""
	_is_default= ""
	_name= ""
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
			return "app_category"
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
			return "app_categorys"
		except Exception as e :
			raise e



	'''
	get Tenant Id of app_category
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of app_category
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
	get True, if this profile is system generated and can not be deleted
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	set True, if this profile is system generated and can not be deleted
	'''
	@is_default.setter
	def is_default(self,is_default):
		try :
			if not isinstance(is_default,bool):
				raise TypeError("is_default must be set to bool value")
			self._is_default = is_default
		except Exception as e :
			raise e


	'''
	get Application Category
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Application Category
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
	get Id is system generated key for all the app_category
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the app_category
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
	Use this operation to add app_category.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				app_category_obj= app_category()
				return cls.perform_operation_bulk_request(service,"add", resource,app_category_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete app_category(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					app_category_obj=app_category()
					return cls.delete_bulk_request(client,resource,app_category_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get app_category.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				app_category_obj=app_category()
				response = app_category_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify app_category.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				app_category_obj=app_category()
				return cls.update_bulk_request(client,resource,app_category_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of app_category resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			app_category_obj = app_category()
			option_ = options()
			option_._filter=filter_
			return app_category_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the app_category resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			app_category_obj = app_category()
			option_ = options()
			option_._count=True
			response = app_category_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of app_category resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			app_category_obj = app_category()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = app_category_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(app_category_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.app_category
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(app_category_responses, response, "app_category_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.app_category_response_array
				i=0
				error = [app_category() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.app_category_response_array
			i=0
			app_category_objs = [app_category() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_app_category'):
					for props in obj._app_category:
						result = service.payload_formatter.string_to_bulk_resource(app_category_response,self.__class__.__name__,props)
						app_category_objs[i] = result.app_category
						i=i+1
			return app_category_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(app_category,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class app_category_response(base_response):
	def __init__(self,length=1) :
		self.app_category= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.app_category= [ app_category() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class app_category_responses(base_response):
	def __init__(self,length=1) :
		self.app_category_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.app_category_response_array = [ app_category() for _ in range(length)]
