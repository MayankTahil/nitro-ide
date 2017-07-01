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
Configuration for various swicthes used for CPU allocation to the VMs resource
'''

class xen_cpu_switches(base_resource):
	_use_new_schema_for_decapolis= ""
	_use_both_sockets_for_smaller_vms= ""
	_id= ""
	_shared_pool_across_sockets= ""
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
			return "xen_cpu_switches"
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
			return "xen_cpu_switchess"
		except Exception as e :
			raise e



	'''
	get Total Thread Count
	'''
	@property
	def use_new_schema_for_decapolis(self) :
		try:
			return self._use_new_schema_for_decapolis
		except Exception as e :
			raise e


	'''
	get Total Thread Count
	'''
	@property
	def use_both_sockets_for_smaller_vms(self) :
		try:
			return self._use_both_sockets_for_smaller_vms
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the CPUs
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the CPUs
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
	get Total Thread Count
	'''
	@property
	def shared_pool_across_sockets(self) :
		try:
			return self._shared_pool_across_sockets
		except Exception as e :
			raise e

	'''
	Use this operation to get data from plugin.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				xen_cpu_switches_obj=xen_cpu_switches()
				response = xen_cpu_switches_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of xen_cpu_switches resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			xen_cpu_switches_obj = xen_cpu_switches()
			option_ = options()
			option_._filter=filter_
			return xen_cpu_switches_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the xen_cpu_switches resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			xen_cpu_switches_obj = xen_cpu_switches()
			option_ = options()
			option_._count=True
			response = xen_cpu_switches_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of xen_cpu_switches resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			xen_cpu_switches_obj = xen_cpu_switches()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = xen_cpu_switches_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(xen_cpu_switches_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.xen_cpu_switches
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(xen_cpu_switches_responses, response, "xen_cpu_switches_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.xen_cpu_switches_response_array
				i=0
				error = [xen_cpu_switches() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.xen_cpu_switches_response_array
			i=0
			xen_cpu_switches_objs = [xen_cpu_switches() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_xen_cpu_switches'):
					for props in obj._xen_cpu_switches:
						result = service.payload_formatter.string_to_bulk_resource(xen_cpu_switches_response,self.__class__.__name__,props)
						xen_cpu_switches_objs[i] = result.xen_cpu_switches
						i=i+1
			return xen_cpu_switches_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(xen_cpu_switches,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class xen_cpu_switches_response(base_response):
	def __init__(self,length=1) :
		self.xen_cpu_switches= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.xen_cpu_switches= [ xen_cpu_switches() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class xen_cpu_switches_responses(base_response):
	def __init__(self,length=1) :
		self.xen_cpu_switches_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.xen_cpu_switches_response_array = [ xen_cpu_switches() for _ in range(length)]
