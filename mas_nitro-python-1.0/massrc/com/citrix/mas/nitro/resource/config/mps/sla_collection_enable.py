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
Configuration for AF SLA Record Collection resource
'''

class sla_collection_enable(base_resource):
	_sla_enable= ""
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
			return "sla_collection_enable"
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
			return "sla_collection_enables"
		except Exception as e :
			raise e



	'''
	get AF SLA Collection enable value
	'''
	@property
	def sla_enable(self) :
		try:
			return self._sla_enable
		except Exception as e :
			raise e
	'''
	set AF SLA Collection enable value
	'''
	@sla_enable.setter
	def sla_enable(self,sla_enable):
		try :
			if not isinstance(sla_enable,bool):
				raise TypeError("sla_enable must be set to bool value")
			self._sla_enable = sla_enable
		except Exception as e :
			raise e

	'''
	To get the AF SLA Collection value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sla_collection_enable_obj=sla_collection_enable()
				response = sla_collection_enable_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set the AF SLA Collection value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				sla_collection_enable_obj=sla_collection_enable()
				return cls.update_bulk_request(client,resource,sla_collection_enable_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sla_collection_enable resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sla_collection_enable_obj = sla_collection_enable()
			option_ = options()
			option_._filter=filter_
			return sla_collection_enable_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sla_collection_enable resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sla_collection_enable_obj = sla_collection_enable()
			option_ = options()
			option_._count=True
			response = sla_collection_enable_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sla_collection_enable resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sla_collection_enable_obj = sla_collection_enable()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sla_collection_enable_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sla_collection_enable_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sla_collection_enable
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sla_collection_enable_responses, response, "sla_collection_enable_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sla_collection_enable_response_array
				i=0
				error = [sla_collection_enable() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sla_collection_enable_response_array
			i=0
			sla_collection_enable_objs = [sla_collection_enable() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sla_collection_enable'):
					for props in obj._sla_collection_enable:
						result = service.payload_formatter.string_to_bulk_resource(sla_collection_enable_response,self.__class__.__name__,props)
						sla_collection_enable_objs[i] = result.sla_collection_enable
						i=i+1
			return sla_collection_enable_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sla_collection_enable,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sla_collection_enable_response(base_response):
	def __init__(self,length=1) :
		self.sla_collection_enable= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sla_collection_enable= [ sla_collection_enable() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sla_collection_enable_responses(base_response):
	def __init__(self,length=1) :
		self.sla_collection_enable_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sla_collection_enable_response_array = [ sla_collection_enable() for _ in range(length)]
