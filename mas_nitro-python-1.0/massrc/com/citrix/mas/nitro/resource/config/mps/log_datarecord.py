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
Configuration for Af datarecord logging enable or disable resource
'''

class log_datarecord(base_resource):
	_cbwan= ""
	_web= ""
	_tcpopt= ""
	_hdx= ""
	_videoopt= ""
	_security= ""
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
			return "log_datarecord"
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
			return "log_datarecords"
		except Exception as e :
			raise e



	'''
	get Enable CB wan insight data record logging value
	'''
	@property
	def cbwan(self) :
		try:
			return self._cbwan
		except Exception as e :
			raise e
	'''
	set Enable CB wan insight data record logging value
	'''
	@cbwan.setter
	def cbwan(self,cbwan):
		try :
			if not isinstance(cbwan,bool):
				raise TypeError("cbwan must be set to bool value")
			self._cbwan = cbwan
		except Exception as e :
			raise e


	'''
	get Enable web insight data record logging value
	'''
	@property
	def web(self) :
		try:
			return self._web
		except Exception as e :
			raise e
	'''
	set Enable web insight data record logging value
	'''
	@web.setter
	def web(self,web):
		try :
			if not isinstance(web,bool):
				raise TypeError("web must be set to bool value")
			self._web = web
		except Exception as e :
			raise e


	'''
	get Enable tcp insight data record logging value
	'''
	@property
	def tcpopt(self) :
		try:
			return self._tcpopt
		except Exception as e :
			raise e
	'''
	set Enable tcp insight data record logging value
	'''
	@tcpopt.setter
	def tcpopt(self,tcpopt):
		try :
			if not isinstance(tcpopt,bool):
				raise TypeError("tcpopt must be set to bool value")
			self._tcpopt = tcpopt
		except Exception as e :
			raise e


	'''
	get Enable hdx insight data record logging value
	'''
	@property
	def hdx(self) :
		try:
			return self._hdx
		except Exception as e :
			raise e
	'''
	set Enable hdx insight data record logging value
	'''
	@hdx.setter
	def hdx(self,hdx):
		try :
			if not isinstance(hdx,bool):
				raise TypeError("hdx must be set to bool value")
			self._hdx = hdx
		except Exception as e :
			raise e


	'''
	get Enable video insight data record logging value
	'''
	@property
	def videoopt(self) :
		try:
			return self._videoopt
		except Exception as e :
			raise e
	'''
	set Enable video insight data record logging value
	'''
	@videoopt.setter
	def videoopt(self,videoopt):
		try :
			if not isinstance(videoopt,bool):
				raise TypeError("videoopt must be set to bool value")
			self._videoopt = videoopt
		except Exception as e :
			raise e


	'''
	get Enable security insight data record logging value
	'''
	@property
	def security(self) :
		try:
			return self._security
		except Exception as e :
			raise e
	'''
	set Enable security insight data record logging value
	'''
	@security.setter
	def security(self,security):
		try :
			if not isinstance(security,bool):
				raise TypeError("security must be set to bool value")
			self._security = security
		except Exception as e :
			raise e

	'''
	To set data record logging value.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				log_datarecord_obj= log_datarecord()
				return cls.perform_operation_bulk_request(service,"add", resource,log_datarecord_obj)
		except Exception as e :
			raise e

	'''
	To get data record logging value.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				log_datarecord_obj=log_datarecord()
				response = log_datarecord_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	To set data record logging value.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				log_datarecord_obj=log_datarecord()
				return cls.update_bulk_request(client,resource,log_datarecord_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of log_datarecord resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			log_datarecord_obj = log_datarecord()
			option_ = options()
			option_._filter=filter_
			return log_datarecord_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the log_datarecord resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			log_datarecord_obj = log_datarecord()
			option_ = options()
			option_._count=True
			response = log_datarecord_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of log_datarecord resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			log_datarecord_obj = log_datarecord()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = log_datarecord_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(log_datarecord_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.log_datarecord
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(log_datarecord_responses, response, "log_datarecord_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.log_datarecord_response_array
				i=0
				error = [log_datarecord() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.log_datarecord_response_array
			i=0
			log_datarecord_objs = [log_datarecord() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_log_datarecord'):
					for props in obj._log_datarecord:
						result = service.payload_formatter.string_to_bulk_resource(log_datarecord_response,self.__class__.__name__,props)
						log_datarecord_objs[i] = result.log_datarecord
						i=i+1
			return log_datarecord_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(log_datarecord,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class log_datarecord_response(base_response):
	def __init__(self,length=1) :
		self.log_datarecord= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.log_datarecord= [ log_datarecord() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class log_datarecord_responses(base_response):
	def __init__(self,length=1) :
		self.log_datarecord_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.log_datarecord_response_array = [ log_datarecord() for _ in range(length)]
