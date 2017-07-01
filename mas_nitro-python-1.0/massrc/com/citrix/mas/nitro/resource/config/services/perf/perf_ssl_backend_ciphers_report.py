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
Configuration for SSL Back-end Ciphers report resource
'''

class perf_ssl_backend_ciphers_report(base_resource):
	_sslbenullciphersrate= ""
	_sslbkendcipheraes256rate= ""
	_sslbe64bitrc4ciphersrate= ""
	_sslbe56bitrc2ciphersrate= ""
	_sslbe40bitdesciphersrate= ""
	_sslbe40bitrc4ciphersrate= ""
	_sslbe56bitdesciphersrate= ""
	_sslbe168bit3desciphersrate= ""
	_device_ip_address= ""
	_sslbe128bitrc2ciphersrate= ""
	_sslbe40bitrc2ciphersrate= ""
	_timestamp= ""
	_sslbkendcipheraes128rate= ""
	_sslbe56bitrc4ciphersrate= ""
	_sslbe128bitrc4ciphersrate= ""
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
			return "perf_ssl_backend_ciphers_report"
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
			return "perf_ssl_backend_ciphers_reports"
		except Exception as e :
			raise e



	'''
	get sslbenullciphersrate Value 
	'''
	@property
	def sslbenullciphersrate(self) :
		try:
			return self._sslbenullciphersrate
		except Exception as e :
			raise e
	'''
	set sslbenullciphersrate Value 
	'''
	@sslbenullciphersrate.setter
	def sslbenullciphersrate(self,sslbenullciphersrate):
		try :
			if not isinstance(sslbenullciphersrate,float):
				raise TypeError("sslbenullciphersrate must be set to float value")
			self._sslbenullciphersrate = sslbenullciphersrate
		except Exception as e :
			raise e


	'''
	get sslbkendcipheraes256rate Value 
	'''
	@property
	def sslbkendcipheraes256rate(self) :
		try:
			return self._sslbkendcipheraes256rate
		except Exception as e :
			raise e
	'''
	set sslbkendcipheraes256rate Value 
	'''
	@sslbkendcipheraes256rate.setter
	def sslbkendcipheraes256rate(self,sslbkendcipheraes256rate):
		try :
			if not isinstance(sslbkendcipheraes256rate,float):
				raise TypeError("sslbkendcipheraes256rate must be set to float value")
			self._sslbkendcipheraes256rate = sslbkendcipheraes256rate
		except Exception as e :
			raise e


	'''
	get sslbe64bitrc4ciphersrate Value 
	'''
	@property
	def sslbe64bitrc4ciphersrate(self) :
		try:
			return self._sslbe64bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe64bitrc4ciphersrate Value 
	'''
	@sslbe64bitrc4ciphersrate.setter
	def sslbe64bitrc4ciphersrate(self,sslbe64bitrc4ciphersrate):
		try :
			if not isinstance(sslbe64bitrc4ciphersrate,float):
				raise TypeError("sslbe64bitrc4ciphersrate must be set to float value")
			self._sslbe64bitrc4ciphersrate = sslbe64bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe56bitrc2ciphersrate Value 
	'''
	@property
	def sslbe56bitrc2ciphersrate(self) :
		try:
			return self._sslbe56bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe56bitrc2ciphersrate Value 
	'''
	@sslbe56bitrc2ciphersrate.setter
	def sslbe56bitrc2ciphersrate(self,sslbe56bitrc2ciphersrate):
		try :
			if not isinstance(sslbe56bitrc2ciphersrate,float):
				raise TypeError("sslbe56bitrc2ciphersrate must be set to float value")
			self._sslbe56bitrc2ciphersrate = sslbe56bitrc2ciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe40bitdesciphersrate Value 
	'''
	@property
	def sslbe40bitdesciphersrate(self) :
		try:
			return self._sslbe40bitdesciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe40bitdesciphersrate Value 
	'''
	@sslbe40bitdesciphersrate.setter
	def sslbe40bitdesciphersrate(self,sslbe40bitdesciphersrate):
		try :
			if not isinstance(sslbe40bitdesciphersrate,float):
				raise TypeError("sslbe40bitdesciphersrate must be set to float value")
			self._sslbe40bitdesciphersrate = sslbe40bitdesciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe40bitrc4ciphersrate Value
	'''
	@property
	def sslbe40bitrc4ciphersrate(self) :
		try:
			return self._sslbe40bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe40bitrc4ciphersrate Value
	'''
	@sslbe40bitrc4ciphersrate.setter
	def sslbe40bitrc4ciphersrate(self,sslbe40bitrc4ciphersrate):
		try :
			if not isinstance(sslbe40bitrc4ciphersrate,float):
				raise TypeError("sslbe40bitrc4ciphersrate must be set to float value")
			self._sslbe40bitrc4ciphersrate = sslbe40bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe56bitdesciphersrate Value 
	'''
	@property
	def sslbe56bitdesciphersrate(self) :
		try:
			return self._sslbe56bitdesciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe56bitdesciphersrate Value 
	'''
	@sslbe56bitdesciphersrate.setter
	def sslbe56bitdesciphersrate(self,sslbe56bitdesciphersrate):
		try :
			if not isinstance(sslbe56bitdesciphersrate,float):
				raise TypeError("sslbe56bitdesciphersrate must be set to float value")
			self._sslbe56bitdesciphersrate = sslbe56bitdesciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe168bit3desciphersrate Value 
	'''
	@property
	def sslbe168bit3desciphersrate(self) :
		try:
			return self._sslbe168bit3desciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe168bit3desciphersrate Value 
	'''
	@sslbe168bit3desciphersrate.setter
	def sslbe168bit3desciphersrate(self,sslbe168bit3desciphersrate):
		try :
			if not isinstance(sslbe168bit3desciphersrate,float):
				raise TypeError("sslbe168bit3desciphersrate must be set to float value")
			self._sslbe168bit3desciphersrate = sslbe168bit3desciphersrate
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
	get sslbe128bitrc2ciphersrate Value 
	'''
	@property
	def sslbe128bitrc2ciphersrate(self) :
		try:
			return self._sslbe128bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe128bitrc2ciphersrate Value 
	'''
	@sslbe128bitrc2ciphersrate.setter
	def sslbe128bitrc2ciphersrate(self,sslbe128bitrc2ciphersrate):
		try :
			if not isinstance(sslbe128bitrc2ciphersrate,float):
				raise TypeError("sslbe128bitrc2ciphersrate must be set to float value")
			self._sslbe128bitrc2ciphersrate = sslbe128bitrc2ciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe40bitrc2ciphersrate Value 
	'''
	@property
	def sslbe40bitrc2ciphersrate(self) :
		try:
			return self._sslbe40bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe40bitrc2ciphersrate Value 
	'''
	@sslbe40bitrc2ciphersrate.setter
	def sslbe40bitrc2ciphersrate(self,sslbe40bitrc2ciphersrate):
		try :
			if not isinstance(sslbe40bitrc2ciphersrate,float):
				raise TypeError("sslbe40bitrc2ciphersrate must be set to float value")
			self._sslbe40bitrc2ciphersrate = sslbe40bitrc2ciphersrate
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
	get sslbkendcipheraes128rate Value 
	'''
	@property
	def sslbkendcipheraes128rate(self) :
		try:
			return self._sslbkendcipheraes128rate
		except Exception as e :
			raise e
	'''
	set sslbkendcipheraes128rate Value 
	'''
	@sslbkendcipheraes128rate.setter
	def sslbkendcipheraes128rate(self,sslbkendcipheraes128rate):
		try :
			if not isinstance(sslbkendcipheraes128rate,float):
				raise TypeError("sslbkendcipheraes128rate must be set to float value")
			self._sslbkendcipheraes128rate = sslbkendcipheraes128rate
		except Exception as e :
			raise e


	'''
	get sslbe56bitrc4ciphersrate Value 
	'''
	@property
	def sslbe56bitrc4ciphersrate(self) :
		try:
			return self._sslbe56bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe56bitrc4ciphersrate Value 
	'''
	@sslbe56bitrc4ciphersrate.setter
	def sslbe56bitrc4ciphersrate(self,sslbe56bitrc4ciphersrate):
		try :
			if not isinstance(sslbe56bitrc4ciphersrate,float):
				raise TypeError("sslbe56bitrc4ciphersrate must be set to float value")
			self._sslbe56bitrc4ciphersrate = sslbe56bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get sslbe128bitrc4ciphersrate Value 
	'''
	@property
	def sslbe128bitrc4ciphersrate(self) :
		try:
			return self._sslbe128bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set sslbe128bitrc4ciphersrate Value 
	'''
	@sslbe128bitrc4ciphersrate.setter
	def sslbe128bitrc4ciphersrate(self,sslbe128bitrc4ciphersrate):
		try :
			if not isinstance(sslbe128bitrc4ciphersrate,float):
				raise TypeError("sslbe128bitrc4ciphersrate must be set to float value")
			self._sslbe128bitrc4ciphersrate = sslbe128bitrc4ciphersrate
		except Exception as e :
			raise e

	'''
	Use this operation to get SSL Back-end Ciphers statistics.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_ssl_backend_ciphers_report_obj=perf_ssl_backend_ciphers_report()
				response = perf_ssl_backend_ciphers_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_ssl_backend_ciphers_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_ssl_backend_ciphers_report_obj = perf_ssl_backend_ciphers_report()
			option_ = options()
			option_._filter=filter_
			return perf_ssl_backend_ciphers_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_ssl_backend_ciphers_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_ssl_backend_ciphers_report_obj = perf_ssl_backend_ciphers_report()
			option_ = options()
			option_._count=True
			response = perf_ssl_backend_ciphers_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_ssl_backend_ciphers_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_ssl_backend_ciphers_report_obj = perf_ssl_backend_ciphers_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_ssl_backend_ciphers_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_ssl_backend_ciphers_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_ssl_backend_ciphers_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_ssl_backend_ciphers_report_responses, response, "perf_ssl_backend_ciphers_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_ssl_backend_ciphers_report_response_array
				i=0
				error = [perf_ssl_backend_ciphers_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_ssl_backend_ciphers_report_response_array
			i=0
			perf_ssl_backend_ciphers_report_objs = [perf_ssl_backend_ciphers_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_ssl_backend_ciphers_report'):
					for props in obj._perf_ssl_backend_ciphers_report:
						result = service.payload_formatter.string_to_bulk_resource(perf_ssl_backend_ciphers_report_response,self.__class__.__name__,props)
						perf_ssl_backend_ciphers_report_objs[i] = result.perf_ssl_backend_ciphers_report
						i=i+1
			return perf_ssl_backend_ciphers_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_ssl_backend_ciphers_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_ssl_backend_ciphers_report_response(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_backend_ciphers_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_ssl_backend_ciphers_report= [ perf_ssl_backend_ciphers_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_ssl_backend_ciphers_report_responses(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_backend_ciphers_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_ssl_backend_ciphers_report_response_array = [ perf_ssl_backend_ciphers_report() for _ in range(length)]
