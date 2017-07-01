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
Configuration for This table holds stat info to be persistant across reboots for appflow feature. resource
'''

class af_persistant_stat_info(base_resource):
	_propkey= ""
	_propvalue= ""
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
			return "af_persistant_stat_info"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._propkey
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
			return "af_persistant_stat_infos"
		except Exception as e :
			raise e



	'''
	get Key of the property.
	'''
	@property
	def propkey(self) :
		try:
			return self._propkey
		except Exception as e :
			raise e
	'''
	set Key of the property.
	'''
	@propkey.setter
	def propkey(self,propkey):
		try :
			if not isinstance(propkey,str):
				raise TypeError("propkey must be set to str value")
			self._propkey = propkey
		except Exception as e :
			raise e


	'''
	get Value of the property.
	'''
	@property
	def propvalue(self) :
		try:
			return self._propvalue
		except Exception as e :
			raise e
	'''
	set Value of the property.
	'''
	@propvalue.setter
	def propvalue(self,propvalue):
		try :
			if not isinstance(propvalue,str):
				raise TypeError("propvalue must be set to str value")
			self._propvalue = propvalue
		except Exception as e :
			raise e

	'''
	Use this operation to delete a property.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					af_persistant_stat_info_obj=af_persistant_stat_info()
					return cls.delete_bulk_request(client,resource,af_persistant_stat_info_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get a value for a Property based on Key..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				af_persistant_stat_info_obj=af_persistant_stat_info()
				response = af_persistant_stat_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of af_persistant_stat_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			af_persistant_stat_info_obj = af_persistant_stat_info()
			option_ = options()
			option_._filter=filter_
			return af_persistant_stat_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the af_persistant_stat_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			af_persistant_stat_info_obj = af_persistant_stat_info()
			option_ = options()
			option_._count=True
			response = af_persistant_stat_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of af_persistant_stat_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			af_persistant_stat_info_obj = af_persistant_stat_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = af_persistant_stat_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(af_persistant_stat_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.af_persistant_stat_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(af_persistant_stat_info_responses, response, "af_persistant_stat_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.af_persistant_stat_info_response_array
				i=0
				error = [af_persistant_stat_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.af_persistant_stat_info_response_array
			i=0
			af_persistant_stat_info_objs = [af_persistant_stat_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_af_persistant_stat_info'):
					for props in obj._af_persistant_stat_info:
						result = service.payload_formatter.string_to_bulk_resource(af_persistant_stat_info_response,self.__class__.__name__,props)
						af_persistant_stat_info_objs[i] = result.af_persistant_stat_info
						i=i+1
			return af_persistant_stat_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(af_persistant_stat_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class af_persistant_stat_info_response(base_response):
	def __init__(self,length=1) :
		self.af_persistant_stat_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.af_persistant_stat_info= [ af_persistant_stat_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class af_persistant_stat_info_responses(base_response):
	def __init__(self,length=1) :
		self.af_persistant_stat_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.af_persistant_stat_info_response_array = [ af_persistant_stat_info() for _ in range(length)]
