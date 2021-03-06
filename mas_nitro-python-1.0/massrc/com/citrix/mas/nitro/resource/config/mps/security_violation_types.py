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
Configuration for This table holds info of various violations types  resource
'''

class security_violation_types(base_resource):
	_violation_category= ""
	_id= ""
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
			return "security_violation_types"
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
			return "security_violation_typess"
		except Exception as e :
			raise e



	'''
	get Violation Category
	'''
	@property
	def violation_category(self) :
		try:
			return self._violation_category
		except Exception as e :
			raise e
	'''
	set Violation Category
	'''
	@violation_category.setter
	def violation_category(self,violation_category):
		try :
			if not isinstance(violation_category,int):
				raise TypeError("violation_category must be set to int value")
			self._violation_category = violation_category
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the managed devices
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the managed devices
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
	get Violation Type Description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Violation Type Description
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
	Use this operation to delete a property.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					security_violation_types_obj=security_violation_types()
					return cls.delete_bulk_request(client,resource,security_violation_types_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get a value for a violation type based on Id..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				security_violation_types_obj=security_violation_types()
				response = security_violation_types_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of security_violation_types resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			security_violation_types_obj = security_violation_types()
			option_ = options()
			option_._filter=filter_
			return security_violation_types_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the security_violation_types resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			security_violation_types_obj = security_violation_types()
			option_ = options()
			option_._count=True
			response = security_violation_types_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of security_violation_types resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			security_violation_types_obj = security_violation_types()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = security_violation_types_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(security_violation_types_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.security_violation_types
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(security_violation_types_responses, response, "security_violation_types_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.security_violation_types_response_array
				i=0
				error = [security_violation_types() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.security_violation_types_response_array
			i=0
			security_violation_types_objs = [security_violation_types() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_security_violation_types'):
					for props in obj._security_violation_types:
						result = service.payload_formatter.string_to_bulk_resource(security_violation_types_response,self.__class__.__name__,props)
						security_violation_types_objs[i] = result.security_violation_types
						i=i+1
			return security_violation_types_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(security_violation_types,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class security_violation_types_response(base_response):
	def __init__(self,length=1) :
		self.security_violation_types= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.security_violation_types= [ security_violation_types() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class security_violation_types_responses(base_response):
	def __init__(self,length=1) :
		self.security_violation_types_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.security_violation_types_response_array = [ security_violation_types() for _ in range(length)]
