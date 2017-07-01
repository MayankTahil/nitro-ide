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
from massrc.com.citrix.mas.nitro.resource.config.mps.snmp_varbind import snmp_varbind


'''
Configuration for SNMP BULK RESULT resource
'''

class agent_snmp_bulk_result(base_resource):
	_snmp_result=[]
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
			return "agent_snmp_bulk_result"
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
			return "agent_snmp_bulk_results"
		except Exception as e :
			raise e



	'''
	get SNMP Result
	'''
	@property
	def snmp_result(self) :
		try:
			return self._snmp_result
		except Exception as e :
			raise e
	'''
	set SNMP Result
	'''
	@snmp_result.setter
	def snmp_result(self,snmp_result) :
		try :
			if not isinstance(snmp_result,list):
				raise TypeError("snmp_result must be set to array of snmp_varbind value")
			for item in snmp_result :
				if not isinstance(item,snmp_varbind):
					raise TypeError("item must be set to snmp_varbind value")
			self._snmp_result = snmp_result
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_snmp_bulk_result_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.agent_snmp_bulk_result
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(agent_snmp_bulk_result_responses, response, "agent_snmp_bulk_result_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.agent_snmp_bulk_result_response_array
				i=0
				error = [agent_snmp_bulk_result() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.agent_snmp_bulk_result_response_array
			i=0
			agent_snmp_bulk_result_objs = [agent_snmp_bulk_result() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_agent_snmp_bulk_result'):
					for props in obj._agent_snmp_bulk_result:
						result = service.payload_formatter.string_to_bulk_resource(agent_snmp_bulk_result_response,self.__class__.__name__,props)
						agent_snmp_bulk_result_objs[i] = result.agent_snmp_bulk_result
						i=i+1
			return agent_snmp_bulk_result_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(agent_snmp_bulk_result,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class agent_snmp_bulk_result_response(base_response):
	def __init__(self,length=1) :
		self.agent_snmp_bulk_result= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.agent_snmp_bulk_result= [ agent_snmp_bulk_result() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class agent_snmp_bulk_result_responses(base_response):
	def __init__(self,length=1) :
		self.agent_snmp_bulk_result_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.agent_snmp_bulk_result_response_array = [ agent_snmp_bulk_result() for _ in range(length)]
