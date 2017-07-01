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
Configuration for Entity Tags resource
'''

class entity_tags(base_resource):
	_tag_value= ""
	_parent_name= ""
	_id= ""
	_tag_key= ""
	_parent_id= ""
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
			return "entity_tags"
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
			return "entity_tagss"
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
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(entity_tags_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.entity_tags
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(entity_tags_responses, response, "entity_tags_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.entity_tags_response_array
				i=0
				error = [entity_tags() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.entity_tags_response_array
			i=0
			entity_tags_objs = [entity_tags() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_entity_tags'):
					for props in obj._entity_tags:
						result = service.payload_formatter.string_to_bulk_resource(entity_tags_response,self.__class__.__name__,props)
						entity_tags_objs[i] = result.entity_tags
						i=i+1
			return entity_tags_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(entity_tags,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class entity_tags_response(base_response):
	def __init__(self,length=1) :
		self.entity_tags= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.entity_tags= [ entity_tags() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class entity_tags_responses(base_response):
	def __init__(self,length=1) :
		self.entity_tags_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.entity_tags_response_array = [ entity_tags() for _ in range(length)]
