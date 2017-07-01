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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_clag_node import ns_clag_node


'''
Configuration for CLAG Interface resource
'''

class ns_clag_interface(base_resource):
	_channel_id= ""
	_channel_tag_all_vlans= ""
	_channel_ha_monitoring= ""
	_lacp_channel_time= ""
	_channel_interface_list=[]
	_lacp_mode= ""
	_clip= ""
	_channel_alias= ""
	_has_foreign_interfaces= ""
	_lacp_channel_mac_address= ""
	_id= ""
	_channel_type= ""
	_mtu= ""
	_act_id= ""
	_sync_operation= ""
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
			return "ns_clag_interface"
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
			return "ns_clag_interfaces"
		except Exception as e :
			raise e



	'''
	get Channel ID if this interface represents a channel (CLA/1, CLA/2 ...)
	'''
	@property
	def channel_id(self) :
		try:
			return self._channel_id
		except Exception as e :
			raise e
	'''
	set Channel ID if this interface represents a channel (CLA/1, CLA/2 ...)
	'''
	@channel_id.setter
	def channel_id(self,channel_id):
		try :
			if not isinstance(channel_id,str):
				raise TypeError("channel_id must be set to str value")
			self._channel_id = channel_id
		except Exception as e :
			raise e


	'''
	get If true then all the member interfaces of this channel are tagged. Possible values: true and false
	'''
	@property
	def channel_tag_all_vlans(self) :
		try:
			return self._channel_tag_all_vlans
		except Exception as e :
			raise e
	'''
	set If true then all the member interfaces of this channel are tagged. Possible values: true and false
	'''
	@channel_tag_all_vlans.setter
	def channel_tag_all_vlans(self,channel_tag_all_vlans):
		try :
			if not isinstance(channel_tag_all_vlans,bool):
				raise TypeError("channel_tag_all_vlans must be set to bool value")
			self._channel_tag_all_vlans = channel_tag_all_vlans
		except Exception as e :
			raise e


	'''
	get HA-monitoring control for the channel. Possible values: true and false
	'''
	@property
	def channel_ha_monitoring(self) :
		try:
			return self._channel_ha_monitoring
		except Exception as e :
			raise e
	'''
	set HA-monitoring control for the channel. Possible values: true and false
	'''
	@channel_ha_monitoring.setter
	def channel_ha_monitoring(self,channel_ha_monitoring):
		try :
			if not isinstance(channel_ha_monitoring,bool):
				raise TypeError("channel_ha_monitoring must be set to bool value")
			self._channel_ha_monitoring = channel_ha_monitoring
		except Exception as e :
			raise e


	'''
	get LACP time. Possible values: long and short
	'''
	@property
	def lacp_channel_time(self) :
		try:
			return self._lacp_channel_time
		except Exception as e :
			raise e
	'''
	set LACP time. Possible values: long and short
	'''
	@lacp_channel_time.setter
	def lacp_channel_time(self,lacp_channel_time):
		try :
			if not isinstance(lacp_channel_time,str):
				raise TypeError("lacp_channel_time must be set to str value")
			self._lacp_channel_time = lacp_channel_time
		except Exception as e :
			raise e


	'''
	get Array of CLAG nodes that are part of this channel (10/1, 10/4)
	'''
	@property
	def channel_interface_list(self) :
		try:
			return self._channel_interface_list
		except Exception as e :
			raise e
	'''
	set Array of CLAG nodes that are part of this channel (10/1, 10/4)
	'''
	@channel_interface_list.setter
	def channel_interface_list(self,channel_interface_list) :
		try :
			if not isinstance(channel_interface_list,list):
				raise TypeError("channel_interface_list must be set to array of ns_clag_node value")
			for item in channel_interface_list :
				if not isinstance(item,ns_clag_node):
					raise TypeError("item must be set to ns_clag_node value")
			self._channel_interface_list = channel_interface_list
		except Exception as e :
			raise e


	'''
	get LACP mode can be either ACTIVE, PASSIVE, DISABLED. Applicable for channel
	'''
	@property
	def lacp_mode(self) :
		try:
			return self._lacp_mode
		except Exception as e :
			raise e


	'''
	get Cluster IPAddress
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IPAddress
	'''
	@clip.setter
	def clip(self,clip):
		try :
			if not isinstance(clip,str):
				raise TypeError("clip must be set to str value")
			self._clip = clip
		except Exception as e :
			raise e


	'''
	get Alias name for this channel
	'''
	@property
	def channel_alias(self) :
		try:
			return self._channel_alias
		except Exception as e :
			raise e
	'''
	set Alias name for this channel
	'''
	@channel_alias.setter
	def channel_alias(self,channel_alias):
		try :
			if not isinstance(channel_alias,str):
				raise TypeError("channel_alias must be set to str value")
			self._channel_alias = channel_alias
		except Exception as e :
			raise e


	'''
	get Indicates whether CLAG has interfaces from remote SDX. Possible values: true and false
	'''
	@property
	def has_foreign_interfaces(self) :
		try:
			return self._has_foreign_interfaces
		except Exception as e :
			raise e
	'''
	set Indicates whether CLAG has interfaces from remote SDX. Possible values: true and false
	'''
	@has_foreign_interfaces.setter
	def has_foreign_interfaces(self,has_foreign_interfaces):
		try :
			if not isinstance(has_foreign_interfaces,bool):
				raise TypeError("has_foreign_interfaces must be set to bool value")
			self._has_foreign_interfaces = has_foreign_interfaces
		except Exception as e :
			raise e


	'''
	get Mac address of the bond on cluster
	'''
	@property
	def lacp_channel_mac_address(self) :
		try:
			return self._lacp_channel_mac_address
		except Exception as e :
			raise e


	'''
	get Id is system generated key for CLAG
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for CLAG
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
	get Channel type to represent the CLAG type
	'''
	@property
	def channel_type(self) :
		try:
			return self._channel_type
		except Exception as e :
			raise e


	'''
	get MTU value, should be between 1500-9216
	'''
	@property
	def mtu(self) :
		try:
			return self._mtu
		except Exception as e :
			raise e
	'''
	set MTU value, should be between 1500-9216
	'''
	@mtu.setter
	def mtu(self,mtu):
		try :
			if not isinstance(mtu,int):
				raise TypeError("mtu must be set to int value")
			self._mtu = mtu
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
	Use this operation to create CLAG.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_clag_interface_obj= ns_clag_interface()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_clag_interface_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete CLAG.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_clag_interface_obj=ns_clag_interface()
					return cls.delete_bulk_request(client,resource,ns_clag_interface_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get CLAG.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_clag_interface_obj=ns_clag_interface()
				response = ns_clag_interface_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify CLAG.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_clag_interface_obj=ns_clag_interface()
				return cls.update_bulk_request(client,resource,ns_clag_interface_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_clag_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_clag_interface_obj = ns_clag_interface()
			option_ = options()
			option_._filter=filter_
			return ns_clag_interface_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_clag_interface resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_clag_interface_obj = ns_clag_interface()
			option_ = options()
			option_._count=True
			response = ns_clag_interface_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_clag_interface resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_clag_interface_obj = ns_clag_interface()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_clag_interface_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_clag_interface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_clag_interface
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_clag_interface_responses, response, "ns_clag_interface_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_clag_interface_response_array
				i=0
				error = [ns_clag_interface() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_clag_interface_response_array
			i=0
			ns_clag_interface_objs = [ns_clag_interface() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_clag_interface'):
					for props in obj._ns_clag_interface:
						result = service.payload_formatter.string_to_bulk_resource(ns_clag_interface_response,self.__class__.__name__,props)
						ns_clag_interface_objs[i] = result.ns_clag_interface
						i=i+1
			return ns_clag_interface_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_clag_interface,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_clag_interface_response(base_response):
	def __init__(self,length=1) :
		self.ns_clag_interface= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_clag_interface= [ ns_clag_interface() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_clag_interface_responses(base_response):
	def __init__(self,length=1) :
		self.ns_clag_interface_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_clag_interface_response_array = [ ns_clag_interface() for _ in range(length)]
