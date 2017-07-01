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
Configuration for License server information resource
'''

class license_server_info(base_resource):
	_license_port= ""
	_node_id= ""
	_vendor_daemon_port= ""
	_id= ""
	_proxy_port= ""
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
			return "license_server_info"
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
			return "license_server_infos"
		except Exception as e :
			raise e



	'''
	get license port
	'''
	@property
	def license_port(self) :
		try:
			return self._license_port
		except Exception as e :
			raise e
	'''
	set license port
	'''
	@license_port.setter
	def license_port(self,license_port):
		try :
			if not isinstance(license_port,int):
				raise TypeError("license_port must be set to int value")
			self._license_port = license_port
		except Exception as e :
			raise e


	'''
	get Node identification of a license server in multi-node
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Node identification of a license server in multi-node
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e


	'''
	get license vendor daemon port
	'''
	@property
	def vendor_daemon_port(self) :
		try:
			return self._vendor_daemon_port
		except Exception as e :
			raise e
	'''
	set license vendor daemon port
	'''
	@vendor_daemon_port.setter
	def vendor_daemon_port(self,vendor_daemon_port):
		try :
			if not isinstance(vendor_daemon_port,int):
				raise TypeError("vendor_daemon_port must be set to int value")
			self._vendor_daemon_port = vendor_daemon_port
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Proxy server port for jazz license
	'''
	@property
	def proxy_port(self) :
		try:
			return self._proxy_port
		except Exception as e :
			raise e
	'''
	set Proxy server port for jazz license
	'''
	@proxy_port.setter
	def proxy_port(self,proxy_port):
		try :
			if not isinstance(proxy_port,int):
				raise TypeError("proxy_port must be set to int value")
			self._proxy_port = proxy_port
		except Exception as e :
			raise e

	'''
	Use this operation to get License server details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_server_info_obj=license_server_info()
				response = license_server_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_server_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_server_info_obj = license_server_info()
			option_ = options()
			option_._filter=filter_
			return license_server_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_server_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_server_info_obj = license_server_info()
			option_ = options()
			option_._count=True
			response = license_server_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_server_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_server_info_obj = license_server_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_server_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_server_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_server_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_server_info_responses, response, "license_server_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_server_info_response_array
				i=0
				error = [license_server_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_server_info_response_array
			i=0
			license_server_info_objs = [license_server_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_server_info'):
					for props in obj._license_server_info:
						result = service.payload_formatter.string_to_bulk_resource(license_server_info_response,self.__class__.__name__,props)
						license_server_info_objs[i] = result.license_server_info
						i=i+1
			return license_server_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_server_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_server_info_response(base_response):
	def __init__(self,length=1) :
		self.license_server_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_server_info= [ license_server_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_server_info_responses(base_response):
	def __init__(self,length=1) :
		self.license_server_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_server_info_response_array = [ license_server_info() for _ in range(length)]
