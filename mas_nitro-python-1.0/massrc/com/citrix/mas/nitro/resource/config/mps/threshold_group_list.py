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
Configuration for Group List e.g. HDX, WEB, WAN resource
'''

class threshold_group_list(base_resource):
	_feature= ""
	_group_name= ""
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
			return "threshold_group_list"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "threshold_group_lists"
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
	set Feature
	'''
	@feature.setter
	def feature(self,feature):
		try :
			if not isinstance(feature,str):
				raise TypeError("feature must be set to str value")
			self._feature = feature
		except Exception as e :
			raise e


	'''
	get Group Name
	'''
	@property
	def group_name(self) :
		try:
			return self._group_name
		except Exception as e :
			raise e
	'''
	set Group Name
	'''
	@group_name.setter
	def group_name(self,group_name):
		try :
			if not isinstance(group_name,str):
				raise TypeError("group_name must be set to str value")
			self._group_name = group_name
		except Exception as e :
			raise e

	'''
	get group list based on deployment.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				threshold_group_list_obj=threshold_group_list()
				response = threshold_group_list_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of threshold_group_list resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			threshold_group_list_obj = threshold_group_list()
			option_ = options()
			option_._filter=filter_
			return threshold_group_list_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the threshold_group_list resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			threshold_group_list_obj = threshold_group_list()
			option_ = options()
			option_._count=True
			response = threshold_group_list_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of threshold_group_list resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			threshold_group_list_obj = threshold_group_list()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = threshold_group_list_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(threshold_group_list_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.threshold_group_list
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_group_list_responses, response, "threshold_group_list_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.threshold_group_list_response_array
				i=0
				error = [threshold_group_list() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.threshold_group_list_response_array
			i=0
			threshold_group_list_objs = [threshold_group_list() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_threshold_group_list'):
					for props in obj._threshold_group_list:
						result = service.payload_formatter.string_to_bulk_resource(threshold_group_list_response,self.__class__.__name__,props)
						threshold_group_list_objs[i] = result.threshold_group_list
						i=i+1
			return threshold_group_list_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(threshold_group_list,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class threshold_group_list_response(base_response):
	def __init__(self,length=1) :
		self.threshold_group_list= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.threshold_group_list= [ threshold_group_list() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class threshold_group_list_responses(base_response):
	def __init__(self,length=1) :
		self.threshold_group_list_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.threshold_group_list_response_array = [ threshold_group_list() for _ in range(length)]
