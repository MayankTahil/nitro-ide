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

class client_connection(base_resource):
	_hits= ""
	_count= ""
	_longitude= ""
	_latitude= ""
	_client_rtt= ""
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
			return "client_connection"
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
			return "client_connections"
		except Exception as e :
			raise e



	'''
	get Hits
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	set Hits
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,int):
				raise TypeError("hits must be set to int value")
			self._hits = hits
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
	get client RTT.
	'''
	@property
	def client_rtt(self) :
		try:
			return self._client_rtt
		except Exception as e :
			raise e
	'''
	set client RTT.
	'''
	@client_rtt.setter
	def client_rtt(self,client_rtt):
		try :
			if not isinstance(client_rtt,int):
				raise TypeError("client_rtt must be set to int value")
			self._client_rtt = client_rtt
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(client_connection_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.client_connection
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(client_connection_responses, response, "client_connection_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.client_connection_response_array
				i=0
				error = [client_connection() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.client_connection_response_array
			i=0
			client_connection_objs = [client_connection() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_client_connection'):
					for props in obj._client_connection:
						result = service.payload_formatter.string_to_bulk_resource(client_connection_response,self.__class__.__name__,props)
						client_connection_objs[i] = result.client_connection
						i=i+1
			return client_connection_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(client_connection,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class client_connection_response(base_response):
	def __init__(self,length=1) :
		self.client_connection= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.client_connection= [ client_connection() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class client_connection_responses(base_response):
	def __init__(self,length=1) :
		self.client_connection_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.client_connection_response_array = [ client_connection() for _ in range(length)]
