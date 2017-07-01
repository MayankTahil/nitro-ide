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

from massrc.com.citrix.mas.nitro.resource.config.mps.threshold import threshold

'''
Configuration for Thresholds resource
'''

class insight_threshold(threshold):
	_exporter_id= ""
	_ctnsappname= ""
	_stylebook_flag= ""
	_rpt_sample_time= ""
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
			return "insight_threshold"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(insight_threshold,self).get_object_id()
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
			return "insight_thresholds"
		except Exception as e :
			raise e



	'''
	get Exporter Id
	'''
	@property
	def exporter_id(self) :
		try:
			return self._exporter_id
		except Exception as e :
			raise e
	'''
	set Exporter Id
	'''
	@exporter_id.setter
	def exporter_id(self,exporter_id):
		try :
			if not isinstance(exporter_id,long):
				raise TypeError("exporter_id must be set to long value")
			self._exporter_id = exporter_id
		except Exception as e :
			raise e


	'''
	get AppName
	'''
	@property
	def ctnsappname(self) :
		try:
			return self._ctnsappname
		except Exception as e :
			raise e
	'''
	set AppName
	'''
	@ctnsappname.setter
	def ctnsappname(self,ctnsappname):
		try :
			if not isinstance(ctnsappname,str):
				raise TypeError("ctnsappname must be set to str value")
			self._ctnsappname = ctnsappname
		except Exception as e :
			raise e


	'''
	get Stylebook threshold configuration true or false
	'''
	@property
	def stylebook_flag(self) :
		try:
			return self._stylebook_flag
		except Exception as e :
			raise e
	'''
	set Stylebook threshold configuration true or false
	'''
	@stylebook_flag.setter
	def stylebook_flag(self,stylebook_flag):
		try :
			if not isinstance(stylebook_flag,bool):
				raise TypeError("stylebook_flag must be set to bool value")
			self._stylebook_flag = stylebook_flag
		except Exception as e :
			raise e


	'''
	get Report Sample time.
	'''
	@property
	def rpt_sample_time(self) :
		try:
			return self._rpt_sample_time
		except Exception as e :
			raise e
	'''
	set Report Sample time.
	'''
	@rpt_sample_time.setter
	def rpt_sample_time(self,rpt_sample_time):
		try :
			if not isinstance(rpt_sample_time,long):
				raise TypeError("rpt_sample_time must be set to long value")
			self._rpt_sample_time = rpt_sample_time
		except Exception as e :
			raise e

	'''
	add insight threshold configuration.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				insight_threshold_obj= insight_threshold()
				return cls.perform_operation_bulk_request(service,"add", resource,insight_threshold_obj)
		except Exception as e :
			raise e

	'''
	Delete insight threshold configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					insight_threshold_obj=insight_threshold()
					return cls.delete_bulk_request(client,resource,insight_threshold_obj)
		except Exception as e :
			raise e

	'''
	get insight threshold configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				insight_threshold_obj=insight_threshold()
				response = insight_threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify insight threshold configuraiton.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				insight_threshold_obj=insight_threshold()
				return cls.update_bulk_request(client,resource,insight_threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of insight_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			insight_threshold_obj = insight_threshold()
			option_ = options()
			option_._filter=filter_
			return insight_threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the insight_threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			insight_threshold_obj = insight_threshold()
			option_ = options()
			option_._count=True
			response = insight_threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of insight_threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			insight_threshold_obj = insight_threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = insight_threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(insight_threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.insight_threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(insight_threshold_responses, response, "insight_threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.insight_threshold_response_array
				i=0
				error = [insight_threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.insight_threshold_response_array
			i=0
			insight_threshold_objs = [insight_threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_insight_threshold'):
					for props in obj._insight_threshold:
						result = service.payload_formatter.string_to_bulk_resource(insight_threshold_response,self.__class__.__name__,props)
						insight_threshold_objs[i] = result.insight_threshold
						i=i+1
			return insight_threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(insight_threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class insight_threshold_response(base_response):
	def __init__(self,length=1) :
		self.insight_threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.insight_threshold= [ insight_threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class insight_threshold_responses(base_response):
	def __init__(self,length=1) :
		self.insight_threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.insight_threshold_response_array = [ insight_threshold() for _ in range(length)]
