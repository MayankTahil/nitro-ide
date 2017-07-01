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
Configuration for SSL Settings resource
'''

class ssl_settings(base_resource):
	_sslreneg= ""
	_tlsv1= ""
	_sslv3= ""
	_tlsv1_1= ""
	_tlsv1_2= ""
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
			return "ssl_settings"
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
			return "ssl_settingss"
		except Exception as e :
			raise e



	'''
	get Enable SSL Renegotiation
	'''
	@property
	def sslreneg(self) :
		try:
			return self._sslreneg
		except Exception as e :
			raise e
	'''
	set Enable SSL Renegotiation
	'''
	@sslreneg.setter
	def sslreneg(self,sslreneg):
		try :
			if not isinstance(sslreneg,bool):
				raise TypeError("sslreneg must be set to bool value")
			self._sslreneg = sslreneg
		except Exception as e :
			raise e


	'''
	get Enable TLSv1
	'''
	@property
	def tlsv1(self) :
		try:
			return self._tlsv1
		except Exception as e :
			raise e
	'''
	set Enable TLSv1
	'''
	@tlsv1.setter
	def tlsv1(self,tlsv1):
		try :
			if not isinstance(tlsv1,bool):
				raise TypeError("tlsv1 must be set to bool value")
			self._tlsv1 = tlsv1
		except Exception as e :
			raise e


	'''
	get Enable SSLv3
	'''
	@property
	def sslv3(self) :
		try:
			return self._sslv3
		except Exception as e :
			raise e
	'''
	set Enable SSLv3
	'''
	@sslv3.setter
	def sslv3(self,sslv3):
		try :
			if not isinstance(sslv3,bool):
				raise TypeError("sslv3 must be set to bool value")
			self._sslv3 = sslv3
		except Exception as e :
			raise e


	'''
	get Enable TLSv1.1
	'''
	@property
	def tlsv1_1(self) :
		try:
			return self._tlsv1_1
		except Exception as e :
			raise e
	'''
	set Enable TLSv1.1
	'''
	@tlsv1_1.setter
	def tlsv1_1(self,tlsv1_1):
		try :
			if not isinstance(tlsv1_1,bool):
				raise TypeError("tlsv1_1 must be set to bool value")
			self._tlsv1_1 = tlsv1_1
		except Exception as e :
			raise e


	'''
	get Enable TLSv1.2
	'''
	@property
	def tlsv1_2(self) :
		try:
			return self._tlsv1_2
		except Exception as e :
			raise e
	'''
	set Enable TLSv1.2
	'''
	@tlsv1_2.setter
	def tlsv1_2(self,tlsv1_2):
		try :
			if not isinstance(tlsv1_2,bool):
				raise TypeError("tlsv1_2 must be set to bool value")
			self._tlsv1_2 = tlsv1_2
		except Exception as e :
			raise e

	'''
	Use this operation to get ssl settings.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ssl_settings_obj=ssl_settings()
				response = ssl_settings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify ssl settings.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ssl_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ssl_settings_obj = ssl_settings()
			option_ = options()
			option_._filter=filter_
			return ssl_settings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ssl_settings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ssl_settings_obj = ssl_settings()
			option_ = options()
			option_._count=True
			response = ssl_settings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ssl_settings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ssl_settings_obj = ssl_settings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ssl_settings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ssl_settings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssl_settings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ssl_settings_responses, response, "ssl_settings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ssl_settings_response_array
				i=0
				error = [ssl_settings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ssl_settings_response_array
			i=0
			ssl_settings_objs = [ssl_settings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ssl_settings'):
					for props in obj._ssl_settings:
						result = service.payload_formatter.string_to_bulk_resource(ssl_settings_response,self.__class__.__name__,props)
						ssl_settings_objs[i] = result.ssl_settings
						i=i+1
			return ssl_settings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ssl_settings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ssl_settings_response(base_response):
	def __init__(self,length=1) :
		self.ssl_settings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ssl_settings= [ ssl_settings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ssl_settings_responses(base_response):
	def __init__(self,length=1) :
		self.ssl_settings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ssl_settings_response_array = [ ssl_settings() for _ in range(length)]
