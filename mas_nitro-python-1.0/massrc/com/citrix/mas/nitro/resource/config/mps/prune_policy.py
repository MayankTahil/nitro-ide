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
Configuration for Prune Policy resource
'''

class prune_policy(base_resource):
	_policy_name= ""
	_data_to_keep_in_days= ""
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
			return "prune_policy"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._policy_name
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
			return "prune_policys"
		except Exception as e :
			raise e



	'''
	get Policy Name
	'''
	@property
	def policy_name(self) :
		try:
			return self._policy_name
		except Exception as e :
			raise e
	'''
	set Policy Name
	'''
	@policy_name.setter
	def policy_name(self,policy_name):
		try :
			if not isinstance(policy_name,str):
				raise TypeError("policy_name must be set to str value")
			self._policy_name = policy_name
		except Exception as e :
			raise e


	'''
	get Number of days data to retain
	'''
	@property
	def data_to_keep_in_days(self) :
		try:
			return self._data_to_keep_in_days
		except Exception as e :
			raise e
	'''
	set Number of days data to retain
	'''
	@data_to_keep_in_days.setter
	def data_to_keep_in_days(self,data_to_keep_in_days):
		try :
			if not isinstance(data_to_keep_in_days,int):
				raise TypeError("data_to_keep_in_days must be set to int value")
			self._data_to_keep_in_days = data_to_keep_in_days
		except Exception as e :
			raise e

	'''
	Use this operation to get the prune policy to view number of days data to retain.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				prune_policy_obj=prune_policy()
				response = prune_policy_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify the number of days data to retain.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of prune_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			prune_policy_obj = prune_policy()
			option_ = options()
			option_._filter=filter_
			return prune_policy_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the prune_policy resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			prune_policy_obj = prune_policy()
			option_ = options()
			option_._count=True
			response = prune_policy_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of prune_policy resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			prune_policy_obj = prune_policy()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = prune_policy_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(prune_policy_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.prune_policy
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(prune_policy_responses, response, "prune_policy_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.prune_policy_response_array
				i=0
				error = [prune_policy() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.prune_policy_response_array
			i=0
			prune_policy_objs = [prune_policy() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_prune_policy'):
					for props in obj._prune_policy:
						result = service.payload_formatter.string_to_bulk_resource(prune_policy_response,self.__class__.__name__,props)
						prune_policy_objs[i] = result.prune_policy
						i=i+1
			return prune_policy_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(prune_policy,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class prune_policy_response(base_response):
	def __init__(self,length=1) :
		self.prune_policy= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.prune_policy= [ prune_policy() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class prune_policy_responses(base_response):
	def __init__(self,length=1) :
		self.prune_policy_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.prune_policy_response_array = [ prune_policy() for _ in range(length)]
