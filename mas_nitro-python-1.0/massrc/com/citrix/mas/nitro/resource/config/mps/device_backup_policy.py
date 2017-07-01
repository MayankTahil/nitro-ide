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
Configuration for Device Backup  Policy resource
'''

class device_backup_policy(base_resource):
	_polling_interval= ""
	_backup_on_cfg_sav_trap= ""
	_device_family= ""
	_backup_password= ""
	_number_of_backups= ""
	_encrypt_backup_file= ""
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
			return "device_backup_policy"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "device_backup_policys"
		except Exception as e :
			raise e



	'''
	get Frequency of device backup in hours
	'''
	@property
	def polling_interval(self) :
		try:
			return self._polling_interval
		except Exception as e :
			raise e
	'''
	set Frequency of device backup in hours
	'''
	@polling_interval.setter
	def polling_interval(self,polling_interval):
		try :
			if not isinstance(polling_interval,int):
				raise TypeError("polling_interval must be set to int value")
			self._polling_interval = polling_interval
		except Exception as e :
			raise e


	'''
	get Backup On recieving NetscalerConfigSave trap
	'''
	@property
	def backup_on_cfg_sav_trap(self) :
		try:
			return self._backup_on_cfg_sav_trap
		except Exception as e :
			raise e
	'''
	set Backup On recieving NetscalerConfigSave trap
	'''
	@backup_on_cfg_sav_trap.setter
	def backup_on_cfg_sav_trap(self,backup_on_cfg_sav_trap):
		try :
			if not isinstance(backup_on_cfg_sav_trap,bool):
				raise TypeError("backup_on_cfg_sav_trap must be set to bool value")
			self._backup_on_cfg_sav_trap = backup_on_cfg_sav_trap
		except Exception as e :
			raise e


	'''
	get Device family whose devices need to be backed up.
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device family whose devices need to be backed up.
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
	get Number of backup files maintained per device
	'''
	@property
	def number_of_backups(self) :
		try:
			return self._number_of_backups
		except Exception as e :
			raise e
	'''
	set Number of backup files maintained per device
	'''
	@number_of_backups.setter
	def number_of_backups(self,number_of_backups):
		try :
			if not isinstance(number_of_backups,int):
				raise TypeError("number_of_backups must be set to int value")
			self._number_of_backups = number_of_backups
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
	 Use this operation to start device backup now.
	'''
	@classmethod
	def do_poll(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"do_poll")
		except Exception as e :
			raise e

	'''
	Use this operation to get the frequency of device backup.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_backup_policy_obj=device_backup_policy()
				response = device_backup_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to set the frequency of device backup.
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
	Use this API to fetch filtered set of device_backup_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_backup_policy_obj = device_backup_policy()
			option_ = options()
			option_._filter=filter_
			return device_backup_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_backup_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_backup_policy_obj = device_backup_policy()
			option_ = options()
			option_._count=True
			response = device_backup_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_backup_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_backup_policy_obj = device_backup_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_backup_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_backup_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_backup_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_backup_policy_responses, response, "device_backup_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_backup_policy_response_array
				i=0
				error = [device_backup_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_backup_policy_response_array
			i=0
			device_backup_policy_objs = [device_backup_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_backup_policy'):
					for props in obj._device_backup_policy:
						result = service.payload_formatter.string_to_bulk_resource(device_backup_policy_response,self.__class__.__name__,props)
						device_backup_policy_objs[i] = result.device_backup_policy
						i=i+1
			return device_backup_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_backup_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_backup_policy_response(base_response):
	def __init__(self,length=1) :
		self.device_backup_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_backup_policy= [ device_backup_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_backup_policy_responses(base_response):
	def __init__(self,length=1) :
		self.device_backup_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_backup_policy_response_array = [ device_backup_policy() for _ in range(length)]
