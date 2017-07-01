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
Configuration for Tenants assigned to a tenantgroup resource
'''

class tenantgroup_tenants(base_resource):
	_ref= ""
	_tenantgroup_id= ""
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
			return "/admin/v1/tenantgroups/{tenantgroup_id}/tenants"
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
			return "tenantgroup_tenants"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "tenantgroup_tenantss"
		except Exception as e :
			raise e



	'''
	get ref is the id of tenant present in tenantgroup
	'''
	@property
	def ref(self) :
		try:
			return self._ref
		except Exception as e :
			raise e
	'''
	set ref is the id of tenant present in tenantgroup
	'''
	@ref.setter
	def ref(self,ref):
		try :
			if not isinstance(ref,str):
				raise TypeError("ref must be set to str value")
			self._ref = ref
		except Exception as e :
			raise e


	'''
	get tenantgroup id in which tenants are to be added
	'''
	@property
	def tenantgroup_id(self) :
		try:
			return self._tenantgroup_id
		except Exception as e :
			raise e
	'''
	set tenantgroup id in which tenants are to be added
	'''
	@tenantgroup_id.setter
	def tenantgroup_id(self,tenantgroup_id):
		try :
			if not isinstance(tenantgroup_id,str):
				raise TypeError("tenantgroup_id must be set to str value")
			self._tenantgroup_id = tenantgroup_id
		except Exception as e :
			raise e

	'''
	Use this operation to get tenants of a tenantgroup.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tenantgroup_tenants_obj=tenantgroup_tenants()
				response = tenantgroup_tenants_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify tenants in a tenantgroup.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				tenantgroup_tenants_obj=resource[0]
				return cls.update_bulk_request(client,resource,tenantgroup_tenants_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenantgroup_tenants resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenantgroup_tenants_obj = tenantgroup_tenants()
			option_ = options()
			option_._filter=filter_
			return tenantgroup_tenants_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenantgroup_tenants resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenantgroup_tenants_obj = tenantgroup_tenants()
			option_ = options()
			option_._count=True
			response = tenantgroup_tenants_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenantgroup_tenants resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenantgroup_tenants_obj = tenantgroup_tenants()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenantgroup_tenants_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenantgroup_tenants_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenantgroup_tenants
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenantgroup_tenants_responses, response, "tenantgroup_tenants_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenantgroup_tenants_response_array
				i=0
				error = [tenantgroup_tenants() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenantgroup_tenants_response_array
			i=0
			tenantgroup_tenants_objs = [tenantgroup_tenants() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenantgroup_tenants'):
					for props in obj._tenantgroup_tenants:
						result = service.payload_formatter.string_to_bulk_resource(tenantgroup_tenants_response,self.__class__.__name__,props)
						tenantgroup_tenants_objs[i] = result.tenantgroup_tenants
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenantgroup_tenants,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenantgroup_tenants_response(base_response):
	def __init__(self,length=1) :
		self.tenantgroup_tenants= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenantgroup_tenants= [ tenantgroup_tenants() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenantgroup_tenants_responses(base_response):
	def __init__(self,length=1) :
		self.tenantgroup_tenants_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenantgroup_tenants_response_array = [ tenantgroup_tenants() for _ in range(length)]
