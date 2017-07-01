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
Configuration for Backup File External storage resource
'''

class backup_external_storage(base_resource):
	_parent_name= ""
	_delete_from_svm= ""
	_port= ""
	_parent_id= ""
	_username= ""
	_transfer_protocol= ""
	_password= ""
	_directory_path= ""
	_server= ""
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
			return "backup_external_storage"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._server
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
			return "backup_external_storages"
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
	get Password for backup file encryption
	'''
	@property
	def delete_from_svm(self) :
		try:
			return self._delete_from_svm
		except Exception as e :
			raise e
	'''
	set Password for backup file encryption
	'''
	@delete_from_svm.setter
	def delete_from_svm(self,delete_from_svm):
		try :
			if not isinstance(delete_from_svm,bool):
				raise TypeError("delete_from_svm must be set to bool value")
			self._delete_from_svm = delete_from_svm
		except Exception as e :
			raise e


	'''
	get External transfer server port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set External transfer server port
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
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
	get Uername
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Uername
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get File transfer Protocol: SCP, SFTP or FTP
	'''
	@property
	def transfer_protocol(self) :
		try:
			return self._transfer_protocol
		except Exception as e :
			raise e
	'''
	set File transfer Protocol: SCP, SFTP or FTP
	'''
	@transfer_protocol.setter
	def transfer_protocol(self,transfer_protocol):
		try :
			if not isinstance(transfer_protocol,str):
				raise TypeError("transfer_protocol must be set to str value")
			self._transfer_protocol = transfer_protocol
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get External server directory path where backup file will be uploaded
	'''
	@property
	def directory_path(self) :
		try:
			return self._directory_path
		except Exception as e :
			raise e
	'''
	set External server directory path where backup file will be uploaded
	'''
	@directory_path.setter
	def directory_path(self,directory_path):
		try :
			if not isinstance(directory_path,str):
				raise TypeError("directory_path must be set to str value")
			self._directory_path = directory_path
		except Exception as e :
			raise e


	'''
	get External server IP Address/Hostname
	'''
	@property
	def server(self) :
		try:
			return self._server
		except Exception as e :
			raise e
	'''
	set External server IP Address/Hostname
	'''
	@server.setter
	def server(self,server):
		try :
			if not isinstance(server,str):
				raise TypeError("server must be set to str value")
			self._server = server
		except Exception as e :
			raise e

	'''
	Use this operation to display external transfer server information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				backup_external_storage_obj=backup_external_storage()
				response = backup_external_storage_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify the external transfer server information.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				backup_external_storage_obj=backup_external_storage()
				return cls.update_bulk_request(client,resource,backup_external_storage_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of backup_external_storage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			backup_external_storage_obj = backup_external_storage()
			option_ = options()
			option_._filter=filter_
			return backup_external_storage_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the backup_external_storage resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			backup_external_storage_obj = backup_external_storage()
			option_ = options()
			option_._count=True
			response = backup_external_storage_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of backup_external_storage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			backup_external_storage_obj = backup_external_storage()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = backup_external_storage_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(backup_external_storage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.backup_external_storage
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(backup_external_storage_responses, response, "backup_external_storage_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.backup_external_storage_response_array
				i=0
				error = [backup_external_storage() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.backup_external_storage_response_array
			i=0
			backup_external_storage_objs = [backup_external_storage() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_backup_external_storage'):
					for props in obj._backup_external_storage:
						result = service.payload_formatter.string_to_bulk_resource(backup_external_storage_response,self.__class__.__name__,props)
						backup_external_storage_objs[i] = result.backup_external_storage
						i=i+1
			return backup_external_storage_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(backup_external_storage,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class backup_external_storage_response(base_response):
	def __init__(self,length=1) :
		self.backup_external_storage= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.backup_external_storage= [ backup_external_storage() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class backup_external_storage_responses(base_response):
	def __init__(self,length=1) :
		self.backup_external_storage_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.backup_external_storage_response_array = [ backup_external_storage() for _ in range(length)]
