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
from massrc.com.citrix.mas.nitro.resource.config.mps.csv_export import csv_export


'''
Configuration for Export report resource
'''

class export_report(base_resource):
	_page_name= ""
	_recurrence_option= ""
	_report_context= ""
	_export_format= ""
	_description= ""
	_report_title= ""
	_mail_profile_name= ""
	_recurrence= ""
	_tz_offset= ""
	_file_name= ""
	_csv_export_arr=[]
	_export_time= ""
	_export_now= ""
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
			return "export_report"
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
			return "export_reports"
		except Exception as e :
			raise e



	'''
	get Page name.
	'''
	@property
	def page_name(self) :
		try:
			return self._page_name
		except Exception as e :
			raise e
	'''
	set Page name.
	'''
	@page_name.setter
	def page_name(self,page_name):
		try :
			if not isinstance(page_name,str):
				raise TypeError("page_name must be set to str value")
			self._page_name = page_name
		except Exception as e :
			raise e


	'''
	get Recurrence option (Weekly -> mon - sun, Monthly -> date in DD format).
	'''
	@property
	def recurrence_option(self) :
		try:
			return self._recurrence_option
		except Exception as e :
			raise e
	'''
	set Recurrence option (Weekly -> mon - sun, Monthly -> date in DD format).
	'''
	@recurrence_option.setter
	def recurrence_option(self,recurrence_option):
		try :
			if not isinstance(recurrence_option,str):
				raise TypeError("recurrence_option must be set to str value")
			self._recurrence_option = recurrence_option
		except Exception as e :
			raise e


	'''
	get Report context.
	'''
	@property
	def report_context(self) :
		try:
			return self._report_context
		except Exception as e :
			raise e
	'''
	set Report context.
	'''
	@report_context.setter
	def report_context(self,report_context):
		try :
			if not isinstance(report_context,str):
				raise TypeError("report_context must be set to str value")
			self._report_context = report_context
		except Exception as e :
			raise e


	'''
	get Report Export format (PDF/JPEG/PNG)
	'''
	@property
	def export_format(self) :
		try:
			return self._export_format
		except Exception as e :
			raise e
	'''
	set Report Export format (PDF/JPEG/PNG)
	'''
	@export_format.setter
	def export_format(self,export_format):
		try :
			if not isinstance(export_format,str):
				raise TypeError("export_format must be set to str value")
			self._export_format = export_format
		except Exception as e :
			raise e


	'''
	get Report Description.
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Report Description.
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Report Title
	'''
	@property
	def report_title(self) :
		try:
			return self._report_title
		except Exception as e :
			raise e
	'''
	set Report Title
	'''
	@report_title.setter
	def report_title(self,report_title):
		try :
			if not isinstance(report_title,str):
				raise TypeError("report_title must be set to str value")
			self._report_title = report_title
		except Exception as e :
			raise e


	'''
	get Mail profile name to send notification mail.
	'''
	@property
	def mail_profile_name(self) :
		try:
			return self._mail_profile_name
		except Exception as e :
			raise e
	'''
	set Mail profile name to send notification mail.
	'''
	@mail_profile_name.setter
	def mail_profile_name(self,mail_profile_name):
		try :
			if not isinstance(mail_profile_name,str):
				raise TypeError("mail_profile_name must be set to str value")
			self._mail_profile_name = mail_profile_name
		except Exception as e :
			raise e


	'''
	get Recurrence (Daily, Weekly, Monthly).
	'''
	@property
	def recurrence(self) :
		try:
			return self._recurrence
		except Exception as e :
			raise e
	'''
	set Recurrence (Daily, Weekly, Monthly).
	'''
	@recurrence.setter
	def recurrence(self,recurrence):
		try :
			if not isinstance(recurrence,str):
				raise TypeError("recurrence must be set to str value")
			self._recurrence = recurrence
		except Exception as e :
			raise e


	'''
	get Time zone offset.
	'''
	@property
	def tz_offset(self) :
		try:
			return self._tz_offset
		except Exception as e :
			raise e
	'''
	set Time zone offset.
	'''
	@tz_offset.setter
	def tz_offset(self,tz_offset):
		try :
			if not isinstance(tz_offset,int):
				raise TypeError("tz_offset must be set to int value")
			self._tz_offset = tz_offset
		except Exception as e :
			raise e


	'''
	get Report File name.
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Report File name.
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
	get CSV Export Array
	'''
	@property
	def csv_export_arr(self) :
		try:
			return self._csv_export_arr
		except Exception as e :
			raise e
	'''
	set CSV Export Array
	'''
	@csv_export_arr.setter
	def csv_export_arr(self,csv_export_arr) :
		try :
			if not isinstance(csv_export_arr,list):
				raise TypeError("csv_export_arr must be set to array of csv_export value")
			for item in csv_export_arr :
				if not isinstance(item,csv_export):
					raise TypeError("item must be set to csv_export value")
			self._csv_export_arr = csv_export_arr
		except Exception as e :
			raise e


	'''
	get Report Export time epoch (string representation of 11 digit numbers).
	'''
	@property
	def export_time(self) :
		try:
			return self._export_time
		except Exception as e :
			raise e
	'''
	set Report Export time epoch (string representation of 11 digit numbers).
	'''
	@export_time.setter
	def export_time(self,export_time):
		try :
			if not isinstance(export_time,str):
				raise TypeError("export_time must be set to str value")
			self._export_time = export_time
		except Exception as e :
			raise e


	'''
	get Export now
	'''
	@property
	def export_now(self) :
		try:
			return self._export_now
		except Exception as e :
			raise e
	'''
	set Export now
	'''
	@export_now.setter
	def export_now(self,export_now):
		try :
			if not isinstance(export_now,bool):
				raise TypeError("export_now must be set to bool value")
			self._export_now = export_now
		except Exception as e :
			raise e

	'''
	Use this operation to export report.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				export_report_obj= export_report()
				return cls.perform_operation_bulk_request(service,"add", resource,export_report_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to download exported report.
	'''

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(export_report_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.export_report
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(export_report_responses, response, "export_report_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.export_report_response_array
				i=0
				error = [export_report() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.export_report_response_array
			i=0
			export_report_objs = [export_report() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_export_report'):
					for props in obj._export_report:
						result = service.payload_formatter.string_to_bulk_resource(export_report_response,self.__class__.__name__,props)
						export_report_objs[i] = result.export_report
						i=i+1
			return export_report_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(export_report,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class export_report_response(base_response):
	def __init__(self,length=1) :
		self.export_report= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.export_report= [ export_report() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class export_report_responses(base_response):
	def __init__(self,length=1) :
		self.export_report_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.export_report_response_array = [ export_report() for _ in range(length)]
