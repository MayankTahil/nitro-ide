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
Configuration for NetScaler Service Group Member Bindings resource
'''

class ns_servicegroupmember_binding(base_resource):
	_ip= ""
	_hostname= ""
	_state= ""
	_ns_ip_address= ""
	_customserverid= ""
	_weight= ""
	_id= ""
	_servicegroupname= ""
	_svrstate= ""
	_poll_time= ""
	_port= ""
	_display_name= ""
	_serverid= ""
	_servername= ""
	_comment= ""
	_partition_name= ""
	_hash_id= ""
	_save_config= ""
	_delay= ""
	_svc_grp_id= ""
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
			return "ns_servicegroupmember_binding"
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
			return "ns_servicegroupmember_bindings"
		except Exception as e :
			raise e



	'''
	get Server IP
	'''
	@property
	def ip(self) :
		try:
			return self._ip
		except Exception as e :
			raise e
	'''
	set Server IP
	'''
	@ip.setter
	def ip(self,ip):
		try :
			if not isinstance(ip,str):
				raise TypeError("ip must be set to str value")
			self._ip = ip
		except Exception as e :
			raise e


	'''
	get Host name of the Managed device 
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get state
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set state
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
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
	get CustomServerID
	'''
	@property
	def customserverid(self) :
		try:
			return self._customserverid
		except Exception as e :
			raise e
	'''
	set CustomServerID
	'''
	@customserverid.setter
	def customserverid(self,customserverid):
		try :
			if not isinstance(customserverid,str):
				raise TypeError("customserverid must be set to str value")
			self._customserverid = customserverid
		except Exception as e :
			raise e


	'''
	get Weight
	'''
	@property
	def weight(self) :
		try:
			return self._weight
		except Exception as e :
			raise e
	'''
	set Weight
	'''
	@weight.setter
	def weight(self,weight):
		try :
			if not isinstance(weight,str):
				raise TypeError("weight must be set to str value")
			self._weight = weight
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
	get Service Group Name
	'''
	@property
	def servicegroupname(self) :
		try:
			return self._servicegroupname
		except Exception as e :
			raise e
	'''
	set Service Group Name
	'''
	@servicegroupname.setter
	def servicegroupname(self,servicegroupname):
		try :
			if not isinstance(servicegroupname,str):
				raise TypeError("servicegroupname must be set to str value")
			self._servicegroupname = servicegroupname
		except Exception as e :
			raise e


	'''
	get Server State
	'''
	@property
	def svrstate(self) :
		try:
			return self._svrstate
		except Exception as e :
			raise e
	'''
	set Server State
	'''
	@svrstate.setter
	def svrstate(self,svrstate):
		try :
			if not isinstance(svrstate,str):
				raise TypeError("svrstate must be set to str value")
			self._svrstate = svrstate
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
	get Server Port
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Server Port
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
	get Display Name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get ServerID
	'''
	@property
	def serverid(self) :
		try:
			return self._serverid
		except Exception as e :
			raise e
	'''
	set ServerID
	'''
	@serverid.setter
	def serverid(self,serverid):
		try :
			if not isinstance(serverid,str):
				raise TypeError("serverid must be set to str value")
			self._serverid = serverid
		except Exception as e :
			raise e


	'''
	get ServerName
	'''
	@property
	def servername(self) :
		try:
			return self._servername
		except Exception as e :
			raise e
	'''
	set ServerName
	'''
	@servername.setter
	def servername(self,servername):
		try :
			if not isinstance(servername,str):
				raise TypeError("servername must be set to str value")
			self._servername = servername
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
	get Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e


	'''
	get Hash Id
	'''
	@property
	def hash_id(self) :
		try:
			return self._hash_id
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
	Service Group ID
	'''
	@property
	def svc_grp_id(self):
		try:
			return self._svc_grp_id
		except Exception as e :
			raise e
	'''
	Service Group ID
	'''
	@svc_grp_id.setter
	def svc_grp_id(self,svc_grp_id):
		try :
			if not isinstance(svc_grp_id,str):
				raise TypeError("svc_grp_id must be set to str value")
			self._svc_grp_id = svc_grp_id
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
	Use this operation to enable the Service Member Group.
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
	Use this operation to get Service Member Group Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_servicegroupmember_binding_obj=ns_servicegroupmember_binding()
				response = ns_servicegroupmember_binding_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to disable the Service Member Group.
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
	Use this API to fetch filtered set of ns_servicegroupmember_binding resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_servicegroupmember_binding_obj = ns_servicegroupmember_binding()
			option_ = options()
			option_._filter=filter_
			return ns_servicegroupmember_binding_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_servicegroupmember_binding resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_servicegroupmember_binding_obj = ns_servicegroupmember_binding()
			option_ = options()
			option_._count=True
			response = ns_servicegroupmember_binding_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_servicegroupmember_binding resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_servicegroupmember_binding_obj = ns_servicegroupmember_binding()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_servicegroupmember_binding_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_servicegroupmember_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_servicegroupmember_binding
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_servicegroupmember_binding_responses, response, "ns_servicegroupmember_binding_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_servicegroupmember_binding_response_array
				i=0
				error = [ns_servicegroupmember_binding() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_servicegroupmember_binding_response_array
			i=0
			ns_servicegroupmember_binding_objs = [ns_servicegroupmember_binding() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_servicegroupmember_binding'):
					for props in obj._ns_servicegroupmember_binding:
						result = service.payload_formatter.string_to_bulk_resource(ns_servicegroupmember_binding_response,self.__class__.__name__,props)
						ns_servicegroupmember_binding_objs[i] = result.ns_servicegroupmember_binding
						i=i+1
			return ns_servicegroupmember_binding_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_servicegroupmember_binding,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_servicegroupmember_binding_response(base_response):
	def __init__(self,length=1) :
		self.ns_servicegroupmember_binding= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_servicegroupmember_binding= [ ns_servicegroupmember_binding() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_servicegroupmember_binding_responses(base_response):
	def __init__(self,length=1) :
		self.ns_servicegroupmember_binding_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_servicegroupmember_binding_response_array = [ ns_servicegroupmember_binding() for _ in range(length)]
