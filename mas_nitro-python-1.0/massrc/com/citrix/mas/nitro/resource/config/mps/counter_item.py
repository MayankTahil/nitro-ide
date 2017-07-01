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
Configuration for counter_item Resource resource
'''

class counter_item(base_resource):
	_parent_name= ""
	_timestamp= ""
	_value= ""
	_parent_id= ""
	_anomaly= ""
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
			return "counter_item"
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
			return "counter_items"
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
	get Timestamp of the anomalous counter
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set Timestamp of the anomalous counter
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get Value of the anomalous counter
	'''
	@property
	def value(self) :
		try:
			return self._value
		except Exception as e :
			raise e
	'''
	set Value of the anomalous counter
	'''
	@value.setter
	def value(self,value):
		try :
			if not isinstance(value,float):
				raise TypeError("value must be set to float value")
			self._value = value
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
	get If the counter item is anomalous
	'''
	@property
	def anomaly(self) :
		try:
			return self._anomaly
		except Exception as e :
			raise e
	'''
	set If the counter item is anomalous
	'''
	@anomaly.setter
	def anomaly(self,anomaly):
		try :
			if not isinstance(anomaly,bool):
				raise TypeError("anomaly must be set to bool value")
			self._anomaly = anomaly
		except Exception as e :
			raise e

	'''
	Use this operation to get the anamoly.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				counter_item_obj=counter_item()
				response = counter_item_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of counter_item resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			counter_item_obj = counter_item()
			option_ = options()
			option_._filter=filter_
			return counter_item_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the counter_item resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			counter_item_obj = counter_item()
			option_ = options()
			option_._count=True
			response = counter_item_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of counter_item resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			counter_item_obj = counter_item()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = counter_item_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(counter_item_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.counter_item
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(counter_item_responses, response, "counter_item_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.counter_item_response_array
				i=0
				error = [counter_item() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.counter_item_response_array
			i=0
			counter_item_objs = [counter_item() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_counter_item'):
					for props in obj._counter_item:
						result = service.payload_formatter.string_to_bulk_resource(counter_item_response,self.__class__.__name__,props)
						counter_item_objs[i] = result.counter_item
						i=i+1
			return counter_item_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(counter_item,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class counter_item_response(base_response):
	def __init__(self,length=1) :
		self.counter_item= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.counter_item= [ counter_item() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class counter_item_responses(base_response):
	def __init__(self,length=1) :
		self.counter_item_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.counter_item_response_array = [ counter_item() for _ in range(length)]
