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
Configuration for Network Service LB Config resource
'''

class network_service_lb_config(base_resource):
	_lb_subnet_ip= ""
	_lb_port= ""
	_service_ip_address= ""
	_network_service_name= ""
	_parent_id= ""
	_formation_template_id= ""
	_lb_protocol= ""
	_id= ""
	_lb_method= ""
	_parent_name= ""
	_lb_serviceinterface_id= ""
	_network_service_id= ""
	_lb_persistence_method= ""
	_service= ""
	_lb_clientinterface_id= ""
	_lb_virtual_ip= ""
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
			return "network_service_lb_config"
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
			return "network_service_lb_configs"
		except Exception as e :
			raise e



	'''
	get Reference to obtain LB Subnet IP
	'''
	@property
	def lb_subnet_ip(self) :
		try:
			return self._lb_subnet_ip
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Subnet IP
	'''
	@lb_subnet_ip.setter
	def lb_subnet_ip(self,lb_subnet_ip):
		try :
			if not isinstance(lb_subnet_ip,str):
				raise TypeError("lb_subnet_ip must be set to str value")
			self._lb_subnet_ip = lb_subnet_ip
		except Exception as e :
			raise e


	'''
	get Reference to obtain LB Port
	'''
	@property
	def lb_port(self) :
		try:
			return self._lb_port
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Port
	'''
	@lb_port.setter
	def lb_port(self,lb_port):
		try :
			if not isinstance(lb_port,str):
				raise TypeError("lb_port must be set to str value")
			self._lb_port = lb_port
		except Exception as e :
			raise e


	'''
	get Reference to obtain service ip address
	'''
	@property
	def service_ip_address(self) :
		try:
			return self._service_ip_address
		except Exception as e :
			raise e
	'''
	set Reference to obtain service ip address
	'''
	@service_ip_address.setter
	def service_ip_address(self,service_ip_address):
		try :
			if not isinstance(service_ip_address,str):
				raise TypeError("service_ip_address must be set to str value")
			self._service_ip_address = service_ip_address
		except Exception as e :
			raise e


	'''
	get Network Service Name
	'''
	@property
	def network_service_name(self) :
		try:
			return self._network_service_name
		except Exception as e :
			raise e
	'''
	set Network Service Name
	'''
	@network_service_name.setter
	def network_service_name(self,network_service_name):
		try :
			if not isinstance(network_service_name,str):
				raise TypeError("network_service_name must be set to str value")
			self._network_service_name = network_service_name
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Formation Template ID
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set Formation Template ID
	'''
	@formation_template_id.setter
	def formation_template_id(self,formation_template_id):
		try :
			if not isinstance(formation_template_id,str):
				raise TypeError("formation_template_id must be set to str value")
			self._formation_template_id = formation_template_id
		except Exception as e :
			raise e


	'''
	get Reference to obtain LB Protocol
	'''
	@property
	def lb_protocol(self) :
		try:
			return self._lb_protocol
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Protocol
	'''
	@lb_protocol.setter
	def lb_protocol(self,lb_protocol):
		try :
			if not isinstance(lb_protocol,str):
				raise TypeError("lb_protocol must be set to str value")
			self._lb_protocol = lb_protocol
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get Reference to obtain LB Method
	'''
	@property
	def lb_method(self) :
		try:
			return self._lb_method
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Method
	'''
	@lb_method.setter
	def lb_method(self,lb_method):
		try :
			if not isinstance(lb_method,str):
				raise TypeError("lb_method must be set to str value")
			self._lb_method = lb_method
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Reference to LB Service Interface ID
	'''
	@property
	def lb_serviceinterface_id(self) :
		try:
			return self._lb_serviceinterface_id
		except Exception as e :
			raise e
	'''
	set Reference to LB Service Interface ID
	'''
	@lb_serviceinterface_id.setter
	def lb_serviceinterface_id(self,lb_serviceinterface_id):
		try :
			if not isinstance(lb_serviceinterface_id,int):
				raise TypeError("lb_serviceinterface_id must be set to int value")
			self._lb_serviceinterface_id = lb_serviceinterface_id
		except Exception as e :
			raise e


	'''
	get Network Service ID
	'''
	@property
	def network_service_id(self) :
		try:
			return self._network_service_id
		except Exception as e :
			raise e
	'''
	set Network Service ID
	'''
	@network_service_id.setter
	def network_service_id(self,network_service_id):
		try :
			if not isinstance(network_service_id,str):
				raise TypeError("network_service_id must be set to str value")
			self._network_service_id = network_service_id
		except Exception as e :
			raise e


	'''
	get Reference to obtain LB Persistence Method
	'''
	@property
	def lb_persistence_method(self) :
		try:
			return self._lb_persistence_method
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Persistence Method
	'''
	@lb_persistence_method.setter
	def lb_persistence_method(self,lb_persistence_method):
		try :
			if not isinstance(lb_persistence_method,str):
				raise TypeError("lb_persistence_method must be set to str value")
			self._lb_persistence_method = lb_persistence_method
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def service(self) :
		try:
			return self._service
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@service.setter
	def service(self,service):
		try :
			if not isinstance(service,str):
				raise TypeError("service must be set to str value")
			self._service = service
		except Exception as e :
			raise e


	'''
	get Reference to LB Client Interface ID
	'''
	@property
	def lb_clientinterface_id(self) :
		try:
			return self._lb_clientinterface_id
		except Exception as e :
			raise e
	'''
	set Reference to LB Client Interface ID
	'''
	@lb_clientinterface_id.setter
	def lb_clientinterface_id(self,lb_clientinterface_id):
		try :
			if not isinstance(lb_clientinterface_id,int):
				raise TypeError("lb_clientinterface_id must be set to int value")
			self._lb_clientinterface_id = lb_clientinterface_id
		except Exception as e :
			raise e


	'''
	get Reference to obtain LB Virtual IP
	'''
	@property
	def lb_virtual_ip(self) :
		try:
			return self._lb_virtual_ip
		except Exception as e :
			raise e
	'''
	set Reference to obtain LB Virtual IP
	'''
	@lb_virtual_ip.setter
	def lb_virtual_ip(self,lb_virtual_ip):
		try :
			if not isinstance(lb_virtual_ip,str):
				raise TypeError("lb_virtual_ip must be set to str value")
			self._lb_virtual_ip = lb_virtual_ip
		except Exception as e :
			raise e

	'''
	Use this operation to get the network service lb config.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_service_lb_config_obj=network_service_lb_config()
				response = network_service_lb_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_service_lb_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_service_lb_config_obj = network_service_lb_config()
			option_ = options()
			option_._filter=filter_
			return network_service_lb_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_service_lb_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_service_lb_config_obj = network_service_lb_config()
			option_ = options()
			option_._count=True
			response = network_service_lb_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_service_lb_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_service_lb_config_obj = network_service_lb_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_service_lb_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_service_lb_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_service_lb_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_service_lb_config_responses, response, "network_service_lb_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_service_lb_config_response_array
				i=0
				error = [network_service_lb_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_service_lb_config_response_array
			i=0
			network_service_lb_config_objs = [network_service_lb_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_service_lb_config'):
					for props in obj._network_service_lb_config:
						result = service.payload_formatter.string_to_bulk_resource(network_service_lb_config_response,self.__class__.__name__,props)
						network_service_lb_config_objs[i] = result.network_service_lb_config
						i=i+1
			return network_service_lb_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_service_lb_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_service_lb_config_response(base_response):
	def __init__(self,length=1) :
		self.network_service_lb_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_service_lb_config= [ network_service_lb_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_service_lb_config_responses(base_response):
	def __init__(self,length=1) :
		self.network_service_lb_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_service_lb_config_response_array = [ network_service_lb_config() for _ in range(length)]
