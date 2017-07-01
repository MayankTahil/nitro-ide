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
Configuration for Performance Poll Data resource
'''

class cbwanopt_poll_data(base_resource):
	_counter_group= ""
	_id= ""
	_device_ip_address= ""
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
			return "cbwanopt_poll_data"
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
			return "cbwanopt_poll_datas"
		except Exception as e :
			raise e



	'''
	get CounterGroup
	'''
	@property
	def counter_group(self) :
		try:
			return self._counter_group
		except Exception as e :
			raise e
	'''
	set CounterGroup
	'''
	@counter_group.setter
	def counter_group(self,counter_group):
		try :
			if not isinstance(counter_group,str):
				raise TypeError("counter_group must be set to str value")
			self._counter_group = counter_group
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
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
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get counter Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				cbwanopt_poll_data_obj=cbwanopt_poll_data()
				response = cbwanopt_poll_data_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of cbwanopt_poll_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			cbwanopt_poll_data_obj = cbwanopt_poll_data()
			option_ = options()
			option_._filter=filter_
			return cbwanopt_poll_data_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the cbwanopt_poll_data resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			cbwanopt_poll_data_obj = cbwanopt_poll_data()
			option_ = options()
			option_._count=True
			response = cbwanopt_poll_data_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of cbwanopt_poll_data resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			cbwanopt_poll_data_obj = cbwanopt_poll_data()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = cbwanopt_poll_data_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(cbwanopt_poll_data_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cbwanopt_poll_data
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(cbwanopt_poll_data_responses, response, "cbwanopt_poll_data_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.cbwanopt_poll_data_response_array
				i=0
				error = [cbwanopt_poll_data() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.cbwanopt_poll_data_response_array
			i=0
			cbwanopt_poll_data_objs = [cbwanopt_poll_data() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_cbwanopt_poll_data'):
					for props in obj._cbwanopt_poll_data:
						result = service.payload_formatter.string_to_bulk_resource(cbwanopt_poll_data_response,self.__class__.__name__,props)
						cbwanopt_poll_data_objs[i] = result.cbwanopt_poll_data
						i=i+1
			return cbwanopt_poll_data_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(cbwanopt_poll_data,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class cbwanopt_poll_data_response(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_poll_data= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.cbwanopt_poll_data= [ cbwanopt_poll_data() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class cbwanopt_poll_data_responses(base_response):
	def __init__(self,length=1) :
		self.cbwanopt_poll_data_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.cbwanopt_poll_data_response_array = [ cbwanopt_poll_data() for _ in range(length)]
