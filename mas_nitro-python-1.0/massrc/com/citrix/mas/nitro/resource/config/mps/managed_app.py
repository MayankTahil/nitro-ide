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
from massrc.com.citrix.mas.nitro.resource.config.mps.network_function_config import network_function_config


'''
Configuration for Managed Application resource
'''

class managed_app(base_resource):
	_app_networking_data= ""
	_is_app_placed= ""
	_lb_role= ""
	_container_manager= ""
	_app_id= ""
	_app_netfuncs_config=[]
	_networking_manager= ""
	_app_dns= ""
	_appname= ""
	_dns_manager= ""
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
			return "managed_app"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._app_id
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
			return "managed_apps"
		except Exception as e :
			raise e



	'''
	get app networking blob that can be used by placement logic
	'''
	@property
	def app_networking_data(self) :
		try:
			return self._app_networking_data
		except Exception as e :
			raise e
	'''
	set app networking blob that can be used by placement logic
	'''
	@app_networking_data.setter
	def app_networking_data(self,app_networking_data):
		try :
			if not isinstance(app_networking_data,str):
				raise TypeError("app_networking_data must be set to str value")
			self._app_networking_data = app_networking_data
		except Exception as e :
			raise e


	'''
	get 1 if app is placed on some NS, else 0.
	'''
	@property
	def is_app_placed(self) :
		try:
			return self._is_app_placed
		except Exception as e :
			raise e
	'''
	set 1 if app is placed on some NS, else 0.
	'''
	@is_app_placed.setter
	def is_app_placed(self,is_app_placed):
		try :
			if not isinstance(is_app_placed,bool):
				raise TypeError("is_app_placed must be set to bool value")
			self._is_app_placed = is_app_placed
		except Exception as e :
			raise e


	'''
	get Application is applied only on the devices with the same Lb role
	'''
	@property
	def lb_role(self) :
		try:
			return self._lb_role
		except Exception as e :
			raise e
	'''
	set Application is applied only on the devices with the same Lb role
	'''
	@lb_role.setter
	def lb_role(self,lb_role):
		try :
			if not isinstance(lb_role,str):
				raise TypeError("lb_role must be set to str value")
			self._lb_role = lb_role
		except Exception as e :
			raise e


	'''
	get Container orchestration system
	'''
	@property
	def container_manager(self) :
		try:
			return self._container_manager
		except Exception as e :
			raise e
	'''
	set Container orchestration system
	'''
	@container_manager.setter
	def container_manager(self,container_manager):
		try :
			if not isinstance(container_manager,str):
				raise TypeError("container_manager must be set to str value")
			self._container_manager = container_manager
		except Exception as e :
			raise e


	'''
	get Id for the managed application
	'''
	@property
	def app_id(self) :
		try:
			return self._app_id
		except Exception as e :
			raise e
	'''
	set Id for the managed application
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
	get Network function related config for the application
	'''
	@property
	def app_netfuncs_config(self) :
		try:
			return self._app_netfuncs_config
		except Exception as e :
			raise e
	'''
	set Network function related config for the application
	'''
	@app_netfuncs_config.setter
	def app_netfuncs_config(self,app_netfuncs_config) :
		try :
			if not isinstance(app_netfuncs_config,list):
				raise TypeError("app_netfuncs_config must be set to array of network_function_config value")
			for item in app_netfuncs_config :
				if not isinstance(item,network_function_config):
					raise TypeError("item must be set to network_function_config value")
			self._app_netfuncs_config = app_netfuncs_config
		except Exception as e :
			raise e


	'''
	get System used to setup the network
	'''
	@property
	def networking_manager(self) :
		try:
			return self._networking_manager
		except Exception as e :
			raise e
	'''
	set System used to setup the network
	'''
	@networking_manager.setter
	def networking_manager(self,networking_manager):
		try :
			if not isinstance(networking_manager,str):
				raise TypeError("networking_manager must be set to str value")
			self._networking_manager = networking_manager
		except Exception as e :
			raise e


	'''
	get Doman name service for Application
	'''
	@property
	def app_dns(self) :
		try:
			return self._app_dns
		except Exception as e :
			raise e
	'''
	set Doman name service for Application
	'''
	@app_dns.setter
	def app_dns(self,app_dns):
		try :
			if not isinstance(app_dns,str):
				raise TypeError("app_dns must be set to str value")
			self._app_dns = app_dns
		except Exception as e :
			raise e


	'''
	get Name of the Application
	'''
	@property
	def appname(self) :
		try:
			return self._appname
		except Exception as e :
			raise e
	'''
	set Name of the Application
	'''
	@appname.setter
	def appname(self,appname):
		try :
			if not isinstance(appname,str):
				raise TypeError("appname must be set to str value")
			self._appname = appname
		except Exception as e :
			raise e


	'''
	get Domain Name Service manager
	'''
	@property
	def dns_manager(self) :
		try:
			return self._dns_manager
		except Exception as e :
			raise e
	'''
	set Domain Name Service manager
	'''
	@dns_manager.setter
	def dns_manager(self,dns_manager):
		try :
			if not isinstance(dns_manager,str):
				raise TypeError("dns_manager must be set to str value")
			self._dns_manager = dns_manager
		except Exception as e :
			raise e


	'''
	get Dummy Id needed for input get requests
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Dummy Id needed for input get requests
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
	Use this operation to add an managed application.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				managed_app_obj= managed_app()
				return cls.perform_operation_bulk_request(service,"add", resource,managed_app_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete an managed application.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					managed_app_obj=managed_app()
					return cls.delete_bulk_request(client,resource,managed_app_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get an managed application.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				managed_app_obj=managed_app()
				response = managed_app_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update managed application.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				managed_app_obj=managed_app()
				return cls.update_bulk_request(client,resource,managed_app_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of managed_app resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			managed_app_obj = managed_app()
			option_ = options()
			option_._filter=filter_
			return managed_app_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the managed_app resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			managed_app_obj = managed_app()
			option_ = options()
			option_._count=True
			response = managed_app_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of managed_app resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			managed_app_obj = managed_app()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = managed_app_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(managed_app_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.managed_app
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_app_responses, response, "managed_app_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.managed_app_response_array
				i=0
				error = [managed_app() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.managed_app_response_array
			i=0
			managed_app_objs = [managed_app() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_managed_app'):
					for props in obj._managed_app:
						result = service.payload_formatter.string_to_bulk_resource(managed_app_response,self.__class__.__name__,props)
						managed_app_objs[i] = result.managed_app
						i=i+1
			return managed_app_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(managed_app,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class managed_app_response(base_response):
	def __init__(self,length=1) :
		self.managed_app= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.managed_app= [ managed_app() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class managed_app_responses(base_response):
	def __init__(self,length=1) :
		self.managed_app_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.managed_app_response_array = [ managed_app() for _ in range(length)]
