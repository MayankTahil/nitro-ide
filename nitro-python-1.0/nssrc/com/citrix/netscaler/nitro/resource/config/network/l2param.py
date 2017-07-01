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

class l2param(base_resource) :
	""" Configuration for Layer 2 related parameter resource. """
	def __init__(self) :
		self._mbfpeermacupdate = None
		self._maxbridgecollision = None
		self._bdggrpproxyarp = None
		self._bdgsetting = None
		self._garponvridintf = None
		self._macmodefwdmypkt = None
		self._usemymac = None
		self._proxyarp = None
		self._garpreply = None
		self._mbfinstlearning = None
		self._rstintfonhafo = None
		self._skipproxyingbsdtraffic = None
		self._returntoethernetsender = None
		self._stopmacmoveupdate = None
		self._bridgeagetimeout = None

	@property
	def mbfpeermacupdate(self) :
		r"""When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10.
		"""
		try :
			return self._mbfpeermacupdate
		except Exception as e:
			raise e

	@mbfpeermacupdate.setter
	def mbfpeermacupdate(self, mbfpeermacupdate) :
		r"""When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10
		"""
		try :
			self._mbfpeermacupdate = mbfpeermacupdate
		except Exception as e:
			raise e

	@property
	def maxbridgecollision(self) :
		r"""Maximum bridge collision for loop detection .<br/>Default value: 20.
		"""
		try :
			return self._maxbridgecollision
		except Exception as e:
			raise e

	@maxbridgecollision.setter
	def maxbridgecollision(self, maxbridgecollision) :
		r"""Maximum bridge collision for loop detection .<br/>Default value: 20
		"""
		try :
			self._maxbridgecollision = maxbridgecollision
		except Exception as e:
			raise e

	@property
	def bdggrpproxyarp(self) :
		r"""Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._bdggrpproxyarp
		except Exception as e:
			raise e

	@bdggrpproxyarp.setter
	def bdggrpproxyarp(self, bdggrpproxyarp) :
		r"""Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._bdggrpproxyarp = bdggrpproxyarp
		except Exception as e:
			raise e

	@property
	def bdgsetting(self) :
		r"""Bridging settings for C2C behavior. If enabled, each PE will learn MAC entries independently. Otherwise, when L2 mode is ON, learned MAC entries on a PE will be broadcasted to all other PEs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._bdgsetting
		except Exception as e:
			raise e

	@bdgsetting.setter
	def bdgsetting(self, bdgsetting) :
		r"""Bridging settings for C2C behavior. If enabled, each PE will learn MAC entries independently. Otherwise, when L2 mode is ON, learned MAC entries on a PE will be broadcasted to all other PEs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._bdgsetting = bdgsetting
		except Exception as e:
			raise e

	@property
	def garponvridintf(self) :
		r"""Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._garponvridintf
		except Exception as e:
			raise e

	@garponvridintf.setter
	def garponvridintf(self, garponvridintf) :
		r"""Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._garponvridintf = garponvridintf
		except Exception as e:
			raise e

	@property
	def macmodefwdmypkt(self) :
		r"""Allows MAC mode vserver to pick and forward the packets even if it is destined to NetScaler owned VIP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._macmodefwdmypkt
		except Exception as e:
			raise e

	@macmodefwdmypkt.setter
	def macmodefwdmypkt(self, macmodefwdmypkt) :
		r"""Allows MAC mode vserver to pick and forward the packets even if it is destined to NetScaler owned VIP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._macmodefwdmypkt = macmodefwdmypkt
		except Exception as e:
			raise e

	@property
	def usemymac(self) :
		r"""Use Netscaler MAC for all outgoing packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usemymac
		except Exception as e:
			raise e

	@usemymac.setter
	def usemymac(self, usemymac) :
		r"""Use Netscaler MAC for all outgoing packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usemymac = usemymac
		except Exception as e:
			raise e

	@property
	def proxyarp(self) :
		r"""Proxies the ARP as Netscaler MAC for FreeBSD.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._proxyarp
		except Exception as e:
			raise e

	@proxyarp.setter
	def proxyarp(self, proxyarp) :
		r"""Proxies the ARP as Netscaler MAC for FreeBSD.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._proxyarp = proxyarp
		except Exception as e:
			raise e

	@property
	def garpreply(self) :
		r"""Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._garpreply
		except Exception as e:
			raise e

	@garpreply.setter
	def garpreply(self, garpreply) :
		r"""Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._garpreply = garpreply
		except Exception as e:
			raise e

	@property
	def mbfinstlearning(self) :
		r"""Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mbfinstlearning
		except Exception as e:
			raise e

	@mbfinstlearning.setter
	def mbfinstlearning(self, mbfinstlearning) :
		r"""Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mbfinstlearning = mbfinstlearning
		except Exception as e:
			raise e

	@property
	def rstintfonhafo(self) :
		r"""Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rstintfonhafo
		except Exception as e:
			raise e

	@rstintfonhafo.setter
	def rstintfonhafo(self, rstintfonhafo) :
		r"""Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rstintfonhafo = rstintfonhafo
		except Exception as e:
			raise e

	@property
	def skipproxyingbsdtraffic(self) :
		r"""Control source parameters (IP and Port) for FreeBSD initiated traffic. If Enabled, source parameters are retained. Else proxy the source parameters based on next hop.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skipproxyingbsdtraffic
		except Exception as e:
			raise e

	@skipproxyingbsdtraffic.setter
	def skipproxyingbsdtraffic(self, skipproxyingbsdtraffic) :
		r"""Control source parameters (IP and Port) for FreeBSD initiated traffic. If Enabled, source parameters are retained. Else proxy the source parameters based on next hop.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skipproxyingbsdtraffic = skipproxyingbsdtraffic
		except Exception as e:
			raise e

	@property
	def returntoethernetsender(self) :
		r""" Return to ethernet sender.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._returntoethernetsender
		except Exception as e:
			raise e

	@returntoethernetsender.setter
	def returntoethernetsender(self, returntoethernetsender) :
		r""" Return to ethernet sender.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._returntoethernetsender = returntoethernetsender
		except Exception as e:
			raise e

	@property
	def stopmacmoveupdate(self) :
		r"""Stop Update of server mac change to NAT sessions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._stopmacmoveupdate
		except Exception as e:
			raise e

	@stopmacmoveupdate.setter
	def stopmacmoveupdate(self, stopmacmoveupdate) :
		r"""Stop Update of server mac change to NAT sessions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._stopmacmoveupdate = stopmacmoveupdate
		except Exception as e:
			raise e

	@property
	def bridgeagetimeout(self) :
		r"""Time-out value for the bridge table entries, in seconds. The new value applies only to the entries that are dynamically learned after the new value is set. Previously existing bridge table entries expire after the previously configured time-out value.<br/>Default value: 300<br/>Minimum length =  60<br/>Maximum length =  300.
		"""
		try :
			return self._bridgeagetimeout
		except Exception as e:
			raise e

	@bridgeagetimeout.setter
	def bridgeagetimeout(self, bridgeagetimeout) :
		r"""Time-out value for the bridge table entries, in seconds. The new value applies only to the entries that are dynamically learned after the new value is set. Previously existing bridge table entries expire after the previously configured time-out value.<br/>Default value: 300<br/>Minimum length =  60<br/>Maximum length =  300
		"""
		try :
			self._bridgeagetimeout = bridgeagetimeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(l2param_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.l2param
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update l2param.
		"""
		try :
			if type(resource) is not list :
				updateresource = l2param()
				updateresource.mbfpeermacupdate = resource.mbfpeermacupdate
				updateresource.maxbridgecollision = resource.maxbridgecollision
				updateresource.bdggrpproxyarp = resource.bdggrpproxyarp
				updateresource.bdgsetting = resource.bdgsetting
				updateresource.garponvridintf = resource.garponvridintf
				updateresource.macmodefwdmypkt = resource.macmodefwdmypkt
				updateresource.usemymac = resource.usemymac
				updateresource.proxyarp = resource.proxyarp
				updateresource.garpreply = resource.garpreply
				updateresource.mbfinstlearning = resource.mbfinstlearning
				updateresource.rstintfonhafo = resource.rstintfonhafo
				updateresource.skipproxyingbsdtraffic = resource.skipproxyingbsdtraffic
				updateresource.returntoethernetsender = resource.returntoethernetsender
				updateresource.stopmacmoveupdate = resource.stopmacmoveupdate
				updateresource.bridgeagetimeout = resource.bridgeagetimeout
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of l2param resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = l2param()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the l2param resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = l2param()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Proxyarp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Usemymac:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Macmodefwdmypkt:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Bdgsetting:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Bdggrpproxyarp:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Returntoethernetsender:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Garponvridintf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rstintfonhafo:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Garpreply:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mbfinstlearning:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skipproxyingbsdtraffic:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Stopmacmoveupdate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class l2param_response(base_response) :
	def __init__(self, length=1) :
		self.l2param = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.l2param = [l2param() for _ in range(length)]

