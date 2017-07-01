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
Configuration for NTP Server resource
'''

class ntp_server(base_resource):
	_preferred_server= ""
	_maxpoll= ""
	_minpoll= ""
	_autokey= ""
	_key_id= ""
	_server= ""
	_client= ""
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
			return "ntp_server"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._server
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
			return "ntp_servers"
		except Exception as e :
			raise e



	'''
	get NTP Server Preferred
	'''
	@property
	def preferred_server(self) :
		try:
			return self._preferred_server
		except Exception as e :
			raise e
	'''
	set NTP Server Preferred
	'''
	@preferred_server.setter
	def preferred_server(self,preferred_server):
		try :
			if not isinstance(preferred_server,bool):
				raise TypeError("preferred_server must be set to bool value")
			self._preferred_server = preferred_server
		except Exception as e :
			raise e


	'''
	get Maximum Poll Interval
	'''
	@property
	def maxpoll(self) :
		try:
			return self._maxpoll
		except Exception as e :
			raise e
	'''
	set Maximum Poll Interval
	'''
	@maxpoll.setter
	def maxpoll(self,maxpoll):
		try :
			if not isinstance(maxpoll,int):
				raise TypeError("maxpoll must be set to int value")
			self._maxpoll = maxpoll
		except Exception as e :
			raise e


	'''
	get Minimum Poll Interval
	'''
	@property
	def minpoll(self) :
		try:
			return self._minpoll
		except Exception as e :
			raise e
	'''
	set Minimum Poll Interval
	'''
	@minpoll.setter
	def minpoll(self,minpoll):
		try :
			if not isinstance(minpoll,int):
				raise TypeError("minpoll must be set to int value")
			self._minpoll = minpoll
		except Exception as e :
			raise e


	'''
	get Autokey Public Key Authentication
	'''
	@property
	def autokey(self) :
		try:
			return self._autokey
		except Exception as e :
			raise e
	'''
	set Autokey Public Key Authentication
	'''
	@autokey.setter
	def autokey(self,autokey):
		try :
			if not isinstance(autokey,bool):
				raise TypeError("autokey must be set to bool value")
			self._autokey = autokey
		except Exception as e :
			raise e


	'''
	get Key Identifier for Symmetric Key Authentication
	'''
	@property
	def key_id(self) :
		try:
			return self._key_id
		except Exception as e :
			raise e
	'''
	set Key Identifier for Symmetric Key Authentication
	'''
	@key_id.setter
	def key_id(self,key_id):
		try :
			if not isinstance(key_id,int):
				raise TypeError("key_id must be set to int value")
			self._key_id = key_id
		except Exception as e :
			raise e


	'''
	get NTP Time Server Address
	'''
	@property
	def server(self) :
		try:
			return self._server
		except Exception as e :
			raise e
	'''
	set NTP Time Server Address
	'''
	@server.setter
	def server(self,server):
		try :
			if not isinstance(server,str):
				raise TypeError("server must be set to str value")
			self._server = server
		except Exception as e :
			raise e

	'''
	Sender of request, whether from Setup Wizard or direct NTP configuration
	'''
	@property
	def client(self):
		try:
			return self._client
		except Exception as e :
			raise e
	'''
	Sender of request, whether from Setup Wizard or direct NTP configuration
	'''
	@client.setter
	def client(self,client):
		try :
			if not isinstance(client,str):
				raise TypeError("client must be set to str value")
			self._client = client
		except Exception as e :
			raise e

	'''
	Use this operation to add NTP Server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ntp_server_obj= ntp_server()
				return cls.perform_operation_bulk_request(service,"add", resource,ntp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete NTP Server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ntp_server_obj=ntp_server()
					return cls.delete_bulk_request(client,resource,ntp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NTP Server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ntp_server_obj=ntp_server()
				response = ntp_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify NTP Server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ntp_server_obj=ntp_server()
				return cls.update_bulk_request(client,resource,ntp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ntp_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ntp_server_obj = ntp_server()
			option_ = options()
			option_._filter=filter_
			return ntp_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ntp_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ntp_server_obj = ntp_server()
			option_ = options()
			option_._count=True
			response = ntp_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ntp_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ntp_server_obj = ntp_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ntp_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ntp_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ntp_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ntp_server_responses, response, "ntp_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ntp_server_response_array
				i=0
				error = [ntp_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ntp_server_response_array
			i=0
			ntp_server_objs = [ntp_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ntp_server'):
					for props in obj._ntp_server:
						result = service.payload_formatter.string_to_bulk_resource(ntp_server_response,self.__class__.__name__,props)
						ntp_server_objs[i] = result.ntp_server
						i=i+1
			return ntp_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ntp_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ntp_server_response(base_response):
	def __init__(self,length=1) :
		self.ntp_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ntp_server= [ ntp_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ntp_server_responses(base_response):
	def __init__(self,length=1) :
		self.ntp_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ntp_server_response_array = [ ntp_server() for _ in range(length)]
