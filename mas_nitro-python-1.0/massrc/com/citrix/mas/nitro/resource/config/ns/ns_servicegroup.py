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
Configuration for NS Service Group Information resource
'''

class ns_servicegroup(base_resource):
	_svrstate= ""
	_hostname= ""
	_svc_grp_state_timestamp= ""
	_svc_grp_mem_port= ""
	_svc_grp_name= ""
	_poll_time= ""
	_display_name= ""
	_svc_grp_effective_state= ""
	_ns_ip_address= ""
	_partition_name= ""
	_comment= ""
	_svc_grp_mem_ip_address= ""
	_svc_grp_mem_state= ""
	_id= ""
	_svc_grp_mem_type= ""
	_save_config= ""
	_lb_id= ""
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
			return "ns_servicegroup"
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
			return "ns_servicegroups"
		except Exception as e :
			raise e



	'''
	get Service State
	'''
	@property
	def svrstate(self) :
		try:
			return self._svrstate
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
	get Service Group Last State Change Time
	'''
	@property
	def svc_grp_state_timestamp(self) :
		try:
			return self._svc_grp_state_timestamp
		except Exception as e :
			raise e


	'''
	get Service Group Member Port
	'''
	@property
	def svc_grp_mem_port(self) :
		try:
			return self._svc_grp_mem_port
		except Exception as e :
			raise e
	'''
	set Service Group Member Port
	'''
	@svc_grp_mem_port.setter
	def svc_grp_mem_port(self,svc_grp_mem_port):
		try :
			if not isinstance(svc_grp_mem_port,int):
				raise TypeError("svc_grp_mem_port must be set to int value")
			self._svc_grp_mem_port = svc_grp_mem_port
		except Exception as e :
			raise e


	'''
	get Service Group Name
	'''
	@property
	def svc_grp_name(self) :
		try:
			return self._svc_grp_name
		except Exception as e :
			raise e
	'''
	set Service Group Name
	'''
	@svc_grp_name.setter
	def svc_grp_name(self,svc_grp_name):
		try :
			if not isinstance(svc_grp_name,str):
				raise TypeError("svc_grp_name must be set to str value")
			self._svc_grp_name = svc_grp_name
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
	get Service Group Effective State
	'''
	@property
	def svc_grp_effective_state(self) :
		try:
			return self._svc_grp_effective_state
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
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Comment
	'''
	@property
	def comment(self) :
		try:
			return self._comment
		except Exception as e :
			raise e


	'''
	get Service Group Member IP Address
	'''
	@property
	def svc_grp_mem_ip_address(self) :
		try:
			return self._svc_grp_mem_ip_address
		except Exception as e :
			raise e
	'''
	set Service Group Member IP Address
	'''
	@svc_grp_mem_ip_address.setter
	def svc_grp_mem_ip_address(self,svc_grp_mem_ip_address):
		try :
			if not isinstance(svc_grp_mem_ip_address,str):
				raise TypeError("svc_grp_mem_ip_address must be set to str value")
			self._svc_grp_mem_ip_address = svc_grp_mem_ip_address
		except Exception as e :
			raise e


	'''
	get Service Group Member State
	'''
	@property
	def svc_grp_mem_state(self) :
		try:
			return self._svc_grp_mem_state
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
	get Service Group Member Type
	'''
	@property
	def svc_grp_mem_type(self) :
		try:
			return self._svc_grp_mem_type
		except Exception as e :
			raise e

	'''
	Save configuration after service enable/disable
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	Save configuration after service enable/disable
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
	LB ID
	'''
	@property
	def lb_id(self):
		try:
			return self._lb_id
		except Exception as e :
			raise e
	'''
	LB ID
	'''
	@lb_id.setter
	def lb_id(self,lb_id):
		try :
			if not isinstance(lb_id,str):
				raise TypeError("lb_id must be set to str value")
			self._lb_id = lb_id
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
	Use this operation to enable the service group.
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
	Use this operation to get Service Group Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_servicegroup_obj=ns_servicegroup()
				response = ns_servicegroup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to disable the service group.
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
	Use this API to fetch filtered set of ns_servicegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_servicegroup_obj = ns_servicegroup()
			option_ = options()
			option_._filter=filter_
			return ns_servicegroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_servicegroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_servicegroup_obj = ns_servicegroup()
			option_ = options()
			option_._count=True
			response = ns_servicegroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_servicegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_servicegroup_obj = ns_servicegroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_servicegroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_servicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_servicegroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_servicegroup_responses, response, "ns_servicegroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_servicegroup_response_array
				i=0
				error = [ns_servicegroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_servicegroup_response_array
			i=0
			ns_servicegroup_objs = [ns_servicegroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_servicegroup'):
					for props in obj._ns_servicegroup:
						result = service.payload_formatter.string_to_bulk_resource(ns_servicegroup_response,self.__class__.__name__,props)
						ns_servicegroup_objs[i] = result.ns_servicegroup
						i=i+1
			return ns_servicegroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_servicegroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_servicegroup_response(base_response):
	def __init__(self,length=1) :
		self.ns_servicegroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_servicegroup= [ ns_servicegroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_servicegroup_responses(base_response):
	def __init__(self,length=1) :
		self.ns_servicegroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_servicegroup_response_array = [ ns_servicegroup() for _ in range(length)]
