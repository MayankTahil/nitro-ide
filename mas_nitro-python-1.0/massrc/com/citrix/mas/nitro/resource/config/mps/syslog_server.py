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
Configuration for Syslog Server resource
'''

class syslog_server(base_resource):
	_log_level_all= ""
	_name= ""
	_log_level_warning= ""
	_log_level_error= ""
	_port= ""
	_log_levels= ""
	_log_level_info= ""
	_log_level_critical= ""
	_ip_address= ""
	_log_level_none= ""
	_address_type= ""
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
			return "syslog_server"
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
			return "syslog_servers"
		except Exception as e :
			raise e



	'''
	get Send logs of all levels to this syslog server
	'''
	@property
	def log_level_all(self) :
		try:
			return self._log_level_all
		except Exception as e :
			raise e
	'''
	set Send logs of all levels to this syslog server
	'''
	@log_level_all.setter
	def log_level_all(self,log_level_all):
		try :
			if not isinstance(log_level_all,bool):
				raise TypeError("log_level_all must be set to bool value")
			self._log_level_all = log_level_all
		except Exception as e :
			raise e


	'''
	get Syslog server name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Syslog server name
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
	get Send logs of level warning to this syslog server
	'''
	@property
	def log_level_warning(self) :
		try:
			return self._log_level_warning
		except Exception as e :
			raise e
	'''
	set Send logs of level warning to this syslog server
	'''
	@log_level_warning.setter
	def log_level_warning(self,log_level_warning):
		try :
			if not isinstance(log_level_warning,bool):
				raise TypeError("log_level_warning must be set to bool value")
			self._log_level_warning = log_level_warning
		except Exception as e :
			raise e


	'''
	get Send logs of level error to this syslog server
	'''
	@property
	def log_level_error(self) :
		try:
			return self._log_level_error
		except Exception as e :
			raise e
	'''
	set Send logs of level error to this syslog server
	'''
	@log_level_error.setter
	def log_level_error(self,log_level_error):
		try :
			if not isinstance(log_level_error,bool):
				raise TypeError("log_level_error must be set to bool value")
			self._log_level_error = log_level_error
		except Exception as e :
			raise e


	'''
	get Syslog server port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Syslog server port
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get Set of all log levels at which messages are sent to this syslog server
	'''
	@property
	def log_levels(self) :
		try:
			return self._log_levels
		except Exception as e :
			raise e


	'''
	get Send logs of level info to this syslog server
	'''
	@property
	def log_level_info(self) :
		try:
			return self._log_level_info
		except Exception as e :
			raise e
	'''
	set Send logs of level info to this syslog server
	'''
	@log_level_info.setter
	def log_level_info(self,log_level_info):
		try :
			if not isinstance(log_level_info,bool):
				raise TypeError("log_level_info must be set to bool value")
			self._log_level_info = log_level_info
		except Exception as e :
			raise e


	'''
	get Send logs of level critical to this syslog server
	'''
	@property
	def log_level_critical(self) :
		try:
			return self._log_level_critical
		except Exception as e :
			raise e
	'''
	set Send logs of level critical to this syslog server
	'''
	@log_level_critical.setter
	def log_level_critical(self,log_level_critical):
		try :
			if not isinstance(log_level_critical,bool):
				raise TypeError("log_level_critical must be set to bool value")
			self._log_level_critical = log_level_critical
		except Exception as e :
			raise e


	'''
	get Syslog server IP address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Syslog server IP address
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
	get Send no logs to this syslog server
	'''
	@property
	def log_level_none(self) :
		try:
			return self._log_level_none
		except Exception as e :
			raise e
	'''
	set Send no logs to this syslog server
	'''
	@log_level_none.setter
	def log_level_none(self,log_level_none):
		try :
			if not isinstance(log_level_none,bool):
				raise TypeError("log_level_none must be set to bool value")
			self._log_level_none = log_level_none
		except Exception as e :
			raise e


	'''
	get Configuration Type. Values: 0: IPv4, 1: IPv6
	'''
	@property
	def address_type(self) :
		try:
			return self._address_type
		except Exception as e :
			raise e

	'''
	Use this operation to add a syslog server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				syslog_server_obj= syslog_server()
				return cls.perform_operation_bulk_request(service,"add", resource,syslog_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a syslog server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					syslog_server_obj=syslog_server()
					return cls.delete_bulk_request(client,resource,syslog_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get all the syslog servers.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				syslog_server_obj=syslog_server()
				response = syslog_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a syslog server.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				syslog_server_obj=syslog_server()
				return cls.update_bulk_request(client,resource,syslog_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_server_obj = syslog_server()
			option_ = options()
			option_._filter=filter_
			return syslog_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_server_obj = syslog_server()
			option_ = options()
			option_._count=True
			response = syslog_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_server_obj = syslog_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_server_responses, response, "syslog_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_server_response_array
				i=0
				error = [syslog_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_server_response_array
			i=0
			syslog_server_objs = [syslog_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_server'):
					for props in obj._syslog_server:
						result = service.payload_formatter.string_to_bulk_resource(syslog_server_response,self.__class__.__name__,props)
						syslog_server_objs[i] = result.syslog_server
						i=i+1
			return syslog_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_server_response(base_response):
	def __init__(self,length=1) :
		self.syslog_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_server= [ syslog_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_server_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_server_response_array = [ syslog_server() for _ in range(length)]
