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
Configuration for MPS Network Configuration resource
'''

class mps_network_config(base_resource):
	_alternate_dns_v6= ""
	_dns= ""
	_gateway= ""
	_alternate_dns= ""
	_config_type= ""
	_dns_v6= ""
	_gateway_ipv6= ""
	_ip_address= ""
	_netmask= ""
	_ipv6_address= ""
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
			return "mps_network_config"
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
			return "mps_network_configs"
		except Exception as e :
			raise e



	'''
	get Alternate DNS Server IPv6 Address
	'''
	@property
	def alternate_dns_v6(self) :
		try:
			return self._alternate_dns_v6
		except Exception as e :
			raise e
	'''
	set Alternate DNS Server IPv6 Address
	'''
	@alternate_dns_v6.setter
	def alternate_dns_v6(self,alternate_dns_v6):
		try :
			if not isinstance(alternate_dns_v6,str):
				raise TypeError("alternate_dns_v6 must be set to str value")
			self._alternate_dns_v6 = alternate_dns_v6
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
	get Alternate DNS Server
	'''
	@property
	def alternate_dns(self) :
		try:
			return self._alternate_dns
		except Exception as e :
			raise e
	'''
	set Alternate DNS Server
	'''
	@alternate_dns.setter
	def alternate_dns(self,alternate_dns):
		try :
			if not isinstance(alternate_dns,str):
				raise TypeError("alternate_dns must be set to str value")
			self._alternate_dns = alternate_dns
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
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
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
	get Management Service IPv6 Address
	'''
	@property
	def ipv6_address(self) :
		try:
			return self._ipv6_address
		except Exception as e :
			raise e
	'''
	set Management Service IPv6 Address
	'''
	@ipv6_address.setter
	def ipv6_address(self,ipv6_address):
		try :
			if not isinstance(ipv6_address,str):
				raise TypeError("ipv6_address must be set to str value")
			self._ipv6_address = ipv6_address
		except Exception as e :
			raise e

	'''
	Use this operation to get MPS network configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_network_config_obj=mps_network_config()
				response = mps_network_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify MPS network configuration.
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
	Use this API to fetch filtered set of mps_network_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_network_config_obj = mps_network_config()
			option_ = options()
			option_._filter=filter_
			return mps_network_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_network_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_network_config_obj = mps_network_config()
			option_ = options()
			option_._count=True
			response = mps_network_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_network_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_network_config_obj = mps_network_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_network_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_network_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_network_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_network_config_responses, response, "mps_network_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_network_config_response_array
				i=0
				error = [mps_network_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_network_config_response_array
			i=0
			mps_network_config_objs = [mps_network_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_network_config'):
					for props in obj._mps_network_config:
						result = service.payload_formatter.string_to_bulk_resource(mps_network_config_response,self.__class__.__name__,props)
						mps_network_config_objs[i] = result.mps_network_config
						i=i+1
			return mps_network_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_network_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_network_config_response(base_response):
	def __init__(self,length=1) :
		self.mps_network_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_network_config= [ mps_network_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_network_config_responses(base_response):
	def __init__(self,length=1) :
		self.mps_network_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_network_config_response_array = [ mps_network_config() for _ in range(length)]
