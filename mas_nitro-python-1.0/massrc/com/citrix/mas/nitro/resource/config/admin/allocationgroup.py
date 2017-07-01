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
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember


'''
Configuration for NetScaler Control Center allocates NetScaler instances according to the SLA that is defined as part this service package. resource
'''

class allocationgroup(base_resource):
	_partitionspec= ""
	_devicespec= ""
	_device_type= ""
	_placement_scheme= ""
	_devicegroup= ""
	_allocationpolicy= ""
	_device_allocation_type= ""
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
			return "allocationgroup"
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
			return "allocationgroups"
		except Exception as e :
			raise e



	'''
	get ID of a Partition Specification. The partition specification will be used while creating partition
	'''
	@property
	def partitionspec(self) :
		try:
			return self._partitionspec
		except Exception as e :
			raise e
	'''
	set ID of a Partition Specification. The partition specification will be used while creating partition
	'''
	@partitionspec.setter
	def partitionspec(self,partitionspec):
		try :
			if not isinstance(partitionspec,groupmember):
				raise TypeError("partitionspec must be set to groupmember value")
			self._partitionspec = partitionspec
		except Exception as e :
			raise e


	'''
	get ID of a Device Specification. The device specification will be used while creating device instances
	'''
	@property
	def devicespec(self) :
		try:
			return self._devicespec
		except Exception as e :
			raise e
	'''
	set ID of a Device Specification. The device specification will be used while creating device instances
	'''
	@devicespec.setter
	def devicespec(self,devicespec):
		try :
			if not isinstance(devicespec,groupmember):
				raise TypeError("devicespec must be set to groupmember value")
			self._devicespec = devicespec
		except Exception as e :
			raise e


	'''
	get The device type that has to be allocated. Possible values - 'NetScaler'
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set The device type that has to be allocated. Possible values - 'NetScaler'
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
		except Exception as e :
			raise e


	'''
	get The allocation policy scheme which will help allocating a device when allocation policy is 'shared'. Possible values - 'roundrobin', 'leastentity'
	'''
	@property
	def placement_scheme(self) :
		try:
			return self._placement_scheme
		except Exception as e :
			raise e
	'''
	set The allocation policy scheme which will help allocating a device when allocation policy is 'shared'. Possible values - 'roundrobin', 'leastentity'
	'''
	@placement_scheme.setter
	def placement_scheme(self,placement_scheme):
		try :
			if not isinstance(placement_scheme,str):
				raise TypeError("placement_scheme must be set to str value")
			self._placement_scheme = placement_scheme
		except Exception as e :
			raise e


	'''
	get Devicegroup from which devices will be allocated
	'''
	@property
	def devicegroup(self) :
		try:
			return self._devicegroup
		except Exception as e :
			raise e
	'''
	set Devicegroup from which devices will be allocated
	'''
	@devicegroup.setter
	def devicegroup(self,devicegroup):
		try :
			if not isinstance(devicegroup,groupmember):
				raise TypeError("devicegroup must be set to groupmember value")
			self._devicegroup = devicegroup
		except Exception as e :
			raise e


	'''
	get The allocation policy of the device instance. Possible values - 'shared', 'dedicated'
	'''
	@property
	def allocationpolicy(self) :
		try:
			return self._allocationpolicy
		except Exception as e :
			raise e
	'''
	set The allocation policy of the device instance. Possible values - 'shared', 'dedicated'
	'''
	@allocationpolicy.setter
	def allocationpolicy(self,allocationpolicy):
		try :
			if not isinstance(allocationpolicy,str):
				raise TypeError("allocationpolicy must be set to str value")
			self._allocationpolicy = allocationpolicy
		except Exception as e :
			raise e


	'''
	get The device instance that has to be allocated. Possible values - 'netScaler', 'partition'
	'''
	@property
	def device_allocation_type(self) :
		try:
			return self._device_allocation_type
		except Exception as e :
			raise e
	'''
	set The device instance that has to be allocated. Possible values - 'netScaler', 'partition'
	'''
	@device_allocation_type.setter
	def device_allocation_type(self,device_allocation_type):
		try :
			if not isinstance(device_allocation_type,str):
				raise TypeError("device_allocation_type must be set to str value")
			self._device_allocation_type = device_allocation_type
		except Exception as e :
			raise e

	'''
	Use this operation to get OpenStack cloud details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				allocationgroup_obj=allocationgroup()
				response = allocationgroup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of allocationgroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			allocationgroup_obj = allocationgroup()
			option_ = options()
			option_._filter=filter_
			return allocationgroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the allocationgroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			allocationgroup_obj = allocationgroup()
			option_ = options()
			option_._count=True
			response = allocationgroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of allocationgroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			allocationgroup_obj = allocationgroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = allocationgroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(allocationgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.allocationgroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(allocationgroup_responses, response, "allocationgroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.allocationgroup_response_array
				i=0
				error = [allocationgroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.allocationgroup_response_array
			i=0
			allocationgroup_objs = [allocationgroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_allocationgroup'):
					for props in obj._allocationgroup:
						result = service.payload_formatter.string_to_bulk_resource(allocationgroup_response,self.__class__.__name__,props)
						allocationgroup_objs[i] = result.allocationgroup
						i=i+1
			return allocationgroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(allocationgroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class allocationgroup_response(base_response):
	def __init__(self,length=1) :
		self.allocationgroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.allocationgroup= [ allocationgroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class allocationgroup_responses(base_response):
	def __init__(self,length=1) :
		self.allocationgroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.allocationgroup_response_array = [ allocationgroup() for _ in range(length)]
