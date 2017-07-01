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
Configuration for Backup resource
'''

class sdx_backup_restore(base_resource):
	_ip_address_list=[]
	_name= ""
	_reset_type= ""
	_file_name= ""
	_act_id= ""
	_ip_address= ""
	_type= ""
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
			return "sdx_backup_restore"
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
			return "sdx_backup_restores"
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
	get Name of VM device
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get Reset Type [0: Reset (Without Network Configuration), 1: Reset (With Network Configuration), 2: Appliance Reset, 3: Appliance Restore, 4: Instance Restore, 5: Backup ]
	'''
	@property
	def reset_type(self) :
		try:
			return self._reset_type
		except Exception as e :
			raise e
	'''
	set Reset Type [0: Reset (Without Network Configuration), 1: Reset (With Network Configuration), 2: Appliance Reset, 3: Appliance Restore, 4: Instance Restore, 5: Backup ]
	'''
	@reset_type.setter
	def reset_type(self,reset_type):
		try :
			if not isinstance(reset_type,int):
				raise TypeError("reset_type must be set to int value")
			self._reset_type = reset_type
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
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get IP Address for this VM device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Type of device, (br | ns)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e

	'''
	Use this operation to Restore factory default.
	'''
	@classmethod
	def factoryreset(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"factoryreset")
		except Exception as e :
			raise e

	'''
	Use this operation to get backup/restore information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_backup_restore_obj=sdx_backup_restore()
				response = sdx_backup_restore_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to Restore.
	'''
	@classmethod
	def restore(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"restore")
		except Exception as e :
			raise e

	'''
	Use this operation to Backup.
	'''
	@classmethod
	def backup(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"backup")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_backup_restore resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_backup_restore_obj = sdx_backup_restore()
			option_ = options()
			option_._filter=filter_
			return sdx_backup_restore_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_backup_restore resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_backup_restore_obj = sdx_backup_restore()
			option_ = options()
			option_._count=True
			response = sdx_backup_restore_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_backup_restore resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_backup_restore_obj = sdx_backup_restore()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_backup_restore_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_backup_restore_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_backup_restore
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_backup_restore_responses, response, "sdx_backup_restore_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_backup_restore_response_array
				i=0
				error = [sdx_backup_restore() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_backup_restore_response_array
			i=0
			sdx_backup_restore_objs = [sdx_backup_restore() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_backup_restore'):
					for props in obj._sdx_backup_restore:
						result = service.payload_formatter.string_to_bulk_resource(sdx_backup_restore_response,self.__class__.__name__,props)
						sdx_backup_restore_objs[i] = result.sdx_backup_restore
						i=i+1
			return sdx_backup_restore_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_backup_restore,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_backup_restore_response(base_response):
	def __init__(self,length=1) :
		self.sdx_backup_restore= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_backup_restore= [ sdx_backup_restore() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_backup_restore_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_backup_restore_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_backup_restore_response_array = [ sdx_backup_restore() for _ in range(length)]
