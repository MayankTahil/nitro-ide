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
Configuration for Password Policy configuration resource
'''

class password_policy(base_resource):
	_enable_password_complexity= ""
	_minimum_password_length= ""
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
			return "password_policy"
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
			return "password_policys"
		except Exception as e :
			raise e



	'''
	get Enable user Password complexity
	'''
	@property
	def enable_password_complexity(self) :
		try:
			return self._enable_password_complexity
		except Exception as e :
			raise e
	'''
	set Enable user Password complexity
	'''
	@enable_password_complexity.setter
	def enable_password_complexity(self,enable_password_complexity):
		try :
			if not isinstance(enable_password_complexity,bool):
				raise TypeError("enable_password_complexity must be set to bool value")
			self._enable_password_complexity = enable_password_complexity
		except Exception as e :
			raise e


	'''
	get Minimum password length 
	'''
	@property
	def minimum_password_length(self) :
		try:
			return self._minimum_password_length
		except Exception as e :
			raise e
	'''
	set Minimum password length 
	'''
	@minimum_password_length.setter
	def minimum_password_length(self,minimum_password_length):
		try :
			if not isinstance(minimum_password_length,int):
				raise TypeError("minimum_password_length must be set to int value")
			self._minimum_password_length = minimum_password_length
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
	Use this operation to get Password Policy details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				password_policy_obj=password_policy()
				response = password_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify Password Policy details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				password_policy_obj=password_policy()
				return cls.update_bulk_request(client,resource,password_policy_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of password_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			password_policy_obj = password_policy()
			option_ = options()
			option_._filter=filter_
			return password_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the password_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			password_policy_obj = password_policy()
			option_ = options()
			option_._count=True
			response = password_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of password_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			password_policy_obj = password_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = password_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(password_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.password_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(password_policy_responses, response, "password_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.password_policy_response_array
				i=0
				error = [password_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.password_policy_response_array
			i=0
			password_policy_objs = [password_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_password_policy'):
					for props in obj._password_policy:
						result = service.payload_formatter.string_to_bulk_resource(password_policy_response,self.__class__.__name__,props)
						password_policy_objs[i] = result.password_policy
						i=i+1
			return password_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(password_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class password_policy_response(base_response):
	def __init__(self,length=1) :
		self.password_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.password_policy= [ password_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class password_policy_responses(base_response):
	def __init__(self,length=1) :
		self.password_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.password_policy_response_array = [ password_policy() for _ in range(length)]
