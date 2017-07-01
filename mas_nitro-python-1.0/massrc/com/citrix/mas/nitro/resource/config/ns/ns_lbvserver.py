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
Configuration for NS Lbvserver Information resource
'''

class ns_lbvserver(base_resource):
	_user_managed= ""
	_curclntconnections= ""
	_vsvr_state= ""
	_vsvr_state_timestamp= ""
	_hostname= ""
	_state= ""
	_ns_ip_address= ""
	_lbmethod= ""
	_activeservices= ""
	_vsvr_type= ""
	_id= ""
	_totalservices= ""
	_vsvr_port= ""
	_vsvr_health= ""
	_name= ""
	_cursrvrconnections= ""
	_poll_time= ""
	_display_name= ""
	_managed= ""
	_persistencetype= ""
	_comment= ""
	_partition_name= ""
	_vsvr_ip_address= ""
	_throughput= ""
	_save_config= ""
	_svc_name= ""
	_svc_id= ""
	_svc_grp_name= ""
	_svc_grp_id= ""
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
			return "ns_lbvserver"
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
			return "ns_lbvservers"
		except Exception as e :
			raise e



	'''
	get User Managed Idenfication
	'''
	@property
	def user_managed(self) :
		try:
			return self._user_managed
		except Exception as e :
			raise e
	'''
	set User Managed Idenfication
	'''
	@user_managed.setter
	def user_managed(self,user_managed):
		try :
			if not isinstance(user_managed,bool):
				raise TypeError("user_managed must be set to bool value")
			self._user_managed = user_managed
		except Exception as e :
			raise e


	'''
	get curclntconnections Value
	'''
	@property
	def curclntconnections(self) :
		try:
			return self._curclntconnections
		except Exception as e :
			raise e
	'''
	set curclntconnections Value
	'''
	@curclntconnections.setter
	def curclntconnections(self,curclntconnections):
		try :
			if not isinstance(curclntconnections,float):
				raise TypeError("curclntconnections must be set to float value")
			self._curclntconnections = curclntconnections
		except Exception as e :
			raise e


	'''
	get Vserver Effective State
	'''
	@property
	def vsvr_state(self) :
		try:
			return self._vsvr_state
		except Exception as e :
			raise e


	'''
	get Vserver Last State Change Time
	'''
	@property
	def vsvr_state_timestamp(self) :
		try:
			return self._vsvr_state_timestamp
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
	get Vserver State
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
	get lbmethod
	'''
	@property
	def lbmethod(self) :
		try:
			return self._lbmethod
		except Exception as e :
			raise e


	'''
	get Active services bound to the LB Vserver
	'''
	@property
	def activeservices(self) :
		try:
			return self._activeservices
		except Exception as e :
			raise e


	'''
	get Vserver Type
	'''
	@property
	def vsvr_type(self) :
		try:
			return self._vsvr_type
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
	get Total services bound to the LB Vserver
	'''
	@property
	def totalservices(self) :
		try:
			return self._totalservices
		except Exception as e :
			raise e


	'''
	get Vserver Port
	'''
	@property
	def vsvr_port(self) :
		try:
			return self._vsvr_port
		except Exception as e :
			raise e
	'''
	set Vserver Port
	'''
	@vsvr_port.setter
	def vsvr_port(self,vsvr_port):
		try :
			if not isinstance(vsvr_port,int):
				raise TypeError("vsvr_port must be set to int value")
			self._vsvr_port = vsvr_port
		except Exception as e :
			raise e


	'''
	get Vserver Health
	'''
	@property
	def vsvr_health(self) :
		try:
			return self._vsvr_health
		except Exception as e :
			raise e


	'''
	get Vserver Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Vserver Name
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
	get cursrvrconnections Value
	'''
	@property
	def cursrvrconnections(self) :
		try:
			return self._cursrvrconnections
		except Exception as e :
			raise e
	'''
	set cursrvrconnections Value
	'''
	@cursrvrconnections.setter
	def cursrvrconnections(self,cursrvrconnections):
		try :
			if not isinstance(cursrvrconnections,float):
				raise TypeError("cursrvrconnections must be set to float value")
			self._cursrvrconnections = cursrvrconnections
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
	get Managed
	'''
	@property
	def managed(self) :
		try:
			return self._managed
		except Exception as e :
			raise e
	'''
	set Managed
	'''
	@managed.setter
	def managed(self,managed):
		try :
			if not isinstance(managed,bool):
				raise TypeError("managed must be set to bool value")
			self._managed = managed
		except Exception as e :
			raise e


	'''
	get Persistence Type
	'''
	@property
	def persistencetype(self) :
		try:
			return self._persistencetype
		except Exception as e :
			raise e


	'''
	get Vserver State
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
	get Vserver IP Address
	'''
	@property
	def vsvr_ip_address(self) :
		try:
			return self._vsvr_ip_address
		except Exception as e :
			raise e
	'''
	set Vserver IP Address
	'''
	@vsvr_ip_address.setter
	def vsvr_ip_address(self,vsvr_ip_address):
		try :
			if not isinstance(vsvr_ip_address,str):
				raise TypeError("vsvr_ip_address must be set to str value")
			self._vsvr_ip_address = vsvr_ip_address
		except Exception as e :
			raise e


	'''
	get throughput value
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set throughput value
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,float):
				raise TypeError("throughput must be set to float value")
			self._throughput = throughput
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
	Service Name
	'''
	@property
	def svc_name(self):
		try:
			return self._svc_name
		except Exception as e :
			raise e
	'''
	Service Name
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
	Service ID
	'''
	@property
	def svc_id(self):
		try:
			return self._svc_id
		except Exception as e :
			raise e
	'''
	Service ID
	'''
	@svc_id.setter
	def svc_id(self,svc_id):
		try :
			if not isinstance(svc_id,str):
				raise TypeError("svc_id must be set to str value")
			self._svc_id = svc_id
		except Exception as e :
			raise e

	'''
	Service Group Name
	'''
	@property
	def svc_grp_name(self):
		try:
			return self._svc_grp_name
		except Exception as e :
			raise e
	'''
	Service Group Name
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
	Use this operation to enable the Vserver.
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
	Use this operation to get Vserver Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_lbvserver_obj=ns_lbvserver()
				response = ns_lbvserver_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to disable the Vserver.
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
	Use this API to fetch filtered set of ns_lbvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_lbvserver_obj = ns_lbvserver()
			option_ = options()
			option_._filter=filter_
			return ns_lbvserver_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_lbvserver resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_lbvserver_obj = ns_lbvserver()
			option_ = options()
			option_._count=True
			response = ns_lbvserver_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_lbvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_lbvserver_obj = ns_lbvserver()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_lbvserver_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_lbvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_lbvserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_lbvserver_responses, response, "ns_lbvserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_lbvserver_response_array
				i=0
				error = [ns_lbvserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_lbvserver_response_array
			i=0
			ns_lbvserver_objs = [ns_lbvserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_lbvserver'):
					for props in obj._ns_lbvserver:
						result = service.payload_formatter.string_to_bulk_resource(ns_lbvserver_response,self.__class__.__name__,props)
						ns_lbvserver_objs[i] = result.ns_lbvserver
						i=i+1
			return ns_lbvserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_lbvserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_lbvserver_response(base_response):
	def __init__(self,length=1) :
		self.ns_lbvserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_lbvserver= [ ns_lbvserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_lbvserver_responses(base_response):
	def __init__(self,length=1) :
		self.ns_lbvserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_lbvserver_response_array = [ ns_lbvserver() for _ in range(length)]
