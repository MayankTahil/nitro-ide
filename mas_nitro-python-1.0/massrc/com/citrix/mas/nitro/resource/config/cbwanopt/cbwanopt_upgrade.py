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
Configuration for Upgrade CBWANOPT resource
'''

class cbwanopt_upgrade(base_resource):
	_device_groups=[]
	_sdx_ip_address_arr=[]
	_image_name= ""
	_on_error= ""
	_execute_sequentially= ""
	_task_id= ""
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
			return "cbwanopt_upgrade"
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
			return "cbwanopt_upgrades"
		except Exception as e :
			raise e



	'''
	get Device Group Array on which for which job is run
	'''
	@property
	def device_groups(self) :
		try:
			return self._device_groups
		except Exception as e :
			raise e
	'''
	set Device Group Array on which for which job is run
	'''
	@device_groups.setter
	def device_groups(self,device_groups) :
		try :
			if not isinstance(device_groups,list):
				raise TypeError("device_groups must be set to array of str value")
			for item in device_groups :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_groups = device_groups
		except Exception as e :
			raise e


	'''
	get List of CloudBridge WAN Optimization device IP Address
	'''
	@property
	def sdx_ip_address_arr(self) :
		try:
			return self._sdx_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of CloudBridge WAN Optimization device IP Address
	'''
	@sdx_ip_address_arr.setter
	def sdx_ip_address_arr(self,sdx_ip_address_arr) :
		try :
			if not isinstance(sdx_ip_address_arr,list):
				raise TypeError("sdx_ip_address_arr must be set to array of str value")
			for item in sdx_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._sdx_ip_address_arr = sdx_ip_address_arr
		except Exception as e :
			raise e


	'''
	get image_name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set image_name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
	'''
	@on_error.setter
	def on_error(self,on_error):
		try :
			if not isinstance(on_error,str):
				raise TypeError("on_error must be set to str value")
			self._on_error = on_error
		except Exception as e :
			raise e


	'''
	get True if configuration template is to be applied to devices sequentially
	'''
	@property
	def execute_sequentially(self) :
		try:
			return self._execute_sequentially
		except Exception as e :
			raise e
	'''
	set True if configuration template is to be applied to devices sequentially
	'''
	@execute_sequentially.setter
	def execute_sequentially(self,execute_sequentially):
		try :
			if not isinstance(execute_sequentially,bool):
				raise TypeError("execute_sequentially must be set to bool value")
			self._execute_sequentially = execute_sequentially
		except Exception as e :
			raise e


	'''
	get Task ID
	'''
	@property
	def task_id(self) :
		try:
			return self._task_id
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade CBWANOPT.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"upgrade")
			else : 
				cbwanopt_upgrade_obj= cbwanopt_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade", resource,cbwanopt_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cbwanopt_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cbwanopt_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cbwanopt_upgrade_responses, response, "cbwanopt_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cbwanopt_upgrade_response_array
				i=0
				error = [cbwanopt_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cbwanopt_upgrade_response_array
			i=0
			cbwanopt_upgrade_objs = [cbwanopt_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cbwanopt_upgrade'):
					for props in obj._cbwanopt_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(cbwanopt_upgrade_response,self.__class__.__name__,props)
						cbwanopt_upgrade_objs[i] = result.cbwanopt_upgrade
						i=i+1
			return cbwanopt_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cbwanopt_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cbwanopt_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cbwanopt_upgrade= [ cbwanopt_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cbwanopt_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cbwanopt_upgrade_response_array = [ cbwanopt_upgrade() for _ in range(length)]
