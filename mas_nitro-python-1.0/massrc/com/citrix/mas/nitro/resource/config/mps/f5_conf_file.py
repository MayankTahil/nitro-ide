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
Configuration for f5 Configuration File resource
'''

class f5_conf_file(base_resource):
	_file_location_path= ""
	_file_size= ""
	_file_name= ""
	_file_last_modified= ""
	_is_main= ""
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
			return "f5_conf_file"
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
			return "f5_conf_file"
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
	get File Size
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
	get File Location on Client for upload/download
	'''
	@property
	def is_main(self) :
		try:
			return self._is_main
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
	'''
	@is_main.setter
	def is_main(self,is_main):
		try :
			if not isinstance(is_main,bool):
				raise TypeError("is_main must be set to bool value")
			self._is_main = is_main
		except Exception as e :
			raise e

	'''
	Use this operation to upload  f5 config file.
	'''

	'''
	Use this operation to upload  f5 config file.
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
	Use this operation to f5 config files.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					f5_conf_file_obj=f5_conf_file()
					return cls.delete_bulk_request(client,resource,f5_conf_file_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get f5 config files.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				f5_conf_file_obj=f5_conf_file()
				response = f5_conf_file_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to f5 config files.
	'''

	'''
	Use this operation to f5 config files.
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
	Use this API to fetch filtered set of f5_conf_file resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			f5_conf_file_obj = f5_conf_file()
			option_ = options()
			option_._filter=filter_
			return f5_conf_file_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the f5_conf_file resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			f5_conf_file_obj = f5_conf_file()
			option_ = options()
			option_._count=True
			response = f5_conf_file_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of f5_conf_file resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			f5_conf_file_obj = f5_conf_file()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = f5_conf_file_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(f5_conf_file_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.f5_conf_file
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(f5_conf_file_responses, response, "f5_conf_file_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.f5_conf_file_response_array
				i=0
				error = [f5_conf_file() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.f5_conf_file_response_array
			i=0
			f5_conf_file_objs = [f5_conf_file() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_f5_conf_file'):
					for props in obj._f5_conf_file:
						result = service.payload_formatter.string_to_bulk_resource(f5_conf_file_response,self.__class__.__name__,props)
						f5_conf_file_objs[i] = result.f5_conf_file
						i=i+1
			return f5_conf_file_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(f5_conf_file,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class f5_conf_file_response(base_response):
	def __init__(self,length=1) :
		self.f5_conf_file= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.f5_conf_file= [ f5_conf_file() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class f5_conf_file_responses(base_response):
	def __init__(self,length=1) :
		self.f5_conf_file_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.f5_conf_file_response_array = [ f5_conf_file() for _ in range(length)]
