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
Configuration for Preauth token required for Agent registration resource
'''

class trust_preauthtoken(base_resource):
	_name= ""
	_token= ""
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
			return "trust_preauthtoken"
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
			return "trust_preauthtokens"
		except Exception as e :
			raise e


	'''
	Name of the Tenant
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name of the Tenant
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
	Preauth token for a tenant
	'''
	@property
	def token(self):
		try:
			return self._token
		except Exception as e :
			raise e
	'''
	Preauth token for a tenant
	'''
	@token.setter
	def token(self,token):
		try :
			if not isinstance(token,str):
				raise TypeError("token must be set to str value")
			self._token = token
		except Exception as e :
			raise e

	'''
	Use this operation to generate a preauthtoken for a tenant.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				trust_preauthtoken_obj=trust_preauthtoken()
				response = trust_preauthtoken_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of trust_preauthtoken resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			trust_preauthtoken_obj = trust_preauthtoken()
			option_ = options()
			option_._filter=filter_
			return trust_preauthtoken_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the trust_preauthtoken resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			trust_preauthtoken_obj = trust_preauthtoken()
			option_ = options()
			option_._count=True
			response = trust_preauthtoken_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of trust_preauthtoken resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			trust_preauthtoken_obj = trust_preauthtoken()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = trust_preauthtoken_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(trust_preauthtoken_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.trust_preauthtoken
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(trust_preauthtoken_responses, response, "trust_preauthtoken_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.trust_preauthtoken_response_array
				i=0
				error = [trust_preauthtoken() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.trust_preauthtoken_response_array
			i=0
			trust_preauthtoken_objs = [trust_preauthtoken() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_trust_preauthtoken'):
					for props in obj._trust_preauthtoken:
						result = service.payload_formatter.string_to_bulk_resource(trust_preauthtoken_response,self.__class__.__name__,props)
						trust_preauthtoken_objs[i] = result.trust_preauthtoken
						i=i+1
			return trust_preauthtoken_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(trust_preauthtoken,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class trust_preauthtoken_response(base_response):
	def __init__(self,length=1) :
		self.trust_preauthtoken= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.trust_preauthtoken= [ trust_preauthtoken() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class trust_preauthtoken_responses(base_response):
	def __init__(self,length=1) :
		self.trust_preauthtoken_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.trust_preauthtoken_response_array = [ trust_preauthtoken() for _ in range(length)]
