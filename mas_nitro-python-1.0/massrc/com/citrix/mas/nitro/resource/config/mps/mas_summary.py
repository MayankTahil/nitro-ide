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
Configuration for MAS Summary resource
'''

class mas_summary(base_resource):
	_sdwanwo_count= ""
	_sdx_count= ""
	_partition_count= ""
	_gateway_count= ""
	_ns_service_count= ""
	_ns_vip_count= ""
	_haproxy_count= ""
	_application_count= ""
	_ns_count= ""
	_ns_ssl_certkey_count= ""
	_ns_servicegroup_count= ""
	_tenant_count= ""
	_sdwanee_count= ""
	_dc_count= ""
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
			return "mas_summary"
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
			return "mas_summarys"
		except Exception as e :
			raise e


	'''
	SDWAN WO count
	'''
	@property
	def sdwanwo_count(self):
		try:
			return self._sdwanwo_count
		except Exception as e :
			raise e

	'''
	SDX count
	'''
	@property
	def sdx_count(self):
		try:
			return self._sdx_count
		except Exception as e :
			raise e

	'''
	Admin Partitions count
	'''
	@property
	def partition_count(self):
		try:
			return self._partition_count
		except Exception as e :
			raise e

	'''
	Gateway count
	'''
	@property
	def gateway_count(self):
		try:
			return self._gateway_count
		except Exception as e :
			raise e

	'''
	Service count
	'''
	@property
	def ns_service_count(self):
		try:
			return self._ns_service_count
		except Exception as e :
			raise e

	'''
	VIP count
	'''
	@property
	def ns_vip_count(self):
		try:
			return self._ns_vip_count
		except Exception as e :
			raise e

	'''
	HAProxy count
	'''
	@property
	def haproxy_count(self):
		try:
			return self._haproxy_count
		except Exception as e :
			raise e

	'''
	Application count
	'''
	@property
	def application_count(self):
		try:
			return self._application_count
		except Exception as e :
			raise e

	'''
	NS count
	'''
	@property
	def ns_count(self):
		try:
			return self._ns_count
		except Exception as e :
			raise e

	'''
	SSL certificate count
	'''
	@property
	def ns_ssl_certkey_count(self):
		try:
			return self._ns_ssl_certkey_count
		except Exception as e :
			raise e

	'''
	Service count
	'''
	@property
	def ns_servicegroup_count(self):
		try:
			return self._ns_servicegroup_count
		except Exception as e :
			raise e

	'''
	Tenants count
	'''
	@property
	def tenant_count(self):
		try:
			return self._tenant_count
		except Exception as e :
			raise e

	'''
	SDWAN EE count
	'''
	@property
	def sdwanee_count(self):
		try:
			return self._sdwanee_count
		except Exception as e :
			raise e

	'''
	DataCenter count
	'''
	@property
	def dc_count(self):
		try:
			return self._dc_count
		except Exception as e :
			raise e

	'''
	Use this operation to get MAS summary.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mas_summary_obj=mas_summary()
				response = mas_summary_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_summary_obj = mas_summary()
			option_ = options()
			option_._filter=filter_
			return mas_summary_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_summary resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_summary_obj = mas_summary()
			option_ = options()
			option_._count=True
			response = mas_summary_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_summary resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_summary_obj = mas_summary()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_summary_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_summary_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_summary
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_summary_responses, response, "mas_summary_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_summary_response_array
				i=0
				error = [mas_summary() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_summary_response_array
			i=0
			mas_summary_objs = [mas_summary() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_summary'):
					for props in obj._mas_summary:
						result = service.payload_formatter.string_to_bulk_resource(mas_summary_response,self.__class__.__name__,props)
						mas_summary_objs[i] = result.mas_summary
						i=i+1
			return mas_summary_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_summary,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_summary_response(base_response):
	def __init__(self,length=1) :
		self.mas_summary= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_summary= [ mas_summary() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_summary_responses(base_response):
	def __init__(self,length=1) :
		self.mas_summary_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_summary_response_array = [ mas_summary() for _ in range(length)]
