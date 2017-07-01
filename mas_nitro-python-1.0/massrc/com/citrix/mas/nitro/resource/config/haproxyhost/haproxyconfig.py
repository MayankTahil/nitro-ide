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
Configuration for HAProxy Config resource
'''

class haproxyconfig(base_resource):
	_config= ""
	_haproxy_id= ""
	_id= ""
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
			return "haproxyconfig"
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
			return "haproxyconfigs"
		except Exception as e :
			raise e



	'''
	get Config content of HA Proxy Instance.
	'''
	@property
	def config(self) :
		try:
			return self._config
		except Exception as e :
			raise e
	'''
	set Config content of HA Proxy Instance.
	'''
	@config.setter
	def config(self,config):
		try :
			if not isinstance(config,str):
				raise TypeError("config must be set to str value")
			self._config = config
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the HAProxy Instances
	'''
	@property
	def haproxy_id(self) :
		try:
			return self._haproxy_id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the HAProxy Instances
	'''
	@haproxy_id.setter
	def haproxy_id(self,haproxy_id):
		try :
			if not isinstance(haproxy_id,str):
				raise TypeError("haproxy_id must be set to str value")
			self._haproxy_id = haproxy_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the HAProxy Instances
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the HAProxy Instances
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
	Use this operation to add a HAProxy config in DB.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				haproxyconfig_obj= haproxyconfig()
				return cls.perform_operation_bulk_request(service,"add", resource,haproxyconfig_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get HAProxy config.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				haproxyconfig_obj=haproxyconfig()
				response = haproxyconfig_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of haproxyconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			haproxyconfig_obj = haproxyconfig()
			option_ = options()
			option_._filter=filter_
			return haproxyconfig_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the haproxyconfig resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			haproxyconfig_obj = haproxyconfig()
			option_ = options()
			option_._count=True
			response = haproxyconfig_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of haproxyconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			haproxyconfig_obj = haproxyconfig()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = haproxyconfig_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(haproxyconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.haproxyconfig
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxyconfig_responses, response, "haproxyconfig_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.haproxyconfig_response_array
				i=0
				error = [haproxyconfig() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.haproxyconfig_response_array
			i=0
			haproxyconfig_objs = [haproxyconfig() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_haproxyconfig'):
					for props in obj._haproxyconfig:
						result = service.payload_formatter.string_to_bulk_resource(haproxyconfig_response,self.__class__.__name__,props)
						haproxyconfig_objs[i] = result.haproxyconfig
						i=i+1
			return haproxyconfig_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(haproxyconfig,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class haproxyconfig_response(base_response):
	def __init__(self,length=1) :
		self.haproxyconfig= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.haproxyconfig= [ haproxyconfig() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class haproxyconfig_responses(base_response):
	def __init__(self,length=1) :
		self.haproxyconfig_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.haproxyconfig_response_array = [ haproxyconfig() for _ in range(length)]
