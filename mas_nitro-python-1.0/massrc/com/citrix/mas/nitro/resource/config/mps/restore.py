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
from massrc.com.citrix.mas.nitro.resource.config.mps.backup_component import backup_component


'''
Configuration for Restore resource
'''

class restore(base_resource):
	_backup_components=[]
	_act_id= ""
	_restore_type= ""
	_backup_file_name= ""
	_backup_password= ""
	_ip_address_list=[]
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
			return "restore"
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
			return "restores"
		except Exception as e :
			raise e



	'''
	get Backup Components
	'''
	@property
	def backup_components(self) :
		try:
			return self._backup_components
		except Exception as e :
			raise e
	'''
	set Backup Components
	'''
	@backup_components.setter
	def backup_components(self,backup_components) :
		try :
			if not isinstance(backup_components,list):
				raise TypeError("backup_components must be set to array of backup_component value")
			for item in backup_components :
				if not isinstance(item,backup_component):
					raise TypeError("item must be set to backup_component value")
			self._backup_components = backup_components
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get  
	'''
	@property
	def restore_type(self) :
		try:
			return self._restore_type
		except Exception as e :
			raise e
	'''
	set  
	'''
	@restore_type.setter
	def restore_type(self,restore_type):
		try :
			if not isinstance(restore_type,int):
				raise TypeError("restore_type must be set to int value")
			self._restore_type = restore_type
		except Exception as e :
			raise e


	'''
	get Backup file name
	'''
	@property
	def backup_file_name(self) :
		try:
			return self._backup_file_name
		except Exception as e :
			raise e
	'''
	set Backup file name
	'''
	@backup_file_name.setter
	def backup_file_name(self,backup_file_name):
		try :
			if not isinstance(backup_file_name,str):
				raise TypeError("backup_file_name must be set to str value")
			self._backup_file_name = backup_file_name
		except Exception as e :
			raise e


	'''
	get Password of encrypted backup file
	'''
	@property
	def backup_password(self) :
		try:
			return self._backup_password
		except Exception as e :
			raise e
	'''
	set Password of encrypted backup file
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
	get List of VM IP Address
	'''
	@property
	def ip_address_list(self) :
		try:
			return self._ip_address_list
		except Exception as e :
			raise e
	'''
	set List of VM IP Address
	'''
	@ip_address_list.setter
	def ip_address_list(self,ip_address_list) :
		try :
			if not isinstance(ip_address_list,list):
				raise TypeError("ip_address_list must be set to array of str value")
			for item in ip_address_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ip_address_list = ip_address_list
		except Exception as e :
			raise e

	'''
	Use this operation to restore the Appliance.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				restore_obj= restore()
				return cls.perform_operation_bulk_request(service,"add", resource,restore_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get restore component information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				restore_obj=restore()
				response = restore_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of restore resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			restore_obj = restore()
			option_ = options()
			option_._filter=filter_
			return restore_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the restore resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			restore_obj = restore()
			option_ = options()
			option_._count=True
			response = restore_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of restore resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			restore_obj = restore()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = restore_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(restore_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.restore
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(restore_responses, response, "restore_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.restore_response_array
				i=0
				error = [restore() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.restore_response_array
			i=0
			restore_objs = [restore() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_restore'):
					for props in obj._restore:
						result = service.payload_formatter.string_to_bulk_resource(restore_response,self.__class__.__name__,props)
						restore_objs[i] = result.restore
						i=i+1
			return restore_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(restore,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class restore_response(base_response):
	def __init__(self,length=1) :
		self.restore= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.restore= [ restore() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class restore_responses(base_response):
	def __init__(self,length=1) :
		self.restore_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.restore_response_array = [ restore() for _ in range(length)]
