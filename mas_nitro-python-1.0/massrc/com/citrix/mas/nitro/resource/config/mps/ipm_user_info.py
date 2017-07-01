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
Configuration for This table holds user info for IPM. resource
'''

class ipm_user_info(base_resource):
	_password= ""
	_username= ""
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
			return "ipm_user_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._username
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
			return "ipm_user_infos"
		except Exception as e :
			raise e



	'''
	get Dyn password.
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Dyn password.
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Dyn Username.
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Dyn Username.
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e

	'''
	Use this operation to delete a username.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ipm_user_info_obj=ipm_user_info()
					return cls.delete_bulk_request(client,resource,ipm_user_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get a value for a username..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ipm_user_info_obj=ipm_user_info()
				response = ipm_user_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ipm_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ipm_user_info_obj = ipm_user_info()
			option_ = options()
			option_._filter=filter_
			return ipm_user_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ipm_user_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ipm_user_info_obj = ipm_user_info()
			option_ = options()
			option_._count=True
			response = ipm_user_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ipm_user_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ipm_user_info_obj = ipm_user_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ipm_user_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ipm_user_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipm_user_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ipm_user_info_responses, response, "ipm_user_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ipm_user_info_response_array
				i=0
				error = [ipm_user_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ipm_user_info_response_array
			i=0
			ipm_user_info_objs = [ipm_user_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ipm_user_info'):
					for props in obj._ipm_user_info:
						result = service.payload_formatter.string_to_bulk_resource(ipm_user_info_response,self.__class__.__name__,props)
						ipm_user_info_objs[i] = result.ipm_user_info
						i=i+1
			return ipm_user_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ipm_user_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ipm_user_info_response(base_response):
	def __init__(self,length=1) :
		self.ipm_user_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ipm_user_info= [ ipm_user_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ipm_user_info_responses(base_response):
	def __init__(self,length=1) :
		self.ipm_user_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ipm_user_info_response_array = [ ipm_user_info() for _ in range(length)]
