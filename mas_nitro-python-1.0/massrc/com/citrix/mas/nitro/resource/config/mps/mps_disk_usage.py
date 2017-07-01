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
Configuration for Available Disks Usage resource
'''

class mps_disk_usage(base_resource):
	_free_space= ""
	_parent_name= ""
	_disk_usage= ""
	_used_space= ""
	_parent_id= ""
	_disk_name= ""
	_total_space= ""
	_disk_partition= ""
	_disk_slice= ""
	_id= ""
	_disk_capacity= ""
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
			return "mps_disk_usage"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
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
			return "mps_disk_usages"
		except Exception as e :
			raise e



	'''
	get Free space available in KB
	'''
	@property
	def free_space(self) :
		try:
			return self._free_space
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Disk Usage (%)
	'''
	@property
	def disk_usage(self) :
		try:
			return self._disk_usage
		except Exception as e :
			raise e


	'''
	get Used space available in KB
	'''
	@property
	def used_space(self) :
		try:
			return self._used_space
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Disk Name
	'''
	@property
	def disk_name(self) :
		try:
			return self._disk_name
		except Exception as e :
			raise e


	'''
	get Total space in KB
	'''
	@property
	def total_space(self) :
		try:
			return self._total_space
		except Exception as e :
			raise e


	'''
	get Disk Partition
	'''
	@property
	def disk_partition(self) :
		try:
			return self._disk_partition
		except Exception as e :
			raise e
	'''
	set Disk Partition
	'''
	@disk_partition.setter
	def disk_partition(self,disk_partition):
		try :
			if not isinstance(disk_partition,str):
				raise TypeError("disk_partition must be set to str value")
			self._disk_partition = disk_partition
		except Exception as e :
			raise e


	'''
	get Disk Slice
	'''
	@property
	def disk_slice(self) :
		try:
			return self._disk_slice
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e


	'''
	get Disk Total Capacity in KB
	'''
	@property
	def disk_capacity(self) :
		try:
			return self._disk_capacity
		except Exception as e :
			raise e

	'''
	Use this operation to get MPS monitorind health stats.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_disk_usage_obj=mps_disk_usage()
				response = mps_disk_usage_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_disk_usage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_disk_usage_obj = mps_disk_usage()
			option_ = options()
			option_._filter=filter_
			return mps_disk_usage_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_disk_usage resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_disk_usage_obj = mps_disk_usage()
			option_ = options()
			option_._count=True
			response = mps_disk_usage_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_disk_usage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_disk_usage_obj = mps_disk_usage()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_disk_usage_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_disk_usage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_disk_usage
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_disk_usage_responses, response, "mps_disk_usage_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_disk_usage_response_array
				i=0
				error = [mps_disk_usage() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_disk_usage_response_array
			i=0
			mps_disk_usage_objs = [mps_disk_usage() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_disk_usage'):
					for props in obj._mps_disk_usage:
						result = service.payload_formatter.string_to_bulk_resource(mps_disk_usage_response,self.__class__.__name__,props)
						mps_disk_usage_objs[i] = result.mps_disk_usage
						i=i+1
			return mps_disk_usage_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_disk_usage,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_disk_usage_response(base_response):
	def __init__(self,length=1) :
		self.mps_disk_usage= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_disk_usage= [ mps_disk_usage() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_disk_usage_responses(base_response):
	def __init__(self,length=1) :
		self.mps_disk_usage_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_disk_usage_response_array = [ mps_disk_usage() for _ in range(length)]
