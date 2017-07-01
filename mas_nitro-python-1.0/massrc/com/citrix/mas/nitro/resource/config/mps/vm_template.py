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
Configuration for VM Template resource
'''

class vm_template(base_resource):
	_device_family= ""
	_name= ""
	_type= ""
	_id= ""
	_description= ""
	_uuid= ""
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
			return "vm_template"
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
			return "vm_templates"
		except Exception as e :
			raise e



	'''
	get Device family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device family
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Template Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Template Name
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
	get Type of device, (Xen | NS)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of device, (Xen | NS)
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the VM Templates
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the VM Templates
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
	get Description of vm_template
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e


	'''
	get UUID of Template
	'''
	@property
	def uuid(self) :
		try:
			return self._uuid
		except Exception as e :
			raise e

	'''
	Use this operation to get VM Template.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				vm_template_obj=vm_template()
				response = vm_template_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of vm_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			vm_template_obj = vm_template()
			option_ = options()
			option_._filter=filter_
			return vm_template_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the vm_template resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			vm_template_obj = vm_template()
			option_ = options()
			option_._count=True
			response = vm_template_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of vm_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			vm_template_obj = vm_template()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = vm_template_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(vm_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vm_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(vm_template_responses, response, "vm_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.vm_template_response_array
				i=0
				error = [vm_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.vm_template_response_array
			i=0
			vm_template_objs = [vm_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_vm_template'):
					for props in obj._vm_template:
						result = service.payload_formatter.string_to_bulk_resource(vm_template_response,self.__class__.__name__,props)
						vm_template_objs[i] = result.vm_template
						i=i+1
			return vm_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(vm_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class vm_template_response(base_response):
	def __init__(self,length=1) :
		self.vm_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.vm_template= [ vm_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class vm_template_responses(base_response):
	def __init__(self,length=1) :
		self.vm_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.vm_template_response_array = [ vm_template() for _ in range(length)]
