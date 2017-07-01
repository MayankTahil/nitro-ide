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
from massrc.com.citrix.mas.nitro.resource.config.mps.parameter import parameter


'''
Configuration for Formation Network resource
'''

class formation_network(base_resource):
	_network_iprange= ""
	_name= ""
	_network_type= ""
	_description= ""
	_parameters=[]
	_platform_network_type= ""
	_formation_template_id= ""
	_traffic_type= ""
	_traffic_load= ""
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
			return "formation_network"
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
			return "formation_networks"
		except Exception as e :
			raise e



	'''
	get Network IP Range (In X.Y.*.* or StartIP-EndIP Format)
	'''
	@property
	def network_iprange(self) :
		try:
			return self._network_iprange
		except Exception as e :
			raise e
	'''
	set Network IP Range (In X.Y.*.* or StartIP-EndIP Format)
	'''
	@network_iprange.setter
	def network_iprange(self,network_iprange):
		try :
			if not isinstance(network_iprange,str):
				raise TypeError("network_iprange must be set to str value")
			self._network_iprange = network_iprange
		except Exception as e :
			raise e


	'''
	get Network Pool Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Network Pool Name
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
	get Network Type (External / Internal)
	'''
	@property
	def network_type(self) :
		try:
			return self._network_type
		except Exception as e :
			raise e
	'''
	set Network Type (External / Internal)
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
	get Description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Parameters of the service
	'''
	@property
	def parameters(self) :
		try:
			return self._parameters
		except Exception as e :
			raise e
	'''
	set Parameters of the service
	'''
	@parameters.setter
	def parameters(self,parameters) :
		try :
			if not isinstance(parameters,list):
				raise TypeError("parameters must be set to array of parameter value")
			for item in parameters :
				if not isinstance(item,parameter):
					raise TypeError("item must be set to parameter value")
			self._parameters = parameters
		except Exception as e :
			raise e


	'''
	get Platform Network Type
	'''
	@property
	def platform_network_type(self) :
		try:
			return self._platform_network_type
		except Exception as e :
			raise e
	'''
	set Platform Network Type
	'''
	@platform_network_type.setter
	def platform_network_type(self,platform_network_type):
		try :
			if not isinstance(platform_network_type,str):
				raise TypeError("platform_network_type must be set to str value")
			self._platform_network_type = platform_network_type
		except Exception as e :
			raise e


	'''
	get Template Id
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set Template Id
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
	get Traffic Type (Data / Management)
	'''
	@property
	def traffic_type(self) :
		try:
			return self._traffic_type
		except Exception as e :
			raise e
	'''
	set Traffic Type (Data / Management)
	'''
	@traffic_type.setter
	def traffic_type(self,traffic_type):
		try :
			if not isinstance(traffic_type,str):
				raise TypeError("traffic_type must be set to str value")
			self._traffic_type = traffic_type
		except Exception as e :
			raise e


	'''
	get Traffic Load (low / high)
	'''
	@property
	def traffic_load(self) :
		try:
			return self._traffic_load
		except Exception as e :
			raise e
	'''
	set Traffic Load (low / high)
	'''
	@traffic_load.setter
	def traffic_load(self,traffic_load):
		try :
			if not isinstance(traffic_load,str):
				raise TypeError("traffic_load must be set to str value")
			self._traffic_load = traffic_load
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the networks
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the networks
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
	Use this operation to get the formation networks.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				formation_network_obj=formation_network()
				response = formation_network_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of formation_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			formation_network_obj = formation_network()
			option_ = options()
			option_._filter=filter_
			return formation_network_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the formation_network resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			formation_network_obj = formation_network()
			option_ = options()
			option_._count=True
			response = formation_network_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of formation_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			formation_network_obj = formation_network()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = formation_network_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(formation_network_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.formation_network
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(formation_network_responses, response, "formation_network_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.formation_network_response_array
				i=0
				error = [formation_network() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.formation_network_response_array
			i=0
			formation_network_objs = [formation_network() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_formation_network'):
					for props in obj._formation_network:
						result = service.payload_formatter.string_to_bulk_resource(formation_network_response,self.__class__.__name__,props)
						formation_network_objs[i] = result.formation_network
						i=i+1
			return formation_network_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(formation_network,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class formation_network_response(base_response):
	def __init__(self,length=1) :
		self.formation_network= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.formation_network= [ formation_network() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class formation_network_responses(base_response):
	def __init__(self,length=1) :
		self.formation_network_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.formation_network_response_array = [ formation_network() for _ in range(length)]
