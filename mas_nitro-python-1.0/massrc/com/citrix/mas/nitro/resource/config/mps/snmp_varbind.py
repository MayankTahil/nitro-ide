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
Configuration for snmp_varbind resource
'''

class snmp_varbind(base_resource):
	_value= ""
	_oid= ""
	_type= ""
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
			return "snmp_varbind"
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
			return "snmp_varbinds"
		except Exception as e :
			raise e


	'''
	value
	'''
	@property
	def value(self):
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	value
	'''
	@value.setter
	def value(self,value):
		try :
			if not isinstance(value,str):
				raise TypeError("value must be set to str value")
			self._value = value
		except Exception as e :
			raise e

	'''
	OID For SNMP
	'''
	@property
	def oid(self):
		try:
			return self._oid
		except Exception as e :
			raise e
	'''
	OID For SNMP
	'''
	@oid.setter
	def oid(self,oid):
		try :
			if not isinstance(oid,str):
				raise TypeError("oid must be set to str value")
			self._oid = oid
		except Exception as e :
			raise e

	'''
	Type
	'''
	@property
	def type(self):
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	Type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,int):
				raise TypeError("type must be set to int value")
			self._type = type
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_varbind_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_varbind
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_varbind_responses, response, "snmp_varbind_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_varbind_response_array
				i=0
				error = [snmp_varbind() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_varbind_response_array
			i=0
			snmp_varbind_objs = [snmp_varbind() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_varbind'):
					for props in obj._snmp_varbind:
						result = service.payload_formatter.string_to_bulk_resource(snmp_varbind_response,self.__class__.__name__,props)
						snmp_varbind_objs[i] = result.snmp_varbind
						i=i+1
			return snmp_varbind_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_varbind,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_varbind_response(base_response):
	def __init__(self,length=1) :
		self.snmp_varbind= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_varbind= [ snmp_varbind() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_varbind_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_varbind_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_varbind_response_array = [ snmp_varbind() for _ in range(length)]
