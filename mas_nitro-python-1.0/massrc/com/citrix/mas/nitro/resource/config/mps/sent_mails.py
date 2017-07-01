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
Configuration for Sent mail record item keeping. resource
'''

class sent_mails(base_resource):
	_to_list= ""
	_failed_message= ""
	_subject= ""
	_bcc_list= ""
	_is_auth= ""
	_cc_list= ""
	_port= ""
	_is_sent= ""
	_message= ""
	_username= ""
	_timestamp= ""
	_id= ""
	_is_ssl= ""
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
			return "sent_mails"
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
			return "sent_mailss"
		except Exception as e :
			raise e



	'''
	get List of to whom send the mail. 
	'''
	@property
	def to_list(self) :
		try:
			return self._to_list
		except Exception as e :
			raise e
	'''
	set List of to whom send the mail. 
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
	get Subject of the mail sent.
	'''
	@property
	def failed_message(self) :
		try:
			return self._failed_message
		except Exception as e :
			raise e
	'''
	set Subject of the mail sent.
	'''
	@failed_message.setter
	def failed_message(self,failed_message):
		try :
			if not isinstance(failed_message,str):
				raise TypeError("failed_message must be set to str value")
			self._failed_message = failed_message
		except Exception as e :
			raise e


	'''
	get Subject of the mail sent.
	'''
	@property
	def subject(self) :
		try:
			return self._subject
		except Exception as e :
			raise e
	'''
	set Subject of the mail sent.
	'''
	@subject.setter
	def subject(self,subject):
		try :
			if not isinstance(subject,str):
				raise TypeError("subject must be set to str value")
			self._subject = subject
		except Exception as e :
			raise e


	'''
	get List to whom BCC the mail.
	'''
	@property
	def bcc_list(self) :
		try:
			return self._bcc_list
		except Exception as e :
			raise e
	'''
	set List to whom BCC the mail.
	'''
	@bcc_list.setter
	def bcc_list(self,bcc_list):
		try :
			if not isinstance(bcc_list,str):
				raise TypeError("bcc_list must be set to str value")
			self._bcc_list = bcc_list
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
	get List to whom CC the mail.
	'''
	@property
	def cc_list(self) :
		try:
			return self._cc_list
		except Exception as e :
			raise e
	'''
	set List to whom CC the mail.
	'''
	@cc_list.setter
	def cc_list(self,cc_list):
		try :
			if not isinstance(cc_list,str):
				raise TypeError("cc_list must be set to str value")
			self._cc_list = cc_list
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
	get Is this mail sent successfully.
	'''
	@property
	def is_sent(self) :
		try:
			return self._is_sent
		except Exception as e :
			raise e
	'''
	set Is this mail sent successfully.
	'''
	@is_sent.setter
	def is_sent(self,is_sent):
		try :
			if not isinstance(is_sent,bool):
				raise TypeError("is_sent must be set to bool value")
			self._is_sent = is_sent
		except Exception as e :
			raise e


	'''
	get Content of the mail sent.
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e
	'''
	set Content of the mail sent.
	'''
	@message.setter
	def message(self,message):
		try :
			if not isinstance(message,str):
				raise TypeError("message must be set to str value")
			self._message = message
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
	get Time when the mail was sent
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the sent mail record.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the sent mail record.
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
	get Profile name through which mail sent.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name through which mail sent.
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
	Use this operation to delete sent mail details..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					sent_mails_obj=sent_mails()
					return cls.delete_bulk_request(client,resource,sent_mails_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get sent mail details..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				sent_mails_obj=sent_mails()
				response = sent_mails_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of sent_mails resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			sent_mails_obj = sent_mails()
			option_ = options()
			option_._filter=filter_
			return sent_mails_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the sent_mails resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			sent_mails_obj = sent_mails()
			option_ = options()
			option_._count=True
			response = sent_mails_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of sent_mails resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			sent_mails_obj = sent_mails()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = sent_mails_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(sent_mails_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sent_mails
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(sent_mails_responses, response, "sent_mails_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.sent_mails_response_array
				i=0
				error = [sent_mails() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.sent_mails_response_array
			i=0
			sent_mails_objs = [sent_mails() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_sent_mails'):
					for props in obj._sent_mails:
						result = service.payload_formatter.string_to_bulk_resource(sent_mails_response,self.__class__.__name__,props)
						sent_mails_objs[i] = result.sent_mails
						i=i+1
			return sent_mails_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(sent_mails,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class sent_mails_response(base_response):
	def __init__(self,length=1) :
		self.sent_mails= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.sent_mails= [ sent_mails() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class sent_mails_responses(base_response):
	def __init__(self,length=1) :
		self.sent_mails_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.sent_mails_response_array = [ sent_mails() for _ in range(length)]
