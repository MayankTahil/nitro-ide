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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_lbvserver_diagnostic import ns_lbvserver_diagnostic
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_nonlbvserver_diagnostic import ns_nonlbvserver_diagnostic
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_nonlbvserver_diagnostic import ns_nonlbvserver_diagnostic
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_nonlbvserver_diagnostic import ns_nonlbvserver_diagnostic


'''
Configuration for Insight Diagnostic resource
'''

class ns_insight_diagnostic(base_resource):
	_httpreferer= ""
	_templaterefresh= ""
	_securityinsightrecordinterval= ""
	_hostname= ""
	_ns_ip_address= ""
	_httpsetcookie= ""
	_httpvia= ""
	_lbvserver=[]
	_httpdomain= ""
	_httpsetcookie2= ""
	_vpnvserver=[]
	_flowrecordinterval= ""
	_httpauthorization= ""
	_skipcacheredirectionhttptransaction= ""
	_aaausername= ""
	_udppmtu= ""
	_clienttrafficonly= ""
	_securityinsighttraffic= ""
	_httpcontenttype= ""
	_crvserver=[]
	_csvserver=[]
	_httpmethod= ""
	_httplocation= ""
	_is_appflow_enabled= ""
	_identifiersessionname= ""
	_connectionchaining= ""
	_httpxforwardedfor= ""
	_appnamerefresh= ""
	_observationdomainname= ""
	_identifiername= ""
	_httpcookie= ""
	_httpurl= ""
	_httpuseragent= ""
	_httphost= ""
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
			return "ns_insight_diagnostic"
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
			return "ns_insight_diagnostics"
		except Exception as e :
			raise e



	'''
	get  HTTP referer logging.
	'''
	@property
	def httpreferer(self) :
		try:
			return self._httpreferer
		except Exception as e :
			raise e
	'''
	set  HTTP referer logging.
	'''
	@httpreferer.setter
	def httpreferer(self,httpreferer):
		try :
			if not isinstance(httpreferer,str):
				raise TypeError("httpreferer must be set to str value")
			self._httpreferer = httpreferer
		except Exception as e :
			raise e


	'''
	get IPFIX template refresh interval.
	'''
	@property
	def templaterefresh(self) :
		try:
			return self._templaterefresh
		except Exception as e :
			raise e
	'''
	set IPFIX template refresh interval.
	'''
	@templaterefresh.setter
	def templaterefresh(self,templaterefresh):
		try :
			if not isinstance(templaterefresh,int):
				raise TypeError("templaterefresh must be set to int value")
			self._templaterefresh = templaterefresh
		except Exception as e :
			raise e


	'''
	get SecurityInsight record export interval.
	'''
	@property
	def securityinsightrecordinterval(self) :
		try:
			return self._securityinsightrecordinterval
		except Exception as e :
			raise e
	'''
	set SecurityInsight record export interval.
	'''
	@securityinsightrecordinterval.setter
	def securityinsightrecordinterval(self,securityinsightrecordinterval):
		try :
			if not isinstance(securityinsightrecordinterval,int):
				raise TypeError("securityinsightrecordinterval must be set to int value")
			self._securityinsightrecordinterval = securityinsightrecordinterval
		except Exception as e :
			raise e


	'''
	get Hostname of NetScaler.
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Hostname of NetScaler.
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e


	'''
	get NS IP Address
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NS IP Address
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
	get HTTP Setcookie header logging.
	'''
	@property
	def httpsetcookie(self) :
		try:
			return self._httpsetcookie
		except Exception as e :
			raise e
	'''
	set HTTP Setcookie header logging.
	'''
	@httpsetcookie.setter
	def httpsetcookie(self,httpsetcookie):
		try :
			if not isinstance(httpsetcookie,str):
				raise TypeError("httpsetcookie must be set to str value")
			self._httpsetcookie = httpsetcookie
		except Exception as e :
			raise e


	'''
	get HTTP Via header logging.
	'''
	@property
	def httpvia(self) :
		try:
			return self._httpvia
		except Exception as e :
			raise e
	'''
	set HTTP Via header logging.
	'''
	@httpvia.setter
	def httpvia(self,httpvia):
		try :
			if not isinstance(httpvia,str):
				raise TypeError("httpvia must be set to str value")
			self._httpvia = httpvia
		except Exception as e :
			raise e


	'''
	get load balancing vserver Diagnostic
	'''
	@property
	def lbvserver(self) :
		try:
			return self._lbvserver
		except Exception as e :
			raise e
	'''
	set load balancing vserver Diagnostic
	'''
	@lbvserver.setter
	def lbvserver(self,lbvserver) :
		try :
			if not isinstance(lbvserver,list):
				raise TypeError("lbvserver must be set to array of ns_lbvserver_diagnostic value")
			for item in lbvserver :
				if not isinstance(item,ns_lbvserver_diagnostic):
					raise TypeError("item must be set to ns_lbvserver_diagnostic value")
			self._lbvserver = lbvserver
		except Exception as e :
			raise e


	'''
	get HTTP Domain Name logging.
	'''
	@property
	def httpdomain(self) :
		try:
			return self._httpdomain
		except Exception as e :
			raise e
	'''
	set HTTP Domain Name logging.
	'''
	@httpdomain.setter
	def httpdomain(self,httpdomain):
		try :
			if not isinstance(httpdomain,str):
				raise TypeError("httpdomain must be set to str value")
			self._httpdomain = httpdomain
		except Exception as e :
			raise e


	'''
	get HTTP Setcookie2 header logging.
	'''
	@property
	def httpsetcookie2(self) :
		try:
			return self._httpsetcookie2
		except Exception as e :
			raise e
	'''
	set HTTP Setcookie2 header logging.
	'''
	@httpsetcookie2.setter
	def httpsetcookie2(self,httpsetcookie2):
		try :
			if not isinstance(httpsetcookie2,str):
				raise TypeError("httpsetcookie2 must be set to str value")
			self._httpsetcookie2 = httpsetcookie2
		except Exception as e :
			raise e


	'''
	get VPN Vserver Diagnostic
	'''
	@property
	def vpnvserver(self) :
		try:
			return self._vpnvserver
		except Exception as e :
			raise e
	'''
	set VPN Vserver Diagnostic
	'''
	@vpnvserver.setter
	def vpnvserver(self,vpnvserver) :
		try :
			if not isinstance(vpnvserver,list):
				raise TypeError("vpnvserver must be set to array of ns_nonlbvserver_diagnostic value")
			for item in vpnvserver :
				if not isinstance(item,ns_nonlbvserver_diagnostic):
					raise TypeError("item must be set to ns_nonlbvserver_diagnostic value")
			self._vpnvserver = vpnvserver
		except Exception as e :
			raise e


	'''
	get IPFIX flow record export interval.
	'''
	@property
	def flowrecordinterval(self) :
		try:
			return self._flowrecordinterval
		except Exception as e :
			raise e
	'''
	set IPFIX flow record export interval.
	'''
	@flowrecordinterval.setter
	def flowrecordinterval(self,flowrecordinterval):
		try :
			if not isinstance(flowrecordinterval,int):
				raise TypeError("flowrecordinterval must be set to int value")
			self._flowrecordinterval = flowrecordinterval
		except Exception as e :
			raise e


	'''
	get HTTP Authorization header logging.
	'''
	@property
	def httpauthorization(self) :
		try:
			return self._httpauthorization
		except Exception as e :
			raise e
	'''
	set HTTP Authorization header logging.
	'''
	@httpauthorization.setter
	def httpauthorization(self,httpauthorization):
		try :
			if not isinstance(httpauthorization,str):
				raise TypeError("httpauthorization must be set to str value")
			self._httpauthorization = httpauthorization
		except Exception as e :
			raise e


	'''
	get Skip Cache Redirection HTTP Transaction.
	'''
	@property
	def skipcacheredirectionhttptransaction(self) :
		try:
			return self._skipcacheredirectionhttptransaction
		except Exception as e :
			raise e
	'''
	set Skip Cache Redirection HTTP Transaction.
	'''
	@skipcacheredirectionhttptransaction.setter
	def skipcacheredirectionhttptransaction(self,skipcacheredirectionhttptransaction):
		try :
			if not isinstance(skipcacheredirectionhttptransaction,str):
				raise TypeError("skipcacheredirectionhttptransaction must be set to str value")
			self._skipcacheredirectionhttptransaction = skipcacheredirectionhttptransaction
		except Exception as e :
			raise e


	'''
	get  AAA username logging.
	'''
	@property
	def aaausername(self) :
		try:
			return self._aaausername
		except Exception as e :
			raise e
	'''
	set  AAA username logging.
	'''
	@aaausername.setter
	def aaausername(self,aaausername):
		try :
			if not isinstance(aaausername,str):
				raise TypeError("aaausername must be set to str value")
			self._aaausername = aaausername
		except Exception as e :
			raise e


	'''
	get IPFIX UDP Path MTU.
	'''
	@property
	def udppmtu(self) :
		try:
			return self._udppmtu
		except Exception as e :
			raise e
	'''
	set IPFIX UDP Path MTU.
	'''
	@udppmtu.setter
	def udppmtu(self,udppmtu):
		try :
			if not isinstance(udppmtu,int):
				raise TypeError("udppmtu must be set to int value")
			self._udppmtu = udppmtu
		except Exception as e :
			raise e


	'''
	get Log only client-side traffic.
	'''
	@property
	def clienttrafficonly(self) :
		try:
			return self._clienttrafficonly
		except Exception as e :
			raise e
	'''
	set Log only client-side traffic.
	'''
	@clienttrafficonly.setter
	def clienttrafficonly(self,clienttrafficonly):
		try :
			if not isinstance(clienttrafficonly,str):
				raise TypeError("clienttrafficonly must be set to str value")
			self._clienttrafficonly = clienttrafficonly
		except Exception as e :
			raise e


	'''
	get Stream Identifier Session Name logging.
	'''
	@property
	def securityinsighttraffic(self) :
		try:
			return self._securityinsighttraffic
		except Exception as e :
			raise e
	'''
	set Stream Identifier Session Name logging.
	'''
	@securityinsighttraffic.setter
	def securityinsighttraffic(self,securityinsighttraffic):
		try :
			if not isinstance(securityinsighttraffic,str):
				raise TypeError("securityinsighttraffic must be set to str value")
			self._securityinsighttraffic = securityinsighttraffic
		except Exception as e :
			raise e


	'''
	get HTTP Content-Type header logging.
	'''
	@property
	def httpcontenttype(self) :
		try:
			return self._httpcontenttype
		except Exception as e :
			raise e
	'''
	set HTTP Content-Type header logging.
	'''
	@httpcontenttype.setter
	def httpcontenttype(self,httpcontenttype):
		try :
			if not isinstance(httpcontenttype,str):
				raise TypeError("httpcontenttype must be set to str value")
			self._httpcontenttype = httpcontenttype
		except Exception as e :
			raise e


	'''
	get Cache Redirection Vserver Diagnostic
	'''
	@property
	def crvserver(self) :
		try:
			return self._crvserver
		except Exception as e :
			raise e
	'''
	set Cache Redirection Vserver Diagnostic
	'''
	@crvserver.setter
	def crvserver(self,crvserver) :
		try :
			if not isinstance(crvserver,list):
				raise TypeError("crvserver must be set to array of ns_nonlbvserver_diagnostic value")
			for item in crvserver :
				if not isinstance(item,ns_nonlbvserver_diagnostic):
					raise TypeError("item must be set to ns_nonlbvserver_diagnostic value")
			self._crvserver = crvserver
		except Exception as e :
			raise e


	'''
	get Content switching vserver Diagnostic
	'''
	@property
	def csvserver(self) :
		try:
			return self._csvserver
		except Exception as e :
			raise e
	'''
	set Content switching vserver Diagnostic
	'''
	@csvserver.setter
	def csvserver(self,csvserver) :
		try :
			if not isinstance(csvserver,list):
				raise TypeError("csvserver must be set to array of ns_nonlbvserver_diagnostic value")
			for item in csvserver :
				if not isinstance(item,ns_nonlbvserver_diagnostic):
					raise TypeError("item must be set to ns_nonlbvserver_diagnostic value")
			self._csvserver = csvserver
		except Exception as e :
			raise e


	'''
	get  HTTP Method logging.
	'''
	@property
	def httpmethod(self) :
		try:
			return self._httpmethod
		except Exception as e :
			raise e
	'''
	set  HTTP Method logging.
	'''
	@httpmethod.setter
	def httpmethod(self,httpmethod):
		try :
			if not isinstance(httpmethod,str):
				raise TypeError("httpmethod must be set to str value")
			self._httpmethod = httpmethod
		except Exception as e :
			raise e


	'''
	get HTTP Location header logging.
	'''
	@property
	def httplocation(self) :
		try:
			return self._httplocation
		except Exception as e :
			raise e
	'''
	set HTTP Location header logging.
	'''
	@httplocation.setter
	def httplocation(self,httplocation):
		try :
			if not isinstance(httplocation,str):
				raise TypeError("httplocation must be set to str value")
			self._httplocation = httplocation
		except Exception as e :
			raise e


	'''
	get true if appflow is enabled at NetScaler
	'''
	@property
	def is_appflow_enabled(self) :
		try:
			return self._is_appflow_enabled
		except Exception as e :
			raise e
	'''
	set true if appflow is enabled at NetScaler
	'''
	@is_appflow_enabled.setter
	def is_appflow_enabled(self,is_appflow_enabled):
		try :
			if not isinstance(is_appflow_enabled,bool):
				raise TypeError("is_appflow_enabled must be set to bool value")
			self._is_appflow_enabled = is_appflow_enabled
		except Exception as e :
			raise e


	'''
	get Stream Identifier Session Name logging.
	'''
	@property
	def identifiersessionname(self) :
		try:
			return self._identifiersessionname
		except Exception as e :
			raise e
	'''
	set Stream Identifier Session Name logging.
	'''
	@identifiersessionname.setter
	def identifiersessionname(self,identifiersessionname):
		try :
			if not isinstance(identifiersessionname,str):
				raise TypeError("identifiersessionname must be set to str value")
			self._identifiersessionname = identifiersessionname
		except Exception as e :
			raise e


	'''
	get Connection Chaining.
	'''
	@property
	def connectionchaining(self) :
		try:
			return self._connectionchaining
		except Exception as e :
			raise e
	'''
	set Connection Chaining.
	'''
	@connectionchaining.setter
	def connectionchaining(self,connectionchaining):
		try :
			if not isinstance(connectionchaining,str):
				raise TypeError("connectionchaining must be set to str value")
			self._connectionchaining = connectionchaining
		except Exception as e :
			raise e


	'''
	get HTTP X-Forwarded-For header logging.
	'''
	@property
	def httpxforwardedfor(self) :
		try:
			return self._httpxforwardedfor
		except Exception as e :
			raise e
	'''
	set HTTP X-Forwarded-For header logging.
	'''
	@httpxforwardedfor.setter
	def httpxforwardedfor(self,httpxforwardedfor):
		try :
			if not isinstance(httpxforwardedfor,str):
				raise TypeError("httpxforwardedfor must be set to str value")
			self._httpxforwardedfor = httpxforwardedfor
		except Exception as e :
			raise e


	'''
	get Appname refresh interval.
	'''
	@property
	def appnamerefresh(self) :
		try:
			return self._appnamerefresh
		except Exception as e :
			raise e
	'''
	set Appname refresh interval.
	'''
	@appnamerefresh.setter
	def appnamerefresh(self,appnamerefresh):
		try :
			if not isinstance(appnamerefresh,int):
				raise TypeError("appnamerefresh must be set to int value")
			self._appnamerefresh = appnamerefresh
		except Exception as e :
			raise e


	'''
	get IPFIX Observation Domain Name.
	'''
	@property
	def observationdomainname(self) :
		try:
			return self._observationdomainname
		except Exception as e :
			raise e
	'''
	set IPFIX Observation Domain Name.
	'''
	@observationdomainname.setter
	def observationdomainname(self,observationdomainname):
		try :
			if not isinstance(observationdomainname,str):
				raise TypeError("observationdomainname must be set to str value")
			self._observationdomainname = observationdomainname
		except Exception as e :
			raise e


	'''
	get Stream Identifier Name logging.
	'''
	@property
	def identifiername(self) :
		try:
			return self._identifiername
		except Exception as e :
			raise e
	'''
	set Stream Identifier Name logging.
	'''
	@identifiername.setter
	def identifiername(self,identifiername):
		try :
			if not isinstance(identifiername,str):
				raise TypeError("identifiername must be set to str value")
			self._identifiername = identifiername
		except Exception as e :
			raise e


	'''
	get  HTTP COOKIE LOGGING.
	'''
	@property
	def httpcookie(self) :
		try:
			return self._httpcookie
		except Exception as e :
			raise e
	'''
	set  HTTP COOKIE LOGGING.
	'''
	@httpcookie.setter
	def httpcookie(self,httpcookie):
		try :
			if not isinstance(httpcookie,str):
				raise TypeError("httpcookie must be set to str value")
			self._httpcookie = httpcookie
		except Exception as e :
			raise e


	'''
	get HTTP URL logging.
	'''
	@property
	def httpurl(self) :
		try:
			return self._httpurl
		except Exception as e :
			raise e
	'''
	set HTTP URL logging.
	'''
	@httpurl.setter
	def httpurl(self,httpurl):
		try :
			if not isinstance(httpurl,str):
				raise TypeError("httpurl must be set to str value")
			self._httpurl = httpurl
		except Exception as e :
			raise e


	'''
	get  HTTP User Agent Logging.
	'''
	@property
	def httpuseragent(self) :
		try:
			return self._httpuseragent
		except Exception as e :
			raise e
	'''
	set  HTTP User Agent Logging.
	'''
	@httpuseragent.setter
	def httpuseragent(self,httpuseragent):
		try :
			if not isinstance(httpuseragent,str):
				raise TypeError("httpuseragent must be set to str value")
			self._httpuseragent = httpuseragent
		except Exception as e :
			raise e


	'''
	get  HTTP Host logging.
	'''
	@property
	def httphost(self) :
		try:
			return self._httphost
		except Exception as e :
			raise e
	'''
	set  HTTP Host logging.
	'''
	@httphost.setter
	def httphost(self,httphost):
		try :
			if not isinstance(httphost,str):
				raise TypeError("httphost must be set to str value")
			self._httphost = httphost
		except Exception as e :
			raise e

	'''
	Use this method to diagnose NetScaler.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_insight_diagnostic_obj=ns_insight_diagnostic()
				response = ns_insight_diagnostic_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_insight_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_insight_diagnostic_obj = ns_insight_diagnostic()
			option_ = options()
			option_._filter=filter_
			return ns_insight_diagnostic_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_insight_diagnostic resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_insight_diagnostic_obj = ns_insight_diagnostic()
			option_ = options()
			option_._count=True
			response = ns_insight_diagnostic_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_insight_diagnostic resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_insight_diagnostic_obj = ns_insight_diagnostic()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_insight_diagnostic_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_insight_diagnostic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_insight_diagnostic
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_insight_diagnostic_responses, response, "ns_insight_diagnostic_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_insight_diagnostic_response_array
				i=0
				error = [ns_insight_diagnostic() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_insight_diagnostic_response_array
			i=0
			ns_insight_diagnostic_objs = [ns_insight_diagnostic() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_insight_diagnostic'):
					for props in obj._ns_insight_diagnostic:
						result = service.payload_formatter.string_to_bulk_resource(ns_insight_diagnostic_response,self.__class__.__name__,props)
						ns_insight_diagnostic_objs[i] = result.ns_insight_diagnostic
						i=i+1
			return ns_insight_diagnostic_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_insight_diagnostic,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_insight_diagnostic_response(base_response):
	def __init__(self,length=1) :
		self.ns_insight_diagnostic= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_insight_diagnostic= [ ns_insight_diagnostic() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_insight_diagnostic_responses(base_response):
	def __init__(self,length=1) :
		self.ns_insight_diagnostic_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_insight_diagnostic_response_array = [ ns_insight_diagnostic() for _ in range(length)]
