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
Configuration for Rescources in a sdxvm resource
'''

class sdxvmspec(base_resource):
	_memory= ""
	_cpu= ""
	_version= ""
	_name= ""
	_throughput= ""
	_id= ""
	_ssl_chips= ""
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
			return "/admin/v1/provisioning/sdxvmspecs"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "sdxvmspecs"
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
			return "sdxvmspec"
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
			return "sdxvmspecs"
		except Exception as e :
			raise e



	'''
	get Memory of sdx VM
	'''
	@property
	def memory(self) :
		try:
			return self._memory
		except Exception as e :
			raise e
	'''
	set Memory of sdx VM
	'''
	@memory.setter
	def memory(self,memory):
		try :
			if not isinstance(memory,str):
				raise TypeError("memory must be set to str value")
			self._memory = memory
		except Exception as e :
			raise e


	'''
	get cpu
	'''
	@property
	def cpu(self) :
		try:
			return self._cpu
		except Exception as e :
			raise e
	'''
	set cpu
	'''
	@cpu.setter
	def cpu(self,cpu):
		try :
			if not isinstance(cpu,str):
				raise TypeError("cpu must be set to str value")
			self._cpu = cpu
		except Exception as e :
			raise e


	'''
	get Version of sdx VM
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set Version of sdx VM
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Name of sdx VM
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of sdx VM
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
	get Throughput of sdx VM
	'''
	@property
	def throughput(self) :
		try:
			return self._throughput
		except Exception as e :
			raise e
	'''
	set Throughput of sdx VM
	'''
	@throughput.setter
	def throughput(self,throughput):
		try :
			if not isinstance(throughput,str):
				raise TypeError("throughput must be set to str value")
			self._throughput = throughput
		except Exception as e :
			raise e


	'''
	get Id is system generated key for partition specs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for partition specs
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
	get ssl_chips
	'''
	@property
	def ssl_chips(self) :
		try:
			return self._ssl_chips
		except Exception as e :
			raise e
	'''
	set ssl_chips
	'''
	@ssl_chips.setter
	def ssl_chips(self,ssl_chips):
		try :
			if not isinstance(ssl_chips,str):
				raise TypeError("ssl_chips must be set to str value")
			self._ssl_chips = ssl_chips
		except Exception as e :
			raise e

	'''
	Use this operation to add .
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				sdxvmspec_obj= sdxvmspec()
				return cls.perform_operation_bulk_request(service,"add", resource,sdxvmspec_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					sdxvmspec_obj=sdxvmspec()
					return cls.delete_bulk_request(client,resource,sdxvmspec_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdxvmspec_obj=sdxvmspec()
				response = sdxvmspec_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				sdxvmspec_obj=resource[0]
				return cls.update_bulk_request(client,resource,sdxvmspec_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdxvmspec resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdxvmspec_obj = sdxvmspec()
			option_ = options()
			option_._filter=filter_
			return sdxvmspec_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdxvmspec resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdxvmspec_obj = sdxvmspec()
			option_ = options()
			option_._count=True
			response = sdxvmspec_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdxvmspec resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdxvmspec_obj = sdxvmspec()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdxvmspec_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdxvmspec_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdxvmspec
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdxvmspec_responses, response, "sdxvmspec_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdxvmspec_response_array
				i=0
				error = [sdxvmspec() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdxvmspec_response_array
			i=0
			sdxvmspec_objs = [sdxvmspec() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdxvmspec'):
					for props in obj._sdxvmspec:
						result = service.payload_formatter.string_to_bulk_resource(sdxvmspec_response,self.__class__.__name__,props)
						sdxvmspec_objs[i] = result.sdxvmspec
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdxvmspec,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdxvmspec_response(base_response):
	def __init__(self,length=1) :
		self.sdxvmspec= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdxvmspec= [ sdxvmspec() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdxvmspec_responses(base_response):
	def __init__(self,length=1) :
		self.sdxvmspec_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdxvmspec_response_array = [ sdxvmspec() for _ in range(length)]
