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
Configuration for SSL CPU utilization and key exchange metrics report resource
'''

class perf_ssl_cpu_keyexchange_report(base_resource):
	_ssldh2048keyexchangesrate= ""
	_ssldh1024keyexchangesrate= ""
	_sslbedh2048keyexchangesrate= ""
	_sslbersa1024keyexchangesrate= ""
	_sslecdhe256keyexchangesrate= ""
	_sslecdhe384keyexchangesrate= ""
	_sslecdhe521keyexchangesrate= ""
	_device_ip_address= ""
	_sslbersa2048keyexchangesrate= ""
	_sslrsa1024keyexchangesrate= ""
	_sslbedh1024keyexchangesrate= ""
	_timestamp= ""
	_sslrsa2048keyexchangesrate= ""
	_sslecdhe224keyexchangesrate= ""
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
			return "perf_ssl_cpu_keyexchange_report"
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
			return "perf_ssl_cpu_keyexchange_reports"
		except Exception as e :
			raise e



	'''
	get ssldh2048keyexchangesrate Value 
	'''
	@property
	def ssldh2048keyexchangesrate(self) :
		try:
			return self._ssldh2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set ssldh2048keyexchangesrate Value 
	'''
	@ssldh2048keyexchangesrate.setter
	def ssldh2048keyexchangesrate(self,ssldh2048keyexchangesrate):
		try :
			if not isinstance(ssldh2048keyexchangesrate,float):
				raise TypeError("ssldh2048keyexchangesrate must be set to float value")
			self._ssldh2048keyexchangesrate = ssldh2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get ssldh1024keyexchangesrate Value 
	'''
	@property
	def ssldh1024keyexchangesrate(self) :
		try:
			return self._ssldh1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set ssldh1024keyexchangesrate Value 
	'''
	@ssldh1024keyexchangesrate.setter
	def ssldh1024keyexchangesrate(self,ssldh1024keyexchangesrate):
		try :
			if not isinstance(ssldh1024keyexchangesrate,float):
				raise TypeError("ssldh1024keyexchangesrate must be set to float value")
			self._ssldh1024keyexchangesrate = ssldh1024keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbedh2048keyexchangesrate Value 
	'''
	@property
	def sslbedh2048keyexchangesrate(self) :
		try:
			return self._sslbedh2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbedh2048keyexchangesrate Value 
	'''
	@sslbedh2048keyexchangesrate.setter
	def sslbedh2048keyexchangesrate(self,sslbedh2048keyexchangesrate):
		try :
			if not isinstance(sslbedh2048keyexchangesrate,float):
				raise TypeError("sslbedh2048keyexchangesrate must be set to float value")
			self._sslbedh2048keyexchangesrate = sslbedh2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbersa1024keyexchangesrate Value 
	'''
	@property
	def sslbersa1024keyexchangesrate(self) :
		try:
			return self._sslbersa1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbersa1024keyexchangesrate Value 
	'''
	@sslbersa1024keyexchangesrate.setter
	def sslbersa1024keyexchangesrate(self,sslbersa1024keyexchangesrate):
		try :
			if not isinstance(sslbersa1024keyexchangesrate,float):
				raise TypeError("sslbersa1024keyexchangesrate must be set to float value")
			self._sslbersa1024keyexchangesrate = sslbersa1024keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslecdhe256keyexchangesrate Value 
	'''
	@property
	def sslecdhe256keyexchangesrate(self) :
		try:
			return self._sslecdhe256keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslecdhe256keyexchangesrate Value 
	'''
	@sslecdhe256keyexchangesrate.setter
	def sslecdhe256keyexchangesrate(self,sslecdhe256keyexchangesrate):
		try :
			if not isinstance(sslecdhe256keyexchangesrate,float):
				raise TypeError("sslecdhe256keyexchangesrate must be set to float value")
			self._sslecdhe256keyexchangesrate = sslecdhe256keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslecdhe384keyexchangesrate Value 
	'''
	@property
	def sslecdhe384keyexchangesrate(self) :
		try:
			return self._sslecdhe384keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslecdhe384keyexchangesrate Value 
	'''
	@sslecdhe384keyexchangesrate.setter
	def sslecdhe384keyexchangesrate(self,sslecdhe384keyexchangesrate):
		try :
			if not isinstance(sslecdhe384keyexchangesrate,float):
				raise TypeError("sslecdhe384keyexchangesrate must be set to float value")
			self._sslecdhe384keyexchangesrate = sslecdhe384keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslecdhe521keyexchangesrate Value 
	'''
	@property
	def sslecdhe521keyexchangesrate(self) :
		try:
			return self._sslecdhe521keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslecdhe521keyexchangesrate Value 
	'''
	@sslecdhe521keyexchangesrate.setter
	def sslecdhe521keyexchangesrate(self,sslecdhe521keyexchangesrate):
		try :
			if not isinstance(sslecdhe521keyexchangesrate,float):
				raise TypeError("sslecdhe521keyexchangesrate must be set to float value")
			self._sslecdhe521keyexchangesrate = sslecdhe521keyexchangesrate
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
	get sslbersa2048keyexchangesrate Value 
	'''
	@property
	def sslbersa2048keyexchangesrate(self) :
		try:
			return self._sslbersa2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbersa2048keyexchangesrate Value 
	'''
	@sslbersa2048keyexchangesrate.setter
	def sslbersa2048keyexchangesrate(self,sslbersa2048keyexchangesrate):
		try :
			if not isinstance(sslbersa2048keyexchangesrate,float):
				raise TypeError("sslbersa2048keyexchangesrate must be set to float value")
			self._sslbersa2048keyexchangesrate = sslbersa2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslrsa1024keyexchangesrate Value
	'''
	@property
	def sslrsa1024keyexchangesrate(self) :
		try:
			return self._sslrsa1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslrsa1024keyexchangesrate Value
	'''
	@sslrsa1024keyexchangesrate.setter
	def sslrsa1024keyexchangesrate(self,sslrsa1024keyexchangesrate):
		try :
			if not isinstance(sslrsa1024keyexchangesrate,float):
				raise TypeError("sslrsa1024keyexchangesrate must be set to float value")
			self._sslrsa1024keyexchangesrate = sslrsa1024keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslbedh1024keyexchangesrate Value 
	'''
	@property
	def sslbedh1024keyexchangesrate(self) :
		try:
			return self._sslbedh1024keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslbedh1024keyexchangesrate Value 
	'''
	@sslbedh1024keyexchangesrate.setter
	def sslbedh1024keyexchangesrate(self,sslbedh1024keyexchangesrate):
		try :
			if not isinstance(sslbedh1024keyexchangesrate,float):
				raise TypeError("sslbedh1024keyexchangesrate must be set to float value")
			self._sslbedh1024keyexchangesrate = sslbedh1024keyexchangesrate
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
	get sslrsa2048keyexchangesrate Value 
	'''
	@property
	def sslrsa2048keyexchangesrate(self) :
		try:
			return self._sslrsa2048keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslrsa2048keyexchangesrate Value 
	'''
	@sslrsa2048keyexchangesrate.setter
	def sslrsa2048keyexchangesrate(self,sslrsa2048keyexchangesrate):
		try :
			if not isinstance(sslrsa2048keyexchangesrate,float):
				raise TypeError("sslrsa2048keyexchangesrate must be set to float value")
			self._sslrsa2048keyexchangesrate = sslrsa2048keyexchangesrate
		except Exception as e :
			raise e


	'''
	get sslecdhe224keyexchangesrate Value 
	'''
	@property
	def sslecdhe224keyexchangesrate(self) :
		try:
			return self._sslecdhe224keyexchangesrate
		except Exception as e :
			raise e
	'''
	set sslecdhe224keyexchangesrate Value 
	'''
	@sslecdhe224keyexchangesrate.setter
	def sslecdhe224keyexchangesrate(self,sslecdhe224keyexchangesrate):
		try :
			if not isinstance(sslecdhe224keyexchangesrate,float):
				raise TypeError("sslecdhe224keyexchangesrate must be set to float value")
			self._sslecdhe224keyexchangesrate = sslecdhe224keyexchangesrate
		except Exception as e :
			raise e

	'''
	Use this operation to get SSL CPU utilization vs key exchange metric statistics.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_ssl_cpu_keyexchange_report_obj=perf_ssl_cpu_keyexchange_report()
				response = perf_ssl_cpu_keyexchange_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_ssl_cpu_keyexchange_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_ssl_cpu_keyexchange_report_obj = perf_ssl_cpu_keyexchange_report()
			option_ = options()
			option_._filter=filter_
			return perf_ssl_cpu_keyexchange_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_ssl_cpu_keyexchange_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_ssl_cpu_keyexchange_report_obj = perf_ssl_cpu_keyexchange_report()
			option_ = options()
			option_._count=True
			response = perf_ssl_cpu_keyexchange_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_ssl_cpu_keyexchange_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_ssl_cpu_keyexchange_report_obj = perf_ssl_cpu_keyexchange_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_ssl_cpu_keyexchange_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_ssl_cpu_keyexchange_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_ssl_cpu_keyexchange_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_ssl_cpu_keyexchange_report_responses, response, "perf_ssl_cpu_keyexchange_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_ssl_cpu_keyexchange_report_response_array
				i=0
				error = [perf_ssl_cpu_keyexchange_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_ssl_cpu_keyexchange_report_response_array
			i=0
			perf_ssl_cpu_keyexchange_report_objs = [perf_ssl_cpu_keyexchange_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_ssl_cpu_keyexchange_report'):
					for props in obj._perf_ssl_cpu_keyexchange_report:
						result = service.payload_formatter.string_to_bulk_resource(perf_ssl_cpu_keyexchange_report_response,self.__class__.__name__,props)
						perf_ssl_cpu_keyexchange_report_objs[i] = result.perf_ssl_cpu_keyexchange_report
						i=i+1
			return perf_ssl_cpu_keyexchange_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_ssl_cpu_keyexchange_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_ssl_cpu_keyexchange_report_response(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_cpu_keyexchange_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_ssl_cpu_keyexchange_report= [ perf_ssl_cpu_keyexchange_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_ssl_cpu_keyexchange_report_responses(base_response):
	def __init__(self,length=1) :
		self.perf_ssl_cpu_keyexchange_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_ssl_cpu_keyexchange_report_response_array = [ perf_ssl_cpu_keyexchange_report() for _ in range(length)]
