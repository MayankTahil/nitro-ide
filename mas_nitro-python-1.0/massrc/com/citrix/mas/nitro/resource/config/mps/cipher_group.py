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
Configuration for Cipher Group resource
'''

class cipher_group(base_resource):
	_cipher_group_description= ""
	_is_applied= ""
	_cipher_group_name= ""
	_is_predefined= ""
	_cipher_name_list_array=[]
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
			return "cipher_group"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._cipher_group_name
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
			return "cipher_groups"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def cipher_group_description(self) :
		try:
			return self._cipher_group_description
		except Exception as e :
			raise e
	'''
	set 
	'''
	@cipher_group_description.setter
	def cipher_group_description(self,cipher_group_description):
		try :
			if not isinstance(cipher_group_description,str):
				raise TypeError("cipher_group_description must be set to str value")
			self._cipher_group_description = cipher_group_description
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def is_applied(self) :
		try:
			return self._is_applied
		except Exception as e :
			raise e
	'''
	set 
	'''
	@is_applied.setter
	def is_applied(self,is_applied):
		try :
			if not isinstance(is_applied,bool):
				raise TypeError("is_applied must be set to bool value")
			self._is_applied = is_applied
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def cipher_group_name(self) :
		try:
			return self._cipher_group_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@cipher_group_name.setter
	def cipher_group_name(self,cipher_group_name):
		try :
			if not isinstance(cipher_group_name,str):
				raise TypeError("cipher_group_name must be set to str value")
			self._cipher_group_name = cipher_group_name
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def is_predefined(self) :
		try:
			return self._is_predefined
		except Exception as e :
			raise e
	'''
	set 
	'''
	@is_predefined.setter
	def is_predefined(self,is_predefined):
		try :
			if not isinstance(is_predefined,bool):
				raise TypeError("is_predefined must be set to bool value")
			self._is_predefined = is_predefined
		except Exception as e :
			raise e

	'''
	list of cipher suites in form of array of strings
	'''
	@property
	def cipher_name_list_array(self) :
		try:
			return self._cipher_name_list_array
		except Exception as e :
			raise e
	'''
	list of cipher suites in form of array of strings
	'''
	@cipher_name_list_array.setter
	def cipher_name_list_array(self,cipher_name_list_array) :
		try :
			if not isinstance(cipher_name_list_array,list):
				raise TypeError("cipher_name_list_array must be set to array of str value")
			for item in cipher_name_list_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._cipher_name_list_array = cipher_name_list_array
		except Exception as e :
			raise e

	'''
	Use this operation to add a Cipher Group.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				cipher_group_obj= cipher_group()
				return cls.perform_operation_bulk_request(service,"add", resource,cipher_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Cipher Group(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					cipher_group_obj=cipher_group()
					return cls.delete_bulk_request(client,resource,cipher_group_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Cipher Group details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cipher_group_obj=cipher_group()
				response = cipher_group_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a Cipher Group.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				cipher_group_obj=cipher_group()
				return cls.update_bulk_request(client,resource,cipher_group_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cipher_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cipher_group_obj = cipher_group()
			option_ = options()
			option_._filter=filter_
			return cipher_group_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cipher_group resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cipher_group_obj = cipher_group()
			option_ = options()
			option_._count=True
			response = cipher_group_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cipher_group resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cipher_group_obj = cipher_group()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cipher_group_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cipher_group_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cipher_group
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cipher_group_responses, response, "cipher_group_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cipher_group_response_array
				i=0
				error = [cipher_group() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cipher_group_response_array
			i=0
			cipher_group_objs = [cipher_group() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cipher_group'):
					for props in obj._cipher_group:
						result = service.payload_formatter.string_to_bulk_resource(cipher_group_response,self.__class__.__name__,props)
						cipher_group_objs[i] = result.cipher_group
						i=i+1
			return cipher_group_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cipher_group,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cipher_group_response(base_response):
	def __init__(self,length=1) :
		self.cipher_group= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cipher_group= [ cipher_group() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cipher_group_responses(base_response):
	def __init__(self,length=1) :
		self.cipher_group_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cipher_group_response_array = [ cipher_group() for _ in range(length)]
