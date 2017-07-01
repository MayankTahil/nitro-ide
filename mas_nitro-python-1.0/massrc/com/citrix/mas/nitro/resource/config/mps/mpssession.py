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
Configuration for Client Session resource
'''

class mpssession(base_resource):
	_tenant_name= ""
	_expire_after= ""
	_login_time= ""
	_permission= ""
	_session_timeout= ""
	_port= ""
	_username= ""
	_client_type= ""
	_last_activity_time= ""
	_is_external_auth= ""
	_id= ""
	_ip_address= ""
	_is_self= ""
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
			return "mpssession"
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
			return "mpssessions"
		except Exception as e :
			raise e



	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get Session will expire after these many seconds
	'''
	@property
	def expire_after(self) :
		try:
			return self._expire_after
		except Exception as e :
			raise e


	'''
	get Session was initiated at this time
	'''
	@property
	def login_time(self) :
		try:
			return self._login_time
		except Exception as e :
			raise e


	'''
	get Permission to identify who created the session
	'''
	@property
	def permission(self) :
		try:
			return self._permission
		except Exception as e :
			raise e
	'''
	set Permission to identify who created the session
	'''
	@permission.setter
	def permission(self,permission):
		try :
			if not isinstance(permission,str):
				raise TypeError("permission must be set to str value")
			self._permission = permission
		except Exception as e :
			raise e


	'''
	get Session Timeout set for this session
	'''
	@property
	def session_timeout(self) :
		try:
			return self._session_timeout
		except Exception as e :
			raise e


	'''
	get Port from where this session was initiated
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e


	'''
	get User Name who initiated this session
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Client Type
	'''
	@property
	def client_type(self) :
		try:
			return self._client_type
		except Exception as e :
			raise e


	'''
	get Last Activity Time for this session
	'''
	@property
	def last_activity_time(self) :
		try:
			return self._last_activity_time
		except Exception as e :
			raise e


	'''
	get Is session created by using external authentication
	'''
	@property
	def is_external_auth(self) :
		try:
			return self._is_external_auth
		except Exception as e :
			raise e
	'''
	set Is session created by using external authentication
	'''
	@is_external_auth.setter
	def is_external_auth(self,is_external_auth):
		try :
			if not isinstance(is_external_auth,bool):
				raise TypeError("is_external_auth must be set to bool value")
			self._is_external_auth = is_external_auth
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the client sessions
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the client sessions
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
	get IP Aaddress from where this session was initiated
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e

	'''
	true, if this session is for current logged-in user
	'''
	@property
	def is_self(self):
		try:
			return self._is_self
		except Exception as e :
			raise e

	'''
	Use this operation to get client sessions.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mpssession_obj=mpssession()
				response = mpssession_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Kill client session by providing id.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					mpssession_obj=mpssession()
					return cls.delete_bulk_request(client,resource,mpssession_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mpssession resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mpssession_obj = mpssession()
			option_ = options()
			option_._filter=filter_
			return mpssession_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mpssession resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mpssession_obj = mpssession()
			option_ = options()
			option_._count=True
			response = mpssession_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mpssession resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mpssession_obj = mpssession()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mpssession_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mpssession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mpssession
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mpssession_responses, response, "mpssession_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mpssession_response_array
				i=0
				error = [mpssession() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mpssession_response_array
			i=0
			mpssession_objs = [mpssession() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mpssession'):
					for props in obj._mpssession:
						result = service.payload_formatter.string_to_bulk_resource(mpssession_response,self.__class__.__name__,props)
						mpssession_objs[i] = result.mpssession
						i=i+1
			return mpssession_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mpssession,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mpssession_response(base_response):
	def __init__(self,length=1) :
		self.mpssession= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mpssession= [ mpssession() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mpssession_responses(base_response):
	def __init__(self,length=1) :
		self.mpssession_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mpssession_response_array = [ mpssession() for _ in range(length)]
