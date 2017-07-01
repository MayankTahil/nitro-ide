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
Configuration for remote backup resource
'''

class remote_backup(base_resource):
	_password= ""
	_name= ""
	_username= ""
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
			return "remote_backup"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "remote_backups"
		except Exception as e :
			raise e



	'''
	get Password of the Remote backup VM
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password of the Remote backup VM
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
	get Backup node IP Address
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Backup node IP Address
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
	get User Name of the Remote backup VM
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set User Name of the Remote backup VM
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
	Use this operation to add the backup nodes to db.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				remote_backup_obj= remote_backup()
				return cls.perform_operation_bulk_request(service,"add", resource,remote_backup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get backup nodes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				remote_backup_obj=remote_backup()
				response = remote_backup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of remote_backup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			remote_backup_obj = remote_backup()
			option_ = options()
			option_._filter=filter_
			return remote_backup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the remote_backup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			remote_backup_obj = remote_backup()
			option_ = options()
			option_._count=True
			response = remote_backup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of remote_backup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			remote_backup_obj = remote_backup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = remote_backup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(remote_backup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.remote_backup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(remote_backup_responses, response, "remote_backup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.remote_backup_response_array
				i=0
				error = [remote_backup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.remote_backup_response_array
			i=0
			remote_backup_objs = [remote_backup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_remote_backup'):
					for props in obj._remote_backup:
						result = service.payload_formatter.string_to_bulk_resource(remote_backup_response,self.__class__.__name__,props)
						remote_backup_objs[i] = result.remote_backup
						i=i+1
			return remote_backup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(remote_backup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class remote_backup_response(base_response):
	def __init__(self,length=1) :
		self.remote_backup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.remote_backup= [ remote_backup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class remote_backup_responses(base_response):
	def __init__(self,length=1) :
		self.remote_backup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.remote_backup_response_array = [ remote_backup() for _ in range(length)]
