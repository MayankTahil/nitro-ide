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
Configuration for visualizer lbv server binding resource
'''

class ns_visualizer_lb_bindings(base_resource):
	_lbvserver_auditsyslogpolicy_binding=[]
	_lbvserver_appfwpolicy_binding=[]
	_lbvserver_rewritepolicy_binding=[]
	_policy_type= ""
	_lbvserver_spilloverpolicy_binding=[]
	_lbvserver_auditnslogpolicy_binding=[]
	_lbvserver_transformpolicy_binding=[]
	_lbvserver_appqoepolicy_binding=[]
	_lbvserver_filterpolicy_binding=[]
	_lbvserver_csvserver_binding=[]
	_lbvserver_feopolicy_binding=[]
	_lbvserver_appflowpolicy_binding=[]
	_ip_address= ""
	_lbvserver_authorizationpolicy_binding=[]
	_lbvserver_capolicy_binding=[]
	_name= ""
	_lbvserver_servicegroup_binding=[]
	_lbvserver_cachepolicy_binding=[]
	_port= ""
	_lbvserver_service_binding=[]
	_lbvserver_responderpolicy_binding=[]
	_type= ""
	_ipaddress= ""
	_lbvserver_tmtrafficpolicy_binding=[]
	_lbvserver_cmppolicy_binding=[]
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
			return "ns_visualizer_lb_bindings"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._name
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
			return "ns_visualizer_lb_bindingss"
		except Exception as e :
			raise e



	'''
	get Audit syslog policy binding of Lbvserver
	'''
	@property
	def lbvserver_auditsyslogpolicy_binding(self) :
		try:
			return self._lbvserver_auditsyslogpolicy_binding
		except Exception as e :
			raise e
	'''
	set Audit syslog policy binding of Lbvserver
	'''
	@lbvserver_auditsyslogpolicy_binding.setter
	def lbvserver_auditsyslogpolicy_binding(self,lbvserver_auditsyslogpolicy_binding) :
		try :
			if not isinstance(lbvserver_auditsyslogpolicy_binding,list):
				raise TypeError("lbvserver_auditsyslogpolicy_binding must be set to array of str value")
			for item in lbvserver_auditsyslogpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_auditsyslogpolicy_binding = lbvserver_auditsyslogpolicy_binding
		except Exception as e :
			raise e


	'''
	get App Flow policy binding of Lbvserver
	'''
	@property
	def lbvserver_appfwpolicy_binding(self) :
		try:
			return self._lbvserver_appfwpolicy_binding
		except Exception as e :
			raise e
	'''
	set App Flow policy binding of Lbvserver
	'''
	@lbvserver_appfwpolicy_binding.setter
	def lbvserver_appfwpolicy_binding(self,lbvserver_appfwpolicy_binding) :
		try :
			if not isinstance(lbvserver_appfwpolicy_binding,list):
				raise TypeError("lbvserver_appfwpolicy_binding must be set to array of str value")
			for item in lbvserver_appfwpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_appfwpolicy_binding = lbvserver_appfwpolicy_binding
		except Exception as e :
			raise e


	'''
	get Rewrite policy binding of Lbvserver
	'''
	@property
	def lbvserver_rewritepolicy_binding(self) :
		try:
			return self._lbvserver_rewritepolicy_binding
		except Exception as e :
			raise e
	'''
	set Rewrite policy binding of Lbvserver
	'''
	@lbvserver_rewritepolicy_binding.setter
	def lbvserver_rewritepolicy_binding(self,lbvserver_rewritepolicy_binding) :
		try :
			if not isinstance(lbvserver_rewritepolicy_binding,list):
				raise TypeError("lbvserver_rewritepolicy_binding must be set to array of str value")
			for item in lbvserver_rewritepolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_rewritepolicy_binding = lbvserver_rewritepolicy_binding
		except Exception as e :
			raise e


	'''
	get Policy Type
	'''
	@property
	def policy_type(self) :
		try:
			return self._policy_type
		except Exception as e :
			raise e
	'''
	set Policy Type
	'''
	@policy_type.setter
	def policy_type(self,policy_type):
		try :
			if not isinstance(policy_type,str):
				raise TypeError("policy_type must be set to str value")
			self._policy_type = policy_type
		except Exception as e :
			raise e


	'''
	get Spill Over policy binding of Lbvserver
	'''
	@property
	def lbvserver_spilloverpolicy_binding(self) :
		try:
			return self._lbvserver_spilloverpolicy_binding
		except Exception as e :
			raise e
	'''
	set Spill Over policy binding of Lbvserver
	'''
	@lbvserver_spilloverpolicy_binding.setter
	def lbvserver_spilloverpolicy_binding(self,lbvserver_spilloverpolicy_binding) :
		try :
			if not isinstance(lbvserver_spilloverpolicy_binding,list):
				raise TypeError("lbvserver_spilloverpolicy_binding must be set to array of str value")
			for item in lbvserver_spilloverpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_spilloverpolicy_binding = lbvserver_spilloverpolicy_binding
		except Exception as e :
			raise e


	'''
	get  Audit ns policy binding of Lbvserver
	'''
	@property
	def lbvserver_auditnslogpolicy_binding(self) :
		try:
			return self._lbvserver_auditnslogpolicy_binding
		except Exception as e :
			raise e
	'''
	set  Audit ns policy binding of Lbvserver
	'''
	@lbvserver_auditnslogpolicy_binding.setter
	def lbvserver_auditnslogpolicy_binding(self,lbvserver_auditnslogpolicy_binding) :
		try :
			if not isinstance(lbvserver_auditnslogpolicy_binding,list):
				raise TypeError("lbvserver_auditnslogpolicy_binding must be set to array of str value")
			for item in lbvserver_auditnslogpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_auditnslogpolicy_binding = lbvserver_auditnslogpolicy_binding
		except Exception as e :
			raise e


	'''
	get Transform policy binding of Lbvserver
	'''
	@property
	def lbvserver_transformpolicy_binding(self) :
		try:
			return self._lbvserver_transformpolicy_binding
		except Exception as e :
			raise e
	'''
	set Transform policy binding of Lbvserver
	'''
	@lbvserver_transformpolicy_binding.setter
	def lbvserver_transformpolicy_binding(self,lbvserver_transformpolicy_binding) :
		try :
			if not isinstance(lbvserver_transformpolicy_binding,list):
				raise TypeError("lbvserver_transformpolicy_binding must be set to array of str value")
			for item in lbvserver_transformpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_transformpolicy_binding = lbvserver_transformpolicy_binding
		except Exception as e :
			raise e


	'''
	get app qo policy binding of Lbvserver
	'''
	@property
	def lbvserver_appqoepolicy_binding(self) :
		try:
			return self._lbvserver_appqoepolicy_binding
		except Exception as e :
			raise e
	'''
	set app qo policy binding of Lbvserver
	'''
	@lbvserver_appqoepolicy_binding.setter
	def lbvserver_appqoepolicy_binding(self,lbvserver_appqoepolicy_binding) :
		try :
			if not isinstance(lbvserver_appqoepolicy_binding,list):
				raise TypeError("lbvserver_appqoepolicy_binding must be set to array of str value")
			for item in lbvserver_appqoepolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_appqoepolicy_binding = lbvserver_appqoepolicy_binding
		except Exception as e :
			raise e


	'''
	get Filter policy binding of Lbvserver
	'''
	@property
	def lbvserver_filterpolicy_binding(self) :
		try:
			return self._lbvserver_filterpolicy_binding
		except Exception as e :
			raise e
	'''
	set Filter policy binding of Lbvserver
	'''
	@lbvserver_filterpolicy_binding.setter
	def lbvserver_filterpolicy_binding(self,lbvserver_filterpolicy_binding) :
		try :
			if not isinstance(lbvserver_filterpolicy_binding,list):
				raise TypeError("lbvserver_filterpolicy_binding must be set to array of str value")
			for item in lbvserver_filterpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_filterpolicy_binding = lbvserver_filterpolicy_binding
		except Exception as e :
			raise e


	'''
	get CSV Server binding of Lbvserver
	'''
	@property
	def lbvserver_csvserver_binding(self) :
		try:
			return self._lbvserver_csvserver_binding
		except Exception as e :
			raise e
	'''
	set CSV Server binding of Lbvserver
	'''
	@lbvserver_csvserver_binding.setter
	def lbvserver_csvserver_binding(self,lbvserver_csvserver_binding) :
		try :
			if not isinstance(lbvserver_csvserver_binding,list):
				raise TypeError("lbvserver_csvserver_binding must be set to array of str value")
			for item in lbvserver_csvserver_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_csvserver_binding = lbvserver_csvserver_binding
		except Exception as e :
			raise e


	'''
	get Feo policy binding of Lbvserver
	'''
	@property
	def lbvserver_feopolicy_binding(self) :
		try:
			return self._lbvserver_feopolicy_binding
		except Exception as e :
			raise e
	'''
	set Feo policy binding of Lbvserver
	'''
	@lbvserver_feopolicy_binding.setter
	def lbvserver_feopolicy_binding(self,lbvserver_feopolicy_binding) :
		try :
			if not isinstance(lbvserver_feopolicy_binding,list):
				raise TypeError("lbvserver_feopolicy_binding must be set to array of str value")
			for item in lbvserver_feopolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_feopolicy_binding = lbvserver_feopolicy_binding
		except Exception as e :
			raise e


	'''
	get App Flow policy binding of Lbvserver
	'''
	@property
	def lbvserver_appflowpolicy_binding(self) :
		try:
			return self._lbvserver_appflowpolicy_binding
		except Exception as e :
			raise e
	'''
	set App Flow policy binding of Lbvserver
	'''
	@lbvserver_appflowpolicy_binding.setter
	def lbvserver_appflowpolicy_binding(self,lbvserver_appflowpolicy_binding) :
		try :
			if not isinstance(lbvserver_appflowpolicy_binding,list):
				raise TypeError("lbvserver_appflowpolicy_binding must be set to array of str value")
			for item in lbvserver_appflowpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_appflowpolicy_binding = lbvserver_appflowpolicy_binding
		except Exception as e :
			raise e


	'''
	get IP Address
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Authorization policy binding of Lbvserver
	'''
	@property
	def lbvserver_authorizationpolicy_binding(self) :
		try:
			return self._lbvserver_authorizationpolicy_binding
		except Exception as e :
			raise e
	'''
	set Authorization policy binding of Lbvserver
	'''
	@lbvserver_authorizationpolicy_binding.setter
	def lbvserver_authorizationpolicy_binding(self,lbvserver_authorizationpolicy_binding) :
		try :
			if not isinstance(lbvserver_authorizationpolicy_binding,list):
				raise TypeError("lbvserver_authorizationpolicy_binding must be set to array of str value")
			for item in lbvserver_authorizationpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_authorizationpolicy_binding = lbvserver_authorizationpolicy_binding
		except Exception as e :
			raise e


	'''
	get CA policy binding of Lbvserver
	'''
	@property
	def lbvserver_capolicy_binding(self) :
		try:
			return self._lbvserver_capolicy_binding
		except Exception as e :
			raise e
	'''
	set CA policy binding of Lbvserver
	'''
	@lbvserver_capolicy_binding.setter
	def lbvserver_capolicy_binding(self,lbvserver_capolicy_binding) :
		try :
			if not isinstance(lbvserver_capolicy_binding,list):
				raise TypeError("lbvserver_capolicy_binding must be set to array of str value")
			for item in lbvserver_capolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_capolicy_binding = lbvserver_capolicy_binding
		except Exception as e :
			raise e


	'''
	get Name of lbvserver
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of lbvserver
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Service group binding of Lbvserver
	'''
	@property
	def lbvserver_servicegroup_binding(self) :
		try:
			return self._lbvserver_servicegroup_binding
		except Exception as e :
			raise e
	'''
	set Service group binding of Lbvserver
	'''
	@lbvserver_servicegroup_binding.setter
	def lbvserver_servicegroup_binding(self,lbvserver_servicegroup_binding) :
		try :
			if not isinstance(lbvserver_servicegroup_binding,list):
				raise TypeError("lbvserver_servicegroup_binding must be set to array of str value")
			for item in lbvserver_servicegroup_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_servicegroup_binding = lbvserver_servicegroup_binding
		except Exception as e :
			raise e


	'''
	get Cache policy binding of Lbvserver
	'''
	@property
	def lbvserver_cachepolicy_binding(self) :
		try:
			return self._lbvserver_cachepolicy_binding
		except Exception as e :
			raise e
	'''
	set Cache policy binding of Lbvserver
	'''
	@lbvserver_cachepolicy_binding.setter
	def lbvserver_cachepolicy_binding(self,lbvserver_cachepolicy_binding) :
		try :
			if not isinstance(lbvserver_cachepolicy_binding,list):
				raise TypeError("lbvserver_cachepolicy_binding must be set to array of str value")
			for item in lbvserver_cachepolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_cachepolicy_binding = lbvserver_cachepolicy_binding
		except Exception as e :
			raise e


	'''
	get Port number for the virtual server
	'''
	@property
	def port(self) :
		try:
			return self._port
		except Exception as e :
			raise e
	'''
	set Port number for the virtual server
	'''
	@port.setter
	def port(self,port):
		try :
			if not isinstance(port,str):
				raise TypeError("port must be set to str value")
			self._port = port
		except Exception as e :
			raise e


	'''
	get Service binding of Lbvserver
	'''
	@property
	def lbvserver_service_binding(self) :
		try:
			return self._lbvserver_service_binding
		except Exception as e :
			raise e
	'''
	set Service binding of Lbvserver
	'''
	@lbvserver_service_binding.setter
	def lbvserver_service_binding(self,lbvserver_service_binding) :
		try :
			if not isinstance(lbvserver_service_binding,list):
				raise TypeError("lbvserver_service_binding must be set to array of str value")
			for item in lbvserver_service_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_service_binding = lbvserver_service_binding
		except Exception as e :
			raise e


	'''
	get Responder policy binding of Lbvserver
	'''
	@property
	def lbvserver_responderpolicy_binding(self) :
		try:
			return self._lbvserver_responderpolicy_binding
		except Exception as e :
			raise e
	'''
	set Responder policy binding of Lbvserver
	'''
	@lbvserver_responderpolicy_binding.setter
	def lbvserver_responderpolicy_binding(self,lbvserver_responderpolicy_binding) :
		try :
			if not isinstance(lbvserver_responderpolicy_binding,list):
				raise TypeError("lbvserver_responderpolicy_binding must be set to array of str value")
			for item in lbvserver_responderpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_responderpolicy_binding = lbvserver_responderpolicy_binding
		except Exception as e :
			raise e


	'''
	get type
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set type
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get IP Address of  virtual server
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set IP Address of  virtual server
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress):
		try :
			if not isinstance(ipaddress,str):
				raise TypeError("ipaddress must be set to str value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get TM Traffic policy binding of Lbvserver
	'''
	@property
	def lbvserver_tmtrafficpolicy_binding(self) :
		try:
			return self._lbvserver_tmtrafficpolicy_binding
		except Exception as e :
			raise e
	'''
	set TM Traffic policy binding of Lbvserver
	'''
	@lbvserver_tmtrafficpolicy_binding.setter
	def lbvserver_tmtrafficpolicy_binding(self,lbvserver_tmtrafficpolicy_binding) :
		try :
			if not isinstance(lbvserver_tmtrafficpolicy_binding,list):
				raise TypeError("lbvserver_tmtrafficpolicy_binding must be set to array of str value")
			for item in lbvserver_tmtrafficpolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_tmtrafficpolicy_binding = lbvserver_tmtrafficpolicy_binding
		except Exception as e :
			raise e


	'''
	get Compression policy binding of Lbvserver
	'''
	@property
	def lbvserver_cmppolicy_binding(self) :
		try:
			return self._lbvserver_cmppolicy_binding
		except Exception as e :
			raise e
	'''
	set Compression policy binding of Lbvserver
	'''
	@lbvserver_cmppolicy_binding.setter
	def lbvserver_cmppolicy_binding(self,lbvserver_cmppolicy_binding) :
		try :
			if not isinstance(lbvserver_cmppolicy_binding,list):
				raise TypeError("lbvserver_cmppolicy_binding must be set to array of str value")
			for item in lbvserver_cmppolicy_binding :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._lbvserver_cmppolicy_binding = lbvserver_cmppolicy_binding
		except Exception as e :
			raise e

	'''
	Use this operation to get lbvserver.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_visualizer_lb_bindings_obj=ns_visualizer_lb_bindings()
				response = ns_visualizer_lb_bindings_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_visualizer_lb_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_visualizer_lb_bindings_obj = ns_visualizer_lb_bindings()
			option_ = options()
			option_._filter=filter_
			return ns_visualizer_lb_bindings_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_visualizer_lb_bindings resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_visualizer_lb_bindings_obj = ns_visualizer_lb_bindings()
			option_ = options()
			option_._count=True
			response = ns_visualizer_lb_bindings_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_visualizer_lb_bindings resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_visualizer_lb_bindings_obj = ns_visualizer_lb_bindings()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_visualizer_lb_bindings_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_visualizer_lb_bindings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_visualizer_lb_bindings
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_visualizer_lb_bindings_responses, response, "ns_visualizer_lb_bindings_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_visualizer_lb_bindings_response_array
				i=0
				error = [ns_visualizer_lb_bindings() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_visualizer_lb_bindings_response_array
			i=0
			ns_visualizer_lb_bindings_objs = [ns_visualizer_lb_bindings() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_visualizer_lb_bindings'):
					for props in obj._ns_visualizer_lb_bindings:
						result = service.payload_formatter.string_to_bulk_resource(ns_visualizer_lb_bindings_response,self.__class__.__name__,props)
						ns_visualizer_lb_bindings_objs[i] = result.ns_visualizer_lb_bindings
						i=i+1
			return ns_visualizer_lb_bindings_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_visualizer_lb_bindings,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_visualizer_lb_bindings_response(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_lb_bindings= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_visualizer_lb_bindings= [ ns_visualizer_lb_bindings() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_visualizer_lb_bindings_responses(base_response):
	def __init__(self,length=1) :
		self.ns_visualizer_lb_bindings_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_visualizer_lb_bindings_response_array = [ ns_visualizer_lb_bindings() for _ in range(length)]
