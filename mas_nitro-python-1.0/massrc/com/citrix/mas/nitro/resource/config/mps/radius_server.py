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
Configuration for Radius Server configuration resource
'''

class radius_server(base_resource):
	_auth_timeout= ""
	_group_separator= ""
	_pass_encoding= ""
	_enable_nas_ip= ""
	_radius_key= ""
	_default_authentication_group= ""
	_ip_vendor_id= ""
	_id= ""
	_ip_address= ""
	_ip_attribute_type= ""
	_attribute_type= ""
	_nas_id= ""
	_vendor_id= ""
	_name= ""
	_port= ""
	_groups_prefix= ""
	_pwd_vendor_id= ""
	_pwd_attribute_type= ""
	_accounting= ""
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
			return "radius_server"
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
			return "radius_servers"
		except Exception as e :
			raise e



	'''
	get The maximum number of seconds the system will wait for a response from the Radius server
	'''
	@property
	def auth_timeout(self) :
		try:
			return self._auth_timeout
		except Exception as e :
			raise e
	'''
	set The maximum number of seconds the system will wait for a response from the Radius server
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
	get  Group separator string that delimits group names within a RADIUS attribute for RADIUS group extraction
	'''
	@property
	def group_separator(self) :
		try:
			return self._group_separator
		except Exception as e :
			raise e
	'''
	set  Group separator string that delimits group names within a RADIUS attribute for RADIUS group extraction
	'''
	@group_separator.setter
	def group_separator(self,group_separator):
		try :
			if not isinstance(group_separator,str):
				raise TypeError("group_separator must be set to str value")
			self._group_separator = group_separator
		except Exception as e :
			raise e


	'''
	get Enable password encoding in RADIUS packets send to the RADIUS server
	'''
	@property
	def pass_encoding(self) :
		try:
			return self._pass_encoding
		except Exception as e :
			raise e
	'''
	set Enable password encoding in RADIUS packets send to the RADIUS server
	'''
	@pass_encoding.setter
	def pass_encoding(self,pass_encoding):
		try :
			if not isinstance(pass_encoding,str):
				raise TypeError("pass_encoding must be set to str value")
			self._pass_encoding = pass_encoding
		except Exception as e :
			raise e


	'''
	get Enable NAS IP extraction
	'''
	@property
	def enable_nas_ip(self) :
		try:
			return self._enable_nas_ip
		except Exception as e :
			raise e
	'''
	set Enable NAS IP extraction
	'''
	@enable_nas_ip.setter
	def enable_nas_ip(self,enable_nas_ip):
		try :
			if not isinstance(enable_nas_ip,bool):
				raise TypeError("enable_nas_ip must be set to bool value")
			self._enable_nas_ip = enable_nas_ip
		except Exception as e :
			raise e


	'''
	get Key of radius server
	'''
	@property
	def radius_key(self) :
		try:
			return self._radius_key
		except Exception as e :
			raise e
	'''
	set Key of radius server
	'''
	@radius_key.setter
	def radius_key(self,radius_key):
		try :
			if not isinstance(radius_key,str):
				raise TypeError("radius_key must be set to str value")
			self._radius_key = radius_key
		except Exception as e :
			raise e


	'''
	get This is the default group that is chosen when the authentication succeeds in addition to extracted groups
	'''
	@property
	def default_authentication_group(self) :
		try:
			return self._default_authentication_group
		except Exception as e :
			raise e
	'''
	set This is the default group that is chosen when the authentication succeeds in addition to extracted groups
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
	get The vendor ID of the attribute in the RADIUS response which denotes the intranet IP
	'''
	@property
	def ip_vendor_id(self) :
		try:
			return self._ip_vendor_id
		except Exception as e :
			raise e
	'''
	set The vendor ID of the attribute in the RADIUS response which denotes the intranet IP
	'''
	@ip_vendor_id.setter
	def ip_vendor_id(self,ip_vendor_id):
		try :
			if not isinstance(ip_vendor_id,int):
				raise TypeError("ip_vendor_id must be set to int value")
			self._ip_vendor_id = ip_vendor_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the radius servers
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the radius servers
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
	get IP Address of radius server
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address of radius server
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
	get The attribute type of the remote IP address attribute in a RADIUS response
	'''
	@property
	def ip_attribute_type(self) :
		try:
			return self._ip_attribute_type
		except Exception as e :
			raise e
	'''
	set The attribute type of the remote IP address attribute in a RADIUS response
	'''
	@ip_attribute_type.setter
	def ip_attribute_type(self,ip_attribute_type):
		try :
			if not isinstance(ip_attribute_type,int):
				raise TypeError("ip_attribute_type must be set to int value")
			self._ip_attribute_type = ip_attribute_type
		except Exception as e :
			raise e


	'''
	get Attribute type for RADIUS group extraction
	'''
	@property
	def attribute_type(self) :
		try:
			return self._attribute_type
		except Exception as e :
			raise e
	'''
	set Attribute type for RADIUS group extraction
	'''
	@attribute_type.setter
	def attribute_type(self,attribute_type):
		try :
			if not isinstance(attribute_type,int):
				raise TypeError("attribute_type must be set to int value")
			self._attribute_type = attribute_type
		except Exception as e :
			raise e


	'''
	get NAS ID
	'''
	@property
	def nas_id(self) :
		try:
			return self._nas_id
		except Exception as e :
			raise e
	'''
	set NAS ID
	'''
	@nas_id.setter
	def nas_id(self,nas_id):
		try :
			if not isinstance(nas_id,str):
				raise TypeError("nas_id must be set to str value")
			self._nas_id = nas_id
		except Exception as e :
			raise e


	'''
	get Vendor ID for RADIUS group extraction
	'''
	@property
	def vendor_id(self) :
		try:
			return self._vendor_id
		except Exception as e :
			raise e
	'''
	set Vendor ID for RADIUS group extraction
	'''
	@vendor_id.setter
	def vendor_id(self,vendor_id):
		try :
			if not isinstance(vendor_id,int):
				raise TypeError("vendor_id must be set to int value")
			self._vendor_id = vendor_id
		except Exception as e :
			raise e


	'''
	get Name of radius server
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of radius server
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
	get Port number of radius server
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Port number of radius server
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
	get Prefix string that precedes group names within a RADIUS attribute for RADIUS group extraction
	'''
	@property
	def groups_prefix(self) :
		try:
			return self._groups_prefix
		except Exception as e :
			raise e
	'''
	set Prefix string that precedes group names within a RADIUS attribute for RADIUS group extraction
	'''
	@groups_prefix.setter
	def groups_prefix(self,groups_prefix):
		try :
			if not isinstance(groups_prefix,str):
				raise TypeError("groups_prefix must be set to str value")
			self._groups_prefix = groups_prefix
		except Exception as e :
			raise e


	'''
	get Vendor ID of the password in the RADIUS response. Used to extract the user password
	'''
	@property
	def pwd_vendor_id(self) :
		try:
			return self._pwd_vendor_id
		except Exception as e :
			raise e
	'''
	set Vendor ID of the password in the RADIUS response. Used to extract the user password
	'''
	@pwd_vendor_id.setter
	def pwd_vendor_id(self,pwd_vendor_id):
		try :
			if not isinstance(pwd_vendor_id,int):
				raise TypeError("pwd_vendor_id must be set to int value")
			self._pwd_vendor_id = pwd_vendor_id
		except Exception as e :
			raise e


	'''
	get The attribute type of the password attribute in a RADIUS response.
	'''
	@property
	def pwd_attribute_type(self) :
		try:
			return self._pwd_attribute_type
		except Exception as e :
			raise e
	'''
	set The attribute type of the password attribute in a RADIUS response.
	'''
	@pwd_attribute_type.setter
	def pwd_attribute_type(self,pwd_attribute_type):
		try :
			if not isinstance(pwd_attribute_type,int):
				raise TypeError("pwd_attribute_type must be set to int value")
			self._pwd_attribute_type = pwd_attribute_type
		except Exception as e :
			raise e


	'''
	get Enable accounting in the radius server
	'''
	@property
	def accounting(self) :
		try:
			return self._accounting
		except Exception as e :
			raise e
	'''
	set Enable accounting in the radius server
	'''
	@accounting.setter
	def accounting(self,accounting):
		try :
			if not isinstance(accounting,bool):
				raise TypeError("accounting must be set to bool value")
			self._accounting = accounting
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
	Use this operation to add Radius server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				radius_server_obj= radius_server()
				return cls.perform_operation_bulk_request(service,"add", resource,radius_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Radius server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					radius_server_obj=radius_server()
					return cls.delete_bulk_request(client,resource,radius_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Radius server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				radius_server_obj=radius_server()
				response = radius_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify Radius server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				radius_server_obj=radius_server()
				return cls.update_bulk_request(client,resource,radius_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of radius_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			radius_server_obj = radius_server()
			option_ = options()
			option_._filter=filter_
			return radius_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the radius_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			radius_server_obj = radius_server()
			option_ = options()
			option_._count=True
			response = radius_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of radius_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			radius_server_obj = radius_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = radius_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(radius_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.radius_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(radius_server_responses, response, "radius_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.radius_server_response_array
				i=0
				error = [radius_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.radius_server_response_array
			i=0
			radius_server_objs = [radius_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_radius_server'):
					for props in obj._radius_server:
						result = service.payload_formatter.string_to_bulk_resource(radius_server_response,self.__class__.__name__,props)
						radius_server_objs[i] = result.radius_server
						i=i+1
			return radius_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(radius_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class radius_server_response(base_response):
	def __init__(self,length=1) :
		self.radius_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.radius_server= [ radius_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class radius_server_responses(base_response):
	def __init__(self,length=1) :
		self.radius_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.radius_server_response_array = [ radius_server() for _ in range(length)]
