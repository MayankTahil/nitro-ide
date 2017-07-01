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
Configuration for Netowork Service Deployment resource
'''

class network_service_dpl(base_resource):
	_template_name= ""
	_name= ""
	_number_of_instances= ""
	_resource_profile= ""
	_license= ""
	_image= ""
	_parameters=[]
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
			return "network_service_dpl"
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
			return "network_service_dpls"
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
	get resource_profile of the service deployment
	'''
	@property
	def resource_profile(self) :
		try:
			return self._resource_profile
		except Exception as e :
			raise e
	'''
	set resource_profile of the service deployment
	'''
	@resource_profile.setter
	def resource_profile(self,resource_profile):
		try :
			if not isinstance(resource_profile,network_service_resource_profile):
				raise TypeError("resource_profile must be set to network_service_resource_profile value")
			self._resource_profile = resource_profile
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
	get 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set 
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
	Use this operation to get the network service deployment.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				network_service_dpl_obj=network_service_dpl()
				response = network_service_dpl_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of network_service_dpl resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			network_service_dpl_obj = network_service_dpl()
			option_ = options()
			option_._filter=filter_
			return network_service_dpl_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the network_service_dpl resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			network_service_dpl_obj = network_service_dpl()
			option_ = options()
			option_._count=True
			response = network_service_dpl_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of network_service_dpl resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			network_service_dpl_obj = network_service_dpl()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = network_service_dpl_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(network_service_dpl_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.network_service_dpl
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(network_service_dpl_responses, response, "network_service_dpl_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.network_service_dpl_response_array
				i=0
				error = [network_service_dpl() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.network_service_dpl_response_array
			i=0
			network_service_dpl_objs = [network_service_dpl() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_network_service_dpl'):
					for props in obj._network_service_dpl:
						result = service.payload_formatter.string_to_bulk_resource(network_service_dpl_response,self.__class__.__name__,props)
						network_service_dpl_objs[i] = result.network_service_dpl
						i=i+1
			return network_service_dpl_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(network_service_dpl,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class network_service_dpl_response(base_response):
	def __init__(self,length=1) :
		self.network_service_dpl= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.network_service_dpl= [ network_service_dpl() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class network_service_dpl_responses(base_response):
	def __init__(self,length=1) :
		self.network_service_dpl_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.network_service_dpl_response_array = [ network_service_dpl() for _ in range(length)]
