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

class sslservicegroup(base_resource) :
	""" Configuration for SSL service group resource. """
	def __init__(self) :
		self._servicegroupname = None
		self._sslprofile = None
		self._sessreuse = None
		self._sesstimeout = None
		self._ssl3 = None
		self._tls1 = None
		self._tls11 = None
		self._tls12 = None
		self._snienable = None
		self._ocspstapling = None
		self._serverauth = None
		self._commonname = None
		self._sendclosenotify = None
		self._strictsigdigestcheck = None
		self._dh = None
		self._dhfile = None
		self._dhcount = None
		self._dhkeyexpsizelimit = None
		self._ersa = None
		self._ersacount = None
		self._cipherredirect = None
		self._cipherurl = None
		self._sslv2redirect = None
		self._sslv2url = None
		self._clientauth = None
		self._clientcert = None
		self._sslredirect = None
		self._redirectportrewrite = None
		self._nonfipsciphers = None
		self._ssl2 = None
		self._ocspcheck = None
		self._crlcheck = None
		self._cleartextport = None
		self._servicename = None
		self._ca = None
		self._snicert = None
		self.___count = 0

	@property
	def servicegroupname(self) :
		r"""Name of the SSL service group for which to set advanced configuration.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the SSL service group for which to set advanced configuration.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def sslprofile(self) :
		r"""Name of the SSL profile that contains SSL settings for the Service Group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sslprofile
		except Exception as e:
			raise e

	@sslprofile.setter
	def sslprofile(self, sslprofile) :
		r"""Name of the SSL profile that contains SSL settings for the Service Group.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sslprofile = sslprofile
		except Exception as e:
			raise e

	@property
	def sessreuse(self) :
		r"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessreuse
		except Exception as e:
			raise e

	@sessreuse.setter
	def sessreuse(self, sessreuse) :
		r"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessreuse = sessreuse
		except Exception as e:
			raise e

	@property
	def sesstimeout(self) :
		r"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 300<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		r"""Time, in seconds, for which to keep the session active. Any session resumption request received after the timeout period will require a fresh SSL handshake and establishment of a new SSL session.<br/>Default value: 300<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def ssl3(self) :
		r"""State of SSLv3 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl3
		except Exception as e:
			raise e

	@ssl3.setter
	def ssl3(self, ssl3) :
		r"""State of SSLv3 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl3 = ssl3
		except Exception as e:
			raise e

	@property
	def tls1(self) :
		r"""State of TLSv1.0 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls1
		except Exception as e:
			raise e

	@tls1.setter
	def tls1(self, tls1) :
		r"""State of TLSv1.0 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls1 = tls1
		except Exception as e:
			raise e

	@property
	def tls11(self) :
		r"""State of TLSv1.1 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls11
		except Exception as e:
			raise e

	@tls11.setter
	def tls11(self, tls11) :
		r"""State of TLSv1.1 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls11 = tls11
		except Exception as e:
			raise e

	@property
	def tls12(self) :
		r"""State of TLSv1.2 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls12
		except Exception as e:
			raise e

	@tls12.setter
	def tls12(self, tls12) :
		r"""State of TLSv1.2 protocol support for the SSL service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls12 = tls12
		except Exception as e:
			raise e

	@property
	def snienable(self) :
		r"""State of the Server Name Indication (SNI) feature on the service. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snienable
		except Exception as e:
			raise e

	@snienable.setter
	def snienable(self, snienable) :
		r"""State of the Server Name Indication (SNI) feature on the service. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snienable = snienable
		except Exception as e:
			raise e

	@property
	def ocspstapling(self) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ocspstapling
		except Exception as e:
			raise e

	@ocspstapling.setter
	def ocspstapling(self, ocspstapling) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ocspstapling = ocspstapling
		except Exception as e:
			raise e

	@property
	def serverauth(self) :
		r"""State of server authentication support for the SSL service group.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._serverauth
		except Exception as e:
			raise e

	@serverauth.setter
	def serverauth(self, serverauth) :
		r"""State of server authentication support for the SSL service group.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._serverauth = serverauth
		except Exception as e:
			raise e

	@property
	def commonname(self) :
		r"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1.
		"""
		try :
			return self._commonname
		except Exception as e:
			raise e

	@commonname.setter
	def commonname(self, commonname) :
		r"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1
		"""
		try :
			self._commonname = commonname
		except Exception as e:
			raise e

	@property
	def sendclosenotify(self) :
		r"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._sendclosenotify
		except Exception as e:
			raise e

	@sendclosenotify.setter
	def sendclosenotify(self, sendclosenotify) :
		r"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._sendclosenotify = sendclosenotify
		except Exception as e:
			raise e

	@property
	def strictsigdigestcheck(self) :
		r"""Parameter indicating to check whether peer's certificate is signed with one of signature-hash combination supported by Netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._strictsigdigestcheck
		except Exception as e:
			raise e

	@strictsigdigestcheck.setter
	def strictsigdigestcheck(self, strictsigdigestcheck) :
		r"""Parameter indicating to check whether peer's certificate is signed with one of signature-hash combination supported by Netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._strictsigdigestcheck = strictsigdigestcheck
		except Exception as e:
			raise e

	@property
	def dh(self) :
		r"""The state of DH key exchange support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dh
		except Exception as e:
			raise e

	@property
	def dhfile(self) :
		r"""The  file name and path for the DH parameter.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@property
	def dhcount(self) :
		r"""The  refresh  count  for  the re-generation of DH public-key and private-key from the DH parameter.<br/>Minimum value =  0<br/>Maximum value =  65534.
		"""
		try :
			return self._dhcount
		except Exception as e:
			raise e

	@property
	def dhkeyexpsizelimit(self) :
		r"""This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dhkeyexpsizelimit
		except Exception as e:
			raise e

	@property
	def ersa(self) :
		r"""The state of Ephemeral RSA key exchange support for the SSL service group.Ephemeral RSA is used for export ciphers.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ersa
		except Exception as e:
			raise e

	@property
	def ersacount(self) :
		r"""The  refresh  count  for the re-generation of RSA public-key and private-key pair.<br/>Minimum value =  0<br/>Maximum value =  65534.
		"""
		try :
			return self._ersacount
		except Exception as e:
			raise e

	@property
	def cipherredirect(self) :
		r"""The state of Cipher Redirect feature. Cipher Redirect feature can be used to provide more readable information to SSL clients about mismatch in ciphers between the client and the SSL vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipherredirect
		except Exception as e:
			raise e

	@property
	def cipherurl(self) :
		r"""The redirect URL to be used with the  Cipher  Redirect  feature.
		"""
		try :
			return self._cipherurl
		except Exception as e:
			raise e

	@property
	def sslv2redirect(self) :
		r"""The state of SSLv2 Redirect feature.SSLv2 Redirect feature can be used to provide more readable information to SSL client about non-support of SSLv2 protocol on the SSL vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslv2redirect
		except Exception as e:
			raise e

	@property
	def sslv2url(self) :
		r"""The  redirect URL to be used with SSLv2 Redirect feature.
		"""
		try :
			return self._sslv2url
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		r"""The state of Client-Authentication support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		r"""The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@property
	def sslredirect(self) :
		r"""The state of HTTPS redirects for the SSL service group.
		This is required for the proper functioning of the redirect messages from the server. The redirect message from the server provides the new location for the moved object. This is contained in the HTTP header field: Location, e.g. Location: http://www.moved.org/here.html
		For the SSL session, if the client browser receives this message, the browser will try to connect to the new location. This will break the secure SSL session, as the object has moved from a secure site (https://) to an un-secure one (http://). Generally browsers flash a warning message on the screen and prompt the user, either to continue or disconnect.
		The above feature, when enabled will automatically convert all such http:// redirect message to https://. This will not break the client SSL session.
		Note: The set ssl service command can be used for configuring a front-end SSL service for service based SSL Off-Loading, or a backend SSL service for backend-encryption setup.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslredirect
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		r"""The state of port-rewrite feature.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@property
	def nonfipsciphers(self) :
		r"""The state of usage of non FIPS approved ciphers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nonfipsciphers
		except Exception as e:
			raise e

	@property
	def ssl2(self) :
		r"""The  state of SSLv2 protocol support for the SSL service group.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl2
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		r"""The port on the back-end web-servers where the clear-text data is sent by system. Use this setting for the wildcard IP based SSL Acceleration configuration (*:443).<br/>Minimum value =  0<br/>Maximum value =  65534<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""The service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def ca(self) :
		r"""CA certificate.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@property
	def snicert(self) :
		r"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			return self._snicert
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservicegroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update sslservicegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslservicegroup()
				updateresource.servicegroupname = resource.servicegroupname
				updateresource.sslprofile = resource.sslprofile
				updateresource.sessreuse = resource.sessreuse
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.ssl3 = resource.ssl3
				updateresource.tls1 = resource.tls1
				updateresource.tls11 = resource.tls11
				updateresource.tls12 = resource.tls12
				updateresource.snienable = resource.snienable
				updateresource.ocspstapling = resource.ocspstapling
				updateresource.serverauth = resource.serverauth
				updateresource.commonname = resource.commonname
				updateresource.sendclosenotify = resource.sendclosenotify
				updateresource.strictsigdigestcheck = resource.strictsigdigestcheck
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslservicegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicegroupname = resource[i].servicegroupname
						updateresources[i].sslprofile = resource[i].sslprofile
						updateresources[i].sessreuse = resource[i].sessreuse
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].ssl3 = resource[i].ssl3
						updateresources[i].tls1 = resource[i].tls1
						updateresources[i].tls11 = resource[i].tls11
						updateresources[i].tls12 = resource[i].tls12
						updateresources[i].snienable = resource[i].snienable
						updateresources[i].ocspstapling = resource[i].ocspstapling
						updateresources[i].serverauth = resource[i].serverauth
						updateresources[i].commonname = resource[i].commonname
						updateresources[i].sendclosenotify = resource[i].sendclosenotify
						updateresources[i].strictsigdigestcheck = resource[i].strictsigdigestcheck
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslservicegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslservicegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.servicegroupname = resource
				else :
					unsetresource.servicegroupname = resource.servicegroupname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i].servicegroupname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslservicegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslservicegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslservicegroup()
					obj.servicegroupname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslservicegroup() for _ in range(len(name))]
						obj = [sslservicegroup() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslservicegroup()
							obj[i].servicegroupname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslservicegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslservicegroup resources configured on NetScaler.
		"""
		try :
			obj = sslservicegroup()
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
		r""" Use this API to count filtered the set of sslservicegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservicegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sslredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ersa:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sessreuse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl3:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls1:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ocspstapling:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslv2redirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

	class Tls11:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls12:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nonfipsciphers:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Serverauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipherredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snienable:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Strictsigdigestcheck:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcert:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Dhkeyexpsizelimit:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Clientauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

class sslservicegroup_response(base_response) :
	def __init__(self, length=1) :
		self.sslservicegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservicegroup = [sslservicegroup() for _ in range(length)]

