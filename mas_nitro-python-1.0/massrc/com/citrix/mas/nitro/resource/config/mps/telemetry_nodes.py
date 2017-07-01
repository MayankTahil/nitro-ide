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
Configuration for This table holds details of Telemetry nodes. resource
'''

class telemetry_nodes(base_resource):
	_ip_address= ""
	_id= ""
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
			return "telemetry_nodes"
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
			return "telemetry_nodess"
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
	get Id is system generated key for all the Telemetry nodes
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Telemetry nodes
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
	Use this operation to add the Telemetry node to db.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				telemetry_nodes_obj= telemetry_nodes()
				return cls.perform_operation_bulk_request(service,"add", resource,telemetry_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Telemetry node.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					telemetry_nodes_obj=telemetry_nodes()
					return cls.delete_bulk_request(client,resource,telemetry_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Telemetry nodes..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				telemetry_nodes_obj=telemetry_nodes()
				response = telemetry_nodes_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of telemetry_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			telemetry_nodes_obj = telemetry_nodes()
			option_ = options()
			option_._filter=filter_
			return telemetry_nodes_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the telemetry_nodes resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			telemetry_nodes_obj = telemetry_nodes()
			option_ = options()
			option_._count=True
			response = telemetry_nodes_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of telemetry_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			telemetry_nodes_obj = telemetry_nodes()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = telemetry_nodes_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(telemetry_nodes_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.telemetry_nodes
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(telemetry_nodes_responses, response, "telemetry_nodes_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.telemetry_nodes_response_array
				i=0
				error = [telemetry_nodes() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.telemetry_nodes_response_array
			i=0
			telemetry_nodes_objs = [telemetry_nodes() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_telemetry_nodes'):
					for props in obj._telemetry_nodes:
						result = service.payload_formatter.string_to_bulk_resource(telemetry_nodes_response,self.__class__.__name__,props)
						telemetry_nodes_objs[i] = result.telemetry_nodes
						i=i+1
			return telemetry_nodes_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(telemetry_nodes,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class telemetry_nodes_response(base_response):
	def __init__(self,length=1) :
		self.telemetry_nodes= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.telemetry_nodes= [ telemetry_nodes() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class telemetry_nodes_responses(base_response):
	def __init__(self,length=1) :
		self.telemetry_nodes_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.telemetry_nodes_response_array = [ telemetry_nodes() for _ in range(length)]
