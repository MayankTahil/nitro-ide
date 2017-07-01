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
Configuration for Device Backup resource
'''

class device_backup(base_resource):
	_device_family= ""
	_image_filesize= ""
	_last_updated_time= ""
	_backup_filesize= ""
	_tenant_id= ""
	_device_name= ""
	_image_filename= ""
	_backup_filename= ""
	_id= ""
	_ip_address= ""
	_encrypted= ""
	_act_id= ""
	_backup_password= ""
	_use_global_password= ""
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
			return "device_backup"
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
			return "device_backups"
		except Exception as e :
			raise e



	'''
	get Device family.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device family.
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Image File Size
	'''
	@property
	def image_filesize(self) :
		try:
			return self._image_filesize
		except Exception as e :
			raise e
	'''
	set Image File Size
	'''
	@image_filesize.setter
	def image_filesize(self,image_filesize):
		try :
			if not isinstance(image_filesize,int):
				raise TypeError("image_filesize must be set to int value")
			self._image_filesize = image_filesize
		except Exception as e :
			raise e


	'''
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
		except Exception as e :
			raise e
	'''
	set Last Updated Time
	'''
	@last_updated_time.setter
	def last_updated_time(self,last_updated_time):
		try :
			if not isinstance(last_updated_time,int):
				raise TypeError("last_updated_time must be set to int value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get Backup file size
	'''
	@property
	def backup_filesize(self) :
		try:
			return self._backup_filesize
		except Exception as e :
			raise e
	'''
	set Backup file size
	'''
	@backup_filesize.setter
	def backup_filesize(self,backup_filesize):
		try :
			if not isinstance(backup_filesize,int):
				raise TypeError("backup_filesize must be set to int value")
			self._backup_filesize = backup_filesize
		except Exception as e :
			raise e


	'''
	get Tenant ID
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Device Hostname
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
		except Exception as e :
			raise e


	'''
	get Name of the image file backed up
	'''
	@property
	def image_filename(self) :
		try:
			return self._image_filename
		except Exception as e :
			raise e


	'''
	get Name of the backed up file
	'''
	@property
	def backup_filename(self) :
		try:
			return self._backup_filename
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all backed up files
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all backed up files
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
	get Device IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Indicates if the backup files are encrypted
	'''
	@property
	def encrypted(self):
		try:
			return self._encrypted
		except Exception as e :
			raise e
	'''
	Indicates if the backup files are encrypted
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
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	Backup Password
	'''
	@property
	def backup_password(self):
		try:
			return self._backup_password
		except Exception as e :
			raise e
	'''
	Backup Password
	'''
	@backup_password.setter
	def backup_password(self,backup_password):
		try :
			if not isinstance(backup_password,str):
				raise TypeError("backup_password must be set to str value")
			self._backup_password = backup_password
		except Exception as e :
			raise e

	'''
	Global Password
	'''
	@property
	def use_global_password(self):
		try:
			return self._use_global_password
		except Exception as e :
			raise e
	'''
	Global Password
	'''
	@use_global_password.setter
	def use_global_password(self,use_global_password):
		try :
			if not isinstance(use_global_password,bool):
				raise TypeError("use_global_password must be set to bool value")
			self._use_global_password = use_global_password
		except Exception as e :
			raise e

	'''
	Use this operation to poll all backup  file from a device and updated the database.
	'''

	'''
	Use this operation to poll all backup  file from a device and updated the database.
	'''
	@classmethod
	def devicebackup(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"devicebackup")
			else : 
				device_backup_obj= device_backup()
				return cls.perform_operation_bulk_request(service,"devicebackup", resource,device_backup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload backed up file.
	'''

	'''
	Use this operation to upload backed up file.
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
	Use this operation to delete NetScaler configuration template.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					device_backup_obj=device_backup()
					return cls.delete_bulk_request(client,resource,device_backup_obj)
		except Exception as e :
			raise e

	'''
	Get backed up files of devices.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_backup_obj=device_backup()
				response = device_backup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to restore backed up file.
	'''

	'''
	Use this operation to restore backed up file.
	'''
	@classmethod
	def devicerestore(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"devicerestore")
			else : 
				device_backup_obj= device_backup()
				return cls.perform_operation_bulk_request(service,"devicerestore", resource,device_backup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download backed up file.
	'''

	'''
	Use this operation to download backed up file.
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
	Use this API to fetch filtered set of device_backup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_backup_obj = device_backup()
			option_ = options()
			option_._filter=filter_
			return device_backup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_backup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_backup_obj = device_backup()
			option_ = options()
			option_._count=True
			response = device_backup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_backup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_backup_obj = device_backup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_backup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_backup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_backup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_backup_responses, response, "device_backup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_backup_response_array
				i=0
				error = [device_backup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_backup_response_array
			i=0
			device_backup_objs = [device_backup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_backup'):
					for props in obj._device_backup:
						result = service.payload_formatter.string_to_bulk_resource(device_backup_response,self.__class__.__name__,props)
						device_backup_objs[i] = result.device_backup
						i=i+1
			return device_backup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_backup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_backup_response(base_response):
	def __init__(self,length=1) :
		self.device_backup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_backup= [ device_backup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_backup_responses(base_response):
	def __init__(self,length=1) :
		self.device_backup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_backup_response_array = [ device_backup() for _ in range(length)]
