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
Configuration for NS HA Pair Configure Template resource
'''

class ns_hapair_template(base_resource):
	_configCoordinator= ""
	_nssecondary_ip_address= ""
	_backplane= ""
	_clusterid= ""
	_secondary_ip_address= ""
	_secondary_nodeid= ""
	_inc_enabled= ""
	_on_error= ""
	_primary_nodeid= ""
	_execute_sequentially= ""
	_nsprimary_ip_address= ""
	_act_id= ""
	_clip= ""
	_primary_ip_address= ""
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
			return "ns_hapair_template"
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
			return "ns_hapair_templates"
		except Exception as e :
			raise e



	'''
	get Node to be designated as Config Coordinator - primary or secondary
	'''
	@property
	def configCoordinator(self) :
		try:
			return self._configCoordinator
		except Exception as e :
			raise e
	'''
	set Node to be designated as Config Coordinator - primary or secondary
	'''
	@configCoordinator.setter
	def configCoordinator(self,configCoordinator):
		try :
			if not isinstance(configCoordinator,str):
				raise TypeError("configCoordinator must be set to str value")
			self._configCoordinator = configCoordinator
		except Exception as e :
			raise e


	'''
	get Secondary HA Node NSIP Address
	'''
	@property
	def nssecondary_ip_address(self) :
		try:
			return self._nssecondary_ip_address
		except Exception as e :
			raise e
	'''
	set Secondary HA Node NSIP Address
	'''
	@nssecondary_ip_address.setter
	def nssecondary_ip_address(self,nssecondary_ip_address):
		try :
			if not isinstance(nssecondary_ip_address,str):
				raise TypeError("nssecondary_ip_address must be set to str value")
			self._nssecondary_ip_address = nssecondary_ip_address
		except Exception as e :
			raise e


	'''
	get Backplane Interface
	'''
	@property
	def backplane(self) :
		try:
			return self._backplane
		except Exception as e :
			raise e
	'''
	set Backplane Interface
	'''
	@backplane.setter
	def backplane(self,backplane):
		try :
			if not isinstance(backplane,str):
				raise TypeError("backplane must be set to str value")
			self._backplane = backplane
		except Exception as e :
			raise e


	'''
	get Cluster Id
	'''
	@property
	def clusterid(self) :
		try:
			return self._clusterid
		except Exception as e :
			raise e
	'''
	set Cluster Id
	'''
	@clusterid.setter
	def clusterid(self,clusterid):
		try :
			if not isinstance(clusterid,int):
				raise TypeError("clusterid must be set to int value")
			self._clusterid = clusterid
		except Exception as e :
			raise e


	'''
	get Secondary HA Node IP Address
	'''
	@property
	def secondary_ip_address(self) :
		try:
			return self._secondary_ip_address
		except Exception as e :
			raise e
	'''
	set Secondary HA Node IP Address
	'''
	@secondary_ip_address.setter
	def secondary_ip_address(self,secondary_ip_address):
		try :
			if not isinstance(secondary_ip_address,str):
				raise TypeError("secondary_ip_address must be set to str value")
			self._secondary_ip_address = secondary_ip_address
		except Exception as e :
			raise e


	'''
	get Secondary Node ID
	'''
	@property
	def secondary_nodeid(self) :
		try:
			return self._secondary_nodeid
		except Exception as e :
			raise e
	'''
	set Secondary Node ID
	'''
	@secondary_nodeid.setter
	def secondary_nodeid(self,secondary_nodeid):
		try :
			if not isinstance(secondary_nodeid,int):
				raise TypeError("secondary_nodeid must be set to int value")
			self._secondary_nodeid = secondary_nodeid
		except Exception as e :
			raise e


	'''
	get Turn on INC mode on self node
	'''
	@property
	def inc_enabled(self) :
		try:
			return self._inc_enabled
		except Exception as e :
			raise e
	'''
	set Turn on INC mode on self node
	'''
	@inc_enabled.setter
	def inc_enabled(self,inc_enabled):
		try :
			if not isinstance(inc_enabled,bool):
				raise TypeError("inc_enabled must be set to bool value")
			self._inc_enabled = inc_enabled
		except Exception as e :
			raise e


	'''
	get Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
	'''
	@property
	def on_error(self) :
		try:
			return self._on_error
		except Exception as e :
			raise e
	'''
	set Behaviour on encountering error while applying configuration template on a device: CONTINUE|EXIT
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
	get Prmiary Node ID
	'''
	@property
	def primary_nodeid(self) :
		try:
			return self._primary_nodeid
		except Exception as e :
			raise e
	'''
	set Prmiary Node ID
	'''
	@primary_nodeid.setter
	def primary_nodeid(self,primary_nodeid):
		try :
			if not isinstance(primary_nodeid,int):
				raise TypeError("primary_nodeid must be set to int value")
			self._primary_nodeid = primary_nodeid
		except Exception as e :
			raise e


	'''
	get True if configuration template is to be applied to devices sequentially
	'''
	@property
	def execute_sequentially(self) :
		try:
			return self._execute_sequentially
		except Exception as e :
			raise e
	'''
	set True if configuration template is to be applied to devices sequentially
	'''
	@execute_sequentially.setter
	def execute_sequentially(self,execute_sequentially):
		try :
			if not isinstance(execute_sequentially,bool):
				raise TypeError("execute_sequentially must be set to bool value")
			self._execute_sequentially = execute_sequentially
		except Exception as e :
			raise e


	'''
	get Primary HA Node NSIP Address
	'''
	@property
	def nsprimary_ip_address(self) :
		try:
			return self._nsprimary_ip_address
		except Exception as e :
			raise e
	'''
	set Primary HA Node NSIP Address
	'''
	@nsprimary_ip_address.setter
	def nsprimary_ip_address(self,nsprimary_ip_address):
		try :
			if not isinstance(nsprimary_ip_address,str):
				raise TypeError("nsprimary_ip_address must be set to str value")
			self._nsprimary_ip_address = nsprimary_ip_address
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
	get Primary HA Node IP Address
	'''
	@property
	def primary_ip_address(self) :
		try:
			return self._primary_ip_address
		except Exception as e :
			raise e
	'''
	set Primary HA Node IP Address
	'''
	@primary_ip_address.setter
	def primary_ip_address(self,primary_ip_address):
		try :
			if not isinstance(primary_ip_address,str):
				raise TypeError("primary_ip_address must be set to str value")
			self._primary_ip_address = primary_ip_address
		except Exception as e :
			raise e

	'''
	Use this operation to get ns ha pair.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_hapair_template_obj=ns_hapair_template()
				response = ns_hapair_template_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_hapair_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_hapair_template_obj = ns_hapair_template()
			option_ = options()
			option_._filter=filter_
			return ns_hapair_template_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_hapair_template resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_hapair_template_obj = ns_hapair_template()
			option_ = options()
			option_._count=True
			response = ns_hapair_template_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_hapair_template resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_hapair_template_obj = ns_hapair_template()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_hapair_template_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_hapair_template_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_hapair_template
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_hapair_template_responses, response, "ns_hapair_template_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_hapair_template_response_array
				i=0
				error = [ns_hapair_template() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_hapair_template_response_array
			i=0
			ns_hapair_template_objs = [ns_hapair_template() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_hapair_template'):
					for props in obj._ns_hapair_template:
						result = service.payload_formatter.string_to_bulk_resource(ns_hapair_template_response,self.__class__.__name__,props)
						ns_hapair_template_objs[i] = result.ns_hapair_template
						i=i+1
			return ns_hapair_template_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_hapair_template,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_hapair_template_response(base_response):
	def __init__(self,length=1) :
		self.ns_hapair_template= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_hapair_template= [ ns_hapair_template() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_hapair_template_responses(base_response):
	def __init__(self,length=1) :
		self.ns_hapair_template_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_hapair_template_response_array = [ ns_hapair_template() for _ in range(length)]
