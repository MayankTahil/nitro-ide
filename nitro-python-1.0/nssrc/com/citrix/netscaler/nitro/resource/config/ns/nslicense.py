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

class nslicense(base_resource) :
	""" Configuration for license resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._wl = None
		self._sp = None
		self._lb = None
		self._cs = None
		self._cr = None
		self._sc = None
		self._cmp = None
		self._delta = None
		self._pq = None
		self._ssl = None
		self._gslb = None
		self._gslbp = None
		self._hdosp = None
		self._routing = None
		self._cf = None
		self._contentaccelerator = None
		self._ic = None
		self._sslvpn = None
		self._f_sslvpn_users = None
		self._f_ica_users = None
		self._aaa = None
		self._ospf = None
		self._rip = None
		self._bgp = None
		self._rewrite = None
		self._ipv6pt = None
		self._appfw = None
		self._responder = None
		self._agee = None
		self._nsxn = None
		self._htmlinjection = None
		self._modelid = None
		self._push = None
		self._wionns = None
		self._appflow = None
		self._cloudbridge = None
		self._cloudbridgeappliance = None
		self._cloudextenderappliance = None
		self._isis = None
		self._cluster = None
		self._ch = None
		self._appqoe = None
		self._appflowica = None
		self._isstandardlic = None
		self._isenterpriselic = None
		self._isplatinumlic = None
		self._issgwylic = None
		self._rise = None
		self._feo = None
		self._lsn = None
		self._licensingmode = None
		self._rdpproxy = None
		self._rep = None
		self._urlfiltering = None
		self._videooptimization = None

	@property
	def wl(self) :
		r"""Web Logging.
		"""
		try :
			return self._wl
		except Exception as e:
			raise e

	@property
	def sp(self) :
		r"""Surge Protection.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	@property
	def lb(self) :
		r"""Load Balancing.
		"""
		try :
			return self._lb
		except Exception as e:
			raise e

	@property
	def cs(self) :
		r"""Content Switching.
		"""
		try :
			return self._cs
		except Exception as e:
			raise e

	@property
	def cr(self) :
		r"""Cache Redirect.
		"""
		try :
			return self._cr
		except Exception as e:
			raise e

	@property
	def sc(self) :
		r"""Sure Connect.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		r"""Compression.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@property
	def delta(self) :
		r"""Delta Compression.
		"""
		try :
			return self._delta
		except Exception as e:
			raise e

	@property
	def pq(self) :
		r"""Priority Queuing.
		"""
		try :
			return self._pq
		except Exception as e:
			raise e

	@property
	def ssl(self) :
		r"""Secure Sockets Layer.
		"""
		try :
			return self._ssl
		except Exception as e:
			raise e

	@property
	def gslb(self) :
		r"""Global Server Load Balancing.
		"""
		try :
			return self._gslb
		except Exception as e:
			raise e

	@property
	def gslbp(self) :
		r"""GSLB Proximity.
		"""
		try :
			return self._gslbp
		except Exception as e:
			raise e

	@property
	def hdosp(self) :
		r"""DOS Protection.
		"""
		try :
			return self._hdosp
		except Exception as e:
			raise e

	@property
	def routing(self) :
		r"""Routing.
		"""
		try :
			return self._routing
		except Exception as e:
			raise e

	@property
	def cf(self) :
		r"""Content Filter.
		"""
		try :
			return self._cf
		except Exception as e:
			raise e

	@property
	def contentaccelerator(self) :
		r"""transparent Integrated Caching.
		"""
		try :
			return self._contentaccelerator
		except Exception as e:
			raise e

	@property
	def ic(self) :
		r"""Integrated Caching.
		"""
		try :
			return self._ic
		except Exception as e:
			raise e

	@property
	def sslvpn(self) :
		r"""SSL VPN.
		"""
		try :
			return self._sslvpn
		except Exception as e:
			raise e

	@property
	def f_sslvpn_users(self) :
		r"""Number of licensed users allowed by this license.
		"""
		try :
			return self._f_sslvpn_users
		except Exception as e:
			raise e

	@property
	def f_ica_users(self) :
		r"""Number of licensed users allowed by ICAONLY license. As long as the AG Feature is licensed,
		unlimited number of ICA connections are accepted.
		(In API, 0 value for this parameter means unlimited when AG license in ON).
		"""
		try :
			return self._f_ica_users
		except Exception as e:
			raise e

	@property
	def aaa(self) :
		r"""AAA.
		"""
		try :
			return self._aaa
		except Exception as e:
			raise e

	@property
	def ospf(self) :
		r"""OSPF Routing.
		"""
		try :
			return self._ospf
		except Exception as e:
			raise e

	@property
	def rip(self) :
		r"""RIP Routing.
		"""
		try :
			return self._rip
		except Exception as e:
			raise e

	@property
	def bgp(self) :
		r"""BGP Routing.
		"""
		try :
			return self._bgp
		except Exception as e:
			raise e

	@property
	def rewrite(self) :
		r"""Rewrite.
		"""
		try :
			return self._rewrite
		except Exception as e:
			raise e

	@property
	def ipv6pt(self) :
		r"""IPv6 protocol translation.
		"""
		try :
			return self._ipv6pt
		except Exception as e:
			raise e

	@property
	def appfw(self) :
		r"""Application Firewall.
		"""
		try :
			return self._appfw
		except Exception as e:
			raise e

	@property
	def responder(self) :
		r"""Responder.
		"""
		try :
			return self._responder
		except Exception as e:
			raise e

	@property
	def agee(self) :
		try :
			return self._agee
		except Exception as e:
			raise e

	@property
	def nsxn(self) :
		try :
			return self._nsxn
		except Exception as e:
			raise e

	@property
	def htmlinjection(self) :
		r"""HTML Injection.
		"""
		try :
			return self._htmlinjection
		except Exception as e:
			raise e

	@property
	def modelid(self) :
		r"""Model Number ID.
		"""
		try :
			return self._modelid
		except Exception as e:
			raise e

	@property
	def push(self) :
		r"""NetScaler Push.
		"""
		try :
			return self._push
		except Exception as e:
			raise e

	@property
	def wionns(self) :
		r"""WI on NS.
		"""
		try :
			return self._wionns
		except Exception as e:
			raise e

	@property
	def appflow(self) :
		r"""AppFlow.
		"""
		try :
			return self._appflow
		except Exception as e:
			raise e

	@property
	def cloudbridge(self) :
		r"""CloudBridge.
		"""
		try :
			return self._cloudbridge
		except Exception as e:
			raise e

	@property
	def cloudbridgeappliance(self) :
		try :
			return self._cloudbridgeappliance
		except Exception as e:
			raise e

	@property
	def cloudextenderappliance(self) :
		try :
			return self._cloudextenderappliance
		except Exception as e:
			raise e

	@property
	def isis(self) :
		r"""ISIS Routing.
		"""
		try :
			return self._isis
		except Exception as e:
			raise e

	@property
	def cluster(self) :
		r"""Clustering.
		"""
		try :
			return self._cluster
		except Exception as e:
			raise e

	@property
	def ch(self) :
		r"""Call Home.
		"""
		try :
			return self._ch
		except Exception as e:
			raise e

	@property
	def appqoe(self) :
		r"""AppQoS.
		"""
		try :
			return self._appqoe
		except Exception as e:
			raise e

	@property
	def appflowica(self) :
		r"""Appflow for ICA.
		"""
		try :
			return self._appflowica
		except Exception as e:
			raise e

	@property
	def isstandardlic(self) :
		r"""Standard License.
		"""
		try :
			return self._isstandardlic
		except Exception as e:
			raise e

	@property
	def isenterpriselic(self) :
		r"""Enterprise License.
		"""
		try :
			return self._isenterpriselic
		except Exception as e:
			raise e

	@property
	def isplatinumlic(self) :
		r"""Platinum License.
		"""
		try :
			return self._isplatinumlic
		except Exception as e:
			raise e

	@property
	def issgwylic(self) :
		r"""Simple Gateway License.
		"""
		try :
			return self._issgwylic
		except Exception as e:
			raise e

	@property
	def rise(self) :
		r"""RISE.
		"""
		try :
			return self._rise
		except Exception as e:
			raise e

	@property
	def feo(self) :
		r"""Front End Optimization.
		"""
		try :
			return self._feo
		except Exception as e:
			raise e

	@property
	def lsn(self) :
		r"""Large Scale NAT.
		"""
		try :
			return self._lsn
		except Exception as e:
			raise e

	@property
	def licensingmode(self) :
		r"""Pooled Licensed.<br/>Default value: Local<br/>Possible values = Local, Pooled, CICO.
		"""
		try :
			return self._licensingmode
		except Exception as e:
			raise e

	@property
	def rdpproxy(self) :
		r"""RDPPROXY.
		"""
		try :
			return self._rdpproxy
		except Exception as e:
			raise e

	@property
	def rep(self) :
		r"""Reputation Services.
		"""
		try :
			return self._rep
		except Exception as e:
			raise e

	@property
	def urlfiltering(self) :
		r"""URL Filtering.
		"""
		try :
			return self._urlfiltering
		except Exception as e:
			raise e

	@property
	def videooptimization(self) :
		r"""Video Optimization.
		"""
		try :
			return self._videooptimization
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslicense_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslicense
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nslicense resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslicense()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Licensingmode:
		Local = "Local"
		Pooled = "Pooled"
		CICO = "CICO"

class nslicense_response(base_response) :
	def __init__(self, length=1) :
		self.nslicense = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslicense = [nslicense() for _ in range(length)]

