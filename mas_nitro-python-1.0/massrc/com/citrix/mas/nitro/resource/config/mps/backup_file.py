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
from massrc.com.citrix.mas.nitro.resource.config.mps.backup_external_storage import backup_external_storage


'''
Configuration for Backup files resource
'''

class backup_file(base_resource):
	_encrypted= ""
	_file_location_path= ""
	_file_size= ""
	_external_storage_info= ""
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
			return "backup_file"
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
			return "backup"
		except Exception as e :
			raise e



	'''
	get Encrypted backup files
	'''
	@property
	def encrypted(self) :
		try:
			return self._encrypted
		except Exception as e :
			raise e
	'''
	set Encrypted backup files
	'''
	@encrypted.setter
	def encrypted(self,encrypted):
		try :
			if not isinstance(encrypted,bool):
				raise TypeError("encrypted must be set to bool value")
			self._encrypted = encrypted
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
	get Information of the External storage for backup file
	'''
	@property
	def external_storage_info(self) :
		try:
			return self._external_storage_info
		except Exception as e :
			raise e
	'''
	set Information of the External storage for backup file
	'''
	@external_storage_info.setter
	def external_storage_info(self,external_storage_info):
		try :
			if not isinstance(external_storage_info,backup_external_storage):
				raise TypeError("external_storage_info must be set to backup_external_storage value")
			self._external_storage_info = external_storage_info
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
	Use this operation to upload  backup file.
	'''

	'''
	Use this operation to upload  backup file.
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
	Use this operation to delete backup file.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					backup_file_obj=backup_file()
					return cls.delete_bulk_request(client,resource,backup_file_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get backup file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				backup_file_obj=backup_file()
				response = backup_file_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to download backup file.
	'''

	'''
	Use this operation to download backup file.
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
	Use this API to fetch filtered set of backup_file resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			backup_file_obj = backup_file()
			option_ = options()
			option_._filter=filter_
			return backup_file_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the backup_file resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			backup_file_obj = backup_file()
			option_ = options()
			option_._count=True
			response = backup_file_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of backup_file resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			backup_file_obj = backup_file()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = backup_file_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(backup_file_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.backup_file
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(backup_file_responses, response, "backup_file_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.backup_file_response_array
				i=0
				error = [backup_file() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.backup_file_response_array
			i=0
			backup_file_objs = [backup_file() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_backup_file'):
					for props in obj._backup_file:
						result = service.payload_formatter.string_to_bulk_resource(backup_file_response,self.__class__.__name__,props)
						backup_file_objs[i] = result.backup_file
						i=i+1
			return backup_file_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(backup_file,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class backup_file_response(base_response):
	def __init__(self,length=1) :
		self.backup_file= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.backup_file= [ backup_file() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class backup_file_responses(base_response):
	def __init__(self,length=1) :
		self.backup_file_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.backup_file_response_array = [ backup_file() for _ in range(length)]
