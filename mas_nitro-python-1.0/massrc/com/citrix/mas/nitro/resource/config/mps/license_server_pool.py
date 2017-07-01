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
Configuration for License pool capacity of license server resource
'''

class license_server_pool(base_resource):
	_std_bw_available= ""
	_plt_bw_available= ""
	_std_bw_total= ""
	_ent_bw_available= ""
	_ent_bw_total= ""
	_instance_total= ""
	_plt_bw_total= ""
	_instance_available= ""
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
			return "license_server_pool"
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
			return "license_server_pools"
		except Exception as e :
			raise e



	'''
	get Available Standard Bandwidth pool in Gbps
	'''
	@property
	def std_bw_available(self) :
		try:
			return self._std_bw_available
		except Exception as e :
			raise e


	'''
	get Available Platinum Bandwidth pool in Gbps
	'''
	@property
	def plt_bw_available(self) :
		try:
			return self._plt_bw_available
		except Exception as e :
			raise e


	'''
	get Total Standard Bandwidth pool in Gbps
	'''
	@property
	def std_bw_total(self) :
		try:
			return self._std_bw_total
		except Exception as e :
			raise e


	'''
	get Available Enterprise Bandwidth pool in Gbps
	'''
	@property
	def ent_bw_available(self) :
		try:
			return self._ent_bw_available
		except Exception as e :
			raise e


	'''
	get Total Enterprise Bandwidth pool in Gbps
	'''
	@property
	def ent_bw_total(self) :
		try:
			return self._ent_bw_total
		except Exception as e :
			raise e


	'''
	get Total instance pool
	'''
	@property
	def instance_total(self) :
		try:
			return self._instance_total
		except Exception as e :
			raise e


	'''
	get Total Platinum Bandwidth pool in Gbps
	'''
	@property
	def plt_bw_total(self) :
		try:
			return self._plt_bw_total
		except Exception as e :
			raise e


	'''
	get Available instance pool
	'''
	@property
	def instance_available(self) :
		try:
			return self._instance_available
		except Exception as e :
			raise e
	'''
	set Available instance pool
	'''
	@instance_available.setter
	def instance_available(self,instance_available):
		try :
			if not isinstance(instance_available,long):
				raise TypeError("instance_available must be set to long value")
			self._instance_available = instance_available
		except Exception as e :
			raise e

	'''
	Use this operation to get license pool details of license server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_server_pool_obj=license_server_pool()
				response = license_server_pool_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_server_pool resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_server_pool_obj = license_server_pool()
			option_ = options()
			option_._filter=filter_
			return license_server_pool_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_server_pool resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_server_pool_obj = license_server_pool()
			option_ = options()
			option_._count=True
			response = license_server_pool_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_server_pool resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_server_pool_obj = license_server_pool()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_server_pool_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_server_pool_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_server_pool
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_server_pool_responses, response, "license_server_pool_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_server_pool_response_array
				i=0
				error = [license_server_pool() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_server_pool_response_array
			i=0
			license_server_pool_objs = [license_server_pool() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_server_pool'):
					for props in obj._license_server_pool:
						result = service.payload_formatter.string_to_bulk_resource(license_server_pool_response,self.__class__.__name__,props)
						license_server_pool_objs[i] = result.license_server_pool
						i=i+1
			return license_server_pool_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_server_pool,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_server_pool_response(base_response):
	def __init__(self,length=1) :
		self.license_server_pool= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_server_pool= [ license_server_pool() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_server_pool_responses(base_response):
	def __init__(self,length=1) :
		self.license_server_pool_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_server_pool_response_array = [ license_server_pool() for _ in range(length)]
