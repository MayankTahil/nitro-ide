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
Configuration for TACACS Server configuration resource
'''

class tacacs_server(base_resource):
	_tacacs_key= ""
	_auth_timeout= ""
	_name= ""
	_port= ""
	_id= ""
	_ip_address= ""
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
			return "tacacs_server"
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
			return "tacacs_servers"
		except Exception as e :
			raise e



	'''
	get Key shared between the TACACS+ server and clients
	'''
	@property
	def tacacs_key(self) :
		try:
			return self._tacacs_key
		except Exception as e :
			raise e
	'''
	set Key shared between the TACACS+ server and clients
	'''
	@tacacs_key.setter
	def tacacs_key(self,tacacs_key):
		try :
			if not isinstance(tacacs_key,str):
				raise TypeError("tacacs_key must be set to str value")
			self._tacacs_key = tacacs_key
		except Exception as e :
			raise e


	'''
	get The maximum number of seconds the system will wait for a response from the TACACS server
	'''
	@property
	def auth_timeout(self) :
		try:
			return self._auth_timeout
		except Exception as e :
			raise e
	'''
	set The maximum number of seconds the system will wait for a response from the TACACS server
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
	get Name of TACACS server
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of TACACS server
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
	get port number of TACACS server
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set port number of TACACS server
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
	get Id is system generated key for all the TACACS servers
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the TACACS servers
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
	get IP Address of TACACS server
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address of TACACS server
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
	get Enable accounting in the tacacs server
	'''
	@property
	def accounting(self) :
		try:
			return self._accounting
		except Exception as e :
			raise e
	'''
	set Enable accounting in the tacacs server
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
	Use this operation to add TACACS server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				tacacs_server_obj= tacacs_server()
				return cls.perform_operation_bulk_request(service,"add", resource,tacacs_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete TACACS server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					tacacs_server_obj=tacacs_server()
					return cls.delete_bulk_request(client,resource,tacacs_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get TACACS server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tacacs_server_obj=tacacs_server()
				response = tacacs_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify TACACS server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				tacacs_server_obj=tacacs_server()
				return cls.update_bulk_request(client,resource,tacacs_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tacacs_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tacacs_server_obj = tacacs_server()
			option_ = options()
			option_._filter=filter_
			return tacacs_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tacacs_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tacacs_server_obj = tacacs_server()
			option_ = options()
			option_._count=True
			response = tacacs_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tacacs_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tacacs_server_obj = tacacs_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tacacs_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tacacs_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tacacs_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tacacs_server_responses, response, "tacacs_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tacacs_server_response_array
				i=0
				error = [tacacs_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tacacs_server_response_array
			i=0
			tacacs_server_objs = [tacacs_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tacacs_server'):
					for props in obj._tacacs_server:
						result = service.payload_formatter.string_to_bulk_resource(tacacs_server_response,self.__class__.__name__,props)
						tacacs_server_objs[i] = result.tacacs_server
						i=i+1
			return tacacs_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tacacs_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tacacs_server_response(base_response):
	def __init__(self,length=1) :
		self.tacacs_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tacacs_server= [ tacacs_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tacacs_server_responses(base_response):
	def __init__(self,length=1) :
		self.tacacs_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tacacs_server_response_array = [ tacacs_server() for _ in range(length)]
