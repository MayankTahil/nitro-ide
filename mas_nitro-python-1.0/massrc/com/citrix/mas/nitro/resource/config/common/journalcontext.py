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
from massrc.com.citrix.mas.nitro.resource.config.common.journalcontextscope import journalcontextscope


'''
Configuration for JournalContext configuration resource
'''

class journalcontext(base_resource):
	_scopes= ""
	_is_default= ""
	_service_name= ""
	_end_time= ""
	_status= ""
	_name= ""
	_start_time= ""
	_id= ""
	_message= ""
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/admin/v1/journalcontexts"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "journalcontexts"
		except Exception as e :
			raise e

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
			return "journalcontext"
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
			return "journalcontexts"
		except Exception as e :
			raise e



	'''
	get The effected entities due to this request
	'''
	@property
	def scopes(self) :
		try:
			return self._scopes
		except Exception as e :
			raise e
	'''
	set The effected entities due to this request
	'''
	@scopes.setter
	def scopes(self,scopes):
		try :
			if not isinstance(scopes,journalcontextscope):
				raise TypeError("scopes must be set to journalcontextscope value")
			self._scopes = scopes
		except Exception as e :
			raise e


	'''
	get The context is default or not
	'''
	@property
	def is_default(self) :
		try:
			return self._is_default
		except Exception as e :
			raise e
	'''
	set The context is default or not
	'''
	@is_default.setter
	def is_default(self,is_default):
		try :
			if not isinstance(is_default,str):
				raise TypeError("is_default must be set to str value")
			self._is_default = is_default
		except Exception as e :
			raise e


	'''
	get Name of service-request which started the context
	'''
	@property
	def service_name(self) :
		try:
			return self._service_name
		except Exception as e :
			raise e
	'''
	set Name of service-request which started the context
	'''
	@service_name.setter
	def service_name(self,service_name):
		try :
			if not isinstance(service_name,str):
				raise TypeError("service_name must be set to str value")
			self._service_name = service_name
		except Exception as e :
			raise e


	'''
	get End time of request
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e
	'''
	set End time of request
	'''
	@end_time.setter
	def end_time(self,end_time):
		try :
			if not isinstance(end_time,str):
				raise TypeError("end_time must be set to str value")
			self._end_time = end_time
		except Exception as e :
			raise e


	'''
	get Status of context could be attempted/finished/Error/Rollback in progress/Rollback Completed
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Status of context could be attempted/finished/Error/Rollback in progress/Rollback Completed
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get Name of the context
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of the context
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Start time of request.
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e
	'''
	set Start time of request.
	'''
	@start_time.setter
	def start_time(self,start_time):
		try :
			if not isinstance(start_time,str):
				raise TypeError("start_time must be set to str value")
			self._start_time = start_time
		except Exception as e :
			raise e


	'''
	get Id is system generated key for context
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for context
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
	get message to be displayed if there is some error in processing request
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set message to be displayed if there is some error in processing request
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
		except Exception as e :
			raise e

	'''
	Use this operation to get context details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				journalcontext_obj=journalcontext()
				response = journalcontext_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of journalcontext resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			journalcontext_obj = journalcontext()
			option_ = options()
			option_._filter=filter_
			return journalcontext_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the journalcontext resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			journalcontext_obj = journalcontext()
			option_ = options()
			option_._count=True
			response = journalcontext_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of journalcontext resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			journalcontext_obj = journalcontext()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = journalcontext_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(journalcontext_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.journalcontext
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(journalcontext_responses, response, "journalcontext_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.journalcontext_response_array
				i=0
				error = [journalcontext() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.journalcontext_response_array
			i=0
			journalcontext_objs = [journalcontext() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_journalcontext'):
					for props in obj._journalcontext:
						result = service.payload_formatter.string_to_bulk_resource(journalcontext_response,self.__class__.__name__,props)
						journalcontext_objs[i] = result.journalcontext
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(journalcontext,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class journalcontext_response(base_response):
	def __init__(self,length=1) :
		self.journalcontext= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.journalcontext= [ journalcontext() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class journalcontext_responses(base_response):
	def __init__(self,length=1) :
		self.journalcontext_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.journalcontext_response_array = [ journalcontext() for _ in range(length)]
