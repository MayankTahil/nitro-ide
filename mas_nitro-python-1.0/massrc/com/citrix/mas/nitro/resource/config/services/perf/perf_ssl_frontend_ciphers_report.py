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
Configuration for SSL Front-end Ciphers report resource
'''

class perf_ssl_frontend_ciphers_report(base_resource):
	_ssl56bitdesciphersrate= ""
	_ssl128bitrc2ciphersrate= ""
	_ssl168bit3desciphersrate= ""
	_sslnullciphersrate= ""
	_ssl40bitrc2ciphersrate= ""
	_ssl56bitrc4ciphersrate= ""
	_ssl128bitrc4ciphersrate= ""
	_device_ip_address= ""
	_sslcipheraes128rate= ""
	_timestamp= ""
	_sslcipheraes256rate= ""
	_ssl64bitrc4ciphersrate= ""
	_ssl40bitdesciphersrate= ""
	_ssl40bitrc4ciphersrate= ""
	_ssl56bitrc2ciphersrate= ""
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
			return "perf_ssl_frontend_ciphers_report"
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
			return "perf_ssl_frontend_ciphers_reports"
		except Exception as e :
			raise e



	'''
	get ssl56bitdesciphersrate Value 
	'''
	@property
	def ssl56bitdesciphersrate(self) :
		try:
			return self._ssl56bitdesciphersrate
		except Exception as e :
			raise e
	'''
	set ssl56bitdesciphersrate Value 
	'''
	@ssl56bitdesciphersrate.setter
	def ssl56bitdesciphersrate(self,ssl56bitdesciphersrate):
		try :
			if not isinstance(ssl56bitdesciphersrate,float):
				raise TypeError("ssl56bitdesciphersrate must be set to float value")
			self._ssl56bitdesciphersrate = ssl56bitdesciphersrate
		except Exception as e :
			raise e


	'''
	get ssl128bitrc2ciphersrate Value 
	'''
	@property
	def ssl128bitrc2ciphersrate(self) :
		try:
			return self._ssl128bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl128bitrc2ciphersrate Value 
	'''
	@ssl128bitrc2ciphersrate.setter
	def ssl128bitrc2ciphersrate(self,ssl128bitrc2ciphersrate):
		try :
			if not isinstance(ssl128bitrc2ciphersrate,float):
				raise TypeError("ssl128bitrc2ciphersrate must be set to float value")
			self._ssl128bitrc2ciphersrate = ssl128bitrc2ciphersrate
		except Exception as e :
			raise e


	'''
	get ssl168bit3desciphersrate Value 
	'''
	@property
	def ssl168bit3desciphersrate(self) :
		try:
			return self._ssl168bit3desciphersrate
		except Exception as e :
			raise e
	'''
	set ssl168bit3desciphersrate Value 
	'''
	@ssl168bit3desciphersrate.setter
	def ssl168bit3desciphersrate(self,ssl168bit3desciphersrate):
		try :
			if not isinstance(ssl168bit3desciphersrate,float):
				raise TypeError("ssl168bit3desciphersrate must be set to float value")
			self._ssl168bit3desciphersrate = ssl168bit3desciphersrate
		except Exception as e :
			raise e


	'''
	get sslnullciphersrate Value 
	'''
	@property
	def sslnullciphersrate(self) :
		try:
			return self._sslnullciphersrate
		except Exception as e :
			raise e
	'''
	set sslnullciphersrate Value 
	'''
	@sslnullciphersrate.setter
	def sslnullciphersrate(self,sslnullciphersrate):
		try :
			if not isinstance(sslnullciphersrate,float):
				raise TypeError("sslnullciphersrate must be set to float value")
			self._sslnullciphersrate = sslnullciphersrate
		except Exception as e :
			raise e


	'''
	get ssl40bitrc2ciphersrate Value 
	'''
	@property
	def ssl40bitrc2ciphersrate(self) :
		try:
			return self._ssl40bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl40bitrc2ciphersrate Value 
	'''
	@ssl40bitrc2ciphersrate.setter
	def ssl40bitrc2ciphersrate(self,ssl40bitrc2ciphersrate):
		try :
			if not isinstance(ssl40bitrc2ciphersrate,float):
				raise TypeError("ssl40bitrc2ciphersrate must be set to float value")
			self._ssl40bitrc2ciphersrate = ssl40bitrc2ciphersrate
		except Exception as e :
			raise e


	'''
	get ssl56bitrc4ciphersrate Value 
	'''
	@property
	def ssl56bitrc4ciphersrate(self) :
		try:
			return self._ssl56bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl56bitrc4ciphersrate Value 
	'''
	@ssl56bitrc4ciphersrate.setter
	def ssl56bitrc4ciphersrate(self,ssl56bitrc4ciphersrate):
		try :
			if not isinstance(ssl56bitrc4ciphersrate,float):
				raise TypeError("ssl56bitrc4ciphersrate must be set to float value")
			self._ssl56bitrc4ciphersrate = ssl56bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get ssl128bitrc4ciphersrate Value 
	'''
	@property
	def ssl128bitrc4ciphersrate(self) :
		try:
			return self._ssl128bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl128bitrc4ciphersrate Value 
	'''
	@ssl128bitrc4ciphersrate.setter
	def ssl128bitrc4ciphersrate(self,ssl128bitrc4ciphersrate):
		try :
			if not isinstance(ssl128bitrc4ciphersrate,float):
				raise TypeError("ssl128bitrc4ciphersrate must be set to float value")
			self._ssl128bitrc4ciphersrate = ssl128bitrc4ciphersrate
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
	get sslcipheraes128rate Value 
	'''
	@property
	def sslcipheraes128rate(self) :
		try:
			return self._sslcipheraes128rate
		except Exception as e :
			raise e
	'''
	set sslcipheraes128rate Value 
	'''
	@sslcipheraes128rate.setter
	def sslcipheraes128rate(self,sslcipheraes128rate):
		try :
			if not isinstance(sslcipheraes128rate,float):
				raise TypeError("sslcipheraes128rate must be set to float value")
			self._sslcipheraes128rate = sslcipheraes128rate
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
	get sslcipheraes256rate Value 
	'''
	@property
	def sslcipheraes256rate(self) :
		try:
			return self._sslcipheraes256rate
		except Exception as e :
			raise e
	'''
	set sslcipheraes256rate Value 
	'''
	@sslcipheraes256rate.setter
	def sslcipheraes256rate(self,sslcipheraes256rate):
		try :
			if not isinstance(sslcipheraes256rate,float):
				raise TypeError("sslcipheraes256rate must be set to float value")
			self._sslcipheraes256rate = sslcipheraes256rate
		except Exception as e :
			raise e


	'''
	get ssl64bitrc4ciphersrate Value 
	'''
	@property
	def ssl64bitrc4ciphersrate(self) :
		try:
			return self._ssl64bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl64bitrc4ciphersrate Value 
	'''
	@ssl64bitrc4ciphersrate.setter
	def ssl64bitrc4ciphersrate(self,ssl64bitrc4ciphersrate):
		try :
			if not isinstance(ssl64bitrc4ciphersrate,float):
				raise TypeError("ssl64bitrc4ciphersrate must be set to float value")
			self._ssl64bitrc4ciphersrate = ssl64bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get ssl40bitdesciphersrate Value 
	'''
	@property
	def ssl40bitdesciphersrate(self) :
		try:
			return self._ssl40bitdesciphersrate
		except Exception as e :
			raise e
	'''
	set ssl40bitdesciphersrate Value 
	'''
	@ssl40bitdesciphersrate.setter
	def ssl40bitdesciphersrate(self,ssl40bitdesciphersrate):
		try :
			if not isinstance(ssl40bitdesciphersrate,float):
				raise TypeError("ssl40bitdesciphersrate must be set to float value")
			self._ssl40bitdesciphersrate = ssl40bitdesciphersrate
		except Exception as e :
			raise e


	'''
	get ssl40bitrc4ciphersrate Value
	'''
	@property
	def ssl40bitrc4ciphersrate(self) :
		try:
			return self._ssl40bitrc4ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl40bitrc4ciphersrate Value
	'''
	@ssl40bitrc4ciphersrate.setter
	def ssl40bitrc4ciphersrate(self,ssl40bitrc4ciphersrate):
		try :
			if not isinstance(ssl40bitrc4ciphersrate,float):
				raise TypeError("ssl40bitrc4ciphersrate must be set to float value")
			self._ssl40bitrc4ciphersrate = ssl40bitrc4ciphersrate
		except Exception as e :
			raise e


	'''
	get ssl56bitrc2ciphersrate Value 
	'''
	@property
	def ssl56bitrc2ciphersrate(self) :
		try:
			return self._ssl56bitrc2ciphersrate
		except Exception as e :
			raise e
	'''
	set ssl56bitrc2ciphersrate Value 
	'''
	@ssl56bitrc2ciphersrate.setter
	def ssl56bitrc2ciphersrate(self,ssl56bitrc2ciphersrate):
		try :
			if not isinstance(ssl56bitrc2ciphersrate,float):
				raise TypeError("ssl56bitrc2ciphersrate must be set to float value")
			self._ssl56bitrc2ciphersrate = ssl56bitrc2ciphersrate
		except Exception as e :
			raise e

	'''
	Use this operation to get SSL Front-end Ciphers statistics.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_ssl_frontend_ciphers_report_obj=perf_ssl_frontend_ciphers_report()
				response = perf_ssl_frontend_ciphers_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_ssl_frontend_ciphers_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_ssl_frontend_ciphers_report_obj = perf_ssl_frontend_ciphers_report()
			option_ = options()
			option_._filter=filter_
			return perf_ssl_frontend_ciphers_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_ssl_frontend_ciphers_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_ssl_frontend_ciphers_report_obj = perf_ssl_frontend_ciphers_report()
			option_ = options()
			option_._count=True
			response = perf_ssl_frontend_ciphers_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_ssl_frontend_ciphers_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_ssl_frontend_ciphers_report_obj = perf_ssl_frontend_ciphers_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_ssl_frontend_ciphers_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_ssl_frontend_ciphers_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_ssl_frontend_ciphers_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_ssl_frontend_ciphers_report_responses, response, "perf_ssl_frontend_ciphers_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_ssl_frontend_ciphers_report_response_array
				i=0
				error = [perf_ssl_frontend_ciphers_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_ssl_frontend_ciphers_report_response_array
			i=0
			perf_ssl_frontend_ciphers_report_objs = [perf_ssl_frontend_ciphers_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_ssl_frontend_ciphers_report'):
					for props in obj._perf_ssl_frontend_ciphers_report:
						result = service.payload_formatter.string_to_bulk_resource(perf_ssl_frontend_ciphers_report_response,self.__class__.__name__,props)
						perf_ssl_frontend_ciphers_report_objs[i] = result.perf_ssl_frontend_ciphers_report
						i=i+1
			return perf_ssl_frontend_ciphers_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_ssl_frontend_ciphers_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_ssl_frontend_ciphers_report_response(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_frontend_ciphers_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_ssl_frontend_ciphers_report= [ perf_ssl_frontend_ciphers_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_ssl_frontend_ciphers_report_responses(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_frontend_ciphers_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_ssl_frontend_ciphers_report_response_array = [ perf_ssl_frontend_ciphers_report() for _ in range(length)]
