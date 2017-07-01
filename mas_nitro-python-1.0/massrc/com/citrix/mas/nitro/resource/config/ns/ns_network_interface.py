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
Configuration for NS Network Interfaces resource
'''

class ns_network_interface(base_resource):
	_partition_name= ""
	_devicename= ""
	_poll_time= ""
	_id= ""
	_state= ""
	_ns_ip_address= ""
	_hostname= ""
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
			return "ns_network_interface"
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
			return "ns_network_interfaces"
		except Exception as e :
			raise e



	'''
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Device/Interface Name
	'''
	@property
	def devicename(self) :
		try:
			return self._devicename
		except Exception as e :
			raise e
	'''
	set Device/Interface Name
	'''
	@devicename.setter
	def devicename(self,devicename):
		try :
			if not isinstance(devicename,str):
				raise TypeError("devicename must be set to str value")
			self._devicename = devicename
		except Exception as e :
			raise e


	'''
	get Last Polling Time
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
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
	get State Enabled|Disabled
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e


	'''
	get NS IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NS IP Address
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
	Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def hostname(self):
		try:
			return self._hostname
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler network interfaces.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_network_interface_obj=ns_network_interface()
				response = ns_network_interface_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_network_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_network_interface_obj = ns_network_interface()
			option_ = options()
			option_._filter=filter_
			return ns_network_interface_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_network_interface resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_network_interface_obj = ns_network_interface()
			option_ = options()
			option_._count=True
			response = ns_network_interface_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_network_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_network_interface_obj = ns_network_interface()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_network_interface_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_network_interface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_network_interface
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_network_interface_responses, response, "ns_network_interface_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_network_interface_response_array
				i=0
				error = [ns_network_interface() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_network_interface_response_array
			i=0
			ns_network_interface_objs = [ns_network_interface() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_network_interface'):
					for props in obj._ns_network_interface:
						result = service.payload_formatter.string_to_bulk_resource(ns_network_interface_response,self.__class__.__name__,props)
						ns_network_interface_objs[i] = result.ns_network_interface
						i=i+1
			return ns_network_interface_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_network_interface,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_network_interface_response(base_response):
	def __init__(self,length=1) :
		self.ns_network_interface= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_network_interface= [ ns_network_interface() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_network_interface_responses(base_response):
	def __init__(self,length=1) :
		self.ns_network_interface_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_network_interface_response_array = [ ns_network_interface() for _ in range(length)]
