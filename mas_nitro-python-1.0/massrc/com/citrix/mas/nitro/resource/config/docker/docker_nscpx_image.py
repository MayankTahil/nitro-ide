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
Configuration for NetScaler CPX Image File resource
'''

class docker_nscpx_image(base_resource):
	_file_location_path= ""
	_file_size= ""
	_file_name= ""
	_file_last_modified= ""
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
			return "docker_nscpx_image"
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
			return "docker_nscpx_images"
		except Exception as e :
			raise e



	'''
	get File Location on Client for upload/download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
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
	get Last Modified
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e

	'''
	Use this operation to upload NetScaler CPX image file.
	'''

	'''
	Use this operation to upload NetScaler CPX image file.
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
	Use this operation to delete NetScaler CPX image file.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					docker_nscpx_image_obj=docker_nscpx_image()
					return cls.delete_bulk_request(client,resource,docker_nscpx_image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler CPX image file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				docker_nscpx_image_obj=docker_nscpx_image()
				response = docker_nscpx_image_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to download NetScaler CPX image file.
	'''

	'''
	Use this operation to download NetScaler CPX image file.
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
	Use this API to fetch filtered set of docker_nscpx_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			docker_nscpx_image_obj = docker_nscpx_image()
			option_ = options()
			option_._filter=filter_
			return docker_nscpx_image_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the docker_nscpx_image resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			docker_nscpx_image_obj = docker_nscpx_image()
			option_ = options()
			option_._count=True
			response = docker_nscpx_image_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of docker_nscpx_image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			docker_nscpx_image_obj = docker_nscpx_image()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = docker_nscpx_image_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(docker_nscpx_image_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.docker_nscpx_image
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(docker_nscpx_image_responses, response, "docker_nscpx_image_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.docker_nscpx_image_response_array
				i=0
				error = [docker_nscpx_image() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.docker_nscpx_image_response_array
			i=0
			docker_nscpx_image_objs = [docker_nscpx_image() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_docker_nscpx_image'):
					for props in obj._docker_nscpx_image:
						result = service.payload_formatter.string_to_bulk_resource(docker_nscpx_image_response,self.__class__.__name__,props)
						docker_nscpx_image_objs[i] = result.docker_nscpx_image
						i=i+1
			return docker_nscpx_image_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(docker_nscpx_image,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class docker_nscpx_image_response(base_response):
	def __init__(self,length=1) :
		self.docker_nscpx_image= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.docker_nscpx_image= [ docker_nscpx_image() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class docker_nscpx_image_responses(base_response):
	def __init__(self,length=1) :
		self.docker_nscpx_image_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.docker_nscpx_image_response_array = [ docker_nscpx_image() for _ in range(length)]
