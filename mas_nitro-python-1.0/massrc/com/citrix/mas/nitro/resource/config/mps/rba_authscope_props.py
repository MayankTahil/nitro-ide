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
Configuration for RBA Authorized Scope Properties resource
'''

class rba_authscope_props(base_resource):
	_parent_name= ""
	_propname= ""
	_rbaoperator= ""
	_id= ""
	_parent_id= ""
	_propvalue= ""
	_propvalues=[]
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
			return "rba_authscope_props"
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
			return "rba_authscope_propss"
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
	get Prop Name
	'''
	@property
	def propname(self) :
		try:
			return self._propname
		except Exception as e :
			raise e
	'''
	set Prop Name
	'''
	@propname.setter
	def propname(self,propname):
		try :
			if not isinstance(propname,str):
				raise TypeError("propname must be set to str value")
			self._propname = propname
		except Exception as e :
			raise e


	'''
	get RBA operator
	'''
	@property
	def rbaoperator(self) :
		try:
			return self._rbaoperator
		except Exception as e :
			raise e
	'''
	set RBA operator
	'''
	@rbaoperator.setter
	def rbaoperator(self,rbaoperator):
		try :
			if not isinstance(rbaoperator,str):
				raise TypeError("rbaoperator must be set to str value")
			self._rbaoperator = rbaoperator
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the auth scope properties
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the auth scope properties
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
	get Prop Value
	'''
	@property
	def propvalue(self) :
		try:
			return self._propvalue
		except Exception as e :
			raise e
	'''
	set Prop Value
	'''
	@propvalue.setter
	def propvalue(self,propvalue):
		try :
			if not isinstance(propvalue,str):
				raise TypeError("propvalue must be set to str value")
			self._propvalue = propvalue
		except Exception as e :
			raise e

	'''
	Values for a Propname
	'''
	@property
	def propvalues(self) :
		try:
			return self._propvalues
		except Exception as e :
			raise e
	'''
	Values for a Propname
	'''
	@propvalues.setter
	def propvalues(self,propvalues) :
		try :
			if not isinstance(propvalues,list):
				raise TypeError("propvalues must be set to array of str value")
			for item in propvalues :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._propvalues = propvalues
		except Exception as e :
			raise e

	'''
	Use this operation to add RBA auth scope props.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				rba_authscope_props_obj= rba_authscope_props()
				return cls.perform_operation_bulk_request(service,"add", resource,rba_authscope_props_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete RBA auth scope props.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					rba_authscope_props_obj=rba_authscope_props()
					return cls.delete_bulk_request(client,resource,rba_authscope_props_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get RBA auth scope props.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				rba_authscope_props_obj=rba_authscope_props()
				response = rba_authscope_props_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify RBA auth scope props.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				rba_authscope_props_obj=rba_authscope_props()
				return cls.update_bulk_request(client,resource,rba_authscope_props_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of rba_authscope_props resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			rba_authscope_props_obj = rba_authscope_props()
			option_ = options()
			option_._filter=filter_
			return rba_authscope_props_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the rba_authscope_props resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			rba_authscope_props_obj = rba_authscope_props()
			option_ = options()
			option_._count=True
			response = rba_authscope_props_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of rba_authscope_props resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			rba_authscope_props_obj = rba_authscope_props()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = rba_authscope_props_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(rba_authscope_props_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rba_authscope_props
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(rba_authscope_props_responses, response, "rba_authscope_props_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.rba_authscope_props_response_array
				i=0
				error = [rba_authscope_props() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.rba_authscope_props_response_array
			i=0
			rba_authscope_props_objs = [rba_authscope_props() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_rba_authscope_props'):
					for props in obj._rba_authscope_props:
						result = service.payload_formatter.string_to_bulk_resource(rba_authscope_props_response,self.__class__.__name__,props)
						rba_authscope_props_objs[i] = result.rba_authscope_props
						i=i+1
			return rba_authscope_props_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(rba_authscope_props,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class rba_authscope_props_response(base_response):
	def __init__(self,length=1) :
		self.rba_authscope_props= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.rba_authscope_props= [ rba_authscope_props() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class rba_authscope_props_responses(base_response):
	def __init__(self,length=1) :
		self.rba_authscope_props_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.rba_authscope_props_response_array = [ rba_authscope_props() for _ in range(length)]
