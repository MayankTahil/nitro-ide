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
Configuration for NS Callhome Information resource
'''

class ns_callhome(base_resource):
	_powfirstfail= ""
	_callhomesenablestatus= ""
	_proxy_mode= ""
	_powlatestfail= ""
	_flashlatestfail= ""
	_restartfirstfail= ""
	_hddlatestfail= ""
	_proxy_server_ip= ""
	_flashfirstfail= ""
	_ip_address= ""
	_restartlatestfail= ""
	_proxy_server_port= ""
	_hddfirstfail= ""
	_email_address= ""
	_callhomestatus= ""
	_name= ""
	_ns_ip_address_arr=[]
	_sslcardfirstfailure= ""
	_sslcardlatestfailure= ""
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
			return "ns_callhome"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._ip_address
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
			return "ns_callhomes"
		except Exception as e :
			raise e



	'''
	get First occurrence power supply unit failure
	'''
	@property
	def powfirstfail(self) :
		try:
			return self._powfirstfail
		except Exception as e :
			raise e


	'''
	get Callhome feature enabled/disable
	'''
	@property
	def callhomesenablestatus(self) :
		try:
			return self._callhomesenablestatus
		except Exception as e :
			raise e


	'''
	get Deploy the callhome proxy mode.Possible values YES or NO
	'''
	@property
	def proxy_mode(self) :
		try:
			return self._proxy_mode
		except Exception as e :
			raise e
	'''
	set Deploy the callhome proxy mode.Possible values YES or NO
	'''
	@proxy_mode.setter
	def proxy_mode(self,proxy_mode):
		try :
			if not isinstance(proxy_mode,str):
				raise TypeError("proxy_mode must be set to str value")
			self._proxy_mode = proxy_mode
		except Exception as e :
			raise e


	'''
	get Latest occurrence power supply unit failure
	'''
	@property
	def powlatestfail(self) :
		try:
			return self._powlatestfail
		except Exception as e :
			raise e


	'''
	get Latest occurrence compact flash failure
	'''
	@property
	def flashlatestfail(self) :
		try:
			return self._flashlatestfail
		except Exception as e :
			raise e


	'''
	get First occurrence warm restart failure
	'''
	@property
	def restartfirstfail(self) :
		try:
			return self._restartfirstfail
		except Exception as e :
			raise e


	'''
	get Latest occurrence hard disk drive failure
	'''
	@property
	def hddlatestfail(self) :
		try:
			return self._hddlatestfail
		except Exception as e :
			raise e


	'''
	get Proxy Server IP address
	'''
	@property
	def proxy_server_ip(self) :
		try:
			return self._proxy_server_ip
		except Exception as e :
			raise e
	'''
	set Proxy Server IP address
	'''
	@proxy_server_ip.setter
	def proxy_server_ip(self,proxy_server_ip):
		try :
			if not isinstance(proxy_server_ip,str):
				raise TypeError("proxy_server_ip must be set to str value")
			self._proxy_server_ip = proxy_server_ip
		except Exception as e :
			raise e


	'''
	get First occurrence compact flash failure
	'''
	@property
	def flashfirstfail(self) :
		try:
			return self._flashfirstfail
		except Exception as e :
			raise e


	'''
	get NS IP Address for callhome
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set NS IP Address for callhome
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
	get Latest occurrence warm restart failure
	'''
	@property
	def restartlatestfail(self) :
		try:
			return self._restartlatestfail
		except Exception as e :
			raise e


	'''
	get Proxy server Port
	'''
	@property
	def proxy_server_port(self) :
		try:
			return self._proxy_server_port
		except Exception as e :
			raise e
	'''
	set Proxy server Port
	'''
	@proxy_server_port.setter
	def proxy_server_port(self,proxy_server_port):
		try :
			if not isinstance(proxy_server_port,int):
				raise TypeError("proxy_server_port must be set to int value")
			self._proxy_server_port = proxy_server_port
		except Exception as e :
			raise e


	'''
	get First occurrence hard disk drive failure
	'''
	@property
	def hddfirstfail(self) :
		try:
			return self._hddfirstfail
		except Exception as e :
			raise e


	'''
	get The contact person's E-mail address
	'''
	@property
	def email_address(self) :
		try:
			return self._email_address
		except Exception as e :
			raise e
	'''
	set The contact person's E-mail address
	'''
	@email_address.setter
	def email_address(self,email_address):
		try :
			if not isinstance(email_address,str):
				raise TypeError("email_address must be set to str value")
			self._email_address = email_address
		except Exception as e :
			raise e


	'''
	get Callhome feature register with upload server successful/failed
	'''
	@property
	def callhomestatus(self) :
		try:
			return self._callhomestatus
		except Exception as e :
			raise e


	'''
	get Name of the vpx Instance
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the vpx Instance
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
	get List of NS IP Address
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of NS IP Address
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e


	'''
	get First occurrence SSL card failure
	'''
	@property
	def sslcardfirstfailure(self) :
		try:
			return self._sslcardfirstfailure
		except Exception as e :
			raise e


	'''
	get Latest occurrence SSL card failure
	'''
	@property
	def sslcardlatestfailure(self) :
		try:
			return self._sslcardlatestfailure
		except Exception as e :
			raise e

	'''
	Use this operation to perform poll now on NetScaler Instance.
	'''
	@classmethod
	def pollnow(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"pollnow")
			else : 
				ns_callhome_obj= ns_callhome()
				return cls.perform_operation_bulk_request(service,"pollnow", resource,ns_callhome_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to enable callhome on NetScaler Instance.
	'''
	@classmethod
	def enable(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"enable")
			else : 
				ns_callhome_obj= ns_callhome()
				return cls.perform_operation_bulk_request(service,"enable", resource,ns_callhome_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Callhome instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_callhome_obj=ns_callhome()
				response = ns_callhome_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify callhome Instance.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_callhome_obj=ns_callhome()
				return cls.update_bulk_request(client,resource,ns_callhome_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to disable callhome on NetScaler Instance.
	'''
	@classmethod
	def disable(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"disable")
			else : 
				ns_callhome_obj= ns_callhome()
				return cls.perform_operation_bulk_request(service,"disable", resource,ns_callhome_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_callhome resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_callhome_obj = ns_callhome()
			option_ = options()
			option_._filter=filter_
			return ns_callhome_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_callhome resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_callhome_obj = ns_callhome()
			option_ = options()
			option_._count=True
			response = ns_callhome_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_callhome resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_callhome_obj = ns_callhome()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_callhome_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_callhome_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_callhome
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_callhome_responses, response, "ns_callhome_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_callhome_response_array
				i=0
				error = [ns_callhome() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_callhome_response_array
			i=0
			ns_callhome_objs = [ns_callhome() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_callhome'):
					for props in obj._ns_callhome:
						result = service.payload_formatter.string_to_bulk_resource(ns_callhome_response,self.__class__.__name__,props)
						ns_callhome_objs[i] = result.ns_callhome
						i=i+1
			return ns_callhome_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_callhome,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_callhome_response(base_response):
	def __init__(self,length=1) :
		self.ns_callhome= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_callhome= [ ns_callhome() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_callhome_responses(base_response):
	def __init__(self,length=1) :
		self.ns_callhome_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_callhome_response_array = [ ns_callhome() for _ in range(length)]
