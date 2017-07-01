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
Configuration for NS GSLB Services Information resource
'''

class ns_gslbservice(base_resource):
	_svc_state= ""
	_svc_port= ""
	_hostname= ""
	_svc_type= ""
	_poll_time= ""
	_display_name= ""
	_ns_ip_address= ""
	_svc_ip_address= ""
	_partition_name= ""
	_svc_state_timestamp= ""
	_svc_name= ""
	_id= ""
	_save_config= ""
	_vsvr_name= ""
	_delay= ""
	_graceful= ""
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
			return "ns_gslbservice"
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
			return "ns_gslbservices"
		except Exception as e :
			raise e



	'''
	get Service State
	'''
	@property
	def svc_state(self) :
		try:
			return self._svc_state
		except Exception as e :
			raise e


	'''
	get Service Port
	'''
	@property
	def svc_port(self) :
		try:
			return self._svc_port
		except Exception as e :
			raise e
	'''
	set Service Port
	'''
	@svc_port.setter
	def svc_port(self,svc_port):
		try :
			if not isinstance(svc_port,int):
				raise TypeError("svc_port must be set to int value")
			self._svc_port = svc_port
		except Exception as e :
			raise e


	'''
	get Hostname of the managed device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of the managed device
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e


	'''
	get Service Type
	'''
	@property
	def svc_type(self) :
		try:
			return self._svc_type
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
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
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
	get Service IP Address
	'''
	@property
	def svc_ip_address(self) :
		try:
			return self._svc_ip_address
		except Exception as e :
			raise e
	'''
	set Service IP Address
	'''
	@svc_ip_address.setter
	def svc_ip_address(self,svc_ip_address):
		try :
			if not isinstance(svc_ip_address,str):
				raise TypeError("svc_ip_address must be set to str value")
			self._svc_ip_address = svc_ip_address
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
	get Service Last Statechange Time Stamp
	'''
	@property
	def svc_state_timestamp(self) :
		try:
			return self._svc_state_timestamp
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def svc_name(self) :
		try:
			return self._svc_name
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@svc_name.setter
	def svc_name(self,svc_name):
		try :
			if not isinstance(svc_name,str):
				raise TypeError("svc_name must be set to str value")
			self._svc_name = svc_name
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
	Save configuration after gslb service enable/disable
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	Save configuration after gslb service enable/disable
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
	Vserver Name
	'''
	@property
	def vsvr_name(self):
		try:
			return self._vsvr_name
		except Exception as e :
			raise e
	'''
	Vserver Name
	'''
	@vsvr_name.setter
	def vsvr_name(self,vsvr_name):
		try :
			if not isinstance(vsvr_name,str):
				raise TypeError("vsvr_name must be set to str value")
			self._vsvr_name = vsvr_name
		except Exception as e :
			raise e

	'''
	Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service
	'''
	@property
	def delay(self):
		try:
			return self._delay
		except Exception as e :
			raise e
	'''
	Time, in seconds, allocated to the NetScaler appliance for a graceful shutdown of the service
	'''
	@delay.setter
	def delay(self,delay):
		try :
			if not isinstance(delay,float):
				raise TypeError("delay must be set to float value")
			self._delay = delay
		except Exception as e :
			raise e

	'''
	Graceful shutdown of Service.
	'''
	@property
	def graceful(self):
		try:
			return self._graceful
		except Exception as e :
			raise e
	'''
	Graceful shutdown of Service.
	'''
	@graceful.setter
	def graceful(self,graceful):
		try :
			if not isinstance(graceful,bool):
				raise TypeError("graceful must be set to bool value")
			self._graceful = graceful
		except Exception as e :
			raise e

	'''
	Use this operation to enable the GSLB Service.
	'''
	@classmethod
	def enable(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"enable")
		except Exception as e :
			raise e

	'''
	Use this operation to get GSLB Service Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_gslbservice_obj=ns_gslbservice()
				response = ns_gslbservice_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to disable the GSLB Service.
	'''
	@classmethod
	def disable(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"disable")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_gslbservice resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_gslbservice_obj = ns_gslbservice()
			option_ = options()
			option_._filter=filter_
			return ns_gslbservice_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_gslbservice resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_gslbservice_obj = ns_gslbservice()
			option_ = options()
			option_._count=True
			response = ns_gslbservice_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_gslbservice resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_gslbservice_obj = ns_gslbservice()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_gslbservice_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_gslbservice_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_gslbservice
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_gslbservice_responses, response, "ns_gslbservice_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_gslbservice_response_array
				i=0
				error = [ns_gslbservice() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_gslbservice_response_array
			i=0
			ns_gslbservice_objs = [ns_gslbservice() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_gslbservice'):
					for props in obj._ns_gslbservice:
						result = service.payload_formatter.string_to_bulk_resource(ns_gslbservice_response,self.__class__.__name__,props)
						ns_gslbservice_objs[i] = result.ns_gslbservice
						i=i+1
			return ns_gslbservice_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_gslbservice,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_gslbservice_response(base_response):
	def __init__(self,length=1) :
		self.ns_gslbservice= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_gslbservice= [ ns_gslbservice() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_gslbservice_responses(base_response):
	def __init__(self,length=1) :
		self.ns_gslbservice_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_gslbservice_response_array = [ ns_gslbservice() for _ in range(length)]
