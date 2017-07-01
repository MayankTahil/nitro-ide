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
Configuration for SDWAN-WO send compression ratio resource
'''

class perf_wsdevice_send_compression_ratio_report(base_resource):
	_sendcompressionratio= ""
	_timestamp= ""
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
			return "perf_wsdevice_send_compression_ratio_report"
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
			return "perf_wsdevice_send_compression_ratio_reports"
		except Exception as e :
			raise e



	'''
	get Send compression ratio
	'''
	@property
	def sendcompressionratio(self) :
		try:
			return self._sendcompressionratio
		except Exception as e :
			raise e
	'''
	set Send compression ratio
	'''
	@sendcompressionratio.setter
	def sendcompressionratio(self,sendcompressionratio):
		try :
			if not isinstance(sendcompressionratio,float):
				raise TypeError("sendcompressionratio must be set to float value")
			self._sendcompressionratio = sendcompressionratio
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
	Use this operation to get SDWAN-WO Send compression ratio information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_wsdevice_send_compression_ratio_report_obj=perf_wsdevice_send_compression_ratio_report()
				response = perf_wsdevice_send_compression_ratio_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_wsdevice_send_compression_ratio_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_wsdevice_send_compression_ratio_report_obj = perf_wsdevice_send_compression_ratio_report()
			option_ = options()
			option_._filter=filter_
			return perf_wsdevice_send_compression_ratio_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_wsdevice_send_compression_ratio_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_wsdevice_send_compression_ratio_report_obj = perf_wsdevice_send_compression_ratio_report()
			option_ = options()
			option_._count=True
			response = perf_wsdevice_send_compression_ratio_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_wsdevice_send_compression_ratio_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_wsdevice_send_compression_ratio_report_obj = perf_wsdevice_send_compression_ratio_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_wsdevice_send_compression_ratio_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_wsdevice_send_compression_ratio_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_wsdevice_send_compression_ratio_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_wsdevice_send_compression_ratio_report_responses, response, "perf_wsdevice_send_compression_ratio_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_wsdevice_send_compression_ratio_report_response_array
				i=0
				error = [perf_wsdevice_send_compression_ratio_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_wsdevice_send_compression_ratio_report_response_array
			i=0
			perf_wsdevice_send_compression_ratio_report_objs = [perf_wsdevice_send_compression_ratio_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_wsdevice_send_compression_ratio_report'):
					for props in obj._perf_wsdevice_send_compression_ratio_report:
						result = service.payload_formatter.string_to_bulk_resource(perf_wsdevice_send_compression_ratio_report_response,self.__class__.__name__,props)
						perf_wsdevice_send_compression_ratio_report_objs[i] = result.perf_wsdevice_send_compression_ratio_report
						i=i+1
			return perf_wsdevice_send_compression_ratio_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_wsdevice_send_compression_ratio_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_wsdevice_send_compression_ratio_report_response(base_response):
	def __init__(self,length=1) :
		self.perf_wsdevice_send_compression_ratio_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_wsdevice_send_compression_ratio_report= [ perf_wsdevice_send_compression_ratio_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_wsdevice_send_compression_ratio_report_responses(base_response):
	def __init__(self,length=1) :
		self.perf_wsdevice_send_compression_ratio_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_wsdevice_send_compression_ratio_report_response_array = [ perf_wsdevice_send_compression_ratio_report() for _ in range(length)]
