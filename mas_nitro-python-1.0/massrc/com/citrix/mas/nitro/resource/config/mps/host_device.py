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

from massrc.com.citrix.mas.nitro.resource.config.mps.managed_device import managed_device

'''
Configuration for host resource
'''

class host_device(managed_device):
	_tx= ""
	_memory_total= ""
	_ssl_cores_total= ""
	_rx= ""
	_disk_usage= ""
	_memory_usage= ""
	_disk_space= ""
	_uuid= ""
	_number_of_cpu= ""
	_disk_free= ""
	_memory_free= ""
	_cpu_usage= ""
	_enabled= ""
	_ssl_cores_free= ""
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
			return "host_device"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(host_device,self).get_object_id()
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
			return "host_devices"
		except Exception as e :
			raise e



	'''
	get Out Throughput (Mbps) of host
	'''
	@property
	def tx(self) :
		try:
			return self._tx
		except Exception as e :
			raise e


	'''
	get Total memory of host in MB
	'''
	@property
	def memory_total(self) :
		try:
			return self._memory_total
		except Exception as e :
			raise e


	'''
	get Total SSL Cores available in host
	'''
	@property
	def ssl_cores_total(self) :
		try:
			return self._ssl_cores_total
		except Exception as e :
			raise e


	'''
	get In Throughput (Mbps) of host
	'''
	@property
	def rx(self) :
		try:
			return self._rx
		except Exception as e :
			raise e


	'''
	get Disk usage (MB) for host
	'''
	@property
	def disk_usage(self) :
		try:
			return self._disk_usage
		except Exception as e :
			raise e


	'''
	get Memory Usage (%) of host
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e


	'''
	get Show Disk Space (MB) available on host
	'''
	@property
	def disk_space(self) :
		try:
			return self._disk_space
		except Exception as e :
			raise e


	'''
	get UUID of host
	'''
	@property
	def uuid(self) :
		try:
			return self._uuid
		except Exception as e :
			raise e


	'''
	get Number of total CPU of host
	'''
	@property
	def number_of_cpu(self) :
		try:
			return self._number_of_cpu
		except Exception as e :
			raise e


	'''
	get Show free Disk Space (MB) available on host
	'''
	@property
	def disk_free(self) :
		try:
			return self._disk_free
		except Exception as e :
			raise e


	'''
	get Free memory available (MB) in host
	'''
	@property
	def memory_free(self) :
		try:
			return self._memory_free
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of host
	'''
	@property
	def cpu_usage(self) :
		try:
			return self._cpu_usage
		except Exception as e :
			raise e


	'''
	get host State
	'''
	@property
	def enabled(self) :
		try:
			return self._enabled
		except Exception as e :
			raise e

	'''
	Free SSL Cores
	'''
	@property
	def ssl_cores_free(self):
		try:
			return self._ssl_cores_free
		except Exception as e :
			raise e

	'''
	Use this operation to get host.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				host_device_obj=host_device()
				response = host_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of host_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			host_device_obj = host_device()
			option_ = options()
			option_._filter=filter_
			return host_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the host_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			host_device_obj = host_device()
			option_ = options()
			option_._count=True
			response = host_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of host_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			host_device_obj = host_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = host_device_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(host_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.host_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(host_device_responses, response, "host_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.host_device_response_array
				i=0
				error = [host_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.host_device_response_array
			i=0
			host_device_objs = [host_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_host_device'):
					for props in obj._host_device:
						result = service.payload_formatter.string_to_bulk_resource(host_device_response,self.__class__.__name__,props)
						host_device_objs[i] = result.host_device
						i=i+1
			return host_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(host_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class host_device_response(base_response):
	def __init__(self,length=1) :
		self.host_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.host_device= [ host_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class host_device_responses(base_response):
	def __init__(self,length=1) :
		self.host_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.host_device_response_array = [ host_device() for _ in range(length)]
