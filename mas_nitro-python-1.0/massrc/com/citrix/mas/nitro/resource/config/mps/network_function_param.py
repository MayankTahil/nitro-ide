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
from massrc.com.citrix.mas.nitro.resource.config.mps.app_device import app_device


'''
Configuration for Parameters for the Network function config for the application resource
'''

class network_function_param(base_resource):
	_parameters= ""
	_parent_name= ""
	_netfunc_id= ""
	_config_id= ""
	_id= ""
	_app_devices=[]
	_parent_id= ""
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
			return "network_function_param"
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
			return "network_function_params"
		except Exception as e :
			raise e



	'''
	get Payload parameters for the network function
	'''
	@property
	def parameters(self) :
		try:
			return self._parameters
		except Exception as e :
			raise e
	'''
	set Payload parameters for the network function
	'''
	@parameters.setter
	def parameters(self,parameters):
		try :
			if not isinstance(parameters,str):
				raise TypeError("parameters must be set to str value")
			self._parameters = parameters
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
	get ID of network function
	'''
	@property
	def netfunc_id(self) :
		try:
			return self._netfunc_id
		except Exception as e :
			raise e
	'''
	set ID of network function
	'''
	@netfunc_id.setter
	def netfunc_id(self,netfunc_id):
		try :
			if not isinstance(netfunc_id,str):
				raise TypeError("netfunc_id must be set to str value")
			self._netfunc_id = netfunc_id
		except Exception as e :
			raise e


	'''
	get Stylebook config Id for the managed application
	'''
	@property
	def config_id(self) :
		try:
			return self._config_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the servers
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the servers
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
	get Details of devices used by the managed app
	'''
	@property
	def app_devices(self) :
		try:
			return self._app_devices
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
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_function_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_function_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_function_param_responses, response, "network_function_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_function_param_response_array
				i=0
				error = [network_function_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_function_param_response_array
			i=0
			network_function_param_objs = [network_function_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_function_param'):
					for props in obj._network_function_param:
						result = service.payload_formatter.string_to_bulk_resource(network_function_param_response,self.__class__.__name__,props)
						network_function_param_objs[i] = result.network_function_param
						i=i+1
			return network_function_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_function_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_function_param_response(base_response):
	def __init__(self,length=1) :
		self.network_function_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_function_param= [ network_function_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_function_param_responses(base_response):
	def __init__(self,length=1) :
		self.network_function_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_function_param_response_array = [ network_function_param() for _ in range(length)]
