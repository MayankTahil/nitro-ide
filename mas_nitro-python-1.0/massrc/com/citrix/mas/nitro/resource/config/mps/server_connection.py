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
Configuration for server properties resource
'''

class server_connection(base_resource):
	_server_rtt= ""
	_count= ""
	_longitude= ""
	_latitude= ""
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
			return "server_connection"
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
			return "server_connections"
		except Exception as e :
			raise e



	'''
	get client RTT.
	'''
	@property
	def server_rtt(self) :
		try:
			return self._server_rtt
		except Exception as e :
			raise e
	'''
	set client RTT.
	'''
	@server_rtt.setter
	def server_rtt(self,server_rtt):
		try :
			if not isinstance(server_rtt,int):
				raise TypeError("server_rtt must be set to int value")
			self._server_rtt = server_rtt
		except Exception as e :
			raise e


	'''
	get count
	'''
	@property
	def count(self) :
		try:
			return self._count
		except Exception as e :
			raise e
	'''
	set count
	'''
	@count.setter
	def count(self,count):
		try :
			if not isinstance(count,int):
				raise TypeError("count must be set to int value")
			self._count = count
		except Exception as e :
			raise e


	'''
	get longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_connection_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server_connection
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(server_connection_responses, response, "server_connection_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.server_connection_response_array
				i=0
				error = [server_connection() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.server_connection_response_array
			i=0
			server_connection_objs = [server_connection() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_server_connection'):
					for props in obj._server_connection:
						result = service.payload_formatter.string_to_bulk_resource(server_connection_response,self.__class__.__name__,props)
						server_connection_objs[i] = result.server_connection
						i=i+1
			return server_connection_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(server_connection,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class server_connection_response(base_response):
	def __init__(self,length=1) :
		self.server_connection= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.server_connection= [ server_connection() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class server_connection_responses(base_response):
	def __init__(self,length=1) :
		self.server_connection_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.server_connection_response_array = [ server_connection() for _ in range(length)]
