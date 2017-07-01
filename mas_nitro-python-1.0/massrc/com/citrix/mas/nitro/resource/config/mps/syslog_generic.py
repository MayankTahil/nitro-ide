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
Configuration for Syslog generic table resource
'''

class syslog_generic(base_resource):
	_source= ""
	_device_family= ""
	_event_id= ""
	_system_name= ""
	_full_message= ""
	_isparsed= ""
	_ttime= ""
	_device_type= ""
	_host_name= ""
	_id= ""
	_type= ""
	_syslog_msg= ""
	_severity= ""
	_module= ""
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
			return "syslog_generic"
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
			return "syslog_generics"
		except Exception as e :
			raise e



	'''
	get source.
	'''
	@property
	def source(self) :
		try:
			return self._source
		except Exception as e :
			raise e


	'''
	get Device family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e


	'''
	get <TODO>
	'''
	@property
	def event_id(self) :
		try:
			return self._event_id
		except Exception as e :
			raise e


	'''
	get Device System Name
	'''
	@property
	def system_name(self) :
		try:
			return self._system_name
		except Exception as e :
			raise e


	'''
	get Syslog original Message.
	'''
	@property
	def full_message(self) :
		try:
			return self._full_message
		except Exception as e :
			raise e


	'''
	get Whethersyslog message is parsed successfully or not
	'''
	@property
	def isparsed(self) :
		try:
			return self._isparsed
		except Exception as e :
			raise e


	'''
	get ttime
	'''
	@property
	def ttime(self) :
		try:
			return self._ttime
		except Exception as e :
			raise e


	'''
	get Device Type
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
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
	get Id is system generated key for all the syslog generic record.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the syslog generic record.
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
	get Type Name.
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e


	'''
	get Syslog original Message.
	'''
	@property
	def syslog_msg(self) :
		try:
			return self._syslog_msg
		except Exception as e :
			raise e


	'''
	get severity
	'''
	@property
	def severity(self) :
		try:
			return self._severity
		except Exception as e :
			raise e


	'''
	get Module Name.
	'''
	@property
	def module(self) :
		try:
			return self._module
		except Exception as e :
			raise e

	'''
	Report for generic syslog message received by this collector..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				syslog_generic_obj=syslog_generic()
				response = syslog_generic_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_generic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_generic_obj = syslog_generic()
			option_ = options()
			option_._filter=filter_
			return syslog_generic_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_generic resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_generic_obj = syslog_generic()
			option_ = options()
			option_._count=True
			response = syslog_generic_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_generic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_generic_obj = syslog_generic()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_generic_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_generic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_generic
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_generic_responses, response, "syslog_generic_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_generic_response_array
				i=0
				error = [syslog_generic() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_generic_response_array
			i=0
			syslog_generic_objs = [syslog_generic() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_generic'):
					for props in obj._syslog_generic:
						result = service.payload_formatter.string_to_bulk_resource(syslog_generic_response,self.__class__.__name__,props)
						syslog_generic_objs[i] = result.syslog_generic
						i=i+1
			return syslog_generic_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_generic,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_generic_response(base_response):
	def __init__(self,length=1) :
		self.syslog_generic= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_generic= [ syslog_generic() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_generic_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_generic_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_generic_response_array = [ syslog_generic() for _ in range(length)]
