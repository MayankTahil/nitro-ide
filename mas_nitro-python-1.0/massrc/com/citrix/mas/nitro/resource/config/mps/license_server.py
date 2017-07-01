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
Configuration for License server information resource
'''

class license_server(base_resource):
	_grace_time_left= ""
	_server= ""
	_id= ""
	_connection_status= ""
	_grace= ""
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
			return "license_server"
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
			return "license_servers"
		except Exception as e :
			raise e



	'''
	get grace time remaining left in Hours
	'''
	@property
	def grace_time_left(self) :
		try:
			return self._grace_time_left
		except Exception as e :
			raise e


	'''
	get Server/IP address of License server
	'''
	@property
	def server(self) :
		try:
			return self._server
		except Exception as e :
			raise e
	'''
	set Server/IP address of License server
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
	get License server is connected
	'''
	@property
	def connection_status(self) :
		try:
			return self._connection_status
		except Exception as e :
			raise e


	'''
	get Box is running on grace
	'''
	@property
	def grace(self) :
		try:
			return self._grace
		except Exception as e :
			raise e


	'''
	get License port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set License port
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
	Use this operation to add License server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				license_server_obj= license_server()
				return cls.perform_operation_bulk_request(service,"add", resource,license_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete License server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					license_server_obj=license_server()
					return cls.delete_bulk_request(client,resource,license_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get License server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_server_obj=license_server()
				response = license_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify License server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				license_server_obj=license_server()
				return cls.update_bulk_request(client,resource,license_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_server_obj = license_server()
			option_ = options()
			option_._filter=filter_
			return license_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_server_obj = license_server()
			option_ = options()
			option_._count=True
			response = license_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_server_obj = license_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_server_responses, response, "license_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_server_response_array
				i=0
				error = [license_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_server_response_array
			i=0
			license_server_objs = [license_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_server'):
					for props in obj._license_server:
						result = service.payload_formatter.string_to_bulk_resource(license_server_response,self.__class__.__name__,props)
						license_server_objs[i] = result.license_server
						i=i+1
			return license_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_server_response(base_response):
	def __init__(self,length=1) :
		self.license_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_server= [ license_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_server_responses(base_response):
	def __init__(self,length=1) :
		self.license_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_server_response_array = [ license_server() for _ in range(length)]
