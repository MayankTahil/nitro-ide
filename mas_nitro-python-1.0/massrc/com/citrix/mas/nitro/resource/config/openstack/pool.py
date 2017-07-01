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
Configuration for OpenStack Pools resource
'''

class pool(base_resource):
	_protocol= ""
	_subnet_id= ""
	_admin_state_up= ""
	_status= ""
	_vip_id= ""
	_subnet_gateway_ip= ""
	_network_type= ""
	_tenant_id= ""
	_subnet_cidr= ""
	_segmentation_id= ""
	_id= ""
	_loadbalancer_id= ""
	_lb_method= ""
	_name= ""
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
			return "/oca/v1/pools"
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
			return "pool"
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
			return "pools"
		except Exception as e :
			raise e



	'''
	get Protocol of pool. The possible values of protocol are HTTP, HTTPS or TCP
	'''
	@property
	def protocol(self) :
		try:
			return self._protocol
		except Exception as e :
			raise e
	'''
	set Protocol of pool. The possible values of protocol are HTTP, HTTPS or TCP
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
	get Subnet Id used in pool.
	'''
	@property
	def subnet_id(self) :
		try:
			return self._subnet_id
		except Exception as e :
			raise e
	'''
	set Subnet Id used in pool.
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
	get Admin State Up status of pool in OpenStack.
	'''
	@property
	def admin_state_up(self) :
		try:
			return self._admin_state_up
		except Exception as e :
			raise e
	'''
	set Admin State Up status of pool in OpenStack.
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
	get Status of pool.
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of pool.
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
	get Id of VIP in OpenStack
	'''
	@property
	def vip_id(self) :
		try:
			return self._vip_id
		except Exception as e :
			raise e
	'''
	set Id of VIP in OpenStack
	'''
	@vip_id.setter
	def vip_id(self,vip_id):
		try :
			if not isinstance(vip_id,str):
				raise TypeError("vip_id must be set to str value")
			self._vip_id = vip_id
		except Exception as e :
			raise e


	'''
	get Subnet Gateway Ip of pool.
	'''
	@property
	def subnet_gateway_ip(self) :
		try:
			return self._subnet_gateway_ip
		except Exception as e :
			raise e
	'''
	set Subnet Gateway Ip of pool.
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
	get Type of network where pool is present.
	'''
	@property
	def network_type(self) :
		try:
			return self._network_type
		except Exception as e :
			raise e
	'''
	set Type of network where pool is present.
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
	get Id of tenant in openstack
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of tenant in openstack
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
	get Subnet Cidr of pool.
	'''
	@property
	def subnet_cidr(self) :
		try:
			return self._subnet_cidr
		except Exception as e :
			raise e
	'''
	set Subnet Cidr of pool.
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
	get Segmentation Id of pool.
	'''
	@property
	def segmentation_id(self) :
		try:
			return self._segmentation_id
		except Exception as e :
			raise e
	'''
	set Segmentation Id of pool.
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
	get Id is system generated key for openstack cloud
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for openstack cloud
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
	get Id of loadbalancer of which the pool is part of.
	'''
	@property
	def loadbalancer_id(self) :
		try:
			return self._loadbalancer_id
		except Exception as e :
			raise e
	'''
	set Id of loadbalancer of which the pool is part of.
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
	get LB Method of pool. The possible values of lb_method are 'ROUND_ROBIN', 'LEAST_CONNECTIONS', 'SOURCE_IP'
	'''
	@property
	def lb_method(self) :
		try:
			return self._lb_method
		except Exception as e :
			raise e
	'''
	set LB Method of pool. The possible values of lb_method are 'ROUND_ROBIN', 'LEAST_CONNECTIONS', 'SOURCE_IP'
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
	get Name of openstack.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of openstack.
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
	get Description of pool.
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of pool.
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
	get Network Id of the pool.
	'''
	@property
	def network_id(self) :
		try:
			return self._network_id
		except Exception as e :
			raise e
	'''
	set Network Id of the pool.
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
	Use this operation to get Pool details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				pool_obj=pool()
				response = pool_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of pool resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			pool_obj = pool()
			option_ = options()
			option_._filter=filter_
			return pool_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the pool resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			pool_obj = pool()
			option_ = options()
			option_._count=True
			response = pool_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of pool resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			pool_obj = pool()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = pool_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(pool_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pool
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(pool_responses, response, "pool_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.pool_response_array
				i=0
				error = [pool() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.pool_response_array
			i=0
			pool_objs = [pool() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_pool'):
					for props in obj._pool:
						result = service.payload_formatter.string_to_bulk_resource(pool_response,self.__class__.__name__,props)
						pool_objs[i] = result.pool
						i=i+1
			return pool_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(pool,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class pool_response(base_response):
	def __init__(self,length=1) :
		self.pool= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.pool= [ pool() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class pool_responses(base_response):
	def __init__(self,length=1) :
		self.pool_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.pool_response_array = [ pool() for _ in range(length)]
