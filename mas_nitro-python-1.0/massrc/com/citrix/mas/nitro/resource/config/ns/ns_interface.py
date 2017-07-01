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
Configuration for NetScaler Interface resource
'''

class ns_interface(base_resource):
	_is_cluster_node= ""
	_vif_list=[]
	_pif_list=[]
	_nodeid= ""
	_ip_address= ""
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
			return "ns_interface"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._ip_address
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
			return "ns_interfaces"
		except Exception as e :
			raise e



	'''
	get Is the node is part of cluster or not
	'''
	@property
	def is_cluster_node(self) :
		try:
			return self._is_cluster_node
		except Exception as e :
			raise e
	'''
	set Is the node is part of cluster or not
	'''
	@is_cluster_node.setter
	def is_cluster_node(self,is_cluster_node):
		try :
			if not isinstance(is_cluster_node,bool):
				raise TypeError("is_cluster_node must be set to bool value")
			self._is_cluster_node = is_cluster_node
		except Exception as e :
			raise e


	'''
	get Virtual Interface List
	'''
	@property
	def vif_list(self) :
		try:
			return self._vif_list
		except Exception as e :
			raise e
	'''
	set Virtual Interface List
	'''
	@vif_list.setter
	def vif_list(self,vif_list) :
		try :
			if not isinstance(vif_list,list):
				raise TypeError("vif_list must be set to array of str value")
			for item in vif_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vif_list = vif_list
		except Exception as e :
			raise e


	'''
	get Physical Interface List
	'''
	@property
	def pif_list(self) :
		try:
			return self._pif_list
		except Exception as e :
			raise e
	'''
	set Physical Interface List
	'''
	@pif_list.setter
	def pif_list(self,pif_list) :
		try :
			if not isinstance(pif_list,list):
				raise TypeError("pif_list must be set to array of str value")
			for item in pif_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._pif_list = pif_list
		except Exception as e :
			raise e


	'''
	get Node Id applicable on cluster
	'''
	@property
	def nodeid(self) :
		try:
			return self._nodeid
		except Exception as e :
			raise e
	'''
	set Node Id applicable on cluster
	'''
	@nodeid.setter
	def nodeid(self,nodeid):
		try :
			if not isinstance(nodeid,int):
				raise TypeError("nodeid must be set to int value")
			self._nodeid = nodeid
		except Exception as e :
			raise e


	'''
	get Netscaler IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Netscaler IP Address
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
	Use this operation to get VM Physical and Virtual Interface list.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_interface_obj=ns_interface()
				response = ns_interface_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_interface_obj = ns_interface()
			option_ = options()
			option_._filter=filter_
			return ns_interface_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_interface resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_interface_obj = ns_interface()
			option_ = options()
			option_._count=True
			response = ns_interface_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_interface_obj = ns_interface()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_interface_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_interface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_interface
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_interface_responses, response, "ns_interface_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_interface_response_array
				i=0
				error = [ns_interface() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_interface_response_array
			i=0
			ns_interface_objs = [ns_interface() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_interface'):
					for props in obj._ns_interface:
						result = service.payload_formatter.string_to_bulk_resource(ns_interface_response,self.__class__.__name__,props)
						ns_interface_objs[i] = result.ns_interface
						i=i+1
			return ns_interface_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_interface,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_interface_response(base_response):
	def __init__(self,length=1) :
		self.ns_interface= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_interface= [ ns_interface() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_interface_responses(base_response):
	def __init__(self,length=1) :
		self.ns_interface_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_interface_response_array = [ ns_interface() for _ in range(length)]
