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
Configuration for Company Information of Tenant resource
'''

class tenant_company_info(base_resource):
	_department= ""
	_company_name= ""
	_zip_code= ""
	_state= ""
	_last_name= ""
	_parent_id= ""
	_city= ""
	_tenant_id= ""
	_url= ""
	_address= ""
	_id= ""
	_email_address= ""
	_country= ""
	_parent_name= ""
	_phone_number= ""
	_preferred_lang= ""
	_first_name= ""
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
			return "tenant_company_info"
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
			return "tenant_company_infos"
		except Exception as e :
			raise e



	'''
	get Department of the tenant
	'''
	@property
	def department(self) :
		try:
			return self._department
		except Exception as e :
			raise e
	'''
	set Department of the tenant
	'''
	@department.setter
	def department(self,department):
		try :
			if not isinstance(department,str):
				raise TypeError("department must be set to str value")
			self._department = department
		except Exception as e :
			raise e


	'''
	get Name of the tenant company
	'''
	@property
	def company_name(self) :
		try:
			return self._company_name
		except Exception as e :
			raise e
	'''
	set Name of the tenant company
	'''
	@company_name.setter
	def company_name(self,company_name):
		try :
			if not isinstance(company_name,str):
				raise TypeError("company_name must be set to str value")
			self._company_name = company_name
		except Exception as e :
			raise e


	'''
	get Zipcode of the tenant
	'''
	@property
	def zip_code(self) :
		try:
			return self._zip_code
		except Exception as e :
			raise e
	'''
	set Zipcode of the tenant
	'''
	@zip_code.setter
	def zip_code(self,zip_code):
		try :
			if not isinstance(zip_code,str):
				raise TypeError("zip_code must be set to str value")
			self._zip_code = zip_code
		except Exception as e :
			raise e


	'''
	get State of the tenant
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set State of the tenant
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get URL of the tenant
	'''
	@property
	def last_name(self) :
		try:
			return self._last_name
		except Exception as e :
			raise e
	'''
	set URL of the tenant
	'''
	@last_name.setter
	def last_name(self,last_name):
		try :
			if not isinstance(last_name,str):
				raise TypeError("last_name must be set to str value")
			self._last_name = last_name
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get City of the tenant
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set City of the tenant
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e


	'''
	get Id of the parent tenant
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Id of the parent tenant
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get URL of the tenant
	'''
	@property
	def url(self) :
		try:
			return self._url
		except Exception as e :
			raise e
	'''
	set URL of the tenant
	'''
	@url.setter
	def url(self,url):
		try :
			if not isinstance(url,str):
				raise TypeError("url must be set to str value")
			self._url = url
		except Exception as e :
			raise e


	'''
	get URL of the tenant
	'''
	@property
	def address(self) :
		try:
			return self._address
		except Exception as e :
			raise e
	'''
	set URL of the tenant
	'''
	@address.setter
	def address(self,address):
		try :
			if not isinstance(address,str):
				raise TypeError("address must be set to str value")
			self._address = address
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	get Email Address of the tenant
	'''
	@property
	def email_address(self) :
		try:
			return self._email_address
		except Exception as e :
			raise e
	'''
	set Email Address of the tenant
	'''
	@email_address.setter
	def email_address(self,email_address):
		try :
			if not isinstance(email_address,str):
				raise TypeError("email_address must be set to str value")
			self._email_address = email_address
		except Exception as e :
			raise e


	'''
	get Country of the tenant
	'''
	@property
	def country(self) :
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	set Country of the tenant
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get Phone number of the tenant
	'''
	@property
	def phone_number(self) :
		try:
			return self._phone_number
		except Exception as e :
			raise e
	'''
	set Phone number of the tenant
	'''
	@phone_number.setter
	def phone_number(self,phone_number):
		try :
			if not isinstance(phone_number,str):
				raise TypeError("phone_number must be set to str value")
			self._phone_number = phone_number
		except Exception as e :
			raise e


	'''
	get Preferred Language
	'''
	@property
	def preferred_lang(self) :
		try:
			return self._preferred_lang
		except Exception as e :
			raise e
	'''
	set Preferred Language
	'''
	@preferred_lang.setter
	def preferred_lang(self,preferred_lang):
		try :
			if not isinstance(preferred_lang,str):
				raise TypeError("preferred_lang must be set to str value")
			self._preferred_lang = preferred_lang
		except Exception as e :
			raise e


	'''
	get First name of the tenant
	'''
	@property
	def first_name(self) :
		try:
			return self._first_name
		except Exception as e :
			raise e
	'''
	set First name of the tenant
	'''
	@first_name.setter
	def first_name(self,first_name):
		try :
			if not isinstance(first_name,str):
				raise TypeError("first_name must be set to str value")
			self._first_name = first_name
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_company_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tenant_company_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(tenant_company_info_responses, response, "tenant_company_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.tenant_company_info_response_array
				i=0
				error = [tenant_company_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.tenant_company_info_response_array
			i=0
			tenant_company_info_objs = [tenant_company_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_tenant_company_info'):
					for props in obj._tenant_company_info:
						result = service.payload_formatter.string_to_bulk_resource(tenant_company_info_response,self.__class__.__name__,props)
						tenant_company_info_objs[i] = result.tenant_company_info
						i=i+1
			return tenant_company_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(tenant_company_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class tenant_company_info_response(base_response):
	def __init__(self,length=1) :
		self.tenant_company_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.tenant_company_info= [ tenant_company_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class tenant_company_info_responses(base_response):
	def __init__(self,length=1) :
		self.tenant_company_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.tenant_company_info_response_array = [ tenant_company_info() for _ in range(length)]
