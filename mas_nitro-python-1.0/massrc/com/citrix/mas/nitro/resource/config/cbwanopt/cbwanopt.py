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
Configuration for CBWANOPT resource
'''

class cbwanopt(vm_device):
	_lan_out= ""
	_current_time= ""
	_qosstatus= ""
	_data_reduction= ""
	_max_plugins= ""
	_active_connections= ""
	_connected_plugins= ""
	_wan_out= ""
	_bandwidth_mode= ""
	_wan_in= ""
	_ha_peer_ip_address= ""
	_platform= ""
	_unacl_connections= ""
	_ha_peer_state= ""
	_havmip= ""
	_memory_usage= ""
	_is_sdx_platform= ""
	_system_load= ""
	_license= ""
	_acl_connections= ""
	_bandwidth_limit= ""
	_ha_state= ""
	_build_number= ""
	_bypass= ""
	_operation_status= ""
	_cpu_usage= ""
	_lan_in= ""
	_ha_peer_id= ""
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
			return "cbwanopt"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(cbwanopt,self).get_object_id()
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
			return "cbwanopts"
		except Exception as e :
			raise e



	'''
	get LAN Out of CloudBridge Instance in Mbps
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
	get Total Active Connections on CloudBridge Instance
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
	get WAN Out of CloudBridge Instance in Mbps
	'''
	@property
	def wan_out(self) :
		try:
			return self._wan_out
		except Exception as e :
			raise e


	'''
	get Boost status : Bandwidth Mode of CloudBridge Instance
	'''
	@property
	def bandwidth_mode(self) :
		try:
			return self._bandwidth_mode
		except Exception as e :
			raise e


	'''
	get WAN In of CloudBridge Instance in Mbps
	'''
	@property
	def wan_in(self) :
		try:
			return self._wan_in
		except Exception as e :
			raise e


	'''
	get Peer IP Address of CloudBridge WAN Opt Instance
	'''
	@property
	def ha_peer_ip_address(self) :
		try:
			return self._ha_peer_ip_address
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
	get non-accelerated connections
	'''
	@property
	def unacl_connections(self) :
		try:
			return self._unacl_connections
		except Exception as e :
			raise e


	'''
	get Peer State of Sd-WAN WO Instance in HA mode
	'''
	@property
	def ha_peer_state(self) :
		try:
			return self._ha_peer_state
		except Exception as e :
			raise e


	'''
	get HA VM IPAddress
	'''
	@property
	def havmip(self) :
		try:
			return self._havmip
		except Exception as e :
			raise e


	'''
	get Memory Usage (%) of CBWANOPT Instance
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e


	'''
	get True if it is SDX platform
	'''
	@property
	def is_sdx_platform(self) :
		try:
			return self._is_sdx_platform
		except Exception as e :
			raise e
	'''
	set True if it is SDX platform
	'''
	@is_sdx_platform.setter
	def is_sdx_platform(self,is_sdx_platform):
		try :
			if not isinstance(is_sdx_platform,bool):
				raise TypeError("is_sdx_platform must be set to bool value")
			self._is_sdx_platform = is_sdx_platform
		except Exception as e :
			raise e


	'''
	get System Load (%) on CloudBridge Instance
	'''
	@property
	def system_load(self) :
		try:
			return self._system_load
		except Exception as e :
			raise e


	'''
	get CloudBridge License
	'''
	@property
	def license(self) :
		try:
			return self._license
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
	get bandwidth limit of CloudBridge Instance (K-Bits/sec)
	'''
	@property
	def bandwidth_limit(self) :
		try:
			return self._bandwidth_limit
		except Exception as e :
			raise e


	'''
	get State of CloudBridge WAN Opt Instance in HA mode
	'''
	@property
	def ha_state(self) :
		try:
			return self._ha_state
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
	get bypass value of CloudBridge WAN Opt Instance
	'''
	@property
	def bypass(self) :
		try:
			return self._bypass
		except Exception as e :
			raise e


	'''
	get Operation status of CloudBridge WAN Opt Instance
	'''
	@property
	def operation_status(self) :
		try:
			return self._operation_status
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of CBWANOPT Instance
	'''
	@property
	def cpu_usage(self) :
		try:
			return self._cpu_usage
		except Exception as e :
			raise e


	'''
	get Lan In of CloudBridge Instance in Mbps
	'''
	@property
	def lan_in(self) :
		try:
			return self._lan_in
		except Exception as e :
			raise e


	'''
	get Id of the Peer in an HA setup
	'''
	@property
	def ha_peer_id(self) :
		try:
			return self._ha_peer_id
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
	Use this operation to unmanage CBWANOPT device.
	'''

	'''
	Use this operation to unmanage CBWANOPT device.
	'''
	@classmethod
	def unmanage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"unmanage")
			else : 
				cbwanopt_obj= cbwanopt()
				return cls.perform_operation_bulk_request(service,"unmanage", resource,cbwanopt_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to reboot CBWANOPT device.
	'''

	'''
	Use this operation to reboot CBWANOPT device.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"reboot")
			else : 
				cbwanopt_obj= cbwanopt()
				return cls.perform_operation_bulk_request(service,"reboot", resource,cbwanopt_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add CBWANOPT device.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				cbwanopt_obj= cbwanopt()
				return cls.perform_operation_bulk_request(service,"add", resource,cbwanopt_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete CBWANOPT device.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					cbwanopt_obj=cbwanopt()
					return cls.delete_bulk_request(client,resource,cbwanopt_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get CBWANOPT device .
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cbwanopt_obj=cbwanopt()
				response = cbwanopt_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to manage CBWANOPT device.
	'''

	'''
	Use this operation to manage CBWANOPT device.
	'''
	@classmethod
	def manage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"manage")
			else : 
				cbwanopt_obj= cbwanopt()
				return cls.perform_operation_bulk_request(service,"manage", resource,cbwanopt_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cbwanopt resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cbwanopt_obj = cbwanopt()
			option_ = options()
			option_._filter=filter_
			return cbwanopt_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cbwanopt resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cbwanopt_obj = cbwanopt()
			option_ = options()
			option_._count=True
			response = cbwanopt_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cbwanopt resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cbwanopt_obj = cbwanopt()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cbwanopt_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cbwanopt_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cbwanopt
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cbwanopt_responses, response, "cbwanopt_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cbwanopt_response_array
				i=0
				error = [cbwanopt() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cbwanopt_response_array
			i=0
			cbwanopt_objs = [cbwanopt() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cbwanopt'):
					for props in obj._cbwanopt:
						result = service.payload_formatter.string_to_bulk_resource(cbwanopt_response,self.__class__.__name__,props)
						cbwanopt_objs[i] = result.cbwanopt
						i=i+1
			return cbwanopt_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cbwanopt,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cbwanopt_response(base_response):
	def __init__(self,length=1) :
		self.cbwanopt= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cbwanopt= [ cbwanopt() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cbwanopt_responses(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cbwanopt_response_array = [ cbwanopt() for _ in range(length)]
