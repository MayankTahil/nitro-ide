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
from massrc.com.citrix.mas.nitro.resource.config.mps.rba_module_client_data import rba_module_client_data


'''
Configuration for RBA Client Data resource
'''

class rba_client_data(base_resource):
	_modules=[]
	_child_node= ""
	_serial_id= ""
	_name= ""
	_id= ""
	_ui_component= ""
	_display_name= ""
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
			return "rba_client_data"
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
			return "rba_client_datas"
		except Exception as e :
			raise e



	'''
	get RBA module client data
	'''
	@property
	def modules(self) :
		try:
			return self._modules
		except Exception as e :
			raise e
	'''
	set RBA module client data
	'''
	@modules.setter
	def modules(self,modules) :
		try :
			if not isinstance(modules,list):
				raise TypeError("modules must be set to array of rba_module_client_data value")
			for item in modules :
				if not isinstance(item,rba_module_client_data):
					raise TypeError("item must be set to rba_module_client_data value")
			self._modules = modules
		except Exception as e :
			raise e


	'''
	get This property is for internal use
	'''
	@property
	def child_node(self) :
		try:
			return self._child_node
		except Exception as e :
			raise e


	'''
	get Sequence number
	'''
	@property
	def serial_id(self) :
		try:
			return self._serial_id
		except Exception as e :
			raise e
	'''
	set Sequence number
	'''
	@serial_id.setter
	def serial_id(self,serial_id):
		try :
			if not isinstance(serial_id,int):
				raise TypeError("serial_id must be set to int value")
			self._serial_id = serial_id
		except Exception as e :
			raise e


	'''
	get parent module name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the system policys
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the system policys
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
	get if its UI component
	'''
	@property
	def ui_component(self) :
		try:
			return self._ui_component
		except Exception as e :
			raise e


	'''
	get parent module display name
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e

	'''
	Use this operation to add RBA client data.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				rba_client_data_obj= rba_client_data()
				return cls.perform_operation_bulk_request(service,"add", resource,rba_client_data_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete RBA client data.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					rba_client_data_obj=rba_client_data()
					return cls.delete_bulk_request(client,resource,rba_client_data_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get RBA client data.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				rba_client_data_obj=rba_client_data()
				response = rba_client_data_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of rba_client_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			rba_client_data_obj = rba_client_data()
			option_ = options()
			option_._filter=filter_
			return rba_client_data_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the rba_client_data resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			rba_client_data_obj = rba_client_data()
			option_ = options()
			option_._count=True
			response = rba_client_data_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of rba_client_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			rba_client_data_obj = rba_client_data()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = rba_client_data_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(rba_client_data_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_client_data
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_client_data_responses, response, "rba_client_data_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_client_data_response_array
				i=0
				error = [rba_client_data() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_client_data_response_array
			i=0
			rba_client_data_objs = [rba_client_data() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_client_data'):
					for props in obj._rba_client_data:
						result = service.payload_formatter.string_to_bulk_resource(rba_client_data_response,self.__class__.__name__,props)
						rba_client_data_objs[i] = result.rba_client_data
						i=i+1
			return rba_client_data_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_client_data,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_client_data_response(base_response):
	def __init__(self,length=1) :
		self.rba_client_data= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_client_data= [ rba_client_data() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_client_data_responses(base_response):
	def __init__(self,length=1) :
		self.rba_client_data_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_client_data_response_array = [ rba_client_data() for _ in range(length)]
