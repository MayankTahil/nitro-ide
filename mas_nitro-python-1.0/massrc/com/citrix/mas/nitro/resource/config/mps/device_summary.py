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
Configuration for City wise devices summary resource
'''

class device_summary(base_resource):
	_total_critical_events= ""
	_longitude= ""
	_total_devices_outofservice= ""
	_total_major_events= ""
	_total_events= ""
	_cityname= ""
	_total_agents_outofservice= ""
	_tenant_id= ""
	_total_agents_up= ""
	_total_number_of_devices= ""
	_total_devices_down= ""
	_latitude= ""
	_total_devices_up= ""
	_total_number_of_agents= ""
	_total_agents_down= ""
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
			return "device_summary"
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
			return "device_summarys"
		except Exception as e :
			raise e



	'''
	get Total Critical events city wise.
	'''
	@property
	def total_critical_events(self) :
		try:
			return self._total_critical_events
		except Exception as e :
			raise e


	'''
	get longitude of the city
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e


	'''
	get Total devices out of service city wise.
	'''
	@property
	def total_devices_outofservice(self) :
		try:
			return self._total_devices_outofservice
		except Exception as e :
			raise e


	'''
	get Total major events.
	'''
	@property
	def total_major_events(self) :
		try:
			return self._total_major_events
		except Exception as e :
			raise e


	'''
	get Total events city wise.
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
	get Total agents out of service city wise.
	'''
	@property
	def total_agents_outofservice(self) :
		try:
			return self._total_agents_outofservice
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
	get Total agents up city wise.
	'''
	@property
	def total_agents_up(self) :
		try:
			return self._total_agents_up
		except Exception as e :
			raise e


	'''
	get Total number of devices deployed city wise..
	'''
	@property
	def total_number_of_devices(self) :
		try:
			return self._total_number_of_devices
		except Exception as e :
			raise e


	'''
	get Total agents down city wise.
	'''
	@property
	def total_devices_down(self) :
		try:
			return self._total_devices_down
		except Exception as e :
			raise e


	'''
	get latitude of the city
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e


	'''
	get Total agents down city wise.
	'''
	@property
	def total_devices_up(self) :
		try:
			return self._total_devices_up
		except Exception as e :
			raise e


	'''
	get Total number of agents deployed city wise.
	'''
	@property
	def total_number_of_agents(self) :
		try:
			return self._total_number_of_agents
		except Exception as e :
			raise e


	'''
	get Total agents down city wise.
	'''
	@property
	def total_agents_down(self) :
		try:
			return self._total_agents_down
		except Exception as e :
			raise e

	'''
	Use this operation to get device summary report.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				device_summary_obj=device_summary()
				response = device_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of device_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			device_summary_obj = device_summary()
			option_ = options()
			option_._filter=filter_
			return device_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the device_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			device_summary_obj = device_summary()
			option_ = options()
			option_._count=True
			response = device_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of device_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			device_summary_obj = device_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = device_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(device_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_summary_responses, response, "device_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_summary_response_array
				i=0
				error = [device_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_summary_response_array
			i=0
			device_summary_objs = [device_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_summary'):
					for props in obj._device_summary:
						result = service.payload_formatter.string_to_bulk_resource(device_summary_response,self.__class__.__name__,props)
						device_summary_objs[i] = result.device_summary
						i=i+1
			return device_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_summary_response(base_response):
	def __init__(self,length=1) :
		self.device_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_summary= [ device_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_summary_responses(base_response):
	def __init__(self,length=1) :
		self.device_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_summary_response_array = [ device_summary() for _ in range(length)]
