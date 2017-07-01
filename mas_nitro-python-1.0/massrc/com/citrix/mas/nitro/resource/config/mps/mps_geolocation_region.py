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
Configuration for Geolocation Region Information resource
'''

class mps_geolocation_region(base_resource):
	_region_code= ""
	_region_name= ""
	_country_code= ""
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
			return "mps_geolocation_region"
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
			return "mps_geolocation_regions"
		except Exception as e :
			raise e



	'''
	get region_code
	'''
	@property
	def region_code(self) :
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	set region_code
	'''
	@region_code.setter
	def region_code(self,region_code):
		try :
			if not isinstance(region_code,str):
				raise TypeError("region_code must be set to str value")
			self._region_code = region_code
		except Exception as e :
			raise e


	'''
	get region_name
	'''
	@property
	def region_name(self) :
		try:
			return self._region_name
		except Exception as e :
			raise e
	'''
	set region_name
	'''
	@region_name.setter
	def region_name(self,region_name):
		try :
			if not isinstance(region_name,str):
				raise TypeError("region_name must be set to str value")
			self._region_name = region_name
		except Exception as e :
			raise e


	'''
	get country_code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set country_code
	'''
	@country_code.setter
	def country_code(self,country_code):
		try :
			if not isinstance(country_code,str):
				raise TypeError("country_code must be set to str value")
			self._country_code = country_code
		except Exception as e :
			raise e

	'''
	Use this operation to get ip block.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_geolocation_region_obj=mps_geolocation_region()
				response = mps_geolocation_region_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_geolocation_region resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_geolocation_region_obj = mps_geolocation_region()
			option_ = options()
			option_._filter=filter_
			return mps_geolocation_region_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_geolocation_region resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_geolocation_region_obj = mps_geolocation_region()
			option_ = options()
			option_._count=True
			response = mps_geolocation_region_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_geolocation_region resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_geolocation_region_obj = mps_geolocation_region()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_geolocation_region_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_geolocation_region_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_geolocation_region
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_geolocation_region_responses, response, "mps_geolocation_region_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_geolocation_region_response_array
				i=0
				error = [mps_geolocation_region() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_geolocation_region_response_array
			i=0
			mps_geolocation_region_objs = [mps_geolocation_region() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_geolocation_region'):
					for props in obj._mps_geolocation_region:
						result = service.payload_formatter.string_to_bulk_resource(mps_geolocation_region_response,self.__class__.__name__,props)
						mps_geolocation_region_objs[i] = result.mps_geolocation_region
						i=i+1
			return mps_geolocation_region_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_geolocation_region,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_geolocation_region_response(base_response):
	def __init__(self,length=1) :
		self.mps_geolocation_region= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_geolocation_region= [ mps_geolocation_region() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_geolocation_region_responses(base_response):
	def __init__(self,length=1) :
		self.mps_geolocation_region_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_geolocation_region_response_array = [ mps_geolocation_region() for _ in range(length)]
