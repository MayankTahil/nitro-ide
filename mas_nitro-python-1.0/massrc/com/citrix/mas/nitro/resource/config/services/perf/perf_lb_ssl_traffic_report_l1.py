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
Configuration for LBVServer resource
'''

class perf_lb_ssl_traffic_report_l1(base_resource):
	_sslctxsessionnewrate= ""
	_vsvrName= ""
	_sslctxdecbytesrate= ""
	_timestamp= ""
	_sslctxsessionhitsrate= ""
	_sslctxencbytesrate= ""
	_device_ip_address= ""
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
			return "perf_lb_ssl_traffic_report_l1"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "perf_lb_ssl_traffic_report_l1s"
		except Exception as e :
			raise e



	'''
	get sslctxsessionnewrate Value 
	'''
	@property
	def sslctxsessionnewrate(self) :
		try:
			return self._sslctxsessionnewrate
		except Exception as e :
			raise e
	'''
	set sslctxsessionnewrate Value 
	'''
	@sslctxsessionnewrate.setter
	def sslctxsessionnewrate(self,sslctxsessionnewrate):
		try :
			if not isinstance(sslctxsessionnewrate,float):
				raise TypeError("sslctxsessionnewrate must be set to float value")
			self._sslctxsessionnewrate = sslctxsessionnewrate
		except Exception as e :
			raise e


	'''
	get vsvrName Value 
	'''
	@property
	def vsvrName(self) :
		try:
			return self._vsvrName
		except Exception as e :
			raise e
	'''
	set vsvrName Value 
	'''
	@vsvrName.setter
	def vsvrName(self,vsvrName):
		try :
			if not isinstance(vsvrName,str):
				raise TypeError("vsvrName must be set to str value")
			self._vsvrName = vsvrName
		except Exception as e :
			raise e


	'''
	get sslctxdecbytesrate Value
	'''
	@property
	def sslctxdecbytesrate(self) :
		try:
			return self._sslctxdecbytesrate
		except Exception as e :
			raise e
	'''
	set sslctxdecbytesrate Value
	'''
	@sslctxdecbytesrate.setter
	def sslctxdecbytesrate(self,sslctxdecbytesrate):
		try :
			if not isinstance(sslctxdecbytesrate,float):
				raise TypeError("sslctxdecbytesrate must be set to float value")
			self._sslctxdecbytesrate = sslctxdecbytesrate
		except Exception as e :
			raise e


	'''
	get timestamp in milliseconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in milliseconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get sslctxsessionhitsrate Value
	'''
	@property
	def sslctxsessionhitsrate(self) :
		try:
			return self._sslctxsessionhitsrate
		except Exception as e :
			raise e
	'''
	set sslctxsessionhitsrate Value
	'''
	@sslctxsessionhitsrate.setter
	def sslctxsessionhitsrate(self,sslctxsessionhitsrate):
		try :
			if not isinstance(sslctxsessionhitsrate,float):
				raise TypeError("sslctxsessionhitsrate must be set to float value")
			self._sslctxsessionhitsrate = sslctxsessionhitsrate
		except Exception as e :
			raise e


	'''
	get sslctxencbytesrate Value 
	'''
	@property
	def sslctxencbytesrate(self) :
		try:
			return self._sslctxencbytesrate
		except Exception as e :
			raise e
	'''
	set sslctxencbytesrate Value 
	'''
	@sslctxencbytesrate.setter
	def sslctxencbytesrate(self,sslctxencbytesrate):
		try :
			if not isinstance(sslctxencbytesrate,float):
				raise TypeError("sslctxencbytesrate must be set to float value")
			self._sslctxencbytesrate = sslctxencbytesrate
		except Exception as e :
			raise e


	'''
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get LB Vserver Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_lb_ssl_traffic_report_l1_obj=perf_lb_ssl_traffic_report_l1()
				response = perf_lb_ssl_traffic_report_l1_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_lb_ssl_traffic_report_l1 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_lb_ssl_traffic_report_l1_obj = perf_lb_ssl_traffic_report_l1()
			option_ = options()
			option_._filter=filter_
			return perf_lb_ssl_traffic_report_l1_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_lb_ssl_traffic_report_l1 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_lb_ssl_traffic_report_l1_obj = perf_lb_ssl_traffic_report_l1()
			option_ = options()
			option_._count=True
			response = perf_lb_ssl_traffic_report_l1_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_lb_ssl_traffic_report_l1 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_lb_ssl_traffic_report_l1_obj = perf_lb_ssl_traffic_report_l1()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_lb_ssl_traffic_report_l1_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_lb_ssl_traffic_report_l1_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_lb_ssl_traffic_report_l1
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_lb_ssl_traffic_report_l1_responses, response, "perf_lb_ssl_traffic_report_l1_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_lb_ssl_traffic_report_l1_response_array
				i=0
				error = [perf_lb_ssl_traffic_report_l1() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_lb_ssl_traffic_report_l1_response_array
			i=0
			perf_lb_ssl_traffic_report_l1_objs = [perf_lb_ssl_traffic_report_l1() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_lb_ssl_traffic_report_l1'):
					for props in obj._perf_lb_ssl_traffic_report_l1:
						result = service.payload_formatter.string_to_bulk_resource(perf_lb_ssl_traffic_report_l1_response,self.__class__.__name__,props)
						perf_lb_ssl_traffic_report_l1_objs[i] = result.perf_lb_ssl_traffic_report_l1
						i=i+1
			return perf_lb_ssl_traffic_report_l1_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_lb_ssl_traffic_report_l1,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_lb_ssl_traffic_report_l1_response(base_response):
	def __init__(self,length=1) :
		self.perf_lb_ssl_traffic_report_l1= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_lb_ssl_traffic_report_l1= [ perf_lb_ssl_traffic_report_l1() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_lb_ssl_traffic_report_l1_responses(base_response):
	def __init__(self,length=1) :
		self.perf_lb_ssl_traffic_report_l1_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_lb_ssl_traffic_report_l1_response_array = [ perf_lb_ssl_traffic_report_l1() for _ in range(length)]
