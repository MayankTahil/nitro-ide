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
Configuration for visualizer network bindings resource
'''

class ns_visualizer_network_bindings(base_resource):
	_vlan_nsip_binding=[]
	_vlan_interface_binding=[]
	_name= ""
	_ip_address= ""
	_vlan_bridgegroup_binding=[]
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
			return "ns_visualizer_network_bindings"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "ns_visualizer_network_bindingss"
		except Exception as e :
			raise e



	'''
	get VLAN NetScaler binding
	'''
	@property
	def vlan_nsip_binding(self) :
		try:
			return self._vlan_nsip_binding
		except Exception as e :
			raise e
	'''
	set VLAN NetScaler binding
	'''
	@vlan_nsip_binding.setter
	def vlan_nsip_binding(self,vlan_nsip_binding) :
		try :
			if not isinstance(vlan_nsip_binding,list):
				raise TypeError("vlan_nsip_binding must be set to array of str value")
			for item in vlan_nsip_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vlan_nsip_binding = vlan_nsip_binding
		except Exception as e :
			raise e


	'''
	get VLAN interface binding
	'''
	@property
	def vlan_interface_binding(self) :
		try:
			return self._vlan_interface_binding
		except Exception as e :
			raise e
	'''
	set VLAN interface binding
	'''
	@vlan_interface_binding.setter
	def vlan_interface_binding(self,vlan_interface_binding) :
		try :
			if not isinstance(vlan_interface_binding,list):
				raise TypeError("vlan_interface_binding must be set to array of str value")
			for item in vlan_interface_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vlan_interface_binding = vlan_interface_binding
		except Exception as e :
			raise e


	'''
	get Name of network binding
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of network binding
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
	get VLAN bridge group binding
	'''
	@property
	def vlan_bridgegroup_binding(self) :
		try:
			return self._vlan_bridgegroup_binding
		except Exception as e :
			raise e
	'''
	set VLAN bridge group binding
	'''
	@vlan_bridgegroup_binding.setter
	def vlan_bridgegroup_binding(self,vlan_bridgegroup_binding) :
		try :
			if not isinstance(vlan_bridgegroup_binding,list):
				raise TypeError("vlan_bridgegroup_binding must be set to array of str value")
			for item in vlan_bridgegroup_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vlan_bridgegroup_binding = vlan_bridgegroup_binding
		except Exception as e :
			raise e

	'''
	Use this operation to get Network bindings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_visualizer_network_bindings_obj=ns_visualizer_network_bindings()
				response = ns_visualizer_network_bindings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_visualizer_network_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_visualizer_network_bindings_obj = ns_visualizer_network_bindings()
			option_ = options()
			option_._filter=filter_
			return ns_visualizer_network_bindings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_visualizer_network_bindings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_visualizer_network_bindings_obj = ns_visualizer_network_bindings()
			option_ = options()
			option_._count=True
			response = ns_visualizer_network_bindings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_visualizer_network_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_visualizer_network_bindings_obj = ns_visualizer_network_bindings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_visualizer_network_bindings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_visualizer_network_bindings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_visualizer_network_bindings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_visualizer_network_bindings_responses, response, "ns_visualizer_network_bindings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_visualizer_network_bindings_response_array
				i=0
				error = [ns_visualizer_network_bindings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_visualizer_network_bindings_response_array
			i=0
			ns_visualizer_network_bindings_objs = [ns_visualizer_network_bindings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_visualizer_network_bindings'):
					for props in obj._ns_visualizer_network_bindings:
						result = service.payload_formatter.string_to_bulk_resource(ns_visualizer_network_bindings_response,self.__class__.__name__,props)
						ns_visualizer_network_bindings_objs[i] = result.ns_visualizer_network_bindings
						i=i+1
			return ns_visualizer_network_bindings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_visualizer_network_bindings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_visualizer_network_bindings_response(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_network_bindings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_visualizer_network_bindings= [ ns_visualizer_network_bindings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_visualizer_network_bindings_responses(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_network_bindings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_visualizer_network_bindings_response_array = [ ns_visualizer_network_bindings() for _ in range(length)]
