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
Configuration for NS MPX Cluster Template resource
'''

class ns_mpxcluster_template(base_resource):
	_cco= ""
	_clip= ""
	_backplane= ""
	_clusterid= ""
	_devices=[]
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
			return "ns_mpxcluster_template"
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
			return "ns_mpxcluster_templates"
		except Exception as e :
			raise e



	'''
	get CCO IP address
	'''
	@property
	def cco(self) :
		try:
			return self._cco
		except Exception as e :
			raise e
	'''
	set CCO IP address
	'''
	@cco.setter
	def cco(self,cco):
		try :
			if not isinstance(cco,str):
				raise TypeError("cco must be set to str value")
			self._cco = cco
		except Exception as e :
			raise e


	'''
	get Cluster IPAddress
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IPAddress
	'''
	@clip.setter
	def clip(self,clip):
		try :
			if not isinstance(clip,str):
				raise TypeError("clip must be set to str value")
			self._clip = clip
		except Exception as e :
			raise e


	'''
	get Backplane Interface
	'''
	@property
	def backplane(self) :
		try:
			return self._backplane
		except Exception as e :
			raise e
	'''
	set Backplane Interface
	'''
	@backplane.setter
	def backplane(self,backplane):
		try :
			if not isinstance(backplane,str):
				raise TypeError("backplane must be set to str value")
			self._backplane = backplane
		except Exception as e :
			raise e


	'''
	get Cluster Id
	'''
	@property
	def clusterid(self) :
		try:
			return self._clusterid
		except Exception as e :
			raise e
	'''
	set Cluster Id
	'''
	@clusterid.setter
	def clusterid(self,clusterid):
		try :
			if not isinstance(clusterid,int):
				raise TypeError("clusterid must be set to int value")
			self._clusterid = clusterid
		except Exception as e :
			raise e


	'''
	get Device IP Address Array on which template is applied
	'''
	@property
	def devices(self) :
		try:
			return self._devices
		except Exception as e :
			raise e
	'''
	set Device IP Address Array on which template is applied
	'''
	@devices.setter
	def devices(self,devices) :
		try :
			if not isinstance(devices,list):
				raise TypeError("devices must be set to array of str value")
			for item in devices :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._devices = devices
		except Exception as e :
			raise e

	'''
	Use this operation to get MPX Cluster Info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_mpxcluster_template_obj=ns_mpxcluster_template()
				response = ns_mpxcluster_template_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_mpxcluster_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_mpxcluster_template_obj = ns_mpxcluster_template()
			option_ = options()
			option_._filter=filter_
			return ns_mpxcluster_template_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_mpxcluster_template resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_mpxcluster_template_obj = ns_mpxcluster_template()
			option_ = options()
			option_._count=True
			response = ns_mpxcluster_template_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_mpxcluster_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_mpxcluster_template_obj = ns_mpxcluster_template()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_mpxcluster_template_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_mpxcluster_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_mpxcluster_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_mpxcluster_template_responses, response, "ns_mpxcluster_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_mpxcluster_template_response_array
				i=0
				error = [ns_mpxcluster_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_mpxcluster_template_response_array
			i=0
			ns_mpxcluster_template_objs = [ns_mpxcluster_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_mpxcluster_template'):
					for props in obj._ns_mpxcluster_template:
						result = service.payload_formatter.string_to_bulk_resource(ns_mpxcluster_template_response,self.__class__.__name__,props)
						ns_mpxcluster_template_objs[i] = result.ns_mpxcluster_template
						i=i+1
			return ns_mpxcluster_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_mpxcluster_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_mpxcluster_template_response(base_response):
	def __init__(self,length=1) :
		self.ns_mpxcluster_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_mpxcluster_template= [ ns_mpxcluster_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_mpxcluster_template_responses(base_response):
	def __init__(self,length=1) :
		self.ns_mpxcluster_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_mpxcluster_template_response_array = [ ns_mpxcluster_template() for _ in range(length)]
