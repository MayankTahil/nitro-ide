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
Configuration for CBSDX Single Bundle Build File resource
'''

class cb_sb_image(base_resource):
	_file_size= ""
	_modified_timestamp= ""
	_file_name= ""
	_is_dir= ""
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
			return "cb_sb_image"
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
			return "cb_sb_images"
		except Exception as e :
			raise e



	'''
	get file_size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get Last Modified
	'''
	@property
	def modified_timestamp(self) :
		try:
			return self._modified_timestamp
		except Exception as e :
			raise e


	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
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
	get Is the file a directory?
	'''
	@property
	def is_dir(self) :
		try:
			return self._is_dir
		except Exception as e :
			raise e
	'''
	set Is the file a directory?
	'''
	@is_dir.setter
	def is_dir(self,is_dir):
		try :
			if not isinstance(is_dir,bool):
				raise TypeError("is_dir must be set to bool value")
			self._is_dir = is_dir
		except Exception as e :
			raise e

	'''
	Use this operation to upload build file.
	'''

	'''
	Use this operation to upload build file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to delete build file.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					cb_sb_image_obj=cb_sb_image()
					return cls.delete_bulk_request(client,resource,cb_sb_image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get build file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cb_sb_image_obj=cb_sb_image()
				response = cb_sb_image_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to download build file.
	'''

	'''
	Use this operation to download build file.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cb_sb_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cb_sb_image_obj = cb_sb_image()
			option_ = options()
			option_._filter=filter_
			return cb_sb_image_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cb_sb_image resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cb_sb_image_obj = cb_sb_image()
			option_ = options()
			option_._count=True
			response = cb_sb_image_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cb_sb_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cb_sb_image_obj = cb_sb_image()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cb_sb_image_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cb_sb_image_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cb_sb_image
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cb_sb_image_responses, response, "cb_sb_image_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cb_sb_image_response_array
				i=0
				error = [cb_sb_image() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cb_sb_image_response_array
			i=0
			cb_sb_image_objs = [cb_sb_image() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cb_sb_image'):
					for props in obj._cb_sb_image:
						result = service.payload_formatter.string_to_bulk_resource(cb_sb_image_response,self.__class__.__name__,props)
						cb_sb_image_objs[i] = result.cb_sb_image
						i=i+1
			return cb_sb_image_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cb_sb_image,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cb_sb_image_response(base_response):
	def __init__(self,length=1) :
		self.cb_sb_image= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cb_sb_image= [ cb_sb_image() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cb_sb_image_responses(base_response):
	def __init__(self,length=1) :
		self.cb_sb_image_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cb_sb_image_response_array = [ cb_sb_image() for _ in range(length)]
