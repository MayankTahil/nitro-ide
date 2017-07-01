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
from massrc.com.citrix.mas.nitro.resource.config.mps.license_user_detail import license_user_detail


'''
Configuration for License Information resource
'''

class license_info(base_resource):
	_license_type= ""
	_user_info=[]
	_feature= ""
	_license_used= ""
	_act_id= ""
	_id= ""
	_product= ""
	_license_available= ""
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
			return "license_info"
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
			return "license_infos"
		except Exception as e :
			raise e



	'''
	get License Type [Retail, NFR, Eval, TP, System]
	'''
	@property
	def license_type(self) :
		try:
			return self._license_type
		except Exception as e :
			raise e


	'''
	get userInfo
	'''
	@property
	def user_info(self) :
		try:
			return self._user_info
		except Exception as e :
			raise e


	'''
	get Feature
	'''
	@property
	def feature(self) :
		try:
			return self._feature
		except Exception as e :
			raise e


	'''
	get Used Licenses
	'''
	@property
	def license_used(self) :
		try:
			return self._license_used
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get System generated value
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set System generated value
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
	get Product
	'''
	@property
	def product(self) :
		try:
			return self._product
		except Exception as e :
			raise e


	'''
	get Available Licenses
	'''
	@property
	def license_available(self) :
		try:
			return self._license_available
		except Exception as e :
			raise e

	'''
	Use this operation to apply new licenses files.
	'''

	'''
	Use this operation to apply new licenses files.
	'''
	@classmethod
	def apply(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"apply")
		except Exception as e :
			raise e

	'''
	Use this operation to get license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				license_info_obj=license_info()
				response = license_info_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of license_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			license_info_obj = license_info()
			option_ = options()
			option_._filter=filter_
			return license_info_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the license_info resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			license_info_obj = license_info()
			option_ = options()
			option_._count=True
			response = license_info_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of license_info resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			license_info_obj = license_info()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = license_info_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(license_info_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.license_info
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(license_info_responses, response, "license_info_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.license_info_response_array
				i=0
				error = [license_info() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.license_info_response_array
			i=0
			license_info_objs = [license_info() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_license_info'):
					for props in obj._license_info:
						result = service.payload_formatter.string_to_bulk_resource(license_info_response,self.__class__.__name__,props)
						license_info_objs[i] = result.license_info
						i=i+1
			return license_info_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(license_info,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class license_info_response(base_response):
	def __init__(self,length=1) :
		self.license_info= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.license_info= [ license_info() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class license_info_responses(base_response):
	def __init__(self,length=1) :
		self.license_info_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.license_info_response_array = [ license_info() for _ in range(length)]
