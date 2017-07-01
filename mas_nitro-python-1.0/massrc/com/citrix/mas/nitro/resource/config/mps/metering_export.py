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
Configuration for Metering Data Export resource
'''

class metering_export(base_resource):
	_end_time= ""
	_file_size= ""
	_file_name= ""
	_start_time= ""
	_file_last_modified= ""
	_duration= ""
	_ip_address= ""
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
			return "metering_export"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "metering_exports"
		except Exception as e :
			raise e



	'''
	get End Time of interval for which export is generated
	'''
	@property
	def end_time(self) :
		try:
			return self._end_time
		except Exception as e :
			raise e


	'''
	get file_size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e


	'''
	get Start Time of interval for which export is generated
	'''
	@property
	def start_time(self) :
		try:
			return self._start_time
		except Exception as e :
			raise e


	'''
	get Last Modified
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get Interval Duration for which export is generated
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e


	'''
	get IP Address for this VM device for which metering data export is required
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for this VM device for which metering data export is required
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get metering data export.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				metering_export_obj=metering_export()
				response = metering_export_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of metering_export resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			metering_export_obj = metering_export()
			option_ = options()
			option_._filter=filter_
			return metering_export_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the metering_export resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			metering_export_obj = metering_export()
			option_ = options()
			option_._count=True
			response = metering_export_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of metering_export resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			metering_export_obj = metering_export()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = metering_export_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(metering_export_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.metering_export
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(metering_export_responses, response, "metering_export_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.metering_export_response_array
				i=0
				error = [metering_export() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.metering_export_response_array
			i=0
			metering_export_objs = [metering_export() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_metering_export'):
					for props in obj._metering_export:
						result = service.payload_formatter.string_to_bulk_resource(metering_export_response,self.__class__.__name__,props)
						metering_export_objs[i] = result.metering_export
						i=i+1
			return metering_export_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(metering_export,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class metering_export_response(base_response):
	def __init__(self,length=1) :
		self.metering_export= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.metering_export= [ metering_export() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class metering_export_responses(base_response):
	def __init__(self,length=1) :
		self.metering_export_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.metering_export_response_array = [ metering_export() for _ in range(length)]
