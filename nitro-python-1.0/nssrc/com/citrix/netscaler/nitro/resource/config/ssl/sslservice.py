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

class sslservice(base_resource) :
	""" Configuration for SSL service resource. """
	def __init__(self) :
		self._servicename = None
		self._dh = None
		self._dhfile = None
		self._dhcount = None
		self._dhkeyexpsizelimit = None
		self._ersa = None
		self._ersacount = None
		self._sessreuse = None
		self._sesstimeout = None
		self._cipherredirect = None
		self._cipherurl = None
		self._sslv2redirect = None
		self._sslv2url = None
		self._clientauth = None
		self._clientcert = None
		self._sslredirect = None
		self._redirectportrewrite = None
		self._ssl2 = None
		self._ssl3 = None
		self._tls1 = None
		self._tls11 = None
		self._tls12 = None
		self._snienable = None
		self._ocspstapling = None
		self._serverauth = None
		self._commonname = None
		self._pushenctrigger = None
		self._sendclosenotify = None
		self._dtlsprofilename = None
		self._sslprofile = None
		self._strictsigdigestcheck = None
		self._nonfipsciphers = None
		self._service = None
		self._skipcaname = None
		self._dtlsflag = None
		self.___count = 0

	@property
	def servicename(self) :
		r"""Name of the SSL service.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		r"""Name of the SSL service.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def dh(self) :
		r"""State of Diffie-Hellman (DH) key exchange. This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dh
		except Exception as e:
			raise e

	@dh.setter
	def dh(self, dh) :
		r"""State of Diffie-Hellman (DH) key exchange. This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dh = dh
		except Exception as e:
			raise e

	@property
	def dhfile(self) :
		r"""Name for and, optionally, path to the PEM-format DH parameter file to be installed. /nsconfig/ssl/ is the default path. This parameter is not applicable when configuring a backend service.<br/>Minimum length =  1.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@dhfile.setter
	def dhfile(self, dhfile) :
		r"""Name for and, optionally, path to the PEM-format DH parameter file to be installed. /nsconfig/ssl/ is the default path. This parameter is not applicable when configuring a backend service.<br/>Minimum length =  1
		"""
		try :
			self._dhfile = dhfile
		except Exception as e:
			raise e

	@property
	def dhcount(self) :
		r"""Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh). This parameter is not applicable when configuring a backend service.<br/>Maximum length =  65534.
		"""
		try :
			return self._dhcount
		except Exception as e:
			raise e

	@dhcount.setter
	def dhcount(self, dhcount) :
		r"""Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh). This parameter is not applicable when configuring a backend service.<br/>Maximum length =  65534
		"""
		try :
			self._dhcount = dhcount
		except Exception as e:
			raise e

	@property
	def dhkeyexpsizelimit(self) :
		r"""This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dhkeyexpsizelimit
		except Exception as e:
			raise e

	@dhkeyexpsizelimit.setter
	def dhkeyexpsizelimit(self, dhkeyexpsizelimit) :
		r"""This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dhkeyexpsizelimit = dhkeyexpsizelimit
		except Exception as e:
			raise e

	@property
	def ersa(self) :
		r"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ersa
		except Exception as e:
			raise e

	@ersa.setter
	def ersa(self, ersa) :
		r"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ersa = ersa
		except Exception as e:
			raise e

	@property
	def ersacount(self) :
		r"""Refresh count for regeneration of RSA public-key and private-key pair. Zero (0) specifies infinite usage (no refresh). 
		This parameter is not applicable when configuring a backend service.<br/>Maximum length =  65534.
		"""
		try :
			return self._ersacount
		except Exception as e:
			raise e

	@ersacount.setter
	def ersacount(self, ersacount) :
		r"""Refresh count for regeneration of RSA public-key and private-key pair. Zero (0) specifies infinite usage (no refresh). 
		This parameter is not applicable when configuring a backend service.<br/>Maximum length =  65534
		"""
		try :
			self._ersacount = ersacount
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
	def cipherredirect(self) :
		r"""State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipherredirect
		except Exception as e:
			raise e

	@cipherredirect.setter
	def cipherredirect(self, cipherredirect) :
		r"""State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cipherredirect = cipherredirect
		except Exception as e:
			raise e

	@property
	def cipherurl(self) :
		r"""URL of the page to which to redirect the client in case of a cipher mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		This parameter is not applicable when configuring a backend service.
		"""
		try :
			return self._cipherurl
		except Exception as e:
			raise e

	@cipherurl.setter
	def cipherurl(self, cipherurl) :
		r"""URL of the page to which to redirect the client in case of a cipher mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		This parameter is not applicable when configuring a backend service.
		"""
		try :
			self._cipherurl = cipherurl
		except Exception as e:
			raise e

	@property
	def sslv2redirect(self) :
		r"""State of SSLv2 Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a protocol version mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslv2redirect
		except Exception as e:
			raise e

	@sslv2redirect.setter
	def sslv2redirect(self, sslv2redirect) :
		r"""State of SSLv2 Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a protocol version mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslv2redirect = sslv2redirect
		except Exception as e:
			raise e

	@property
	def sslv2url(self) :
		r"""URL of the page to which to redirect the client in case of a protocol version mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		This parameter is not applicable when configuring a backend service.
		"""
		try :
			return self._sslv2url
		except Exception as e:
			raise e

	@sslv2url.setter
	def sslv2url(self, sslv2url) :
		r"""URL of the page to which to redirect the client in case of a protocol version mismatch. Typically, this page has a clear explanation of the error or an alternative location that the transaction can continue from.
		This parameter is not applicable when configuring a backend service.
		"""
		try :
			self._sslv2url = sslv2url
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		r"""State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate. 
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@clientauth.setter
	def clientauth(self, clientauth) :
		r"""State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate. 
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientauth = clientauth
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		r"""Type of client authentication. If this parameter is set to MANDATORY, the appliance terminates the SSL handshake if the SSL client does not provide a valid certificate. With the OPTIONAL setting, the appliance requests a certificate from the SSL clients but proceeds with the SSL transaction even if the client presents an invalid certificate.
		This parameter is not applicable when configuring a backend SSL service.
		Caution: Define proper access control policies before changing this setting to Optional.<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@clientcert.setter
	def clientcert(self, clientcert) :
		r"""Type of client authentication. If this parameter is set to MANDATORY, the appliance terminates the SSL handshake if the SSL client does not provide a valid certificate. With the OPTIONAL setting, the appliance requests a certificate from the SSL clients but proceeds with the SSL transaction even if the client presents an invalid certificate.
		This parameter is not applicable when configuring a backend SSL service.
		Caution: Define proper access control policies before changing this setting to Optional.<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._clientcert = clientcert
		except Exception as e:
			raise e

	@property
	def sslredirect(self) :
		r"""State of HTTPS redirects for the SSL service. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslredirect
		except Exception as e:
			raise e

	@sslredirect.setter
	def sslredirect(self, sslredirect) :
		r"""State of HTTPS redirects for the SSL service. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslredirect = sslredirect
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		r"""State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@redirectportrewrite.setter
	def redirectportrewrite(self, redirectportrewrite) :
		r"""State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._redirectportrewrite = redirectportrewrite
		except Exception as e:
			raise e

	@property
	def ssl2(self) :
		r"""State of SSLv2 protocol support for the SSL service.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl2
		except Exception as e:
			raise e

	@ssl2.setter
	def ssl2(self, ssl2) :
		r"""State of SSLv2 protocol support for the SSL service.
		This parameter is not applicable when configuring a backend service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl2 = ssl2
		except Exception as e:
			raise e

	@property
	def ssl3(self) :
		r"""State of SSLv3 protocol support for the SSL service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl3
		except Exception as e:
			raise e

	@ssl3.setter
	def ssl3(self, ssl3) :
		r"""State of SSLv3 protocol support for the SSL service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl3 = ssl3
		except Exception as e:
			raise e

	@property
	def tls1(self) :
		r"""State of TLSv1.0 protocol support for the SSL service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls1
		except Exception as e:
			raise e

	@tls1.setter
	def tls1(self, tls1) :
		r"""State of TLSv1.0 protocol support for the SSL service.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls1 = tls1
		except Exception as e:
			raise e

	@property
	def tls11(self) :
		r"""State of TLSv1.1 protocol support for the SSL service. Enabled for Front-end service on MPX-CVM platform only.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls11
		except Exception as e:
			raise e

	@tls11.setter
	def tls11(self, tls11) :
		r"""State of TLSv1.1 protocol support for the SSL service. Enabled for Front-end service on MPX-CVM platform only.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls11 = tls11
		except Exception as e:
			raise e

	@property
	def tls12(self) :
		r"""State of TLSv1.2 protocol support for the SSL service. Enabled for Front-end service on MPX-CVM platform only.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls12
		except Exception as e:
			raise e

	@tls12.setter
	def tls12(self, tls12) :
		r"""State of TLSv1.2 protocol support for the SSL service. Enabled for Front-end service on MPX-CVM platform only.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls12 = tls12
		except Exception as e:
			raise e

	@property
	def snienable(self) :
		r"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snienable
		except Exception as e:
			raise e

	@snienable.setter
	def snienable(self, snienable) :
		r"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snienable = snienable
		except Exception as e:
			raise e

	@property
	def ocspstapling(self) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ocspstapling
		except Exception as e:
			raise e

	@ocspstapling.setter
	def ocspstapling(self, ocspstapling) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ocspstapling = ocspstapling
		except Exception as e:
			raise e

	@property
	def serverauth(self) :
		r"""State of server authentication support for the SSL service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._serverauth
		except Exception as e:
			raise e

	@serverauth.setter
	def serverauth(self, serverauth) :
		r"""State of server authentication support for the SSL service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
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
	def pushenctrigger(self) :
		r"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer.
		"""
		try :
			return self._pushenctrigger
		except Exception as e:
			raise e

	@pushenctrigger.setter
	def pushenctrigger(self, pushenctrigger) :
		r"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer
		"""
		try :
			self._pushenctrigger = pushenctrigger
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
	def dtlsprofilename(self) :
		r"""Name of the DTLS profile that contains DTLS settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dtlsprofilename
		except Exception as e:
			raise e

	@dtlsprofilename.setter
	def dtlsprofilename(self, dtlsprofilename) :
		r"""Name of the DTLS profile that contains DTLS settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dtlsprofilename = dtlsprofilename
		except Exception as e:
			raise e

	@property
	def sslprofile(self) :
		r"""Name of the SSL profile that contains SSL settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sslprofile
		except Exception as e:
			raise e

	@sslprofile.setter
	def sslprofile(self, sslprofile) :
		r"""Name of the SSL profile that contains SSL settings for the service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sslprofile = sslprofile
		except Exception as e:
			raise e

	@property
	def strictsigdigestcheck(self) :
		r"""Parameter indicating to check whether peer's certificate during TLS1.2 handshake is signed with one of signature-hash combination supported by Netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._strictsigdigestcheck
		except Exception as e:
			raise e

	@strictsigdigestcheck.setter
	def strictsigdigestcheck(self, strictsigdigestcheck) :
		r"""Parameter indicating to check whether peer's certificate during TLS1.2 handshake is signed with one of signature-hash combination supported by Netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._strictsigdigestcheck = strictsigdigestcheck
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
	def service(self) :
		try :
			return self._service
		except Exception as e:
			raise e

	@property
	def skipcaname(self) :
		r"""The flag is used to indicate whether this particular CA certificate's CA_Name needs to be sent to the SSL client while requesting      for client certificate in a SSL handshake.
		"""
		try :
			return self._skipcaname
		except Exception as e:
			raise e

	@property
	def dtlsflag(self) :
		r"""The flag is used to indicate whether DTLS is set or not.
		"""
		try :
			return self._dtlsflag
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservice_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservice
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicename is not None :
				return str(self.servicename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update sslservice.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslservice()
				updateresource.servicename = resource.servicename
				updateresource.dh = resource.dh
				updateresource.dhfile = resource.dhfile
				updateresource.dhcount = resource.dhcount
				updateresource.dhkeyexpsizelimit = resource.dhkeyexpsizelimit
				updateresource.ersa = resource.ersa
				updateresource.ersacount = resource.ersacount
				updateresource.sessreuse = resource.sessreuse
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.cipherredirect = resource.cipherredirect
				updateresource.cipherurl = resource.cipherurl
				updateresource.sslv2redirect = resource.sslv2redirect
				updateresource.sslv2url = resource.sslv2url
				updateresource.clientauth = resource.clientauth
				updateresource.clientcert = resource.clientcert
				updateresource.sslredirect = resource.sslredirect
				updateresource.redirectportrewrite = resource.redirectportrewrite
				updateresource.ssl2 = resource.ssl2
				updateresource.ssl3 = resource.ssl3
				updateresource.tls1 = resource.tls1
				updateresource.tls11 = resource.tls11
				updateresource.tls12 = resource.tls12
				updateresource.snienable = resource.snienable
				updateresource.ocspstapling = resource.ocspstapling
				updateresource.serverauth = resource.serverauth
				updateresource.commonname = resource.commonname
				updateresource.pushenctrigger = resource.pushenctrigger
				updateresource.sendclosenotify = resource.sendclosenotify
				updateresource.dtlsprofilename = resource.dtlsprofilename
				updateresource.sslprofile = resource.sslprofile
				updateresource.strictsigdigestcheck = resource.strictsigdigestcheck
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslservice() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].servicename = resource[i].servicename
						updateresources[i].dh = resource[i].dh
						updateresources[i].dhfile = resource[i].dhfile
						updateresources[i].dhcount = resource[i].dhcount
						updateresources[i].dhkeyexpsizelimit = resource[i].dhkeyexpsizelimit
						updateresources[i].ersa = resource[i].ersa
						updateresources[i].ersacount = resource[i].ersacount
						updateresources[i].sessreuse = resource[i].sessreuse
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].cipherredirect = resource[i].cipherredirect
						updateresources[i].cipherurl = resource[i].cipherurl
						updateresources[i].sslv2redirect = resource[i].sslv2redirect
						updateresources[i].sslv2url = resource[i].sslv2url
						updateresources[i].clientauth = resource[i].clientauth
						updateresources[i].clientcert = resource[i].clientcert
						updateresources[i].sslredirect = resource[i].sslredirect
						updateresources[i].redirectportrewrite = resource[i].redirectportrewrite
						updateresources[i].ssl2 = resource[i].ssl2
						updateresources[i].ssl3 = resource[i].ssl3
						updateresources[i].tls1 = resource[i].tls1
						updateresources[i].tls11 = resource[i].tls11
						updateresources[i].tls12 = resource[i].tls12
						updateresources[i].snienable = resource[i].snienable
						updateresources[i].ocspstapling = resource[i].ocspstapling
						updateresources[i].serverauth = resource[i].serverauth
						updateresources[i].commonname = resource[i].commonname
						updateresources[i].pushenctrigger = resource[i].pushenctrigger
						updateresources[i].sendclosenotify = resource[i].sendclosenotify
						updateresources[i].dtlsprofilename = resource[i].dtlsprofilename
						updateresources[i].sslprofile = resource[i].sslprofile
						updateresources[i].strictsigdigestcheck = resource[i].strictsigdigestcheck
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslservice resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslservice()
				if type(resource) !=  type(unsetresource):
					unsetresource.servicename = resource
				else :
					unsetresource.servicename = resource.servicename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservice() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslservice() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicename = resource[i].servicename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslservice resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslservice()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslservice()
					obj.servicename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslservice() for _ in range(len(name))]
						obj = [sslservice() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslservice()
							obj[i].servicename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslservice resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservice()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslservice resources configured on NetScaler.
		"""
		try :
			obj = sslservice()
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
		r""" Use this API to count filtered the set of sslservice resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslservice()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Tls11:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ersa:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls12:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nonfipsciphers:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Serverauth:
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

	class Snienable:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipherredirect:
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

	class Pushenctrigger:
		Always = "Always"
		Merge = "Merge"
		Ignore = "Ignore"
		Timer = "Timer"

	class Ocspstapling:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslv2redirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

class sslservice_response(base_response) :
	def __init__(self, length=1) :
		self.sslservice = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservice = [sslservice() for _ in range(length)]

