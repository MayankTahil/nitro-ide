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
Configuration for sdwanvw_appflowconfig resource.
'''

class sdwanvw_appflowconfig(base_resource):
	_tcp_hdx= ""
	_hdx= ""
	_connection_chaining= ""
	_ip_address= ""
	_id= ""
	_appflowfeature= ""
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
			return "sdwanvw_appflowconfig"
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
			return "sdwanvw_appflowconfigs"
		except Exception as e :
			raise e



	'''
	get tcp_hdx
	'''
	@property
	def tcp_hdx(self) :
		try:
			return self._tcp_hdx
		except Exception as e :
			raise e
	'''
	set tcp_hdx
	'''
	@tcp_hdx.setter
	def tcp_hdx(self,tcp_hdx):
		try :
			if not isinstance(tcp_hdx,bool):
				raise TypeError("tcp_hdx must be set to bool value")
			self._tcp_hdx = tcp_hdx
		except Exception as e :
			raise e


	'''
	get hdx
	'''
	@property
	def hdx(self) :
		try:
			return self._hdx
		except Exception as e :
			raise e
	'''
	set hdx
	'''
	@hdx.setter
	def hdx(self,hdx):
		try :
			if not isinstance(hdx,bool):
				raise TypeError("hdx must be set to bool value")
			self._hdx = hdx
		except Exception as e :
			raise e


	'''
	get connection_chaining
	'''
	@property
	def connection_chaining(self) :
		try:
			return self._connection_chaining
		except Exception as e :
			raise e
	'''
	set connection_chaining
	'''
	@connection_chaining.setter
	def connection_chaining(self,connection_chaining):
		try :
			if not isinstance(connection_chaining,bool):
				raise TypeError("connection_chaining must be set to bool value")
			self._connection_chaining = connection_chaining
		except Exception as e :
			raise e


	'''
	get BR IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set BR IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get BR IP Address
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set BR IP Address
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
	get appflowfeature
	'''
	@property
	def appflowfeature(self) :
		try:
			return self._appflowfeature
		except Exception as e :
			raise e
	'''
	set appflowfeature
	'''
	@appflowfeature.setter
	def appflowfeature(self,appflowfeature):
		try :
			if not isinstance(appflowfeature,bool):
				raise TypeError("appflowfeature must be set to bool value")
			self._appflowfeature = appflowfeature
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdwanvw_appflowconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdwanvw_appflowconfig_obj = sdwanvw_appflowconfig()
			option_ = options()
			option_._filter=filter_
			return sdwanvw_appflowconfig_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdwanvw_appflowconfig resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdwanvw_appflowconfig_obj = sdwanvw_appflowconfig()
			option_ = options()
			option_._count=True
			response = sdwanvw_appflowconfig_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdwanvw_appflowconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdwanvw_appflowconfig_obj = sdwanvw_appflowconfig()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdwanvw_appflowconfig_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdwanvw_appflowconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdwanvw_appflowconfig
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdwanvw_appflowconfig_responses, response, "sdwanvw_appflowconfig_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdwanvw_appflowconfig_response_array
				i=0
				error = [sdwanvw_appflowconfig() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdwanvw_appflowconfig_response_array
			i=0
			sdwanvw_appflowconfig_objs = [sdwanvw_appflowconfig() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdwanvw_appflowconfig'):
					for props in obj._sdwanvw_appflowconfig:
						result = service.payload_formatter.string_to_bulk_resource(sdwanvw_appflowconfig_response,self.__class__.__name__,props)
						sdwanvw_appflowconfig_objs[i] = result.sdwanvw_appflowconfig
						i=i+1
			return sdwanvw_appflowconfig_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdwanvw_appflowconfig,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdwanvw_appflowconfig_response(base_response):
	def __init__(self,length=1) :
		self.sdwanvw_appflowconfig= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdwanvw_appflowconfig= [ sdwanvw_appflowconfig() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdwanvw_appflowconfig_responses(base_response):
	def __init__(self,length=1) :
		self.sdwanvw_appflowconfig_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdwanvw_appflowconfig_response_array = [ sdwanvw_appflowconfig() for _ in range(length)]
