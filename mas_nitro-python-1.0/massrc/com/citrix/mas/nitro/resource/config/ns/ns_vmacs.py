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
Configuration for vmacs for shared vlans resource
'''

class ns_vmacs(base_resource):
	_vmacs= ""
	_ns_ip_address= ""
	_increment_by= ""
	_generation_method= ""
	_vmac_count= ""
	_act_id= ""
	_sync_operation= ""
	_base_vmac= ""
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
			return "ns_vmacs"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._ns_ip_address
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
			return "ns_vmacss"
		except Exception as e :
			raise e



	'''
	get Comma Seperated VMac list
	'''
	@property
	def vmacs(self) :
		try:
			return self._vmacs
		except Exception as e :
			raise e
	'''
	set Comma Seperated VMac list
	'''
	@vmacs.setter
	def vmacs(self,vmacs):
		try :
			if not isinstance(vmacs,str):
				raise TypeError("vmacs must be set to str value")
			self._vmacs = vmacs
		except Exception as e :
			raise e


	'''
	get NetScaler IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NetScaler IP Address
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e

	'''
	increment by
	'''
	@property
	def increment_by(self):
		try:
			return self._increment_by
		except Exception as e :
			raise e
	'''
	increment by
	'''
	@increment_by.setter
	def increment_by(self,increment_by):
		try :
			if not isinstance(increment_by,int):
				raise TypeError("increment_by must be set to int value")
			self._increment_by = increment_by
		except Exception as e :
			raise e

	'''
	(MANUAL, BASE or RANDOM)
	'''
	@property
	def generation_method(self):
		try:
			return self._generation_method
		except Exception as e :
			raise e
	'''
	(MANUAL, BASE or RANDOM)
	'''
	@generation_method.setter
	def generation_method(self,generation_method):
		try :
			if not isinstance(generation_method,str):
				raise TypeError("generation_method must be set to str value")
			self._generation_method = generation_method
		except Exception as e :
			raise e

	'''
	increment by
	'''
	@property
	def vmac_count(self):
		try:
			return self._vmac_count
		except Exception as e :
			raise e
	'''
	increment by
	'''
	@vmac_count.setter
	def vmac_count(self,vmac_count):
		try :
			if not isinstance(vmac_count,int):
				raise TypeError("vmac_count must be set to int value")
			self._vmac_count = vmac_count
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	sync operation
	'''
	@property
	def sync_operation(self):
		try:
			return self._sync_operation
		except Exception as e :
			raise e
	'''
	sync operation
	'''
	@sync_operation.setter
	def sync_operation(self,sync_operation):
		try :
			if not isinstance(sync_operation,bool):
				raise TypeError("sync_operation must be set to bool value")
			self._sync_operation = sync_operation
		except Exception as e :
			raise e

	'''
	Base VMac Address
	'''
	@property
	def base_vmac(self):
		try:
			return self._base_vmac
		except Exception as e :
			raise e
	'''
	Base VMac Address
	'''
	@base_vmac.setter
	def base_vmac(self,base_vmac):
		try :
			if not isinstance(base_vmac,str):
				raise TypeError("base_vmac must be set to str value")
			self._base_vmac = base_vmac
		except Exception as e :
			raise e

	'''
	Use this operation to generate and add vmacs to a specific NS.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_vmacs_obj= ns_vmacs()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_vmacs_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to reset interface settings.
	'''
	@classmethod
	def remove(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"remove")
			else : 
				ns_vmacs_obj= ns_vmacs()
				return cls.perform_operation_bulk_request(service,"remove", resource,ns_vmacs_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to list vmacs generated for all ns or a specific NS.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_vmacs_obj=ns_vmacs()
				response = ns_vmacs_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_vmacs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_vmacs_obj = ns_vmacs()
			option_ = options()
			option_._filter=filter_
			return ns_vmacs_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_vmacs resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_vmacs_obj = ns_vmacs()
			option_ = options()
			option_._count=True
			response = ns_vmacs_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_vmacs resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_vmacs_obj = ns_vmacs()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_vmacs_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_vmacs_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_vmacs
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_vmacs_responses, response, "ns_vmacs_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_vmacs_response_array
				i=0
				error = [ns_vmacs() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_vmacs_response_array
			i=0
			ns_vmacs_objs = [ns_vmacs() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_vmacs'):
					for props in obj._ns_vmacs:
						result = service.payload_formatter.string_to_bulk_resource(ns_vmacs_response,self.__class__.__name__,props)
						ns_vmacs_objs[i] = result.ns_vmacs
						i=i+1
			return ns_vmacs_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_vmacs,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_vmacs_response(base_response):
	def __init__(self,length=1) :
		self.ns_vmacs= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_vmacs= [ ns_vmacs() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_vmacs_responses(base_response):
	def __init__(self,length=1) :
		self.ns_vmacs_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_vmacs_response_array = [ ns_vmacs() for _ in range(length)]
