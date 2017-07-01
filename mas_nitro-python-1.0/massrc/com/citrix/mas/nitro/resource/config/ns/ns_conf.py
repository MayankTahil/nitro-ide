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
Configuration for ns.conf file on NetScaler resource
'''

class ns_conf(base_resource):
	_diff_reportname= ""
	_hostname= ""
	_diff_status= ""
	_display_name= ""
	_ns_ip_address= ""
	_last_updated_time= ""
	_device_name= ""
	_templatediff_reportname= ""
	_id= ""
	_templatediff_status= ""
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
			return "ns_conf"
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
			return "ns_confs"
		except Exception as e :
			raise e



	'''
	get Name of the SavedVsRunning diff reportname
	'''
	@property
	def diff_reportname(self) :
		try:
			return self._diff_reportname
		except Exception as e :
			raise e


	'''
	get Host Name of the device
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get Tells whether a diff exists between running and saved configuration on NS
	'''
	@property
	def diff_status(self) :
		try:
			return self._diff_status
		except Exception as e :
			raise e
	'''
	set Tells whether a diff exists between running and saved configuration on NS
	'''
	@diff_status.setter
	def diff_status(self,diff_status):
		try :
			if not isinstance(diff_status,str):
				raise TypeError("diff_status must be set to str value")
			self._diff_status = diff_status
		except Exception as e :
			raise e


	'''
	get Display Name of the device
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e


	'''
	get List of NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set List of NetScaler IP Address
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
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
		except Exception as e :
			raise e
	'''
	set Last Updated Time
	'''
	@last_updated_time.setter
	def last_updated_time(self,last_updated_time):
		try :
			if not isinstance(last_updated_time,int):
				raise TypeError("last_updated_time must be set to int value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get Name of the device
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
		except Exception as e :
			raise e


	'''
	get Name of the Template diff reports
	'''
	@property
	def templatediff_reportname(self) :
		try:
			return self._templatediff_reportname
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all ns.conf files
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all ns.conf files
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
	get Tells whether a diff exists between templates associated to the  NS and the running configuration
	'''
	@property
	def templatediff_status(self) :
		try:
			return self._templatediff_status
		except Exception as e :
			raise e
	'''
	set Tells whether a diff exists between templates associated to the  NS and the running configuration
	'''
	@templatediff_status.setter
	def templatediff_status(self,templatediff_status):
		try :
			if not isinstance(templatediff_status,str):
				raise TypeError("templatediff_status must be set to str value")
			self._templatediff_status = templatediff_status
		except Exception as e :
			raise e

	'''
	Get ns.conf information from NS Instance(s).
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_conf_obj=ns_conf()
				response = ns_conf_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_conf resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_conf_obj = ns_conf()
			option_ = options()
			option_._filter=filter_
			return ns_conf_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_conf resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_conf_obj = ns_conf()
			option_ = options()
			option_._count=True
			response = ns_conf_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_conf resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_conf_obj = ns_conf()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_conf_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_conf_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_conf
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_conf_responses, response, "ns_conf_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_conf_response_array
				i=0
				error = [ns_conf() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_conf_response_array
			i=0
			ns_conf_objs = [ns_conf() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_conf'):
					for props in obj._ns_conf:
						result = service.payload_formatter.string_to_bulk_resource(ns_conf_response,self.__class__.__name__,props)
						ns_conf_objs[i] = result.ns_conf
						i=i+1
			return ns_conf_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_conf,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_conf_response(base_response):
	def __init__(self,length=1) :
		self.ns_conf= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_conf= [ ns_conf() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_conf_responses(base_response):
	def __init__(self,length=1) :
		self.ns_conf_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_conf_response_array = [ ns_conf() for _ in range(length)]
