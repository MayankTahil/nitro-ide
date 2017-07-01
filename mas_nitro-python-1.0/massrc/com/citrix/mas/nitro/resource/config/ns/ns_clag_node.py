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
Configuration for CLAG node resource
'''

class ns_clag_node(base_resource):
	_local_node= ""
	_interface_name= ""
	_parent_name= ""
	_nodeid= ""
	_id= ""
	_parent_id= ""
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
			return "ns_clag_node"
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
			return "ns_clag_nodes"
		except Exception as e :
			raise e



	'''
	get Flag which represents either a local node or foreign node
	'''
	@property
	def local_node(self) :
		try:
			return self._local_node
		except Exception as e :
			raise e
	'''
	set Flag which represents either a local node or foreign node
	'''
	@local_node.setter
	def local_node(self,local_node):
		try :
			if not isinstance(local_node,bool):
				raise TypeError("local_node must be set to bool value")
			self._local_node = local_node
		except Exception as e :
			raise e


	'''
	get Name of the interface
	'''
	@property
	def interface_name(self) :
		try:
			return self._interface_name
		except Exception as e :
			raise e
	'''
	set Name of the interface
	'''
	@interface_name.setter
	def interface_name(self,interface_name):
		try :
			if not isinstance(interface_name,str):
				raise TypeError("interface_name must be set to str value")
			self._interface_name = interface_name
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
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	Use this operation to get criteria.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_clag_node_obj=ns_clag_node()
				response = ns_clag_node_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_clag_node resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_clag_node_obj = ns_clag_node()
			option_ = options()
			option_._filter=filter_
			return ns_clag_node_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_clag_node resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_clag_node_obj = ns_clag_node()
			option_ = options()
			option_._count=True
			response = ns_clag_node_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_clag_node resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_clag_node_obj = ns_clag_node()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_clag_node_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_clag_node_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_clag_node
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_clag_node_responses, response, "ns_clag_node_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_clag_node_response_array
				i=0
				error = [ns_clag_node() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_clag_node_response_array
			i=0
			ns_clag_node_objs = [ns_clag_node() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_clag_node'):
					for props in obj._ns_clag_node:
						result = service.payload_formatter.string_to_bulk_resource(ns_clag_node_response,self.__class__.__name__,props)
						ns_clag_node_objs[i] = result.ns_clag_node
						i=i+1
			return ns_clag_node_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_clag_node,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_clag_node_response(base_response):
	def __init__(self,length=1) :
		self.ns_clag_node= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_clag_node= [ ns_clag_node() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_clag_node_responses(base_response):
	def __init__(self,length=1) :
		self.ns_clag_node_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_clag_node_response_array = [ ns_clag_node() for _ in range(length)]
