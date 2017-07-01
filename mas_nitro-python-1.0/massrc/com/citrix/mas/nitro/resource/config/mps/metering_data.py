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
Configuration for Metering Data for VM Devices resource
'''

class metering_data(base_resource):
	_interval_txmbits= ""
	_burst_thpt= ""
	_tx= ""
	_rx= ""
	_start_time= ""
	_min_thpt= ""
	_interval_rxmbits= ""
	_poll_time= ""
	_max_thpt_limit= ""
	_total_txmbits= ""
	_thpt_limit= ""
	_total_rxmbits= ""
	_id= ""
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
			return "metering_data"
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
			return "metering_datas"
		except Exception as e :
			raise e



	'''
	get Out Tx of VM Instance for Interval in Mbits
	'''
	@property
	def interval_txmbits(self) :
		try:
			return self._interval_txmbits
		except Exception as e :
			raise e


	'''
	get Burst Throughput of VM Instance in Mbps
	'''
	@property
	def burst_thpt(self) :
		try:
			return self._burst_thpt
		except Exception as e :
			raise e


	'''
	get Out Throughput of VM Instance in Mbps
	'''
	@property
	def tx(self) :
		try:
			return self._tx
		except Exception as e :
			raise e


	'''
	get In Throughput of VM Instance in Mbps
	'''
	@property
	def rx(self) :
		try:
			return self._rx
		except Exception as e :
			raise e


	'''
	get Start Time of Interval for which data was recorded
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e


	'''
	get Minimum Throughput allocated to Instance in Mbps
	'''
	@property
	def min_thpt(self) :
		try:
			return self._min_thpt
		except Exception as e :
			raise e


	'''
	get In Rx of VM Instance for Interval in Mbits
	'''
	@property
	def interval_rxmbits(self) :
		try:
			return self._interval_rxmbits
		except Exception as e :
			raise e


	'''
	get Poll Time at which data was recorded
	'''
	@property
	def poll_time(self) :
		try:
			return self._poll_time
		except Exception as e :
			raise e


	'''
	get Maximum Throughput Limit allowed for VM Instance in Mbps
	'''
	@property
	def max_thpt_limit(self) :
		try:
			return self._max_thpt_limit
		except Exception as e :
			raise e


	'''
	get Out Total Rx of VM Instance in Mbits
	'''
	@property
	def total_txmbits(self) :
		try:
			return self._total_txmbits
		except Exception as e :
			raise e


	'''
	get Throughput Limit configured for VM Instance in Mbps
	'''
	@property
	def thpt_limit(self) :
		try:
			return self._thpt_limit
		except Exception as e :
			raise e


	'''
	get In Total Rx of VM Instance in Mbits
	'''
	@property
	def total_rxmbits(self) :
		try:
			return self._total_rxmbits
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the metering data points
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the metering data points
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
	IP Address for this VM device for which data is recorded
	'''
	@property
	def ip_address(self):
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	IP Address for this VM device for which data is recorded
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
	Use this operation to get metering data.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				metering_data_obj=metering_data()
				response = metering_data_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of metering_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			metering_data_obj = metering_data()
			option_ = options()
			option_._filter=filter_
			return metering_data_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the metering_data resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			metering_data_obj = metering_data()
			option_ = options()
			option_._count=True
			response = metering_data_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of metering_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			metering_data_obj = metering_data()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = metering_data_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(metering_data_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.metering_data
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(metering_data_responses, response, "metering_data_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.metering_data_response_array
				i=0
				error = [metering_data() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.metering_data_response_array
			i=0
			metering_data_objs = [metering_data() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_metering_data'):
					for props in obj._metering_data:
						result = service.payload_formatter.string_to_bulk_resource(metering_data_response,self.__class__.__name__,props)
						metering_data_objs[i] = result.metering_data
						i=i+1
			return metering_data_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(metering_data,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class metering_data_response(base_response):
	def __init__(self,length=1) :
		self.metering_data= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.metering_data= [ metering_data() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class metering_data_responses(base_response):
	def __init__(self,length=1) :
		self.metering_data_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.metering_data_response_array = [ metering_data() for _ in range(length)]
