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
Configuration for SNMP Agent Manager configuration resource
'''

class snmp_manager(base_resource):
	_community= ""
	_netmask= ""
	_ip_address= ""
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
			return "snmp_manager"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._ip_address
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
			return "snmp_managers"
		except Exception as e :
			raise e



	'''
	get Community Name
	'''
	@property
	def community(self) :
		try:
			return self._community
		except Exception as e :
			raise e
	'''
	set Community Name
	'''
	@community.setter
	def community(self,community):
		try :
			if not isinstance(community,str):
				raise TypeError("community must be set to str value")
			self._community = community
		except Exception as e :
			raise e


	'''
	get Netmask
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set Netmask
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Manager IPAddress
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set Manager IPAddress
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
	Use this operation to add SNMP Manager.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				snmp_manager_obj= snmp_manager()
				return cls.perform_operation_bulk_request(service,"add", resource,snmp_manager_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete SNMP Manager.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					snmp_manager_obj=snmp_manager()
					return cls.delete_bulk_request(client,resource,snmp_manager_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get SNMP Manager details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_manager_obj=snmp_manager()
				response = snmp_manager_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify SNMP Manager.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_manager_obj=snmp_manager()
				return cls.update_bulk_request(client,resource,snmp_manager_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_manager resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_manager_obj = snmp_manager()
			option_ = options()
			option_._filter=filter_
			return snmp_manager_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_manager resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_manager_obj = snmp_manager()
			option_ = options()
			option_._count=True
			response = snmp_manager_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_manager resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_manager_obj = snmp_manager()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_manager_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_manager_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_manager
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_manager_responses, response, "snmp_manager_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_manager_response_array
				i=0
				error = [snmp_manager() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_manager_response_array
			i=0
			snmp_manager_objs = [snmp_manager() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_manager'):
					for props in obj._snmp_manager:
						result = service.payload_formatter.string_to_bulk_resource(snmp_manager_response,self.__class__.__name__,props)
						snmp_manager_objs[i] = result.snmp_manager
						i=i+1
			return snmp_manager_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_manager,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_manager_response(base_response):
	def __init__(self,length=1) :
		self.snmp_manager= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_manager= [ snmp_manager() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_manager_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_manager_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_manager_response_array = [ snmp_manager() for _ in range(length)]
