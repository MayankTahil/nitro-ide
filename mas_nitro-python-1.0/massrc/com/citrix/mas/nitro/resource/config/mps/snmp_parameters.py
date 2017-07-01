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
Configuration for SNMP parameters resource
'''

class snmp_parameters(base_resource):
	_privPassword= ""
	_retries= ""
	_privProtocol= ""
	_version= ""
	_securityName= ""
	_community= ""
	_timeout= ""
	_authProtocol= ""
	_authPassword= ""
	_securityLevel= ""
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
			return "snmp_parameters"
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
			return "snmp_parameterss"
		except Exception as e :
			raise e



	'''
	get SNMP privPassword
	'''
	@property
	def privPassword(self) :
		try:
			return self._privPassword
		except Exception as e :
			raise e
	'''
	set SNMP privPassword
	'''
	@privPassword.setter
	def privPassword(self,privPassword):
		try :
			if not isinstance(privPassword,str):
				raise TypeError("privPassword must be set to str value")
			self._privPassword = privPassword
		except Exception as e :
			raise e


	'''
	get SNMP retries
	'''
	@property
	def retries(self) :
		try:
			return self._retries
		except Exception as e :
			raise e
	'''
	set SNMP retries
	'''
	@retries.setter
	def retries(self,retries):
		try :
			if not isinstance(retries,int):
				raise TypeError("retries must be set to int value")
			self._retries = retries
		except Exception as e :
			raise e


	'''
	get SNMP privProtocol
	'''
	@property
	def privProtocol(self) :
		try:
			return self._privProtocol
		except Exception as e :
			raise e
	'''
	set SNMP privProtocol
	'''
	@privProtocol.setter
	def privProtocol(self,privProtocol):
		try :
			if not isinstance(privProtocol,str):
				raise TypeError("privProtocol must be set to str value")
			self._privProtocol = privProtocol
		except Exception as e :
			raise e


	'''
	get SNMP Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set SNMP Version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,long):
				raise TypeError("version must be set to long value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get SNMP securityName
	'''
	@property
	def securityName(self) :
		try:
			return self._securityName
		except Exception as e :
			raise e
	'''
	set SNMP securityName
	'''
	@securityName.setter
	def securityName(self,securityName):
		try :
			if not isinstance(securityName,str):
				raise TypeError("securityName must be set to str value")
			self._securityName = securityName
		except Exception as e :
			raise e


	'''
	get SNMP Community
	'''
	@property
	def community(self) :
		try:
			return self._community
		except Exception as e :
			raise e
	'''
	set SNMP Community
	'''
	@community.setter
	def community(self,community):
		try :
			if not isinstance(community,str):
				raise TypeError("community must be set to str value")
			self._community = community
		except Exception as e :
			raise e


	'''
	get SNMP timeout
	'''
	@property
	def timeout(self) :
		try:
			return self._timeout
		except Exception as e :
			raise e
	'''
	set SNMP timeout
	'''
	@timeout.setter
	def timeout(self,timeout):
		try :
			if not isinstance(timeout,long):
				raise TypeError("timeout must be set to long value")
			self._timeout = timeout
		except Exception as e :
			raise e


	'''
	get SNMP authProtocol
	'''
	@property
	def authProtocol(self) :
		try:
			return self._authProtocol
		except Exception as e :
			raise e
	'''
	set SNMP authProtocol
	'''
	@authProtocol.setter
	def authProtocol(self,authProtocol):
		try :
			if not isinstance(authProtocol,str):
				raise TypeError("authProtocol must be set to str value")
			self._authProtocol = authProtocol
		except Exception as e :
			raise e


	'''
	get SNMP authPassword
	'''
	@property
	def authPassword(self) :
		try:
			return self._authPassword
		except Exception as e :
			raise e
	'''
	set SNMP authPassword
	'''
	@authPassword.setter
	def authPassword(self,authPassword):
		try :
			if not isinstance(authPassword,str):
				raise TypeError("authPassword must be set to str value")
			self._authPassword = authPassword
		except Exception as e :
			raise e


	'''
	get SNMP securityLevel
	'''
	@property
	def securityLevel(self) :
		try:
			return self._securityLevel
		except Exception as e :
			raise e
	'''
	set SNMP securityLevel
	'''
	@securityLevel.setter
	def securityLevel(self,securityLevel):
		try :
			if not isinstance(securityLevel,int):
				raise TypeError("securityLevel must be set to int value")
			self._securityLevel = securityLevel
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_parameters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_parameters
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_parameters_responses, response, "snmp_parameters_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_parameters_response_array
				i=0
				error = [snmp_parameters() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_parameters_response_array
			i=0
			snmp_parameters_objs = [snmp_parameters() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_parameters'):
					for props in obj._snmp_parameters:
						result = service.payload_formatter.string_to_bulk_resource(snmp_parameters_response,self.__class__.__name__,props)
						snmp_parameters_objs[i] = result.snmp_parameters
						i=i+1
			return snmp_parameters_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_parameters,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_parameters_response(base_response):
	def __init__(self,length=1) :
		self.snmp_parameters= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_parameters= [ snmp_parameters() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_parameters_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_parameters_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_parameters_response_array = [ snmp_parameters() for _ in range(length)]
