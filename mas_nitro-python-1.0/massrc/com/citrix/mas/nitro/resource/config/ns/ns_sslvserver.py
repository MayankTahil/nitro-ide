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
Configuration for NS SSLvserver Information resource
'''

class ns_sslvserver(base_resource):
	_tls11= ""
	_ersa= ""
	_dh= ""
	_tls12= ""
	_ns_ip_address= ""
	_ssl3= ""
	_id= ""
	_tls10= ""
	_name= ""
	_poll_time= ""
	_display_name= ""
	_managed= ""
	_ssl2= ""
	_partition_name= ""
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
			return "ns_sslvserver"
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
			return "ns_sslvservers"
		except Exception as e :
			raise e



	'''
	get tls11
	'''
	@property
	def tls11(self) :
		try:
			return self._tls11
		except Exception as e :
			raise e
	'''
	set tls11
	'''
	@tls11.setter
	def tls11(self,tls11):
		try :
			if not isinstance(tls11,bool):
				raise TypeError("tls11 must be set to bool value")
			self._tls11 = tls11
		except Exception as e :
			raise e


	'''
	get ersa
	'''
	@property
	def ersa(self) :
		try:
			return self._ersa
		except Exception as e :
			raise e
	'''
	set ersa
	'''
	@ersa.setter
	def ersa(self,ersa):
		try :
			if not isinstance(ersa,bool):
				raise TypeError("ersa must be set to bool value")
			self._ersa = ersa
		except Exception as e :
			raise e


	'''
	get dh
	'''
	@property
	def dh(self) :
		try:
			return self._dh
		except Exception as e :
			raise e
	'''
	set dh
	'''
	@dh.setter
	def dh(self,dh):
		try :
			if not isinstance(dh,bool):
				raise TypeError("dh must be set to bool value")
			self._dh = dh
		except Exception as e :
			raise e


	'''
	get tls12
	'''
	@property
	def tls12(self) :
		try:
			return self._tls12
		except Exception as e :
			raise e
	'''
	set tls12
	'''
	@tls12.setter
	def tls12(self,tls12):
		try :
			if not isinstance(tls12,bool):
				raise TypeError("tls12 must be set to bool value")
			self._tls12 = tls12
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
	get ssl3
	'''
	@property
	def ssl3(self) :
		try:
			return self._ssl3
		except Exception as e :
			raise e
	'''
	set ssl3
	'''
	@ssl3.setter
	def ssl3(self,ssl3):
		try :
			if not isinstance(ssl3,bool):
				raise TypeError("ssl3 must be set to bool value")
			self._ssl3 = ssl3
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
	get tls1
	'''
	@property
	def tls10(self) :
		try:
			return self._tls10
		except Exception as e :
			raise e
	'''
	set tls1
	'''
	@tls10.setter
	def tls10(self,tls10):
		try :
			if not isinstance(tls10,bool):
				raise TypeError("tls10 must be set to bool value")
			self._tls10 = tls10
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
	get ssl2
	'''
	@property
	def ssl2(self) :
		try:
			return self._ssl2
		except Exception as e :
			raise e
	'''
	set ssl2
	'''
	@ssl2.setter
	def ssl2(self,ssl2):
		try :
			if not isinstance(ssl2,bool):
				raise TypeError("ssl2 must be set to bool value")
			self._ssl2 = ssl2
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
				ns_sslvserver_obj=ns_sslvserver()
				response = ns_sslvserver_obj.get_resources(client,option_)
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
	Use this API to fetch filtered set of ns_sslvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_sslvserver_obj = ns_sslvserver()
			option_ = options()
			option_._filter=filter_
			return ns_sslvserver_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_sslvserver resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_sslvserver_obj = ns_sslvserver()
			option_ = options()
			option_._count=True
			response = ns_sslvserver_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_sslvserver resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_sslvserver_obj = ns_sslvserver()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_sslvserver_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_sslvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_sslvserver
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_sslvserver_responses, response, "ns_sslvserver_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_sslvserver_response_array
				i=0
				error = [ns_sslvserver() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_sslvserver_response_array
			i=0
			ns_sslvserver_objs = [ns_sslvserver() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_sslvserver'):
					for props in obj._ns_sslvserver:
						result = service.payload_formatter.string_to_bulk_resource(ns_sslvserver_response,self.__class__.__name__,props)
						ns_sslvserver_objs[i] = result.ns_sslvserver
						i=i+1
			return ns_sslvserver_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_sslvserver,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_sslvserver_response(base_response):
	def __init__(self,length=1) :
		self.ns_sslvserver= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_sslvserver= [ ns_sslvserver() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_sslvserver_responses(base_response):
	def __init__(self,length=1) :
		self.ns_sslvserver_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_sslvserver_response_array = [ ns_sslvserver() for _ in range(length)]
