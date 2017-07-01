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
Configuration for ns_cluster_nodegroup resource.
'''

class ns_cluster_nodegroup(base_resource):
	_password= ""
	_clip= ""
	_name= ""
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
			return "ns_cluster_nodegroup"
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
			return "ns_cluster_nodegroups"
		except Exception as e :
			raise e



	'''
	get Password of the Configuration Coordinator node(Cluster IP)
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password of the Configuration Coordinator node(Cluster IP)
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
	get Cluster IPAddress where this nodegroup will be added
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IPAddress where this nodegroup will be added
	'''
	@clip.setter
	def clip(self,clip):
		try :
			if not isinstance(clip,str):
				raise TypeError("clip must be set to str value")
			self._clip = clip
		except Exception as e :
			raise e


	'''
	get Cluster Node Group Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Cluster Node Group Name
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
	Use this operation to add new node group on cluster instance.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_cluster_nodegroup_obj= ns_cluster_nodegroup()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_cluster_nodegroup_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_cluster_nodegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_cluster_nodegroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_cluster_nodegroup_responses, response, "ns_cluster_nodegroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_cluster_nodegroup_response_array
				i=0
				error = [ns_cluster_nodegroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_cluster_nodegroup_response_array
			i=0
			ns_cluster_nodegroup_objs = [ns_cluster_nodegroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_cluster_nodegroup'):
					for props in obj._ns_cluster_nodegroup:
						result = service.payload_formatter.string_to_bulk_resource(ns_cluster_nodegroup_response,self.__class__.__name__,props)
						ns_cluster_nodegroup_objs[i] = result.ns_cluster_nodegroup
						i=i+1
			return ns_cluster_nodegroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_cluster_nodegroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_cluster_nodegroup_response(base_response):
	def __init__(self,length=1) :
		self.ns_cluster_nodegroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_cluster_nodegroup= [ ns_cluster_nodegroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_cluster_nodegroup_responses(base_response):
	def __init__(self,length=1) :
		self.ns_cluster_nodegroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_cluster_nodegroup_response_array = [ ns_cluster_nodegroup() for _ in range(length)]
