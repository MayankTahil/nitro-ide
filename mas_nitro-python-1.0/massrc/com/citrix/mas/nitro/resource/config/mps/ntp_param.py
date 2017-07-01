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
Configuration for NTP Parameters resource
'''

class ntp_param(base_resource):
	_trusted_key_list=[]
	_automax_logsec= ""
	_revoke_logsec= ""
	_authentication= ""
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
			return "ntp_param"
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
			return "ntp_params"
		except Exception as e :
			raise e



	'''
	get List of Trusted Key Identifiers for Symmetric Key Cryptography
	'''
	@property
	def trusted_key_list(self) :
		try:
			return self._trusted_key_list
		except Exception as e :
			raise e
	'''
	set List of Trusted Key Identifiers for Symmetric Key Cryptography
	'''
	@trusted_key_list.setter
	def trusted_key_list(self,trusted_key_list) :
		try :
			if not isinstance(trusted_key_list,list):
				raise TypeError("trusted_key_list must be set to array of int value")
			for item in trusted_key_list :
				if not isinstance(item,int):
					raise TypeError("item must be set to int value")
			self._trusted_key_list = trusted_key_list
		except Exception as e :
			raise e


	'''
	get Automax Interval (as power of 2 in seconds)
	'''
	@property
	def automax_logsec(self) :
		try:
			return self._automax_logsec
		except Exception as e :
			raise e
	'''
	set Automax Interval (as power of 2 in seconds)
	'''
	@automax_logsec.setter
	def automax_logsec(self,automax_logsec):
		try :
			if not isinstance(automax_logsec,int):
				raise TypeError("automax_logsec must be set to int value")
			self._automax_logsec = automax_logsec
		except Exception as e :
			raise e


	'''
	get Revoke Interval (as power of 2 in seconds)
	'''
	@property
	def revoke_logsec(self) :
		try:
			return self._revoke_logsec
		except Exception as e :
			raise e
	'''
	set Revoke Interval (as power of 2 in seconds)
	'''
	@revoke_logsec.setter
	def revoke_logsec(self,revoke_logsec):
		try :
			if not isinstance(revoke_logsec,int):
				raise TypeError("revoke_logsec must be set to int value")
			self._revoke_logsec = revoke_logsec
		except Exception as e :
			raise e


	'''
	get Authentication Enabled
	'''
	@property
	def authentication(self) :
		try:
			return self._authentication
		except Exception as e :
			raise e
	'''
	set Authentication Enabled
	'''
	@authentication.setter
	def authentication(self,authentication):
		try :
			if not isinstance(authentication,bool):
				raise TypeError("authentication must be set to bool value")
			self._authentication = authentication
		except Exception as e :
			raise e

	'''
	Use this operation to get NTP Server.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ntp_param_obj=ntp_param()
				response = ntp_param_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify NTP Server.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ntp_param_obj=ntp_param()
				return cls.update_bulk_request(client,resource,ntp_param_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ntp_param resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ntp_param_obj = ntp_param()
			option_ = options()
			option_._filter=filter_
			return ntp_param_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ntp_param resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ntp_param_obj = ntp_param()
			option_ = options()
			option_._count=True
			response = ntp_param_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ntp_param resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ntp_param_obj = ntp_param()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ntp_param_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ntp_param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ntp_param
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ntp_param_responses, response, "ntp_param_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ntp_param_response_array
				i=0
				error = [ntp_param() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ntp_param_response_array
			i=0
			ntp_param_objs = [ntp_param() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ntp_param'):
					for props in obj._ntp_param:
						result = service.payload_formatter.string_to_bulk_resource(ntp_param_response,self.__class__.__name__,props)
						ntp_param_objs[i] = result.ntp_param
						i=i+1
			return ntp_param_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ntp_param,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ntp_param_response(base_response):
	def __init__(self,length=1) :
		self.ntp_param= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ntp_param= [ ntp_param() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ntp_param_responses(base_response):
	def __init__(self,length=1) :
		self.ntp_param_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ntp_param_response_array = [ ntp_param() for _ in range(length)]
