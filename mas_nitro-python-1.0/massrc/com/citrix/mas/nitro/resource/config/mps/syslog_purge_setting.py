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
from massrc.com.citrix.mas.nitro.resource.config.mps.syslog_purge_setting_details import syslog_purge_setting_details


'''
Configuration for Syslog Purge Setting resource
'''

class syslog_purge_setting(base_resource):
	_purge_interval_for_appfw_data= ""
	_id= ""
	_details=[]
	_purge_interval_for_generic_data= ""
	_purge_interval_for_gateway_data= ""
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
			return "syslog_purge_setting"
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
			return "syslog_purge_settings"
		except Exception as e :
			raise e



	'''
	get purge_interval_for_appfw_data
	'''
	@property
	def purge_interval_for_appfw_data(self) :
		try:
			return self._purge_interval_for_appfw_data
		except Exception as e :
			raise e
	'''
	set purge_interval_for_appfw_data
	'''
	@purge_interval_for_appfw_data.setter
	def purge_interval_for_appfw_data(self,purge_interval_for_appfw_data):
		try :
			if not isinstance(purge_interval_for_appfw_data,int):
				raise TypeError("purge_interval_for_appfw_data must be set to int value")
			self._purge_interval_for_appfw_data = purge_interval_for_appfw_data
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
	get Syslog Purge Setting Details
	'''
	@property
	def details(self) :
		try:
			return self._details
		except Exception as e :
			raise e
	'''
	set Syslog Purge Setting Details
	'''
	@details.setter
	def details(self,details) :
		try :
			if not isinstance(details,list):
				raise TypeError("details must be set to array of syslog_purge_setting_details value")
			for item in details :
				if not isinstance(item,syslog_purge_setting_details):
					raise TypeError("item must be set to syslog_purge_setting_details value")
			self._details = details
		except Exception as e :
			raise e


	'''
	get purge_interval_for_generic_data
	'''
	@property
	def purge_interval_for_generic_data(self) :
		try:
			return self._purge_interval_for_generic_data
		except Exception as e :
			raise e
	'''
	set purge_interval_for_generic_data
	'''
	@purge_interval_for_generic_data.setter
	def purge_interval_for_generic_data(self,purge_interval_for_generic_data):
		try :
			if not isinstance(purge_interval_for_generic_data,int):
				raise TypeError("purge_interval_for_generic_data must be set to int value")
			self._purge_interval_for_generic_data = purge_interval_for_generic_data
		except Exception as e :
			raise e


	'''
	get purge_interval_for_gateway_data.
	'''
	@property
	def purge_interval_for_gateway_data(self) :
		try:
			return self._purge_interval_for_gateway_data
		except Exception as e :
			raise e
	'''
	set purge_interval_for_gateway_data.
	'''
	@purge_interval_for_gateway_data.setter
	def purge_interval_for_gateway_data(self,purge_interval_for_gateway_data):
		try :
			if not isinstance(purge_interval_for_gateway_data,int):
				raise TypeError("purge_interval_for_gateway_data must be set to int value")
			self._purge_interval_for_gateway_data = purge_interval_for_gateway_data
		except Exception as e :
			raise e

	'''
	Use this operation to get syslog purge settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				syslog_purge_setting_obj=syslog_purge_setting()
				response = syslog_purge_setting_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify syslog purge settings.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				syslog_purge_setting_obj=syslog_purge_setting()
				return cls.update_bulk_request(client,resource,syslog_purge_setting_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_purge_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_purge_setting_obj = syslog_purge_setting()
			option_ = options()
			option_._filter=filter_
			return syslog_purge_setting_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_purge_setting resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_purge_setting_obj = syslog_purge_setting()
			option_ = options()
			option_._count=True
			response = syslog_purge_setting_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_purge_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_purge_setting_obj = syslog_purge_setting()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_purge_setting_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_purge_setting_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_purge_setting
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_purge_setting_responses, response, "syslog_purge_setting_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_purge_setting_response_array
				i=0
				error = [syslog_purge_setting() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_purge_setting_response_array
			i=0
			syslog_purge_setting_objs = [syslog_purge_setting() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_purge_setting'):
					for props in obj._syslog_purge_setting:
						result = service.payload_formatter.string_to_bulk_resource(syslog_purge_setting_response,self.__class__.__name__,props)
						syslog_purge_setting_objs[i] = result.syslog_purge_setting
						i=i+1
			return syslog_purge_setting_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_purge_setting,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_purge_setting_response(base_response):
	def __init__(self,length=1) :
		self.syslog_purge_setting= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_purge_setting= [ syslog_purge_setting() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_purge_setting_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_purge_setting_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_purge_setting_response_array = [ syslog_purge_setting() for _ in range(length)]
