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

from massrc.com.citrix.mas.nitro.resource.config.mps.host_device import host_device

'''
Configuration for SDX resource
'''

class sdx(host_device):
	_max_throughput= ""
	_current_time= ""
	_bios_version= ""
	_hostid= ""
	_available_throughput= ""
	_build_number= ""
	_max_number_of_instances= ""
	_product= ""
	_platform= ""
	_available_number_of_instances= ""
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
			return "sdx"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(sdx,self).get_object_id()
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
			return "sdxs"
		except Exception as e :
			raise e



	'''
	get Maximum Throughput in Mbps
	'''
	@property
	def max_throughput(self) :
		try:
			return self._max_throughput
		except Exception as e :
			raise e


	'''
	get Current Time
	'''
	@property
	def current_time(self) :
		try:
			return self._current_time
		except Exception as e :
			raise e


	'''
	get BIOS Version
	'''
	@property
	def bios_version(self) :
		try:
			return self._bios_version
		except Exception as e :
			raise e


	'''
	get Host Id
	'''
	@property
	def hostid(self) :
		try:
			return self._hostid
		except Exception as e :
			raise e


	'''
	get Available Throughput in Mbps
	'''
	@property
	def available_throughput(self) :
		try:
			return self._available_throughput
		except Exception as e :
			raise e


	'''
	get Build Number
	'''
	@property
	def build_number(self) :
		try:
			return self._build_number
		except Exception as e :
			raise e


	'''
	get Maximum Instances
	'''
	@property
	def max_number_of_instances(self) :
		try:
			return self._max_number_of_instances
		except Exception as e :
			raise e


	'''
	get Product Name
	'''
	@property
	def product(self) :
		try:
			return self._product
		except Exception as e :
			raise e


	'''
	get Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e


	'''
	get Available Instances
	'''
	@property
	def available_number_of_instances(self) :
		try:
			return self._available_number_of_instances
		except Exception as e :
			raise e

	'''
	Use this operation to unmanage SDX device.
	'''

	'''
	Use this operation to unmanage SDX device.
	'''
	@classmethod
	def unmanage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"unmanage")
			else : 
				sdx_obj= sdx()
				return cls.perform_operation_bulk_request(service,"unmanage", resource,sdx_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to reboot SDX device.
	'''

	'''
	Use this operation to reboot SDX device.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"reboot")
			else : 
				sdx_obj= sdx()
				return cls.perform_operation_bulk_request(service,"reboot", resource,sdx_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add SDX device.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				sdx_obj= sdx()
				return cls.perform_operation_bulk_request(service,"add", resource,sdx_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete SDX device.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					sdx_obj=sdx()
					return cls.delete_bulk_request(client,resource,sdx_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get SDX device .
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_obj=sdx()
				response = sdx_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to manage SDX device.
	'''

	'''
	Use this operation to manage SDX device.
	'''
	@classmethod
	def manage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"manage")
			else : 
				sdx_obj= sdx()
				return cls.perform_operation_bulk_request(service,"manage", resource,sdx_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_obj = sdx()
			option_ = options()
			option_._filter=filter_
			return sdx_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_obj = sdx()
			option_ = options()
			option_._count=True
			response = sdx_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_obj = sdx()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_responses, response, "sdx_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_response_array
				i=0
				error = [sdx() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_response_array
			i=0
			sdx_objs = [sdx() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx'):
					for props in obj._sdx:
						result = service.payload_formatter.string_to_bulk_resource(sdx_response,self.__class__.__name__,props)
						sdx_objs[i] = result.sdx
						i=i+1
			return sdx_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_response(base_response):
	def __init__(self,length=1) :
		self.sdx= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx= [ sdx() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_response_array = [ sdx() for _ in range(length)]
