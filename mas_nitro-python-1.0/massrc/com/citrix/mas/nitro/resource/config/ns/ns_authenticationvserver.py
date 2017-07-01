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
Configuration for NS Authvserver Information resource
'''

class ns_authenticationvserver(base_resource):
	_vsvr_port= ""
	_user_managed= ""
	_name= ""
	_hostname= ""
	_poll_time= ""
	_display_name= ""
	_state= ""
	_ns_ip_address= ""
	_managed= ""
	_partition_name= ""
	_vsvr_ip_address= ""
	_vsvr_type= ""
	_throughput= ""
	_id= ""
	_save_config= ""
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
			return "ns_authenticationvserver"
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
			return "ns_authenticationvservers"
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
	get Hostname of the managed device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
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
	get Vserver Type
	'''
	@property
	def vsvr_type(self) :
		try:
			return self._vsvr_type
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
				ns_authenticationvserver_obj=ns_authenticationvserver()
				response = ns_authenticationvserver_obj.get_resources(client,option_)
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
	Use this API to fetch filtered set of ns_authenticationvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_authenticationvserver_obj = ns_authenticationvserver()
			option_ = options()
			option_._filter=filter_
			return ns_authenticationvserver_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_authenticationvserver resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_authenticationvserver_obj = ns_authenticationvserver()
			option_ = options()
			option_._count=True
			response = ns_authenticationvserver_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_authenticationvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_authenticationvserver_obj = ns_authenticationvserver()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_authenticationvserver_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_authenticationvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_authenticationvserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_authenticationvserver_responses, response, "ns_authenticationvserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_authenticationvserver_response_array
				i=0
				error = [ns_authenticationvserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_authenticationvserver_response_array
			i=0
			ns_authenticationvserver_objs = [ns_authenticationvserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_authenticationvserver'):
					for props in obj._ns_authenticationvserver:
						result = service.payload_formatter.string_to_bulk_resource(ns_authenticationvserver_response,self.__class__.__name__,props)
						ns_authenticationvserver_objs[i] = result.ns_authenticationvserver
						i=i+1
			return ns_authenticationvserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_authenticationvserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_authenticationvserver_response(base_response):
	def __init__(self,length=1) :
		self.ns_authenticationvserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_authenticationvserver= [ ns_authenticationvserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_authenticationvserver_responses(base_response):
	def __init__(self,length=1) :
		self.ns_authenticationvserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_authenticationvserver_response_array = [ ns_authenticationvserver() for _ in range(length)]
