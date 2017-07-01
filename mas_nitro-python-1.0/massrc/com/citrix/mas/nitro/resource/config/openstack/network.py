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
Configuration for Setting of Management Network resource
'''

class network(base_resource):
	_nsm_id= ""
	_subnet_id= ""
	_subnet_cidr= ""
	_segmentation_id= ""
	_name= ""
	_subnet_gateway_ip= ""
	_network_type= ""
	_network_id= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/oca/v1/networks"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "networks"
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
			return "network"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._network_id
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
			return "networks"
		except Exception as e :
			raise e



	'''
	get Id of the nsm client corresponding to the tenant
	'''
	@property
	def nsm_id(self) :
		try:
			return self._nsm_id
		except Exception as e :
			raise e
	'''
	set Id of the nsm client corresponding to the tenant
	'''
	@nsm_id.setter
	def nsm_id(self,nsm_id):
		try :
			if not isinstance(nsm_id,str):
				raise TypeError("nsm_id must be set to str value")
			self._nsm_id = nsm_id
		except Exception as e :
			raise e


	'''
	get Id of the subnet of the network
	'''
	@property
	def subnet_id(self) :
		try:
			return self._subnet_id
		except Exception as e :
			raise e
	'''
	set Id of the subnet of the network
	'''
	@subnet_id.setter
	def subnet_id(self,subnet_id):
		try :
			if not isinstance(subnet_id,str):
				raise TypeError("subnet_id must be set to str value")
			self._subnet_id = subnet_id
		except Exception as e :
			raise e


	'''
	get subnet range
	'''
	@property
	def subnet_cidr(self) :
		try:
			return self._subnet_cidr
		except Exception as e :
			raise e
	'''
	set subnet range
	'''
	@subnet_cidr.setter
	def subnet_cidr(self,subnet_cidr):
		try :
			if not isinstance(subnet_cidr,str):
				raise TypeError("subnet_cidr must be set to str value")
			self._subnet_cidr = subnet_cidr
		except Exception as e :
			raise e


	'''
	get Segmentation id of the network
	'''
	@property
	def segmentation_id(self) :
		try:
			return self._segmentation_id
		except Exception as e :
			raise e
	'''
	set Segmentation id of the network
	'''
	@segmentation_id.setter
	def segmentation_id(self,segmentation_id):
		try :
			if not isinstance(segmentation_id,str):
				raise TypeError("segmentation_id must be set to str value")
			self._segmentation_id = segmentation_id
		except Exception as e :
			raise e


	'''
	get name of the network
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name of the network
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
	get The IP of the gateway of subnet
	'''
	@property
	def subnet_gateway_ip(self) :
		try:
			return self._subnet_gateway_ip
		except Exception as e :
			raise e
	'''
	set The IP of the gateway of subnet
	'''
	@subnet_gateway_ip.setter
	def subnet_gateway_ip(self,subnet_gateway_ip):
		try :
			if not isinstance(subnet_gateway_ip,str):
				raise TypeError("subnet_gateway_ip must be set to str value")
			self._subnet_gateway_ip = subnet_gateway_ip
		except Exception as e :
			raise e


	'''
	get network type of the network
	'''
	@property
	def network_type(self) :
		try:
			return self._network_type
		except Exception as e :
			raise e
	'''
	set network type of the network
	'''
	@network_type.setter
	def network_type(self,network_type):
		try :
			if not isinstance(network_type,str):
				raise TypeError("network_type must be set to str value")
			self._network_type = network_type
		except Exception as e :
			raise e


	'''
	get Id of the network
	'''
	@property
	def network_id(self) :
		try:
			return self._network_id
		except Exception as e :
			raise e
	'''
	set Id of the network
	'''
	@network_id.setter
	def network_id(self,network_id):
		try :
			if not isinstance(network_id,str):
				raise TypeError("network_id must be set to str value")
			self._network_id = network_id
		except Exception as e :
			raise e

	'''
	Use this operation to add a network.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				network_obj= network()
				return cls.perform_operation_bulk_request(service,"add", resource,network_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a network.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					network_obj=network()
					return cls.delete_bulk_request(client,resource,network_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get network details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_obj=network()
				response = network_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_obj = network()
			option_ = options()
			option_._filter=filter_
			return network_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_obj = network()
			option_ = options()
			option_._count=True
			response = network_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_obj = network()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_responses, response, "network_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_response_array
				i=0
				error = [network() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_response_array
			i=0
			network_objs = [network() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network'):
					for props in obj._network:
						result = service.payload_formatter.string_to_bulk_resource(network_response,self.__class__.__name__,props)
						network_objs[i] = result.network
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_response(base_response):
	def __init__(self,length=1) :
		self.network= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network= [ network() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_responses(base_response):
	def __init__(self,length=1) :
		self.network_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_response_array = [ network() for _ in range(length)]
