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
Configuration for Current Verisons resource
'''

class version_matrix_status(base_resource):
	_status_code= ""
	_xen_hotfix= ""
	_status= ""
	_xen_version= ""
	_br_version= ""
	_svm_version= ""
	_ns_version= ""
	_xen_supplemental_pack_version= ""
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
			return "version_matrix_status"
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
			return "version_matrix_statuss"
		except Exception as e :
			raise e



	'''
	get 0 - OK, 1 - Incompatible, 2 - Manifest file Missing 3- can not perform version compatibility
	'''
	@property
	def status_code(self) :
		try:
			return self._status_code
		except Exception as e :
			raise e


	'''
	get It will return xen hotfixes name-label
	'''
	@property
	def xen_hotfix(self) :
		try:
			return self._xen_hotfix
		except Exception as e :
			raise e


	'''
	get it will return OK if there is no compatability issues, else Error Message
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get XenServer Version
	'''
	@property
	def xen_version(self) :
		try:
			return self._xen_version
		except Exception as e :
			raise e


	'''
	get Repeater Version
	'''
	@property
	def br_version(self) :
		try:
			return self._br_version
		except Exception as e :
			raise e


	'''
	get Service Management Version
	'''
	@property
	def svm_version(self) :
		try:
			return self._svm_version
		except Exception as e :
			raise e


	'''
	get NetScaler Version
	'''
	@property
	def ns_version(self) :
		try:
			return self._ns_version
		except Exception as e :
			raise e


	'''
	get Xen Supplemental Pack Version
	'''
	@property
	def xen_supplemental_pack_version(self) :
		try:
			return self._xen_supplemental_pack_version
		except Exception as e :
			raise e

	'''
	Use this operation to get currently running versions.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				version_matrix_status_obj=version_matrix_status()
				response = version_matrix_status_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of version_matrix_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			version_matrix_status_obj = version_matrix_status()
			option_ = options()
			option_._filter=filter_
			return version_matrix_status_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the version_matrix_status resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			version_matrix_status_obj = version_matrix_status()
			option_ = options()
			option_._count=True
			response = version_matrix_status_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of version_matrix_status resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			version_matrix_status_obj = version_matrix_status()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = version_matrix_status_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(version_matrix_status_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.version_matrix_status
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(version_matrix_status_responses, response, "version_matrix_status_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.version_matrix_status_response_array
				i=0
				error = [version_matrix_status() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.version_matrix_status_response_array
			i=0
			version_matrix_status_objs = [version_matrix_status() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_version_matrix_status'):
					for props in obj._version_matrix_status:
						result = service.payload_formatter.string_to_bulk_resource(version_matrix_status_response,self.__class__.__name__,props)
						version_matrix_status_objs[i] = result.version_matrix_status
						i=i+1
			return version_matrix_status_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(version_matrix_status,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class version_matrix_status_response(base_response):
	def __init__(self,length=1) :
		self.version_matrix_status= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.version_matrix_status= [ version_matrix_status() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class version_matrix_status_responses(base_response):
	def __init__(self,length=1) :
		self.version_matrix_status_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.version_matrix_status_response_array = [ version_matrix_status() for _ in range(length)]
