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
Configuration for SMS profile resource
'''

class sms_profile(base_resource):
	_tenant_id= ""
	_to_list= ""
	_id= ""
	_server_name= ""
	_profile_name= ""
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
			return "sms_profile"
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
			return "sms_profiles"
		except Exception as e :
			raise e



	'''
	get Tenant Id of the Config Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get To list.
	'''
	@property
	def to_list(self) :
		try:
			return self._to_list
		except Exception as e :
			raise e
	'''
	set To list.
	'''
	@to_list.setter
	def to_list(self,to_list):
		try :
			if not isinstance(to_list,str):
				raise TypeError("to_list must be set to str value")
			self._to_list = to_list
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the sms profile.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sms profile.
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
	get SMS server name
	'''
	@property
	def server_name(self) :
		try:
			return self._server_name
		except Exception as e :
			raise e
	'''
	set SMS server name
	'''
	@server_name.setter
	def server_name(self,server_name):
		try :
			if not isinstance(server_name,str):
				raise TypeError("server_name must be set to str value")
			self._server_name = server_name
		except Exception as e :
			raise e


	'''
	get Profile name for the sms setting.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name for the sms setting.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Use this operation to add sms profile..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				sms_profile_obj= sms_profile()
				return cls.perform_operation_bulk_request(service,"add", resource,sms_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete sms profile..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					sms_profile_obj=sms_profile()
					return cls.delete_bulk_request(client,resource,sms_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get sms profile..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sms_profile_obj=sms_profile()
				response = sms_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify sms profile..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				sms_profile_obj=sms_profile()
				return cls.update_bulk_request(client,resource,sms_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sms_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sms_profile_obj = sms_profile()
			option_ = options()
			option_._filter=filter_
			return sms_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sms_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sms_profile_obj = sms_profile()
			option_ = options()
			option_._count=True
			response = sms_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sms_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sms_profile_obj = sms_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sms_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sms_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sms_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sms_profile_responses, response, "sms_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sms_profile_response_array
				i=0
				error = [sms_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sms_profile_response_array
			i=0
			sms_profile_objs = [sms_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sms_profile'):
					for props in obj._sms_profile:
						result = service.payload_formatter.string_to_bulk_resource(sms_profile_response,self.__class__.__name__,props)
						sms_profile_objs[i] = result.sms_profile
						i=i+1
			return sms_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sms_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sms_profile_response(base_response):
	def __init__(self,length=1) :
		self.sms_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sms_profile= [ sms_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sms_profile_responses(base_response):
	def __init__(self,length=1) :
		self.sms_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sms_profile_response_array = [ sms_profile() for _ in range(length)]
