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
Configuration for web detail data collection config resource
'''

class web_detail_data_collection_config(base_resource):
	_server_response_time= ""
	_network_latency_server_side= ""
	_application_response_time= ""
	_name= ""
	_http_rsp_status_2xx_enabled= ""
	_network_latency_client_side= ""
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
			return "web_detail_data_collection_config"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "web_detail_data_collection_configs"
		except Exception as e :
			raise e



	'''
	get Server Response Time should be greate than or equal to value.(millisec)
	'''
	@property
	def server_response_time(self) :
		try:
			return self._server_response_time
		except Exception as e :
			raise e
	'''
	set Server Response Time should be greate than or equal to value.(millisec)
	'''
	@server_response_time.setter
	def server_response_time(self,server_response_time):
		try :
			if not isinstance(server_response_time,long):
				raise TypeError("server_response_time must be set to long value")
			self._server_response_time = server_response_time
		except Exception as e :
			raise e


	'''
	get Network Latency Client server Time should be greate than or equal to value.(millisec)
	'''
	@property
	def network_latency_server_side(self) :
		try:
			return self._network_latency_server_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client server Time should be greate than or equal to value.(millisec)
	'''
	@network_latency_server_side.setter
	def network_latency_server_side(self,network_latency_server_side):
		try :
			if not isinstance(network_latency_server_side,long):
				raise TypeError("network_latency_server_side must be set to long value")
			self._network_latency_server_side = network_latency_server_side
		except Exception as e :
			raise e


	'''
	get Application Response Time should be greater than or equal to value. (millisec)
	'''
	@property
	def application_response_time(self) :
		try:
			return self._application_response_time
		except Exception as e :
			raise e
	'''
	set Application Response Time should be greater than or equal to value. (millisec)
	'''
	@application_response_time.setter
	def application_response_time(self,application_response_time):
		try :
			if not isinstance(application_response_time,long):
				raise TypeError("application_response_time must be set to long value")
			self._application_response_time = application_response_time
		except Exception as e :
			raise e


	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get HTTP Response Status Method collect enabled for 2xx response.
	'''
	@property
	def http_rsp_status_2xx_enabled(self) :
		try:
			return self._http_rsp_status_2xx_enabled
		except Exception as e :
			raise e
	'''
	set HTTP Response Status Method collect enabled for 2xx response.
	'''
	@http_rsp_status_2xx_enabled.setter
	def http_rsp_status_2xx_enabled(self,http_rsp_status_2xx_enabled):
		try :
			if not isinstance(http_rsp_status_2xx_enabled,int):
				raise TypeError("http_rsp_status_2xx_enabled must be set to int value")
			self._http_rsp_status_2xx_enabled = http_rsp_status_2xx_enabled
		except Exception as e :
			raise e


	'''
	get Network Latency Client side Time should be greate than value or equal to .(millisec)
	'''
	@property
	def network_latency_client_side(self) :
		try:
			return self._network_latency_client_side
		except Exception as e :
			raise e
	'''
	set Network Latency Client side Time should be greate than value or equal to .(millisec)
	'''
	@network_latency_client_side.setter
	def network_latency_client_side(self,network_latency_client_side):
		try :
			if not isinstance(network_latency_client_side,long):
				raise TypeError("network_latency_client_side must be set to long value")
			self._network_latency_client_side = network_latency_client_side
		except Exception as e :
			raise e

	'''
	Use this operation to get configured value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				web_detail_data_collection_config_obj=web_detail_data_collection_config()
				response = web_detail_data_collection_config_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify parameter value.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				web_detail_data_collection_config_obj=web_detail_data_collection_config()
				return cls.update_bulk_request(client,resource,web_detail_data_collection_config_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of web_detail_data_collection_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			web_detail_data_collection_config_obj = web_detail_data_collection_config()
			option_ = options()
			option_._filter=filter_
			return web_detail_data_collection_config_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the web_detail_data_collection_config resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			web_detail_data_collection_config_obj = web_detail_data_collection_config()
			option_ = options()
			option_._count=True
			response = web_detail_data_collection_config_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of web_detail_data_collection_config resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			web_detail_data_collection_config_obj = web_detail_data_collection_config()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = web_detail_data_collection_config_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(web_detail_data_collection_config_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.web_detail_data_collection_config
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(web_detail_data_collection_config_responses, response, "web_detail_data_collection_config_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.web_detail_data_collection_config_response_array
				i=0
				error = [web_detail_data_collection_config() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.web_detail_data_collection_config_response_array
			i=0
			web_detail_data_collection_config_objs = [web_detail_data_collection_config() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_web_detail_data_collection_config'):
					for props in obj._web_detail_data_collection_config:
						result = service.payload_formatter.string_to_bulk_resource(web_detail_data_collection_config_response,self.__class__.__name__,props)
						web_detail_data_collection_config_objs[i] = result.web_detail_data_collection_config
						i=i+1
			return web_detail_data_collection_config_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(web_detail_data_collection_config,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class web_detail_data_collection_config_response(base_response):
	def __init__(self,length=1) :
		self.web_detail_data_collection_config= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.web_detail_data_collection_config= [ web_detail_data_collection_config() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class web_detail_data_collection_config_responses(base_response):
	def __init__(self,length=1) :
		self.web_detail_data_collection_config_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.web_detail_data_collection_config_response_array = [ web_detail_data_collection_config() for _ in range(length)]
