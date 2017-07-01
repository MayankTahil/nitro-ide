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
Configuration for System Status resource
'''

class mps(base_resource):
	_maps_apikey= ""
	_build_number_short= ""
	_is_cloud= ""
	_current_time= ""
	_sysid= ""
	_hostname= ""
	_bios_version= ""
	_hostid= ""
	_is_member_of_default_group= ""
	_product_version= ""
	_deployment_type= ""
	_uptime= ""
	_current_user_permission= ""
	_platform= ""
	_hypervisor_uptime= ""
	_product_build_number= ""
	_serial= ""
	_privilege_feature= ""
	_host= ""
	_username= ""
	_current_tenant= ""
	_time_zone_offset= ""
	_build_number= ""
	_current_time_formatted= ""
	_time_zone= ""
	_product= ""
	_current_tenant_id= ""
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
			return "mps"
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
			return "mpss"
		except Exception as e :
			raise e



	'''
	get Maps API Key
	'''
	@property
	def maps_apikey(self) :
		try:
			return self._maps_apikey
		except Exception as e :
			raise e
	'''
	set Maps API Key
	'''
	@maps_apikey.setter
	def maps_apikey(self,maps_apikey):
		try :
			if not isinstance(maps_apikey,str):
				raise TypeError("maps_apikey must be set to str value")
			self._maps_apikey = maps_apikey
		except Exception as e :
			raise e


	'''
	get Build Number without Date
	'''
	@property
	def build_number_short(self) :
		try:
			return self._build_number_short
		except Exception as e :
			raise e


	'''
	get True if its a cloud deployment
	'''
	@property
	def is_cloud(self) :
		try:
			return self._is_cloud
		except Exception as e :
			raise e
	'''
	set True if its a cloud deployment
	'''
	@is_cloud.setter
	def is_cloud(self,is_cloud):
		try :
			if not isinstance(is_cloud,bool):
				raise TypeError("is_cloud must be set to bool value")
			self._is_cloud = is_cloud
		except Exception as e :
			raise e


	'''
	get Current Time
	'''
	@property
	def current_time(self) :
		try:
			return self._current_time
		except Exception as e :
			raise e


	'''
	get System Id
	'''
	@property
	def sysid(self) :
		try:
			return self._sysid
		except Exception as e :
			raise e


	'''
	get Host name on which system is running
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e


	'''
	get BIOS Version
	'''
	@property
	def bios_version(self) :
		try:
			return self._bios_version
		except Exception as e :
			raise e


	'''
	get Host Id
	'''
	@property
	def hostid(self) :
		try:
			return self._hostid
		except Exception as e :
			raise e


	'''
	get Is Member Of Default Group
	'''
	@property
	def is_member_of_default_group(self) :
		try:
			return self._is_member_of_default_group
		except Exception as e :
			raise e
	'''
	set Is Member Of Default Group
	'''
	@is_member_of_default_group.setter
	def is_member_of_default_group(self,is_member_of_default_group):
		try :
			if not isinstance(is_member_of_default_group,bool):
				raise TypeError("is_member_of_default_group must be set to bool value")
			self._is_member_of_default_group = is_member_of_default_group
		except Exception as e :
			raise e


	'''
	get Product Version
	'''
	@property
	def product_version(self) :
		try:
			return self._product_version
		except Exception as e :
			raise e


	'''
	get Indicates the type of deployment of MAS: standalone or ha or scaleout.
	'''
	@property
	def deployment_type(self) :
		try:
			return self._deployment_type
		except Exception as e :
			raise e
	'''
	set Indicates the type of deployment of MAS: standalone or ha or scaleout.
	'''
	@deployment_type.setter
	def deployment_type(self,deployment_type):
		try :
			if not isinstance(deployment_type,str):
				raise TypeError("deployment_type must be set to str value")
			self._deployment_type = deployment_type
		except Exception as e :
			raise e


	'''
	get Uptime
	'''
	@property
	def uptime(self) :
		try:
			return self._uptime
		except Exception as e :
			raise e


	'''
	get This property will show the permission type for current user
	'''
	@property
	def current_user_permission(self) :
		try:
			return self._current_user_permission
		except Exception as e :
			raise e


	'''
	get Platform
	'''
	@property
	def platform(self) :
		try:
			return self._platform
		except Exception as e :
			raise e


	'''
	get Hypervisor Uptime
	'''
	@property
	def hypervisor_uptime(self) :
		try:
			return self._hypervisor_uptime
		except Exception as e :
			raise e


	'''
	get Product Build Number
	'''
	@property
	def product_build_number(self) :
		try:
			return self._product_build_number
		except Exception as e :
			raise e


	'''
	get Serial Number
	'''
	@property
	def serial(self) :
		try:
			return self._serial
		except Exception as e :
			raise e


	'''
	get privilege_feature
	'''
	@property
	def privilege_feature(self) :
		try:
			return self._privilege_feature
		except Exception as e :
			raise e
	'''
	set privilege_feature
	'''
	@privilege_feature.setter
	def privilege_feature(self,privilege_feature):
		try :
			if not isinstance(privilege_feature,str):
				raise TypeError("privilege_feature must be set to str value")
			self._privilege_feature = privilege_feature
		except Exception as e :
			raise e


	'''
	get Host IP Address on which system is running, this will set for each client session only
	'''
	@property
	def host(self) :
		try:
			return self._host
		except Exception as e :
			raise e


	'''
	get User Name who is currently connected to the system
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Current Tenant Name for logged-in user
	'''
	@property
	def current_tenant(self) :
		try:
			return self._current_tenant
		except Exception as e :
			raise e


	'''
	get Time zone offset in minutes (Example:-330)
	'''
	@property
	def time_zone_offset(self) :
		try:
			return self._time_zone_offset
		except Exception as e :
			raise e


	'''
	get Build Number
	'''
	@property
	def build_number(self) :
		try:
			return self._build_number
		except Exception as e :
			raise e


	'''
	get Current Time (Formatted)
	'''
	@property
	def current_time_formatted(self) :
		try:
			return self._current_time_formatted
		except Exception as e :
			raise e


	'''
	get Server Time Zone
	'''
	@property
	def time_zone(self) :
		try:
			return self._time_zone
		except Exception as e :
			raise e


	'''
	get Product Name
	'''
	@property
	def product(self) :
		try:
			return self._product
		except Exception as e :
			raise e


	'''
	get Current Tenant Id for logged-in user
	'''
	@property
	def current_tenant_id(self) :
		try:
			return self._current_tenant_id
		except Exception as e :
			raise e

	'''
	Use this operation to reboot.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"reboot")
		except Exception as e :
			raise e

	'''
	Use this operation to get system status.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mps_obj=mps()
				response = mps_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mps resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mps_obj = mps()
			option_ = options()
			option_._filter=filter_
			return mps_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mps resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mps_obj = mps()
			option_ = options()
			option_._count=True
			response = mps_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mps resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mps_obj = mps()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mps_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mps_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mps
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mps_responses, response, "mps_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mps_response_array
				i=0
				error = [mps() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mps_response_array
			i=0
			mps_objs = [mps() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mps'):
					for props in obj._mps:
						result = service.payload_formatter.string_to_bulk_resource(mps_response,self.__class__.__name__,props)
						mps_objs[i] = result.mps
						i=i+1
			return mps_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mps,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mps_response(base_response):
	def __init__(self,length=1) :
		self.mps= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mps= [ mps() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mps_responses(base_response):
	def __init__(self,length=1) :
		self.mps_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mps_response_array = [ mps() for _ in range(length)]
