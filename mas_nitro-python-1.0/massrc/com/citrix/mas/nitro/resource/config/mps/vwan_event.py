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
Configuration for VWAN EVENT resource
'''

class vwan_event(base_resource):
	_source= ""
	_wan_link_state= ""
	_virtual_path= ""
	_status_message= ""
	_rpt_sample_time= ""
	_virtual_path_state= ""
	_message= ""
	_host_name= ""
	_type= ""
	_id= ""
	_category= ""
	_severity= ""
	_wan_link= ""
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
			return "vwan_event"
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
			return "vwan_events"
		except Exception as e :
			raise e



	'''
	get Source
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e


	'''
	get Internal Event ID used in the source device.
	'''
	@property
	def wan_link_state(self) :
		try:
			return self._wan_link_state
		except Exception as e :
			raise e


	'''
	get Operation Type
	'''
	@property
	def virtual_path(self) :
		try:
			return self._virtual_path
		except Exception as e :
			raise e


	'''
	get status_message
	'''
	@property
	def status_message(self) :
		try:
			return self._status_message
		except Exception as e :
			raise e


	'''
	get Event Time
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e


	'''
	get virtual_path_state
	'''
	@property
	def virtual_path_state(self) :
		try:
			return self._virtual_path_state
		except Exception as e :
			raise e


	'''
	get VWAN Event_Message
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e


	'''
	get Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def host_name(self) :
		try:
			return self._host_name
		except Exception as e :
			raise e


	'''
	get type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the events
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the events
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
	get Category of VWAN Event
	'''
	@property
	def category(self) :
		try:
			return self._category
		except Exception as e :
			raise e


	'''
	get Severity of Vwan Event
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e


	'''
	get WAN Link
	'''
	@property
	def wan_link(self) :
		try:
			return self._wan_link
		except Exception as e :
			raise e

	'''
	Use this operation to get events.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vwan_event_obj=vwan_event()
				response = vwan_event_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vwan_event resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vwan_event_obj = vwan_event()
			option_ = options()
			option_._filter=filter_
			return vwan_event_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vwan_event resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vwan_event_obj = vwan_event()
			option_ = options()
			option_._count=True
			response = vwan_event_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vwan_event resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vwan_event_obj = vwan_event()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vwan_event_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vwan_event_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vwan_event
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vwan_event_responses, response, "vwan_event_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vwan_event_response_array
				i=0
				error = [vwan_event() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vwan_event_response_array
			i=0
			vwan_event_objs = [vwan_event() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vwan_event'):
					for props in obj._vwan_event:
						result = service.payload_formatter.string_to_bulk_resource(vwan_event_response,self.__class__.__name__,props)
						vwan_event_objs[i] = result.vwan_event
						i=i+1
			return vwan_event_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vwan_event,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vwan_event_response(base_response):
	def __init__(self,length=1) :
		self.vwan_event= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vwan_event= [ vwan_event() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vwan_event_responses(base_response):
	def __init__(self,length=1) :
		self.vwan_event_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vwan_event_response_array = [ vwan_event() for _ in range(length)]
