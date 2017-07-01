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
Configuration for Ns event devices summary resource
'''

class ns_event_summary(base_resource):
	_total_critical_events= ""
	_longitude= ""
	_tenant_id= ""
	_is_agent= ""
	_latitude= ""
	_total_major_events= ""
	_ip_address= ""
	_instance_state= ""
	_cityname= ""
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
			return "ns_event_summary"
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
			return "ns_event_summarys"
		except Exception as e :
			raise e



	'''
	get Total Critical events city wise.
	'''
	@property
	def total_critical_events(self) :
		try:
			return self._total_critical_events
		except Exception as e :
			raise e


	'''
	get longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Is this device acting as Gateway.
	'''
	@property
	def is_agent(self) :
		try:
			return self._is_agent
		except Exception as e :
			raise e
	'''
	set Is this device acting as Gateway.
	'''
	@is_agent.setter
	def is_agent(self,is_agent):
		try :
			if not isinstance(is_agent,bool):
				raise TypeError("is_agent must be set to bool value")
			self._is_agent = is_agent
		except Exception as e :
			raise e


	'''
	get latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e


	'''
	get Total major events.
	'''
	@property
	def total_major_events(self) :
		try:
			return self._total_major_events
		except Exception as e :
			raise e


	'''
	get ip_address of the device.
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set ip_address of the device.
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
	get State of device, UP only if device accessible
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
		except Exception as e :
			raise e


	'''
	get City Name
	'''
	@property
	def cityname(self) :
		try:
			return self._cityname
		except Exception as e :
			raise e
	'''
	set City Name
	'''
	@cityname.setter
	def cityname(self,cityname):
		try :
			if not isinstance(cityname,str):
				raise TypeError("cityname must be set to str value")
			self._cityname = cityname
		except Exception as e :
			raise e

	'''
	Use this operation to get device summary report..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_event_summary_obj=ns_event_summary()
				response = ns_event_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_event_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_event_summary_obj = ns_event_summary()
			option_ = options()
			option_._filter=filter_
			return ns_event_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_event_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_event_summary_obj = ns_event_summary()
			option_ = options()
			option_._count=True
			response = ns_event_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_event_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_event_summary_obj = ns_event_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_event_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_event_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_event_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_event_summary_responses, response, "ns_event_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_event_summary_response_array
				i=0
				error = [ns_event_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_event_summary_response_array
			i=0
			ns_event_summary_objs = [ns_event_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_event_summary'):
					for props in obj._ns_event_summary:
						result = service.payload_formatter.string_to_bulk_resource(ns_event_summary_response,self.__class__.__name__,props)
						ns_event_summary_objs[i] = result.ns_event_summary
						i=i+1
			return ns_event_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_event_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_event_summary_response(base_response):
	def __init__(self,length=1) :
		self.ns_event_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_event_summary= [ ns_event_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_event_summary_responses(base_response):
	def __init__(self,length=1) :
		self.ns_event_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_event_summary_response_array = [ ns_event_summary() for _ in range(length)]
