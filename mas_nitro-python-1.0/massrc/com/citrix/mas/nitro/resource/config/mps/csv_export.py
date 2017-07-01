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
Configuration for CSV Export resource
'''

class csv_export(base_resource):
	_report_end_time= ""
	_order_by= ""
	_args= ""
	_report_start_time= ""
	_resource_id= ""
	_asc= ""
	_duration_summary= ""
	_id= ""
	_section_title= ""
	_attrs= ""
	_is_count= ""
	_filter= ""
	_detailview= ""
	_duration= ""
	_cr_enabled= ""
	_sla_enabled= ""
	_type= ""
	_resource_name= ""
	_csv_mapping_id= ""
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
			return "csv_export"
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
			return "csv_exports"
		except Exception as e :
			raise e



	'''
	get Report end time.
	'''
	@property
	def report_end_time(self) :
		try:
			return self._report_end_time
		except Exception as e :
			raise e
	'''
	set Report end time.
	'''
	@report_end_time.setter
	def report_end_time(self,report_end_time):
		try :
			if not isinstance(report_end_time,long):
				raise TypeError("report_end_time must be set to long value")
			self._report_end_time = report_end_time
		except Exception as e :
			raise e


	'''
	get Order By
	'''
	@property
	def order_by(self) :
		try:
			return self._order_by
		except Exception as e :
			raise e
	'''
	set Order By
	'''
	@order_by.setter
	def order_by(self,order_by):
		try :
			if not isinstance(order_by,str):
				raise TypeError("order_by must be set to str value")
			self._order_by = order_by
		except Exception as e :
			raise e


	'''
	get args
	'''
	@property
	def args(self) :
		try:
			return self._args
		except Exception as e :
			raise e
	'''
	set args
	'''
	@args.setter
	def args(self,args):
		try :
			if not isinstance(args,str):
				raise TypeError("args must be set to str value")
			self._args = args
		except Exception as e :
			raise e


	'''
	get Report start time.
	'''
	@property
	def report_start_time(self) :
		try:
			return self._report_start_time
		except Exception as e :
			raise e
	'''
	set Report start time.
	'''
	@report_start_time.setter
	def report_start_time(self,report_start_time):
		try :
			if not isinstance(report_start_time,long):
				raise TypeError("report_start_time must be set to long value")
			self._report_start_time = report_start_time
		except Exception as e :
			raise e


	'''
	get Resource id
	'''
	@property
	def resource_id(self) :
		try:
			return self._resource_id
		except Exception as e :
			raise e
	'''
	set Resource id
	'''
	@resource_id.setter
	def resource_id(self,resource_id):
		try :
			if not isinstance(resource_id,str):
				raise TypeError("resource_id must be set to str value")
			self._resource_id = resource_id
		except Exception as e :
			raise e


	'''
	get asc
	'''
	@property
	def asc(self) :
		try:
			return self._asc
		except Exception as e :
			raise e
	'''
	set asc
	'''
	@asc.setter
	def asc(self,asc):
		try :
			if not isinstance(asc,str):
				raise TypeError("asc must be set to str value")
			self._asc = asc
		except Exception as e :
			raise e


	'''
	get Duration summary.
	'''
	@property
	def duration_summary(self) :
		try:
			return self._duration_summary
		except Exception as e :
			raise e
	'''
	set Duration summary.
	'''
	@duration_summary.setter
	def duration_summary(self,duration_summary):
		try :
			if not isinstance(duration_summary,str):
				raise TypeError("duration_summary must be set to str value")
			self._duration_summary = duration_summary
		except Exception as e :
			raise e


	'''
	get Id is CSV export Id
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is CSV export Id
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
	get Section title
	'''
	@property
	def section_title(self) :
		try:
			return self._section_title
		except Exception as e :
			raise e
	'''
	set Section title
	'''
	@section_title.setter
	def section_title(self,section_title):
		try :
			if not isinstance(section_title,str):
				raise TypeError("section_title must be set to str value")
			self._section_title = section_title
		except Exception as e :
			raise e


	'''
	get attrs
	'''
	@property
	def attrs(self) :
		try:
			return self._attrs
		except Exception as e :
			raise e
	'''
	set attrs
	'''
	@attrs.setter
	def attrs(self,attrs):
		try :
			if not isinstance(attrs,str):
				raise TypeError("attrs must be set to str value")
			self._attrs = attrs
		except Exception as e :
			raise e


	'''
	get is_count
	'''
	@property
	def is_count(self) :
		try:
			return self._is_count
		except Exception as e :
			raise e
	'''
	set is_count
	'''
	@is_count.setter
	def is_count(self,is_count):
		try :
			if not isinstance(is_count,str):
				raise TypeError("is_count must be set to str value")
			self._is_count = is_count
		except Exception as e :
			raise e


	'''
	get filter
	'''
	@property
	def filter(self) :
		try:
			return self._filter
		except Exception as e :
			raise e
	'''
	set filter
	'''
	@filter.setter
	def filter(self,filter):
		try :
			if not isinstance(filter,str):
				raise TypeError("filter must be set to str value")
			self._filter = filter
		except Exception as e :
			raise e


	'''
	get detailview
	'''
	@property
	def detailview(self) :
		try:
			return self._detailview
		except Exception as e :
			raise e
	'''
	set detailview
	'''
	@detailview.setter
	def detailview(self,detailview):
		try :
			if not isinstance(detailview,str):
				raise TypeError("detailview must be set to str value")
			self._detailview = detailview
		except Exception as e :
			raise e


	'''
	get Duration
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set Duration
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get CR Enabled.
	'''
	@property
	def cr_enabled(self) :
		try:
			return self._cr_enabled
		except Exception as e :
			raise e
	'''
	set CR Enabled.
	'''
	@cr_enabled.setter
	def cr_enabled(self,cr_enabled):
		try :
			if not isinstance(cr_enabled,str):
				raise TypeError("cr_enabled must be set to str value")
			self._cr_enabled = cr_enabled
		except Exception as e :
			raise e


	'''
	get SLA Enabled.
	'''
	@property
	def sla_enabled(self) :
		try:
			return self._sla_enabled
		except Exception as e :
			raise e
	'''
	set SLA Enabled.
	'''
	@sla_enabled.setter
	def sla_enabled(self,sla_enabled):
		try :
			if not isinstance(sla_enabled,str):
				raise TypeError("sla_enabled must be set to str value")
			self._sla_enabled = sla_enabled
		except Exception as e :
			raise e


	'''
	get Type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Resource name
	'''
	@property
	def resource_name(self) :
		try:
			return self._resource_name
		except Exception as e :
			raise e
	'''
	set Resource name
	'''
	@resource_name.setter
	def resource_name(self,resource_name):
		try :
			if not isinstance(resource_name,str):
				raise TypeError("resource_name must be set to str value")
			self._resource_name = resource_name
		except Exception as e :
			raise e


	'''
	get Schedule export csv_mapping_id
	'''
	@property
	def csv_mapping_id(self) :
		try:
			return self._csv_mapping_id
		except Exception as e :
			raise e
	'''
	set Schedule export csv_mapping_id
	'''
	@csv_mapping_id.setter
	def csv_mapping_id(self,csv_mapping_id):
		try :
			if not isinstance(csv_mapping_id,str):
				raise TypeError("csv_mapping_id must be set to str value")
			self._csv_mapping_id = csv_mapping_id
		except Exception as e :
			raise e

	'''
	Use this operation to add CSV Export.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				csv_export_obj= csv_export()
				return cls.perform_operation_bulk_request(service,"add", resource,csv_export_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete  CSV Export.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					csv_export_obj=csv_export()
					return cls.delete_bulk_request(client,resource,csv_export_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get CSV Export.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				csv_export_obj=csv_export()
				response = csv_export_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of csv_export resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			csv_export_obj = csv_export()
			option_ = options()
			option_._filter=filter_
			return csv_export_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the csv_export resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			csv_export_obj = csv_export()
			option_ = options()
			option_._count=True
			response = csv_export_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of csv_export resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			csv_export_obj = csv_export()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = csv_export_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(csv_export_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.csv_export
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(csv_export_responses, response, "csv_export_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.csv_export_response_array
				i=0
				error = [csv_export() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.csv_export_response_array
			i=0
			csv_export_objs = [csv_export() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_csv_export'):
					for props in obj._csv_export:
						result = service.payload_formatter.string_to_bulk_resource(csv_export_response,self.__class__.__name__,props)
						csv_export_objs[i] = result.csv_export
						i=i+1
			return csv_export_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(csv_export,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class csv_export_response(base_response):
	def __init__(self,length=1) :
		self.csv_export= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.csv_export= [ csv_export() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class csv_export_responses(base_response):
	def __init__(self,length=1) :
		self.csv_export_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.csv_export_response_array = [ csv_export() for _ in range(length)]
