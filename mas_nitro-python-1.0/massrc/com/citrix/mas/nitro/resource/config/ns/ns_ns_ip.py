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
Configuration for NS IP on NetScaler resource
'''

class ns_ns_ip(base_resource):
	_save_config= ""
	_type= ""
	_netmask= ""
	_ipaddress= ""
	_ns_ip_address= ""
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
			return "ns_ns_ip"
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
			return "ns_ns_ips"
		except Exception as e :
			raise e



	'''
	get true, if save config is required
	'''
	@property
	def save_config(self) :
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	set true, if save config is required
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e


	'''
	get Type of IP Address, Possible Values: SNIP
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of IP Address, Possible Values: SNIP
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get netmask
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set netmask
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get NS ipaddress that needs to be created
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set NS ipaddress that needs to be created
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress):
		try :
			if not isinstance(ipaddress,str):
				raise TypeError("ipaddress must be set to str value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address where NSIP needs to be created
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address where NSIP needs to be created
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to add ns ip on NS Instance.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_ns_ip_obj= ns_ns_ip()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_ns_ip_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ns_ip resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ns_ip_obj = ns_ns_ip()
			option_ = options()
			option_._filter=filter_
			return ns_ns_ip_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ns_ip resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ns_ip_obj = ns_ns_ip()
			option_ = options()
			option_._count=True
			response = ns_ns_ip_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ns_ip resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ns_ip_obj = ns_ns_ip()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ns_ip_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ns_ip_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ns_ip
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ns_ip_responses, response, "ns_ns_ip_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ns_ip_response_array
				i=0
				error = [ns_ns_ip() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ns_ip_response_array
			i=0
			ns_ns_ip_objs = [ns_ns_ip() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ns_ip'):
					for props in obj._ns_ns_ip:
						result = service.payload_formatter.string_to_bulk_resource(ns_ns_ip_response,self.__class__.__name__,props)
						ns_ns_ip_objs[i] = result.ns_ns_ip
						i=i+1
			return ns_ns_ip_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ns_ip,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ns_ip_response(base_response):
	def __init__(self,length=1) :
		self.ns_ns_ip= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ns_ip= [ ns_ns_ip() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ns_ip_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ns_ip_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ns_ip_response_array = [ ns_ns_ip() for _ in range(length)]
