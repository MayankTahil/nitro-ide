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
Configuration for SDX Formation Network Mapping resource
'''

class sdx_network_mapping(base_resource):
	_interface_name= ""
	_interface_type= ""
	_sdx_formation_network_id= ""
	_vif_uuid= ""
	_pci_id= ""
	_id= ""
	_vm_uuid= ""
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
			return "sdx_network_mapping"
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
			return "sdx_network_mappings"
		except Exception as e :
			raise e



	'''
	get Name of this interface
	'''
	@property
	def interface_name(self) :
		try:
			return self._interface_name
		except Exception as e :
			raise e
	'''
	set Name of this interface
	'''
	@interface_name.setter
	def interface_name(self,interface_name):
		try :
			if not isinstance(interface_name,str):
				raise TypeError("interface_name must be set to str value")
			self._interface_name = interface_name
		except Exception as e :
			raise e


	'''
	get Interface Type, SRIOV(VF) or PV(VIF)
	'''
	@property
	def interface_type(self) :
		try:
			return self._interface_type
		except Exception as e :
			raise e
	'''
	set Interface Type, SRIOV(VF) or PV(VIF)
	'''
	@interface_type.setter
	def interface_type(self,interface_type):
		try :
			if not isinstance(interface_type,int):
				raise TypeError("interface_type must be set to int value")
			self._interface_type = interface_type
		except Exception as e :
			raise e


	'''
	get SDX Formation Network Id
	'''
	@property
	def sdx_formation_network_id(self) :
		try:
			return self._sdx_formation_network_id
		except Exception as e :
			raise e
	'''
	set SDX Formation Network Id
	'''
	@sdx_formation_network_id.setter
	def sdx_formation_network_id(self,sdx_formation_network_id):
		try :
			if not isinstance(sdx_formation_network_id,str):
				raise TypeError("sdx_formation_network_id must be set to str value")
			self._sdx_formation_network_id = sdx_formation_network_id
		except Exception as e :
			raise e


	'''
	get vif uuid
	'''
	@property
	def vif_uuid(self) :
		try:
			return self._vif_uuid
		except Exception as e :
			raise e
	'''
	set vif uuid
	'''
	@vif_uuid.setter
	def vif_uuid(self,vif_uuid):
		try :
			if not isinstance(vif_uuid,str):
				raise TypeError("vif_uuid must be set to str value")
			self._vif_uuid = vif_uuid
		except Exception as e :
			raise e


	'''
	get PCI Device Id
	'''
	@property
	def pci_id(self) :
		try:
			return self._pci_id
		except Exception as e :
			raise e
	'''
	set PCI Device Id
	'''
	@pci_id.setter
	def pci_id(self,pci_id):
		try :
			if not isinstance(pci_id,str):
				raise TypeError("pci_id must be set to str value")
			self._pci_id = pci_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the sdx networks mappins
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sdx networks mappins
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
	get UUID of VM Instance
	'''
	@property
	def vm_uuid(self) :
		try:
			return self._vm_uuid
		except Exception as e :
			raise e
	'''
	set UUID of VM Instance
	'''
	@vm_uuid.setter
	def vm_uuid(self,vm_uuid):
		try :
			if not isinstance(vm_uuid,str):
				raise TypeError("vm_uuid must be set to str value")
			self._vm_uuid = vm_uuid
		except Exception as e :
			raise e

	'''
	Use this operation to get the network pool.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sdx_network_mapping_obj=sdx_network_mapping()
				response = sdx_network_mapping_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sdx_network_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sdx_network_mapping_obj = sdx_network_mapping()
			option_ = options()
			option_._filter=filter_
			return sdx_network_mapping_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sdx_network_mapping resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sdx_network_mapping_obj = sdx_network_mapping()
			option_ = options()
			option_._count=True
			response = sdx_network_mapping_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sdx_network_mapping resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sdx_network_mapping_obj = sdx_network_mapping()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sdx_network_mapping_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sdx_network_mapping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdx_network_mapping
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdx_network_mapping_responses, response, "sdx_network_mapping_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdx_network_mapping_response_array
				i=0
				error = [sdx_network_mapping() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdx_network_mapping_response_array
			i=0
			sdx_network_mapping_objs = [sdx_network_mapping() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdx_network_mapping'):
					for props in obj._sdx_network_mapping:
						result = service.payload_formatter.string_to_bulk_resource(sdx_network_mapping_response,self.__class__.__name__,props)
						sdx_network_mapping_objs[i] = result.sdx_network_mapping
						i=i+1
			return sdx_network_mapping_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdx_network_mapping,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdx_network_mapping_response(base_response):
	def __init__(self,length=1) :
		self.sdx_network_mapping= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdx_network_mapping= [ sdx_network_mapping() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdx_network_mapping_responses(base_response):
	def __init__(self,length=1) :
		self.sdx_network_mapping_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdx_network_mapping_response_array = [ sdx_network_mapping() for _ in range(length)]
