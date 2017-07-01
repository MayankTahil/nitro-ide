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
from massrc.com.citrix.mas.nitro.resource.config.mps.mps_disk_usage import mps_disk_usage


'''
Configuration for Health Monitoring Stats resource
'''

class mps_health(base_resource):
	_disks_usage=[]
	_memory_total= ""
	_disk_total_capacity= ""
	_disk_usage= ""
	_disk_total= ""
	_memory_usage= ""
	_disk_free= ""
	_page_size= ""
	_node_id= ""
	_memory_free= ""
	_cpu_usage= ""
	_id= ""
	_disk_used= ""
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
			return "mps_health"
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
			return "mps_healths"
		except Exception as e :
			raise e



	'''
	get Individual Disks Usage
	'''
	@property
	def disks_usage(self) :
		try:
			return self._disks_usage
		except Exception as e :
			raise e
	'''
	set Individual Disks Usage
	'''
	@disks_usage.setter
	def disks_usage(self,disks_usage) :
		try :
			if not isinstance(disks_usage,list):
				raise TypeError("disks_usage must be set to array of mps_disk_usage value")
			for item in disks_usage :
				if not isinstance(item,mps_disk_usage):
					raise TypeError("item must be set to mps_disk_usage value")
			self._disks_usage = disks_usage
		except Exception as e :
			raise e


	'''
	get Total memory in KB
	'''
	@property
	def memory_total(self) :
		try:
			return self._memory_total
		except Exception as e :
			raise e


	'''
	get Disk Total Capacity in KB
	'''
	@property
	def disk_total_capacity(self) :
		try:
			return self._disk_total_capacity
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
	get Total available disk space in KB
	'''
	@property
	def disk_total(self) :
		try:
			return self._disk_total
		except Exception as e :
			raise e


	'''
	get Memory Usage (%)
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e


	'''
	get Free disk available in KB
	'''
	@property
	def disk_free(self) :
		try:
			return self._disk_free
		except Exception as e :
			raise e


	'''
	get Total memory in KB
	'''
	@property
	def page_size(self) :
		try:
			return self._page_size
		except Exception as e :
			raise e


	'''
	get Application Node ID
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Application Node ID
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e


	'''
	get Free memory available in KB
	'''
	@property
	def memory_free(self) :
		try:
			return self._memory_free
		except Exception as e :
			raise e


	'''
	get CPU Usage (%)
	'''
	@property
	def cpu_usage(self) :
		try:
			return self._cpu_usage
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Disk used in KB
	'''
	@property
	def disk_used(self) :
		try:
			return self._disk_used
		except Exception as e :
			raise e

	'''
	Use this operation to get health stats.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_health_obj=mps_health()
				response = mps_health_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_health resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_health_obj = mps_health()
			option_ = options()
			option_._filter=filter_
			return mps_health_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_health resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_health_obj = mps_health()
			option_ = options()
			option_._count=True
			response = mps_health_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_health resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_health_obj = mps_health()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_health_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_health_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_health
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_health_responses, response, "mps_health_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_health_response_array
				i=0
				error = [mps_health() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_health_response_array
			i=0
			mps_health_objs = [mps_health() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_health'):
					for props in obj._mps_health:
						result = service.payload_formatter.string_to_bulk_resource(mps_health_response,self.__class__.__name__,props)
						mps_health_objs[i] = result.mps_health
						i=i+1
			return mps_health_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_health,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_health_response(base_response):
	def __init__(self,length=1) :
		self.mps_health= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_health= [ mps_health() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_health_responses(base_response):
	def __init__(self,length=1) :
		self.mps_health_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_health_response_array = [ mps_health() for _ in range(length)]
