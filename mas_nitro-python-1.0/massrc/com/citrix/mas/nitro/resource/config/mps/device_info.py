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
from massrc.com.citrix.mas.nitro.resource.config.mps.anomaly_item import anomaly_item


'''
Configuration for device_info Resource resource
'''

class device_info(base_resource):
	_report_end_time= ""
	_anomaly_data=[]
	_rpt_sample_time= ""
	_duration= ""
	_anomaly_count= ""
	_device_name= ""
	_report_start_time= ""
	_id= ""
	_server_ip= ""
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
			return "device_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._server_ip
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
			return "device_infos"
		except Exception as e :
			raise e



	'''
	get report_end_time for getting the logs in milliseconds
	'''
	@property
	def report_end_time(self) :
		try:
			return self._report_end_time
		except Exception as e :
			raise e
	'''
	set report_end_time for getting the logs in milliseconds
	'''
	@report_end_time.setter
	def report_end_time(self,report_end_time):
		try :
			if not isinstance(report_end_time,float):
				raise TypeError("report_end_time must be set to float value")
			self._report_end_time = report_end_time
		except Exception as e :
			raise e


	'''
	get List of anomalous values and their timestamp
	'''
	@property
	def anomaly_data(self) :
		try:
			return self._anomaly_data
		except Exception as e :
			raise e
	'''
	set List of anomalous values and their timestamp
	'''
	@anomaly_data.setter
	def anomaly_data(self,anomaly_data) :
		try :
			if not isinstance(anomaly_data,list):
				raise TypeError("anomaly_data must be set to array of anomaly_item value")
			for item in anomaly_data :
				if not isinstance(item,anomaly_item):
					raise TypeError("item must be set to anomaly_item value")
			self._anomaly_data = anomaly_data
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set 
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,float):
				raise TypeError("rpt_sample_time must be set to float value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e


	'''
	get Calculation frequency period daily,weekly etc
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Calculation frequency period daily,weekly etc
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get Number of anomalies
	'''
	@property
	def anomaly_count(self) :
		try:
			return self._anomaly_count
		except Exception as e :
			raise e
	'''
	set Number of anomalies
	'''
	@anomaly_count.setter
	def anomaly_count(self,anomaly_count):
		try :
			if not isinstance(anomaly_count,int):
				raise TypeError("anomaly_count must be set to int value")
			self._anomaly_count = anomaly_count
		except Exception as e :
			raise e


	'''
	get Name of the Device
	'''
	@property
	def device_name(self) :
		try:
			return self._device_name
		except Exception as e :
			raise e
	'''
	set Name of the Device
	'''
	@device_name.setter
	def device_name(self,device_name):
		try :
			if not isinstance(device_name,str):
				raise TypeError("device_name must be set to str value")
			self._device_name = device_name
		except Exception as e :
			raise e


	'''
	get report_start_time for getting the logs in milliseconds
	'''
	@property
	def report_start_time(self) :
		try:
			return self._report_start_time
		except Exception as e :
			raise e
	'''
	set report_start_time for getting the logs in milliseconds
	'''
	@report_start_time.setter
	def report_start_time(self,report_start_time):
		try :
			if not isinstance(report_start_time,float):
				raise TypeError("report_start_time must be set to float value")
			self._report_start_time = report_start_time
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get Device IP Address
	'''
	@property
	def server_ip(self) :
		try:
			return self._server_ip
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@server_ip.setter
	def server_ip(self,server_ip):
		try :
			if not isinstance(server_ip,str):
				raise TypeError("server_ip must be set to str value")
			self._server_ip = server_ip
		except Exception as e :
			raise e

	'''
	Use this operation to get anomalies.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_info_obj=device_info()
				response = device_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_info_obj = device_info()
			option_ = options()
			option_._filter=filter_
			return device_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_info_obj = device_info()
			option_ = options()
			option_._count=True
			response = device_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_info_obj = device_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_info_responses, response, "device_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_info_response_array
				i=0
				error = [device_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_info_response_array
			i=0
			device_info_objs = [device_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_info'):
					for props in obj._device_info:
						result = service.payload_formatter.string_to_bulk_resource(device_info_response,self.__class__.__name__,props)
						device_info_objs[i] = result.device_info
						i=i+1
			return device_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_info_response(base_response):
	def __init__(self,length=1) :
		self.device_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_info= [ device_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_info_responses(base_response):
	def __init__(self,length=1) :
		self.device_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_info_response_array = [ device_info() for _ in range(length)]
