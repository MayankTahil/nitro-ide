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
Configuration for Event Mgmt Entity State Changes Report resource
'''

class event_entity_state_changes_report(base_resource):
	_category= ""
	_ip_address= ""
	_total_count= ""
	_hostname= ""
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
			return "event_entity_state_changes_report"
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
			return "event_entity_state_changes_reports"
		except Exception as e :
			raise e



	'''
	get category
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e
	'''
	set category
	'''
	@category.setter
	def category(self,category):
		try :
			if not isinstance(category,str):
				raise TypeError("category must be set to str value")
			self._category = category
		except Exception as e :
			raise e


	'''
	get IP Address of the device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address of the device
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
	get Total event count for this device in given sampled timeframe.
	'''
	@property
	def total_count(self) :
		try:
			return self._total_count
		except Exception as e :
			raise e
	'''
	set Total event count for this device in given sampled timeframe.
	'''
	@total_count.setter
	def total_count(self,total_count):
		try :
			if not isinstance(total_count,int):
				raise TypeError("total_count must be set to int value")
			self._total_count = total_count
		except Exception as e :
			raise e

	'''
	Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def hostname(self):
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e

	'''
	Use this operation to get Event entity state changes report data.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				event_entity_state_changes_report_obj=event_entity_state_changes_report()
				response = event_entity_state_changes_report_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of event_entity_state_changes_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			event_entity_state_changes_report_obj = event_entity_state_changes_report()
			option_ = options()
			option_._filter=filter_
			return event_entity_state_changes_report_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the event_entity_state_changes_report resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			event_entity_state_changes_report_obj = event_entity_state_changes_report()
			option_ = options()
			option_._count=True
			response = event_entity_state_changes_report_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of event_entity_state_changes_report resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			event_entity_state_changes_report_obj = event_entity_state_changes_report()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = event_entity_state_changes_report_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(event_entity_state_changes_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.event_entity_state_changes_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(event_entity_state_changes_report_responses, response, "event_entity_state_changes_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.event_entity_state_changes_report_response_array
				i=0
				error = [event_entity_state_changes_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.event_entity_state_changes_report_response_array
			i=0
			event_entity_state_changes_report_objs = [event_entity_state_changes_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_event_entity_state_changes_report'):
					for props in obj._event_entity_state_changes_report:
						result = service.payload_formatter.string_to_bulk_resource(event_entity_state_changes_report_response,self.__class__.__name__,props)
						event_entity_state_changes_report_objs[i] = result.event_entity_state_changes_report
						i=i+1
			return event_entity_state_changes_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(event_entity_state_changes_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class event_entity_state_changes_report_response(base_response):
	def __init__(self,length=1) :
		self.event_entity_state_changes_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.event_entity_state_changes_report= [ event_entity_state_changes_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class event_entity_state_changes_report_responses(base_response):
	def __init__(self,length=1) :
		self.event_entity_state_changes_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.event_entity_state_changes_report_response_array = [ event_entity_state_changes_report() for _ in range(length)]
