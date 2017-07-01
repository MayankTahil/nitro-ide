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
Configuration for tags configuration resource
'''

class tag(base_resource):
	_tag_value= ""
	_entity_id= ""
	_entity_type= ""
	_id= ""
	_tag_key= ""
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
			return "tag"
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
			return "tags"
		except Exception as e :
			raise e



	'''
	get value of the tag
	'''
	@property
	def tag_value(self) :
		try:
			return self._tag_value
		except Exception as e :
			raise e
	'''
	set value of the tag
	'''
	@tag_value.setter
	def tag_value(self,tag_value):
		try :
			if not isinstance(tag_value,str):
				raise TypeError("tag_value must be set to str value")
			self._tag_value = tag_value
		except Exception as e :
			raise e


	'''
	get Id of the entity to be tagged
	'''
	@property
	def entity_id(self) :
		try:
			return self._entity_id
		except Exception as e :
			raise e
	'''
	set Id of the entity to be tagged
	'''
	@entity_id.setter
	def entity_id(self,entity_id):
		try :
			if not isinstance(entity_id,str):
				raise TypeError("entity_id must be set to str value")
			self._entity_id = entity_id
		except Exception as e :
			raise e


	'''
	get Entity to be tagged like managed_device
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	set Entity to be tagged like managed_device
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the tags
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the tags
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
	get key of the tag
	'''
	@property
	def tag_key(self) :
		try:
			return self._tag_key
		except Exception as e :
			raise e
	'''
	set key of the tag
	'''
	@tag_key.setter
	def tag_key(self,tag_key):
		try :
			if not isinstance(tag_key,str):
				raise TypeError("tag_key must be set to str value")
			self._tag_key = tag_key
		except Exception as e :
			raise e

	'''
	Use this operation to add a tag to an entity.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				tag_obj= tag()
				return cls.perform_operation_bulk_request(service,"add", resource,tag_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete tag of an entity.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					tag_obj=tag()
					return cls.delete_bulk_request(client,resource,tag_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get tags applied on entities..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tag_obj=tag()
				response = tag_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tag_obj = tag()
			option_ = options()
			option_._filter=filter_
			return tag_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tag resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tag_obj = tag()
			option_ = options()
			option_._count=True
			response = tag_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tag resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tag_obj = tag()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tag_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tag_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tag
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tag_responses, response, "tag_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tag_response_array
				i=0
				error = [tag() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tag_response_array
			i=0
			tag_objs = [tag() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tag'):
					for props in obj._tag:
						result = service.payload_formatter.string_to_bulk_resource(tag_response,self.__class__.__name__,props)
						tag_objs[i] = result.tag
						i=i+1
			return tag_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tag,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tag_response(base_response):
	def __init__(self,length=1) :
		self.tag= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tag= [ tag() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tag_responses(base_response):
	def __init__(self,length=1) :
		self.tag_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tag_response_array = [ tag() for _ in range(length)]
