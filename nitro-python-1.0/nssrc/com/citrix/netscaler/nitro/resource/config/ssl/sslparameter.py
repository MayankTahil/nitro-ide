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

class sslparameter(base_resource) :
	""" Configuration for SSL parameter resource. """
	def __init__(self) :
		self._quantumsize = None
		self._crlmemorysizemb = None
		self._strictcachecks = None
		self._ssltriggertimeout = None
		self._sendclosenotify = None
		self._encrypttriggerpktcount = None
		self._denysslreneg = None
		self._insertionencoding = None
		self._ocspcachesize = None
		self._pushflag = None
		self._dropreqwithnohostheader = None
		self._pushenctriggertimeout = None
		self._cryptodevdisablelimit = None
		self._undefactioncontrol = None
		self._undefactiondata = None
		self._defaultprofile = None
		self._softwarecryptothreshold = None
		self._hybridfipsmode = None
		self._sigdigesttype = []
		self._sslierrorcache = None
		self._sslimaxerrorcachemem = None
		self._insertcertspace = None
		self._svctls1112disable = None
		self._montls1112disable = None

	@property
	def quantumsize(self) :
		r"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384.
		"""
		try :
			return self._quantumsize
		except Exception as e:
			raise e

	@quantumsize.setter
	def quantumsize(self, quantumsize) :
		r"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384
		"""
		try :
			self._quantumsize = quantumsize
		except Exception as e:
			raise e

	@property
	def crlmemorysizemb(self) :
		r"""Maximum memory size to use for certificate revocation lists (CRLs). This parameter reserves memory for a CRL but sets a limit to the maximum memory that the CRLs loaded on the appliance can consume.<br/>Default value: 256<br/>Minimum length =  10<br/>Maximum length =  1024.
		"""
		try :
			return self._crlmemorysizemb
		except Exception as e:
			raise e

	@crlmemorysizemb.setter
	def crlmemorysizemb(self, crlmemorysizemb) :
		r"""Maximum memory size to use for certificate revocation lists (CRLs). This parameter reserves memory for a CRL but sets a limit to the maximum memory that the CRLs loaded on the appliance can consume.<br/>Default value: 256<br/>Minimum length =  10<br/>Maximum length =  1024
		"""
		try :
			self._crlmemorysizemb = crlmemorysizemb
		except Exception as e:
			raise e

	@property
	def strictcachecks(self) :
		r"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._strictcachecks
		except Exception as e:
			raise e

	@strictcachecks.setter
	def strictcachecks(self, strictcachecks) :
		r"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._strictcachecks = strictcachecks
		except Exception as e:
			raise e

	@property
	def ssltriggertimeout(self) :
		r"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._ssltriggertimeout
		except Exception as e:
			raise e

	@ssltriggertimeout.setter
	def ssltriggertimeout(self, ssltriggertimeout) :
		r"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._ssltriggertimeout = ssltriggertimeout
		except Exception as e:
			raise e

	@property
	def sendclosenotify(self) :
		r"""Send an SSL Close-Notify message to the client at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._sendclosenotify
		except Exception as e:
			raise e

	@sendclosenotify.setter
	def sendclosenotify(self, sendclosenotify) :
		r"""Send an SSL Close-Notify message to the client at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._sendclosenotify = sendclosenotify
		except Exception as e:
			raise e

	@property
	def encrypttriggerpktcount(self) :
		r"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50.
		"""
		try :
			return self._encrypttriggerpktcount
		except Exception as e:
			raise e

	@encrypttriggerpktcount.setter
	def encrypttriggerpktcount(self, encrypttriggerpktcount) :
		r"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50
		"""
		try :
			self._encrypttriggerpktcount = encrypttriggerpktcount
		except Exception as e:
			raise e

	@property
	def denysslreneg(self) :
		r"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE.
		"""
		try :
			return self._denysslreneg
		except Exception as e:
			raise e

	@denysslreneg.setter
	def denysslreneg(self, denysslreneg) :
		r"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE
		"""
		try :
			self._denysslreneg = denysslreneg
		except Exception as e:
			raise e

	@property
	def insertionencoding(self) :
		r"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8.
		"""
		try :
			return self._insertionencoding
		except Exception as e:
			raise e

	@insertionencoding.setter
	def insertionencoding(self, insertionencoding) :
		r"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8
		"""
		try :
			self._insertionencoding = insertionencoding
		except Exception as e:
			raise e

	@property
	def ocspcachesize(self) :
		r"""Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10% of the packet engine memory can be assigned. Because the maximum allowed packet engine memory is 4GB, the maximum value that can be assigned to the OCSP cache is approximately 410 MB.<br/>Default value: 10<br/>Maximum length =  512.
		"""
		try :
			return self._ocspcachesize
		except Exception as e:
			raise e

	@ocspcachesize.setter
	def ocspcachesize(self, ocspcachesize) :
		r"""Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10% of the packet engine memory can be assigned. Because the maximum allowed packet engine memory is 4GB, the maximum value that can be assigned to the OCSP cache is approximately 410 MB.<br/>Default value: 10<br/>Maximum length =  512
		"""
		try :
			self._ocspcachesize = ocspcachesize
		except Exception as e:
			raise e

	@property
	def pushflag(self) :
		r"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3.
		"""
		try :
			return self._pushflag
		except Exception as e:
			raise e

	@pushflag.setter
	def pushflag(self, pushflag) :
		r"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3
		"""
		try :
			self._pushflag = pushflag
		except Exception as e:
			raise e

	@property
	def dropreqwithnohostheader(self) :
		r"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropreqwithnohostheader
		except Exception as e:
			raise e

	@dropreqwithnohostheader.setter
	def dropreqwithnohostheader(self, dropreqwithnohostheader) :
		r"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dropreqwithnohostheader = dropreqwithnohostheader
		except Exception as e:
			raise e

	@property
	def pushenctriggertimeout(self) :
		r"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._pushenctriggertimeout
		except Exception as e:
			raise e

	@pushenctriggertimeout.setter
	def pushenctriggertimeout(self, pushenctriggertimeout) :
		r"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._pushenctriggertimeout = pushenctriggertimeout
		except Exception as e:
			raise e

	@property
	def cryptodevdisablelimit(self) :
		r"""Limit to the number of disabled SSL chips after which the ADC restarts. A value of zero implies that the ADC does not automatically restart.<br/>Default value: 0.
		"""
		try :
			return self._cryptodevdisablelimit
		except Exception as e:
			raise e

	@cryptodevdisablelimit.setter
	def cryptodevdisablelimit(self, cryptodevdisablelimit) :
		r"""Limit to the number of disabled SSL chips after which the ADC restarts. A value of zero implies that the ADC does not automatically restart.<br/>Default value: 0
		"""
		try :
			self._cryptodevdisablelimit = cryptodevdisablelimit
		except Exception as e:
			raise e

	@property
	def undefactioncontrol(self) :
		r"""Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH, NOOP, RESET, or DROP.<br/>Default value: "CLIENTAUTH".
		"""
		try :
			return self._undefactioncontrol
		except Exception as e:
			raise e

	@undefactioncontrol.setter
	def undefactioncontrol(self, undefactioncontrol) :
		r"""Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH, NOOP, RESET, or DROP.<br/>Default value: "CLIENTAUTH"
		"""
		try :
			self._undefactioncontrol = undefactioncontrol
		except Exception as e:
			raise e

	@property
	def undefactiondata(self) :
		r"""Name of the undefined built-in data action: NOOP, RESET or DROP.<br/>Default value: "NOOP".
		"""
		try :
			return self._undefactiondata
		except Exception as e:
			raise e

	@undefactiondata.setter
	def undefactiondata(self, undefactiondata) :
		r"""Name of the undefined built-in data action: NOOP, RESET or DROP.<br/>Default value: "NOOP"
		"""
		try :
			self._undefactiondata = undefactiondata
		except Exception as e:
			raise e

	@property
	def defaultprofile(self) :
		r"""Global parameter used to enable default profile feature.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._defaultprofile
		except Exception as e:
			raise e

	@defaultprofile.setter
	def defaultprofile(self, defaultprofile) :
		r"""Global parameter used to enable default profile feature.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._defaultprofile = defaultprofile
		except Exception as e:
			raise e

	@property
	def softwarecryptothreshold(self) :
		r"""Netscaler CPU utilization threshold (in percentage) beyond which crypto operations are not done in software.
		A value of zero implies that CPU is not utilized for doing crypto in software.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._softwarecryptothreshold
		except Exception as e:
			raise e

	@softwarecryptothreshold.setter
	def softwarecryptothreshold(self, softwarecryptothreshold) :
		r"""Netscaler CPU utilization threshold (in percentage) beyond which crypto operations are not done in software.
		A value of zero implies that CPU is not utilized for doing crypto in software.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._softwarecryptothreshold = softwarecryptothreshold
		except Exception as e:
			raise e

	@property
	def hybridfipsmode(self) :
		r"""When this mode is enabled, system will use additional crypto hardware to accelerate symmetric crypto operations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hybridfipsmode
		except Exception as e:
			raise e

	@hybridfipsmode.setter
	def hybridfipsmode(self, hybridfipsmode) :
		r"""When this mode is enabled, system will use additional crypto hardware to accelerate symmetric crypto operations.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hybridfipsmode = hybridfipsmode
		except Exception as e:
			raise e

	@property
	def sigdigesttype(self) :
		r"""SigDigest Algo that are supported by appliance. Default value may vary according to the cipher supported on the appliance .<br/>Default value: ALL<br/>Possible values = ALL, RSA-MD5, RSA-SHA1, RSA-SHA224, RSA-SHA256, RSA-SHA384, RSA-SHA512, DSA-SHA1, DSA-SHA224, DSA-SHA256, DSA-SHA384, DSA-SHA512, ECDSA-SHA1, ECDSA-SHA224, ECDSA-SHA256, ECDSA-SHA384, ECDSA-SHA512.
		"""
		try :
			return self._sigdigesttype
		except Exception as e:
			raise e

	@sigdigesttype.setter
	def sigdigesttype(self, sigdigesttype) :
		r"""SigDigest Algo that are supported by appliance. Default value may vary according to the cipher supported on the appliance .<br/>Default value: ALL<br/>Possible values = ALL, RSA-MD5, RSA-SHA1, RSA-SHA224, RSA-SHA256, RSA-SHA384, RSA-SHA512, DSA-SHA1, DSA-SHA224, DSA-SHA256, DSA-SHA384, DSA-SHA512, ECDSA-SHA1, ECDSA-SHA224, ECDSA-SHA256, ECDSA-SHA384, ECDSA-SHA512
		"""
		try :
			self._sigdigesttype = sigdigesttype
		except Exception as e:
			raise e

	@property
	def sslierrorcache(self) :
		r"""Enable or disable dynamically learning and caching the learned information to make the subsequent interception or bypass decision. When enabled, NS does the lookup of this cached data to do early bypass.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslierrorcache
		except Exception as e:
			raise e

	@sslierrorcache.setter
	def sslierrorcache(self, sslierrorcache) :
		r"""Enable or disable dynamically learning and caching the learned information to make the subsequent interception or bypass decision. When enabled, NS does the lookup of this cached data to do early bypass.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslierrorcache = sslierrorcache
		except Exception as e:
			raise e

	@property
	def sslimaxerrorcachemem(self) :
		r"""Specify the maximum memory that can be used for caching the learned data. This memory is used as a LRU cache so that the old entries gets replaced with new entry once the set memory limit is fully utilised. A value of 0 decides the limit automatically.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sslimaxerrorcachemem
		except Exception as e:
			raise e

	@sslimaxerrorcachemem.setter
	def sslimaxerrorcachemem(self, sslimaxerrorcachemem) :
		r"""Specify the maximum memory that can be used for caching the learned data. This memory is used as a LRU cache so that the old entries gets replaced with new entry once the set memory limit is fully utilised. A value of 0 decides the limit automatically.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sslimaxerrorcachemem = sslimaxerrorcachemem
		except Exception as e:
			raise e

	@property
	def insertcertspace(self) :
		r"""To insert space between lines in the certificate header of request.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertcertspace
		except Exception as e:
			raise e

	@insertcertspace.setter
	def insertcertspace(self, insertcertspace) :
		r"""To insert space between lines in the certificate header of request.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._insertcertspace = insertcertspace
		except Exception as e:
			raise e

	@property
	def svctls1112disable(self) :
		r"""Disable TLS 1.1 and 1.2 for dynamic and VPN created services.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._svctls1112disable
		except Exception as e:
			raise e

	@property
	def montls1112disable(self) :
		r"""Disable TLS 1.1 and 1.2 for secure (https) monitors bound to SSL_BRIDGE services.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._montls1112disable
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslparameter
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
		r""" Use this API to update sslparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslparameter()
				updateresource.quantumsize = resource.quantumsize
				updateresource.crlmemorysizemb = resource.crlmemorysizemb
				updateresource.strictcachecks = resource.strictcachecks
				updateresource.ssltriggertimeout = resource.ssltriggertimeout
				updateresource.sendclosenotify = resource.sendclosenotify
				updateresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
				updateresource.denysslreneg = resource.denysslreneg
				updateresource.insertionencoding = resource.insertionencoding
				updateresource.ocspcachesize = resource.ocspcachesize
				updateresource.pushflag = resource.pushflag
				updateresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
				updateresource.pushenctriggertimeout = resource.pushenctriggertimeout
				updateresource.cryptodevdisablelimit = resource.cryptodevdisablelimit
				updateresource.undefactioncontrol = resource.undefactioncontrol
				updateresource.undefactiondata = resource.undefactiondata
				updateresource.defaultprofile = resource.defaultprofile
				updateresource.softwarecryptothreshold = resource.softwarecryptothreshold
				updateresource.hybridfipsmode = resource.hybridfipsmode
				updateresource.sigdigesttype = resource.sigdigesttype
				updateresource.sslierrorcache = resource.sslierrorcache
				updateresource.sslimaxerrorcachemem = resource.sslimaxerrorcachemem
				updateresource.insertcertspace = resource.insertcertspace
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Hybridfipsmode:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Denysslreneg:
		NO = "NO"
		FRONTEND_CLIENT = "FRONTEND_CLIENT"
		FRONTEND_CLIENTSERVER = "FRONTEND_CLIENTSERVER"
		ALL = "ALL"
		NONSECURE = "NONSECURE"

	class Insertionencoding:
		Unicode = "Unicode"
		UTF_8 = "UTF-8"

	class Defaultprofile:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Strictcachecks:
		YES = "YES"
		NO = "NO"

	class Quantumsize:
		_4096 = "4096"
		_8192 = "8192"
		_16384 = "16384"

	class Insertcertspace:
		YES = "YES"
		NO = "NO"

	class Svctls1112disable:
		YES = "YES"
		NO = "NO"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

	class Dropreqwithnohostheader:
		YES = "YES"
		NO = "NO"

	class Montls1112disable:
		YES = "YES"
		NO = "NO"

	class Sigdigesttype:
		ALL = "ALL"
		RSA_MD5 = "RSA-MD5"
		RSA_SHA1 = "RSA-SHA1"
		RSA_SHA224 = "RSA-SHA224"
		RSA_SHA256 = "RSA-SHA256"
		RSA_SHA384 = "RSA-SHA384"
		RSA_SHA512 = "RSA-SHA512"
		DSA_SHA1 = "DSA-SHA1"
		DSA_SHA224 = "DSA-SHA224"
		DSA_SHA256 = "DSA-SHA256"
		DSA_SHA384 = "DSA-SHA384"
		DSA_SHA512 = "DSA-SHA512"
		ECDSA_SHA1 = "ECDSA-SHA1"
		ECDSA_SHA224 = "ECDSA-SHA224"
		ECDSA_SHA256 = "ECDSA-SHA256"
		ECDSA_SHA384 = "ECDSA-SHA384"
		ECDSA_SHA512 = "ECDSA-SHA512"

	class Sslierrorcache:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class sslparameter_response(base_response) :
	def __init__(self, length=1) :
		self.sslparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslparameter = [sslparameter() for _ in range(length)]

