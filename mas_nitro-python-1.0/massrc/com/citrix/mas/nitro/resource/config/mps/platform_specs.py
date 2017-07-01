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
Configuration for Platform Specification resource
'''

class platform_specs(base_resource):
	_is_fips_present= ""
	_contains_fortville_nics= ""
	_max_channels= ""
	_max_cores_per_vm= ""
	_is_nextgen= ""
	_no_of_mgmt_interfaces= ""
	_contains_raid= ""
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
			return "platform_specs"
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
			return "platform_specss"
		except Exception as e :
			raise e



	'''
	get To check if FIPS is present
	'''
	@property
	def is_fips_present(self) :
		try:
			return self._is_fips_present
		except Exception as e :
			raise e


	'''
	get check if Fortville nic card is present
	'''
	@property
	def contains_fortville_nics(self) :
		try:
			return self._contains_fortville_nics
		except Exception as e :
			raise e


	'''
	get Maximum number of channels available
	'''
	@property
	def max_channels(self) :
		try:
			return self._max_channels
		except Exception as e :
			raise e


	'''
	get Maximum number of CPU cores which can be allocated to VM
	'''
	@property
	def max_cores_per_vm(self) :
		try:
			return self._max_cores_per_vm
		except Exception as e :
			raise e


	'''
	get If NextGen Platform
	'''
	@property
	def is_nextgen(self) :
		try:
			return self._is_nextgen
		except Exception as e :
			raise e


	'''
	get total number of management interfaces available
	'''
	@property
	def no_of_mgmt_interfaces(self) :
		try:
			return self._no_of_mgmt_interfaces
		except Exception as e :
			raise e


	'''
	get Enable RAID for the platform
	'''
	@property
	def contains_raid(self) :
		try:
			return self._contains_raid
		except Exception as e :
			raise e

	'''
	Use this operation to get platform capability.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				platform_specs_obj=platform_specs()
				response = platform_specs_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of platform_specs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			platform_specs_obj = platform_specs()
			option_ = options()
			option_._filter=filter_
			return platform_specs_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the platform_specs resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			platform_specs_obj = platform_specs()
			option_ = options()
			option_._count=True
			response = platform_specs_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of platform_specs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			platform_specs_obj = platform_specs()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = platform_specs_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(platform_specs_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.platform_specs
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(platform_specs_responses, response, "platform_specs_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.platform_specs_response_array
				i=0
				error = [platform_specs() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.platform_specs_response_array
			i=0
			platform_specs_objs = [platform_specs() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_platform_specs'):
					for props in obj._platform_specs:
						result = service.payload_formatter.string_to_bulk_resource(platform_specs_response,self.__class__.__name__,props)
						platform_specs_objs[i] = result.platform_specs
						i=i+1
			return platform_specs_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(platform_specs,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class platform_specs_response(base_response):
	def __init__(self,length=1) :
		self.platform_specs= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.platform_specs= [ platform_specs() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class platform_specs_responses(base_response):
	def __init__(self,length=1) :
		self.platform_specs_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.platform_specs_response_array = [ platform_specs() for _ in range(length)]
