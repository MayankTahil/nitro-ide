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

class traceroute(base_resource) :
	def __init__(self) :
		self._S = None
		self._n = None
		self._r = None
		self._v = None
		self._M = None
		self._m = None
		self._P = None
		self._p = None
		self._q = None
		self._s = None
		self._T = None
		self._t = None
		self._w = None
		self._host = None
		self._packetlen = None
		self._response = None

	@property
	def S(self) :
		r"""Print a summary of how many probes were not answered for each hop.
		"""
		try :
			return self._S
		except Exception as e:
			raise e

	@S.setter
	def S(self, S) :
		r"""Print a summary of how many probes were not answered for each hop.
		"""
		try :
			self._S = S
		except Exception as e:
			raise e

	@property
	def n(self) :
		r"""Print hop addresses numerically instead of symbolically and numerically.
		"""
		try :
			return self._n
		except Exception as e:
			raise e

	@n.setter
	def n(self, n) :
		r"""Print hop addresses numerically instead of symbolically and numerically.
		"""
		try :
			self._n = n
		except Exception as e:
			raise e

	@property
	def r(self) :
		r"""Bypass normal routing tables and send directly to a host on an attached network. If the host is not on a directly attached network, an error is returned.
		"""
		try :
			return self._r
		except Exception as e:
			raise e

	@r.setter
	def r(self, r) :
		r"""Bypass normal routing tables and send directly to a host on an attached network. If the host is not on a directly attached network, an error is returned.
		"""
		try :
			self._r = r
		except Exception as e:
			raise e

	@property
	def v(self) :
		r"""Verbose output. List received ICMP packets other than TIME_EXCEEDED and UNREACHABLE.
		"""
		try :
			return self._v
		except Exception as e:
			raise e

	@v.setter
	def v(self, v) :
		r"""Verbose output. List received ICMP packets other than TIME_EXCEEDED and UNREACHABLE.
		"""
		try :
			self._v = v
		except Exception as e:
			raise e

	@property
	def M(self) :
		r"""Minimum TTL value used in outgoing probe packets.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._M
		except Exception as e:
			raise e

	@M.setter
	def M(self, M) :
		r"""Minimum TTL value used in outgoing probe packets.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._M = M
		except Exception as e:
			raise e

	@property
	def m(self) :
		r"""Maximum TTL value used in outgoing probe packets. For Nitro API, default value is taken as 10.<br/>Default value: 64<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._m
		except Exception as e:
			raise e

	@m.setter
	def m(self, m) :
		r"""Maximum TTL value used in outgoing probe packets. For Nitro API, default value is taken as 10.<br/>Default value: 64<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._m = m
		except Exception as e:
			raise e

	@property
	def P(self) :
		r"""Send packets of specified IP protocol. The currently supported protocols are UDP and ICMP.<br/>Minimum length =  1<br/>Maximum length =  20.
		"""
		try :
			return self._P
		except Exception as e:
			raise e

	@P.setter
	def P(self, P) :
		r"""Send packets of specified IP protocol. The currently supported protocols are UDP and ICMP.<br/>Minimum length =  1<br/>Maximum length =  20
		"""
		try :
			self._P = P
		except Exception as e:
			raise e

	@property
	def p(self) :
		r"""Base port number used in probes.<br/>Default value: 33434<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._p
		except Exception as e:
			raise e

	@p.setter
	def p(self, p) :
		r"""Base port number used in probes.<br/>Default value: 33434<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._p = p
		except Exception as e:
			raise e

	@property
	def q(self) :
		r"""Number of queries per hop. For Nitro API, defalut value is taken as 1.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._q
		except Exception as e:
			raise e

	@q.setter
	def q(self, q) :
		r"""Number of queries per hop. For Nitro API, defalut value is taken as 1.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._q = q
		except Exception as e:
			raise e

	@property
	def s(self) :
		r"""Source IP address to use in the outgoing query packets. If the IP address does not belong to this appliance,  an error is returned and nothing is sent.<br/>Minimum length =  1.
		"""
		try :
			return self._s
		except Exception as e:
			raise e

	@s.setter
	def s(self, s) :
		r"""Source IP address to use in the outgoing query packets. If the IP address does not belong to this appliance,  an error is returned and nothing is sent.<br/>Minimum length =  1
		"""
		try :
			self._s = s
		except Exception as e:
			raise e

	@property
	def T(self) :
		r"""Traffic Domain Id.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._T
		except Exception as e:
			raise e

	@T.setter
	def T(self, T) :
		r"""Traffic Domain Id.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._T = T
		except Exception as e:
			raise e

	@property
	def t(self) :
		r"""Type-of-service in query packets.<br/>Maximum length =  255.
		"""
		try :
			return self._t
		except Exception as e:
			raise e

	@t.setter
	def t(self, t) :
		r"""Type-of-service in query packets.<br/>Maximum length =  255
		"""
		try :
			self._t = t
		except Exception as e:
			raise e

	@property
	def w(self) :
		r"""Time (in seconds) to wait for a response to a query. For Nitro API, defalut value is set to 3.<br/>Default value: 5<br/>Minimum length =  2<br/>Maximum length =  86399.
		"""
		try :
			return self._w
		except Exception as e:
			raise e

	@w.setter
	def w(self, w) :
		r"""Time (in seconds) to wait for a response to a query. For Nitro API, defalut value is set to 3.<br/>Default value: 5<br/>Minimum length =  2<br/>Maximum length =  86399
		"""
		try :
			self._w = w
		except Exception as e:
			raise e

	@property
	def host(self) :
		r"""Destination host IP address or name.<br/>Minimum length =  1<br/>Maximum length =  64.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@host.setter
	def host(self, host) :
		r"""Destination host IP address or name.<br/>Minimum length =  1<br/>Maximum length =  64
		"""
		try :
			self._host = host
		except Exception as e:
			raise e

	@property
	def packetlen(self) :
		r"""Length (in bytes) of the query packets.<br/>Default value: 44<br/>Minimum length =  44<br/>Maximum length =  32768.
		"""
		try :
			return self._packetlen
		except Exception as e:
			raise e

	@packetlen.setter
	def packetlen(self, packetlen) :
		r"""Length (in bytes) of the query packets.<br/>Default value: 44<br/>Minimum length =  44<br/>Maximum length =  32768
		"""
		try :
			self._packetlen = packetlen
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(traceroute_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.traceroute
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
	def Traceroute(cls, client, resource) :
		r""" Use this API to Traceroute traceroute.
		"""
		try :
			if type(resource) is not list :
				Tracerouteresource = traceroute()
				Tracerouteresource.S = resource.S
				Tracerouteresource.n = resource.n
				Tracerouteresource.r = resource.r
				Tracerouteresource.v = resource.v
				Tracerouteresource.M = resource.M
				Tracerouteresource.m = resource.m
				Tracerouteresource.P = resource.P
				Tracerouteresource.p = resource.p
				Tracerouteresource.q = resource.q
				Tracerouteresource.s = resource.s
				Tracerouteresource.T = resource.T
				Tracerouteresource.t = resource.t
				Tracerouteresource.w = resource.w
				Tracerouteresource.host = resource.host
				Tracerouteresource.packetlen = resource.packetlen
				return Tracerouteresource.perform_operationEx(client)
		except Exception as e :
			raise e

class traceroute_response(base_response) :
	def __init__(self, length=1) :
		self.traceroute = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.traceroute = [traceroute() for _ in range(length)]

