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
Configuration for Backup Policy resource
'''

class backup_policy(base_resource):
	_backup_to_retain= ""
	_enable_external_transfer= ""
	_policy_name= ""
	_external_storage_info= ""
	_backup_password= ""
	_encrypt_backup_file= ""
	_id= ""
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
			return "backup_policy"
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
			return "backup_policys"
		except Exception as e :
			raise e



	'''
	get Number of previous backups to retain
	'''
	@property
	def backup_to_retain(self) :
		try:
			return self._backup_to_retain
		except Exception as e :
			raise e
	'''
	set Number of previous backups to retain
	'''
	@backup_to_retain.setter
	def backup_to_retain(self,backup_to_retain):
		try :
			if not isinstance(backup_to_retain,int):
				raise TypeError("backup_to_retain must be set to int value")
			self._backup_to_retain = backup_to_retain
		except Exception as e :
			raise e


	'''
	get Enable transfer of backup file to external server
	'''
	@property
	def enable_external_transfer(self) :
		try:
			return self._enable_external_transfer
		except Exception as e :
			raise e
	'''
	set Enable transfer of backup file to external server
	'''
	@enable_external_transfer.setter
	def enable_external_transfer(self,enable_external_transfer):
		try :
			if not isinstance(enable_external_transfer,bool):
				raise TypeError("enable_external_transfer must be set to bool value")
			self._enable_external_transfer = enable_external_transfer
		except Exception as e :
			raise e


	'''
	get Policy Name
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set Policy Name
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
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
	get Password for backup file encryption
	'''
	@property
	def backup_password(self) :
		try:
			return self._backup_password
		except Exception as e :
			raise e
	'''
	set Password for backup file encryption
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
	get Encrypts backup files
	'''
	@property
	def encrypt_backup_file(self) :
		try:
			return self._encrypt_backup_file
		except Exception as e :
			raise e
	'''
	set Encrypts backup files
	'''
	@encrypt_backup_file.setter
	def encrypt_backup_file(self,encrypt_backup_file):
		try :
			if not isinstance(encrypt_backup_file,bool):
				raise TypeError("encrypt_backup_file must be set to bool value")
			self._encrypt_backup_file = encrypt_backup_file
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	Use this operation to get backup policy to view the number of previous backups to retain and backup file encryption details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				backup_policy_obj=backup_policy()
				response = backup_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify the number of previous backups to retain and backup file encryption details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of backup_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			backup_policy_obj = backup_policy()
			option_ = options()
			option_._filter=filter_
			return backup_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the backup_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			backup_policy_obj = backup_policy()
			option_ = options()
			option_._count=True
			response = backup_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of backup_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			backup_policy_obj = backup_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = backup_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(backup_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.backup_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(backup_policy_responses, response, "backup_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.backup_policy_response_array
				i=0
				error = [backup_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.backup_policy_response_array
			i=0
			backup_policy_objs = [backup_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_backup_policy'):
					for props in obj._backup_policy:
						result = service.payload_formatter.string_to_bulk_resource(backup_policy_response,self.__class__.__name__,props)
						backup_policy_objs[i] = result.backup_policy
						i=i+1
			return backup_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(backup_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class backup_policy_response(base_response):
	def __init__(self,length=1) :
		self.backup_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.backup_policy= [ backup_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class backup_policy_responses(base_response):
	def __init__(self,length=1) :
		self.backup_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.backup_policy_response_array = [ backup_policy() for _ in range(length)]
