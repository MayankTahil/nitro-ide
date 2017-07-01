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
Configuration for Upgrade SDXTools of GuestVM - Applicable only for GuestVM's that support SDXTools resource
'''

class sdxtools_upgrade(base_resource):
	_image_name= ""
	_ip_address_arr=[]
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
			return "sdxtools_upgrade"
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
			return "sdxtools_upgrades"
		except Exception as e :
			raise e



	'''
	get SDXTools Image name
	'''
	@property
	def image_name(self) :
		try:
			return self._image_name
		except Exception as e :
			raise e
	'''
	set SDXTools Image name
	'''
	@image_name.setter
	def image_name(self,image_name):
		try :
			if not isinstance(image_name,str):
				raise TypeError("image_name must be set to str value")
			self._image_name = image_name
		except Exception as e :
			raise e


	'''
	get List of GuestVM IP Address
	'''
	@property
	def ip_address_arr(self) :
		try:
			return self._ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of GuestVM IP Address
	'''
	@ip_address_arr.setter
	def ip_address_arr(self,ip_address_arr) :
		try :
			if not isinstance(ip_address_arr,list):
				raise TypeError("ip_address_arr must be set to array of str value")
			for item in ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ip_address_arr = ip_address_arr
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade SDXTools of GuestVM Instances.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"upgrade")
			else : 
				sdxtools_upgrade_obj= sdxtools_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade", resource,sdxtools_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdxtools_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sdxtools_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sdxtools_upgrade_responses, response, "sdxtools_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sdxtools_upgrade_response_array
				i=0
				error = [sdxtools_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sdxtools_upgrade_response_array
			i=0
			sdxtools_upgrade_objs = [sdxtools_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sdxtools_upgrade'):
					for props in obj._sdxtools_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(sdxtools_upgrade_response,self.__class__.__name__,props)
						sdxtools_upgrade_objs[i] = result.sdxtools_upgrade
						i=i+1
			return sdxtools_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sdxtools_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sdxtools_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.sdxtools_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sdxtools_upgrade= [ sdxtools_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sdxtools_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.sdxtools_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sdxtools_upgrade_response_array = [ sdxtools_upgrade() for _ in range(length)]
