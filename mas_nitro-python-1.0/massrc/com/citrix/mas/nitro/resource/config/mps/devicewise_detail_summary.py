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

class devicewise_detail_summary(base_resource):
	_is_agent= ""
	_memory_usage= ""
	_agent_ip_address= ""
	_total_events= ""
	_cityname= ""
	_tenant_id= ""
	_agent_name= ""
	_agent_id= ""
	_vm_cpu_usage= ""
	_throughput= ""
	_ip_address= ""
	_instance_state= ""
	_type= ""
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
			return "devicewise_detail_summary"
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
			return "devicewise_detail_summarys"
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
	get memory usage of a device
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e
	'''
	set memory usage of a device
	'''
	@memory_usage.setter
	def memory_usage(self,memory_usage):
		try :
			if not isinstance(memory_usage,float):
				raise TypeError("memory_usage must be set to float value")
			self._memory_usage = memory_usage
		except Exception as e :
			raise e


	'''
	get Total number of devices deployed city wise..
	'''
	@property
	def agent_ip_address(self) :
		try:
			return self._agent_ip_address
		except Exception as e :
			raise e


	'''
	get Total minor events.
	'''
	@property
	def total_events(self) :
		try:
			return self._total_events
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
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Agent Name
	'''
	@property
	def agent_name(self) :
		try:
			return self._agent_name
		except Exception as e :
			raise e
	'''
	set Agent Name
	'''
	@agent_name.setter
	def agent_name(self,agent_name):
		try :
			if not isinstance(agent_name,str):
				raise TypeError("agent_name must be set to str value")
			self._agent_name = agent_name
		except Exception as e :
			raise e


	'''
	get Agent Id
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Agent Id
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of VM Instance
	'''
	@property
	def vm_cpu_usage(self) :
		try:
			return self._vm_cpu_usage
		except Exception as e :
			raise e


	'''
	get Assign throughput in Mbps to VM Instance
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set Assign throughput in Mbps to VM Instance
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,float):
				raise TypeError("throughput must be set to float value")
			self._throughput = throughput
		except Exception as e :
			raise e


	'''
	get Total number of devices deployed city wise..
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
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
	Type of device, (Xen | NS)
	'''
	@property
	def type(self):
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	Type of device, (Xen | NS)
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
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
				devicewise_detail_summary_obj=devicewise_detail_summary()
				response = devicewise_detail_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of devicewise_detail_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			devicewise_detail_summary_obj = devicewise_detail_summary()
			option_ = options()
			option_._filter=filter_
			return devicewise_detail_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the devicewise_detail_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			devicewise_detail_summary_obj = devicewise_detail_summary()
			option_ = options()
			option_._count=True
			response = devicewise_detail_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of devicewise_detail_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			devicewise_detail_summary_obj = devicewise_detail_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = devicewise_detail_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(devicewise_detail_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.devicewise_detail_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(devicewise_detail_summary_responses, response, "devicewise_detail_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.devicewise_detail_summary_response_array
				i=0
				error = [devicewise_detail_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.devicewise_detail_summary_response_array
			i=0
			devicewise_detail_summary_objs = [devicewise_detail_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_devicewise_detail_summary'):
					for props in obj._devicewise_detail_summary:
						result = service.payload_formatter.string_to_bulk_resource(devicewise_detail_summary_response,self.__class__.__name__,props)
						devicewise_detail_summary_objs[i] = result.devicewise_detail_summary
						i=i+1
			return devicewise_detail_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(devicewise_detail_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class devicewise_detail_summary_response(base_response):
	def __init__(self,length=1) :
		self.devicewise_detail_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.devicewise_detail_summary= [ devicewise_detail_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class devicewise_detail_summary_responses(base_response):
	def __init__(self,length=1) :
		self.devicewise_detail_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.devicewise_detail_summary_response_array = [ devicewise_detail_summary() for _ in range(length)]
