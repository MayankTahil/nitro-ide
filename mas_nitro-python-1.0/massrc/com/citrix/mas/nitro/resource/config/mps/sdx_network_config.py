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
Configuration for SDX Network Configuration resource
'''

class sdx_network_config(base_resource):
	_dns= ""
	_gateway= ""
	_svm_ipv6_address= ""
	_additional_dns2= ""
	_additional_dns1= ""
	_config_type= ""
	_svm_ip_address= ""
	_dns_v6= ""
	_gateway_ipv6= ""
	_apply_svm_ip= ""
	_host_ip_address= ""
	_xen_ip_address= ""
	_netmask= ""
	_network_interface= ""
	_sync_to_vm= ""
	_skip_reboot= ""
	_act_id= ""
	_init_status= ""
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
			return "sdx_network_config"
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
			return "sdx_network_configs"
		except Exception as e :
			raise e



	'''
	get DNS Server
	'''
	@property
	def dns(self) :
		try:
			return self._dns
		except Exception as e :
			raise e
	'''
	set DNS Server
	'''
	@dns.setter
	def dns(self,dns):
		try :
			if not isinstance(dns,str):
				raise TypeError("dns must be set to str value")
			self._dns = dns
		except Exception as e :
			raise e


	'''
	get Gateway 
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set Gateway 
	'''
	@gateway.setter
	def gateway(self,gateway):
		try :
			if not isinstance(gateway,str):
				raise TypeError("gateway must be set to str value")
			self._gateway = gateway
		except Exception as e :
			raise e


	'''
	get Management Service IPv6 Address
	'''
	@property
	def svm_ipv6_address(self) :
		try:
			return self._svm_ipv6_address
		except Exception as e :
			raise e
	'''
	set Management Service IPv6 Address
	'''
	@svm_ipv6_address.setter
	def svm_ipv6_address(self,svm_ipv6_address):
		try :
			if not isinstance(svm_ipv6_address,str):
				raise TypeError("svm_ipv6_address must be set to str value")
			self._svm_ipv6_address = svm_ipv6_address
		except Exception as e :
			raise e


	'''
	get Additional DNS Server. Can be IPv4 or IPv6
	'''
	@property
	def additional_dns2(self) :
		try:
			return self._additional_dns2
		except Exception as e :
			raise e
	'''
	set Additional DNS Server. Can be IPv4 or IPv6
	'''
	@additional_dns2.setter
	def additional_dns2(self,additional_dns2):
		try :
			if not isinstance(additional_dns2,str):
				raise TypeError("additional_dns2 must be set to str value")
			self._additional_dns2 = additional_dns2
		except Exception as e :
			raise e


	'''
	get Additional DNS Server. Can be IPv4 or IPv6
	'''
	@property
	def additional_dns1(self) :
		try:
			return self._additional_dns1
		except Exception as e :
			raise e
	'''
	set Additional DNS Server. Can be IPv4 or IPv6
	'''
	@additional_dns1.setter
	def additional_dns1(self,additional_dns1):
		try :
			if not isinstance(additional_dns1,str):
				raise TypeError("additional_dns1 must be set to str value")
			self._additional_dns1 = additional_dns1
		except Exception as e :
			raise e


	'''
	get Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@property
	def config_type(self) :
		try:
			return self._config_type
		except Exception as e :
			raise e
	'''
	set Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@config_type.setter
	def config_type(self,config_type):
		try :
			if not isinstance(config_type,int):
				raise TypeError("config_type must be set to int value")
			self._config_type = config_type
		except Exception as e :
			raise e


	'''
	get Management Service IP Address
	'''
	@property
	def svm_ip_address(self) :
		try:
			return self._svm_ip_address
		except Exception as e :
			raise e
	'''
	set Management Service IP Address
	'''
	@svm_ip_address.setter
	def svm_ip_address(self,svm_ip_address):
		try :
			if not isinstance(svm_ip_address,str):
				raise TypeError("svm_ip_address must be set to str value")
			self._svm_ip_address = svm_ip_address
		except Exception as e :
			raise e


	'''
	get DNS Server IPv6 Address
	'''
	@property
	def dns_v6(self) :
		try:
			return self._dns_v6
		except Exception as e :
			raise e
	'''
	set DNS Server IPv6 Address
	'''
	@dns_v6.setter
	def dns_v6(self,dns_v6):
		try :
			if not isinstance(dns_v6,str):
				raise TypeError("dns_v6 must be set to str value")
			self._dns_v6 = dns_v6
		except Exception as e :
			raise e


	'''
	get Gateway IPv6 Address
	'''
	@property
	def gateway_ipv6(self) :
		try:
			return self._gateway_ipv6
		except Exception as e :
			raise e
	'''
	set Gateway IPv6 Address
	'''
	@gateway_ipv6.setter
	def gateway_ipv6(self,gateway_ipv6):
		try :
			if not isinstance(gateway_ipv6,str):
				raise TypeError("gateway_ipv6 must be set to str value")
			self._gateway_ipv6 = gateway_ipv6
		except Exception as e :
			raise e


	'''
	get Apply SVM IP
	'''
	@property
	def apply_svm_ip(self) :
		try:
			return self._apply_svm_ip
		except Exception as e :
			raise e
	'''
	set Apply SVM IP
	'''
	@apply_svm_ip.setter
	def apply_svm_ip(self,apply_svm_ip):
		try :
			if not isinstance(apply_svm_ip,bool):
				raise TypeError("apply_svm_ip must be set to bool value")
			self._apply_svm_ip = apply_svm_ip
		except Exception as e :
			raise e


	'''
	get Host IP Address
	'''
	@property
	def host_ip_address(self) :
		try:
			return self._host_ip_address
		except Exception as e :
			raise e
	'''
	set Host IP Address
	'''
	@host_ip_address.setter
	def host_ip_address(self,host_ip_address):
		try :
			if not isinstance(host_ip_address,str):
				raise TypeError("host_ip_address must be set to str value")
			self._host_ip_address = host_ip_address
		except Exception as e :
			raise e


	'''
	get XenServer IP Address
	'''
	@property
	def xen_ip_address(self) :
		try:
			return self._xen_ip_address
		except Exception as e :
			raise e
	'''
	set XenServer IP Address
	'''
	@xen_ip_address.setter
	def xen_ip_address(self,xen_ip_address):
		try :
			if not isinstance(xen_ip_address,str):
				raise TypeError("xen_ip_address must be set to str value")
			self._xen_ip_address = xen_ip_address
		except Exception as e :
			raise e


	'''
	get Netmask
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set Netmask
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Interface on which management needs to be enabled
	'''
	@property
	def network_interface(self) :
		try:
			return self._network_interface
		except Exception as e :
			raise e
	'''
	set Interface on which management needs to be enabled
	'''
	@network_interface.setter
	def network_interface(self,network_interface):
		try :
			if not isinstance(network_interface,str):
				raise TypeError("network_interface must be set to str value")
			self._network_interface = network_interface
		except Exception as e :
			raise e

	'''
	Set option to sync or not to sync with CB
	'''
	@property
	def sync_to_vm(self):
		try:
			return self._sync_to_vm
		except Exception as e :
			raise e
	'''
	Set option to sync or not to sync with CB
	'''
	@sync_to_vm.setter
	def sync_to_vm(self,sync_to_vm):
		try :
			if not isinstance(sync_to_vm,bool):
				raise TypeError("sync_to_vm must be set to bool value")
			self._sync_to_vm = sync_to_vm
		except Exception as e :
			raise e

	'''
	Set CB reboot required option during PUT
	'''
	@property
	def skip_reboot(self):
		try:
			return self._skip_reboot
		except Exception as e :
			raise e
	'''
	Set CB reboot required option during PUT
	'''
	@skip_reboot.setter
	def skip_reboot(self,skip_reboot):
		try :
			if not isinstance(skip_reboot,bool):
				raise TypeError("skip_reboot must be set to bool value")
			self._skip_reboot = skip_reboot
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	System initialize status
	'''
	@property
	def init_status(self):
		try:
			return self._init_status
		except Exception as e :
			raise e
	'''
	System initialize status
	'''
	@init_status.setter
	def init_status(self,init_status):
		try :
			if not isinstance(init_status,int):
				raise TypeError("init_status must be set to int value")
			self._init_status = init_status
		except Exception as e :
			raise e

	'''
	Use this operation to get SDX network configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_network_config_obj=sdx_network_config()
				response = sdx_network_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify SDX network configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_network_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_network_config_obj = sdx_network_config()
			option_ = options()
			option_._filter=filter_
			return sdx_network_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_network_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_network_config_obj = sdx_network_config()
			option_ = options()
			option_._count=True
			response = sdx_network_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_network_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_network_config_obj = sdx_network_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_network_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_network_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_network_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_network_config_responses, response, "sdx_network_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_network_config_response_array
				i=0
				error = [sdx_network_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_network_config_response_array
			i=0
			sdx_network_config_objs = [sdx_network_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_network_config'):
					for props in obj._sdx_network_config:
						result = service.payload_formatter.string_to_bulk_resource(sdx_network_config_response,self.__class__.__name__,props)
						sdx_network_config_objs[i] = result.sdx_network_config
						i=i+1
			return sdx_network_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_network_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_network_config_response(base_response):
	def __init__(self,length=1) :
		self.sdx_network_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_network_config= [ sdx_network_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_network_config_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_network_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_network_config_response_array = [ sdx_network_config() for _ in range(length)]
