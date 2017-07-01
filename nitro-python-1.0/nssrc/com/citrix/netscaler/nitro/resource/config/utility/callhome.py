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

class callhome(base_resource) :
	""" Configuration for callhome resource. """
	def __init__(self) :
		self._emailaddress = None
		self._hbcustominterval = None
		self._proxymode = None
		self._ipaddress = None
		self._proxyauthservice = None
		self._port = None
		self._sslcardfirstfailure = None
		self._sslcardlatestfailure = None
		self._powfirstfail = None
		self._powlatestfailure = None
		self._hddfirstfail = None
		self._hddlatestfailure = None
		self._flashfirstfail = None
		self._flashlatestfailure = None
		self._rlfirsthighdrop = None
		self._rllatesthighdrop = None
		self._restartlatestfail = None
		self._memthrefirstanomaly = None
		self._memthrelatestanomaly = None
		self._callhomestatus = []

	@property
	def emailaddress(self) :
		r"""Email address of the contact administrator.<br/>Maximum length =  78.
		"""
		try :
			return self._emailaddress
		except Exception as e:
			raise e

	@emailaddress.setter
	def emailaddress(self, emailaddress) :
		r"""Email address of the contact administrator.<br/>Maximum length =  78
		"""
		try :
			self._emailaddress = emailaddress
		except Exception as e:
			raise e

	@property
	def hbcustominterval(self) :
		r"""Interval (in days) between CallHome heartbeats.<br/>Minimum length =  1<br/>Maximum length =  30.
		"""
		try :
			return self._hbcustominterval
		except Exception as e:
			raise e

	@hbcustominterval.setter
	def hbcustominterval(self, hbcustominterval) :
		r"""Interval (in days) between CallHome heartbeats.<br/>Minimum length =  1<br/>Maximum length =  30
		"""
		try :
			self._hbcustominterval = hbcustominterval
		except Exception as e:
			raise e

	@property
	def proxymode(self) :
		r"""Enables or disables the proxy mode. The proxy server can be set by either specifying the IP address of the server or the name of the service representing the proxy server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._proxymode
		except Exception as e:
			raise e

	@proxymode.setter
	def proxymode(self, proxymode) :
		r"""Enables or disables the proxy mode. The proxy server can be set by either specifying the IP address of the server or the name of the service representing the proxy server.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._proxymode = proxymode
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""IP address of the proxy server.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""IP address of the proxy server.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def proxyauthservice(self) :
		r"""Name of the service that represents the proxy server.<br/>Maximum length =  128.
		"""
		try :
			return self._proxyauthservice
		except Exception as e:
			raise e

	@proxyauthservice.setter
	def proxyauthservice(self, proxyauthservice) :
		r"""Name of the service that represents the proxy server.<br/>Maximum length =  128
		"""
		try :
			self._proxyauthservice = proxyauthservice
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""HTTP port on the Proxy server. This is a mandatory parameter for both IP address and service name based configuration.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""HTTP port on the Proxy server. This is a mandatory parameter for both IP address and service name based configuration.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def sslcardfirstfailure(self) :
		r"""First occurrence SSL card failure.
		"""
		try :
			return self._sslcardfirstfailure
		except Exception as e:
			raise e

	@property
	def sslcardlatestfailure(self) :
		r"""Latest occurrence SSL card failure.
		"""
		try :
			return self._sslcardlatestfailure
		except Exception as e:
			raise e

	@property
	def powfirstfail(self) :
		r"""First occurrence power supply unit failure.
		"""
		try :
			return self._powfirstfail
		except Exception as e:
			raise e

	@property
	def powlatestfailure(self) :
		r"""Latest occurrence power supply unit failure.
		"""
		try :
			return self._powlatestfailure
		except Exception as e:
			raise e

	@property
	def hddfirstfail(self) :
		r"""First occurrence hard disk drive failure.
		"""
		try :
			return self._hddfirstfail
		except Exception as e:
			raise e

	@property
	def hddlatestfailure(self) :
		r"""Latest occurrence hard disk drive failure.
		"""
		try :
			return self._hddlatestfailure
		except Exception as e:
			raise e

	@property
	def flashfirstfail(self) :
		r"""First occurrence compact flash failure.
		"""
		try :
			return self._flashfirstfail
		except Exception as e:
			raise e

	@property
	def flashlatestfailure(self) :
		r"""Latest occurrence compact flush failure.
		"""
		try :
			return self._flashlatestfailure
		except Exception as e:
			raise e

	@property
	def rlfirsthighdrop(self) :
		r"""First occurence of high rate limit drops.
		"""
		try :
			return self._rlfirsthighdrop
		except Exception as e:
			raise e

	@property
	def rllatesthighdrop(self) :
		r"""Latest occurence of high rate limit drops.
		"""
		try :
			return self._rllatesthighdrop
		except Exception as e:
			raise e

	@property
	def restartlatestfail(self) :
		r"""Latest occurrence warm restart failure.
		"""
		try :
			return self._restartlatestfail
		except Exception as e:
			raise e

	@property
	def memthrefirstanomaly(self) :
		r"""First occurrence of memory anomaly.
		"""
		try :
			return self._memthrefirstanomaly
		except Exception as e:
			raise e

	@property
	def memthrelatestanomaly(self) :
		r"""Latest occurrence of memory anomaly.
		"""
		try :
			return self._memthrelatestanomaly
		except Exception as e:
			raise e

	@property
	def callhomestatus(self) :
		r"""Callhome feature enabled/disable, register with upload server successful/failed.<br/>Possible values = ENABLED, DISABLED, SUCCESSFUL, FAILED.
		"""
		try :
			return self._callhomestatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(callhome_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.callhome
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
		r""" Use this API to update callhome.
		"""
		try :
			if type(resource) is not list :
				updateresource = callhome()
				updateresource.emailaddress = resource.emailaddress
				updateresource.hbcustominterval = resource.hbcustominterval
				updateresource.proxymode = resource.proxymode
				updateresource.ipaddress = resource.ipaddress
				updateresource.proxyauthservice = resource.proxyauthservice
				updateresource.port = resource.port
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of callhome resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = callhome()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the callhome resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = callhome()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Callhomestatus:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"
		SUCCESSFUL = "SUCCESSFUL"
		FAILED = "FAILED"

	class Proxymode:
		YES = "YES"
		NO = "NO"

class callhome_response(base_response) :
	def __init__(self, length=1) :
		self.callhome = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.callhome = [callhome() for _ in range(length)]

