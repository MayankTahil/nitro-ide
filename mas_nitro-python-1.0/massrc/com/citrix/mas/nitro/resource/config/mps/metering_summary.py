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
Configuration for Metering Data Summary resource
'''

class metering_summary(base_resource):
	_max_burst= ""
	_min_rx= ""
	_start_time= ""
	_duration= ""
	_number_of_bursts= ""
	_total_txmbits= ""
	_total_rxmbits= ""
	_end_time= ""
	_max_rx= ""
	_max_tx= ""
	_min_tx= ""
	_ip_address= ""
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
			return "metering_summary"
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
			return "metering_summarys"
		except Exception as e :
			raise e



	'''
	get Maximum Burst Throughput of VM Instance for Interval in Mbps
	'''
	@property
	def max_burst(self) :
		try:
			return self._max_burst
		except Exception as e :
			raise e


	'''
	get Minimum In Throughput of VM Instance for Interval in Mbps
	'''
	@property
	def min_rx(self) :
		try:
			return self._min_rx
		except Exception as e :
			raise e


	'''
	get Start Time of interval for which summary is generated
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e


	'''
	get Interval Duration for which summary is generated
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e


	'''
	get Number of bursts by VM Instance in Interval
	'''
	@property
	def number_of_bursts(self) :
		try:
			return self._number_of_bursts
		except Exception as e :
			raise e
	'''
	set Number of bursts by VM Instance in Interval
	'''
	@number_of_bursts.setter
	def number_of_bursts(self,number_of_bursts):
		try :
			if not isinstance(number_of_bursts,int):
				raise TypeError("number_of_bursts must be set to int value")
			self._number_of_bursts = number_of_bursts
		except Exception as e :
			raise e


	'''
	get Out Total Rx of VM Instance for Interval in Mbits
	'''
	@property
	def total_txmbits(self) :
		try:
			return self._total_txmbits
		except Exception as e :
			raise e


	'''
	get In Total Rx of VM Instance for Interval in Mbits
	'''
	@property
	def total_rxmbits(self) :
		try:
			return self._total_rxmbits
		except Exception as e :
			raise e


	'''
	get End Time of interval for which summary is generated
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e


	'''
	get Maximum In Throughput of VM Instance for Interval in Mbps
	'''
	@property
	def max_rx(self) :
		try:
			return self._max_rx
		except Exception as e :
			raise e


	'''
	get Maximum Out Throughput of VM Instance for Interval in Mbps
	'''
	@property
	def max_tx(self) :
		try:
			return self._max_tx
		except Exception as e :
			raise e


	'''
	get Minimum Out Throughput of VM Instance for Interval in Mbps
	'''
	@property
	def min_tx(self) :
		try:
			return self._min_tx
		except Exception as e :
			raise e


	'''
	get IP Address for this VM device for which metering data summary is required
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for this VM device for which metering data summary is required
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
	Use this operation to get metering data summary.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				metering_summary_obj=metering_summary()
				response = metering_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of metering_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			metering_summary_obj = metering_summary()
			option_ = options()
			option_._filter=filter_
			return metering_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the metering_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			metering_summary_obj = metering_summary()
			option_ = options()
			option_._count=True
			response = metering_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of metering_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			metering_summary_obj = metering_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = metering_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(metering_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.metering_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(metering_summary_responses, response, "metering_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.metering_summary_response_array
				i=0
				error = [metering_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.metering_summary_response_array
			i=0
			metering_summary_objs = [metering_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_metering_summary'):
					for props in obj._metering_summary:
						result = service.payload_formatter.string_to_bulk_resource(metering_summary_response,self.__class__.__name__,props)
						metering_summary_objs[i] = result.metering_summary
						i=i+1
			return metering_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(metering_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class metering_summary_response(base_response):
	def __init__(self,length=1) :
		self.metering_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.metering_summary= [ metering_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class metering_summary_responses(base_response):
	def __init__(self,length=1) :
		self.metering_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.metering_summary_response_array = [ metering_summary() for _ in range(length)]
