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
Configuration for License Information resource
'''

class sdx_license(base_resource):
	_std_bw_available= ""
	_max_number_of_ns_instances= ""
	_std_bw_config= ""
	_ent_bw_total= ""
	_act_id= ""
	_available_throughput= ""
	_instances_config= ""
	_plt_bw_total= ""
	_platform= ""
	_max_number_of_instances= ""
	_max_number_of_br_instances= ""
	_plt_bw_available= ""
	_ent_bw_config= ""
	_cluster= ""
	_available_number_of_ns_instances= ""
	_max_throughput= ""
	_std_bw_total= ""
	_ent_bw_available= ""
	_plt_bw_config= ""
	_is_pooled_license= ""
	_available_number_of_instances= ""
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
			return "sdx_license"
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
			return "sdx_licenses"
		except Exception as e :
			raise e



	'''
	get Available standard Bandwidth in Mbps
	'''
	@property
	def std_bw_available(self) :
		try:
			return self._std_bw_available
		except Exception as e :
			raise e


	'''
	get Maximum NetScaler Instances
	'''
	@property
	def max_number_of_ns_instances(self) :
		try:
			return self._max_number_of_ns_instances
		except Exception as e :
			raise e


	'''
	get Configured Standard Bandwidth in Mbps
	'''
	@property
	def std_bw_config(self) :
		try:
			return self._std_bw_config
		except Exception as e :
			raise e


	'''
	get Total enterprise Bandwidth in Mbps
	'''
	@property
	def ent_bw_total(self) :
		try:
			return self._ent_bw_total
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get Available Throughput in Mbps
	'''
	@property
	def available_throughput(self) :
		try:
			return self._available_throughput
		except Exception as e :
			raise e


	'''
	get Instances Configured 
	'''
	@property
	def instances_config(self) :
		try:
			return self._instances_config
		except Exception as e :
			raise e


	'''
	get Maximum platinum Bandwidth in Mbps
	'''
	@property
	def plt_bw_total(self) :
		try:
			return self._plt_bw_total
		except Exception as e :
			raise e


	'''
	get Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e


	'''
	get Maximum Instances
	'''
	@property
	def max_number_of_instances(self) :
		try:
			return self._max_number_of_instances
		except Exception as e :
			raise e


	'''
	get Maximum CloudBridge Instances
	'''
	@property
	def max_number_of_br_instances(self) :
		try:
			return self._max_number_of_br_instances
		except Exception as e :
			raise e


	'''
	get Available platinum Bandwidth in Mbps
	'''
	@property
	def plt_bw_available(self) :
		try:
			return self._plt_bw_available
		except Exception as e :
			raise e


	'''
	get Configured Enterpise Bandwidth in Mbps
	'''
	@property
	def ent_bw_config(self) :
		try:
			return self._ent_bw_config
		except Exception as e :
			raise e


	'''
	get Cluster License
	'''
	@property
	def cluster(self) :
		try:
			return self._cluster
		except Exception as e :
			raise e


	'''
	get Available NetScaler Instances (Shared)
	'''
	@property
	def available_number_of_ns_instances(self) :
		try:
			return self._available_number_of_ns_instances
		except Exception as e :
			raise e


	'''
	get Maximum Throughput in Mbps
	'''
	@property
	def max_throughput(self) :
		try:
			return self._max_throughput
		except Exception as e :
			raise e


	'''
	get Total standard Bandwidth in Mbps
	'''
	@property
	def std_bw_total(self) :
		try:
			return self._std_bw_total
		except Exception as e :
			raise e


	'''
	get Available enterprise Bandwidth in Mbps
	'''
	@property
	def ent_bw_available(self) :
		try:
			return self._ent_bw_available
		except Exception as e :
			raise e


	'''
	get Configured platinum Bandwidth in Mbps
	'''
	@property
	def plt_bw_config(self) :
		try:
			return self._plt_bw_config
		except Exception as e :
			raise e


	'''
	get Platform license for Triscaler feature
	'''
	@property
	def is_pooled_license(self) :
		try:
			return self._is_pooled_license
		except Exception as e :
			raise e


	'''
	get Available Instances
	'''
	@property
	def available_number_of_instances(self) :
		try:
			return self._available_number_of_instances
		except Exception as e :
			raise e

	'''
	Use this operation to apply new licenses files.
	'''
	@classmethod
	def apply(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"apply")
		except Exception as e :
			raise e

	'''
	Use this operation to get SDX license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_license_obj=sdx_license()
				response = sdx_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_license_obj = sdx_license()
			option_ = options()
			option_._filter=filter_
			return sdx_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_license_obj = sdx_license()
			option_ = options()
			option_._count=True
			response = sdx_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_license_obj = sdx_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_license_responses, response, "sdx_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_license_response_array
				i=0
				error = [sdx_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_license_response_array
			i=0
			sdx_license_objs = [sdx_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_license'):
					for props in obj._sdx_license:
						result = service.payload_formatter.string_to_bulk_resource(sdx_license_response,self.__class__.__name__,props)
						sdx_license_objs[i] = result.sdx_license
						i=i+1
			return sdx_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_license_response(base_response):
	def __init__(self,length=1) :
		self.sdx_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_license= [ sdx_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_license_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_license_response_array = [ sdx_license() for _ in range(length)]
