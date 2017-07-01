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
Configuration for Device License Info resource
'''

class device_license_info(base_resource):
	_configured_on_vm= ""
	_current_throughput= ""
	_license_pool= ""
	_allocated_on_vm= ""
	_name= ""
	_days_to_expiry= ""
	_grace= ""
	_managed_device_id= ""
	_license_state= ""
	_last_updated_time= ""
	_allocated= ""
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
			return "device_license_info"
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
			return "device_license_infos"
		except Exception as e :
			raise e



	'''
	get Configured license capacity of VM
	'''
	@property
	def configured_on_vm(self) :
		try:
			return self._configured_on_vm
		except Exception as e :
			raise e


	'''
	get Current Througput of device
	'''
	@property
	def current_throughput(self) :
		try:
			return self._current_throughput
		except Exception as e :
			raise e


	'''
	get License Pool
	'''
	@property
	def license_pool(self) :
		try:
			return self._license_pool
		except Exception as e :
			raise e


	'''
	get Running license capacity of VM
	'''
	@property
	def allocated_on_vm(self) :
		try:
			return self._allocated_on_vm
		except Exception as e :
			raise e


	'''
	get Name of managed device
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get No of days after which grace license expires
	'''
	@property
	def days_to_expiry(self) :
		try:
			return self._days_to_expiry
		except Exception as e :
			raise e


	'''
	get True if this device is managed by NMX
	'''
	@property
	def grace(self) :
		try:
			return self._grace
		except Exception as e :
			raise e


	'''
	get Device id managaed device
	'''
	@property
	def managed_device_id(self) :
		try:
			return self._managed_device_id
		except Exception as e :
			raise e


	'''
	get State of device, UP only if device accessible
	'''
	@property
	def license_state(self) :
		try:
			return self._license_state
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
			if not isinstance(last_updated_time,long):
				raise TypeError("last_updated_time must be set to long value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get Allocate license on License server
	'''
	@property
	def allocated(self) :
		try:
			return self._allocated
		except Exception as e :
			raise e


	'''
	get IP Address for this managed device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Type of device, (Xen | NS)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e

	'''
	Use this operation to get device license info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_license_info_obj=device_license_info()
				response = device_license_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_license_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_license_info_obj = device_license_info()
			option_ = options()
			option_._filter=filter_
			return device_license_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_license_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_license_info_obj = device_license_info()
			option_ = options()
			option_._count=True
			response = device_license_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_license_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_license_info_obj = device_license_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_license_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_license_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_license_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_license_info_responses, response, "device_license_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_license_info_response_array
				i=0
				error = [device_license_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_license_info_response_array
			i=0
			device_license_info_objs = [device_license_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_license_info'):
					for props in obj._device_license_info:
						result = service.payload_formatter.string_to_bulk_resource(device_license_info_response,self.__class__.__name__,props)
						device_license_info_objs[i] = result.device_license_info
						i=i+1
			return device_license_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_license_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_license_info_response(base_response):
	def __init__(self,length=1) :
		self.device_license_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_license_info= [ device_license_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_license_info_responses(base_response):
	def __init__(self,length=1) :
		self.device_license_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_license_info_response_array = [ device_license_info() for _ in range(length)]
