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
Configuration for SNMP configuration resource
'''

class ns_snmp_config(base_resource):
	_save_config= ""
	_trapdestination= ""
	_snmpauthprotocol= ""
	_snmpsecurityname= ""
	_snmpprivprotocol= ""
	_ns_ip_address_arr=[]
	_state= ""
	_ns_ip_address= ""
	_snmpsecuritylevel= ""
	_snmpcommunity= ""
	_snmpprivpassword= ""
	_snmpversion= ""
	_snmpauthpassword= ""
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
			return "ns_snmp_config"
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
			return "ns_snmp_configs"
		except Exception as e :
			raise e



	'''
	get true, if save config is required
	'''
	@property
	def save_config(self) :
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	set true, if save config is required
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e


	'''
	get State of configuration (enable/disable)
	'''
	@property
	def trapdestination(self) :
		try:
			return self._trapdestination
		except Exception as e :
			raise e
	'''
	set State of configuration (enable/disable)
	'''
	@trapdestination.setter
	def trapdestination(self,trapdestination):
		try :
			if not isinstance(trapdestination,str):
				raise TypeError("trapdestination must be set to str value")
			self._trapdestination = trapdestination
		except Exception as e :
			raise e


	'''
	get SNMP v3 auth protocol
	'''
	@property
	def snmpauthprotocol(self) :
		try:
			return self._snmpauthprotocol
		except Exception as e :
			raise e
	'''
	set SNMP v3 auth protocol
	'''
	@snmpauthprotocol.setter
	def snmpauthprotocol(self,snmpauthprotocol):
		try :
			if not isinstance(snmpauthprotocol,str):
				raise TypeError("snmpauthprotocol must be set to str value")
			self._snmpauthprotocol = snmpauthprotocol
		except Exception as e :
			raise e


	'''
	get SNMP v3 security name
	'''
	@property
	def snmpsecurityname(self) :
		try:
			return self._snmpsecurityname
		except Exception as e :
			raise e
	'''
	set SNMP v3 security name
	'''
	@snmpsecurityname.setter
	def snmpsecurityname(self,snmpsecurityname):
		try :
			if not isinstance(snmpsecurityname,str):
				raise TypeError("snmpsecurityname must be set to str value")
			self._snmpsecurityname = snmpsecurityname
		except Exception as e :
			raise e


	'''
	get SNMP v3 priv protocol
	'''
	@property
	def snmpprivprotocol(self) :
		try:
			return self._snmpprivprotocol
		except Exception as e :
			raise e
	'''
	set SNMP v3 priv protocol
	'''
	@snmpprivprotocol.setter
	def snmpprivprotocol(self,snmpprivprotocol):
		try :
			if not isinstance(snmpprivprotocol,str):
				raise TypeError("snmpprivprotocol must be set to str value")
			self._snmpprivprotocol = snmpprivprotocol
		except Exception as e :
			raise e


	'''
	get List of NS IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of NS IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e


	'''
	get State of configuration (enable/disable)
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of configuration (enable/disable)
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get SNMP v3 security level
	'''
	@property
	def snmpsecuritylevel(self) :
		try:
			return self._snmpsecuritylevel
		except Exception as e :
			raise e
	'''
	set SNMP v3 security level
	'''
	@snmpsecuritylevel.setter
	def snmpsecuritylevel(self,snmpsecuritylevel):
		try :
			if not isinstance(snmpsecuritylevel,str):
				raise TypeError("snmpsecuritylevel must be set to str value")
			self._snmpsecuritylevel = snmpsecuritylevel
		except Exception as e :
			raise e


	'''
	get SNMP community
	'''
	@property
	def snmpcommunity(self) :
		try:
			return self._snmpcommunity
		except Exception as e :
			raise e
	'''
	set SNMP community
	'''
	@snmpcommunity.setter
	def snmpcommunity(self,snmpcommunity):
		try :
			if not isinstance(snmpcommunity,str):
				raise TypeError("snmpcommunity must be set to str value")
			self._snmpcommunity = snmpcommunity
		except Exception as e :
			raise e


	'''
	get SNMP v3 priv password
	'''
	@property
	def snmpprivpassword(self) :
		try:
			return self._snmpprivpassword
		except Exception as e :
			raise e
	'''
	set SNMP v3 priv password
	'''
	@snmpprivpassword.setter
	def snmpprivpassword(self,snmpprivpassword):
		try :
			if not isinstance(snmpprivpassword,str):
				raise TypeError("snmpprivpassword must be set to str value")
			self._snmpprivpassword = snmpprivpassword
		except Exception as e :
			raise e


	'''
	get SNMP version
	'''
	@property
	def snmpversion(self) :
		try:
			return self._snmpversion
		except Exception as e :
			raise e
	'''
	set SNMP version
	'''
	@snmpversion.setter
	def snmpversion(self,snmpversion):
		try :
			if not isinstance(snmpversion,str):
				raise TypeError("snmpversion must be set to str value")
			self._snmpversion = snmpversion
		except Exception as e :
			raise e


	'''
	get SNMP v3 auth password
	'''
	@property
	def snmpauthpassword(self) :
		try:
			return self._snmpauthpassword
		except Exception as e :
			raise e
	'''
	set SNMP v3 auth password
	'''
	@snmpauthpassword.setter
	def snmpauthpassword(self,snmpauthpassword):
		try :
			if not isinstance(snmpauthpassword,str):
				raise TypeError("snmpauthpassword must be set to str value")
			self._snmpauthpassword = snmpauthpassword
		except Exception as e :
			raise e

	'''
	add ns snmp configuration.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_snmp_config_obj= ns_snmp_config()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_snmp_config_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp configuration.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_snmp_config_obj=ns_snmp_config()
				return cls.update_bulk_request(client,resource,ns_snmp_config_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_snmp_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_snmp_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_snmp_config_responses, response, "ns_snmp_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_snmp_config_response_array
				i=0
				error = [ns_snmp_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_snmp_config_response_array
			i=0
			ns_snmp_config_objs = [ns_snmp_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_snmp_config'):
					for props in obj._ns_snmp_config:
						result = service.payload_formatter.string_to_bulk_resource(ns_snmp_config_response,self.__class__.__name__,props)
						ns_snmp_config_objs[i] = result.ns_snmp_config
						i=i+1
			return ns_snmp_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_snmp_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_snmp_config_response(base_response):
	def __init__(self,length=1) :
		self.ns_snmp_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_snmp_config= [ ns_snmp_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_snmp_config_responses(base_response):
	def __init__(self,length=1) :
		self.ns_snmp_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_snmp_config_response_array = [ ns_snmp_config() for _ in range(length)]
