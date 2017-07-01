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
Configuration for This provides the FTU state of the user resource
'''

class tenant_system_info(base_resource):
	_services_subscribed= ""
	_tenant_id= ""
	_ftu_state= ""
	_id= ""
	_username= ""
	_agent_download_state= ""
	_services_subscribed_list_arr=[]
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
			return "tenant_system_info"
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
			return "tenant_system_infos"
		except Exception as e :
			raise e



	'''
	get Services Entitled By the user
	'''
	@property
	def services_subscribed(self) :
		try:
			return self._services_subscribed
		except Exception as e :
			raise e
	'''
	set Services Entitled By the user
	'''
	@services_subscribed.setter
	def services_subscribed(self,services_subscribed):
		try :
			if not isinstance(services_subscribed,str):
				raise TypeError("services_subscribed must be set to str value")
			self._services_subscribed = services_subscribed
		except Exception as e :
			raise e


	'''
	get Id of the parent tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Ftu state of the tenant
	'''
	@property
	def ftu_state(self) :
		try:
			return self._ftu_state
		except Exception as e :
			raise e
	'''
	set Ftu state of the tenant
	'''
	@ftu_state.setter
	def ftu_state(self,ftu_state):
		try :
			if not isinstance(ftu_state,int):
				raise TypeError("ftu_state must be set to int value")
			self._ftu_state = ftu_state
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the syslog generic record.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e


	'''
	get user logged in
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set user logged in
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
	get Agent download state
	'''
	@property
	def agent_download_state(self) :
		try:
			return self._agent_download_state
		except Exception as e :
			raise e
	'''
	set Agent download state
	'''
	@agent_download_state.setter
	def agent_download_state(self,agent_download_state):
		try :
			if not isinstance(agent_download_state,int):
				raise TypeError("agent_download_state must be set to int value")
			self._agent_download_state = agent_download_state
		except Exception as e :
			raise e

	'''
	Subscribed Services list
	'''
	@property
	def services_subscribed_list_arr(self) :
		try:
			return self._services_subscribed_list_arr
		except Exception as e :
			raise e
	'''
	Subscribed Services list
	'''
	@services_subscribed_list_arr.setter
	def services_subscribed_list_arr(self,services_subscribed_list_arr) :
		try :
			if not isinstance(services_subscribed_list_arr,list):
				raise TypeError("services_subscribed_list_arr must be set to array of str value")
			for item in services_subscribed_list_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._services_subscribed_list_arr = services_subscribed_list_arr
		except Exception as e :
			raise e

	'''
	Use this operations to add services for the user.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				tenant_system_info_obj= tenant_system_info()
				return cls.perform_operation_bulk_request(service,"add", resource,tenant_system_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get FTU state related information for a user.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				tenant_system_info_obj=tenant_system_info()
				response = tenant_system_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operations to modify services used by  the user.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				tenant_system_info_obj=tenant_system_info()
				return cls.update_bulk_request(client,resource,tenant_system_info_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of tenant_system_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			tenant_system_info_obj = tenant_system_info()
			option_ = options()
			option_._filter=filter_
			return tenant_system_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the tenant_system_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			tenant_system_info_obj = tenant_system_info()
			option_ = options()
			option_._count=True
			response = tenant_system_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of tenant_system_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			tenant_system_info_obj = tenant_system_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = tenant_system_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(tenant_system_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_system_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_system_info_responses, response, "tenant_system_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_system_info_response_array
				i=0
				error = [tenant_system_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_system_info_response_array
			i=0
			tenant_system_info_objs = [tenant_system_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_system_info'):
					for props in obj._tenant_system_info:
						result = service.payload_formatter.string_to_bulk_resource(tenant_system_info_response,self.__class__.__name__,props)
						tenant_system_info_objs[i] = result.tenant_system_info
						i=i+1
			return tenant_system_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_system_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_system_info_response(base_response):
	def __init__(self,length=1) :
		self.tenant_system_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_system_info= [ tenant_system_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_system_info_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_system_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_system_info_response_array = [ tenant_system_info() for _ in range(length)]
