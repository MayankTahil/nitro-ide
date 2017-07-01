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


from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for Login/Logout resource
'''

class login(base_resource):
	_permission= ""
	_session_timeout= ""
	_username= ""
	_password= ""
	_challenge= ""
	_challenge_response= ""
	_client_ip= ""
	_client_port= ""
	_sessionid= ""
	_token= ""
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
			return "login"
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
			return "logins"
		except Exception as e :
			raise e


	'''
	Actions that this user is authorized to perform
	'''
	@property
	def permission(self):
		try:
			return self._permission
		except Exception as e :
			raise e
	'''
	Actions that this user is authorized to perform
	'''
	@permission.setter
	def permission(self,permission):
		try :
			if not isinstance(permission,str):
				raise TypeError("permission must be set to str value")
			self._permission = permission
		except Exception as e :
			raise e

	'''
	Session Timeout in seconds, if no activity is performed for specified time then session will be expired
	'''
	@property
	def session_timeout(self):
		try:
			return self._session_timeout
		except Exception as e :
			raise e
	'''
	Session Timeout in seconds, if no activity is performed for specified time then session will be expired
	'''
	@session_timeout.setter
	def session_timeout(self,session_timeout):
		try :
			if not isinstance(session_timeout,int):
				raise TypeError("session_timeout must be set to int value")
			self._session_timeout = session_timeout
		except Exception as e :
			raise e

	'''
	User Name that wants to login
	'''
	@property
	def username(self):
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	User Name that wants to login
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
	Password
	'''
	@property
	def password(self):
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	Password
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
	Challenge request for authentication
	'''
	@property
	def challenge(self):
		try:
			return self._challenge
		except Exception as e :
			raise e
	'''
	Challenge request for authentication
	'''
	@challenge.setter
	def challenge(self,challenge):
		try :
			if not isinstance(challenge,str):
				raise TypeError("challenge must be set to str value")
			self._challenge = challenge
		except Exception as e :
			raise e

	'''
	Challenge response for authentication
	'''
	@property
	def challenge_response(self):
		try:
			return self._challenge_response
		except Exception as e :
			raise e
	'''
	Challenge response for authentication
	'''
	@challenge_response.setter
	def challenge_response(self,challenge_response):
		try :
			if not isinstance(challenge_response,str):
				raise TypeError("challenge_response must be set to str value")
			self._challenge_response = challenge_response
		except Exception as e :
			raise e

	'''
	Login client IP
	'''
	@property
	def client_ip(self):
		try:
			return self._client_ip
		except Exception as e :
			raise e
	'''
	Login client IP
	'''
	@client_ip.setter
	def client_ip(self,client_ip):
		try :
			if not isinstance(client_ip,str):
				raise TypeError("client_ip must be set to str value")
			self._client_ip = client_ip
		except Exception as e :
			raise e

	'''
	Login Client port
	'''
	@property
	def client_port(self):
		try:
			return self._client_port
		except Exception as e :
			raise e
	'''
	Login Client port
	'''
	@client_port.setter
	def client_port(self,client_port):
		try :
			if not isinstance(client_port,int):
				raise TypeError("client_port must be set to int value")
			self._client_port = client_port
		except Exception as e :
			raise e

	'''
	Session ID would only be set if login was performed successfully
	'''
	@property
	def sessionid(self):
		try:
			return self._sessionid
		except Exception as e :
			raise e
	'''
	Session ID would only be set if login was performed successfully
	'''
	@sessionid.setter
	def sessionid(self,sessionid):
		try :
			if not isinstance(sessionid,str):
				raise TypeError("sessionid must be set to str value")
			self._sessionid = sessionid
		except Exception as e :
			raise e

	'''
	Random token to identify session during logout
	'''
	@property
	def token(self):
		try:
			return self._token
		except Exception as e :
			raise e
	'''
	Random token to identify session during logout
	'''
	@token.setter
	def token(self,token):
		try :
			if not isinstance(token,str):
				raise TypeError("token must be set to str value")
			self._token = token
		except Exception as e :
			raise e

	'''
	Login.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				login_obj= login()
				return cls.perform_operation_bulk_request(service,"add", resource,login_obj)
		except Exception as e :
			raise e

	'''
	Logout.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					login_obj=login()
					return cls.delete_bulk_request(client,resource,login_obj)
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(login_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.login
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(login_responses, response, "login_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.login_response_array
				i=0
				error = [login() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.login_response_array
			i=0
			login_objs = [login() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_login'):
					for props in obj._login:
						result = service.payload_formatter.string_to_bulk_resource(login_response,self.__class__.__name__,props)
						login_objs[i] = result.login
						i=i+1
			return login_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(login,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class login_response(base_response):
	def __init__(self,length=1) :
		self.login= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.login= [ login() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class login_responses(base_response):
	def __init__(self,length=1) :
		self.login_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.login_response_array = [ login() for _ in range(length)]
