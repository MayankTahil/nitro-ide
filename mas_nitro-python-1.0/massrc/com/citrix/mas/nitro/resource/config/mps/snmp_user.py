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
Configuration for SNMP User resource
'''

class snmp_user(base_resource):
	_security_level= ""
	_auth_password= ""
	_privacy_protocol= ""
	_name= ""
	_privacy_password= ""
	_view_name= ""
	_auth_protocol= ""
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
			return "snmp_user"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "snmp_users"
		except Exception as e :
			raise e



	'''
	get Security Level of SNMP User. Values: 0: noAuthNoPriv, 1: authNoPriv, 2: authPriv
	'''
	@property
	def security_level(self) :
		try:
			return self._security_level
		except Exception as e :
			raise e
	'''
	set Security Level of SNMP User. Values: 0: noAuthNoPriv, 1: authNoPriv, 2: authPriv
	'''
	@security_level.setter
	def security_level(self,security_level):
		try :
			if not isinstance(security_level,int):
				raise TypeError("security_level must be set to int value")
			self._security_level = security_level
		except Exception as e :
			raise e


	'''
	get Authentication Password of SNMP User
	'''
	@property
	def auth_password(self) :
		try:
			return self._auth_password
		except Exception as e :
			raise e
	'''
	set Authentication Password of SNMP User
	'''
	@auth_password.setter
	def auth_password(self,auth_password):
		try :
			if not isinstance(auth_password,str):
				raise TypeError("auth_password must be set to str value")
			self._auth_password = auth_password
		except Exception as e :
			raise e


	'''
	get Privacy Protocol of SNMP User. Values: 0:noValue, 1: DES, 2: AES
	'''
	@property
	def privacy_protocol(self) :
		try:
			return self._privacy_protocol
		except Exception as e :
			raise e
	'''
	set Privacy Protocol of SNMP User. Values: 0:noValue, 1: DES, 2: AES
	'''
	@privacy_protocol.setter
	def privacy_protocol(self,privacy_protocol):
		try :
			if not isinstance(privacy_protocol,int):
				raise TypeError("privacy_protocol must be set to int value")
			self._privacy_protocol = privacy_protocol
		except Exception as e :
			raise e


	'''
	get Name of SNMP User
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of SNMP User
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
	get Privacy Password of SNMP User
	'''
	@property
	def privacy_password(self) :
		try:
			return self._privacy_password
		except Exception as e :
			raise e
	'''
	set Privacy Password of SNMP User
	'''
	@privacy_password.setter
	def privacy_password(self,privacy_password):
		try :
			if not isinstance(privacy_password,str):
				raise TypeError("privacy_password must be set to str value")
			self._privacy_password = privacy_password
		except Exception as e :
			raise e


	'''
	get SNMP View Name attached to the SNMP User
	'''
	@property
	def view_name(self) :
		try:
			return self._view_name
		except Exception as e :
			raise e
	'''
	set SNMP View Name attached to the SNMP User
	'''
	@view_name.setter
	def view_name(self,view_name):
		try :
			if not isinstance(view_name,str):
				raise TypeError("view_name must be set to str value")
			self._view_name = view_name
		except Exception as e :
			raise e


	'''
	get Authentication Protocol of SNMP User. Values: 0:noValue, 1: MD5, 2: SHA1
	'''
	@property
	def auth_protocol(self) :
		try:
			return self._auth_protocol
		except Exception as e :
			raise e
	'''
	set Authentication Protocol of SNMP User. Values: 0:noValue, 1: MD5, 2: SHA1
	'''
	@auth_protocol.setter
	def auth_protocol(self,auth_protocol):
		try :
			if not isinstance(auth_protocol,int):
				raise TypeError("auth_protocol must be set to int value")
			self._auth_protocol = auth_protocol
		except Exception as e :
			raise e

	'''
	Use this operation to add SNMP User.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				snmp_user_obj= snmp_user()
				return cls.perform_operation_bulk_request(service,"add", resource,snmp_user_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete SNMP User.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					snmp_user_obj=snmp_user()
					return cls.delete_bulk_request(client,resource,snmp_user_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get SNMP User details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_user_obj=snmp_user()
				response = snmp_user_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify SNMP User.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_user_obj=snmp_user()
				return cls.update_bulk_request(client,resource,snmp_user_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_user resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_user_obj = snmp_user()
			option_ = options()
			option_._filter=filter_
			return snmp_user_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_user resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_user_obj = snmp_user()
			option_ = options()
			option_._count=True
			response = snmp_user_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_user resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_user_obj = snmp_user()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_user_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_user_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_user
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_user_responses, response, "snmp_user_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_user_response_array
				i=0
				error = [snmp_user() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_user_response_array
			i=0
			snmp_user_objs = [snmp_user() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_user'):
					for props in obj._snmp_user:
						result = service.payload_formatter.string_to_bulk_resource(snmp_user_response,self.__class__.__name__,props)
						snmp_user_objs[i] = result.snmp_user
						i=i+1
			return snmp_user_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_user,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_user_response(base_response):
	def __init__(self,length=1) :
		self.snmp_user= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_user= [ snmp_user() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_user_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_user_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_user_response_array = [ snmp_user() for _ in range(length)]
