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
Configuration for f5 To NS Conversion resource
'''

class f5_to_ns(base_resource):
	_output_file= ""
	_blob= ""
	_mode= ""
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
			return "f5_to_ns"
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
			return "f5_to_nss"
		except Exception as e :
			raise e



	'''
	get Output File
	'''
	@property
	def output_file(self) :
		try:
			return self._output_file
		except Exception as e :
			raise e
	'''
	set Output File
	'''
	@output_file.setter
	def output_file(self,output_file):
		try :
			if not isinstance(output_file,str):
				raise TypeError("output_file must be set to str value")
			self._output_file = output_file
		except Exception as e :
			raise e


	'''
	get Output File as a String
	'''
	@property
	def blob(self) :
		try:
			return self._blob
		except Exception as e :
			raise e
	'''
	set Output File as a String
	'''
	@blob.setter
	def blob(self,blob):
		try :
			if not isinstance(blob,str):
				raise TypeError("blob must be set to str value")
			self._blob = blob
		except Exception as e :
			raise e


	'''
	get Policy Name
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set Policy Name
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,str):
				raise TypeError("mode must be set to str value")
			self._mode = mode
		except Exception as e :
			raise e

	'''
	.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				f5_to_ns_obj= f5_to_ns()
				return cls.perform_operation_bulk_request(service,"add", resource,f5_to_ns_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(f5_to_ns_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.f5_to_ns
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(f5_to_ns_responses, response, "f5_to_ns_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.f5_to_ns_response_array
				i=0
				error = [f5_to_ns() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.f5_to_ns_response_array
			i=0
			f5_to_ns_objs = [f5_to_ns() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_f5_to_ns'):
					for props in obj._f5_to_ns:
						result = service.payload_formatter.string_to_bulk_resource(f5_to_ns_response,self.__class__.__name__,props)
						f5_to_ns_objs[i] = result.f5_to_ns
						i=i+1
			return f5_to_ns_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(f5_to_ns,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class f5_to_ns_response(base_response):
	def __init__(self,length=1) :
		self.f5_to_ns= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.f5_to_ns= [ f5_to_ns() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class f5_to_ns_responses(base_response):
	def __init__(self,length=1) :
		self.f5_to_ns_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.f5_to_ns_response_array = [ f5_to_ns() for _ in range(length)]
