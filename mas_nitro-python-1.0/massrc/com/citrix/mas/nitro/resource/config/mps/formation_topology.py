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
Configuration for Formation Topology resource
'''

class formation_topology(base_resource):
	_template_name= ""
	_entity_ip= ""
	_connections= ""
	_entity_state= ""
	_version= ""
	_entity_name= ""
	_formation_instance_id= ""
	_entity_id= ""
	_entity_type= ""
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
			return "formation_topology"
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
			return "formation_topologys"
		except Exception as e :
			raise e



	'''
	get Formation Template Name
	'''
	@property
	def template_name(self) :
		try:
			return self._template_name
		except Exception as e :
			raise e
	'''
	set Formation Template Name
	'''
	@template_name.setter
	def template_name(self,template_name):
		try :
			if not isinstance(template_name,str):
				raise TypeError("template_name must be set to str value")
			self._template_name = template_name
		except Exception as e :
			raise e


	'''
	get Entity IP Address
	'''
	@property
	def entity_ip(self) :
		try:
			return self._entity_ip
		except Exception as e :
			raise e
	'''
	set Entity IP Address
	'''
	@entity_ip.setter
	def entity_ip(self,entity_ip):
		try :
			if not isinstance(entity_ip,str):
				raise TypeError("entity_ip must be set to str value")
			self._entity_ip = entity_ip
		except Exception as e :
			raise e


	'''
	get Connections
	'''
	@property
	def connections(self) :
		try:
			return self._connections
		except Exception as e :
			raise e
	'''
	set Connections
	'''
	@connections.setter
	def connections(self,connections):
		try :
			if not isinstance(connections,str):
				raise TypeError("connections must be set to str value")
			self._connections = connections
		except Exception as e :
			raise e


	'''
	get Entity state
	'''
	@property
	def entity_state(self) :
		try:
			return self._entity_state
		except Exception as e :
			raise e
	'''
	set Entity state
	'''
	@entity_state.setter
	def entity_state(self,entity_state):
		try :
			if not isinstance(entity_state,str):
				raise TypeError("entity_state must be set to str value")
			self._entity_state = entity_state
		except Exception as e :
			raise e


	'''
	get Template version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Template version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Entity Name
	'''
	@property
	def entity_name(self) :
		try:
			return self._entity_name
		except Exception as e :
			raise e
	'''
	set Entity Name
	'''
	@entity_name.setter
	def entity_name(self,entity_name):
		try :
			if not isinstance(entity_name,str):
				raise TypeError("entity_name must be set to str value")
			self._entity_name = entity_name
		except Exception as e :
			raise e


	'''
	get Formation Instance ID
	'''
	@property
	def formation_instance_id(self) :
		try:
			return self._formation_instance_id
		except Exception as e :
			raise e
	'''
	set Formation Instance ID
	'''
	@formation_instance_id.setter
	def formation_instance_id(self,formation_instance_id):
		try :
			if not isinstance(formation_instance_id,str):
				raise TypeError("formation_instance_id must be set to str value")
			self._formation_instance_id = formation_instance_id
		except Exception as e :
			raise e


	'''
	get Entity ID
	'''
	@property
	def entity_id(self) :
		try:
			return self._entity_id
		except Exception as e :
			raise e
	'''
	set Entity ID
	'''
	@entity_id.setter
	def entity_id(self,entity_id):
		try :
			if not isinstance(entity_id,str):
				raise TypeError("entity_id must be set to str value")
			self._entity_id = entity_id
		except Exception as e :
			raise e


	'''
	get Entity Type
	'''
	@property
	def entity_type(self) :
		try:
			return self._entity_type
		except Exception as e :
			raise e
	'''
	set Entity Type
	'''
	@entity_type.setter
	def entity_type(self,entity_type):
		try :
			if not isinstance(entity_type,str):
				raise TypeError("entity_type must be set to str value")
			self._entity_type = entity_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the Formation Instances
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Formation Instances
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
	Use this operation to get the formation topology.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				formation_topology_obj=formation_topology()
				response = formation_topology_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of formation_topology resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			formation_topology_obj = formation_topology()
			option_ = options()
			option_._filter=filter_
			return formation_topology_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the formation_topology resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			formation_topology_obj = formation_topology()
			option_ = options()
			option_._count=True
			response = formation_topology_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of formation_topology resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			formation_topology_obj = formation_topology()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = formation_topology_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(formation_topology_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.formation_topology
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(formation_topology_responses, response, "formation_topology_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.formation_topology_response_array
				i=0
				error = [formation_topology() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.formation_topology_response_array
			i=0
			formation_topology_objs = [formation_topology() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_formation_topology'):
					for props in obj._formation_topology:
						result = service.payload_formatter.string_to_bulk_resource(formation_topology_response,self.__class__.__name__,props)
						formation_topology_objs[i] = result.formation_topology
						i=i+1
			return formation_topology_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(formation_topology,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class formation_topology_response(base_response):
	def __init__(self,length=1) :
		self.formation_topology= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.formation_topology= [ formation_topology() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class formation_topology_responses(base_response):
	def __init__(self,length=1) :
		self.formation_topology_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.formation_topology_response_array = [ formation_topology() for _ in range(length)]
