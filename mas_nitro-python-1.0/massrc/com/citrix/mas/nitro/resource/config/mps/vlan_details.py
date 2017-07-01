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
Configuration for VLAN details resource
'''

class vlan_details(base_resource):
	_vm_ip_address= ""
	_vm_name= ""
	_interface_list= ""
	_vlan_id= ""
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
			return "vlan_details"
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
			return "vlan_detailss"
		except Exception as e :
			raise e



	'''
	get IP Address of the VM where VLAN is configured
	'''
	@property
	def vm_ip_address(self) :
		try:
			return self._vm_ip_address
		except Exception as e :
			raise e


	'''
	get Name of the VM where VLAN is configured
	'''
	@property
	def vm_name(self) :
		try:
			return self._vm_name
		except Exception as e :
			raise e


	'''
	get List of interface associated with VLAN on the VM
	'''
	@property
	def interface_list(self) :
		try:
			return self._interface_list
		except Exception as e :
			raise e


	'''
	get VLAN ID
	'''
	@property
	def vlan_id(self) :
		try:
			return self._vlan_id
		except Exception as e :
			raise e

	'''
	Use this operation to get vlan details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vlan_details_obj=vlan_details()
				response = vlan_details_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vlan_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vlan_details_obj = vlan_details()
			option_ = options()
			option_._filter=filter_
			return vlan_details_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vlan_details resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vlan_details_obj = vlan_details()
			option_ = options()
			option_._count=True
			response = vlan_details_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vlan_details resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vlan_details_obj = vlan_details()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vlan_details_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vlan_details_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vlan_details
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vlan_details_responses, response, "vlan_details_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vlan_details_response_array
				i=0
				error = [vlan_details() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vlan_details_response_array
			i=0
			vlan_details_objs = [vlan_details() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vlan_details'):
					for props in obj._vlan_details:
						result = service.payload_formatter.string_to_bulk_resource(vlan_details_response,self.__class__.__name__,props)
						vlan_details_objs[i] = result.vlan_details
						i=i+1
			return vlan_details_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vlan_details,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vlan_details_response(base_response):
	def __init__(self,length=1) :
		self.vlan_details= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vlan_details= [ vlan_details() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vlan_details_responses(base_response):
	def __init__(self,length=1) :
		self.vlan_details_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vlan_details_response_array = [ vlan_details() for _ in range(length)]
