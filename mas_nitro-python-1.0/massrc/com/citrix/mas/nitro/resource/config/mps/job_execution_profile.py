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
from massrc.com.citrix.mas.nitro.resource.config.mps.eventrule_variable_values import eventrule_variable_values
from massrc.com.citrix.mas.nitro.resource.config.mps.eventrule_configuration_template import eventrule_configuration_template


'''
Configuration for Job Execution Profile resource
'''

class job_execution_profile(base_resource):
	_tenant_id= ""
	_job_name= ""
	_variables=[]
	_template_info= ""
	_id= ""
	_on_error= ""
	_instance_type= ""
	_profile_name= ""
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
			return "job_execution_profile"
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
			return "job_execution_profiles"
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
	get Job Name
	'''
	@property
	def job_name(self) :
		try:
			return self._job_name
		except Exception as e :
			raise e
	'''
	set Job Name
	'''
	@job_name.setter
	def job_name(self,job_name):
		try :
			if not isinstance(job_name,str):
				raise TypeError("job_name must be set to str value")
			self._job_name = job_name
		except Exception as e :
			raise e


	'''
	get Values of Variables used in commands of the configuration template
	'''
	@property
	def variables(self) :
		try:
			return self._variables
		except Exception as e :
			raise e
	'''
	set Values of Variables used in commands of the configuration template
	'''
	@variables.setter
	def variables(self,variables) :
		try :
			if not isinstance(variables,list):
				raise TypeError("variables must be set to array of eventrule_variable_values value")
			for item in variables :
				if not isinstance(item,eventrule_variable_values):
					raise TypeError("item must be set to eventrule_variable_values value")
			self._variables = variables
		except Exception as e :
			raise e


	'''
	get Configuration Template to be executed/scheduled
	'''
	@property
	def template_info(self) :
		try:
			return self._template_info
		except Exception as e :
			raise e
	'''
	set Configuration Template to be executed/scheduled
	'''
	@template_info.setter
	def template_info(self,template_info):
		try :
			if not isinstance(template_info,eventrule_configuration_template):
				raise TypeError("template_info must be set to eventrule_configuration_template value")
			self._template_info = template_info
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the job profile.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the job profile.
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
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT|ROLLBACK
	'''
	@on_error.setter
	def on_error(self,on_error):
		try :
			if not isinstance(on_error,str):
				raise TypeError("on_error must be set to str value")
			self._on_error = on_error
		except Exception as e :
			raise e


	'''
	get Instance Type
	'''
	@property
	def instance_type(self) :
		try:
			return self._instance_type
		except Exception as e :
			raise e
	'''
	set Instance Type
	'''
	@instance_type.setter
	def instance_type(self,instance_type):
		try :
			if not isinstance(instance_type,str):
				raise TypeError("instance_type must be set to str value")
			self._instance_type = instance_type
		except Exception as e :
			raise e


	'''
	get Profile name for the job setting.
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile name for the job setting.
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e

	'''
	Use this operation to add job execution profile..
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				job_execution_profile_obj= job_execution_profile()
				return cls.perform_operation_bulk_request(service,"add", resource,job_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete job execution profile..
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					job_execution_profile_obj=job_execution_profile()
					return cls.delete_bulk_request(client,resource,job_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get job execution profile..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				job_execution_profile_obj=job_execution_profile()
				response = job_execution_profile_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify job execution profile..
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				job_execution_profile_obj=job_execution_profile()
				return cls.update_bulk_request(client,resource,job_execution_profile_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of job_execution_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			job_execution_profile_obj = job_execution_profile()
			option_ = options()
			option_._filter=filter_
			return job_execution_profile_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the job_execution_profile resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			job_execution_profile_obj = job_execution_profile()
			option_ = options()
			option_._count=True
			response = job_execution_profile_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of job_execution_profile resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			job_execution_profile_obj = job_execution_profile()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = job_execution_profile_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(job_execution_profile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.job_execution_profile
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(job_execution_profile_responses, response, "job_execution_profile_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.job_execution_profile_response_array
				i=0
				error = [job_execution_profile() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.job_execution_profile_response_array
			i=0
			job_execution_profile_objs = [job_execution_profile() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_job_execution_profile'):
					for props in obj._job_execution_profile:
						result = service.payload_formatter.string_to_bulk_resource(job_execution_profile_response,self.__class__.__name__,props)
						job_execution_profile_objs[i] = result.job_execution_profile
						i=i+1
			return job_execution_profile_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(job_execution_profile,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class job_execution_profile_response(base_response):
	def __init__(self,length=1) :
		self.job_execution_profile= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.job_execution_profile= [ job_execution_profile() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class job_execution_profile_responses(base_response):
	def __init__(self,length=1) :
		self.job_execution_profile_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.job_execution_profile_response_array = [ job_execution_profile() for _ in range(length)]
