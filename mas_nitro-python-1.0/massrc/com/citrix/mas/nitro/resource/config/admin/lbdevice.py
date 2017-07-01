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
Configuration for Devices resources which associated with tenants based on configured policies. resource
'''

class lbdevice(base_resource):
	_producttype= ""
	_productversion= ""
	_name= ""
	_servicepackage= ""
	_type= ""
	_id= ""
	_provision_ref= ""
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
			return "lbdevice"
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
			return "lbdevices"
		except Exception as e :
			raise e



	'''
	get Product Type of the device
	'''
	@property
	def producttype(self) :
		try:
			return self._producttype
		except Exception as e :
			raise e
	'''
	set Product Type of the device
	'''
	@producttype.setter
	def producttype(self,producttype):
		try :
			if not isinstance(producttype,str):
				raise TypeError("producttype must be set to str value")
			self._producttype = producttype
		except Exception as e :
			raise e


	'''
	get Product version of the device
	'''
	@property
	def productversion(self) :
		try:
			return self._productversion
		except Exception as e :
			raise e
	'''
	set Product version of the device
	'''
	@productversion.setter
	def productversion(self,productversion):
		try :
			if not isinstance(productversion,str):
				raise TypeError("productversion must be set to str value")
			self._productversion = productversion
		except Exception as e :
			raise e


	'''
	get Name of device.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of device.
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
	get servicepackage  of the device
	'''
	@property
	def servicepackage(self) :
		try:
			return self._servicepackage
		except Exception as e :
			raise e
	'''
	set servicepackage  of the device
	'''
	@servicepackage.setter
	def servicepackage(self,servicepackage):
		try :
			if not isinstance(servicepackage,str):
				raise TypeError("servicepackage must be set to str value")
			self._servicepackage = servicepackage
		except Exception as e :
			raise e


	'''
	get Device Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Device Type
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
	get ID of the device
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID of the device
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
	get provision_ref  of the device
	'''
	@property
	def provision_ref(self) :
		try:
			return self._provision_ref
		except Exception as e :
			raise e
	'''
	set provision_ref  of the device
	'''
	@provision_ref.setter
	def provision_ref(self,provision_ref):
		try :
			if not isinstance(provision_ref,str):
				raise TypeError("provision_ref must be set to str value")
			self._provision_ref = provision_ref
		except Exception as e :
			raise e

	'''
	Use this operation to get cloud user details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				lbdevice_obj=lbdevice()
				response = lbdevice_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of lbdevice resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			lbdevice_obj = lbdevice()
			option_ = options()
			option_._filter=filter_
			return lbdevice_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the lbdevice resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			lbdevice_obj = lbdevice()
			option_ = options()
			option_._count=True
			response = lbdevice_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of lbdevice resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			lbdevice_obj = lbdevice()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = lbdevice_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(lbdevice_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbdevice
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(lbdevice_responses, response, "lbdevice_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.lbdevice_response_array
				i=0
				error = [lbdevice() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.lbdevice_response_array
			i=0
			lbdevice_objs = [lbdevice() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_lbdevice'):
					for props in obj._lbdevice:
						result = service.payload_formatter.string_to_bulk_resource(lbdevice_response,self.__class__.__name__,props)
						lbdevice_objs[i] = result.lbdevice
						i=i+1
			return lbdevice_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(lbdevice,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class lbdevice_response(base_response):
	def __init__(self,length=1) :
		self.lbdevice= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.lbdevice= [ lbdevice() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class lbdevice_responses(base_response):
	def __init__(self,length=1) :
		self.lbdevice_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.lbdevice_response_array = [ lbdevice() for _ in range(length)]
