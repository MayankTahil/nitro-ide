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
Configuration for Additional Server node information resource
'''

class server_nodes(base_resource):
	_priority= ""
	_password= ""
	_deployment_status= ""
	_is_pooled_license= ""
	_app_id= ""
	_name= ""
	_state= ""
	_username= ""
	_is_star_node= ""
	_build_name= ""
	_public_key= ""
	_device_count= ""
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
			return "server_nodes"
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
			return "server_nodess"
		except Exception as e :
			raise e



	'''
	get priority of the app node
	'''
	@property
	def priority(self) :
		try:
			return self._priority
		except Exception as e :
			raise e
	'''
	set priority of the app node
	'''
	@priority.setter
	def priority(self,priority):
		try :
			if not isinstance(priority,int):
				raise TypeError("priority must be set to int value")
			self._priority = priority
		except Exception as e :
			raise e


	'''
	get Password
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Deployment status of this node.
	'''
	@property
	def deployment_status(self) :
		try:
			return self._deployment_status
		except Exception as e :
			raise e
	'''
	set Deployment status of this node.
	'''
	@deployment_status.setter
	def deployment_status(self,deployment_status):
		try :
			if not isinstance(deployment_status,bool):
				raise TypeError("deployment_status must be set to bool value")
			self._deployment_status = deployment_status
		except Exception as e :
			raise e


	'''
	get is_pooled_license present on node
	'''
	@property
	def is_pooled_license(self) :
		try:
			return self._is_pooled_license
		except Exception as e :
			raise e
	'''
	set is_pooled_license present on node
	'''
	@is_pooled_license.setter
	def is_pooled_license(self,is_pooled_license):
		try :
			if not isinstance(is_pooled_license,bool):
				raise TypeError("is_pooled_license must be set to bool value")
			self._is_pooled_license = is_pooled_license
		except Exception as e :
			raise e


	'''
	get Node ID of the server node
	'''
	@property
	def app_id(self) :
		try:
			return self._app_id
		except Exception as e :
			raise e
	'''
	set Node ID of the server node
	'''
	@app_id.setter
	def app_id(self,app_id):
		try :
			if not isinstance(app_id,str):
				raise TypeError("app_id must be set to str value")
			self._app_id = app_id
		except Exception as e :
			raise e


	'''
	get Server node IP Address
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Server node IP Address
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
	get State of the App node
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of the App node
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get username configured on Server node.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set username configured on Server node.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e

	'''
	This node is star node or not
	'''
	@property
	def is_star_node(self):
		try:
			return self._is_star_node
		except Exception as e :
			raise e
	'''
	This node is star node or not
	'''
	@is_star_node.setter
	def is_star_node(self,is_star_node):
		try :
			if not isinstance(is_star_node,bool):
				raise TypeError("is_star_node must be set to bool value")
			self._is_star_node = is_star_node
		except Exception as e :
			raise e

	'''
	Build name of the server node
	'''
	@property
	def build_name(self):
		try:
			return self._build_name
		except Exception as e :
			raise e
	'''
	Build name of the server node
	'''
	@build_name.setter
	def build_name(self,build_name):
		try :
			if not isinstance(build_name,str):
				raise TypeError("build_name must be set to str value")
			self._build_name = build_name
		except Exception as e :
			raise e

	'''
	Useful for sending the public key while registration
	'''
	@property
	def public_key(self):
		try:
			return self._public_key
		except Exception as e :
			raise e
	'''
	Useful for sending the public key while registration
	'''
	@public_key.setter
	def public_key(self,public_key):
		try :
			if not isinstance(public_key,str):
				raise TypeError("public_key must be set to str value")
			self._public_key = public_key
		except Exception as e :
			raise e

	'''
	No of managed devices owned by the node
	'''
	@property
	def device_count(self):
		try:
			return self._device_count
		except Exception as e :
			raise e
	'''
	No of managed devices owned by the node
	'''
	@device_count.setter
	def device_count(self,device_count):
		try :
			if not isinstance(device_count,int):
				raise TypeError("device_count must be set to int value")
			self._device_count = device_count
		except Exception as e :
			raise e

	'''
	Use this operation to add server nodes.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				server_nodes_obj= server_nodes()
				return cls.perform_operation_bulk_request(service,"add", resource,server_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete server nodes.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					server_nodes_obj=server_nodes()
					return cls.delete_bulk_request(client,resource,server_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get server nodes.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				server_nodes_obj=server_nodes()
				response = server_nodes_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify server nodes.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				server_nodes_obj=server_nodes()
				return cls.update_bulk_request(client,resource,server_nodes_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of server_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			server_nodes_obj = server_nodes()
			option_ = options()
			option_._filter=filter_
			return server_nodes_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the server_nodes resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			server_nodes_obj = server_nodes()
			option_ = options()
			option_._count=True
			response = server_nodes_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of server_nodes resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			server_nodes_obj = server_nodes()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = server_nodes_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(server_nodes_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server_nodes
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_nodes_responses, response, "server_nodes_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.server_nodes_response_array
				i=0
				error = [server_nodes() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.server_nodes_response_array
			i=0
			server_nodes_objs = [server_nodes() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_server_nodes'):
					for props in obj._server_nodes:
						result = service.payload_formatter.string_to_bulk_resource(server_nodes_response,self.__class__.__name__,props)
						server_nodes_objs[i] = result.server_nodes
						i=i+1
			return server_nodes_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(server_nodes,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class server_nodes_response(base_response):
	def __init__(self,length=1) :
		self.server_nodes= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.server_nodes= [ server_nodes() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class server_nodes_responses(base_response):
	def __init__(self,length=1) :
		self.server_nodes_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.server_nodes_response_array = [ server_nodes() for _ in range(length)]
