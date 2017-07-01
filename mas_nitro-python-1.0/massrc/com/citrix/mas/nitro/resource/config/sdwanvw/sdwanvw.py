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

from massrc.com.citrix.mas.nitro.resource.config.mps.vm_device import vm_device

'''
Configuration for SDWANVW resource
'''

class sdwanvw(vm_device):
	_lan_out= ""
	_current_time= ""
	_qosstatus= ""
	_data_reduction= ""
	_max_plugins= ""
	_hostid= ""
	_active_connections= ""
	_connected_plugins= ""
	_wan_out= ""
	_bandwidth_mode= ""
	_wan_in= ""
	_platform= ""
	_br_cpu_usage= ""
	_unacl_connections= ""
	_system_load= ""
	_license= ""
	_bandwidth_limit= ""
	_acl_connections= ""
	_br_memory_usage= ""
	_build_number= ""
	_lan_in= ""
	_product= ""
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
			return "sdwanvw"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(sdwanvw,self).get_object_id()
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
			return "sdwanvws"
		except Exception as e :
			raise e



	'''
	get LAN Out of NetScaler SD-WAN VW Instance in Mbps
	'''
	@property
	def lan_out(self) :
		try:
			return self._lan_out
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
	get QoS Status
	'''
	@property
	def qosstatus(self) :
		try:
			return self._qosstatus
		except Exception as e :
			raise e


	'''
	get Data Reduction (%)
	'''
	@property
	def data_reduction(self) :
		try:
			return self._data_reduction
		except Exception as e :
			raise e


	'''
	get Maximum plugins
	'''
	@property
	def max_plugins(self) :
		try:
			return self._max_plugins
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
	get Total Active Connections on NetScaler SD-WAN VW Instance
	'''
	@property
	def active_connections(self) :
		try:
			return self._active_connections
		except Exception as e :
			raise e


	'''
	get connected plugins
	'''
	@property
	def connected_plugins(self) :
		try:
			return self._connected_plugins
		except Exception as e :
			raise e


	'''
	get WAN Out of NetScaler SD-WAN VW Instance in Mbps
	'''
	@property
	def wan_out(self) :
		try:
			return self._wan_out
		except Exception as e :
			raise e


	'''
	get Boost status : Bandwidth Mode of NetScaler SD-WAN VW Instance
	'''
	@property
	def bandwidth_mode(self) :
		try:
			return self._bandwidth_mode
		except Exception as e :
			raise e


	'''
	get WAN In of NetScaler SD-WAN VW Instance in Mbps
	'''
	@property
	def wan_in(self) :
		try:
			return self._wan_in
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
	get CPU Usage (%) of NetScaler SD-WAN VW Instance
	'''
	@property
	def br_cpu_usage(self) :
		try:
			return self._br_cpu_usage
		except Exception as e :
			raise e


	'''
	get non-accelerated connections
	'''
	@property
	def unacl_connections(self) :
		try:
			return self._unacl_connections
		except Exception as e :
			raise e


	'''
	get System Load (%) on NetScaler SD-WAN VW Instance
	'''
	@property
	def system_load(self) :
		try:
			return self._system_load
		except Exception as e :
			raise e


	'''
	get NetScaler SD-WAN VW License
	'''
	@property
	def license(self) :
		try:
			return self._license
		except Exception as e :
			raise e


	'''
	get bandwidth limit of NetScaler SD-WAN VW Instance (K-Bits/sec)
	'''
	@property
	def bandwidth_limit(self) :
		try:
			return self._bandwidth_limit
		except Exception as e :
			raise e


	'''
	get Accelerated Connections
	'''
	@property
	def acl_connections(self) :
		try:
			return self._acl_connections
		except Exception as e :
			raise e


	'''
	get Memory Usage (%) of NetScaler SD-WAN VW Instance
	'''
	@property
	def br_memory_usage(self) :
		try:
			return self._br_memory_usage
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
	get Lan In of NetScaler SD-WAN VW Instance in Mbps
	'''
	@property
	def lan_in(self) :
		try:
			return self._lan_in
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
				sdwanvw_obj= sdwanvw()
				return cls.perform_operation_bulk_request(service,"reboot", resource,sdwanvw_obj)
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
				sdwanvw_obj= sdwanvw()
				return cls.perform_operation_bulk_request(service,"add", resource,sdwanvw_obj)
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
					sdwanvw_obj=sdwanvw()
					return cls.delete_bulk_request(client,resource,sdwanvw_obj)
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
				sdwanvw_obj=sdwanvw()
				response = sdwanvw_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdwanvw resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdwanvw_obj = sdwanvw()
			option_ = options()
			option_._filter=filter_
			return sdwanvw_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdwanvw resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdwanvw_obj = sdwanvw()
			option_ = options()
			option_._count=True
			response = sdwanvw_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdwanvw resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdwanvw_obj = sdwanvw()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdwanvw_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdwanvw_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdwanvw
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdwanvw_responses, response, "sdwanvw_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdwanvw_response_array
				i=0
				error = [sdwanvw() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdwanvw_response_array
			i=0
			sdwanvw_objs = [sdwanvw() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdwanvw'):
					for props in obj._sdwanvw:
						result = service.payload_formatter.string_to_bulk_resource(sdwanvw_response,self.__class__.__name__,props)
						sdwanvw_objs[i] = result.sdwanvw
						i=i+1
			return sdwanvw_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdwanvw,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdwanvw_response(base_response):
	def __init__(self,length=1) :
		self.sdwanvw= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdwanvw= [ sdwanvw() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdwanvw_responses(base_response):
	def __init__(self,length=1) :
		self.sdwanvw_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdwanvw_response_array = [ sdwanvw() for _ in range(length)]
