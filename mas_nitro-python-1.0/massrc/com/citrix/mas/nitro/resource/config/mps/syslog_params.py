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
Configuration for Syslog Parameters resource
'''

class syslog_params(base_resource):
	_date_format= ""
	_timezone= ""
	_id= ""
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
			return "syslog_params"
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
			return "syslog_paramss"
		except Exception as e :
			raise e



	'''
	get Format of date to be added in the syslog message
	'''
	@property
	def date_format(self) :
		try:
			return self._date_format
		except Exception as e :
			raise e
	'''
	set Format of date to be added in the syslog message
	'''
	@date_format.setter
	def date_format(self,date_format):
		try :
			if not isinstance(date_format,str):
				raise TypeError("date_format must be set to str value")
			self._date_format = date_format
		except Exception as e :
			raise e


	'''
	get Timezone to be used in the syslog message
	'''
	@property
	def timezone(self) :
		try:
			return self._timezone
		except Exception as e :
			raise e
	'''
	set Timezone to be used in the syslog message
	'''
	@timezone.setter
	def timezone(self,timezone):
		try :
			if not isinstance(timezone,str):
				raise TypeError("timezone must be set to str value")
			self._timezone = timezone
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	Use this operation to get the syslog parameters.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				syslog_params_obj=syslog_params()
				response = syslog_params_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify the syslog parameters.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				syslog_params_obj=syslog_params()
				return cls.update_bulk_request(client,resource,syslog_params_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of syslog_params resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			syslog_params_obj = syslog_params()
			option_ = options()
			option_._filter=filter_
			return syslog_params_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the syslog_params resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			syslog_params_obj = syslog_params()
			option_ = options()
			option_._count=True
			response = syslog_params_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of syslog_params resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			syslog_params_obj = syslog_params()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = syslog_params_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(syslog_params_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.syslog_params
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(syslog_params_responses, response, "syslog_params_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.syslog_params_response_array
				i=0
				error = [syslog_params() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.syslog_params_response_array
			i=0
			syslog_params_objs = [syslog_params() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_syslog_params'):
					for props in obj._syslog_params:
						result = service.payload_formatter.string_to_bulk_resource(syslog_params_response,self.__class__.__name__,props)
						syslog_params_objs[i] = result.syslog_params
						i=i+1
			return syslog_params_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(syslog_params,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class syslog_params_response(base_response):
	def __init__(self,length=1) :
		self.syslog_params= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.syslog_params= [ syslog_params() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class syslog_params_responses(base_response):
	def __init__(self,length=1) :
		self.syslog_params_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.syslog_params_response_array = [ syslog_params() for _ in range(length)]
