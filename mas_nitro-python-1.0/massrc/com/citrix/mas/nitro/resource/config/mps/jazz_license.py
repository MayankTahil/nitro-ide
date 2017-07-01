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
Configuration for Jazz License Information resource
'''

class jazz_license(base_resource):
	_date_purchased= ""
	_session_id= ""
	_features= ""
	_relevance= ""
	_name= ""
	_serial_no= ""
	_count_total= ""
	_count_available= ""
	_id= ""
	_date_exp= ""
	_bind_type= ""
	_use_proxy= ""
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
			return "jazz_license"
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
			return "jazz_licenses"
		except Exception as e :
			raise e



	'''
	get Purchase Date for license
	'''
	@property
	def date_purchased(self) :
		try:
			return self._date_purchased
		except Exception as e :
			raise e
	'''
	set Purchase Date for license
	'''
	@date_purchased.setter
	def date_purchased(self,date_purchased):
		try :
			if not isinstance(date_purchased,str):
				raise TypeError("date_purchased must be set to str value")
			self._date_purchased = date_purchased
		except Exception as e :
			raise e


	'''
	get Session id for license
	'''
	@property
	def session_id(self) :
		try:
			return self._session_id
		except Exception as e :
			raise e
	'''
	set Session id for license
	'''
	@session_id.setter
	def session_id(self,session_id):
		try :
			if not isinstance(session_id,str):
				raise TypeError("session_id must be set to str value")
			self._session_id = session_id
		except Exception as e :
			raise e


	'''
	get Features for license
	'''
	@property
	def features(self) :
		try:
			return self._features
		except Exception as e :
			raise e
	'''
	set Features for license
	'''
	@features.setter
	def features(self,features):
		try :
			if not isinstance(features,str):
				raise TypeError("features must be set to str value")
			self._features = features
		except Exception as e :
			raise e


	'''
	get Relevance of license
	'''
	@property
	def relevance(self) :
		try:
			return self._relevance
		except Exception as e :
			raise e
	'''
	set Relevance of license
	'''
	@relevance.setter
	def relevance(self,relevance):
		try :
			if not isinstance(relevance,int):
				raise TypeError("relevance must be set to int value")
			self._relevance = relevance
		except Exception as e :
			raise e


	'''
	get Name of license
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of license
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
	get Serial Number for license
	'''
	@property
	def serial_no(self) :
		try:
			return self._serial_no
		except Exception as e :
			raise e
	'''
	set Serial Number for license
	'''
	@serial_no.setter
	def serial_no(self,serial_no):
		try :
			if not isinstance(serial_no,str):
				raise TypeError("serial_no must be set to str value")
			self._serial_no = serial_no
		except Exception as e :
			raise e


	'''
	get Count Total of license
	'''
	@property
	def count_total(self) :
		try:
			return self._count_total
		except Exception as e :
			raise e
	'''
	set Count Total of license
	'''
	@count_total.setter
	def count_total(self,count_total):
		try :
			if not isinstance(count_total,int):
				raise TypeError("count_total must be set to int value")
			self._count_total = count_total
		except Exception as e :
			raise e


	'''
	get Count Available of license
	'''
	@property
	def count_available(self) :
		try:
			return self._count_available
		except Exception as e :
			raise e
	'''
	set Count Available of license
	'''
	@count_available.setter
	def count_available(self,count_available):
		try :
			if not isinstance(count_available,int):
				raise TypeError("count_available must be set to int value")
			self._count_available = count_available
		except Exception as e :
			raise e


	'''
	get ID for license
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set ID for license
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
	get Expiry Date for license
	'''
	@property
	def date_exp(self) :
		try:
			return self._date_exp
		except Exception as e :
			raise e
	'''
	set Expiry Date for license
	'''
	@date_exp.setter
	def date_exp(self,date_exp):
		try :
			if not isinstance(date_exp,str):
				raise TypeError("date_exp must be set to str value")
			self._date_exp = date_exp
		except Exception as e :
			raise e


	'''
	get Bind Type for license
	'''
	@property
	def bind_type(self) :
		try:
			return self._bind_type
		except Exception as e :
			raise e
	'''
	set Bind Type for license
	'''
	@bind_type.setter
	def bind_type(self,bind_type):
		try :
			if not isinstance(bind_type,str):
				raise TypeError("bind_type must be set to str value")
			self._bind_type = bind_type
		except Exception as e :
			raise e


	'''
	get Use license proxy configured to connect to citrix backoffice
	'''
	@property
	def use_proxy(self) :
		try:
			return self._use_proxy
		except Exception as e :
			raise e
	'''
	set Use license proxy configured to connect to citrix backoffice
	'''
	@use_proxy.setter
	def use_proxy(self,use_proxy):
		try :
			if not isinstance(use_proxy,bool):
				raise TypeError("use_proxy must be set to bool value")
			self._use_proxy = use_proxy
		except Exception as e :
			raise e

	'''
	Use this operation to Fetch new licenses files.
	'''
	@classmethod
	def fetch(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"fetch")
		except Exception as e :
			raise e

	'''
	Use this operation to get license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				jazz_license_obj=jazz_license()
				response = jazz_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of jazz_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			jazz_license_obj = jazz_license()
			option_ = options()
			option_._filter=filter_
			return jazz_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the jazz_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			jazz_license_obj = jazz_license()
			option_ = options()
			option_._count=True
			response = jazz_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of jazz_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			jazz_license_obj = jazz_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = jazz_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(jazz_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.jazz_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(jazz_license_responses, response, "jazz_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.jazz_license_response_array
				i=0
				error = [jazz_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.jazz_license_response_array
			i=0
			jazz_license_objs = [jazz_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_jazz_license'):
					for props in obj._jazz_license:
						result = service.payload_formatter.string_to_bulk_resource(jazz_license_response,self.__class__.__name__,props)
						jazz_license_objs[i] = result.jazz_license
						i=i+1
			return jazz_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(jazz_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class jazz_license_response(base_response):
	def __init__(self,length=1) :
		self.jazz_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.jazz_license= [ jazz_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class jazz_license_responses(base_response):
	def __init__(self,length=1) :
		self.jazz_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.jazz_license_response_array = [ jazz_license() for _ in range(length)]
