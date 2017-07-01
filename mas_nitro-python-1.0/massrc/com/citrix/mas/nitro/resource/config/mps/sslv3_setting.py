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
Configuration for SSLV3 Setting resource
'''

class sslv3_setting(base_resource):
	_enable= ""
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
			return "sslv3_setting"
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
			return "sslv3_settings"
		except Exception as e :
			raise e



	'''
	get Secure Access only
	'''
	@property
	def enable(self) :
		try:
			return self._enable
		except Exception as e :
			raise e
	'''
	set Secure Access only
	'''
	@enable.setter
	def enable(self,enable):
		try :
			if not isinstance(enable,bool):
				raise TypeError("enable must be set to bool value")
			self._enable = enable
		except Exception as e :
			raise e

	'''
	Use this operation to get sslv3 settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sslv3_setting_obj=sslv3_setting()
				response = sslv3_setting_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify sslv3 settings.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sslv3_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sslv3_setting_obj = sslv3_setting()
			option_ = options()
			option_._filter=filter_
			return sslv3_setting_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sslv3_setting resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sslv3_setting_obj = sslv3_setting()
			option_ = options()
			option_._count=True
			response = sslv3_setting_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sslv3_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sslv3_setting_obj = sslv3_setting()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sslv3_setting_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sslv3_setting_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslv3_setting
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sslv3_setting_responses, response, "sslv3_setting_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sslv3_setting_response_array
				i=0
				error = [sslv3_setting() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sslv3_setting_response_array
			i=0
			sslv3_setting_objs = [sslv3_setting() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sslv3_setting'):
					for props in obj._sslv3_setting:
						result = service.payload_formatter.string_to_bulk_resource(sslv3_setting_response,self.__class__.__name__,props)
						sslv3_setting_objs[i] = result.sslv3_setting
						i=i+1
			return sslv3_setting_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sslv3_setting,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sslv3_setting_response(base_response):
	def __init__(self,length=1) :
		self.sslv3_setting= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sslv3_setting= [ sslv3_setting() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sslv3_setting_responses(base_response):
	def __init__(self,length=1) :
		self.sslv3_setting_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sslv3_setting_response_array = [ sslv3_setting() for _ in range(length)]
