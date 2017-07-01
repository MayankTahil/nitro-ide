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
from massrc.com.citrix.mas.nitro.resource.config.mps.network_service_resource_profile import network_service_resource_profile
from massrc.com.citrix.mas.nitro.resource.config.mps.parameter import parameter


'''
Configuration for Network Service resource
'''

class network_service(base_resource):
	_template_name= ""
	_default_resource_profile= ""
	_min_resource_profile= ""
	_dependent_services= ""
	_formation_template_id= ""
	_id= ""
	_version= ""
	_name= ""
	_number_of_instances= ""
	_description= ""
	_license= ""
	_image= ""
	_parameters=[]
	_max_scale= ""
	_min_scale= ""
	_type= ""
	_vendor= ""
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
			return "network_service"
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
			return "network_services"
		except Exception as e :
			raise e



	'''
	get Service Template Name
	'''
	@property
	def template_name(self) :
		try:
			return self._template_name
		except Exception as e :
			raise e
	'''
	set Service Template Name
	'''
	@template_name.setter
	def template_name(self,template_name):
		try :
			if not isinstance(template_name,str):
				raise TypeError("template_name must be set to str value")
			self._template_name = template_name
		except Exception as e :
			raise e


	'''
	get default_resource_profile of the service
	'''
	@property
	def default_resource_profile(self) :
		try:
			return self._default_resource_profile
		except Exception as e :
			raise e
	'''
	set default_resource_profile of the service
	'''
	@default_resource_profile.setter
	def default_resource_profile(self,default_resource_profile):
		try :
			if not isinstance(default_resource_profile,network_service_resource_profile):
				raise TypeError("default_resource_profile must be set to network_service_resource_profile value")
			self._default_resource_profile = default_resource_profile
		except Exception as e :
			raise e


	'''
	get min_resource_profile
	'''
	@property
	def min_resource_profile(self) :
		try:
			return self._min_resource_profile
		except Exception as e :
			raise e
	'''
	set min_resource_profile
	'''
	@min_resource_profile.setter
	def min_resource_profile(self,min_resource_profile):
		try :
			if not isinstance(min_resource_profile,str):
				raise TypeError("min_resource_profile must be set to str value")
			self._min_resource_profile = min_resource_profile
		except Exception as e :
			raise e


	'''
	get Dependent Network Services
	'''
	@property
	def dependent_services(self) :
		try:
			return self._dependent_services
		except Exception as e :
			raise e
	'''
	set Dependent Network Services
	'''
	@dependent_services.setter
	def dependent_services(self,dependent_services):
		try :
			if not isinstance(dependent_services,str):
				raise TypeError("dependent_services must be set to str value")
			self._dependent_services = dependent_services
		except Exception as e :
			raise e


	'''
	get Template Id
	'''
	@property
	def formation_template_id(self) :
		try:
			return self._formation_template_id
		except Exception as e :
			raise e
	'''
	set Template Id
	'''
	@formation_template_id.setter
	def formation_template_id(self,formation_template_id):
		try :
			if not isinstance(formation_template_id,str):
				raise TypeError("formation_template_id must be set to str value")
			self._formation_template_id = formation_template_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the networks
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the networks
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
	get version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set version
	'''
	@version.setter
	def version(self,version):
		try :
			if not isinstance(version,str):
				raise TypeError("version must be set to str value")
			self._version = version
		except Exception as e :
			raise e


	'''
	get Network Service Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Network Service Name
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Number of instances of Service
	'''
	@property
	def number_of_instances(self) :
		try:
			return self._number_of_instances
		except Exception as e :
			raise e
	'''
	set Number of instances of Service
	'''
	@number_of_instances.setter
	def number_of_instances(self,number_of_instances):
		try :
			if not isinstance(number_of_instances,int):
				raise TypeError("number_of_instances must be set to int value")
			self._number_of_instances = number_of_instances
		except Exception as e :
			raise e


	'''
	get description
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set description
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
	get Service License File
	'''
	@property
	def license(self) :
		try:
			return self._license
		except Exception as e :
			raise e
	'''
	set Service License File
	'''
	@license.setter
	def license(self,license):
		try :
			if not isinstance(license,str):
				raise TypeError("license must be set to str value")
			self._license = license
		except Exception as e :
			raise e


	'''
	get Service Image Name
	'''
	@property
	def image(self) :
		try:
			return self._image
		except Exception as e :
			raise e
	'''
	set Service Image Name
	'''
	@image.setter
	def image(self,image):
		try :
			if not isinstance(image,str):
				raise TypeError("image must be set to str value")
			self._image = image
		except Exception as e :
			raise e


	'''
	get Parameters of the service
	'''
	@property
	def parameters(self) :
		try:
			return self._parameters
		except Exception as e :
			raise e
	'''
	set Parameters of the service
	'''
	@parameters.setter
	def parameters(self,parameters) :
		try :
			if not isinstance(parameters,list):
				raise TypeError("parameters must be set to array of parameter value")
			for item in parameters :
				if not isinstance(item,parameter):
					raise TypeError("item must be set to parameter value")
			self._parameters = parameters
		except Exception as e :
			raise e


	'''
	get max_scale
	'''
	@property
	def max_scale(self) :
		try:
			return self._max_scale
		except Exception as e :
			raise e
	'''
	set max_scale
	'''
	@max_scale.setter
	def max_scale(self,max_scale):
		try :
			if not isinstance(max_scale,int):
				raise TypeError("max_scale must be set to int value")
			self._max_scale = max_scale
		except Exception as e :
			raise e


	'''
	get min_scale
	'''
	@property
	def min_scale(self) :
		try:
			return self._min_scale
		except Exception as e :
			raise e
	'''
	set min_scale
	'''
	@min_scale.setter
	def min_scale(self,min_scale):
		try :
			if not isinstance(min_scale,int):
				raise TypeError("min_scale must be set to int value")
			self._min_scale = min_scale
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
	get vendor
	'''
	@property
	def vendor(self) :
		try:
			return self._vendor
		except Exception as e :
			raise e
	'''
	set vendor
	'''
	@vendor.setter
	def vendor(self,vendor):
		try :
			if not isinstance(vendor,str):
				raise TypeError("vendor must be set to str value")
			self._vendor = vendor
		except Exception as e :
			raise e

	'''
	Use this operation to get the Network Services.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_service_obj=network_service()
				response = network_service_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_service_obj = network_service()
			option_ = options()
			option_._filter=filter_
			return network_service_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_service resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_service_obj = network_service()
			option_ = options()
			option_._count=True
			response = network_service_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_service_obj = network_service()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_service_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_service
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_service_responses, response, "network_service_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_service_response_array
				i=0
				error = [network_service() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_service_response_array
			i=0
			network_service_objs = [network_service() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_service'):
					for props in obj._network_service:
						result = service.payload_formatter.string_to_bulk_resource(network_service_response,self.__class__.__name__,props)
						network_service_objs[i] = result.network_service
						i=i+1
			return network_service_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_service,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_service_response(base_response):
	def __init__(self,length=1) :
		self.network_service= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_service= [ network_service() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_service_responses(base_response):
	def __init__(self,length=1) :
		self.network_service_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_service_response_array = [ network_service() for _ in range(length)]
