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
from massrc.com.citrix.mas.nitro.resource.config.mps.criteria import criteria
from massrc.com.citrix.mas.nitro.resource.config.mps.authorized_scope_app import authorized_scope_app


'''
Configuration for Applications Managed by Management System resource
'''

class application(base_resource):
	_throughput_avg= ""
	_tenant_name= ""
	_app_category= ""
	_curclntconnections= ""
	_name= ""
	_cursrvrconnections= ""
	_user_name= ""
	_tenant_id= ""
	_application_class= ""
	_application_managed= ""
	_id= ""
	_family= ""
	_app_criteria=[]
	_app_components=[]
	_no_of_svcgrp= ""
	_no_of_haproxy_be= ""
	_no_of_auth= ""
	_no_of_gslb= ""
	_no_of_gslbsvc= ""
	_no_of_cr= ""
	_no_of_cs= ""
	_no_of_svr= ""
	_no_of_vpn= ""
	_no_of_lb= ""
	_application_ids=[]
	_no_of_haproxy_fe= ""
	_no_of_svc= ""
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
			return "application"
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
			return "applications"
		except Exception as e :
			raise e



	'''
	get Sum of throughput across all vips of the app
	'''
	@property
	def throughput_avg(self) :
		try:
			return self._throughput_avg
		except Exception as e :
			raise e
	'''
	set Sum of throughput across all vips of the app
	'''
	@throughput_avg.setter
	def throughput_avg(self,throughput_avg):
		try :
			if not isinstance(throughput_avg,float):
				raise TypeError("throughput_avg must be set to float value")
			self._throughput_avg = throughput_avg
		except Exception as e :
			raise e


	'''
	get Tenant Name
	'''
	@property
	def tenant_name(self) :
		try:
			return self._tenant_name
		except Exception as e :
			raise e


	'''
	get Application Category
	'''
	@property
	def app_category(self) :
		try:
			return self._app_category
		except Exception as e :
			raise e
	'''
	set Application Category
	'''
	@app_category.setter
	def app_category(self,app_category):
		try :
			if not isinstance(app_category,str):
				raise TypeError("app_category must be set to str value")
			self._app_category = app_category
		except Exception as e :
			raise e


	'''
	get curclntconnections Value across all vips of the app
	'''
	@property
	def curclntconnections(self) :
		try:
			return self._curclntconnections
		except Exception as e :
			raise e
	'''
	set curclntconnections Value across all vips of the app
	'''
	@curclntconnections.setter
	def curclntconnections(self,curclntconnections):
		try :
			if not isinstance(curclntconnections,float):
				raise TypeError("curclntconnections must be set to float value")
			self._curclntconnections = curclntconnections
		except Exception as e :
			raise e


	'''
	get Application Name
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Application Name
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
	get cursrvrconnections Value across all vips of the app
	'''
	@property
	def cursrvrconnections(self) :
		try:
			return self._cursrvrconnections
		except Exception as e :
			raise e
	'''
	set cursrvrconnections Value across all vips of the app
	'''
	@cursrvrconnections.setter
	def cursrvrconnections(self,cursrvrconnections):
		try :
			if not isinstance(cursrvrconnections,float):
				raise TypeError("cursrvrconnections must be set to float value")
			self._cursrvrconnections = cursrvrconnections
		except Exception as e :
			raise e


	'''
	get User Name
	'''
	@property
	def user_name(self) :
		try:
			return self._user_name
		except Exception as e :
			raise e


	'''
	get Tenant Id
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Application class
	'''
	@property
	def application_class(self) :
		try:
			return self._application_class
		except Exception as e :
			raise e


	'''
	get Managed field
	'''
	@property
	def application_managed(self) :
		try:
			return self._application_managed
		except Exception as e :
			raise e
	'''
	set Managed field
	'''
	@application_managed.setter
	def application_managed(self,application_managed):
		try :
			if not isinstance(application_managed,bool):
				raise TypeError("application_managed must be set to bool value")
			self._application_managed = application_managed
		except Exception as e :
			raise e


	'''
	get Id is system generated key.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key.
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
	get Application Family
	'''
	@property
	def family(self) :
		try:
			return self._family
		except Exception as e :
			raise e
	'''
	set Application Family
	'''
	@family.setter
	def family(self,family):
		try :
			if not isinstance(family,str):
				raise TypeError("family must be set to str value")
			self._family = family
		except Exception as e :
			raise e


	'''
	get Application criteria
	'''
	@property
	def app_criteria(self) :
		try:
			return self._app_criteria
		except Exception as e :
			raise e
	'''
	set Application criteria
	'''
	@app_criteria.setter
	def app_criteria(self,app_criteria) :
		try :
			if not isinstance(app_criteria,list):
				raise TypeError("app_criteria must be set to array of criteria value")
			for item in app_criteria :
				if not isinstance(item,criteria):
					raise TypeError("item must be set to criteria value")
			self._app_criteria = app_criteria
		except Exception as e :
			raise e


	'''
	get Application components
	'''
	@property
	def app_components(self) :
		try:
			return self._app_components
		except Exception as e :
			raise e
	'''
	set Application components
	'''
	@app_components.setter
	def app_components(self,app_components) :
		try :
			if not isinstance(app_components,list):
				raise TypeError("app_components must be set to array of authorized_scope_app value")
			for item in app_components :
				if not isinstance(item,authorized_scope_app):
					raise TypeError("item must be set to authorized_scope_app value")
			self._app_components = app_components
		except Exception as e :
			raise e

	'''
	Number of Service Groups
	'''
	@property
	def no_of_svcgrp(self):
		try:
			return self._no_of_svcgrp
		except Exception as e :
			raise e
	'''
	Number of Service Groups
	'''
	@no_of_svcgrp.setter
	def no_of_svcgrp(self,no_of_svcgrp):
		try :
			if not isinstance(no_of_svcgrp,str):
				raise TypeError("no_of_svcgrp must be set to str value")
			self._no_of_svcgrp = no_of_svcgrp
		except Exception as e :
			raise e

	'''
	Number of Banckends
	'''
	@property
	def no_of_haproxy_be(self):
		try:
			return self._no_of_haproxy_be
		except Exception as e :
			raise e
	'''
	Number of Banckends
	'''
	@no_of_haproxy_be.setter
	def no_of_haproxy_be(self,no_of_haproxy_be):
		try :
			if not isinstance(no_of_haproxy_be,str):
				raise TypeError("no_of_haproxy_be must be set to str value")
			self._no_of_haproxy_be = no_of_haproxy_be
		except Exception as e :
			raise e

	'''
	Number of AUTH VIPs
	'''
	@property
	def no_of_auth(self):
		try:
			return self._no_of_auth
		except Exception as e :
			raise e
	'''
	Number of AUTH VIPs
	'''
	@no_of_auth.setter
	def no_of_auth(self,no_of_auth):
		try :
			if not isinstance(no_of_auth,str):
				raise TypeError("no_of_auth must be set to str value")
			self._no_of_auth = no_of_auth
		except Exception as e :
			raise e

	'''
	Number of GSLB VIPs
	'''
	@property
	def no_of_gslb(self):
		try:
			return self._no_of_gslb
		except Exception as e :
			raise e
	'''
	Number of GSLB VIPs
	'''
	@no_of_gslb.setter
	def no_of_gslb(self,no_of_gslb):
		try :
			if not isinstance(no_of_gslb,str):
				raise TypeError("no_of_gslb must be set to str value")
			self._no_of_gslb = no_of_gslb
		except Exception as e :
			raise e

	'''
	Number of LB VIPs
	'''
	@property
	def no_of_gslbsvc(self):
		try:
			return self._no_of_gslbsvc
		except Exception as e :
			raise e
	'''
	Number of LB VIPs
	'''
	@no_of_gslbsvc.setter
	def no_of_gslbsvc(self,no_of_gslbsvc):
		try :
			if not isinstance(no_of_gslbsvc,str):
				raise TypeError("no_of_gslbsvc must be set to str value")
			self._no_of_gslbsvc = no_of_gslbsvc
		except Exception as e :
			raise e

	'''
	Number of CR VIPs
	'''
	@property
	def no_of_cr(self):
		try:
			return self._no_of_cr
		except Exception as e :
			raise e
	'''
	Number of CR VIPs
	'''
	@no_of_cr.setter
	def no_of_cr(self,no_of_cr):
		try :
			if not isinstance(no_of_cr,str):
				raise TypeError("no_of_cr must be set to str value")
			self._no_of_cr = no_of_cr
		except Exception as e :
			raise e

	'''
	Number of CS VIPs
	'''
	@property
	def no_of_cs(self):
		try:
			return self._no_of_cs
		except Exception as e :
			raise e
	'''
	Number of CS VIPs
	'''
	@no_of_cs.setter
	def no_of_cs(self,no_of_cs):
		try :
			if not isinstance(no_of_cs,str):
				raise TypeError("no_of_cs must be set to str value")
			self._no_of_cs = no_of_cs
		except Exception as e :
			raise e

	'''
	Number of Servers
	'''
	@property
	def no_of_svr(self):
		try:
			return self._no_of_svr
		except Exception as e :
			raise e
	'''
	Number of Servers
	'''
	@no_of_svr.setter
	def no_of_svr(self,no_of_svr):
		try :
			if not isinstance(no_of_svr,str):
				raise TypeError("no_of_svr must be set to str value")
			self._no_of_svr = no_of_svr
		except Exception as e :
			raise e

	'''
	Number of VPN VIPs
	'''
	@property
	def no_of_vpn(self):
		try:
			return self._no_of_vpn
		except Exception as e :
			raise e
	'''
	Number of VPN VIPs
	'''
	@no_of_vpn.setter
	def no_of_vpn(self,no_of_vpn):
		try :
			if not isinstance(no_of_vpn,str):
				raise TypeError("no_of_vpn must be set to str value")
			self._no_of_vpn = no_of_vpn
		except Exception as e :
			raise e

	'''
	Number of LB VIPs
	'''
	@property
	def no_of_lb(self):
		try:
			return self._no_of_lb
		except Exception as e :
			raise e
	'''
	Number of LB VIPs
	'''
	@no_of_lb.setter
	def no_of_lb(self,no_of_lb):
		try :
			if not isinstance(no_of_lb,str):
				raise TypeError("no_of_lb must be set to str value")
			self._no_of_lb = no_of_lb
		except Exception as e :
			raise e

	'''
	Application IDs that are part of this application
	'''
	@property
	def application_ids(self) :
		try:
			return self._application_ids
		except Exception as e :
			raise e
	'''
	Application IDs that are part of this application
	'''
	@application_ids.setter
	def application_ids(self,application_ids) :
		try :
			if not isinstance(application_ids,list):
				raise TypeError("application_ids must be set to array of str value")
			for item in application_ids :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._application_ids = application_ids
		except Exception as e :
			raise e

	'''
	Number of Frontends
	'''
	@property
	def no_of_haproxy_fe(self):
		try:
			return self._no_of_haproxy_fe
		except Exception as e :
			raise e
	'''
	Number of Frontends
	'''
	@no_of_haproxy_fe.setter
	def no_of_haproxy_fe(self,no_of_haproxy_fe):
		try :
			if not isinstance(no_of_haproxy_fe,str):
				raise TypeError("no_of_haproxy_fe must be set to str value")
			self._no_of_haproxy_fe = no_of_haproxy_fe
		except Exception as e :
			raise e

	'''
	Number of Services
	'''
	@property
	def no_of_svc(self):
		try:
			return self._no_of_svc
		except Exception as e :
			raise e
	'''
	Number of Services
	'''
	@no_of_svc.setter
	def no_of_svc(self,no_of_svc):
		try :
			if not isinstance(no_of_svc,str):
				raise TypeError("no_of_svc must be set to str value")
			self._no_of_svc = no_of_svc
		except Exception as e :
			raise e

	'''
	Use this operation to add application.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				application_obj= application()
				return cls.perform_operation_bulk_request(service,"add", resource,application_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to delete application.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					application_obj=application()
					return cls.delete_bulk_request(client,resource,application_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get application.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				application_obj=application()
				response = application_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify application.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				application_obj=application()
				return cls.update_bulk_request(client,resource,application_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			application_obj = application()
			option_ = options()
			option_._filter=filter_
			return application_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the application resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			application_obj = application()
			option_ = options()
			option_._count=True
			response = application_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of application resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			application_obj = application()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = application_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(application_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.application
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(application_responses, response, "application_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.application_response_array
				i=0
				error = [application() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.application_response_array
			i=0
			application_objs = [application() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_application'):
					for props in obj._application:
						result = service.payload_formatter.string_to_bulk_resource(application_response,self.__class__.__name__,props)
						application_objs[i] = result.application
						i=i+1
			return application_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(application,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class application_response(base_response):
	def __init__(self,length=1) :
		self.application= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.application= [ application() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class application_responses(base_response):
	def __init__(self,length=1) :
		self.application_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.application_response_array = [ application() for _ in range(length)]
