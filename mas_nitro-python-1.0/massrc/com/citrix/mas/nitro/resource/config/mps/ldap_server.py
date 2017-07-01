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
Configuration for LDAP Server resource
'''

class ldap_server(base_resource):
	_auth_timeout= ""
	_group_search_subattribute= ""
	_follow_referrals= ""
	_search_filter= ""
	_group_attr_name= ""
	_ldap_host_name= ""
	_change_password= ""
	_default_authentication_group= ""
	_max_nesting_level= ""
	_login_name= ""
	_id= ""
	_ip_address= ""
	_nested_group_extraction= ""
	_group_search_attribute= ""
	_group_name_identifier= ""
	_subattribute_name= ""
	_name= ""
	_validate_ldap_server_certs= ""
	_group_search_filter= ""
	_bind_dn= ""
	_port= ""
	_base_dn= ""
	_sec_type= ""
	_max_ldap_referrals= ""
	_type= ""
	_bind_passwd= ""
	_address_type= ""
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
			return "ldap_server"
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
			return "ldap_servers"
		except Exception as e :
			raise e



	'''
	get The maximum number of seconds the system will wait for a response from the LDAP server
	'''
	@property
	def auth_timeout(self) :
		try:
			return self._auth_timeout
		except Exception as e :
			raise e
	'''
	set The maximum number of seconds the system will wait for a response from the LDAP server
	'''
	@auth_timeout.setter
	def auth_timeout(self,auth_timeout):
		try :
			if not isinstance(auth_timeout,int):
				raise TypeError("auth_timeout must be set to int value")
			self._auth_timeout = auth_timeout
		except Exception as e :
			raise e


	'''
	get LDAP group search subattribute. Used to determine to which groups a group belongs.
	'''
	@property
	def group_search_subattribute(self) :
		try:
			return self._group_search_subattribute
		except Exception as e :
			raise e
	'''
	set LDAP group search subattribute. Used to determine to which groups a group belongs.
	'''
	@group_search_subattribute.setter
	def group_search_subattribute(self,group_search_subattribute):
		try :
			if not isinstance(group_search_subattribute,str):
				raise TypeError("group_search_subattribute must be set to str value")
			self._group_search_subattribute = group_search_subattribute
		except Exception as e :
			raise e


	'''
	get Enable following LDAP referrals received from LDAP server
	'''
	@property
	def follow_referrals(self) :
		try:
			return self._follow_referrals
		except Exception as e :
			raise e
	'''
	set Enable following LDAP referrals received from LDAP server
	'''
	@follow_referrals.setter
	def follow_referrals(self,follow_referrals):
		try :
			if not isinstance(follow_referrals,bool):
				raise TypeError("follow_referrals must be set to bool value")
			self._follow_referrals = follow_referrals
		except Exception as e :
			raise e


	'''
	get The String to be combined with the default LDAP user search string to form the value
	'''
	@property
	def search_filter(self) :
		try:
			return self._search_filter
		except Exception as e :
			raise e
	'''
	set The String to be combined with the default LDAP user search string to form the value
	'''
	@search_filter.setter
	def search_filter(self,search_filter):
		try :
			if not isinstance(search_filter,str):
				raise TypeError("search_filter must be set to str value")
			self._search_filter = search_filter
		except Exception as e :
			raise e


	'''
	get The Attribute name for group extraction from the LDAP server
	'''
	@property
	def group_attr_name(self) :
		try:
			return self._group_attr_name
		except Exception as e :
			raise e
	'''
	set The Attribute name for group extraction from the LDAP server
	'''
	@group_attr_name.setter
	def group_attr_name(self,group_attr_name):
		try :
			if not isinstance(group_attr_name,str):
				raise TypeError("group_attr_name must be set to str value")
			self._group_attr_name = group_attr_name
		except Exception as e :
			raise e


	'''
	get Host Name on the certificate from LDAP Server
	'''
	@property
	def ldap_host_name(self) :
		try:
			return self._ldap_host_name
		except Exception as e :
			raise e
	'''
	set Host Name on the certificate from LDAP Server
	'''
	@ldap_host_name.setter
	def ldap_host_name(self,ldap_host_name):
		try :
			if not isinstance(ldap_host_name,str):
				raise TypeError("ldap_host_name must be set to str value")
			self._ldap_host_name = ldap_host_name
		except Exception as e :
			raise e


	'''
	get Enable change of the user
	'''
	@property
	def change_password(self) :
		try:
			return self._change_password
		except Exception as e :
			raise e
	'''
	set Enable change of the user
	'''
	@change_password.setter
	def change_password(self,change_password):
		try :
			if not isinstance(change_password,bool):
				raise TypeError("change_password must be set to bool value")
			self._change_password = change_password
		except Exception as e :
			raise e


	'''
	get This is the default group
	'''
	@property
	def default_authentication_group(self) :
		try:
			return self._default_authentication_group
		except Exception as e :
			raise e
	'''
	set This is the default group
	'''
	@default_authentication_group.setter
	def default_authentication_group(self,default_authentication_group):
		try :
			if not isinstance(default_authentication_group,str):
				raise TypeError("default_authentication_group must be set to str value")
			self._default_authentication_group = default_authentication_group
		except Exception as e :
			raise e


	'''
	get Number of levels at which group extraction is allowed
	'''
	@property
	def max_nesting_level(self) :
		try:
			return self._max_nesting_level
		except Exception as e :
			raise e
	'''
	set Number of levels at which group extraction is allowed
	'''
	@max_nesting_level.setter
	def max_nesting_level(self,max_nesting_level):
		try :
			if not isinstance(max_nesting_level,int):
				raise TypeError("max_nesting_level must be set to int value")
			self._max_nesting_level = max_nesting_level
		except Exception as e :
			raise e


	'''
	get The name attribute used by the system to query the external LDAP server
	'''
	@property
	def login_name(self) :
		try:
			return self._login_name
		except Exception as e :
			raise e
	'''
	set The name attribute used by the system to query the external LDAP server
	'''
	@login_name.setter
	def login_name(self,login_name):
		try :
			if not isinstance(login_name,str):
				raise TypeError("login_name must be set to str value")
			self._login_name = login_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the ldap servers
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the ldap servers
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
	get The IP address of the LDAP server.
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set The IP address of the LDAP server.
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
	get Enable Nested Group Extraction
	'''
	@property
	def nested_group_extraction(self) :
		try:
			return self._nested_group_extraction
		except Exception as e :
			raise e
	'''
	set Enable Nested Group Extraction
	'''
	@nested_group_extraction.setter
	def nested_group_extraction(self,nested_group_extraction):
		try :
			if not isinstance(nested_group_extraction,bool):
				raise TypeError("nested_group_extraction must be set to bool value")
			self._nested_group_extraction = nested_group_extraction
		except Exception as e :
			raise e


	'''
	get LDAP group search attribute. Used to determine to which groups a group belongs
	'''
	@property
	def group_search_attribute(self) :
		try:
			return self._group_search_attribute
		except Exception as e :
			raise e
	'''
	set LDAP group search attribute. Used to determine to which groups a group belongs
	'''
	@group_search_attribute.setter
	def group_search_attribute(self,group_search_attribute):
		try :
			if not isinstance(group_search_attribute,str):
				raise TypeError("group_search_attribute must be set to str value")
			self._group_search_attribute = group_search_attribute
		except Exception as e :
			raise e


	'''
	get Name that uniquely identifies a group in LDAP server
	'''
	@property
	def group_name_identifier(self) :
		try:
			return self._group_name_identifier
		except Exception as e :
			raise e
	'''
	set Name that uniquely identifies a group in LDAP server
	'''
	@group_name_identifier.setter
	def group_name_identifier(self,group_name_identifier):
		try :
			if not isinstance(group_name_identifier,str):
				raise TypeError("group_name_identifier must be set to str value")
			self._group_name_identifier = group_name_identifier
		except Exception as e :
			raise e


	'''
	get The Sub-Attribute name for group extraction from LDAP server
	'''
	@property
	def subattribute_name(self) :
		try:
			return self._subattribute_name
		except Exception as e :
			raise e
	'''
	set The Sub-Attribute name for group extraction from LDAP server
	'''
	@subattribute_name.setter
	def subattribute_name(self,subattribute_name):
		try :
			if not isinstance(subattribute_name,str):
				raise TypeError("subattribute_name must be set to str value")
			self._subattribute_name = subattribute_name
		except Exception as e :
			raise e


	'''
	get Name of LDAP server
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of LDAP server
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Validate LDAP Server Certificate
	'''
	@property
	def validate_ldap_server_certs(self) :
		try:
			return self._validate_ldap_server_certs
		except Exception as e :
			raise e
	'''
	set Validate LDAP Server Certificate
	'''
	@validate_ldap_server_certs.setter
	def validate_ldap_server_certs(self,validate_ldap_server_certs):
		try :
			if not isinstance(validate_ldap_server_certs,bool):
				raise TypeError("validate_ldap_server_certs must be set to bool value")
			self._validate_ldap_server_certs = validate_ldap_server_certs
		except Exception as e :
			raise e


	'''
	get String to be combined with the default LDAP group search string to form the search value
	'''
	@property
	def group_search_filter(self) :
		try:
			return self._group_search_filter
		except Exception as e :
			raise e
	'''
	set String to be combined with the default LDAP group search string to form the search value
	'''
	@group_search_filter.setter
	def group_search_filter(self,group_search_filter):
		try :
			if not isinstance(group_search_filter,str):
				raise TypeError("group_search_filter must be set to str value")
			self._group_search_filter = group_search_filter
		except Exception as e :
			raise e


	'''
	get The full distinguished name used to bind to the LDAP server
	'''
	@property
	def bind_dn(self) :
		try:
			return self._bind_dn
		except Exception as e :
			raise e
	'''
	set The full distinguished name used to bind to the LDAP server
	'''
	@bind_dn.setter
	def bind_dn(self,bind_dn):
		try :
			if not isinstance(bind_dn,str):
				raise TypeError("bind_dn must be set to str value")
			self._bind_dn = bind_dn
		except Exception as e :
			raise e


	'''
	get The port number on which the LDAP server is running
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set The port number on which the LDAP server is running
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get The base or node where the ldapsearch should start
	'''
	@property
	def base_dn(self) :
		try:
			return self._base_dn
		except Exception as e :
			raise e
	'''
	set The base or node where the ldapsearch should start
	'''
	@base_dn.setter
	def base_dn(self,base_dn):
		try :
			if not isinstance(base_dn,str):
				raise TypeError("base_dn must be set to str value")
			self._base_dn = base_dn
		except Exception as e :
			raise e


	'''
	get The communication type between the system and the LDAP server
	'''
	@property
	def sec_type(self) :
		try:
			return self._sec_type
		except Exception as e :
			raise e
	'''
	set The communication type between the system and the LDAP server
	'''
	@sec_type.setter
	def sec_type(self,sec_type):
		try :
			if not isinstance(sec_type,str):
				raise TypeError("sec_type must be set to str value")
			self._sec_type = sec_type
		except Exception as e :
			raise e


	'''
	get Maximum number of ldap referrals to follow
	'''
	@property
	def max_ldap_referrals(self) :
		try:
			return self._max_ldap_referrals
		except Exception as e :
			raise e
	'''
	set Maximum number of ldap referrals to follow
	'''
	@max_ldap_referrals.setter
	def max_ldap_referrals(self,max_ldap_referrals):
		try :
			if not isinstance(max_ldap_referrals,int):
				raise TypeError("max_ldap_referrals must be set to int value")
			self._max_ldap_referrals = max_ldap_referrals
		except Exception as e :
			raise e


	'''
	get The type of LDAP server
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set The type of LDAP server
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get The password used to bind to the LDAP server
	'''
	@property
	def bind_passwd(self) :
		try:
			return self._bind_passwd
		except Exception as e :
			raise e
	'''
	set The password used to bind to the LDAP server
	'''
	@bind_passwd.setter
	def bind_passwd(self,bind_passwd):
		try :
			if not isinstance(bind_passwd,str):
				raise TypeError("bind_passwd must be set to str value")
			self._bind_passwd = bind_passwd
		except Exception as e :
			raise e


	'''
	get Configuration Type. Values: 0: IPv4, 1: IPv6
	'''
	@property
	def address_type(self) :
		try:
			return self._address_type
		except Exception as e :
			raise e

	'''
	Use this operation to add LDAP server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ldap_server_obj= ldap_server()
				return cls.perform_operation_bulk_request(service,"add", resource,ldap_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete LDAP server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ldap_server_obj=ldap_server()
					return cls.delete_bulk_request(client,resource,ldap_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get LDAP server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ldap_server_obj=ldap_server()
				response = ldap_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify LDAP server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ldap_server_obj=ldap_server()
				return cls.update_bulk_request(client,resource,ldap_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ldap_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ldap_server_obj = ldap_server()
			option_ = options()
			option_._filter=filter_
			return ldap_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ldap_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ldap_server_obj = ldap_server()
			option_ = options()
			option_._count=True
			response = ldap_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ldap_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ldap_server_obj = ldap_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ldap_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ldap_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ldap_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ldap_server_responses, response, "ldap_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ldap_server_response_array
				i=0
				error = [ldap_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ldap_server_response_array
			i=0
			ldap_server_objs = [ldap_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ldap_server'):
					for props in obj._ldap_server:
						result = service.payload_formatter.string_to_bulk_resource(ldap_server_response,self.__class__.__name__,props)
						ldap_server_objs[i] = result.ldap_server
						i=i+1
			return ldap_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ldap_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ldap_server_response(base_response):
	def __init__(self,length=1) :
		self.ldap_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ldap_server= [ ldap_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ldap_server_responses(base_response):
	def __init__(self,length=1) :
		self.ldap_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ldap_server_response_array = [ ldap_server() for _ in range(length)]
