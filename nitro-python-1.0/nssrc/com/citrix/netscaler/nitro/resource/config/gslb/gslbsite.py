#
# Copyright (c) 2008-2016 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class gslbsite(base_resource) :
	""" Configuration for GSLB site resource. """
	def __init__(self) :
		self._sitename = None
		self._sitetype = None
		self._siteipaddress = None
		self._publicip = None
		self._metricexchange = None
		self._nwmetricexchange = None
		self._sessionexchange = None
		self._triggermonitor = None
		self._parentsite = None
		self._clip = None
		self._publicclip = None
		self._naptrreplacementsuffix = None
		self._backupparentlist = []
		self._status = None
		self._persistencemepstatus = None
		self._version = None
		self._curbackupparentip = None
		self.___count = 0

	@property
	def sitename(self) :
		r"""Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsite" or 'my gslbsite').<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		r"""Name for the GSLB site. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my gslbsite" or 'my gslbsite').<br/>Minimum length =  1
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def sitetype(self) :
		r"""Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.<br/>Default value: NONE<br/>Possible values = REMOTE, LOCAL.
		"""
		try :
			return self._sitetype
		except Exception as e:
			raise e

	@sitetype.setter
	def sitetype(self, sitetype) :
		r"""Type of site to create. If the type is not specified, the appliance automatically detects and sets the type on the basis of the IP address being assigned to the site. If the specified site IP address is owned by the appliance (for example, a MIP address or SNIP address), the site is a local site. Otherwise, it is a remote site.<br/>Default value: NONE<br/>Possible values = REMOTE, LOCAL
		"""
		try :
			self._sitetype = sitetype
		except Exception as e:
			raise e

	@property
	def siteipaddress(self) :
		r"""IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).<br/>Minimum length =  1.
		"""
		try :
			return self._siteipaddress
		except Exception as e:
			raise e

	@siteipaddress.setter
	def siteipaddress(self, siteipaddress) :
		r"""IP address for the GSLB site. The GSLB site uses this IP address to communicate with other GSLB sites. For a local site, use any IP address that is owned by the appliance (for example, a SNIP or MIP address, or the IP address of the ADNS service).<br/>Minimum length =  1
		"""
		try :
			self._siteipaddress = siteipaddress
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.<br/>Minimum length =  1.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@publicip.setter
	def publicip(self, publicip) :
		r"""Public IP address for the local site. Required only if the appliance is deployed in a private address space and the site has a public IP address hosted on an external firewall or a NAT device.<br/>Minimum length =  1
		"""
		try :
			self._publicip = publicip
		except Exception as e:
			raise e

	@property
	def metricexchange(self) :
		r"""Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second. 
		If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._metricexchange
		except Exception as e:
			raise e

	@metricexchange.setter
	def metricexchange(self, metricexchange) :
		r"""Exchange metrics with other sites. Metrics are exchanged by using Metric Exchange Protocol (MEP). The appliances in the GSLB setup exchange health information once every second. 
		If you disable metrics exchange, you can use only static load balancing methods (such as round robin, static proximity, or the hash-based methods), and if you disable metrics exchange when a dynamic load balancing method (such as least connection) is in operation, the appliance falls back to round robin. Also, if you disable metrics exchange, you must use a monitor to determine the state of GSLB services. Otherwise, the service is marked as DOWN.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._metricexchange = metricexchange
		except Exception as e:
			raise e

	@property
	def nwmetricexchange(self) :
		r"""Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nwmetricexchange
		except Exception as e:
			raise e

	@nwmetricexchange.setter
	def nwmetricexchange(self, nwmetricexchange) :
		r"""Exchange, with other GSLB sites, network metrics such as round-trip time (RTT), learned from communications with various local DNS (LDNS) servers used by clients. RTT information is used in the dynamic RTT load balancing method, and is exchanged every 5 seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._nwmetricexchange = nwmetricexchange
		except Exception as e:
			raise e

	@property
	def sessionexchange(self) :
		r"""Exchange persistent session entries with other GSLB sites every five seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionexchange
		except Exception as e:
			raise e

	@sessionexchange.setter
	def sessionexchange(self, sessionexchange) :
		r"""Exchange persistent session entries with other GSLB sites every five seconds.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionexchange = sessionexchange
		except Exception as e:
			raise e

	@property
	def triggermonitor(self) :
		r"""Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:
		* ALWAYS - Monitor the GSLB service at all times.
		* MEPDOWN - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.
		MEPDOWN_SVCDOWN - Monitor the service in either of the following situations: 
		* The exchange of metrics through MEP is disabled.
		* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.<br/>Default value: ALWAYS<br/>Possible values = ALWAYS, MEPDOWN, MEPDOWN_SVCDOWN.
		"""
		try :
			return self._triggermonitor
		except Exception as e:
			raise e

	@triggermonitor.setter
	def triggermonitor(self, triggermonitor) :
		r"""Specify the conditions under which the GSLB service must be monitored by a monitor, if one is bound. Available settings function as follows:
		* ALWAYS - Monitor the GSLB service at all times.
		* MEPDOWN - Monitor the GSLB service only when the exchange of metrics through the Metrics Exchange Protocol (MEP) is disabled.
		MEPDOWN_SVCDOWN - Monitor the service in either of the following situations: 
		* The exchange of metrics through MEP is disabled.
		* The exchange of metrics through MEP is enabled but the status of the service, learned through metrics exchange, is DOWN.<br/>Default value: ALWAYS<br/>Possible values = ALWAYS, MEPDOWN, MEPDOWN_SVCDOWN
		"""
		try :
			self._triggermonitor = triggermonitor
		except Exception as e:
			raise e

	@property
	def parentsite(self) :
		r"""Parent site of the GSLB site, in a parent-child topology.
		"""
		try :
			return self._parentsite
		except Exception as e:
			raise e

	@parentsite.setter
	def parentsite(self, parentsite) :
		r"""Parent site of the GSLB site, in a parent-child topology.
		"""
		try :
			self._parentsite = parentsite
		except Exception as e:
			raise e

	@property
	def clip(self) :
		r"""Cluster IP address. Specify this parameter to connect to the remote cluster site for GSLB auto-sync. Note: The cluster IP address is defined when creating the cluster.
		"""
		try :
			return self._clip
		except Exception as e:
			raise e

	@clip.setter
	def clip(self, clip) :
		r"""Cluster IP address. Specify this parameter to connect to the remote cluster site for GSLB auto-sync. Note: The cluster IP address is defined when creating the cluster.
		"""
		try :
			self._clip = clip
		except Exception as e:
			raise e

	@property
	def publicclip(self) :
		r"""IP address to be used to globally access the remote cluster when it is deployed behind a NAT. It can be same as the normal cluster IP address.
		"""
		try :
			return self._publicclip
		except Exception as e:
			raise e

	@publicclip.setter
	def publicclip(self, publicclip) :
		r"""IP address to be used to globally access the remote cluster when it is deployed behind a NAT. It can be same as the normal cluster IP address.
		"""
		try :
			self._publicclip = publicclip
		except Exception as e:
			raise e

	@property
	def naptrreplacementsuffix(self) :
		r"""The naptr replacement suffix configured here will be used to construct the naptr replacement field in NAPTR record.<br/>Minimum length =  1.
		"""
		try :
			return self._naptrreplacementsuffix
		except Exception as e:
			raise e

	@naptrreplacementsuffix.setter
	def naptrreplacementsuffix(self, naptrreplacementsuffix) :
		r"""The naptr replacement suffix configured here will be used to construct the naptr replacement field in NAPTR record.<br/>Minimum length =  1
		"""
		try :
			self._naptrreplacementsuffix = naptrreplacementsuffix
		except Exception as e:
			raise e

	@property
	def backupparentlist(self) :
		r"""The list of backup gslb sites configured in preferred order. Need to be parent gsb sites.<br/>Default value: "None".
		"""
		try :
			return self._backupparentlist
		except Exception as e:
			raise e

	@backupparentlist.setter
	def backupparentlist(self, backupparentlist) :
		r"""The list of backup gslb sites configured in preferred order. Need to be parent gsb sites.<br/>Default value: "None"
		"""
		try :
			self._backupparentlist = backupparentlist
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Current metric exchange status.<br/>Possible values = ACTIVE, INACTIVE, DOWN.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def persistencemepstatus(self) :
		r"""Network metric and persistence exchange MEP connection status.<br/>Possible values = ACTIVE, INACTIVE, DOWN.
		"""
		try :
			return self._persistencemepstatus
		except Exception as e:
			raise e

	@property
	def version(self) :
		r"""will be true if the remote site's version is ncore compatible with the local site.(>= 9.2).
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def curbackupparentip(self) :
		r"""Current active backup parent IP address since the configured is DOWN.
		"""
		try :
			return self._curbackupparentip
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbsite_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbsite
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.sitename is not None :
				return str(self.sitename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add gslbsite.
		"""
		try :
			if type(resource) is not list :
				addresource = gslbsite()
				addresource.sitename = resource.sitename
				addresource.sitetype = resource.sitetype
				addresource.siteipaddress = resource.siteipaddress
				addresource.publicip = resource.publicip
				addresource.metricexchange = resource.metricexchange
				addresource.nwmetricexchange = resource.nwmetricexchange
				addresource.sessionexchange = resource.sessionexchange
				addresource.triggermonitor = resource.triggermonitor
				addresource.parentsite = resource.parentsite
				addresource.clip = resource.clip
				addresource.publicclip = resource.publicclip
				addresource.naptrreplacementsuffix = resource.naptrreplacementsuffix
				addresource.backupparentlist = resource.backupparentlist
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ gslbsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].sitename = resource[i].sitename
						addresources[i].sitetype = resource[i].sitetype
						addresources[i].siteipaddress = resource[i].siteipaddress
						addresources[i].publicip = resource[i].publicip
						addresources[i].metricexchange = resource[i].metricexchange
						addresources[i].nwmetricexchange = resource[i].nwmetricexchange
						addresources[i].sessionexchange = resource[i].sessionexchange
						addresources[i].triggermonitor = resource[i].triggermonitor
						addresources[i].parentsite = resource[i].parentsite
						addresources[i].clip = resource[i].clip
						addresources[i].publicclip = resource[i].publicclip
						addresources[i].naptrreplacementsuffix = resource[i].naptrreplacementsuffix
						addresources[i].backupparentlist = resource[i].backupparentlist
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete gslbsite.
		"""
		try :
			if type(resource) is not list :
				deleteresource = gslbsite()
				if type(resource) !=  type(deleteresource):
					deleteresource.sitename = resource
				else :
					deleteresource.sitename = resource.sitename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sitename = resource[i].sitename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update gslbsite.
		"""
		try :
			if type(resource) is not list :
				updateresource = gslbsite()
				updateresource.sitename = resource.sitename
				updateresource.metricexchange = resource.metricexchange
				updateresource.nwmetricexchange = resource.nwmetricexchange
				updateresource.sessionexchange = resource.sessionexchange
				updateresource.triggermonitor = resource.triggermonitor
				updateresource.naptrreplacementsuffix = resource.naptrreplacementsuffix
				updateresource.backupparentlist = resource.backupparentlist
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ gslbsite() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].sitename = resource[i].sitename
						updateresources[i].metricexchange = resource[i].metricexchange
						updateresources[i].nwmetricexchange = resource[i].nwmetricexchange
						updateresources[i].sessionexchange = resource[i].sessionexchange
						updateresources[i].triggermonitor = resource[i].triggermonitor
						updateresources[i].naptrreplacementsuffix = resource[i].naptrreplacementsuffix
						updateresources[i].backupparentlist = resource[i].backupparentlist
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of gslbsite resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbsite()
				if type(resource) !=  type(unsetresource):
					unsetresource.sitename = resource
				else :
					unsetresource.sitename = resource.sitename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbsite() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sitename = resource[i].sitename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the gslbsite resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbsite()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = gslbsite()
					obj.sitename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [gslbsite() for _ in range(len(name))]
						obj = [gslbsite() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = gslbsite()
							obj[i].sitename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of gslbsite resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the gslbsite resources configured on NetScaler.
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of gslbsite resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbsite()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sessionexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nwmetricexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Status:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"
		DOWN = "DOWN"

	class Triggermonitor:
		ALWAYS = "ALWAYS"
		MEPDOWN = "MEPDOWN"
		MEPDOWN_SVCDOWN = "MEPDOWN_SVCDOWN"

	class Persistencemepstatus:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"
		DOWN = "DOWN"

	class Metricexchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sitetype:
		REMOTE = "REMOTE"
		LOCAL = "LOCAL"

class gslbsite_response(base_response) :
	def __init__(self, length=1) :
		self.gslbsite = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbsite = [gslbsite() for _ in range(length)]

