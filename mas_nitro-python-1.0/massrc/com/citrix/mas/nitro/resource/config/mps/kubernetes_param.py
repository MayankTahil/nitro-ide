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
Configuration for Kubernetes params used in triton config resource
'''

class kubernetes_param(base_resource):
	_parent_name= ""
	_insecure_skip_verify= ""
	_ca= ""
	_token= ""
	_parent_id= ""
	_apiserver= ""
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
			return "kubernetes_param"
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
			return "kubernetes_params"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Whether to skip verifying server certificate
	'''
	@property
	def insecure_skip_verify(self) :
		try:
			return self._insecure_skip_verify
		except Exception as e :
			raise e
	'''
	set Whether to skip verifying server certificate
	'''
	@insecure_skip_verify.setter
	def insecure_skip_verify(self,insecure_skip_verify):
		try :
			if not isinstance(insecure_skip_verify,bool):
				raise TypeError("insecure_skip_verify must be set to bool value")
			self._insecure_skip_verify = insecure_skip_verify
		except Exception as e :
			raise e


	'''
	get Path to the CA certificate
	'''
	@property
	def ca(self) :
		try:
			return self._ca
		except Exception as e :
			raise e
	'''
	set Path to the CA certificate
	'''
	@ca.setter
	def ca(self,ca):
		try :
			if not isinstance(ca,str):
				raise TypeError("ca must be set to str value")
			self._ca = ca
		except Exception as e :
			raise e


	'''
	get Password for kubernetes connection
	'''
	@property
	def token(self) :
		try:
			return self._token
		except Exception as e :
			raise e
	'''
	set Password for kubernetes connection
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
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get URL to be used to connect to API server
	'''
	@property
	def apiserver(self) :
		try:
			return self._apiserver
		except Exception as e :
			raise e
	'''
	set URL to be used to connect to API server
	'''
	@apiserver.setter
	def apiserver(self,apiserver):
		try :
			if not isinstance(apiserver,str):
				raise TypeError("apiserver must be set to str value")
			self._apiserver = apiserver
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(kubernetes_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.kubernetes_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(kubernetes_param_responses, response, "kubernetes_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.kubernetes_param_response_array
				i=0
				error = [kubernetes_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.kubernetes_param_response_array
			i=0
			kubernetes_param_objs = [kubernetes_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_kubernetes_param'):
					for props in obj._kubernetes_param:
						result = service.payload_formatter.string_to_bulk_resource(kubernetes_param_response,self.__class__.__name__,props)
						kubernetes_param_objs[i] = result.kubernetes_param
						i=i+1
			return kubernetes_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(kubernetes_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class kubernetes_param_response(base_response):
	def __init__(self,length=1) :
		self.kubernetes_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.kubernetes_param= [ kubernetes_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class kubernetes_param_responses(base_response):
	def __init__(self,length=1) :
		self.kubernetes_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.kubernetes_param_response_array = [ kubernetes_param() for _ in range(length)]
