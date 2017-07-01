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
from massrc.com.citrix.mas.nitro.resource.config.admin.allocationgroup import allocationgroup
from massrc.com.citrix.mas.nitro.resource.config.admin.groupmember import groupmember


'''
Configuration for NetScaler Control Center allocates NetScaler instances according to the SLA that is defined as part this service package. resource
'''

class servicepackage(base_resource):
	_name= ""
	_cloudplatform_type= ""
	_max_devices_to_autoprovision= ""
	_description= ""
	_isdefault= ""
	_id= ""
	_allocationgroups=[]
	_tenantgroup= ""
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
			return "/admin/v1/servicepackages"
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
			return "servicepackage"
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
			return "servicepackages"
		except Exception as e :
			raise e



	'''
	get Name of service package.
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of service package.
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
	get Cloudplatform registered on MAS
	'''
	@property
	def cloudplatform_type(self) :
		try:
			return self._cloudplatform_type
		except Exception as e :
			raise e
	'''
	set Cloudplatform registered on MAS
	'''
	@cloudplatform_type.setter
	def cloudplatform_type(self,cloudplatform_type):
		try :
			if not isinstance(cloudplatform_type,str):
				raise TypeError("cloudplatform_type must be set to str value")
			self._cloudplatform_type = cloudplatform_type
		except Exception as e :
			raise e


	'''
	get Maximum number of devices to autoprovision
	'''
	@property
	def max_devices_to_autoprovision(self) :
		try:
			return self._max_devices_to_autoprovision
		except Exception as e :
			raise e
	'''
	set Maximum number of devices to autoprovision
	'''
	@max_devices_to_autoprovision.setter
	def max_devices_to_autoprovision(self,max_devices_to_autoprovision):
		try :
			if not isinstance(max_devices_to_autoprovision,str):
				raise TypeError("max_devices_to_autoprovision must be set to str value")
			self._max_devices_to_autoprovision = max_devices_to_autoprovision
		except Exception as e :
			raise e


	'''
	get Description for the service package
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description for the service package
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
	get Is this a default service package. Only one service package can be set as default service package. The default service package is used  for allotment in any lb configuration that is not associated with any service package. Possible values - 'true', 'false'
	'''
	@property
	def isdefault(self) :
		try:
			return self._isdefault
		except Exception as e :
			raise e
	'''
	set Is this a default service package. Only one service package can be set as default service package. The default service package is used  for allotment in any lb configuration that is not associated with any service package. Possible values - 'true', 'false'
	'''
	@isdefault.setter
	def isdefault(self,isdefault):
		try :
			if not isinstance(isdefault,str):
				raise TypeError("isdefault must be set to str value")
			self._isdefault = isdefault
		except Exception as e :
			raise e


	'''
	get Id is system generated key for service package
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for service package
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
	get Device allocation policy for each device type
	'''
	@property
	def allocationgroups(self) :
		try:
			return self._allocationgroups
		except Exception as e :
			raise e
	'''
	set Device allocation policy for each device type
	'''
	@allocationgroups.setter
	def allocationgroups(self,allocationgroups) :
		try :
			if not isinstance(allocationgroups,list):
				raise TypeError("allocationgroups must be set to array of allocationgroup value")
			for item in allocationgroups :
				if not isinstance(item,allocationgroup):
					raise TypeError("item must be set to allocationgroup value")
			self._allocationgroups = allocationgroups
		except Exception as e :
			raise e


	'''
	get Tenant group of the tenants which are part of the service package
	'''
	@property
	def tenantgroup(self) :
		try:
			return self._tenantgroup
		except Exception as e :
			raise e
	'''
	set Tenant group of the tenants which are part of the service package
	'''
	@tenantgroup.setter
	def tenantgroup(self,tenantgroup):
		try :
			if not isinstance(tenantgroup,groupmember):
				raise TypeError("tenantgroup must be set to groupmember value")
			self._tenantgroup = tenantgroup
		except Exception as e :
			raise e

	'''
	Use this operation to add a Service Package.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				servicepackage_obj= servicepackage()
				return cls.perform_operation_bulk_request(service,"add", resource,servicepackage_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete a Service Package.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					servicepackage_obj=servicepackage()
					return cls.delete_bulk_request(client,resource,servicepackage_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get Service Package(s).
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				servicepackage_obj=servicepackage()
				response = servicepackage_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify a Service Package.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				servicepackage_obj=servicepackage()
				return cls.update_bulk_request(client,resource,servicepackage_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of servicepackage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			servicepackage_obj = servicepackage()
			option_ = options()
			option_._filter=filter_
			return servicepackage_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the servicepackage resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			servicepackage_obj = servicepackage()
			option_ = options()
			option_._count=True
			response = servicepackage_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of servicepackage resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			servicepackage_obj = servicepackage()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = servicepackage_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(servicepackage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicepackage
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(servicepackage_responses, response, "servicepackage_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.servicepackage_response_array
				i=0
				error = [servicepackage() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.servicepackage_response_array
			i=0
			servicepackage_objs = [servicepackage() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_servicepackage'):
					for props in obj._servicepackage:
						result = service.payload_formatter.string_to_bulk_resource(servicepackage_response,self.__class__.__name__,props)
						servicepackage_objs[i] = result.servicepackage
						i=i+1
			return servicepackage_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(servicepackage,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class servicepackage_response(base_response):
	def __init__(self,length=1) :
		self.servicepackage= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.servicepackage= [ servicepackage() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class servicepackage_responses(base_response):
	def __init__(self,length=1) :
		self.servicepackage_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.servicepackage_response_array = [ servicepackage() for _ in range(length)]
