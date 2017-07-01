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
Configuration for Scheduled export report job resource
'''

class export_report_job(base_resource):
	_recurrence_option= ""
	_status= ""
	_export_format= ""
	_description= ""
	_mail_profile_name= ""
	_recurrence= ""
	_tz_offset= ""
	_next_scheduletime= ""
	_export_time= ""
	_job_name= ""
	_trigger_start= ""
	_report_name= ""
	_id= ""
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
			return "export_report_job"
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
			return "export_report_jobs"
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
	get Schedule Status
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set Schedule Status
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
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
	get Next Schedule Time
	'''
	@property
	def next_scheduletime(self) :
		try:
			return self._next_scheduletime
		except Exception as e :
			raise e
	'''
	set Next Schedule Time
	'''
	@next_scheduletime.setter
	def next_scheduletime(self,next_scheduletime):
		try :
			if not isinstance(next_scheduletime,int):
				raise TypeError("next_scheduletime must be set to int value")
			self._next_scheduletime = next_scheduletime
		except Exception as e :
			raise e


	'''
	get Report Export time GMT epoch (string representation of 10 digit numbers).
	'''
	@property
	def export_time(self) :
		try:
			return self._export_time
		except Exception as e :
			raise e
	'''
	set Report Export time GMT epoch (string representation of 10 digit numbers).
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
	get job name is ExportJob.
	'''
	@property
	def job_name(self) :
		try:
			return self._job_name
		except Exception as e :
			raise e
	'''
	set job name is ExportJob.
	'''
	@job_name.setter
	def job_name(self,job_name):
		try :
			if not isinstance(job_name,str):
				raise TypeError("job_name must be set to str value")
			self._job_name = job_name
		except Exception as e :
			raise e


	'''
	get Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@property
	def trigger_start(self) :
		try:
			return self._trigger_start
		except Exception as e :
			raise e
	'''
	set Time at which the trigger should start.Format:YY:MM:DD:HH:MM
	'''
	@trigger_start.setter
	def trigger_start(self,trigger_start):
		try :
			if not isinstance(trigger_start,str):
				raise TypeError("trigger_start must be set to str value")
			self._trigger_start = trigger_start
		except Exception as e :
			raise e


	'''
	get report name
	'''
	@property
	def report_name(self) :
		try:
			return self._report_name
		except Exception as e :
			raise e
	'''
	set report name
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
	get Id is job_schedule id for all the export_report_job details
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is job_schedule id for all the export_report_job details
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
	Use this operation to delete export report job..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					export_report_job_obj=export_report_job()
					return cls.delete_bulk_request(client,resource,export_report_job_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get job_schedule detail.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				export_report_job_obj=export_report_job()
				response = export_report_job_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify export report job..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				export_report_job_obj=export_report_job()
				return cls.update_bulk_request(client,resource,export_report_job_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of export_report_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			export_report_job_obj = export_report_job()
			option_ = options()
			option_._filter=filter_
			return export_report_job_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the export_report_job resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			export_report_job_obj = export_report_job()
			option_ = options()
			option_._count=True
			response = export_report_job_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of export_report_job resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			export_report_job_obj = export_report_job()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = export_report_job_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(export_report_job_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.export_report_job
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(export_report_job_responses, response, "export_report_job_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.export_report_job_response_array
				i=0
				error = [export_report_job() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.export_report_job_response_array
			i=0
			export_report_job_objs = [export_report_job() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_export_report_job'):
					for props in obj._export_report_job:
						result = service.payload_formatter.string_to_bulk_resource(export_report_job_response,self.__class__.__name__,props)
						export_report_job_objs[i] = result.export_report_job
						i=i+1
			return export_report_job_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(export_report_job,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class export_report_job_response(base_response):
	def __init__(self,length=1) :
		self.export_report_job= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.export_report_job= [ export_report_job() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class export_report_job_responses(base_response):
	def __init__(self,length=1) :
		self.export_report_job_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.export_report_job_response_array = [ export_report_job() for _ in range(length)]
