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
Configuration for The image uploaded in OpenStack that should be used for provisioning new VMs. resource
'''

class image(base_resource):
	_nsm_id= ""
	_checksum= ""
	_container_format= ""
	_disk_format= ""
	_name= ""
	_id= ""
	_size= ""
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
			return "/oca/v1/images"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "images"
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
			return "image"
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
			return "images"
		except Exception as e :
			raise e



	'''
	get NSM Id of image.
	'''
	@property
	def nsm_id(self) :
		try:
			return self._nsm_id
		except Exception as e :
			raise e
	'''
	set NSM Id of image.
	'''
	@nsm_id.setter
	def nsm_id(self,nsm_id):
		try :
			if not isinstance(nsm_id,str):
				raise TypeError("nsm_id must be set to str value")
			self._nsm_id = nsm_id
		except Exception as e :
			raise e


	'''
	get Checksum of image.
	'''
	@property
	def checksum(self) :
		try:
			return self._checksum
		except Exception as e :
			raise e
	'''
	set Checksum of image.
	'''
	@checksum.setter
	def checksum(self,checksum):
		try :
			if not isinstance(checksum,str):
				raise TypeError("checksum must be set to str value")
			self._checksum = checksum
		except Exception as e :
			raise e


	'''
	get Container Format of image.
	'''
	@property
	def container_format(self) :
		try:
			return self._container_format
		except Exception as e :
			raise e
	'''
	set Container Format of image.
	'''
	@container_format.setter
	def container_format(self,container_format):
		try :
			if not isinstance(container_format,str):
				raise TypeError("container_format must be set to str value")
			self._container_format = container_format
		except Exception as e :
			raise e


	'''
	get Disk Format of image.
	'''
	@property
	def disk_format(self) :
		try:
			return self._disk_format
		except Exception as e :
			raise e
	'''
	set Disk Format of image.
	'''
	@disk_format.setter
	def disk_format(self,disk_format):
		try :
			if not isinstance(disk_format,str):
				raise TypeError("disk_format must be set to str value")
			self._disk_format = disk_format
		except Exception as e :
			raise e


	'''
	get Name of image.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of image.
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
	get Id is system generated key for image.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for image.
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
	get Size of image.
	'''
	@property
	def size(self) :
		try:
			return self._size
		except Exception as e :
			raise e
	'''
	set Size of image.
	'''
	@size.setter
	def size(self,size):
		try :
			if not isinstance(size,str):
				raise TypeError("size must be set to str value")
			self._size = size
		except Exception as e :
			raise e

	'''
	Use this operation to add image details..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				image_obj= image()
				return cls.perform_operation_bulk_request(service,"add", resource,image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to image details.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					image_obj=image()
					return cls.delete_bulk_request(client,resource,image_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get image details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				image_obj=image()
				response = image_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			image_obj = image()
			option_ = options()
			option_._filter=filter_
			return image_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the image resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			image_obj = image()
			option_ = options()
			option_._count=True
			response = image_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of image resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			image_obj = image()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = image_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(image_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.image
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(image_responses, response, "image_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.image_response_array
				i=0
				error = [image() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.image_response_array
			i=0
			image_objs = [image() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_image'):
					for props in obj._image:
						result = service.payload_formatter.string_to_bulk_resource(image_response,self.__class__.__name__,props)
						image_objs[i] = result.image
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(image,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class image_response(base_response):
	def __init__(self,length=1) :
		self.image= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.image= [ image() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class image_responses(base_response):
	def __init__(self,length=1) :
		self.image_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.image_response_array = [ image() for _ in range(length)]
