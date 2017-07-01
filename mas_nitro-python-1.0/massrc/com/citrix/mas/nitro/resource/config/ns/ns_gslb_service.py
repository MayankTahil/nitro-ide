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
Configuration for NetScaler GSLB Service resource
'''

class ns_gslb_service(base_resource):
	_fqdn= ""
	_password= ""
	_sites= ""
	_tenant= ""
	_id= ""
	_siteList=[]
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
			return "ns_gslb_service"
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
			return "ns_gslb_services"
		except Exception as e :
			raise e



	'''
	get Domain Name
	'''
	@property
	def fqdn(self) :
		try:
			return self._fqdn
		except Exception as e :
			raise e
	'''
	set Domain Name
	'''
	@fqdn.setter
	def fqdn(self,fqdn):
		try :
			if not isinstance(fqdn,str):
				raise TypeError("fqdn must be set to str value")
			self._fqdn = fqdn
		except Exception as e :
			raise e


	'''
	get The pass-phrase that was used to encrypt the private-key.
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set The pass-phrase that was used to encrypt the private-key.
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get List of sites
	'''
	@property
	def sites(self) :
		try:
			return self._sites
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def tenant(self) :
		try:
			return self._tenant
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the NetScaler GSLB Service
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the NetScaler GSLB Service
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
	List of sites
	'''
	@property
	def siteList(self) :
		try:
			return self._siteList
		except Exception as e :
			raise e
	'''
	List of sites
	'''
	@siteList.setter
	def siteList(self,siteList) :
		try :
			if not isinstance(siteList,list):
				raise TypeError("siteList must be set to array of str value")
			for item in siteList :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._siteList = siteList
		except Exception as e :
			raise e

	'''
	Use this operation to add NetScaler GSLB Service.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_gslb_service_obj= ns_gslb_service()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_gslb_service_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete NetScaler GSLB Service.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_gslb_service_obj=ns_gslb_service()
					return cls.delete_bulk_request(client,resource,ns_gslb_service_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler GSLB Service.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_gslb_service_obj=ns_gslb_service()
				response = ns_gslb_service_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler GSLB Service.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_gslb_service_obj=ns_gslb_service()
				return cls.update_bulk_request(client,resource,ns_gslb_service_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_gslb_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_gslb_service_obj = ns_gslb_service()
			option_ = options()
			option_._filter=filter_
			return ns_gslb_service_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_gslb_service resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_gslb_service_obj = ns_gslb_service()
			option_ = options()
			option_._count=True
			response = ns_gslb_service_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_gslb_service resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_gslb_service_obj = ns_gslb_service()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_gslb_service_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_gslb_service_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_gslb_service
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_gslb_service_responses, response, "ns_gslb_service_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_gslb_service_response_array
				i=0
				error = [ns_gslb_service() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_gslb_service_response_array
			i=0
			ns_gslb_service_objs = [ns_gslb_service() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_gslb_service'):
					for props in obj._ns_gslb_service:
						result = service.payload_formatter.string_to_bulk_resource(ns_gslb_service_response,self.__class__.__name__,props)
						ns_gslb_service_objs[i] = result.ns_gslb_service
						i=i+1
			return ns_gslb_service_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_gslb_service,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_gslb_service_response(base_response):
	def __init__(self,length=1) :
		self.ns_gslb_service= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_gslb_service= [ ns_gslb_service() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_gslb_service_responses(base_response):
	def __init__(self,length=1) :
		self.ns_gslb_service_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_gslb_service_response_array = [ ns_gslb_service() for _ in range(length)]
