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
Configuration for Trap Forward Profile resource
'''

class trap_forward_profile(base_resource):
	_trap_destination_port= ""
	_tenant_id= ""
	_trap_community= ""
	_id= ""
	_trap_destination= ""
	_profile_name= ""
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
			return "trap_forward_profile"
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
			return "trap_forward_profiles"
		except Exception as e :
			raise e



	'''
	get SNMP port to forward trap 
	'''
	@property
	def trap_destination_port(self) :
		try:
			return self._trap_destination_port
		except Exception as e :
			raise e
	'''
	set SNMP port to forward trap 
	'''
	@trap_destination_port.setter
	def trap_destination_port(self,trap_destination_port):
		try :
			if not isinstance(trap_destination_port,str):
				raise TypeError("trap_destination_port must be set to str value")
			self._trap_destination_port = trap_destination_port
		except Exception as e :
			raise e


	'''
	get Tenant Id 
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get SNMP community.
	'''
	@property
	def trap_community(self) :
		try:
			return self._trap_community
		except Exception as e :
			raise e
	'''
	set SNMP community.
	'''
	@trap_community.setter
	def trap_community(self,trap_community):
		try :
			if not isinstance(trap_community,str):
				raise TypeError("trap_community must be set to str value")
			self._trap_community = trap_community
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the mail profile.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the mail profile.
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
	get SMTP server name
	'''
	@property
	def trap_destination(self) :
		try:
			return self._trap_destination
		except Exception as e :
			raise e
	'''
	set SMTP server name
	'''
	@trap_destination.setter
	def trap_destination(self,trap_destination):
		try :
			if not isinstance(trap_destination,str):
				raise TypeError("trap_destination must be set to str value")
			self._trap_destination = trap_destination
		except Exception as e :
			raise e


	'''
	get Profile name for the mail setting.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name for the mail setting.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Use this operation to add trap_forward profile..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				trap_forward_profile_obj= trap_forward_profile()
				return cls.perform_operation_bulk_request(service,"add", resource,trap_forward_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete trap_forward profile..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					trap_forward_profile_obj=trap_forward_profile()
					return cls.delete_bulk_request(client,resource,trap_forward_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get trap_forward profile..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				trap_forward_profile_obj=trap_forward_profile()
				response = trap_forward_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify trap_forward profile..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				trap_forward_profile_obj=trap_forward_profile()
				return cls.update_bulk_request(client,resource,trap_forward_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of trap_forward_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			trap_forward_profile_obj = trap_forward_profile()
			option_ = options()
			option_._filter=filter_
			return trap_forward_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the trap_forward_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			trap_forward_profile_obj = trap_forward_profile()
			option_ = options()
			option_._count=True
			response = trap_forward_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of trap_forward_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			trap_forward_profile_obj = trap_forward_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = trap_forward_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(trap_forward_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.trap_forward_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(trap_forward_profile_responses, response, "trap_forward_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.trap_forward_profile_response_array
				i=0
				error = [trap_forward_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.trap_forward_profile_response_array
			i=0
			trap_forward_profile_objs = [trap_forward_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_trap_forward_profile'):
					for props in obj._trap_forward_profile:
						result = service.payload_formatter.string_to_bulk_resource(trap_forward_profile_response,self.__class__.__name__,props)
						trap_forward_profile_objs[i] = result.trap_forward_profile
						i=i+1
			return trap_forward_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(trap_forward_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class trap_forward_profile_response(base_response):
	def __init__(self,length=1) :
		self.trap_forward_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.trap_forward_profile= [ trap_forward_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class trap_forward_profile_responses(base_response):
	def __init__(self,length=1) :
		self.trap_forward_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.trap_forward_profile_response_array = [ trap_forward_profile() for _ in range(length)]
