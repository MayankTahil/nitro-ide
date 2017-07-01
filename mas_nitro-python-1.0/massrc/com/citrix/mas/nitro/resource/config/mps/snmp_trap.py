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
Configuration for SNMP Trap Destinations resource
'''

class snmp_trap(base_resource):
	_community= ""
	_version= ""
	_dest_server= ""
	_dest_port= ""
	_user_name=[]
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
			return "snmp_trap"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._dest_server
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
			return "snmp_traps"
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
	get SNMP version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e
	'''
	set SNMP version
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
	get Trap Destination Server Address
	'''
	@property
	def dest_server(self) :
		try:
			return self._dest_server
		except Exception as e :
			raise e
	'''
	set Trap Destination Server Address
	'''
	@dest_server.setter
	def dest_server(self,dest_server):
		try :
			if not isinstance(dest_server,str):
				raise TypeError("dest_server must be set to str value")
			self._dest_server = dest_server
		except Exception as e :
			raise e


	'''
	get Destination Port
	'''
	@property
	def dest_port(self) :
		try:
			return self._dest_port
		except Exception as e :
			raise e
	'''
	set Destination Port
	'''
	@dest_port.setter
	def dest_port(self,dest_port):
		try :
			if not isinstance(dest_port,int):
				raise TypeError("dest_port must be set to int value")
			self._dest_port = dest_port
		except Exception as e :
			raise e


	'''
	get Name of SNMP Trap User
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e
	'''
	set Name of SNMP Trap User
	'''
	@user_name.setter
	def user_name(self,user_name) :
		try :
			if not isinstance(user_name,list):
				raise TypeError("user_name must be set to array of str value")
			for item in user_name :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._user_name = user_name
		except Exception as e :
			raise e

	'''
	Use this operation to add snmp trap destination.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				snmp_trap_obj= snmp_trap()
				return cls.perform_operation_bulk_request(service,"add", resource,snmp_trap_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete snmp trap destination.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					snmp_trap_obj=snmp_trap()
					return cls.delete_bulk_request(client,resource,snmp_trap_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get snmp trap destination details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_trap_obj=snmp_trap()
				response = snmp_trap_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp trap destination.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_trap_obj=snmp_trap()
				return cls.update_bulk_request(client,resource,snmp_trap_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_trap resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_trap_obj = snmp_trap()
			option_ = options()
			option_._filter=filter_
			return snmp_trap_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_trap resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_trap_obj = snmp_trap()
			option_ = options()
			option_._count=True
			response = snmp_trap_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_trap resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_trap_obj = snmp_trap()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_trap_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_trap_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_trap
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_trap_responses, response, "snmp_trap_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_trap_response_array
				i=0
				error = [snmp_trap() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_trap_response_array
			i=0
			snmp_trap_objs = [snmp_trap() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_trap'):
					for props in obj._snmp_trap:
						result = service.payload_formatter.string_to_bulk_resource(snmp_trap_response,self.__class__.__name__,props)
						snmp_trap_objs[i] = result.snmp_trap
						i=i+1
			return snmp_trap_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_trap,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_trap_response(base_response):
	def __init__(self,length=1) :
		self.snmp_trap= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_trap= [ snmp_trap() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_trap_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_trap_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_trap_response_array = [ snmp_trap() for _ in range(length)]
