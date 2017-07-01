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
Configuration for Audit Log resource
'''

class audit_log(base_resource):
	_status= ""
	_port= ""
	_message= ""
	_username= ""
	_client_type= ""
	_tenant_id= ""
	_audittime= ""
	_id= ""
	_ip_address= ""
	_resource_name= ""
	_operation= ""
	_command= ""
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
			return "audit_log"
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
			return "audit_logs"
		except Exception as e :
			raise e



	'''
	get Status of this action whether accepted/rejected by system
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Client port from where operation specified for this entry was performed
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e


	'''
	get Message for this action
	'''
	@property
	def message(self) :
		try:
			return self._message
		except Exception as e :
			raise e


	'''
	get User Name, who performed operation specified for this entry
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e


	'''
	get Client Type
	'''
	@property
	def client_type(self) :
		try:
			return self._client_type
		except Exception as e :
			raise e


	'''
	get Tenant Id of the audit log
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e
	'''
	set Tenant Id of the audit log
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
	get Action Time on which operation specified for this entry was started
	'''
	@property
	def audittime(self) :
		try:
			return self._audittime
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the audit log entries
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the audit log entries
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
	get Client IP Address from where operation specified for this entry was performed
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e


	'''
	get Resource Name on which operation specified for this entry was performed
	'''
	@property
	def resource_name(self) :
		try:
			return self._resource_name
		except Exception as e :
			raise e


	'''
	get Operation Type that is performed
	'''
	@property
	def operation(self) :
		try:
			return self._operation
		except Exception as e :
			raise e


	'''
	get Command given for this action
	'''
	@property
	def command(self) :
		try:
			return self._command
		except Exception as e :
			raise e
	'''
	set Command given for this action
	'''
	@command.setter
	def command(self,command):
		try :
			if not isinstance(command,str):
				raise TypeError("command must be set to str value")
			self._command = command
		except Exception as e :
			raise e


	'''
	get Resource Type on which operation specified for this entry was performed 
	'''
	@property
	def resource_type(self) :
		try:
			return self._resource_type
		except Exception as e :
			raise e

	'''
	Use this operation to get audit log message.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				audit_log_obj=audit_log()
				response = audit_log_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of audit_log resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			audit_log_obj = audit_log()
			option_ = options()
			option_._filter=filter_
			return audit_log_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the audit_log resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			audit_log_obj = audit_log()
			option_ = options()
			option_._count=True
			response = audit_log_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of audit_log resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			audit_log_obj = audit_log()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = audit_log_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(audit_log_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.audit_log
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(audit_log_responses, response, "audit_log_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.audit_log_response_array
				i=0
				error = [audit_log() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.audit_log_response_array
			i=0
			audit_log_objs = [audit_log() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_audit_log'):
					for props in obj._audit_log:
						result = service.payload_formatter.string_to_bulk_resource(audit_log_response,self.__class__.__name__,props)
						audit_log_objs[i] = result.audit_log
						i=i+1
			return audit_log_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(audit_log,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class audit_log_response(base_response):
	def __init__(self,length=1) :
		self.audit_log= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.audit_log= [ audit_log() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class audit_log_responses(base_response):
	def __init__(self,length=1) :
		self.audit_log_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.audit_log_response_array = [ audit_log() for _ in range(length)]
