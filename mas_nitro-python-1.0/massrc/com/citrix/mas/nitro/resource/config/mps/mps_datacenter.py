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
Configuration for MPS Datacentre resource
'''

class mps_datacenter(base_resource):
	_tenant_name= ""
	_longitude= ""
	_is_default= ""
	_location= ""
	_name= ""
	_tenant_id= ""
	_device_type= ""
	_latitude= ""
	_cloud_provider= ""
	_ip_block= ""
	_type= ""
	_id= ""
	_device_ip= ""
	_total_number_of_devices= ""
	_clients=[]
	_server_node_list_array=[]
	_servers=[]
	_total_number_of_agents= ""
	_device_list_array=[]
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
			return "mps_datacenter"
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
			return "mps_datacenters"
		except Exception as e :
			raise e



	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get longitude of the city
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude of the city
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get IS Default Datacentre
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	set IS Default Datacentre
	'''
	@is_default.setter
	def is_default(self,is_default):
		try :
			if not isinstance(is_default,bool):
				raise TypeError("is_default must be set to bool value")
			self._is_default = is_default
		except Exception as e :
			raise e


	'''
	get Cloud Provide
	'''
	@property
	def location(self) :
		try:
			return self._location
		except Exception as e :
			raise e
	'''
	set Cloud Provide
	'''
	@location.setter
	def location(self,location):
		try :
			if not isinstance(location,str):
				raise TypeError("location must be set to str value")
			self._location = location
		except Exception as e :
			raise e


	'''
	get Datacentre Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Datacentre Name
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
	get Tenant ID
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant ID
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get device_type
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set device_type
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,int):
				raise TypeError("device_type must be set to int value")
			self._device_type = device_type
		except Exception as e :
			raise e


	'''
	get latitude of the city
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude of the city
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e


	'''
	get Cloud Provide
	'''
	@property
	def cloud_provider(self) :
		try:
			return self._cloud_provider
		except Exception as e :
			raise e
	'''
	set Cloud Provide
	'''
	@cloud_provider.setter
	def cloud_provider(self,cloud_provider):
		try :
			if not isinstance(cloud_provider,str):
				raise TypeError("cloud_provider must be set to str value")
			self._cloud_provider = cloud_provider
		except Exception as e :
			raise e


	'''
	get ID for IP Block
	'''
	@property
	def ip_block(self) :
		try:
			return self._ip_block
		except Exception as e :
			raise e
	'''
	set ID for IP Block
	'''
	@ip_block.setter
	def ip_block(self,ip_block):
		try :
			if not isinstance(ip_block,str):
				raise TypeError("ip_block must be set to str value")
			self._ip_block = ip_block
		except Exception as e :
			raise e


	'''
	get Datacenter type: Site/Datacenter
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Datacenter type: Site/Datacenter
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,int):
				raise TypeError("type must be set to int value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system users
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system users
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
	get device_ip
	'''
	@property
	def device_ip(self) :
		try:
			return self._device_ip
		except Exception as e :
			raise e
	'''
	set device_ip
	'''
	@device_ip.setter
	def device_ip(self,device_ip):
		try :
			if not isinstance(device_ip,str):
				raise TypeError("device_ip must be set to str value")
			self._device_ip = device_ip
		except Exception as e :
			raise e

	'''
	Total Critical events city wise.
	'''
	@property
	def total_critical_events(self):
		try:
			return self._total_critical_events
		except Exception as e :
			raise e

	'''
	Array for Agent nodes
	'''
	@property
	def agent_node_list_array(self) :
		try:
			return self._agent_node_list_array
		except Exception as e :
			raise e
	'''
	Array for Agent nodes
	'''
	@agent_node_list_array.setter
	def agent_node_list_array(self,agent_node_list_array) :
		try :
			if not isinstance(agent_node_list_array,list):
				raise TypeError("agent_node_list_array must be set to array of str value")
			for item in agent_node_list_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._agent_node_list_array = agent_node_list_array
		except Exception as e :
			raise e

	'''
	Total major events.
	'''
	@property
	def total_major_events(self):
		try:
			return self._total_major_events
		except Exception as e :
			raise e

	'''
	Total events city wise.
	'''
	@property
	def total_events(self):
		try:
			return self._total_events
		except Exception as e :
			raise e

	'''
	Array for Devices
	'''
	@property
	def ip_block_array(self) :
		try:
			return self._ip_block_array
		except Exception as e :
			raise e
	'''
	Array for Devices
	'''
	@ip_block_array.setter
	def ip_block_array(self,ip_block_array) :
		try :
			if not isinstance(ip_block_array,list):
				raise TypeError("ip_block_array must be set to array of str value")
			for item in ip_block_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ip_block_array = ip_block_array
		except Exception as e :
			raise e

	'''
	City Name
	'''
	@property
	def cityname(self):
		try:
			return self._cityname
		except Exception as e :
			raise e
	'''
	City Name
	'''
	@cityname.setter
	def cityname(self,cityname):
		try :
			if not isinstance(cityname,str):
				raise TypeError("cityname must be set to str value")
			self._cityname = cityname
		except Exception as e :
			raise e

	'''
	Count Map
	'''
	@property
	def count_map(self) :
		try:
			return self._count_map
		except Exception as e :
			raise e
	'''
	Count Map
	'''
	@count_map.setter
	def count_map(self,count_map) :
		try :
			if not isinstance(count_map,list):
				raise TypeError("count_map must be set to array of entity_map value")
			for item in count_map :
				if not isinstance(item,entity_map):
					raise TypeError("item must be set to entity_map value")
			self._count_map = count_map
		except Exception as e :
			raise e

	'''
	Total number of devices deployed city wise..
	'''
	@property
	def total_number_of_devices(self):
		try:
			return self._total_number_of_devices
		except Exception as e :
			raise e

	'''
	clients
	'''
	@property
	def clients(self) :
		try:
			return self._clients
		except Exception as e :
			raise e
	'''
	clients
	'''
	@clients.setter
	def clients(self,clients) :
		try :
			if not isinstance(clients,list):
				raise TypeError("clients must be set to array of client_connection value")
			for item in clients :
				if not isinstance(item,client_connection):
					raise TypeError("item must be set to client_connection value")
			self._clients = clients
		except Exception as e :
			raise e

	'''
	Array for Server nodes
	'''
	@property
	def server_node_list_array(self) :
		try:
			return self._server_node_list_array
		except Exception as e :
			raise e
	'''
	Array for Server nodes
	'''
	@server_node_list_array.setter
	def server_node_list_array(self,server_node_list_array) :
		try :
			if not isinstance(server_node_list_array,list):
				raise TypeError("server_node_list_array must be set to array of str value")
			for item in server_node_list_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._server_node_list_array = server_node_list_array
		except Exception as e :
			raise e

	'''
	Count Map
	'''
	@property
	def servers(self) :
		try:
			return self._servers
		except Exception as e :
			raise e
	'''
	Count Map
	'''
	@servers.setter
	def servers(self,servers) :
		try :
			if not isinstance(servers,list):
				raise TypeError("servers must be set to array of server_connection value")
			for item in servers :
				if not isinstance(item,server_connection):
					raise TypeError("item must be set to server_connection value")
			self._servers = servers
		except Exception as e :
			raise e

	'''
	Total number of agents deployed city wise.
	'''
	@property
	def total_number_of_agents(self):
		try:
			return self._total_number_of_agents
		except Exception as e :
			raise e

	'''
	Array for Devices
	'''
	@property
	def device_list_array(self) :
		try:
			return self._device_list_array
		except Exception as e :
			raise e
	'''
	Array for Devices
	'''
	@device_list_array.setter
	def device_list_array(self,device_list_array) :
		try :
			if not isinstance(device_list_array,list):
				raise TypeError("device_list_array must be set to array of str value")
			for item in device_list_array :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._device_list_array = device_list_array
		except Exception as e :
			raise e

	'''
	Use this operation to add Agent information.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				mps_datacenter_obj= mps_datacenter()
				return cls.perform_operation_bulk_request(service,"add", resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete Agent information.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					mps_datacenter_obj=mps_datacenter()
					return cls.delete_bulk_request(client,resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Agent information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_datacenter_obj=mps_datacenter()
				response = mps_datacenter_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify Agent information.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				mps_datacenter_obj=mps_datacenter()
				return cls.update_bulk_request(client,resource,mps_datacenter_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_datacenter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._filter=filter_
			return mps_datacenter_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_datacenter resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._count=True
			response = mps_datacenter_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_datacenter resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_datacenter_obj = mps_datacenter()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_datacenter_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_datacenter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_datacenter
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_datacenter_responses, response, "mps_datacenter_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_datacenter_response_array
				i=0
				error = [mps_datacenter() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_datacenter_response_array
			i=0
			mps_datacenter_objs = [mps_datacenter() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_datacenter'):
					for props in obj._mps_datacenter:
						result = service.payload_formatter.string_to_bulk_resource(mps_datacenter_response,self.__class__.__name__,props)
						mps_datacenter_objs[i] = result.mps_datacenter
						i=i+1
			return mps_datacenter_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_datacenter,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_datacenter_response(base_response):
	def __init__(self,length=1) :
		self.mps_datacenter= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_datacenter= [ mps_datacenter() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_datacenter_responses(base_response):
	def __init__(self,length=1) :
		self.mps_datacenter_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_datacenter_response_array = [ mps_datacenter() for _ in range(length)]
