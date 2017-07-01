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
from massrc.com.citrix.mas.nitro.resource.config.admin.images import images
from massrc.com.citrix.mas.nitro.resource.config.admin.server_boundaries import server_boundaries
from massrc.com.citrix.mas.nitro.resource.config.admin.management_networks import management_networks
from massrc.com.citrix.mas.nitro.resource.config.admin.profiles import profiles
from massrc.com.citrix.mas.nitro.resource.config.admin.profiles import profiles


'''
Configuration for Provision settings can be used to configure global settings such as management network, the image that can be used to provision new NS devices, profiles and licenses. resource
'''

class provision_setting(base_resource):
	_images=[]
	_server_boundaries=[]
	_management_networks=[]
	_licenses=[]
	_profiles=[]
	__count=""

	'''
	get the resource url
	'''
	def get_resource_url(self) :
		try:
			return self.process_url(self.get_unprocessed_url()) 
		except Exception as e :
			raise e

	'''
	get the unprocessed resource url
	'''
	def get_unprocessed_url(self) :
		try:
			return "/admin/v1/provision_settings"
		except Exception as e :
			raise e

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
			return "provision_setting"
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
			return "provision_settings"
		except Exception as e :
			raise e



	'''
	get Image that will be used for provisioning new devices.
	'''
	@property
	def images(self) :
		try:
			return self._images
		except Exception as e :
			raise e
	'''
	set Image that will be used for provisioning new devices.
	'''
	@images.setter
	def images(self,images) :
		try :
			if not isinstance(images,list):
				raise TypeError("images must be set to array of images value")
			for item in images :
				if not isinstance(item,images):
					raise TypeError("item must be set to images value")
			self._images = images
		except Exception as e :
			raise e


	'''
	get Server boundaries present in provision settings.
	'''
	@property
	def server_boundaries(self) :
		try:
			return self._server_boundaries
		except Exception as e :
			raise e
	'''
	set Server boundaries present in provision settings.
	'''
	@server_boundaries.setter
	def server_boundaries(self,server_boundaries) :
		try :
			if not isinstance(server_boundaries,list):
				raise TypeError("server_boundaries must be set to array of server_boundaries value")
			for item in server_boundaries :
				if not isinstance(item,server_boundaries):
					raise TypeError("item must be set to server_boundaries value")
			self._server_boundaries = server_boundaries
		except Exception as e :
			raise e


	'''
	get Management Networks of OpenStack that has to be registered with Control Centre.
	'''
	@property
	def management_networks(self) :
		try:
			return self._management_networks
		except Exception as e :
			raise e
	'''
	set Management Networks of OpenStack that has to be registered with Control Centre.
	'''
	@management_networks.setter
	def management_networks(self,management_networks) :
		try :
			if not isinstance(management_networks,list):
				raise TypeError("management_networks must be set to array of management_networks value")
			for item in management_networks :
				if not isinstance(item,management_networks):
					raise TypeError("item must be set to management_networks value")
			self._management_networks = management_networks
		except Exception as e :
			raise e


	'''
	get Licenses that will be used for newly provisioned devices.
	'''
	@property
	def licenses(self) :
		try:
			return self._licenses
		except Exception as e :
			raise e
	'''
	set Licenses that will be used for newly provisioned devices.
	'''
	@licenses.setter
	def licenses(self,licenses) :
		try :
			if not isinstance(licenses,list):
				raise TypeError("licenses must be set to array of profiles value")
			for item in licenses :
				if not isinstance(item,profiles):
					raise TypeError("item must be set to profiles value")
			self._licenses = licenses
		except Exception as e :
			raise e


	'''
	get Profile that will be used for newly provisioned devices.
	'''
	@property
	def profiles(self) :
		try:
			return self._profiles
		except Exception as e :
			raise e
	'''
	set Profile that will be used for newly provisioned devices.
	'''
	@profiles.setter
	def profiles(self,profiles) :
		try :
			if not isinstance(profiles,list):
				raise TypeError("profiles must be set to array of profiles value")
			for item in profiles :
				if not isinstance(item,profiles):
					raise TypeError("item must be set to profiles value")
			self._profiles = profiles
		except Exception as e :
			raise e

	'''
	Use this operation to get provision_setting details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				provision_setting_obj=provision_setting()
				response = provision_setting_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify provision_setting details.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				provision_setting_obj=provision_setting()
				return cls.update_bulk_request(client,resource,provision_setting_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of provision_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			provision_setting_obj = provision_setting()
			option_ = options()
			option_._filter=filter_
			return provision_setting_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the provision_setting resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			provision_setting_obj = provision_setting()
			option_ = options()
			option_._count=True
			response = provision_setting_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of provision_setting resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			provision_setting_obj = provision_setting()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = provision_setting_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(provision_setting_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.provision_setting
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(provision_setting_responses, response, "provision_setting_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.provision_setting_response_array
				i=0
				error = [provision_setting() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.provision_setting_response_array
			i=0
			provision_setting_objs = [provision_setting() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_provision_setting'):
					for props in obj._provision_setting:
						result = service.payload_formatter.string_to_bulk_resource(provision_setting_response,self.__class__.__name__,props)
						provision_setting_objs[i] = result.provision_setting
						i=i+1
			return provision_setting_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(provision_setting,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class provision_setting_response(base_response):
	def __init__(self,length=1) :
		self.provision_setting= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.provision_setting= [ provision_setting() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class provision_setting_responses(base_response):
	def __init__(self,length=1) :
		self.provision_setting_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.provision_setting_response_array = [ provision_setting() for _ in range(length)]
