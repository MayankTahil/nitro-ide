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

class ping(base_resource) :
	def __init__(self) :
		self._c = None
		self._i = None
		self._I = None
		self._n = None
		self._p = None
		self._q = None
		self._s = None
		self._S = None
		self._T = None
		self._t = None
		self._hostName = None
		self._response = None

	@property
	def c(self) :
		r"""Number of packets to send. The default value is infinite. For Nitro API, defalut value is taken as 5.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._c
		except Exception as e:
			raise e

	@c.setter
	def c(self, c) :
		r"""Number of packets to send. The default value is infinite. For Nitro API, defalut value is taken as 5.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._c = c
		except Exception as e:
			raise e

	@property
	def i(self) :
		r"""Waiting time, in seconds. The default value is 1 second.<br/>Maximum length =  65535.
		"""
		try :
			return self._i
		except Exception as e:
			raise e

	@i.setter
	def i(self, i) :
		r"""Waiting time, in seconds. The default value is 1 second.<br/>Maximum length =  65535
		"""
		try :
			self._i = i
		except Exception as e:
			raise e

	@property
	def I(self) :
		r"""Network interface on which to ping, if you have multiple interfaces.<br/>Minimum length =  1<br/>Maximum length =  15.
		"""
		try :
			return self._I
		except Exception as e:
			raise e

	@I.setter
	def I(self, I) :
		r"""Network interface on which to ping, if you have multiple interfaces.<br/>Minimum length =  1<br/>Maximum length =  15
		"""
		try :
			self._I = I
		except Exception as e:
			raise e

	@property
	def n(self) :
		r"""Numeric output only. No name resolution.
		"""
		try :
			return self._n
		except Exception as e:
			raise e

	@n.setter
	def n(self, n) :
		r"""Numeric output only. No name resolution.
		"""
		try :
			self._n = n
		except Exception as e:
			raise e

	@property
	def p(self) :
		r"""Pattern to fill in packets.  Can be up to 16 bytes, useful for diagnosing data-dependent problems.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._p
		except Exception as e:
			raise e

	@p.setter
	def p(self, p) :
		r"""Pattern to fill in packets.  Can be up to 16 bytes, useful for diagnosing data-dependent problems.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._p = p
		except Exception as e:
			raise e

	@property
	def q(self) :
		r"""Quiet output. Only the summary is printed. For Nitro API, this flag is set by default.
		"""
		try :
			return self._q
		except Exception as e:
			raise e

	@q.setter
	def q(self, q) :
		r"""Quiet output. Only the summary is printed. For Nitro API, this flag is set by default.
		"""
		try :
			self._q = q
		except Exception as e:
			raise e

	@property
	def s(self) :
		r"""Data size, in bytes. The default value is 56.<br/>Maximum length =  65507.
		"""
		try :
			return self._s
		except Exception as e:
			raise e

	@s.setter
	def s(self, s) :
		r"""Data size, in bytes. The default value is 56.<br/>Maximum length =  65507
		"""
		try :
			self._s = s
		except Exception as e:
			raise e

	@property
	def S(self) :
		r"""Source IP address to be used in the outgoing query packets. If the IP addrESS does not belongs to this appliance, an error is returned and nothing is sent.<br/>Minimum length =  1.
		"""
		try :
			return self._S
		except Exception as e:
			raise e

	@S.setter
	def S(self, S) :
		r"""Source IP address to be used in the outgoing query packets. If the IP addrESS does not belongs to this appliance, an error is returned and nothing is sent.<br/>Minimum length =  1
		"""
		try :
			self._S = S
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
		r"""Time-out, in seconds, before ping exits.<br/>Minimum length =  1<br/>Maximum length =  3600.
		"""
		try :
			return self._t
		except Exception as e:
			raise e

	@t.setter
	def t(self, t) :
		r"""Time-out, in seconds, before ping exits.<br/>Minimum length =  1<br/>Maximum length =  3600
		"""
		try :
			self._t = t
		except Exception as e:
			raise e

	@property
	def hostName(self) :
		r"""Address of host to ping.<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._hostName
		except Exception as e:
			raise e

	@hostName.setter
	def hostName(self, hostName) :
		r"""Address of host to ping.<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._hostName = hostName
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
			result = service.payload_formatter.string_to_resource(ping_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ping
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
	def Ping(cls, client, resource) :
		r""" Use this API to Ping ping.
		"""
		try :
			if type(resource) is not list :
				Pingresource = ping()
				Pingresource.c = resource.c
				Pingresource.i = resource.i
				Pingresource.I = resource.I
				Pingresource.n = resource.n
				Pingresource.p = resource.p
				Pingresource.q = resource.q
				Pingresource.s = resource.s
				Pingresource.S = resource.S
				Pingresource.T = resource.T
				Pingresource.t = resource.t
				Pingresource.hostName = resource.hostName
				return Pingresource.perform_operationEx(client)
		except Exception as e :
			raise e

class ping_response(base_response) :
	def __init__(self, length=1) :
		self.ping = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ping = [ping() for _ in range(length)]

