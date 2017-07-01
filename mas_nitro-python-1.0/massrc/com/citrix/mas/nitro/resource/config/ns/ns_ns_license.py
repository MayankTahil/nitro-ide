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
Configuration for ns_ns_license resource.
'''

class ns_ns_license(base_resource):
	_sp= ""
	_hdosp= ""
	_pq= ""
	_sc= ""
	_rise= ""
	_licensingmode= ""
	_isstandardlic= ""
	_modelid= ""
	_cloudxtenderappliance= ""
	_responder= ""
	_cr= ""
	_cloudbridge= ""
	_rewrite= ""
	_id= ""
	_isenterpriselic= ""
	_lb= ""
	_nsxn= ""
	_ic= ""
	_wionns= ""
	_gslbp= ""
	_vpath= ""
	_contentaccelerator= ""
	_cf= ""
	_f_ica_users= ""
	_cloudbridgeappliance= ""
	_rip= ""
	_gslb= ""
	_wl= ""
	_sslvpn= ""
	_push= ""
	_rdpproxy= ""
	_delta= ""
	_lsn= ""
	_cs= ""
	_isclusterkeypresent= ""
	_ospf= ""
	_ipv6pt= ""
	_feo= ""
	_isis= ""
	_bgp= ""
	_appflowica= ""
	_appqoe= ""
	_ch= ""
	_aaa= ""
	_routing= ""
	_cluster= ""
	_f_sslvpn_users= ""
	_agee= ""
	_ssl= ""
	_cmp= ""
	_appflow= ""
	_isplatinumlic= ""
	_appfw= ""
	_htmlinjection= ""
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
			return "ns_ns_license"
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
			return "ns_ns_licenses"
		except Exception as e :
			raise e



	'''
	get sp
	'''
	@property
	def sp(self) :
		try:
			return self._sp
		except Exception as e :
			raise e


	'''
	get hdosp
	'''
	@property
	def hdosp(self) :
		try:
			return self._hdosp
		except Exception as e :
			raise e


	'''
	get pq
	'''
	@property
	def pq(self) :
		try:
			return self._pq
		except Exception as e :
			raise e


	'''
	get sc
	'''
	@property
	def sc(self) :
		try:
			return self._sc
		except Exception as e :
			raise e


	'''
	get rise
	'''
	@property
	def rise(self) :
		try:
			return self._rise
		except Exception as e :
			raise e


	'''
	get license mode (Local/Pooled/CICO)
	'''
	@property
	def licensingmode(self) :
		try:
			return self._licensingmode
		except Exception as e :
			raise e


	'''
	get isstandardlic
	'''
	@property
	def isstandardlic(self) :
		try:
			return self._isstandardlic
		except Exception as e :
			raise e


	'''
	get modelid
	'''
	@property
	def modelid(self) :
		try:
			return self._modelid
		except Exception as e :
			raise e


	'''
	get cloudxtenderappliance
	'''
	@property
	def cloudxtenderappliance(self) :
		try:
			return self._cloudxtenderappliance
		except Exception as e :
			raise e


	'''
	get responder
	'''
	@property
	def responder(self) :
		try:
			return self._responder
		except Exception as e :
			raise e


	'''
	get cr
	'''
	@property
	def cr(self) :
		try:
			return self._cr
		except Exception as e :
			raise e


	'''
	get cloudbridge
	'''
	@property
	def cloudbridge(self) :
		try:
			return self._cloudbridge
		except Exception as e :
			raise e


	'''
	get rewrite
	'''
	@property
	def rewrite(self) :
		try:
			return self._rewrite
		except Exception as e :
			raise e


	'''
	get Id is NetScaler IP Address.
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is NetScaler IP Address.
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
	get isenterpriselic
	'''
	@property
	def isenterpriselic(self) :
		try:
			return self._isenterpriselic
		except Exception as e :
			raise e


	'''
	get lb
	'''
	@property
	def lb(self) :
		try:
			return self._lb
		except Exception as e :
			raise e


	'''
	get nsxn
	'''
	@property
	def nsxn(self) :
		try:
			return self._nsxn
		except Exception as e :
			raise e


	'''
	get ic
	'''
	@property
	def ic(self) :
		try:
			return self._ic
		except Exception as e :
			raise e


	'''
	get wionns
	'''
	@property
	def wionns(self) :
		try:
			return self._wionns
		except Exception as e :
			raise e


	'''
	get gdlbp
	'''
	@property
	def gslbp(self) :
		try:
			return self._gslbp
		except Exception as e :
			raise e


	'''
	get vpath
	'''
	@property
	def vpath(self) :
		try:
			return self._vpath
		except Exception as e :
			raise e


	'''
	get contentaccelerator
	'''
	@property
	def contentaccelerator(self) :
		try:
			return self._contentaccelerator
		except Exception as e :
			raise e


	'''
	get cf
	'''
	@property
	def cf(self) :
		try:
			return self._cf
		except Exception as e :
			raise e


	'''
	get f_ica_users
	'''
	@property
	def f_ica_users(self) :
		try:
			return self._f_ica_users
		except Exception as e :
			raise e
	'''
	set f_ica_users
	'''
	@f_ica_users.setter
	def f_ica_users(self,f_ica_users):
		try :
			if not isinstance(f_ica_users,int):
				raise TypeError("f_ica_users must be set to int value")
			self._f_ica_users = f_ica_users
		except Exception as e :
			raise e


	'''
	get cloudbridgeappliance
	'''
	@property
	def cloudbridgeappliance(self) :
		try:
			return self._cloudbridgeappliance
		except Exception as e :
			raise e


	'''
	get rip
	'''
	@property
	def rip(self) :
		try:
			return self._rip
		except Exception as e :
			raise e


	'''
	get gslb
	'''
	@property
	def gslb(self) :
		try:
			return self._gslb
		except Exception as e :
			raise e


	'''
	get wl
	'''
	@property
	def wl(self) :
		try:
			return self._wl
		except Exception as e :
			raise e


	'''
	get sslvpn
	'''
	@property
	def sslvpn(self) :
		try:
			return self._sslvpn
		except Exception as e :
			raise e


	'''
	get push
	'''
	@property
	def push(self) :
		try:
			return self._push
		except Exception as e :
			raise e


	'''
	get rdpproxy
	'''
	@property
	def rdpproxy(self) :
		try:
			return self._rdpproxy
		except Exception as e :
			raise e


	'''
	get delta
	'''
	@property
	def delta(self) :
		try:
			return self._delta
		except Exception as e :
			raise e


	'''
	get lsn
	'''
	@property
	def lsn(self) :
		try:
			return self._lsn
		except Exception as e :
			raise e


	'''
	get cs
	'''
	@property
	def cs(self) :
		try:
			return self._cs
		except Exception as e :
			raise e


	'''
	get Cluster Feature Key Present
	'''
	@property
	def isclusterkeypresent(self) :
		try:
			return self._isclusterkeypresent
		except Exception as e :
			raise e


	'''
	get ospf
	'''
	@property
	def ospf(self) :
		try:
			return self._ospf
		except Exception as e :
			raise e


	'''
	get ipv6pt
	'''
	@property
	def ipv6pt(self) :
		try:
			return self._ipv6pt
		except Exception as e :
			raise e


	'''
	get feo
	'''
	@property
	def feo(self) :
		try:
			return self._feo
		except Exception as e :
			raise e


	'''
	get isis
	'''
	@property
	def isis(self) :
		try:
			return self._isis
		except Exception as e :
			raise e


	'''
	get bgp
	'''
	@property
	def bgp(self) :
		try:
			return self._bgp
		except Exception as e :
			raise e


	'''
	get appflowica
	'''
	@property
	def appflowica(self) :
		try:
			return self._appflowica
		except Exception as e :
			raise e


	'''
	get appqoe
	'''
	@property
	def appqoe(self) :
		try:
			return self._appqoe
		except Exception as e :
			raise e


	'''
	get ch
	'''
	@property
	def ch(self) :
		try:
			return self._ch
		except Exception as e :
			raise e


	'''
	get aaa
	'''
	@property
	def aaa(self) :
		try:
			return self._aaa
		except Exception as e :
			raise e


	'''
	get routing
	'''
	@property
	def routing(self) :
		try:
			return self._routing
		except Exception as e :
			raise e


	'''
	get Cluster Feature
	'''
	@property
	def cluster(self) :
		try:
			return self._cluster
		except Exception as e :
			raise e


	'''
	get f_sslvpn_users
	'''
	@property
	def f_sslvpn_users(self) :
		try:
			return self._f_sslvpn_users
		except Exception as e :
			raise e
	'''
	set f_sslvpn_users
	'''
	@f_sslvpn_users.setter
	def f_sslvpn_users(self,f_sslvpn_users):
		try :
			if not isinstance(f_sslvpn_users,int):
				raise TypeError("f_sslvpn_users must be set to int value")
			self._f_sslvpn_users = f_sslvpn_users
		except Exception as e :
			raise e


	'''
	get Agee
	'''
	@property
	def agee(self) :
		try:
			return self._agee
		except Exception as e :
			raise e


	'''
	get ssl
	'''
	@property
	def ssl(self) :
		try:
			return self._ssl
		except Exception as e :
			raise e


	'''
	get cmp
	'''
	@property
	def cmp(self) :
		try:
			return self._cmp
		except Exception as e :
			raise e


	'''
	get appflow
	'''
	@property
	def appflow(self) :
		try:
			return self._appflow
		except Exception as e :
			raise e


	'''
	get isplatinumlic
	'''
	@property
	def isplatinumlic(self) :
		try:
			return self._isplatinumlic
		except Exception as e :
			raise e


	'''
	get appfw
	'''
	@property
	def appfw(self) :
		try:
			return self._appfw
		except Exception as e :
			raise e


	'''
	get htmlinjection
	'''
	@property
	def htmlinjection(self) :
		try:
			return self._htmlinjection
		except Exception as e :
			raise e

	'''
	get ns license info.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_ns_license_obj=ns_ns_license()
				response = ns_ns_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ns_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ns_license_obj = ns_ns_license()
			option_ = options()
			option_._filter=filter_
			return ns_ns_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ns_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ns_license_obj = ns_ns_license()
			option_ = options()
			option_._count=True
			response = ns_ns_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ns_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ns_license_obj = ns_ns_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ns_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ns_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ns_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ns_license_responses, response, "ns_ns_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ns_license_response_array
				i=0
				error = [ns_ns_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ns_license_response_array
			i=0
			ns_ns_license_objs = [ns_ns_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ns_license'):
					for props in obj._ns_ns_license:
						result = service.payload_formatter.string_to_bulk_resource(ns_ns_license_response,self.__class__.__name__,props)
						ns_ns_license_objs[i] = result.ns_ns_license
						i=i+1
			return ns_ns_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ns_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ns_license_response(base_response):
	def __init__(self,length=1) :
		self.ns_ns_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ns_license= [ ns_ns_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ns_license_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ns_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ns_license_response_array = [ ns_ns_license() for _ in range(length)]
