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
Configuration for Service used in application container resource
'''

class service(base_resource):
	_parent_name= ""
	_service_ip_address= ""
	_service_port= ""
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
			return "service"
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
			return "services"
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
	get IPv4 or IPv6 Address assigned to the service
	'''
	@property
	def service_ip_address(self) :
		try:
			return self._service_ip_address
		except Exception as e :
			raise e
	'''
	set IPv4 or IPv6 Address assigned to the service
	'''
	@service_ip_address.setter
	def service_ip_address(self,service_ip_address):
		try :
			if not isinstance(service_ip_address,str):
				raise TypeError("service_ip_address must be set to str value")
			self._service_ip_address = service_ip_address
		except Exception as e :
			raise e


	'''
	get Port number of the service
	'''
	@property
	def service_port(self) :
		try:
			return self._service_port
		except Exception as e :
			raise e
	'''
	set Port number of the service
	'''
	@service_port.setter
	def service_port(self,service_port):
		try :
			if not isinstance(service_port,int):
				raise TypeError("service_port must be set to int value")
			self._service_port = service_port
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
			result=service.payload_formatter.string_to_resource(service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.service
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(service_responses, response, "service_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.service_response_array
				i=0
				error = [service() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.service_response_array
			i=0
			service_objs = [service() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_service'):
					for props in obj._service:
						result = service.payload_formatter.string_to_bulk_resource(service_response,self.__class__.__name__,props)
						service_objs[i] = result.service
						i=i+1
			return service_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(service,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class service_response(base_response):
	def __init__(self,length=1) :
		self.service= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.service= [ service() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class service_responses(base_response):
	def __init__(self,length=1) :
		self.service_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.service_response_array = [ service() for _ in range(length)]
