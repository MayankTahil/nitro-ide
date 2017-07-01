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
Configuration for Members resource
'''

class member(base_resource):
	_admin_state_up= ""
	_status= ""
	_protocol_port= ""
	_neutron_uri= ""
	_tenant_id= ""
	_pool_id= ""
	_weight= ""
	_id= ""
	_address= ""
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
			return "/v2.0/lb/members"
		except Exception as e :
			raise e

	'''
	get the plural object name
	'''
	@staticmethod
	def get_plural_object_name() :
		try:
			return "member"
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
			return "member"
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
			return "members"
		except Exception as e :
			raise e



	'''
	get admin_state_up of  member
	'''
	@property
	def admin_state_up(self) :
		try:
			return self._admin_state_up
		except Exception as e :
			raise e
	'''
	set admin_state_up of  member
	'''
	@admin_state_up.setter
	def admin_state_up(self,admin_state_up):
		try :
			if not isinstance(admin_state_up,str):
				raise TypeError("admin_state_up must be set to str value")
			self._admin_state_up = admin_state_up
		except Exception as e :
			raise e


	'''
	get status of member
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e
	'''
	set status of member
	'''
	@status.setter
	def status(self,status):
		try :
			if not isinstance(status,str):
				raise TypeError("status must be set to str value")
			self._status = status
		except Exception as e :
			raise e


	'''
	get protocol_port of member
	'''
	@property
	def protocol_port(self) :
		try:
			return self._protocol_port
		except Exception as e :
			raise e
	'''
	set protocol_port of member
	'''
	@protocol_port.setter
	def protocol_port(self,protocol_port):
		try :
			if not isinstance(protocol_port,str):
				raise TypeError("protocol_port must be set to str value")
			self._protocol_port = protocol_port
		except Exception as e :
			raise e


	'''
	get URI of neutron service in member
	'''
	@property
	def neutron_uri(self) :
		try:
			return self._neutron_uri
		except Exception as e :
			raise e
	'''
	set URI of neutron service in member
	'''
	@neutron_uri.setter
	def neutron_uri(self,neutron_uri):
		try :
			if not isinstance(neutron_uri,str):
				raise TypeError("neutron_uri must be set to str value")
			self._neutron_uri = neutron_uri
		except Exception as e :
			raise e


	'''
	get tenant_id of member.
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set tenant_id of member.
	'''
	@tenant_id.setter
	def tenant_id(self,tenant_id):
		try :
			if not isinstance(tenant_id,str):
				raise TypeError("tenant_id must be set to str value")
			self._tenant_id = tenant_id
		except Exception as e :
			raise e


	'''
	get pool_id of member
	'''
	@property
	def pool_id(self) :
		try:
			return self._pool_id
		except Exception as e :
			raise e
	'''
	set pool_id of member
	'''
	@pool_id.setter
	def pool_id(self,pool_id):
		try :
			if not isinstance(pool_id,str):
				raise TypeError("pool_id must be set to str value")
			self._pool_id = pool_id
		except Exception as e :
			raise e


	'''
	get weight of member
	'''
	@property
	def weight(self) :
		try:
			return self._weight
		except Exception as e :
			raise e
	'''
	set weight of member
	'''
	@weight.setter
	def weight(self,weight):
		try :
			if not isinstance(weight,str):
				raise TypeError("weight must be set to str value")
			self._weight = weight
		except Exception as e :
			raise e


	'''
	get Id is system generated key for member
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for member
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
	get address of member
	'''
	@property
	def address(self) :
		try:
			return self._address
		except Exception as e :
			raise e
	'''
	set address of member
	'''
	@address.setter
	def address(self,address):
		try :
			if not isinstance(address,str):
				raise TypeError("address must be set to str value")
			self._address = address
		except Exception as e :
			raise e

	'''
	Use this operation to get member cloud details.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				member_obj=member()
				response = member_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of member resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			member_obj = member()
			option_ = options()
			option_._filter=filter_
			return member_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the member resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			member_obj = member()
			option_ = options()
			option_._count=True
			response = member_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of member resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			member_obj = member()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = member_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(member_response, response, self.__class__.__name__,class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.member
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(member_responses, response, "member_response_array", class_name=self.__class__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.member_response_array
				i=0
				error = [member() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.member_response_array
			i=0
			member_objs = [member() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_member'):
					for props in obj._member:
						result = service.payload_formatter.string_to_bulk_resource(member_response,self.__class__.__name__,props)
						member_objs[i] = result.member
						i=i+1
			return response
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(member,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class member_response(base_response):
	def __init__(self,length=1) :
		self.member= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.member= [ member() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class member_responses(base_response):
	def __init__(self,length=1) :
		self.member_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.member_response_array = [ member() for _ in range(length)]
