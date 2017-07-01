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

class aaaparameter(base_resource) :
	""" Configuration for AAA parameter resource. """
	def __init__(self) :
		self._enablestaticpagecaching = None
		self._enableenhancedauthfeedback = None
		self._defaultauthtype = None
		self._maxaaausers = None
		self._maxloginattempts = None
		self._failedlogintimeout = None
		self._aaadnatip = None
		self._enablesessionstickiness = None
		self._aaasessionloglevel = None
		self._aaadloglevel = None
		self._dynaddr = None
		self._ftmode = None

	@property
	def enablestaticpagecaching(self) :
		r"""The default state of VPN Static Page caching. If nothing is specified, the default value is set to YES.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablestaticpagecaching
		except Exception as e:
			raise e

	@enablestaticpagecaching.setter
	def enablestaticpagecaching(self, enablestaticpagecaching) :
		r"""The default state of VPN Static Page caching. If nothing is specified, the default value is set to YES.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._enablestaticpagecaching = enablestaticpagecaching
		except Exception as e:
			raise e

	@property
	def enableenhancedauthfeedback(self) :
		r"""Enhanced auth feedback provides more information to the end user about the reason for an authentication failure.  The default value is set to NO.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enableenhancedauthfeedback
		except Exception as e:
			raise e

	@enableenhancedauthfeedback.setter
	def enableenhancedauthfeedback(self, enableenhancedauthfeedback) :
		r"""Enhanced auth feedback provides more information to the end user about the reason for an authentication failure.  The default value is set to NO.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enableenhancedauthfeedback = enableenhancedauthfeedback
		except Exception as e:
			raise e

	@property
	def defaultauthtype(self) :
		r"""The default authentication server type.<br/>Default value: LOCAL<br/>Possible values = LOCAL, LDAP, RADIUS, TACACS, CERT.
		"""
		try :
			return self._defaultauthtype
		except Exception as e:
			raise e

	@defaultauthtype.setter
	def defaultauthtype(self, defaultauthtype) :
		r"""The default authentication server type.<br/>Default value: LOCAL<br/>Possible values = LOCAL, LDAP, RADIUS, TACACS, CERT
		"""
		try :
			self._defaultauthtype = defaultauthtype
		except Exception as e:
			raise e

	@property
	def maxaaausers(self) :
		r"""Maximum number of concurrent users allowed to log on to VPN simultaneously.<br/>Minimum length =  1.
		"""
		try :
			return self._maxaaausers
		except Exception as e:
			raise e

	@maxaaausers.setter
	def maxaaausers(self, maxaaausers) :
		r"""Maximum number of concurrent users allowed to log on to VPN simultaneously.<br/>Minimum length =  1
		"""
		try :
			self._maxaaausers = maxaaausers
		except Exception as e:
			raise e

	@property
	def maxloginattempts(self) :
		r"""Maximum Number of login Attempts.<br/>Minimum length =  1.
		"""
		try :
			return self._maxloginattempts
		except Exception as e:
			raise e

	@maxloginattempts.setter
	def maxloginattempts(self, maxloginattempts) :
		r"""Maximum Number of login Attempts.<br/>Minimum length =  1
		"""
		try :
			self._maxloginattempts = maxloginattempts
		except Exception as e:
			raise e

	@property
	def failedlogintimeout(self) :
		r"""Number of minutes an account will be locked if user exceeds maximum permissible attempts.<br/>Minimum length =  1.
		"""
		try :
			return self._failedlogintimeout
		except Exception as e:
			raise e

	@failedlogintimeout.setter
	def failedlogintimeout(self, failedlogintimeout) :
		r"""Number of minutes an account will be locked if user exceeds maximum permissible attempts.<br/>Minimum length =  1
		"""
		try :
			self._failedlogintimeout = failedlogintimeout
		except Exception as e:
			raise e

	@property
	def aaadnatip(self) :
		r"""Source IP address to use for traffic that is sent to the authentication server.
		"""
		try :
			return self._aaadnatip
		except Exception as e:
			raise e

	@aaadnatip.setter
	def aaadnatip(self, aaadnatip) :
		r"""Source IP address to use for traffic that is sent to the authentication server.
		"""
		try :
			self._aaadnatip = aaadnatip
		except Exception as e:
			raise e

	@property
	def enablesessionstickiness(self) :
		r"""Enables/Disables stickiness to authentication servers.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablesessionstickiness
		except Exception as e:
			raise e

	@enablesessionstickiness.setter
	def enablesessionstickiness(self, enablesessionstickiness) :
		r"""Enables/Disables stickiness to authentication servers.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enablesessionstickiness = enablesessionstickiness
		except Exception as e:
			raise e

	@property
	def aaasessionloglevel(self) :
		r"""Audit log level, which specifies the types of events to log for cli executed commands. 
		Available values function as follows: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: DEFAULT_LOGLEVEL_AAA<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._aaasessionloglevel
		except Exception as e:
			raise e

	@aaasessionloglevel.setter
	def aaasessionloglevel(self, aaasessionloglevel) :
		r"""Audit log level, which specifies the types of events to log for cli executed commands. 
		Available values function as follows: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: DEFAULT_LOGLEVEL_AAA<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._aaasessionloglevel = aaasessionloglevel
		except Exception as e:
			raise e

	@property
	def aaadloglevel(self) :
		r"""AAAD log level, which specifies the types of AAAD events to log in nsvpn.log. 
		Available values function as follows: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._aaadloglevel
		except Exception as e:
			raise e

	@aaadloglevel.setter
	def aaadloglevel(self, aaadloglevel) :
		r"""AAAD log level, which specifies the types of AAAD events to log in nsvpn.log. 
		Available values function as follows: 
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._aaadloglevel = aaadloglevel
		except Exception as e:
			raise e

	@property
	def dynaddr(self) :
		r"""Set by the DHCP client when the IP address was fetched dynamically.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._dynaddr
		except Exception as e:
			raise e

	@dynaddr.setter
	def dynaddr(self, dynaddr) :
		r"""Set by the DHCP client when the IP address was fetched dynamically.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._dynaddr = dynaddr
		except Exception as e:
			raise e

	@property
	def ftmode(self) :
		r"""First time user mode determines which configuration options are shown by default when logging in to the GUI. This setting is controlled by the GUI.<br/>Default value: ON<br/>Possible values = ON, HA, OFF.
		"""
		try :
			return self._ftmode
		except Exception as e:
			raise e

	@ftmode.setter
	def ftmode(self, ftmode) :
		r"""First time user mode determines which configuration options are shown by default when logging in to the GUI. This setting is controlled by the GUI.<br/>Default value: ON<br/>Possible values = ON, HA, OFF
		"""
		try :
			self._ftmode = ftmode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaaparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaaparameter
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
		r""" Use this API to update aaaparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = aaaparameter()
				updateresource.enablestaticpagecaching = resource.enablestaticpagecaching
				updateresource.enableenhancedauthfeedback = resource.enableenhancedauthfeedback
				updateresource.defaultauthtype = resource.defaultauthtype
				updateresource.maxaaausers = resource.maxaaausers
				updateresource.maxloginattempts = resource.maxloginattempts
				updateresource.failedlogintimeout = resource.failedlogintimeout
				updateresource.aaadnatip = resource.aaadnatip
				updateresource.enablesessionstickiness = resource.enablesessionstickiness
				updateresource.aaasessionloglevel = resource.aaasessionloglevel
				updateresource.aaadloglevel = resource.aaadloglevel
				updateresource.dynaddr = resource.dynaddr
				updateresource.ftmode = resource.ftmode
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of aaaparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaaparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaaparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaaparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Aaasessionloglevel:
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

	class Aaadloglevel:
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

	class Defaultauthtype:
		LOCAL = "LOCAL"
		LDAP = "LDAP"
		RADIUS = "RADIUS"
		TACACS = "TACACS"
		CERT = "CERT"

	class Ftmode:
		ON = "ON"
		HA = "HA"
		OFF = "OFF"

	class Dynaddr:
		ON = "ON"
		OFF = "OFF"

	class Enableenhancedauthfeedback:
		YES = "YES"
		NO = "NO"

	class Enablestaticpagecaching:
		YES = "YES"
		NO = "NO"

	class Enablesessionstickiness:
		YES = "YES"
		NO = "NO"

class aaaparameter_response(base_response) :
	def __init__(self, length=1) :
		self.aaaparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaaparameter = [aaaparameter() for _ in range(length)]

