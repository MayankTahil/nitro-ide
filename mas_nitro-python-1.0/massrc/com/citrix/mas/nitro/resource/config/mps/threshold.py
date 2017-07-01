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
Configuration for Thresholds resource
'''

class threshold(base_resource):
	_tenant_name= ""
	_is_enabled= ""
	_sms_profile= ""
	_group_name= ""
	_reference_key= ""
	_name= ""
	_rule= ""
	_duration= ""
	_feature= ""
	_id= ""
	_mail_profile= ""
	_resource_type= ""
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
			return "threshold"
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
			return "thresholds"
		except Exception as e :
			raise e



	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e
	'''
	set Tenant Name
	'''
	@tenant_name.setter
	def tenant_name(self,tenant_name):
		try :
			if not isinstance(tenant_name,str):
				raise TypeError("tenant_name must be set to str value")
			self._tenant_name = tenant_name
		except Exception as e :
			raise e


	'''
	get true or false
	'''
	@property
	def is_enabled(self) :
		try:
			return self._is_enabled
		except Exception as e :
			raise e
	'''
	set true or false
	'''
	@is_enabled.setter
	def is_enabled(self,is_enabled):
		try :
			if not isinstance(is_enabled,str):
				raise TypeError("is_enabled must be set to str value")
			self._is_enabled = is_enabled
		except Exception as e :
			raise e


	'''
	get SMS Profile
	'''
	@property
	def sms_profile(self) :
		try:
			return self._sms_profile
		except Exception as e :
			raise e
	'''
	set SMS Profile
	'''
	@sms_profile.setter
	def sms_profile(self,sms_profile):
		try :
			if not isinstance(sms_profile,str):
				raise TypeError("sms_profile must be set to str value")
			self._sms_profile = sms_profile
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
	get Reference Key
	'''
	@property
	def reference_key(self) :
		try:
			return self._reference_key
		except Exception as e :
			raise e
	'''
	set Reference Key
	'''
	@reference_key.setter
	def reference_key(self,reference_key):
		try :
			if not isinstance(reference_key,str):
				raise TypeError("reference_key must be set to str value")
			self._reference_key = reference_key
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
	get Rule
	'''
	@property
	def rule(self) :
		try:
			return self._rule
		except Exception as e :
			raise e
	'''
	set Rule
	'''
	@rule.setter
	def rule(self,rule):
		try :
			if not isinstance(rule,str):
				raise TypeError("rule must be set to str value")
			self._rule = rule
		except Exception as e :
			raise e


	'''
	get duration of metric to be checked against threshold
	'''
	@property
	def duration(self) :
		try:
			return self._duration
		except Exception as e :
			raise e
	'''
	set duration of metric to be checked against threshold
	'''
	@duration.setter
	def duration(self,duration):
		try :
			if not isinstance(duration,str):
				raise TypeError("duration must be set to str value")
			self._duration = duration
		except Exception as e :
			raise e


	'''
	get feature
	'''
	@property
	def feature(self) :
		try:
			return self._feature
		except Exception as e :
			raise e
	'''
	set feature
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
	get Id is system generated key for all the Thresholds configuration 
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the Thresholds configuration 
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
	get Mail Profile
	'''
	@property
	def mail_profile(self) :
		try:
			return self._mail_profile
		except Exception as e :
			raise e
	'''
	set Mail Profile
	'''
	@mail_profile.setter
	def mail_profile(self,mail_profile):
		try :
			if not isinstance(mail_profile,str):
				raise TypeError("mail_profile must be set to str value")
			self._mail_profile = mail_profile
		except Exception as e :
			raise e


	'''
	get Resource Type
	'''
	@property
	def resource_type(self) :
		try:
			return self._resource_type
		except Exception as e :
			raise e
	'''
	set Resource Type
	'''
	@resource_type.setter
	def resource_type(self,resource_type):
		try :
			if not isinstance(resource_type,str):
				raise TypeError("resource_type must be set to str value")
			self._resource_type = resource_type
		except Exception as e :
			raise e

	'''
	add threshold configuration.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				threshold_obj= threshold()
				return cls.perform_operation_bulk_request(service,"add", resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	Delete threshold configuration.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					threshold_obj=threshold()
					return cls.delete_bulk_request(client,resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	get threshold configuration.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				threshold_obj=threshold()
				response = threshold_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	modify threshold configuraiton.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				threshold_obj=threshold()
				return cls.update_bulk_request(client,resource,threshold_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._filter=filter_
			return threshold_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the threshold resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._count=True
			response = threshold_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of threshold resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			threshold_obj = threshold()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = threshold_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(threshold_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.threshold
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(threshold_responses, response, "threshold_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.threshold_response_array
				i=0
				error = [threshold() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.threshold_response_array
			i=0
			threshold_objs = [threshold() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_threshold'):
					for props in obj._threshold:
						result = service.payload_formatter.string_to_bulk_resource(threshold_response,self.__class__.__name__,props)
						threshold_objs[i] = result.threshold
						i=i+1
			return threshold_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(threshold,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class threshold_response(base_response):
	def __init__(self,length=1) :
		self.threshold= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.threshold= [ threshold() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class threshold_responses(base_response):
	def __init__(self,length=1) :
		self.threshold_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.threshold_response_array = [ threshold() for _ in range(length)]
