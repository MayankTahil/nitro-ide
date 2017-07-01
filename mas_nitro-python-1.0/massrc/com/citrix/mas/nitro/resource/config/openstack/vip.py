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
from massrc.com.citrix.mas.nitro.resource.config.openstack.vipsessionpersistence import vipsessionpersistence
from massrc.com.citrix.mas.nitro.resource.config.openstack.vipdiameter import vipdiameter


'''
Configuration for vip configuration resource
'''

class vip(base_resource):
	_protocol= ""
	_subnet_id= ""
	_admin_state_up= ""
	_status= ""
	_port_id= ""
	_subnet_gateway_ip= ""
	_network_type= ""
	_tenant_id= ""
	_subnet_cidr= ""
	_pool_id= ""
	_segmentation_id= ""
	_connection_limit= ""
	_address= ""
	_id= ""
	_loadbalancer_id= ""
	_session_persistence= ""
	_name= ""
	_protocol_port= ""
	_diameter= ""
	_description= ""
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
			return "/v2.0/lb/vips"
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
			return "vip"
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
			return "vips"
		except Exception as e :
			raise e



	'''
	get Protocol used by vip
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set Protocol used by vip
	'''
	@protocol.setter
	def protocol(self,protocol):
		try :
			if not isinstance(protocol,str):
				raise TypeError("protocol must be set to str value")
			self._protocol = protocol
		except Exception as e :
			raise e


	'''
	get Subnet Id of vip
	'''
	@property
	def subnet_id(self) :
		try:
			return self._subnet_id
		except Exception as e :
			raise e
	'''
	set Subnet Id of vip
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
	get Admin is up or down
	'''
	@property
	def admin_state_up(self) :
		try:
			return self._admin_state_up
		except Exception as e :
			raise e
	'''
	set Admin is up or down
	'''
	@admin_state_up.setter
	def admin_state_up(self,admin_state_up):
		try :
			if not isinstance(admin_state_up,str):
				raise TypeError("admin_state_up must be set to str value")
			self._admin_state_up = admin_state_up
		except Exception as e :
			raise e


	'''
	get status of vip
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set status of vip
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Port Id of requests
	'''
	@property
	def port_id(self) :
		try:
			return self._port_id
		except Exception as e :
			raise e
	'''
	set Port Id of requests
	'''
	@port_id.setter
	def port_id(self,port_id):
		try :
			if not isinstance(port_id,str):
				raise TypeError("port_id must be set to str value")
			self._port_id = port_id
		except Exception as e :
			raise e


	'''
	get Ip of subnet gateway for vip
	'''
	@property
	def subnet_gateway_ip(self) :
		try:
			return self._subnet_gateway_ip
		except Exception as e :
			raise e
	'''
	set Ip of subnet gateway for vip
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
	get Type of network 
	'''
	@property
	def network_type(self) :
		try:
			return self._network_type
		except Exception as e :
			raise e
	'''
	set Type of network 
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
	get Id of admin tenant.
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of admin tenant.
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
	get subnet_cidr for vip
	'''
	@property
	def subnet_cidr(self) :
		try:
			return self._subnet_cidr
		except Exception as e :
			raise e
	'''
	set subnet_cidr for vip
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
	get Vip belongs to this pool id
	'''
	@property
	def pool_id(self) :
		try:
			return self._pool_id
		except Exception as e :
			raise e
	'''
	set Vip belongs to this pool id
	'''
	@pool_id.setter
	def pool_id(self,pool_id):
		try :
			if not isinstance(pool_id,str):
				raise TypeError("pool_id must be set to str value")
			self._pool_id = pool_id
		except Exception as e :
			raise e


	'''
	get Segmentation_id of vip
	'''
	@property
	def segmentation_id(self) :
		try:
			return self._segmentation_id
		except Exception as e :
			raise e
	'''
	set Segmentation_id of vip
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
	get Maximum number of connections allowed for the vip
	'''
	@property
	def connection_limit(self) :
		try:
			return self._connection_limit
		except Exception as e :
			raise e
	'''
	set Maximum number of connections allowed for the vip
	'''
	@connection_limit.setter
	def connection_limit(self,connection_limit):
		try :
			if not isinstance(connection_limit,str):
				raise TypeError("connection_limit must be set to str value")
			self._connection_limit = connection_limit
		except Exception as e :
			raise e


	'''
	get Public Ip address of vip from subnet id
	'''
	@property
	def address(self) :
		try:
			return self._address
		except Exception as e :
			raise e
	'''
	set Public Ip address of vip from subnet id
	'''
	@address.setter
	def address(self,address):
		try :
			if not isinstance(address,str):
				raise TypeError("address must be set to str value")
			self._address = address
		except Exception as e :
			raise e


	'''
	get Id is system generated key for vip
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for vip
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
	get Id of loadbalancer
	'''
	@property
	def loadbalancer_id(self) :
		try:
			return self._loadbalancer_id
		except Exception as e :
			raise e
	'''
	set Id of loadbalancer
	'''
	@loadbalancer_id.setter
	def loadbalancer_id(self,loadbalancer_id):
		try :
			if not isinstance(loadbalancer_id,str):
				raise TypeError("loadbalancer_id must be set to str value")
			self._loadbalancer_id = loadbalancer_id
		except Exception as e :
			raise e


	'''
	get Sesssion persistence state of vip
	'''
	@property
	def session_persistence(self) :
		try:
			return self._session_persistence
		except Exception as e :
			raise e
	'''
	set Sesssion persistence state of vip
	'''
	@session_persistence.setter
	def session_persistence(self,session_persistence):
		try :
			if not isinstance(session_persistence,vipsessionpersistence):
				raise TypeError("session_persistence must be set to vipsessionpersistence value")
			self._session_persistence = session_persistence
		except Exception as e :
			raise e


	'''
	get Name of vip
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of vip
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
	get Port number of protocol
	'''
	@property
	def protocol_port(self) :
		try:
			return self._protocol_port
		except Exception as e :
			raise e
	'''
	set Port number of protocol
	'''
	@protocol_port.setter
	def protocol_port(self,protocol_port):
		try :
			if not isinstance(protocol_port,str):
				raise TypeError("protocol_port must be set to str value")
			self._protocol_port = protocol_port
		except Exception as e :
			raise e


	'''
	get Value of diameter protocol
	'''
	@property
	def diameter(self) :
		try:
			return self._diameter
		except Exception as e :
			raise e
	'''
	set Value of diameter protocol
	'''
	@diameter.setter
	def diameter(self,diameter):
		try :
			if not isinstance(diameter,vipdiameter):
				raise TypeError("diameter must be set to vipdiameter value")
			self._diameter = diameter
		except Exception as e :
			raise e


	'''
	get Describes the properties of vip
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Describes the properties of vip
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
	get Network_id of vip
	'''
	@property
	def network_id(self) :
		try:
			return self._network_id
		except Exception as e :
			raise e
	'''
	set Network_id of vip
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
	Use this operation to get vip details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vip_obj=vip()
				response = vip_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vip resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vip_obj = vip()
			option_ = options()
			option_._filter=filter_
			return vip_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vip resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vip_obj = vip()
			option_ = options()
			option_._count=True
			response = vip_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vip resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vip_obj = vip()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vip_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vip_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vip
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vip_responses, response, "vip_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vip_response_array
				i=0
				error = [vip() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vip_response_array
			i=0
			vip_objs = [vip() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vip'):
					for props in obj._vip:
						result = service.payload_formatter.string_to_bulk_resource(vip_response,self.__class__.__name__,props)
						vip_objs[i] = result.vip
						i=i+1
			return vip_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vip,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vip_response(base_response):
	def __init__(self,length=1) :
		self.vip= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vip= [ vip() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vip_responses(base_response):
	def __init__(self,length=1) :
		self.vip_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vip_response_array = [ vip() for _ in range(length)]
