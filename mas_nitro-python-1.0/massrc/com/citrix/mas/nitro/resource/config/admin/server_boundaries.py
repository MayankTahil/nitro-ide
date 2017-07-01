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
Configuration for Devices selected for a VIP and Pool should be wired to appropriate networks in order to start serving traffic. Server boundary tell if Control Center has to automatically configure networks on the device.  resource
'''

class server_boundaries(base_resource):
	_topology= ""
	_l3config= ""
	__count=""
	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "server_boundaries"
		except Exception as e :
			raise e

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
			return "server_boundaries"
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
			return "server_boundariess"
		except Exception as e :
			raise e



	'''
	get Topology of server_boundary. The possible values are 'L2' and 'L3'.
	'''
	@property
	def topology(self) :
		try:
			return self._topology
		except Exception as e :
			raise e
	'''
	set Topology of server_boundary. The possible values are 'L2' and 'L3'.
	'''
	@topology.setter
	def topology(self,topology):
		try :
			if not isinstance(topology,str):
				raise TypeError("topology must be set to str value")
			self._topology = topology
		except Exception as e :
			raise e


	'''
	get L3config of server_boundary.
	'''
	@property
	def l3config(self) :
		try:
			return self._l3config
		except Exception as e :
			raise e
	'''
	set L3config of server_boundary.
	'''
	@l3config.setter
	def l3config(self,l3config):
		try :
			if not isinstance(l3config,str):
				raise TypeError("l3config must be set to str value")
			self._l3config = l3config
		except Exception as e :
			raise e

	'''
	Use this operation to get server_boundary details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				server_boundaries_obj=server_boundaries()
				response = server_boundaries_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify server_boundary details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				server_boundaries_obj=resource[0]
				return cls.update_bulk_request(client,resource,server_boundaries_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of server_boundaries resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			server_boundaries_obj = server_boundaries()
			option_ = options()
			option_._filter=filter_
			return server_boundaries_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the server_boundaries resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			server_boundaries_obj = server_boundaries()
			option_ = options()
			option_._count=True
			response = server_boundaries_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of server_boundaries resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			server_boundaries_obj = server_boundaries()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = server_boundaries_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(server_boundaries_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server_boundaries
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_boundaries_responses, response, "server_boundaries_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.server_boundaries_response_array
				i=0
				error = [server_boundaries() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.server_boundaries_response_array
			i=0
			server_boundaries_objs = [server_boundaries() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_server_boundaries'):
					for props in obj._server_boundaries:
						result = service.payload_formatter.string_to_bulk_resource(server_boundaries_response,self.__class__.__name__,props)
						server_boundaries_objs[i] = result.server_boundaries
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(server_boundaries,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class server_boundaries_response(base_response):
	def __init__(self,length=1) :
		self.server_boundaries= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.server_boundaries= [ server_boundaries() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class server_boundaries_responses(base_response):
	def __init__(self,length=1) :
		self.server_boundaries_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.server_boundaries_response_array = [ server_boundaries() for _ in range(length)]
