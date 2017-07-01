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
Configuration for JournalContextScope configuration resource
'''

class journalcontextscope(base_resource):
	_validity= ""
	_context_id= ""
	_scope_type= ""
	_id= ""
	_display_name= ""
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
			return "journalcontextscope"
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
			return "journalcontextscopes"
		except Exception as e :
			raise e



	'''
	get validity of the scope
	'''
	@property
	def validity(self) :
		try:
			return self._validity
		except Exception as e :
			raise e
	'''
	set validity of the scope
	'''
	@validity.setter
	def validity(self,validity):
		try :
			if not isinstance(validity,str):
				raise TypeError("validity must be set to str value")
			self._validity = validity
		except Exception as e :
			raise e


	'''
	get Id of context which affects this scope.
	'''
	@property
	def context_id(self) :
		try:
			return self._context_id
		except Exception as e :
			raise e
	'''
	set Id of context which affects this scope.
	'''
	@context_id.setter
	def context_id(self,context_id):
		try :
			if not isinstance(context_id,str):
				raise TypeError("context_id must be set to str value")
			self._context_id = context_id
		except Exception as e :
			raise e


	'''
	get The type of scope
	'''
	@property
	def scope_type(self) :
		try:
			return self._scope_type
		except Exception as e :
			raise e
	'''
	set The type of scope
	'''
	@scope_type.setter
	def scope_type(self,scope_type):
		try :
			if not isinstance(scope_type,str):
				raise TypeError("scope_type must be set to str value")
			self._scope_type = scope_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for scope
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for scope
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
	get name of the scope
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set name of the scope
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e

	'''
	Use this operation to get scope details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				journalcontextscope_obj=journalcontextscope()
				response = journalcontextscope_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of journalcontextscope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			journalcontextscope_obj = journalcontextscope()
			option_ = options()
			option_._filter=filter_
			return journalcontextscope_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the journalcontextscope resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			journalcontextscope_obj = journalcontextscope()
			option_ = options()
			option_._count=True
			response = journalcontextscope_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of journalcontextscope resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			journalcontextscope_obj = journalcontextscope()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = journalcontextscope_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(journalcontextscope_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.journalcontextscope
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(journalcontextscope_responses, response, "journalcontextscope_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.journalcontextscope_response_array
				i=0
				error = [journalcontextscope() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.journalcontextscope_response_array
			i=0
			journalcontextscope_objs = [journalcontextscope() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_journalcontextscope'):
					for props in obj._journalcontextscope:
						result = service.payload_formatter.string_to_bulk_resource(journalcontextscope_response,self.__class__.__name__,props)
						journalcontextscope_objs[i] = result.journalcontextscope
						i=i+1
			return journalcontextscope_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(journalcontextscope,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class journalcontextscope_response(base_response):
	def __init__(self,length=1) :
		self.journalcontextscope= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.journalcontextscope= [ journalcontextscope() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class journalcontextscope_responses(base_response):
	def __init__(self,length=1) :
		self.journalcontextscope_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.journalcontextscope_response_array = [ journalcontextscope() for _ in range(length)]
