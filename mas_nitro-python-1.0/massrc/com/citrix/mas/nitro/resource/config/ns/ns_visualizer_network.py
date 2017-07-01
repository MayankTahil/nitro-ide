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
Configuration for visualizer network resource
'''

class ns_visualizer_network(base_resource):
	_bridgegroup=[]
	_interfaces=[]
	_nsip6=[]
	_vlan=[]
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
			return "ns_visualizer_network"
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
			return "ns_visualizer_networks"
		except Exception as e :
			raise e


	'''
	Bridge group
	'''
	@property
	def bridgegroup(self) :
		try:
			return self._bridgegroup
		except Exception as e :
			raise e
	'''
	Bridge group
	'''
	@bridgegroup.setter
	def bridgegroup(self,bridgegroup) :
		try :
			if not isinstance(bridgegroup,list):
				raise TypeError("bridgegroup must be set to array of str value")
			for item in bridgegroup :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._bridgegroup = bridgegroup
		except Exception as e :
			raise e

	'''
	Interface
	'''
	@property
	def interfaces(self) :
		try:
			return self._interfaces
		except Exception as e :
			raise e
	'''
	Interface
	'''
	@interfaces.setter
	def interfaces(self,interfaces) :
		try :
			if not isinstance(interfaces,list):
				raise TypeError("interfaces must be set to array of str value")
			for item in interfaces :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._interfaces = interfaces
		except Exception as e :
			raise e

	'''
	NetScaler IPV6
	'''
	@property
	def nsip6(self) :
		try:
			return self._nsip6
		except Exception as e :
			raise e
	'''
	NetScaler IPV6
	'''
	@nsip6.setter
	def nsip6(self,nsip6) :
		try :
			if not isinstance(nsip6,list):
				raise TypeError("nsip6 must be set to array of str value")
			for item in nsip6 :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._nsip6 = nsip6
		except Exception as e :
			raise e

	'''
	VLAN
	'''
	@property
	def vlan(self) :
		try:
			return self._vlan
		except Exception as e :
			raise e
	'''
	VLAN
	'''
	@vlan.setter
	def vlan(self,vlan) :
		try :
			if not isinstance(vlan,list):
				raise TypeError("vlan must be set to array of str value")
			for item in vlan :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vlan = vlan
		except Exception as e :
			raise e

	'''
	Use this operation to get Network Bridge group,NetScaler IPV6 and VLANS..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_visualizer_network_obj=ns_visualizer_network()
				response = ns_visualizer_network_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_visualizer_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_visualizer_network_obj = ns_visualizer_network()
			option_ = options()
			option_._filter=filter_
			return ns_visualizer_network_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_visualizer_network resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_visualizer_network_obj = ns_visualizer_network()
			option_ = options()
			option_._count=True
			response = ns_visualizer_network_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_visualizer_network resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_visualizer_network_obj = ns_visualizer_network()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_visualizer_network_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_visualizer_network_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_visualizer_network
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_visualizer_network_responses, response, "ns_visualizer_network_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_visualizer_network_response_array
				i=0
				error = [ns_visualizer_network() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_visualizer_network_response_array
			i=0
			ns_visualizer_network_objs = [ns_visualizer_network() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_visualizer_network'):
					for props in obj._ns_visualizer_network:
						result = service.payload_formatter.string_to_bulk_resource(ns_visualizer_network_response,self.__class__.__name__,props)
						ns_visualizer_network_objs[i] = result.ns_visualizer_network
						i=i+1
			return ns_visualizer_network_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_visualizer_network,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_visualizer_network_response(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_network= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_visualizer_network= [ ns_visualizer_network() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_visualizer_network_responses(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_network_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_visualizer_network_response_array = [ ns_visualizer_network() for _ in range(length)]
