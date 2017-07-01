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
Configuration for Device generic utility resource
'''

class device_generic_resrc(base_resource):
	_act_id= ""
	_failure_action= ""
	_sync= ""
	_payload= ""
	_device_family_type= ""
	_ipaddress=[]
	_resource_type= ""
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
			return "device_generic_resrc"
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
			return "device_generic_resrcs"
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
	get Action taken on failure 
	'''
	@property
	def failure_action(self) :
		try:
			return self._failure_action
		except Exception as e :
			raise e
	'''
	set Action taken on failure 
	'''
	@failure_action.setter
	def failure_action(self,failure_action):
		try :
			if not isinstance(failure_action,str):
				raise TypeError("failure_action must be set to str value")
			self._failure_action = failure_action
		except Exception as e :
			raise e


	'''
	get Ping SVM to check its status
	'''
	@property
	def sync(self) :
		try:
			return self._sync
		except Exception as e :
			raise e
	'''
	set Ping SVM to check its status
	'''
	@sync.setter
	def sync(self,sync):
		try :
			if not isinstance(sync,bool):
				raise TypeError("sync must be set to bool value")
			self._sync = sync
		except Exception as e :
			raise e


	'''
	get Payload/Body Request 
	'''
	@property
	def payload(self) :
		try:
			return self._payload
		except Exception as e :
			raise e
	'''
	set Payload/Body Request 
	'''
	@payload.setter
	def payload(self,payload):
		try :
			if not isinstance(payload,str):
				raise TypeError("payload must be set to str value")
			self._payload = payload
		except Exception as e :
			raise e


	'''
	get Device family type
	'''
	@property
	def device_family_type(self) :
		try:
			return self._device_family_type
		except Exception as e :
			raise e
	'''
	set Device family type
	'''
	@device_family_type.setter
	def device_family_type(self,device_family_type):
		try :
			if not isinstance(device_family_type,str):
				raise TypeError("device_family_type must be set to str value")
			self._device_family_type = device_family_type
		except Exception as e :
			raise e


	'''
	get List of SVM IP Address
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set List of SVM IP Address
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress) :
		try :
			if not isinstance(ipaddress,list):
				raise TypeError("ipaddress must be set to array of str value")
			for item in ipaddress :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get Type of resource
	'''
	@property
	def resource_type(self) :
		try:
			return self._resource_type
		except Exception as e :
			raise e
	'''
	set Type of resource
	'''
	@resource_type.setter
	def resource_type(self,resource_type):
		try :
			if not isinstance(resource_type,str):
				raise TypeError("resource_type must be set to str value")
			self._resource_type = resource_type
		except Exception as e :
			raise e

	'''
	Use this operation to perform configuration on multiple ipaddress.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				device_generic_resrc_obj= device_generic_resrc()
				return cls.perform_operation_bulk_request(service,"add", resource,device_generic_resrc_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_generic_resrc_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.device_generic_resrc
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(device_generic_resrc_responses, response, "device_generic_resrc_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.device_generic_resrc_response_array
				i=0
				error = [device_generic_resrc() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.device_generic_resrc_response_array
			i=0
			device_generic_resrc_objs = [device_generic_resrc() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_device_generic_resrc'):
					for props in obj._device_generic_resrc:
						result = service.payload_formatter.string_to_bulk_resource(device_generic_resrc_response,self.__class__.__name__,props)
						device_generic_resrc_objs[i] = result.device_generic_resrc
						i=i+1
			return device_generic_resrc_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(device_generic_resrc,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class device_generic_resrc_response(base_response):
	def __init__(self,length=1) :
		self.device_generic_resrc= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.device_generic_resrc= [ device_generic_resrc() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class device_generic_resrc_responses(base_response):
	def __init__(self,length=1) :
		self.device_generic_resrc_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.device_generic_resrc_response_array = [ device_generic_resrc() for _ in range(length)]
