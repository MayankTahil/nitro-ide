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
Configuration for SNMP MIB Information resource
'''

class snmp_mib(base_resource):
	_custom_id= ""
	_id= ""
	_location= ""
	_name= ""
	_contact= ""
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
			return "snmp_mib"
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
			return "snmp_mibs"
		except Exception as e :
			raise e



	'''
	get Custom identification number for appliance
	'''
	@property
	def custom_id(self) :
		try:
			return self._custom_id
		except Exception as e :
			raise e
	'''
	set Custom identification number for appliance
	'''
	@custom_id.setter
	def custom_id(self,custom_id):
		try :
			if not isinstance(custom_id,str):
				raise TypeError("custom_id must be set to str value")
			self._custom_id = custom_id
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	Physical location of appliance
	'''
	@property
	def location(self):
		try:
			return self._location
		except Exception as e :
			raise e
	'''
	Physical location of appliance
	'''
	@location.setter
	def location(self,location):
		try :
			if not isinstance(location,str):
				raise TypeError("location must be set to str value")
			self._location = location
		except Exception as e :
			raise e

	'''
	Name for appliance
	'''
	@property
	def name(self):
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	Name for appliance
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
	Name of the administrator for appliance.
	'''
	@property
	def contact(self):
		try:
			return self._contact
		except Exception as e :
			raise e
	'''
	Name of the administrator for appliance.
	'''
	@contact.setter
	def contact(self,contact):
		try :
			if not isinstance(contact,str):
				raise TypeError("contact must be set to str value")
			self._contact = contact
		except Exception as e :
			raise e

	'''
	Use this operation to get snmp mib information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				snmp_mib_obj=snmp_mib()
				response = snmp_mib_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify snmp mib information.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				snmp_mib_obj=snmp_mib()
				return cls.update_bulk_request(client,resource,snmp_mib_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of snmp_mib resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			snmp_mib_obj = snmp_mib()
			option_ = options()
			option_._filter=filter_
			return snmp_mib_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the snmp_mib resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			snmp_mib_obj = snmp_mib()
			option_ = options()
			option_._count=True
			response = snmp_mib_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of snmp_mib resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			snmp_mib_obj = snmp_mib()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = snmp_mib_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(snmp_mib_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp_mib
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(snmp_mib_responses, response, "snmp_mib_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.snmp_mib_response_array
				i=0
				error = [snmp_mib() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.snmp_mib_response_array
			i=0
			snmp_mib_objs = [snmp_mib() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_snmp_mib'):
					for props in obj._snmp_mib:
						result = service.payload_formatter.string_to_bulk_resource(snmp_mib_response,self.__class__.__name__,props)
						snmp_mib_objs[i] = result.snmp_mib
						i=i+1
			return snmp_mib_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(snmp_mib,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class snmp_mib_response(base_response):
	def __init__(self,length=1) :
		self.snmp_mib= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.snmp_mib= [ snmp_mib() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class snmp_mib_responses(base_response):
	def __init__(self,length=1) :
		self.snmp_mib_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.snmp_mib_response_array = [ snmp_mib() for _ in range(length)]
