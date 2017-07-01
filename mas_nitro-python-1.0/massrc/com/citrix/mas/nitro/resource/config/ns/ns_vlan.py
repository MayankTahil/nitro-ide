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
Configuration for NS Vlan resource
'''

class ns_vlan(base_resource):
	_bound_ifaces= ""
	_ns_vlan_ip_address= ""
	_tagged_ifaces= ""
	_if_ipv6_routing= ""
	_ns_vlan_id= ""
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
			return "ns_vlan"
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
			return "ns_vlans"
		except Exception as e :
			raise e



	'''
	get Bounded Interfaces
	'''
	@property
	def bound_ifaces(self) :
		try:
			return self._bound_ifaces
		except Exception as e :
			raise e
	'''
	set Bounded Interfaces
	'''
	@bound_ifaces.setter
	def bound_ifaces(self,bound_ifaces):
		try :
			if not isinstance(bound_ifaces,str):
				raise TypeError("bound_ifaces must be set to str value")
			self._bound_ifaces = bound_ifaces
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_vlan_ip_address(self) :
		try:
			return self._ns_vlan_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_vlan_ip_address.setter
	def ns_vlan_ip_address(self,ns_vlan_ip_address):
		try :
			if not isinstance(ns_vlan_ip_address,str):
				raise TypeError("ns_vlan_ip_address must be set to str value")
			self._ns_vlan_ip_address = ns_vlan_ip_address
		except Exception as e :
			raise e


	'''
	get Tagged Interfaces
	'''
	@property
	def tagged_ifaces(self) :
		try:
			return self._tagged_ifaces
		except Exception as e :
			raise e
	'''
	set Tagged Interfaces
	'''
	@tagged_ifaces.setter
	def tagged_ifaces(self,tagged_ifaces):
		try :
			if not isinstance(tagged_ifaces,str):
				raise TypeError("tagged_ifaces must be set to str value")
			self._tagged_ifaces = tagged_ifaces
		except Exception as e :
			raise e


	'''
	get VLAN for Network 1/8 on VM Instance
	'''
	@property
	def if_ipv6_routing(self) :
		try:
			return self._if_ipv6_routing
		except Exception as e :
			raise e
	'''
	set VLAN for Network 1/8 on VM Instance
	'''
	@if_ipv6_routing.setter
	def if_ipv6_routing(self,if_ipv6_routing):
		try :
			if not isinstance(if_ipv6_routing,str):
				raise TypeError("if_ipv6_routing must be set to str value")
			self._if_ipv6_routing = if_ipv6_routing
		except Exception as e :
			raise e


	'''
	get VLAN Id
	'''
	@property
	def ns_vlan_id(self) :
		try:
			return self._ns_vlan_id
		except Exception as e :
			raise e
	'''
	set VLAN Id
	'''
	@ns_vlan_id.setter
	def ns_vlan_id(self,ns_vlan_id):
		try :
			if not isinstance(ns_vlan_id,int):
				raise TypeError("ns_vlan_id must be set to int value")
			self._ns_vlan_id = ns_vlan_id
		except Exception as e :
			raise e

	'''
	Use this operation to delete configured vlans.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_vlan_obj=ns_vlan()
					return cls.delete_bulk_request(client,resource,ns_vlan_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get configured vlans.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_vlan_obj=ns_vlan()
				response = ns_vlan_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_vlan resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_vlan_obj = ns_vlan()
			option_ = options()
			option_._filter=filter_
			return ns_vlan_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_vlan resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_vlan_obj = ns_vlan()
			option_ = options()
			option_._count=True
			response = ns_vlan_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_vlan resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_vlan_obj = ns_vlan()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_vlan_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_vlan_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_vlan
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_vlan_responses, response, "ns_vlan_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_vlan_response_array
				i=0
				error = [ns_vlan() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_vlan_response_array
			i=0
			ns_vlan_objs = [ns_vlan() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_vlan'):
					for props in obj._ns_vlan:
						result = service.payload_formatter.string_to_bulk_resource(ns_vlan_response,self.__class__.__name__,props)
						ns_vlan_objs[i] = result.ns_vlan
						i=i+1
			return ns_vlan_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_vlan,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_vlan_response(base_response):
	def __init__(self,length=1) :
		self.ns_vlan= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_vlan= [ ns_vlan() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_vlan_responses(base_response):
	def __init__(self,length=1) :
		self.ns_vlan_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_vlan_response_array = [ ns_vlan() for _ in range(length)]
