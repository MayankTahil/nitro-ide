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
Configuration for SNMP Information resource
'''

class snmp_info(base_resource):
	_engine_id= ""
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
			return "snmp_info"
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
			return "snmp_infos"
		except Exception as e :
			raise e



	'''
	get SNMP EngineID
	'''
	@property
	def engine_id(self) :
		try:
			return self._engine_id
		except Exception as e :
			raise e
	'''
	set SNMP EngineID
	'''
	@engine_id.setter
	def engine_id(self,engine_id):
		try :
			if not isinstance(engine_id,str):
				raise TypeError("engine_id must be set to str value")
			self._engine_id = engine_id
		except Exception as e :
			raise e

	'''
	Use this operation to get snmp information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_info_obj=snmp_info()
				response = snmp_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp information.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_info_obj=snmp_info()
				return cls.update_bulk_request(client,resource,snmp_info_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_info_obj = snmp_info()
			option_ = options()
			option_._filter=filter_
			return snmp_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_info_obj = snmp_info()
			option_ = options()
			option_._count=True
			response = snmp_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_info_obj = snmp_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_info_responses, response, "snmp_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_info_response_array
				i=0
				error = [snmp_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_info_response_array
			i=0
			snmp_info_objs = [snmp_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_info'):
					for props in obj._snmp_info:
						result = service.payload_formatter.string_to_bulk_resource(snmp_info_response,self.__class__.__name__,props)
						snmp_info_objs[i] = result.snmp_info
						i=i+1
			return snmp_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_info_response(base_response):
	def __init__(self,length=1) :
		self.snmp_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_info= [ snmp_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_info_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_info_response_array = [ snmp_info() for _ in range(length)]
