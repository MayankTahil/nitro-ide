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
Configuration for Ping resource
'''

class ping(base_resource):
	_device_ipaddress= ""
	_ping_status= ""
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
			return "ping"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._device_ipaddress
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
			return "pings"
		except Exception as e :
			raise e



	'''
	get Device IP Address
	'''
	@property
	def device_ipaddress(self) :
		try:
			return self._device_ipaddress
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@device_ipaddress.setter
	def device_ipaddress(self,device_ipaddress):
		try :
			if not isinstance(device_ipaddress,str):
				raise TypeError("device_ipaddress must be set to str value")
			self._device_ipaddress = device_ipaddress
		except Exception as e :
			raise e


	'''
	get Status of ping
	'''
	@property
	def ping_status(self) :
		try:
			return self._ping_status
		except Exception as e :
			raise e

	'''
	Use this operation to get the status of ping on a given device.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ping_obj=ping()
				response = ping_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ping_obj = ping()
			option_ = options()
			option_._filter=filter_
			return ping_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ping resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ping_obj = ping()
			option_ = options()
			option_._count=True
			response = ping_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ping_obj = ping()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ping_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ping
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ping_responses, response, "ping_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ping_response_array
				i=0
				error = [ping() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ping_response_array
			i=0
			ping_objs = [ping() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ping'):
					for props in obj._ping:
						result = service.payload_formatter.string_to_bulk_resource(ping_response,self.__class__.__name__,props)
						ping_objs[i] = result.ping
						i=i+1
			return ping_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ping,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ping_response(base_response):
	def __init__(self,length=1) :
		self.ping= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ping= [ ping() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ping_responses(base_response):
	def __init__(self,length=1) :
		self.ping_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ping_response_array = [ ping() for _ in range(length)]
