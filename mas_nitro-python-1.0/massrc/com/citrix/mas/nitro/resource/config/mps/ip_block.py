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
Configuration for This collection holds private ip block information. resource
'''

class ip_block(base_resource):
	_longitude= ""
	_region_code= ""
	_end_ip_num= ""
	_country_code= ""
	_name= ""
	_description= ""
	_tenant_id= ""
	_city= ""
	_latitude= ""
	_id= ""
	_start_ip_num= ""
	_custom_city= ""
	_custom_country= ""
	_country= ""
	_end_ip= ""
	_start_ip= ""
	_custom_region= ""
	_region= ""
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
			return "ip_block"
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
			return "ip_blocks"
		except Exception as e :
			raise e



	'''
	get longitude
	'''
	@property
	def longitude(self) :
		try:
			return self._longitude
		except Exception as e :
			raise e
	'''
	set longitude
	'''
	@longitude.setter
	def longitude(self,longitude):
		try :
			if not isinstance(longitude,float):
				raise TypeError("longitude must be set to float value")
			self._longitude = longitude
		except Exception as e :
			raise e


	'''
	get region_code
	'''
	@property
	def region_code(self) :
		try:
			return self._region_code
		except Exception as e :
			raise e
	'''
	set region_code
	'''
	@region_code.setter
	def region_code(self,region_code):
		try :
			if not isinstance(region_code,str):
				raise TypeError("region_code must be set to str value")
			self._region_code = region_code
		except Exception as e :
			raise e


	'''
	get end_ip_num
	'''
	@property
	def end_ip_num(self) :
		try:
			return self._end_ip_num
		except Exception as e :
			raise e
	'''
	set end_ip_num
	'''
	@end_ip_num.setter
	def end_ip_num(self,end_ip_num):
		try :
			if not isinstance(end_ip_num,float):
				raise TypeError("end_ip_num must be set to float value")
			self._end_ip_num = end_ip_num
		except Exception as e :
			raise e


	'''
	get country_code
	'''
	@property
	def country_code(self) :
		try:
			return self._country_code
		except Exception as e :
			raise e
	'''
	set country_code
	'''
	@country_code.setter
	def country_code(self,country_code):
		try :
			if not isinstance(country_code,str):
				raise TypeError("country_code must be set to str value")
			self._country_code = country_code
		except Exception as e :
			raise e


	'''
	get name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set name
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
	get Description about Ip Block
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description about Ip Block
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
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get city
	'''
	@property
	def city(self) :
		try:
			return self._city
		except Exception as e :
			raise e
	'''
	set city
	'''
	@city.setter
	def city(self,city):
		try :
			if not isinstance(city,str):
				raise TypeError("city must be set to str value")
			self._city = city
		except Exception as e :
			raise e


	'''
	get latitude
	'''
	@property
	def latitude(self) :
		try:
			return self._latitude
		except Exception as e :
			raise e
	'''
	set latitude
	'''
	@latitude.setter
	def latitude(self,latitude):
		try :
			if not isinstance(latitude,float):
				raise TypeError("latitude must be set to float value")
			self._latitude = latitude
		except Exception as e :
			raise e


	'''
	get Id is IP block name
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is IP block name
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
	get start_ip_num
	'''
	@property
	def start_ip_num(self) :
		try:
			return self._start_ip_num
		except Exception as e :
			raise e
	'''
	set start_ip_num
	'''
	@start_ip_num.setter
	def start_ip_num(self,start_ip_num):
		try :
			if not isinstance(start_ip_num,float):
				raise TypeError("start_ip_num must be set to float value")
			self._start_ip_num = start_ip_num
		except Exception as e :
			raise e

	'''
	custom_city
	'''
	@property
	def custom_city(self):
		try:
			return self._custom_city
		except Exception as e :
			raise e
	'''
	custom_city
	'''
	@custom_city.setter
	def custom_city(self,custom_city):
		try :
			if not isinstance(custom_city,bool):
				raise TypeError("custom_city must be set to bool value")
			self._custom_city = custom_city
		except Exception as e :
			raise e

	'''
	custom_country
	'''
	@property
	def custom_country(self):
		try:
			return self._custom_country
		except Exception as e :
			raise e
	'''
	custom_country
	'''
	@custom_country.setter
	def custom_country(self,custom_country):
		try :
			if not isinstance(custom_country,bool):
				raise TypeError("custom_country must be set to bool value")
			self._custom_country = custom_country
		except Exception as e :
			raise e

	'''
	country
	'''
	@property
	def country(self):
		try:
			return self._country
		except Exception as e :
			raise e
	'''
	country
	'''
	@country.setter
	def country(self,country):
		try :
			if not isinstance(country,str):
				raise TypeError("country must be set to str value")
			self._country = country
		except Exception as e :
			raise e

	'''
	end_ip
	'''
	@property
	def end_ip(self):
		try:
			return self._end_ip
		except Exception as e :
			raise e
	'''
	end_ip
	'''
	@end_ip.setter
	def end_ip(self,end_ip):
		try :
			if not isinstance(end_ip,str):
				raise TypeError("end_ip must be set to str value")
			self._end_ip = end_ip
		except Exception as e :
			raise e

	'''
	start_ip
	'''
	@property
	def start_ip(self):
		try:
			return self._start_ip
		except Exception as e :
			raise e
	'''
	start_ip
	'''
	@start_ip.setter
	def start_ip(self,start_ip):
		try :
			if not isinstance(start_ip,str):
				raise TypeError("start_ip must be set to str value")
			self._start_ip = start_ip
		except Exception as e :
			raise e

	'''
	custom_region
	'''
	@property
	def custom_region(self):
		try:
			return self._custom_region
		except Exception as e :
			raise e
	'''
	custom_region
	'''
	@custom_region.setter
	def custom_region(self,custom_region):
		try :
			if not isinstance(custom_region,bool):
				raise TypeError("custom_region must be set to bool value")
			self._custom_region = custom_region
		except Exception as e :
			raise e

	'''
	region
	'''
	@property
	def region(self):
		try:
			return self._region
		except Exception as e :
			raise e
	'''
	region
	'''
	@region.setter
	def region(self,region):
		try :
			if not isinstance(region,str):
				raise TypeError("region must be set to str value")
			self._region = region
		except Exception as e :
			raise e

	'''
	Use this operation to add ip block.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ip_block_obj= ip_block()
				return cls.perform_operation_bulk_request(service,"add", resource,ip_block_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete ip block(s).
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ip_block_obj=ip_block()
					return cls.delete_bulk_request(client,resource,ip_block_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get ip block.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ip_block_obj=ip_block()
				response = ip_block_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify ip block.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ip_block_obj=ip_block()
				return cls.update_bulk_request(client,resource,ip_block_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ip_block resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ip_block_obj = ip_block()
			option_ = options()
			option_._filter=filter_
			return ip_block_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ip_block resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ip_block_obj = ip_block()
			option_ = options()
			option_._count=True
			response = ip_block_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ip_block resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ip_block_obj = ip_block()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ip_block_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ip_block_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ip_block
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ip_block_responses, response, "ip_block_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ip_block_response_array
				i=0
				error = [ip_block() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ip_block_response_array
			i=0
			ip_block_objs = [ip_block() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ip_block'):
					for props in obj._ip_block:
						result = service.payload_formatter.string_to_bulk_resource(ip_block_response,self.__class__.__name__,props)
						ip_block_objs[i] = result.ip_block
						i=i+1
			return ip_block_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ip_block,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ip_block_response(base_response):
	def __init__(self,length=1) :
		self.ip_block= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ip_block= [ ip_block() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ip_block_responses(base_response):
	def __init__(self,length=1) :
		self.ip_block_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ip_block_response_array = [ ip_block() for _ in range(length)]
