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
Configuration for CBSDX Single Bundle Upgrade resource
'''

class cb_sb_upgrade(base_resource):
	_file_name= ""
	_ns_ip_arr_to_save=[]
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
			return "cb_sb_upgrade"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "cb_sb_upgrades"
		except Exception as e :
			raise e



	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	List of NetScaler IP address for which config needs to be saved
	'''
	@property
	def ns_ip_arr_to_save(self) :
		try:
			return self._ns_ip_arr_to_save
		except Exception as e :
			raise e
	'''
	List of NetScaler IP address for which config needs to be saved
	'''
	@ns_ip_arr_to_save.setter
	def ns_ip_arr_to_save(self,ns_ip_arr_to_save) :
		try :
			if not isinstance(ns_ip_arr_to_save,list):
				raise TypeError("ns_ip_arr_to_save must be set to array of str value")
			for item in ns_ip_arr_to_save :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_arr_to_save = ns_ip_arr_to_save
		except Exception as e :
			raise e

	'''
	Use this operation to upgrade using single bundle image.
	'''
	@classmethod
	def upgrade(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"upgrade")
			else : 
				cb_sb_upgrade_obj= cb_sb_upgrade()
				return cls.perform_operation_bulk_request(service,"upgrade", resource,cb_sb_upgrade_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cb_sb_upgrade_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cb_sb_upgrade
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cb_sb_upgrade_responses, response, "cb_sb_upgrade_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cb_sb_upgrade_response_array
				i=0
				error = [cb_sb_upgrade() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cb_sb_upgrade_response_array
			i=0
			cb_sb_upgrade_objs = [cb_sb_upgrade() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cb_sb_upgrade'):
					for props in obj._cb_sb_upgrade:
						result = service.payload_formatter.string_to_bulk_resource(cb_sb_upgrade_response,self.__class__.__name__,props)
						cb_sb_upgrade_objs[i] = result.cb_sb_upgrade
						i=i+1
			return cb_sb_upgrade_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cb_sb_upgrade,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cb_sb_upgrade_response(base_response):
	def __init__(self,length=1) :
		self.cb_sb_upgrade= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cb_sb_upgrade= [ cb_sb_upgrade() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cb_sb_upgrade_responses(base_response):
	def __init__(self,length=1) :
		self.cb_sb_upgrade_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cb_sb_upgrade_response_array = [ cb_sb_upgrade() for _ in range(length)]
