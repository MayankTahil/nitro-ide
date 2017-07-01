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
Configuration for mps_user_heatmap resource.
'''

class mps_user_heatmap(base_resource):
	_hits= ""
	_region_code= ""
	_lat= ""
	_total_bytes= ""
	_lng= ""
	_total_count= ""
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
			return "mps_user_heatmap"
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
			return "mps_user_heatmaps"
		except Exception as e :
			raise e



	'''
	get hits
	'''
	@property
	def hits(self) :
		try:
			return self._hits
		except Exception as e :
			raise e
	'''
	set hits
	'''
	@hits.setter
	def hits(self,hits):
		try :
			if not isinstance(hits,long):
				raise TypeError("hits must be set to long value")
			self._hits = hits
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
	get latitude
	'''
	@property
	def lat(self) :
		try:
			return self._lat
		except Exception as e :
			raise e
	'''
	set latitude
	'''
	@lat.setter
	def lat(self,lat):
		try :
			if not isinstance(lat,float):
				raise TypeError("lat must be set to float value")
			self._lat = lat
		except Exception as e :
			raise e


	'''
	get total_bytes
	'''
	@property
	def total_bytes(self) :
		try:
			return self._total_bytes
		except Exception as e :
			raise e
	'''
	set total_bytes
	'''
	@total_bytes.setter
	def total_bytes(self,total_bytes):
		try :
			if not isinstance(total_bytes,long):
				raise TypeError("total_bytes must be set to long value")
			self._total_bytes = total_bytes
		except Exception as e :
			raise e


	'''
	get longitude
	'''
	@property
	def lng(self) :
		try:
			return self._lng
		except Exception as e :
			raise e
	'''
	set longitude
	'''
	@lng.setter
	def lng(self,lng):
		try :
			if not isinstance(lng,float):
				raise TypeError("lng must be set to float value")
			self._lng = lng
		except Exception as e :
			raise e


	'''
	get Total count
	'''
	@property
	def total_count(self) :
		try:
			return self._total_count
		except Exception as e :
			raise e
	'''
	set Total count
	'''
	@total_count.setter
	def total_count(self,total_count):
		try :
			if not isinstance(total_count,int):
				raise TypeError("total_count must be set to int value")
			self._total_count = total_count
		except Exception as e :
			raise e

	'''
	Use this operation to get user heat map.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_user_heatmap_obj=mps_user_heatmap()
				response = mps_user_heatmap_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps_user_heatmap resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_user_heatmap_obj = mps_user_heatmap()
			option_ = options()
			option_._filter=filter_
			return mps_user_heatmap_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps_user_heatmap resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_user_heatmap_obj = mps_user_heatmap()
			option_ = options()
			option_._count=True
			response = mps_user_heatmap_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps_user_heatmap resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_user_heatmap_obj = mps_user_heatmap()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_user_heatmap_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_user_heatmap_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps_user_heatmap
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_user_heatmap_responses, response, "mps_user_heatmap_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_user_heatmap_response_array
				i=0
				error = [mps_user_heatmap() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_user_heatmap_response_array
			i=0
			mps_user_heatmap_objs = [mps_user_heatmap() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps_user_heatmap'):
					for props in obj._mps_user_heatmap:
						result = service.payload_formatter.string_to_bulk_resource(mps_user_heatmap_response,self.__class__.__name__,props)
						mps_user_heatmap_objs[i] = result.mps_user_heatmap
						i=i+1
			return mps_user_heatmap_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps_user_heatmap,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_user_heatmap_response(base_response):
	def __init__(self,length=1) :
		self.mps_user_heatmap= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps_user_heatmap= [ mps_user_heatmap() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_user_heatmap_responses(base_response):
	def __init__(self,length=1) :
		self.mps_user_heatmap_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_user_heatmap_response_array = [ mps_user_heatmap() for _ in range(length)]
