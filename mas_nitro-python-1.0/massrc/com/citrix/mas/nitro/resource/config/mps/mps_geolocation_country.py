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
Configuration for Geolocation Country Information resource
'''

class mps_geolocation_country(base_resource):
	_name= ""
	_code= ""
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
			return "mps_geolocation_country"
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
			return "mps_geolocation_countrys"
		except Exception as e :
			raise e



	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get country_code
	'''
	@property
	def code(self) :
		try:
			return self._code
		except Exception as e :
			raise e
	'''
	set country_code
	'''
	@code.setter
	def code(self,code):
		try :
			if not isinstance(code,str):
				raise TypeError("code must be set to str value")
			self._code = code
		except Exception as e :
			raise e

	'''
	Use this operation to get device summary report.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_geolocation_country_obj=mps_geolocation_country()
				response = mps_geolocation_country_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_geolocation_country resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_geolocation_country_obj = mps_geolocation_country()
			option_ = options()
			option_._filter=filter_
			return mps_geolocation_country_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_geolocation_country resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_geolocation_country_obj = mps_geolocation_country()
			option_ = options()
			option_._count=True
			response = mps_geolocation_country_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_geolocation_country resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_geolocation_country_obj = mps_geolocation_country()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_geolocation_country_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_geolocation_country_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_geolocation_country
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_geolocation_country_responses, response, "mps_geolocation_country_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_geolocation_country_response_array
				i=0
				error = [mps_geolocation_country() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_geolocation_country_response_array
			i=0
			mps_geolocation_country_objs = [mps_geolocation_country() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_geolocation_country'):
					for props in obj._mps_geolocation_country:
						result = service.payload_formatter.string_to_bulk_resource(mps_geolocation_country_response,self.__class__.__name__,props)
						mps_geolocation_country_objs[i] = result.mps_geolocation_country
						i=i+1
			return mps_geolocation_country_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_geolocation_country,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_geolocation_country_response(base_response):
	def __init__(self,length=1) :
		self.mps_geolocation_country= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_geolocation_country= [ mps_geolocation_country() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_geolocation_country_responses(base_response):
	def __init__(self,length=1) :
		self.mps_geolocation_country_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_geolocation_country_response_array = [ mps_geolocation_country() for _ in range(length)]
