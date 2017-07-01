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
Configuration for License proxy configuration resource
'''

class license_proxy_server(base_resource):
	_server= ""
	_id= ""
	_port= ""
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
			return "license_proxy_server"
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
			return "license_proxy_servers"
		except Exception as e :
			raise e



	'''
	get IP address of License Web proxy server
	'''
	@property
	def server(self) :
		try:
			return self._server
		except Exception as e :
			raise e
	'''
	set IP address of License Web proxy server
	'''
	@server.setter
	def server(self,server):
		try :
			if not isinstance(server,str):
				raise TypeError("server must be set to str value")
			self._server = server
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
	get Port number of License Web proxy server
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Port number of License Web proxy server
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
	Use this operation to add License Web proxy server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				license_proxy_server_obj= license_proxy_server()
				return cls.perform_operation_bulk_request(service,"add", resource,license_proxy_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete License Web proxy server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					license_proxy_server_obj=license_proxy_server()
					return cls.delete_bulk_request(client,resource,license_proxy_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get License Web proxy server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_proxy_server_obj=license_proxy_server()
				response = license_proxy_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify License Web proxy server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				license_proxy_server_obj=license_proxy_server()
				return cls.update_bulk_request(client,resource,license_proxy_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_proxy_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_proxy_server_obj = license_proxy_server()
			option_ = options()
			option_._filter=filter_
			return license_proxy_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_proxy_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_proxy_server_obj = license_proxy_server()
			option_ = options()
			option_._count=True
			response = license_proxy_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_proxy_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_proxy_server_obj = license_proxy_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_proxy_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_proxy_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_proxy_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_proxy_server_responses, response, "license_proxy_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_proxy_server_response_array
				i=0
				error = [license_proxy_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_proxy_server_response_array
			i=0
			license_proxy_server_objs = [license_proxy_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_proxy_server'):
					for props in obj._license_proxy_server:
						result = service.payload_formatter.string_to_bulk_resource(license_proxy_server_response,self.__class__.__name__,props)
						license_proxy_server_objs[i] = result.license_proxy_server
						i=i+1
			return license_proxy_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_proxy_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_proxy_server_response(base_response):
	def __init__(self,length=1) :
		self.license_proxy_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_proxy_server= [ license_proxy_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_proxy_server_responses(base_response):
	def __init__(self,length=1) :
		self.license_proxy_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_proxy_server_response_array = [ license_proxy_server() for _ in range(length)]
