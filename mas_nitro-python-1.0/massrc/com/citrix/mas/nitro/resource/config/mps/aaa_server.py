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
from massrc.com.citrix.mas.nitro.resource.config.mps.external_server import external_server


'''
Configuration for AAA Server configuration resource
'''

class aaa_server(base_resource):
	_external_servers=[]
	_fallback_local_authentication= ""
	_primary_server_name= ""
	_id= ""
	_primary_server_type= ""
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
			return "aaa_server"
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
			return "aaa_servers"
		except Exception as e :
			raise e



	'''
	get List of external servers
	'''
	@property
	def external_servers(self) :
		try:
			return self._external_servers
		except Exception as e :
			raise e
	'''
	set List of external servers
	'''
	@external_servers.setter
	def external_servers(self,external_servers) :
		try :
			if not isinstance(external_servers,list):
				raise TypeError("external_servers must be set to array of external_server value")
			for item in external_servers :
				if not isinstance(item,external_server):
					raise TypeError("item must be set to external_server value")
			self._external_servers = external_servers
		except Exception as e :
			raise e


	'''
	get Enable local fallback authentication
	'''
	@property
	def fallback_local_authentication(self) :
		try:
			return self._fallback_local_authentication
		except Exception as e :
			raise e
	'''
	set Enable local fallback authentication
	'''
	@fallback_local_authentication.setter
	def fallback_local_authentication(self,fallback_local_authentication):
		try :
			if not isinstance(fallback_local_authentication,bool):
				raise TypeError("fallback_local_authentication must be set to bool value")
			self._fallback_local_authentication = fallback_local_authentication
		except Exception as e :
			raise e


	'''
	get Name of primary server name
	'''
	@property
	def primary_server_name(self) :
		try:
			return self._primary_server_name
		except Exception as e :
			raise e
	'''
	set Name of primary server name
	'''
	@primary_server_name.setter
	def primary_server_name(self,primary_server_name):
		try :
			if not isinstance(primary_server_name,str):
				raise TypeError("primary_server_name must be set to str value")
			self._primary_server_name = primary_server_name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the servers
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the servers
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
	get Type of primary server. Supported types 1. LOCAL 2.RADIUS 3.LDAP 4.TACACS 5.KEYSTONE
	'''
	@property
	def primary_server_type(self) :
		try:
			return self._primary_server_type
		except Exception as e :
			raise e
	'''
	set Type of primary server. Supported types 1. LOCAL 2.RADIUS 3.LDAP 4.TACACS 5.KEYSTONE
	'''
	@primary_server_type.setter
	def primary_server_type(self,primary_server_type):
		try :
			if not isinstance(primary_server_type,str):
				raise TypeError("primary_server_type must be set to str value")
			self._primary_server_type = primary_server_type
		except Exception as e :
			raise e

	'''
	Use this operation to get AAA server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				aaa_server_obj=aaa_server()
				response = aaa_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify AAA server details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				aaa_server_obj=aaa_server()
				return cls.update_bulk_request(client,resource,aaa_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of aaa_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			aaa_server_obj = aaa_server()
			option_ = options()
			option_._filter=filter_
			return aaa_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the aaa_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			aaa_server_obj = aaa_server()
			option_ = options()
			option_._count=True
			response = aaa_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of aaa_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			aaa_server_obj = aaa_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = aaa_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(aaa_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaa_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(aaa_server_responses, response, "aaa_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.aaa_server_response_array
				i=0
				error = [aaa_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.aaa_server_response_array
			i=0
			aaa_server_objs = [aaa_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_aaa_server'):
					for props in obj._aaa_server:
						result = service.payload_formatter.string_to_bulk_resource(aaa_server_response,self.__class__.__name__,props)
						aaa_server_objs[i] = result.aaa_server
						i=i+1
			return aaa_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(aaa_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class aaa_server_response(base_response):
	def __init__(self,length=1) :
		self.aaa_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.aaa_server= [ aaa_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class aaa_server_responses(base_response):
	def __init__(self,length=1) :
		self.aaa_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.aaa_server_response_array = [ aaa_server() for _ in range(length)]
