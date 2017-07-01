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

class traceroute6(base_resource) :
	def __init__(self) :
		self._n = None
		self._I = None
		self._r = None
		self._v = None
		self._m = None
		self._p = None
		self._q = None
		self._s = None
		self._T = None
		self._w = None
		self._host = None
		self._packetlen = None
		self._response = None

	@property
	def n(self) :
		r"""Print hop addresses numerically rather than symbolically and numerically.
		"""
		try :
			return self._n
		except Exception as e:
			raise e

	@n.setter
	def n(self, n) :
		r"""Print hop addresses numerically rather than symbolically and numerically.
		"""
		try :
			self._n = n
		except Exception as e:
			raise e

	@property
	def I(self) :
		r"""Use ICMP ECHO for probes.
		"""
		try :
			return self._I
		except Exception as e:
			raise e

	@I.setter
	def I(self, I) :
		r"""Use ICMP ECHO for probes.
		"""
		try :
			self._I = I
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
	def m(self) :
		r"""Maximum hop value for outgoing probe packets. For Nitro API, default value is taken as 10.<br/>Default value: 64<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._m
		except Exception as e:
			raise e

	@m.setter
	def m(self, m) :
		r"""Maximum hop value for outgoing probe packets. For Nitro API, default value is taken as 10.<br/>Default value: 64<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._m = m
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
		r"""Number of probes per hop. For Nitro API, default value is taken as 1.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._q
		except Exception as e:
			raise e

	@q.setter
	def q(self, q) :
		r"""Number of probes per hop. For Nitro API, default value is taken as 1.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  65535
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
		r"""Destination host IP address or name.<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@host.setter
	def host(self, host) :
		r"""Destination host IP address or name.<br/>Minimum length =  1<br/>Maximum length =  256
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
			result = service.payload_formatter.string_to_resource(traceroute6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.traceroute6
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
	def Traceroute6(cls, client, resource) :
		r""" Use this API to Traceroute6 traceroute6.
		"""
		try :
			if type(resource) is not list :
				Traceroute6resource = traceroute6()
				Traceroute6resource.n = resource.n
				Traceroute6resource.I = resource.I
				Traceroute6resource.r = resource.r
				Traceroute6resource.v = resource.v
				Traceroute6resource.m = resource.m
				Traceroute6resource.p = resource.p
				Traceroute6resource.q = resource.q
				Traceroute6resource.s = resource.s
				Traceroute6resource.T = resource.T
				Traceroute6resource.w = resource.w
				Traceroute6resource.host = resource.host
				Traceroute6resource.packetlen = resource.packetlen
				return Traceroute6resource.perform_operationEx(client)
		except Exception as e :
			raise e

class traceroute6_response(base_response) :
	def __init__(self, length=1) :
		self.traceroute6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.traceroute6 = [traceroute6() for _ in range(length)]

