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

from massrc.com.citrix.mas.nitro.resource.config.mps.application import application

'''
Configuration for Applications Managed by Management System resource
'''

class ns_application(application):
	_no_of_gslb= ""
	_no_of_cs= ""
	_no_of_lb= ""
	_no_of_svc= ""
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
			return "ns_application"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ns_application,self).get_object_id()
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
			return "ns_applications"
		except Exception as e :
			raise e


	'''
	Number of GSLB VIPs
	'''
	@property
	def no_of_gslb(self):
		try:
			return self._no_of_gslb
		except Exception as e :
			raise e
	'''
	Number of GSLB VIPs
	'''
	@no_of_gslb.setter
	def no_of_gslb(self,no_of_gslb):
		try :
			if not isinstance(no_of_gslb,str):
				raise TypeError("no_of_gslb must be set to str value")
			self._no_of_gslb = no_of_gslb
		except Exception as e :
			raise e

	'''
	Number of CS VIPs
	'''
	@property
	def no_of_cs(self):
		try:
			return self._no_of_cs
		except Exception as e :
			raise e
	'''
	Number of CS VIPs
	'''
	@no_of_cs.setter
	def no_of_cs(self,no_of_cs):
		try :
			if not isinstance(no_of_cs,str):
				raise TypeError("no_of_cs must be set to str value")
			self._no_of_cs = no_of_cs
		except Exception as e :
			raise e

	'''
	Number of LB VIPs
	'''
	@property
	def no_of_lb(self):
		try:
			return self._no_of_lb
		except Exception as e :
			raise e
	'''
	Number of LB VIPs
	'''
	@no_of_lb.setter
	def no_of_lb(self,no_of_lb):
		try :
			if not isinstance(no_of_lb,str):
				raise TypeError("no_of_lb must be set to str value")
			self._no_of_lb = no_of_lb
		except Exception as e :
			raise e

	'''
	Number of Services
	'''
	@property
	def no_of_svc(self):
		try:
			return self._no_of_svc
		except Exception as e :
			raise e
	'''
	Number of Services
	'''
	@no_of_svc.setter
	def no_of_svc(self,no_of_svc):
		try :
			if not isinstance(no_of_svc,str):
				raise TypeError("no_of_svc must be set to str value")
			self._no_of_svc = no_of_svc
		except Exception as e :
			raise e

	'''
	Use this operation to add application.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_application_obj= ns_application()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_application_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete application.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_application_obj=ns_application()
					return cls.delete_bulk_request(client,resource,ns_application_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get application.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_application_obj=ns_application()
				response = ns_application_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify application.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_application_obj=ns_application()
				return cls.update_bulk_request(client,resource,ns_application_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_application_obj = ns_application()
			option_ = options()
			option_._filter=filter_
			return ns_application_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_application resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_application_obj = ns_application()
			option_ = options()
			option_._count=True
			response = ns_application_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_application_obj = ns_application()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_application_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_application_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_application
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_application_responses, response, "ns_application_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_application_response_array
				i=0
				error = [ns_application() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_application_response_array
			i=0
			ns_application_objs = [ns_application() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_application'):
					for props in obj._ns_application:
						result = service.payload_formatter.string_to_bulk_resource(ns_application_response,self.__class__.__name__,props)
						ns_application_objs[i] = result.ns_application
						i=i+1
			return ns_application_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_application,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_application_response(base_response):
	def __init__(self,length=1) :
		self.ns_application= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_application= [ ns_application() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_application_responses(base_response):
	def __init__(self,length=1) :
		self.ns_application_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_application_response_array = [ ns_application() for _ in range(length)]
