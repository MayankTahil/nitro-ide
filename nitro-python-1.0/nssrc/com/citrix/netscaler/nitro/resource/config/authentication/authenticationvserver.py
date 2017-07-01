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

class authenticationvserver(base_resource) :
	""" Configuration for authentication virtual server resource. """
	def __init__(self) :
		self._name = None
		self._servicetype = None
		self._ipv46 = None
		self._range = None
		self._port = None
		self._state = None
		self._authentication = None
		self._authenticationdomain = None
		self._comment = None
		self._td = None
		self._appflowlog = None
		self._maxloginattempts = None
		self._failedlogintimeout = None
		self._newname = None
		self._ip = None
		self._value = None
		self._type = None
		self._curstate = None
		self._status = None
		self._cachetype = None
		self._redirect = None
		self._precedence = None
		self._redirecturl = None
		self._curaaausers = None
		self._rule = None
		self._policy = None
		self._servicename = None
		self._weight = None
		self._cachevserver = None
		self._backupvserver = None
		self._clttimeout = None
		self._somethod = None
		self._sothreshold = None
		self._sopersistence = None
		self._sopersistencetimeout = None
		self._priority = None
		self._downstateflush = None
		self._disableprimaryondown = None
		self._listenpolicy = None
		self._listenpriority = None
		self._tcpprofilename = None
		self._httpprofilename = None
		self._vstype = None
		self._ngname = None
		self._secondary = None
		self._groupextraction = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the new authentication virtual server. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the authentication virtual server is added by using the rename authentication vserver command.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the new authentication virtual server. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the authentication virtual server is added by using the rename authentication vserver command.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy" or 'my authentication policy').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol type of the authentication virtual server. Always SSL.<br/>Default value: SSL<br/>Possible values = SSL.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol type of the authentication virtual server. Always SSL.<br/>Default value: SSL<br/>Possible values = SSL
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		r"""IP address of the authentication virtual server, if a single IP address is assigned to the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@ipv46.setter
	def ipv46(self, ipv46) :
		r"""IP address of the authentication virtual server, if a single IP address is assigned to the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._ipv46 = ipv46
		except Exception as e:
			raise e

	@property
	def range(self) :
		r"""If you are creating a series of virtual servers with a range of IP addresses assigned to them, the length of the range. 
		The new range of authentication virtual servers will have IP addresses consecutively numbered, starting with the primary address specified with the IP Address parameter.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@range.setter
	def range(self, range) :
		r"""If you are creating a series of virtual servers with a range of IP addresses assigned to them, the length of the range. 
		The new range of authentication virtual servers will have IP addresses consecutively numbered, starting with the primary address specified with the IP Address parameter.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._range = range
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""TCP port on which the virtual server accepts connections.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""TCP port on which the virtual server accepts connections.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the new virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the new virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		r"""Require users to be authenticated before sending traffic through this virtual server.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		r"""Require users to be authenticated before sending traffic through this virtual server.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def authenticationdomain(self) :
		r"""The domain of the authentication cookie set by Authentication vserver.<br/>Minimum length =  3<br/>Maximum length =  252.
		"""
		try :
			return self._authenticationdomain
		except Exception as e:
			raise e

	@authenticationdomain.setter
	def authenticationdomain(self, authenticationdomain) :
		r"""The domain of the authentication cookie set by Authentication vserver.<br/>Minimum length =  3<br/>Maximum length =  252
		"""
		try :
			self._authenticationdomain = authenticationdomain
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments associated with this virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments associated with this virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Log AppFlow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Log AppFlow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def maxloginattempts(self) :
		r"""Maximum Number of login Attempts.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._maxloginattempts
		except Exception as e:
			raise e

	@maxloginattempts.setter
	def maxloginattempts(self, maxloginattempts) :
		r"""Maximum Number of login Attempts.<br/>Minimum length =  1<br/>Maximum length =  255
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
	def newname(self) :
		r"""New name of the authentication virtual server. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, 'my authentication policy' or "my authentication policy").<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name of the authentication virtual server. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, 'my authentication policy' or "my authentication policy").<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""The Virtual IP address of the authentication vserver.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def value(self) :
		r"""Indicates whether or not the certificate is bound or if SSL offload is disabled.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""The type of Virtual Server, e.g. CONTENT based or ADDRESS based.<br/>Possible values = CONTENT, ADDRESS.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""The current state of the Virtual server, e.g. UP, DOWN, BUSY, etc.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Whether or not this vserver responds to ARPs and whether or not round-robin selection is temporarily in effect.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		r"""Virtual server's cache type. The options are: TRANSPARENT, REVERSE and FORWARD.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@property
	def redirect(self) :
		r"""The cache redirect policy.
		The valid redirect policies are:
		l.	CACHE - Directs all requests to the cache.
		2.	POLICY - Applies cache redirection policy to determine whether the request should be directed to the cache or origin. This is the default setting.
		3.	ORIGIN - Directs all requests to the origin server.<br/>Possible values = CACHE, POLICY, ORIGIN.
		"""
		try :
			return self._redirect
		except Exception as e:
			raise e

	@property
	def precedence(self) :
		r"""This argument is used only when configuring content switching on the specified virtual server. This is applicable only
		if both the URL and RULE-based policies have been configured on the same virtual server.
		It specifies the type of policy (URL or RULE) that takes precedence on the content switching virtual server. The default setting is RULE.
		l	URL - In this case, the incoming request is matched against the URL-based policies before the rule-based policies.
		l	RULE - In this case, the incoming request is matched against the rule-based policies before the URL-based policies.
		For all URL-based policies, the precedence hierarchy is:
		1.	Domain and exact URL
		2.	Domain, prefix and suffix
		3.	Domain and suffix
		4.	Domain and prefix
		5.	Domain only
		6.	Exact URL
		7.	Prefix and suffix
		8.	Suffix only
		9.	Prefix only
		10.	Default.<br/>Possible values = RULE, URL.
		"""
		try :
			return self._precedence
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		r"""The URL where traffic is redirected if the virtual server in system becomes unavailable. WARNING!	Make sure that the domain you specify in the URL does not match the domain specified in the -d domainName argument of the ###add cs policy### command. If the same domain is specified in both arguments, the request will be continuously redirected to the same unavailable virtual server in the system. If so, the user may not get the requested content.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@property
	def curaaausers(self) :
		r"""The number of current users logged in to this vserver.
		"""
		try :
			return self._curaaausers
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""The name of the rule, or expression, if any, that policy for the authentication server is to use. Rules are combinations of Expressions. Expressions are simple conditions, such as a test for equality, applied to operands, such as a URL string or an IP address. Expression syntax is described in the Installation and Configuration Guide. The default rule is ns_true.
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""The name of the policy, if any, bound to the authentication vserver.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""The name of the service, if any, to which the vserver policy is bound.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight for this service, if any. This weight is used when the system performs load balancing, giving greater priority to a specific service. It is useful when the services bound to a virtual server are of different capacity.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@property
	def cachevserver(self) :
		r"""The name of the default target cache virtual server, if any, to which requests are redirected.
		"""
		try :
			return self._cachevserver
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		r"""The name of the backup vpn virtual server for this vpn virtual server.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""The idle time, if any, in seconds after which the client connection is terminated.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		r"""VPN client applications are allocated from a block of Intranet IP addresses.
		That block may be exhausted after a certain number of connections. This switch specifies the
		method used to determine whether or not a new connection will spillover, or exhaust, the allocated block of
		Intranet IP addresses for that application. Possible values are CONNECTION or DYNAMICCONNECTION.
		CONNECTION means that a static integer value is the hard limit for the spillover threshold. The spillover
		threshold is described below. DYNAMICCONNECTION means that the spillover threshold is set according to
		the maximum number of connections defined for the vpn vserver.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		r"""VPN client applications are allocated from a block of Intranet IP addresses.
		That block may be exhausted after a certain number of connections.
		The value of this option is number of client connections after which the Mapped IP address is used
		as the client source IP address instead of an address from the allocated block of Intranet IP addresses.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		r"""Whether or not cookie-based site persistance is enabled for this VPN vserver. Possible values are 'ConnectionProxy', HTTPRedirect, or NONE.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		r"""The timeout, if any, for cookie-based site persistance of this VPN vserver.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""The priority, if any, of the vpn vserver policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		r"""Perform delayed clean up of connections on this vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		r"""Tells whether traffic will continue reaching backup vservers even after primary comes UP from DOWN state.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@property
	def listenpolicy(self) :
		r"""Listenpolicy configured for authentication vserver.
		"""
		try :
			return self._listenpolicy
		except Exception as e:
			raise e

	@property
	def listenpriority(self) :
		r"""Priority of listen policy for authentication vserver.
		"""
		try :
			return self._listenpriority
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		r"""The name of the TCP profile.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		r"""Name of the HTTP profile.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@property
	def vstype(self) :
		r"""Virtual Server Type, e.g. Load Balancing, Content Switch, Cache Redirection.
		"""
		try :
			return self._vstype
		except Exception as e:
			raise e

	@property
	def ngname(self) :
		r"""Nodegroup devno to which this  authentication vsever belongs to.
		"""
		try :
			return self._ngname
		except Exception as e:
			raise e

	@property
	def secondary(self) :
		r"""Bind the authentication policy to the secondary chain.
		Provides for multifactor authentication in which a user must authenticate via both a primary authentication method and, afterward, via a secondary authentication method.
		Because user groups are aggregated across authentication systems, usernames must be the same on all authentication servers. Passwords can be different.
		"""
		try :
			return self._secondary
		except Exception as e:
			raise e

	@property
	def groupextraction(self) :
		r"""Bind the Authentication policy to a tertiary chain which will be used only for group extraction.  The user will not authenticate against this server, and this will only be called if primary and/or secondary authentication has succeeded.
		"""
		try :
			return self._groupextraction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationvserver()
				addresource.name = resource.name
				addresource.servicetype = resource.servicetype
				addresource.ipv46 = resource.ipv46
				addresource.range = resource.range
				addresource.port = resource.port
				addresource.state = resource.state
				addresource.authentication = resource.authentication
				addresource.authenticationdomain = resource.authenticationdomain
				addresource.comment = resource.comment
				addresource.td = resource.td
				addresource.appflowlog = resource.appflowlog
				addresource.maxloginattempts = resource.maxloginattempts
				addresource.failedlogintimeout = resource.failedlogintimeout
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].servicetype = resource[i].servicetype
						addresources[i].ipv46 = resource[i].ipv46
						addresources[i].range = resource[i].range
						addresources[i].port = resource[i].port
						addresources[i].state = resource[i].state
						addresources[i].authentication = resource[i].authentication
						addresources[i].authenticationdomain = resource[i].authenticationdomain
						addresources[i].comment = resource[i].comment
						addresources[i].td = resource[i].td
						addresources[i].appflowlog = resource[i].appflowlog
						addresources[i].maxloginattempts = resource[i].maxloginattempts
						addresources[i].failedlogintimeout = resource[i].failedlogintimeout
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationvserver()
				updateresource.name = resource.name
				updateresource.ipv46 = resource.ipv46
				updateresource.authentication = resource.authentication
				updateresource.authenticationdomain = resource.authenticationdomain
				updateresource.comment = resource.comment
				updateresource.appflowlog = resource.appflowlog
				updateresource.maxloginattempts = resource.maxloginattempts
				updateresource.failedlogintimeout = resource.failedlogintimeout
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].ipv46 = resource[i].ipv46
						updateresources[i].authentication = resource[i].authentication
						updateresources[i].authenticationdomain = resource[i].authenticationdomain
						updateresources[i].comment = resource[i].comment
						updateresources[i].appflowlog = resource[i].appflowlog
						updateresources[i].maxloginattempts = resource[i].maxloginattempts
						updateresources[i].failedlogintimeout = resource[i].failedlogintimeout
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable authenticationvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = authenticationvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable authenticationvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = authenticationvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ authenticationvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a authenticationvserver resource.
		"""
		try :
			renameresource = authenticationvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationvserver()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationvserver() for _ in range(len(name))]
						obj = [authenticationvserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationvserver()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationvserver resources configured on NetScaler.
		"""
		try :
			obj = authenticationvserver()
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
		r""" Use this API to count filtered the set of authenticationvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Authentication:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachetype:
		TRANSPARENT = "TRANSPARENT"
		REVERSE = "REVERSE"
		FORWARD = "FORWARD"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		SSL = "SSL"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Type:
		CONTENT = "CONTENT"
		ADDRESS = "ADDRESS"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirect:
		CACHE = "CACHE"
		POLICY = "POLICY"
		ORIGIN = "ORIGIN"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Precedence:
		RULE = "RULE"
		URL = "URL"

	class Curstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class authenticationvserver_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationvserver = [authenticationvserver() for _ in range(length)]

