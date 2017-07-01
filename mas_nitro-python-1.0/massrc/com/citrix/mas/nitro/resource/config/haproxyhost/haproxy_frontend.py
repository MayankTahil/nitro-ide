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
Configuration for HAProxy Frontend resource
'''

class haproxy_frontend(base_resource):
	_user_managed= ""
	_instance_id= ""
	_name= ""
	_port= ""
	_host= ""
	_managed= ""
	_configuration_path= ""
	_id= ""
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
			return "haproxy_frontend"
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
			return "haproxy_frontends"
		except Exception as e :
			raise e



	'''
	get User Managed Idenfication
	'''
	@property
	def user_managed(self) :
		try:
			return self._user_managed
		except Exception as e :
			raise e
	'''
	set User Managed Idenfication
	'''
	@user_managed.setter
	def user_managed(self,user_managed):
		try :
			if not isinstance(user_managed,bool):
				raise TypeError("user_managed must be set to bool value")
			self._user_managed = user_managed
		except Exception as e :
			raise e


	'''
	get Instance ID of HA Proxy Instance.
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e


	'''
	get HAProxy frontend name .
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get HAProxy frontend port .
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e


	'''
	get HAProxy frontend host .
	'''
	@property
	def host(self) :
		try:
			return self._host
		except Exception as e :
			raise e


	'''
	get Managed
	'''
	@property
	def managed(self) :
		try:
			return self._managed
		except Exception as e :
			raise e
	'''
	set Managed
	'''
	@managed.setter
	def managed(self,managed):
		try :
			if not isinstance(managed,bool):
				raise TypeError("managed must be set to bool value")
			self._managed = managed
		except Exception as e :
			raise e


	'''
	get Config Path of HA Proxies on this HAPRoxy Host.
	'''
	@property
	def configuration_path(self) :
		try:
			return self._configuration_path
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
	get HAProxy  host  ipaddress.
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get HAProxy frontend for HAProxy Instances.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				haproxy_frontend_obj=haproxy_frontend()
				response = haproxy_frontend_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of haproxy_frontend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			haproxy_frontend_obj = haproxy_frontend()
			option_ = options()
			option_._filter=filter_
			return haproxy_frontend_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the haproxy_frontend resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			haproxy_frontend_obj = haproxy_frontend()
			option_ = options()
			option_._count=True
			response = haproxy_frontend_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of haproxy_frontend resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			haproxy_frontend_obj = haproxy_frontend()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = haproxy_frontend_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(haproxy_frontend_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.haproxy_frontend
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxy_frontend_responses, response, "haproxy_frontend_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.haproxy_frontend_response_array
				i=0
				error = [haproxy_frontend() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.haproxy_frontend_response_array
			i=0
			haproxy_frontend_objs = [haproxy_frontend() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_haproxy_frontend'):
					for props in obj._haproxy_frontend:
						result = service.payload_formatter.string_to_bulk_resource(haproxy_frontend_response,self.__class__.__name__,props)
						haproxy_frontend_objs[i] = result.haproxy_frontend
						i=i+1
			return haproxy_frontend_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(haproxy_frontend,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class haproxy_frontend_response(base_response):
	def __init__(self,length=1) :
		self.haproxy_frontend= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.haproxy_frontend= [ haproxy_frontend() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class haproxy_frontend_responses(base_response):
	def __init__(self,length=1) :
		self.haproxy_frontend_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.haproxy_frontend_response_array = [ haproxy_frontend() for _ in range(length)]
