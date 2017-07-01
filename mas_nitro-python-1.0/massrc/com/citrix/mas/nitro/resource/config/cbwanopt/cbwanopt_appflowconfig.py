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
Configuration for cbwanopt_appflowconfig resource.
'''

class cbwanopt_appflowconfig(base_resource):
	_tcp= ""
	_tcp_hdx= ""
	_agent_list=[]
	_wanOpt= ""
	_geo_support= ""
	_hdx= ""
	_id= ""
	_ip_address= ""
	_appflowfeature= ""
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
			return "cbwanopt_appflowconfig"
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
			return "cbwanopt_appflowconfigs"
		except Exception as e :
			raise e



	'''
	get tcp
	'''
	@property
	def tcp(self) :
		try:
			return self._tcp
		except Exception as e :
			raise e
	'''
	set tcp
	'''
	@tcp.setter
	def tcp(self,tcp):
		try :
			if not isinstance(tcp,bool):
				raise TypeError("tcp must be set to bool value")
			self._tcp = tcp
		except Exception as e :
			raise e


	'''
	get tcp_hdx
	'''
	@property
	def tcp_hdx(self) :
		try:
			return self._tcp_hdx
		except Exception as e :
			raise e
	'''
	set tcp_hdx
	'''
	@tcp_hdx.setter
	def tcp_hdx(self,tcp_hdx):
		try :
			if not isinstance(tcp_hdx,bool):
				raise TypeError("tcp_hdx must be set to bool value")
			self._tcp_hdx = tcp_hdx
		except Exception as e :
			raise e


	'''
	get Agent List, on which traffic will flow
	'''
	@property
	def agent_list(self) :
		try:
			return self._agent_list
		except Exception as e :
			raise e
	'''
	set Agent List, on which traffic will flow
	'''
	@agent_list.setter
	def agent_list(self,agent_list) :
		try :
			if not isinstance(agent_list,list):
				raise TypeError("agent_list must be set to array of str value")
			for item in agent_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._agent_list = agent_list
		except Exception as e :
			raise e


	'''
	get wanOpt
	'''
	@property
	def wanOpt(self) :
		try:
			return self._wanOpt
		except Exception as e :
			raise e
	'''
	set wanOpt
	'''
	@wanOpt.setter
	def wanOpt(self,wanOpt):
		try :
			if not isinstance(wanOpt,bool):
				raise TypeError("wanOpt must be set to bool value")
			self._wanOpt = wanOpt
		except Exception as e :
			raise e


	'''
	get Is this CB device configured to support GEO location.
	'''
	@property
	def geo_support(self) :
		try:
			return self._geo_support
		except Exception as e :
			raise e
	'''
	set Is this CB device configured to support GEO location.
	'''
	@geo_support.setter
	def geo_support(self,geo_support):
		try :
			if not isinstance(geo_support,bool):
				raise TypeError("geo_support must be set to bool value")
			self._geo_support = geo_support
		except Exception as e :
			raise e


	'''
	get hdx
	'''
	@property
	def hdx(self) :
		try:
			return self._hdx
		except Exception as e :
			raise e
	'''
	set hdx
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
	get BR IP Address
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set BR IP Address
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
	get BR IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set BR IP Address
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
	get appflowfeature
	'''
	@property
	def appflowfeature(self) :
		try:
			return self._appflowfeature
		except Exception as e :
			raise e
	'''
	set appflowfeature
	'''
	@appflowfeature.setter
	def appflowfeature(self,appflowfeature):
		try :
			if not isinstance(appflowfeature,bool):
				raise TypeError("appflowfeature must be set to bool value")
			self._appflowfeature = appflowfeature
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cbwanopt_appflowconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cbwanopt_appflowconfig_obj = cbwanopt_appflowconfig()
			option_ = options()
			option_._filter=filter_
			return cbwanopt_appflowconfig_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cbwanopt_appflowconfig resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cbwanopt_appflowconfig_obj = cbwanopt_appflowconfig()
			option_ = options()
			option_._count=True
			response = cbwanopt_appflowconfig_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cbwanopt_appflowconfig resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cbwanopt_appflowconfig_obj = cbwanopt_appflowconfig()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cbwanopt_appflowconfig_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cbwanopt_appflowconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cbwanopt_appflowconfig
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cbwanopt_appflowconfig_responses, response, "cbwanopt_appflowconfig_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cbwanopt_appflowconfig_response_array
				i=0
				error = [cbwanopt_appflowconfig() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cbwanopt_appflowconfig_response_array
			i=0
			cbwanopt_appflowconfig_objs = [cbwanopt_appflowconfig() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cbwanopt_appflowconfig'):
					for props in obj._cbwanopt_appflowconfig:
						result = service.payload_formatter.string_to_bulk_resource(cbwanopt_appflowconfig_response,self.__class__.__name__,props)
						cbwanopt_appflowconfig_objs[i] = result.cbwanopt_appflowconfig
						i=i+1
			return cbwanopt_appflowconfig_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cbwanopt_appflowconfig,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cbwanopt_appflowconfig_response(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_appflowconfig= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cbwanopt_appflowconfig= [ cbwanopt_appflowconfig() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cbwanopt_appflowconfig_responses(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_appflowconfig_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cbwanopt_appflowconfig_response_array = [ cbwanopt_appflowconfig() for _ in range(length)]
