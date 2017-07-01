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
Configuration for NS IP on NetScaler License Available resource
'''

class ns_vserver_license(base_resource):
	_license_status= ""
	_name= ""
	_type= ""
	_ip_address= ""
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
			return "ns_vserver_license"
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
			return "ns_vserver_licenses"
		except Exception as e :
			raise e



	'''
	get true, if license is available
	'''
	@property
	def license_status(self) :
		try:
			return self._license_status
		except Exception as e :
			raise e
	'''
	set true, if license is available
	'''
	@license_status.setter
	def license_status(self,license_status):
		try :
			if not isinstance(license_status,bool):
				raise TypeError("license_status must be set to bool value")
			self._license_status = license_status
		except Exception as e :
			raise e


	'''
	get NS vserver 
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set NS vserver 
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
	get vserver type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set vserver type
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
	get ip_address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set ip_address
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
	Use this API to fetch filtered set of ns_vserver_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_vserver_license_obj = ns_vserver_license()
			option_ = options()
			option_._filter=filter_
			return ns_vserver_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_vserver_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_vserver_license_obj = ns_vserver_license()
			option_ = options()
			option_._count=True
			response = ns_vserver_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_vserver_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_vserver_license_obj = ns_vserver_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_vserver_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_vserver_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_vserver_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_vserver_license_responses, response, "ns_vserver_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_vserver_license_response_array
				i=0
				error = [ns_vserver_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_vserver_license_response_array
			i=0
			ns_vserver_license_objs = [ns_vserver_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_vserver_license'):
					for props in obj._ns_vserver_license:
						result = service.payload_formatter.string_to_bulk_resource(ns_vserver_license_response,self.__class__.__name__,props)
						ns_vserver_license_objs[i] = result.ns_vserver_license
						i=i+1
			return ns_vserver_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_vserver_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_vserver_license_response(base_response):
	def __init__(self,length=1) :
		self.ns_vserver_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_vserver_license= [ ns_vserver_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_vserver_license_responses(base_response):
	def __init__(self,length=1) :
		self.ns_vserver_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_vserver_license_response_array = [ ns_vserver_license() for _ in range(length)]
