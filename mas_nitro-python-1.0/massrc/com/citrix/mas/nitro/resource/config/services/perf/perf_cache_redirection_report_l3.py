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
Configuration for Cache Redirection resource
'''

class perf_cache_redirection_report_l3(base_resource):
	_totalpktssent= ""
	_device_ip_address= ""
	_vsvrName= ""
	_totalpktsrecvd= ""
	_timestamp= ""
	_totalresponsebytes= ""
	_totalrequestbytes= ""
	_responsesrate= ""
	_requestsrate= ""
	_hitsrate= ""
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
			return "perf_cache_redirection_report_l3"
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
			return "perf_cache_redirection_report_l3s"
		except Exception as e :
			raise e



	'''
	get totalpktssent Value 
	'''
	@property
	def totalpktssent(self) :
		try:
			return self._totalpktssent
		except Exception as e :
			raise e
	'''
	set totalpktssent Value 
	'''
	@totalpktssent.setter
	def totalpktssent(self,totalpktssent):
		try :
			if not isinstance(totalpktssent,float):
				raise TypeError("totalpktssent must be set to float value")
			self._totalpktssent = totalpktssent
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
	get totalpktsrecvd Value
	'''
	@property
	def totalpktsrecvd(self) :
		try:
			return self._totalpktsrecvd
		except Exception as e :
			raise e
	'''
	set totalpktsrecvd Value
	'''
	@totalpktsrecvd.setter
	def totalpktsrecvd(self,totalpktsrecvd):
		try :
			if not isinstance(totalpktsrecvd,float):
				raise TypeError("totalpktsrecvd must be set to float value")
			self._totalpktsrecvd = totalpktsrecvd
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
	get totalresponsebytes Value 
	'''
	@property
	def totalresponsebytes(self) :
		try:
			return self._totalresponsebytes
		except Exception as e :
			raise e
	'''
	set totalresponsebytes Value 
	'''
	@totalresponsebytes.setter
	def totalresponsebytes(self,totalresponsebytes):
		try :
			if not isinstance(totalresponsebytes,float):
				raise TypeError("totalresponsebytes must be set to float value")
			self._totalresponsebytes = totalresponsebytes
		except Exception as e :
			raise e


	'''
	get totalrequestbytes Value
	'''
	@property
	def totalrequestbytes(self) :
		try:
			return self._totalrequestbytes
		except Exception as e :
			raise e
	'''
	set totalrequestbytes Value
	'''
	@totalrequestbytes.setter
	def totalrequestbytes(self,totalrequestbytes):
		try :
			if not isinstance(totalrequestbytes,float):
				raise TypeError("totalrequestbytes must be set to float value")
			self._totalrequestbytes = totalrequestbytes
		except Exception as e :
			raise e


	'''
	get responsesrate Value
	'''
	@property
	def responsesrate(self) :
		try:
			return self._responsesrate
		except Exception as e :
			raise e
	'''
	set responsesrate Value
	'''
	@responsesrate.setter
	def responsesrate(self,responsesrate):
		try :
			if not isinstance(responsesrate,float):
				raise TypeError("responsesrate must be set to float value")
			self._responsesrate = responsesrate
		except Exception as e :
			raise e


	'''
	get requestsrate Value 
	'''
	@property
	def requestsrate(self) :
		try:
			return self._requestsrate
		except Exception as e :
			raise e
	'''
	set requestsrate Value 
	'''
	@requestsrate.setter
	def requestsrate(self,requestsrate):
		try :
			if not isinstance(requestsrate,float):
				raise TypeError("requestsrate must be set to float value")
			self._requestsrate = requestsrate
		except Exception as e :
			raise e


	'''
	get hitsrate Value
	'''
	@property
	def hitsrate(self) :
		try:
			return self._hitsrate
		except Exception as e :
			raise e
	'''
	set hitsrate Value
	'''
	@hitsrate.setter
	def hitsrate(self,hitsrate):
		try :
			if not isinstance(hitsrate,float):
				raise TypeError("hitsrate must be set to float value")
			self._hitsrate = hitsrate
		except Exception as e :
			raise e

	'''
	Use this operation to get Cache Redirection Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_cache_redirection_report_l3_obj=perf_cache_redirection_report_l3()
				response = perf_cache_redirection_report_l3_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_cache_redirection_report_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_cache_redirection_report_l3_obj = perf_cache_redirection_report_l3()
			option_ = options()
			option_._filter=filter_
			return perf_cache_redirection_report_l3_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_cache_redirection_report_l3 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_cache_redirection_report_l3_obj = perf_cache_redirection_report_l3()
			option_ = options()
			option_._count=True
			response = perf_cache_redirection_report_l3_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_cache_redirection_report_l3 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_cache_redirection_report_l3_obj = perf_cache_redirection_report_l3()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_cache_redirection_report_l3_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_cache_redirection_report_l3_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_cache_redirection_report_l3
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_cache_redirection_report_l3_responses, response, "perf_cache_redirection_report_l3_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_cache_redirection_report_l3_response_array
				i=0
				error = [perf_cache_redirection_report_l3() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_cache_redirection_report_l3_response_array
			i=0
			perf_cache_redirection_report_l3_objs = [perf_cache_redirection_report_l3() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_cache_redirection_report_l3'):
					for props in obj._perf_cache_redirection_report_l3:
						result = service.payload_formatter.string_to_bulk_resource(perf_cache_redirection_report_l3_response,self.__class__.__name__,props)
						perf_cache_redirection_report_l3_objs[i] = result.perf_cache_redirection_report_l3
						i=i+1
			return perf_cache_redirection_report_l3_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_cache_redirection_report_l3,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_cache_redirection_report_l3_response(base_response):
	def __init__(self,length=1) :
		self.perf_cache_redirection_report_l3= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_cache_redirection_report_l3= [ perf_cache_redirection_report_l3() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_cache_redirection_report_l3_responses(base_response):
	def __init__(self,length=1) :
		self.perf_cache_redirection_report_l3_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_cache_redirection_report_l3_response_array = [ perf_cache_redirection_report_l3() for _ in range(length)]
