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
Configuration for Appflow param for NetScaler resource
'''

class ns_ns_appflowparam(base_resource):
	_observationdomainName= ""
	_template_interval= ""
	_httpxforwardedfor= ""
	_observationdomainid= ""
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
			return "ns_ns_appflowparam"
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
			return "ns_ns_appflowparams"
		except Exception as e :
			raise e



	'''
	get observationdomainName
	'''
	@property
	def observationdomainName(self) :
		try:
			return self._observationdomainName
		except Exception as e :
			raise e
	'''
	set observationdomainName
	'''
	@observationdomainName.setter
	def observationdomainName(self,observationdomainName):
		try :
			if not isinstance(observationdomainName,str):
				raise TypeError("observationdomainName must be set to str value")
			self._observationdomainName = observationdomainName
		except Exception as e :
			raise e


	'''
	get Template refresh interval
	'''
	@property
	def template_interval(self) :
		try:
			return self._template_interval
		except Exception as e :
			raise e
	'''
	set Template refresh interval
	'''
	@template_interval.setter
	def template_interval(self,template_interval):
		try :
			if not isinstance(template_interval,int):
				raise TypeError("template_interval must be set to int value")
			self._template_interval = template_interval
		except Exception as e :
			raise e


	'''
	get 
	'''
	@property
	def httpxforwardedfor(self) :
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	set 
	'''
	@httpxforwardedfor.setter
	def httpxforwardedfor(self,httpxforwardedfor):
		try :
			if not isinstance(httpxforwardedfor,str):
				raise TypeError("httpxforwardedfor must be set to str value")
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e :
			raise e


	'''
	get observationdomainid
	'''
	@property
	def observationdomainid(self) :
		try:
			return self._observationdomainid
		except Exception as e :
			raise e
	'''
	set observationdomainid
	'''
	@observationdomainid.setter
	def observationdomainid(self,observationdomainid):
		try :
			if not isinstance(observationdomainid,str):
				raise TypeError("observationdomainid must be set to str value")
			self._observationdomainid = observationdomainid
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ns_appflowparam resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ns_appflowparam_obj = ns_ns_appflowparam()
			option_ = options()
			option_._filter=filter_
			return ns_ns_appflowparam_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ns_appflowparam resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ns_appflowparam_obj = ns_ns_appflowparam()
			option_ = options()
			option_._count=True
			response = ns_ns_appflowparam_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ns_appflowparam resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ns_appflowparam_obj = ns_ns_appflowparam()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ns_appflowparam_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ns_appflowparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ns_appflowparam
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ns_appflowparam_responses, response, "ns_ns_appflowparam_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ns_appflowparam_response_array
				i=0
				error = [ns_ns_appflowparam() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ns_appflowparam_response_array
			i=0
			ns_ns_appflowparam_objs = [ns_ns_appflowparam() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ns_appflowparam'):
					for props in obj._ns_ns_appflowparam:
						result = service.payload_formatter.string_to_bulk_resource(ns_ns_appflowparam_response,self.__class__.__name__,props)
						ns_ns_appflowparam_objs[i] = result.ns_ns_appflowparam
						i=i+1
			return ns_ns_appflowparam_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ns_appflowparam,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ns_appflowparam_response(base_response):
	def __init__(self,length=1) :
		self.ns_ns_appflowparam= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ns_appflowparam= [ ns_ns_appflowparam() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ns_appflowparam_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ns_appflowparam_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ns_appflowparam_response_array = [ ns_ns_appflowparam() for _ in range(length)]
