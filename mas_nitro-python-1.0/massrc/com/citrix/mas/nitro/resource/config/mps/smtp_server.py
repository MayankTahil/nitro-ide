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
Configuration for SMTP server properties  resource
'''

class smtp_server(base_resource):
	_sender_mail_id= ""
	_is_auth= ""
	_port= ""
	_username= ""
	_password= ""
	_tenant_id= ""
	_id= ""
	_is_ssl= ""
	_server_name= ""
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
			return "smtp_server"
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
			return "smtp_servers"
		except Exception as e :
			raise e



	'''
	get Email Address from which email is to be sent
	'''
	@property
	def sender_mail_id(self) :
		try:
			return self._sender_mail_id
		except Exception as e :
			raise e
	'''
	set Email Address from which email is to be sent
	'''
	@sender_mail_id.setter
	def sender_mail_id(self,sender_mail_id):
		try :
			if not isinstance(sender_mail_id,str):
				raise TypeError("sender_mail_id must be set to str value")
			self._sender_mail_id = sender_mail_id
		except Exception as e :
			raise e


	'''
	get Is authentication enabled for this smtp server
	'''
	@property
	def is_auth(self) :
		try:
			return self._is_auth
		except Exception as e :
			raise e
	'''
	set Is authentication enabled for this smtp server
	'''
	@is_auth.setter
	def is_auth(self,is_auth):
		try :
			if not isinstance(is_auth,bool):
				raise TypeError("is_auth must be set to bool value")
			self._is_auth = is_auth
		except Exception as e :
			raise e


	'''
	get SMTP Server port address.
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set SMTP Server port address.
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,int):
				raise TypeError("port must be set to int value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get Username for the smtp server
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set Username for the smtp server
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
	get Password for the smtp server
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password for the smtp server
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
	get Tenant Id of the Config Jobs
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the smtp server
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the smtp server
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
	get Is this smtp server is SSL support configured.
	'''
	@property
	def is_ssl(self) :
		try:
			return self._is_ssl
		except Exception as e :
			raise e
	'''
	set Is this smtp server is SSL support configured.
	'''
	@is_ssl.setter
	def is_ssl(self,is_ssl):
		try :
			if not isinstance(is_ssl,bool):
				raise TypeError("is_ssl must be set to bool value")
			self._is_ssl = is_ssl
		except Exception as e :
			raise e


	'''
	get SMTP server name
	'''
	@property
	def server_name(self) :
		try:
			return self._server_name
		except Exception as e :
			raise e
	'''
	set SMTP server name
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
	Use this operation to add smtp server.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				smtp_server_obj= smtp_server()
				return cls.perform_operation_bulk_request(service,"add", resource,smtp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete smtp server.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					smtp_server_obj=smtp_server()
					return cls.delete_bulk_request(client,resource,smtp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get smtp server details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				smtp_server_obj=smtp_server()
				response = smtp_server_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify smtp server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				smtp_server_obj=smtp_server()
				return cls.update_bulk_request(client,resource,smtp_server_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of smtp_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			smtp_server_obj = smtp_server()
			option_ = options()
			option_._filter=filter_
			return smtp_server_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the smtp_server resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			smtp_server_obj = smtp_server()
			option_ = options()
			option_._count=True
			response = smtp_server_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of smtp_server resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			smtp_server_obj = smtp_server()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = smtp_server_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(smtp_server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.smtp_server
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(smtp_server_responses, response, "smtp_server_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.smtp_server_response_array
				i=0
				error = [smtp_server() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.smtp_server_response_array
			i=0
			smtp_server_objs = [smtp_server() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_smtp_server'):
					for props in obj._smtp_server:
						result = service.payload_formatter.string_to_bulk_resource(smtp_server_response,self.__class__.__name__,props)
						smtp_server_objs[i] = result.smtp_server
						i=i+1
			return smtp_server_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(smtp_server,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class smtp_server_response(base_response):
	def __init__(self,length=1) :
		self.smtp_server= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.smtp_server= [ smtp_server() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class smtp_server_responses(base_response):
	def __init__(self,length=1) :
		self.smtp_server_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.smtp_server_response_array = [ smtp_server() for _ in range(length)]
