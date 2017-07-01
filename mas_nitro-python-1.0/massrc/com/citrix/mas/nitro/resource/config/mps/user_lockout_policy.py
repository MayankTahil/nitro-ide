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
Configuration for User Lockout Policy configuration resource
'''

class user_lockout_policy(base_resource):
	_user_lockout_interval= ""
	_invalid_logins= ""
	_id= ""
	_enable_user_lockout= ""
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
			return "user_lockout_policy"
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
			return "user_lockout_policys"
		except Exception as e :
			raise e



	'''
	get User lockout Interval in secoonds 
	'''
	@property
	def user_lockout_interval(self) :
		try:
			return self._user_lockout_interval
		except Exception as e :
			raise e
	'''
	set User lockout Interval in secoonds 
	'''
	@user_lockout_interval.setter
	def user_lockout_interval(self,user_lockout_interval):
		try :
			if not isinstance(user_lockout_interval,int):
				raise TypeError("user_lockout_interval must be set to int value")
			self._user_lockout_interval = user_lockout_interval
		except Exception as e :
			raise e


	'''
	get No of invalid logins for User lockout 
	'''
	@property
	def invalid_logins(self) :
		try:
			return self._invalid_logins
		except Exception as e :
			raise e
	'''
	set No of invalid logins for User lockout 
	'''
	@invalid_logins.setter
	def invalid_logins(self,invalid_logins):
		try :
			if not isinstance(invalid_logins,int):
				raise TypeError("invalid_logins must be set to int value")
			self._invalid_logins = invalid_logins
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Enable user User lockout feature
	'''
	@property
	def enable_user_lockout(self) :
		try:
			return self._enable_user_lockout
		except Exception as e :
			raise e
	'''
	set Enable user User lockout feature
	'''
	@enable_user_lockout.setter
	def enable_user_lockout(self,enable_user_lockout):
		try :
			if not isinstance(enable_user_lockout,bool):
				raise TypeError("enable_user_lockout must be set to bool value")
			self._enable_user_lockout = enable_user_lockout
		except Exception as e :
			raise e

	'''
	Use this operation to get User Lockout Policy details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				user_lockout_policy_obj=user_lockout_policy()
				response = user_lockout_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify User Lockout Policy details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				user_lockout_policy_obj=user_lockout_policy()
				return cls.update_bulk_request(client,resource,user_lockout_policy_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of user_lockout_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			user_lockout_policy_obj = user_lockout_policy()
			option_ = options()
			option_._filter=filter_
			return user_lockout_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the user_lockout_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			user_lockout_policy_obj = user_lockout_policy()
			option_ = options()
			option_._count=True
			response = user_lockout_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of user_lockout_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			user_lockout_policy_obj = user_lockout_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = user_lockout_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(user_lockout_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.user_lockout_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(user_lockout_policy_responses, response, "user_lockout_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.user_lockout_policy_response_array
				i=0
				error = [user_lockout_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.user_lockout_policy_response_array
			i=0
			user_lockout_policy_objs = [user_lockout_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_user_lockout_policy'):
					for props in obj._user_lockout_policy:
						result = service.payload_formatter.string_to_bulk_resource(user_lockout_policy_response,self.__class__.__name__,props)
						user_lockout_policy_objs[i] = result.user_lockout_policy
						i=i+1
			return user_lockout_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(user_lockout_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class user_lockout_policy_response(base_response):
	def __init__(self,length=1) :
		self.user_lockout_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.user_lockout_policy= [ user_lockout_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class user_lockout_policy_responses(base_response):
	def __init__(self,length=1) :
		self.user_lockout_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.user_lockout_policy_response_array = [ user_lockout_policy() for _ in range(length)]
