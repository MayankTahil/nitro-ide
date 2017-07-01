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
Configuration for Comparison Table for PE and PI resource
'''

class pe_to_pi_comparison(base_resource):
	_pi_cmd= ""
	_pe_cmd= ""
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
			return "pe_to_pi_comparison"
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
			return "pe_to_pi_comparisons"
		except Exception as e :
			raise e



	'''
	get PI Expression
	'''
	@property
	def pi_cmd(self) :
		try:
			return self._pi_cmd
		except Exception as e :
			raise e
	'''
	set PI Expression
	'''
	@pi_cmd.setter
	def pi_cmd(self,pi_cmd):
		try :
			if not isinstance(pi_cmd,str):
				raise TypeError("pi_cmd must be set to str value")
			self._pi_cmd = pi_cmd
		except Exception as e :
			raise e


	'''
	get PE Expression
	'''
	@property
	def pe_cmd(self) :
		try:
			return self._pe_cmd
		except Exception as e :
			raise e
	'''
	set PE Expression
	'''
	@pe_cmd.setter
	def pe_cmd(self,pe_cmd):
		try :
			if not isinstance(pe_cmd,str):
				raise TypeError("pe_cmd must be set to str value")
			self._pe_cmd = pe_cmd
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(pe_to_pi_comparison_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pe_to_pi_comparison
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(pe_to_pi_comparison_responses, response, "pe_to_pi_comparison_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.pe_to_pi_comparison_response_array
				i=0
				error = [pe_to_pi_comparison() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.pe_to_pi_comparison_response_array
			i=0
			pe_to_pi_comparison_objs = [pe_to_pi_comparison() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_pe_to_pi_comparison'):
					for props in obj._pe_to_pi_comparison:
						result = service.payload_formatter.string_to_bulk_resource(pe_to_pi_comparison_response,self.__class__.__name__,props)
						pe_to_pi_comparison_objs[i] = result.pe_to_pi_comparison
						i=i+1
			return pe_to_pi_comparison_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(pe_to_pi_comparison,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class pe_to_pi_comparison_response(base_response):
	def __init__(self,length=1) :
		self.pe_to_pi_comparison= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.pe_to_pi_comparison= [ pe_to_pi_comparison() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class pe_to_pi_comparison_responses(base_response):
	def __init__(self,length=1) :
		self.pe_to_pi_comparison_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.pe_to_pi_comparison_response_array = [ pe_to_pi_comparison() for _ in range(length)]
