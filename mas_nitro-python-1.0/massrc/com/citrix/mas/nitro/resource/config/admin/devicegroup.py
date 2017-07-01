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
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember


'''
Configuration for Device group consists of a details about type of devices and platforms present in the group, the references of devices and platforms. The devices added to any service package will be present in its device group.  resource
'''

class devicegroup(base_resource):
	_platform_type= ""
	_platforms=[]
	_device_type= ""
	_name= ""
	_id= ""
	_devices=[]
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
			return "/admin/v1/devicegroups"
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
			return "devicegroup"
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
			return "devicegroups"
		except Exception as e :
			raise e



	'''
	get platform_type property hold the type of platform of the devices that are present in the device group. The possible values of platform are: 'netscalersdx', 'netscalermpx', 'netscalervpx', 'nova', 'cloudstack'.
	'''
	@property
	def platform_type(self) :
		try:
			return self._platform_type
		except Exception as e :
			raise e
	'''
	set platform_type property hold the type of platform of the devices that are present in the device group. The possible values of platform are: 'netscalersdx', 'netscalermpx', 'netscalervpx', 'nova', 'cloudstack'.
	'''
	@platform_type.setter
	def platform_type(self,platform_type):
		try :
			if not isinstance(platform_type,str):
				raise TypeError("platform_type must be set to str value")
			self._platform_type = platform_type
		except Exception as e :
			raise e


	'''
	get Platforms present in devicegroup.
	'''
	@property
	def platforms(self) :
		try:
			return self._platforms
		except Exception as e :
			raise e


	'''
	get device_type property hold the type of the devices present in the device group. The two values that are currently supported are 'netscaler' and 'partition'. 
	'''
	@property
	def device_type(self) :
		try:
			return self._device_type
		except Exception as e :
			raise e
	'''
	set device_type property hold the type of the devices present in the device group. The two values that are currently supported are 'netscaler' and 'partition'. 
	'''
	@device_type.setter
	def device_type(self,device_type):
		try :
			if not isinstance(device_type,str):
				raise TypeError("device_type must be set to str value")
			self._device_type = device_type
		except Exception as e :
			raise e


	'''
	get Name of devicegroup.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of devicegroup.
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
	get Id is system generated key for devicegroup.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for devicegroup.
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
	get Devices present in devicegroup.
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e

	'''
	Use this operation to add devicegroup details..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				devicegroup_obj= devicegroup()
				return cls.perform_operation_bulk_request(service,"add", resource,devicegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to devicegroup details.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					devicegroup_obj=devicegroup()
					return cls.delete_bulk_request(client,resource,devicegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get devicegroup details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				devicegroup_obj=devicegroup()
				response = devicegroup_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify devicegroup details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				devicegroup_obj=devicegroup()
				return cls.update_bulk_request(client,resource,devicegroup_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of devicegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			devicegroup_obj = devicegroup()
			option_ = options()
			option_._filter=filter_
			return devicegroup_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the devicegroup resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			devicegroup_obj = devicegroup()
			option_ = options()
			option_._count=True
			response = devicegroup_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of devicegroup resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			devicegroup_obj = devicegroup()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = devicegroup_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(devicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.devicegroup
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(devicegroup_responses, response, "devicegroup_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.devicegroup_response_array
				i=0
				error = [devicegroup() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.devicegroup_response_array
			i=0
			devicegroup_objs = [devicegroup() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_devicegroup'):
					for props in obj._devicegroup:
						result = service.payload_formatter.string_to_bulk_resource(devicegroup_response,self.__class__.__name__,props)
						devicegroup_objs[i] = result.devicegroup
						i=i+1
			return devicegroup_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(devicegroup,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class devicegroup_response(base_response):
	def __init__(self,length=1) :
		self.devicegroup= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.devicegroup= [ devicegroup() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class devicegroup_responses(base_response):
	def __init__(self,length=1) :
		self.devicegroup_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.devicegroup_response_array = [ devicegroup() for _ in range(length)]
