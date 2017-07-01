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
Configuration for Performance Management Reports resource
'''

class perf_reports(base_resource):
	_report_description= ""
	_device_family= ""
	_db_table_name= ""
	_counter_groups= ""
	_report_name= ""
	_enable_on_devices= ""
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
			return "perf_reports"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._report_name
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
			return "perf_reportss"
		except Exception as e :
			raise e



	'''
	get Short Description of the report
	'''
	@property
	def report_description(self) :
		try:
			return self._report_description
		except Exception as e :
			raise e
	'''
	set Short Description of the report
	'''
	@report_description.setter
	def report_description(self,report_description):
		try :
			if not isinstance(report_description,str):
				raise TypeError("report_description must be set to str value")
			self._report_description = report_description
		except Exception as e :
			raise e


	'''
	get Device Family of which this report belongs to
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family of which this report belongs to
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Table Name in DB for the corresponding report
	'''
	@property
	def db_table_name(self) :
		try:
			return self._db_table_name
		except Exception as e :
			raise e
	'''
	set Table Name in DB for the corresponding report
	'''
	@db_table_name.setter
	def db_table_name(self,db_table_name):
		try :
			if not isinstance(db_table_name,str):
				raise TypeError("db_table_name must be set to str value")
			self._db_table_name = db_table_name
		except Exception as e :
			raise e


	'''
	get Counter Group(s) from which the report is generated
	'''
	@property
	def counter_groups(self) :
		try:
			return self._counter_groups
		except Exception as e :
			raise e
	'''
	set Counter Group(s) from which the report is generated
	'''
	@counter_groups.setter
	def counter_groups(self,counter_groups):
		try :
			if not isinstance(counter_groups,str):
				raise TypeError("counter_groups must be set to str value")
			self._counter_groups = counter_groups
		except Exception as e :
			raise e


	'''
	get Name of Report
	'''
	@property
	def report_name(self) :
		try:
			return self._report_name
		except Exception as e :
			raise e
	'''
	set Name of Report
	'''
	@report_name.setter
	def report_name(self,report_name):
		try :
			if not isinstance(report_name,str):
				raise TypeError("report_name must be set to str value")
			self._report_name = report_name
		except Exception as e :
			raise e


	'''
	get On which devices the report is enabled
	'''
	@property
	def enable_on_devices(self) :
		try:
			return self._enable_on_devices
		except Exception as e :
			raise e
	'''
	set On which devices the report is enabled
	'''
	@enable_on_devices.setter
	def enable_on_devices(self,enable_on_devices):
		try :
			if not isinstance(enable_on_devices,str):
				raise TypeError("enable_on_devices must be set to str value")
			self._enable_on_devices = enable_on_devices
		except Exception as e :
			raise e

	'''
	Use this operation to get report Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_reports_obj=perf_reports()
				response = perf_reports_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_reports resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_reports_obj = perf_reports()
			option_ = options()
			option_._filter=filter_
			return perf_reports_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_reports resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_reports_obj = perf_reports()
			option_ = options()
			option_._count=True
			response = perf_reports_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_reports resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_reports_obj = perf_reports()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_reports_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_reports_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_reports
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_reports_responses, response, "perf_reports_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_reports_response_array
				i=0
				error = [perf_reports() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_reports_response_array
			i=0
			perf_reports_objs = [perf_reports() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_reports'):
					for props in obj._perf_reports:
						result = service.payload_formatter.string_to_bulk_resource(perf_reports_response,self.__class__.__name__,props)
						perf_reports_objs[i] = result.perf_reports
						i=i+1
			return perf_reports_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_reports,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_reports_response(base_response):
	def __init__(self,length=1) :
		self.perf_reports= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_reports= [ perf_reports() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_reports_responses(base_response):
	def __init__(self,length=1) :
		self.perf_reports_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_reports_response_array = [ perf_reports() for _ in range(length)]
