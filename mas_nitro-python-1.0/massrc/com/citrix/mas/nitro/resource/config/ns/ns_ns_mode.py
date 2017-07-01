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
Configuration for NS Mode resource
'''

class ns_ns_mode(base_resource):
	_rise_rhi= ""
	_sradv= ""
	_pmtud= ""
	_ns_ip_address= ""
	_dradv= ""
	_tcpb= ""
	_fr= ""
	_dradv6= ""
	_edge= ""
	_usnip= ""
	_bridgebpdus= ""
	_cka= ""
	_ulfd= ""
	_rise_apbr= ""
	_sradv6= ""
	_ns_ip_address_arr=[]
	_mbf= ""
	_l3= ""
	_l2= ""
	_mediaclassification= ""
	_iradv= ""
	_usip= ""
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
			return "ns_ns_mode"
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
			return "ns_ns_modes"
		except Exception as e :
			raise e



	'''
	get true, if rise_rhi feature is enabled
	'''
	@property
	def rise_rhi(self) :
		try:
			return self._rise_rhi
		except Exception as e :
			raise e
	'''
	set true, if rise_rhi feature is enabled
	'''
	@rise_rhi.setter
	def rise_rhi(self,rise_rhi):
		try :
			if not isinstance(rise_rhi,bool):
				raise TypeError("rise_rhi must be set to bool value")
			self._rise_rhi = rise_rhi
		except Exception as e :
			raise e


	'''
	get true, if sradv feature is enabled
	'''
	@property
	def sradv(self) :
		try:
			return self._sradv
		except Exception as e :
			raise e
	'''
	set true, if sradv feature is enabled
	'''
	@sradv.setter
	def sradv(self,sradv):
		try :
			if not isinstance(sradv,bool):
				raise TypeError("sradv must be set to bool value")
			self._sradv = sradv
		except Exception as e :
			raise e


	'''
	get true, if pmtud feature is enabled
	'''
	@property
	def pmtud(self) :
		try:
			return self._pmtud
		except Exception as e :
			raise e
	'''
	set true, if pmtud feature is enabled
	'''
	@pmtud.setter
	def pmtud(self,pmtud):
		try :
			if not isinstance(pmtud,bool):
				raise TypeError("pmtud must be set to bool value")
			self._pmtud = pmtud
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
	get true, if dradv feature is enabled
	'''
	@property
	def dradv(self) :
		try:
			return self._dradv
		except Exception as e :
			raise e
	'''
	set true, if dradv feature is enabled
	'''
	@dradv.setter
	def dradv(self,dradv):
		try :
			if not isinstance(dradv,bool):
				raise TypeError("dradv must be set to bool value")
			self._dradv = dradv
		except Exception as e :
			raise e


	'''
	get true, if tcpb feature is enabled
	'''
	@property
	def tcpb(self) :
		try:
			return self._tcpb
		except Exception as e :
			raise e
	'''
	set true, if tcpb feature is enabled
	'''
	@tcpb.setter
	def tcpb(self,tcpb):
		try :
			if not isinstance(tcpb,bool):
				raise TypeError("tcpb must be set to bool value")
			self._tcpb = tcpb
		except Exception as e :
			raise e


	'''
	get true, if fr feature is enabled
	'''
	@property
	def fr(self) :
		try:
			return self._fr
		except Exception as e :
			raise e
	'''
	set true, if fr feature is enabled
	'''
	@fr.setter
	def fr(self,fr):
		try :
			if not isinstance(fr,bool):
				raise TypeError("fr must be set to bool value")
			self._fr = fr
		except Exception as e :
			raise e


	'''
	get true, if dradv6 feature is enabled
	'''
	@property
	def dradv6(self) :
		try:
			return self._dradv6
		except Exception as e :
			raise e
	'''
	set true, if dradv6 feature is enabled
	'''
	@dradv6.setter
	def dradv6(self,dradv6):
		try :
			if not isinstance(dradv6,bool):
				raise TypeError("dradv6 must be set to bool value")
			self._dradv6 = dradv6
		except Exception as e :
			raise e


	'''
	get true, if edge feature is enabled
	'''
	@property
	def edge(self) :
		try:
			return self._edge
		except Exception as e :
			raise e
	'''
	set true, if edge feature is enabled
	'''
	@edge.setter
	def edge(self,edge):
		try :
			if not isinstance(edge,bool):
				raise TypeError("edge must be set to bool value")
			self._edge = edge
		except Exception as e :
			raise e


	'''
	get true, if usnip feature is enabled
	'''
	@property
	def usnip(self) :
		try:
			return self._usnip
		except Exception as e :
			raise e
	'''
	set true, if usnip feature is enabled
	'''
	@usnip.setter
	def usnip(self,usnip):
		try :
			if not isinstance(usnip,bool):
				raise TypeError("usnip must be set to bool value")
			self._usnip = usnip
		except Exception as e :
			raise e


	'''
	get true, if bridgebpdus feature is enabled
	'''
	@property
	def bridgebpdus(self) :
		try:
			return self._bridgebpdus
		except Exception as e :
			raise e
	'''
	set true, if bridgebpdus feature is enabled
	'''
	@bridgebpdus.setter
	def bridgebpdus(self,bridgebpdus):
		try :
			if not isinstance(bridgebpdus,bool):
				raise TypeError("bridgebpdus must be set to bool value")
			self._bridgebpdus = bridgebpdus
		except Exception as e :
			raise e


	'''
	get true, if cka feature is enabled
	'''
	@property
	def cka(self) :
		try:
			return self._cka
		except Exception as e :
			raise e
	'''
	set true, if cka feature is enabled
	'''
	@cka.setter
	def cka(self,cka):
		try :
			if not isinstance(cka,bool):
				raise TypeError("cka must be set to bool value")
			self._cka = cka
		except Exception as e :
			raise e


	'''
	get true, if ulfd feature is enabled
	'''
	@property
	def ulfd(self) :
		try:
			return self._ulfd
		except Exception as e :
			raise e
	'''
	set true, if ulfd feature is enabled
	'''
	@ulfd.setter
	def ulfd(self,ulfd):
		try :
			if not isinstance(ulfd,bool):
				raise TypeError("ulfd must be set to bool value")
			self._ulfd = ulfd
		except Exception as e :
			raise e


	'''
	get true, if rise_apbr feature is enabled
	'''
	@property
	def rise_apbr(self) :
		try:
			return self._rise_apbr
		except Exception as e :
			raise e
	'''
	set true, if rise_apbr feature is enabled
	'''
	@rise_apbr.setter
	def rise_apbr(self,rise_apbr):
		try :
			if not isinstance(rise_apbr,bool):
				raise TypeError("rise_apbr must be set to bool value")
			self._rise_apbr = rise_apbr
		except Exception as e :
			raise e


	'''
	get true, if sradv6 feature is enabled
	'''
	@property
	def sradv6(self) :
		try:
			return self._sradv6
		except Exception as e :
			raise e
	'''
	set true, if sradv6 feature is enabled
	'''
	@sradv6.setter
	def sradv6(self,sradv6):
		try :
			if not isinstance(sradv6,bool):
				raise TypeError("sradv6 must be set to bool value")
			self._sradv6 = sradv6
		except Exception as e :
			raise e


	'''
	get List of NS IP Addresses
	'''
	@property
	def ns_ip_address_arr(self) :
		try:
			return self._ns_ip_address_arr
		except Exception as e :
			raise e
	'''
	set List of NS IP Addresses
	'''
	@ns_ip_address_arr.setter
	def ns_ip_address_arr(self,ns_ip_address_arr) :
		try :
			if not isinstance(ns_ip_address_arr,list):
				raise TypeError("ns_ip_address_arr must be set to array of str value")
			for item in ns_ip_address_arr :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._ns_ip_address_arr = ns_ip_address_arr
		except Exception as e :
			raise e


	'''
	get true, if mbf feature is enabled
	'''
	@property
	def mbf(self) :
		try:
			return self._mbf
		except Exception as e :
			raise e
	'''
	set true, if mbf feature is enabled
	'''
	@mbf.setter
	def mbf(self,mbf):
		try :
			if not isinstance(mbf,bool):
				raise TypeError("mbf must be set to bool value")
			self._mbf = mbf
		except Exception as e :
			raise e


	'''
	get true, if l3 feature is enabled
	'''
	@property
	def l3(self) :
		try:
			return self._l3
		except Exception as e :
			raise e
	'''
	set true, if l3 feature is enabled
	'''
	@l3.setter
	def l3(self,l3):
		try :
			if not isinstance(l3,bool):
				raise TypeError("l3 must be set to bool value")
			self._l3 = l3
		except Exception as e :
			raise e


	'''
	get true, if l2 feature is enabled
	'''
	@property
	def l2(self) :
		try:
			return self._l2
		except Exception as e :
			raise e
	'''
	set true, if l2 feature is enabled
	'''
	@l2.setter
	def l2(self,l2):
		try :
			if not isinstance(l2,bool):
				raise TypeError("l2 must be set to bool value")
			self._l2 = l2
		except Exception as e :
			raise e


	'''
	get true, if mediaclassification feature is enabled
	'''
	@property
	def mediaclassification(self) :
		try:
			return self._mediaclassification
		except Exception as e :
			raise e
	'''
	set true, if mediaclassification feature is enabled
	'''
	@mediaclassification.setter
	def mediaclassification(self,mediaclassification):
		try :
			if not isinstance(mediaclassification,bool):
				raise TypeError("mediaclassification must be set to bool value")
			self._mediaclassification = mediaclassification
		except Exception as e :
			raise e


	'''
	get true, if iradv feature is enabled
	'''
	@property
	def iradv(self) :
		try:
			return self._iradv
		except Exception as e :
			raise e
	'''
	set true, if iradv feature is enabled
	'''
	@iradv.setter
	def iradv(self,iradv):
		try :
			if not isinstance(iradv,bool):
				raise TypeError("iradv must be set to bool value")
			self._iradv = iradv
		except Exception as e :
			raise e


	'''
	get true, if usip feature is enabled
	'''
	@property
	def usip(self) :
		try:
			return self._usip
		except Exception as e :
			raise e
	'''
	set true, if usip feature is enabled
	'''
	@usip.setter
	def usip(self,usip):
		try :
			if not isinstance(usip,bool):
				raise TypeError("usip must be set to bool value")
			self._usip = usip
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_ns_mode resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_ns_mode_obj = ns_ns_mode()
			option_ = options()
			option_._filter=filter_
			return ns_ns_mode_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_ns_mode resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_ns_mode_obj = ns_ns_mode()
			option_ = options()
			option_._count=True
			response = ns_ns_mode_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_ns_mode resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_ns_mode_obj = ns_ns_mode()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_ns_mode_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_ns_mode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_ns_mode
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_ns_mode_responses, response, "ns_ns_mode_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_ns_mode_response_array
				i=0
				error = [ns_ns_mode() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_ns_mode_response_array
			i=0
			ns_ns_mode_objs = [ns_ns_mode() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_ns_mode'):
					for props in obj._ns_ns_mode:
						result = service.payload_formatter.string_to_bulk_resource(ns_ns_mode_response,self.__class__.__name__,props)
						ns_ns_mode_objs[i] = result.ns_ns_mode
						i=i+1
			return ns_ns_mode_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_ns_mode,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_ns_mode_response(base_response):
	def __init__(self,length=1) :
		self.ns_ns_mode= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_ns_mode= [ ns_ns_mode() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_ns_mode_responses(base_response):
	def __init__(self,length=1) :
		self.ns_ns_mode_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_ns_mode_response_array = [ ns_ns_mode() for _ in range(length)]
