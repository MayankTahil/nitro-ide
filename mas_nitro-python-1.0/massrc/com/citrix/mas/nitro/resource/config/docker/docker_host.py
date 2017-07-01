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

from massrc.com.citrix.mas.nitro.resource.config.mps.host_device import host_device

'''
Configuration for docker host details resource
'''

class docker_host(host_device):
	_container_ids= ""
	_remote_api_port= ""
	_ssl_private_key= ""
	_passphrase= ""
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
			return "docker_host"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(docker_host,self).get_object_id()
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
			return "docker_hosts"
		except Exception as e :
			raise e



	'''
	get IDs of containers on this docker host.
	'''
	@property
	def container_ids(self) :
		try:
			return self._container_ids
		except Exception as e :
			raise e


	'''
	get Remote api port on the docker host.
	'''
	@property
	def remote_api_port(self) :
		try:
			return self._remote_api_port
		except Exception as e :
			raise e
	'''
	set Remote api port on the docker host.
	'''
	@remote_api_port.setter
	def remote_api_port(self,remote_api_port):
		try :
			if not isinstance(remote_api_port,int):
				raise TypeError("remote_api_port must be set to int value")
			self._remote_api_port = remote_api_port
		except Exception as e :
			raise e

	'''
	SSL Private Key for key based authentication
	'''
	@property
	def ssl_private_key(self):
		try:
			return self._ssl_private_key
		except Exception as e :
			raise e
	'''
	SSL Private Key for key based authentication
	'''
	@ssl_private_key.setter
	def ssl_private_key(self,ssl_private_key):
		try :
			if not isinstance(ssl_private_key,str):
				raise TypeError("ssl_private_key must be set to str value")
			self._ssl_private_key = ssl_private_key
		except Exception as e :
			raise e

	'''
	Passphrase with which the private key is encrypted
	'''
	@property
	def passphrase(self):
		try:
			return self._passphrase
		except Exception as e :
			raise e
	'''
	Passphrase with which the private key is encrypted
	'''
	@passphrase.setter
	def passphrase(self,passphrase):
		try :
			if not isinstance(passphrase,str):
				raise TypeError("passphrase must be set to str value")
			self._passphrase = passphrase
		except Exception as e :
			raise e

	'''
	Use this operation to add a Docker host.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				docker_host_obj= docker_host()
				return cls.perform_operation_bulk_request(service,"add", resource,docker_host_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a Docker host.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					docker_host_obj=docker_host()
					return cls.delete_bulk_request(client,resource,docker_host_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get a Docker host.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				docker_host_obj=docker_host()
				response = docker_host_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of docker_host resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			docker_host_obj = docker_host()
			option_ = options()
			option_._filter=filter_
			return docker_host_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the docker_host resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			docker_host_obj = docker_host()
			option_ = options()
			option_._count=True
			response = docker_host_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of docker_host resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			docker_host_obj = docker_host()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = docker_host_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(docker_host_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.docker_host
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(docker_host_responses, response, "docker_host_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.docker_host_response_array
				i=0
				error = [docker_host() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.docker_host_response_array
			i=0
			docker_host_objs = [docker_host() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_docker_host'):
					for props in obj._docker_host:
						result = service.payload_formatter.string_to_bulk_resource(docker_host_response,self.__class__.__name__,props)
						docker_host_objs[i] = result.docker_host
						i=i+1
			return docker_host_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(docker_host,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class docker_host_response(base_response):
	def __init__(self,length=1) :
		self.docker_host= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.docker_host= [ docker_host() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class docker_host_responses(base_response):
	def __init__(self,length=1) :
		self.docker_host_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.docker_host_response_array = [ docker_host() for _ in range(length)]
