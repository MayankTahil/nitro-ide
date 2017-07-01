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
Configuration for criteria resource
'''

class criteria(base_resource):
	_parent_name= ""
	_criteria_type= ""
	_id= ""
	_parent_id= ""
	_criteria_value= ""
	_criteria_condn= ""
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
			return "criteria"
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
			return "criterias"
		except Exception as e :
			raise e



	'''
	get 
	'''
	@property
	def parent_name(self) :
		try:
			return self._parent_name
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_name.setter
	def parent_name(self,parent_name):
		try :
			if not isinstance(parent_name,str):
				raise TypeError("parent_name must be set to str value")
			self._parent_name = parent_name
		except Exception as e :
			raise e


	'''
	get applicationCriteria
	'''
	@property
	def criteria_type(self) :
		try:
			return self._criteria_type
		except Exception as e :
			raise e
	'''
	set applicationCriteria
	'''
	@criteria_type.setter
	def criteria_type(self,criteria_type):
		try :
			if not isinstance(criteria_type,str):
				raise TypeError("criteria_type must be set to str value")
			self._criteria_type = criteria_type
		except Exception as e :
			raise e


	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	get 
	'''
	@property
	def parent_id(self) :
		try:
			return self._parent_id
		except Exception as e :
			raise e
	'''
	set 
	'''
	@parent_id.setter
	def parent_id(self,parent_id):
		try :
			if not isinstance(parent_id,str):
				raise TypeError("parent_id must be set to str value")
			self._parent_id = parent_id
		except Exception as e :
			raise e


	'''
	get Criteria Value
	'''
	@property
	def criteria_value(self) :
		try:
			return self._criteria_value
		except Exception as e :
			raise e
	'''
	set Criteria Value
	'''
	@criteria_value.setter
	def criteria_value(self,criteria_value):
		try :
			if not isinstance(criteria_value,str):
				raise TypeError("criteria_value must be set to str value")
			self._criteria_value = criteria_value
		except Exception as e :
			raise e


	'''
	get Criteria condition
	'''
	@property
	def criteria_condn(self) :
		try:
			return self._criteria_condn
		except Exception as e :
			raise e
	'''
	set Criteria condition
	'''
	@criteria_condn.setter
	def criteria_condn(self,criteria_condn):
		try :
			if not isinstance(criteria_condn,str):
				raise TypeError("criteria_condn must be set to str value")
			self._criteria_condn = criteria_condn
		except Exception as e :
			raise e

	'''
	Use this operation to add criteria.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				criteria_obj= criteria()
				return cls.perform_operation_bulk_request(service,"add", resource,criteria_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete criteria.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					criteria_obj=criteria()
					return cls.delete_bulk_request(client,resource,criteria_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get criteria.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				criteria_obj=criteria()
				response = criteria_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify criteria.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				criteria_obj=criteria()
				return cls.update_bulk_request(client,resource,criteria_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of criteria resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			criteria_obj = criteria()
			option_ = options()
			option_._filter=filter_
			return criteria_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the criteria resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			criteria_obj = criteria()
			option_ = options()
			option_._count=True
			response = criteria_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of criteria resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			criteria_obj = criteria()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = criteria_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(criteria_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.criteria
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(criteria_responses, response, "criteria_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.criteria_response_array
				i=0
				error = [criteria() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.criteria_response_array
			i=0
			criteria_objs = [criteria() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_criteria'):
					for props in obj._criteria:
						result = service.payload_formatter.string_to_bulk_resource(criteria_response,self.__class__.__name__,props)
						criteria_objs[i] = result.criteria
						i=i+1
			return criteria_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(criteria,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class criteria_response(base_response):
	def __init__(self,length=1) :
		self.criteria= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.criteria= [ criteria() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class criteria_responses(base_response):
	def __init__(self,length=1) :
		self.criteria_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.criteria_response_array = [ criteria() for _ in range(length)]
