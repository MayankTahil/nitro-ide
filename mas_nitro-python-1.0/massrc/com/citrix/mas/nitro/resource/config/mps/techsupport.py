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
Configuration for Technical Support resource
'''

class techsupport(base_resource):
	_file_size= ""
	_mode= ""
	_file_last_modified= ""
	_file_location_path= ""
	_file_name= ""
	_act_id= ""
	_vpx_list_for_techsupport=[]
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
			return "techsupport"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._file_name
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
			return "techsupports"
		except Exception as e :
			raise e



	'''
	get File Size
	'''
	@property
	def file_size(self) :
		try:
			return self._file_size
		except Exception as e :
			raise e


	'''
	get Technical support Mode, Possible values Appliance | XenServer | Management Service | NetScaler Insight | Appliance_full | Instances
	'''
	@property
	def mode(self) :
		try:
			return self._mode
		except Exception as e :
			raise e
	'''
	set Technical support Mode, Possible values Appliance | XenServer | Management Service | NetScaler Insight | Appliance_full | Instances
	'''
	@mode.setter
	def mode(self,mode):
		try :
			if not isinstance(mode,str):
				raise TypeError("mode must be set to str value")
			self._mode = mode
		except Exception as e :
			raise e


	'''
	get Last Modified Time
	'''
	@property
	def file_last_modified(self) :
		try:
			return self._file_last_modified
		except Exception as e :
			raise e


	'''
	get File Location on Client for upload/download
	'''
	@property
	def file_location_path(self) :
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	set File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e


	'''
	get Technical support File Name
	'''
	@property
	def file_name(self) :
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	set Technical support File Name
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
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
	get List of VPX for which the techsupport is required (Applicable for only : ManagementServiceIncludingInstances and ApplianceIncludingInstances)
	'''
	@property
	def vpx_list_for_techsupport(self) :
		try:
			return self._vpx_list_for_techsupport
		except Exception as e :
			raise e
	'''
	set List of VPX for which the techsupport is required (Applicable for only : ManagementServiceIncludingInstances and ApplianceIncludingInstances)
	'''
	@vpx_list_for_techsupport.setter
	def vpx_list_for_techsupport(self,vpx_list_for_techsupport) :
		try :
			if not isinstance(vpx_list_for_techsupport,list):
				raise TypeError("vpx_list_for_techsupport must be set to array of str value")
			for item in vpx_list_for_techsupport :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._vpx_list_for_techsupport = vpx_list_for_techsupport
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def XenServer(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"XenServer")
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def start(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"start")
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def ManagementServiceAndXen(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"ManagementServiceAndXen")
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def ManagementServiceIncludingInstances(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"ManagementServiceIncludingInstances")
		except Exception as e :
			raise e

	'''
	Use this operation to get technical support file.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				techsupport_obj=techsupport()
				response = techsupport_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete technical support file.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					techsupport_obj=techsupport()
					return cls.delete_bulk_request(client,resource,techsupport_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def ManagementService(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"ManagementService")
		except Exception as e :
			raise e

	'''
	Use this operation to generate technical support archive.
	'''
	@classmethod
	def ApplianceIncludingInstances(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"ApplianceIncludingInstances")
		except Exception as e :
			raise e

	'''
	Use this operation to download Techsupport file.
	'''

	'''
	Use this operation to download Techsupport file.
	'''
	@classmethod
	def download(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.download_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of techsupport resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			techsupport_obj = techsupport()
			option_ = options()
			option_._filter=filter_
			return techsupport_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the techsupport resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			techsupport_obj = techsupport()
			option_ = options()
			option_._count=True
			response = techsupport_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of techsupport resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			techsupport_obj = techsupport()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = techsupport_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(techsupport_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.techsupport
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(techsupport_responses, response, "techsupport_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.techsupport_response_array
				i=0
				error = [techsupport() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.techsupport_response_array
			i=0
			techsupport_objs = [techsupport() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_techsupport'):
					for props in obj._techsupport:
						result = service.payload_formatter.string_to_bulk_resource(techsupport_response,self.__class__.__name__,props)
						techsupport_objs[i] = result.techsupport
						i=i+1
			return techsupport_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(techsupport,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class techsupport_response(base_response):
	def __init__(self,length=1) :
		self.techsupport= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.techsupport= [ techsupport() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class techsupport_responses(base_response):
	def __init__(self,length=1) :
		self.techsupport_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.techsupport_response_array = [ techsupport() for _ in range(length)]
