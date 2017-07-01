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

class sslcertreq(base_resource) :
	""" Configuration for certificate request resource. """
	def __init__(self) :
		self._reqfile = None
		self._keyfile = None
		self._fipskeyname = None
		self._keyform = None
		self._pempassphrase = None
		self._countryname = None
		self._statename = None
		self._organizationname = None
		self._organizationunitname = None
		self._localityname = None
		self._commonname = None
		self._emailaddress = None
		self._challengepassword = None
		self._companyname = None
		self._digestmethod = None

	@property
	def reqfile(self) :
		r"""Name for and, optionally, path to the certificate signing request (CSR). /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._reqfile
		except Exception as e:
			raise e

	@reqfile.setter
	def reqfile(self, reqfile) :
		r"""Name for and, optionally, path to the certificate signing request (CSR). /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._reqfile = reqfile
		except Exception as e:
			raise e

	@property
	def keyfile(self) :
		r"""Name of and, optionally, path to the private key used to create the certificate signing request, which then becomes part of the certificate-key pair. The private key can be either an RSA or a DSA key. The key must be present in the appliance's local storage. /nsconfig/ssl is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		r"""Name of and, optionally, path to the private key used to create the certificate signing request, which then becomes part of the certificate-key pair. The private key can be either an RSA or a DSA key. The key must be present in the appliance's local storage. /nsconfig/ssl is the default path.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def fipskeyname(self) :
		r"""Name of the FIPS key used to create the certificate signing request. FIPS keys are created inside the Hardware Security Module of the FIPS card.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._fipskeyname
		except Exception as e:
			raise e

	@fipskeyname.setter
	def fipskeyname(self, fipskeyname) :
		r"""Name of the FIPS key used to create the certificate signing request. FIPS keys are created inside the Hardware Security Module of the FIPS card.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._fipskeyname = fipskeyname
		except Exception as e:
			raise e

	@property
	def keyform(self) :
		r"""Format in which the key is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._keyform
		except Exception as e:
			raise e

	@keyform.setter
	def keyform(self, keyform) :
		r"""Format in which the key is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._keyform = keyform
		except Exception as e:
			raise e

	@property
	def pempassphrase(self) :
		r""".<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._pempassphrase
		except Exception as e:
			raise e

	@pempassphrase.setter
	def pempassphrase(self, pempassphrase) :
		r""".<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._pempassphrase = pempassphrase
		except Exception as e:
			raise e

	@property
	def countryname(self) :
		r"""Two letter ISO code for your country. For example, US for United States.<br/>Minimum length =  2<br/>Maximum length =  2.
		"""
		try :
			return self._countryname
		except Exception as e:
			raise e

	@countryname.setter
	def countryname(self, countryname) :
		r"""Two letter ISO code for your country. For example, US for United States.<br/>Minimum length =  2<br/>Maximum length =  2
		"""
		try :
			self._countryname = countryname
		except Exception as e:
			raise e

	@property
	def statename(self) :
		r"""Full name of the state or province where your organization is located. 
		Do not abbreviate.<br/>Minimum length =  1.
		"""
		try :
			return self._statename
		except Exception as e:
			raise e

	@statename.setter
	def statename(self, statename) :
		r"""Full name of the state or province where your organization is located. 
		Do not abbreviate.<br/>Minimum length =  1
		"""
		try :
			self._statename = statename
		except Exception as e:
			raise e

	@property
	def organizationname(self) :
		r"""Name of the organization that will use this certificate. The organization name (corporation, limited partnership, university, or government agency) must be registered with some authority at the national, state, or city level. Use the legal name under which the organization is registered. 
		Do not abbreviate the organization name and do not use the following characters in the name: 
		Angle brackets (< >) tilde (~), exclamation mark, at (@), pound (#), zero (0), caret (^), asterisk (*), forward slash (/), square brackets ([ ]), question mark (?).<br/>Minimum length =  1.
		"""
		try :
			return self._organizationname
		except Exception as e:
			raise e

	@organizationname.setter
	def organizationname(self, organizationname) :
		r"""Name of the organization that will use this certificate. The organization name (corporation, limited partnership, university, or government agency) must be registered with some authority at the national, state, or city level. Use the legal name under which the organization is registered. 
		Do not abbreviate the organization name and do not use the following characters in the name: 
		Angle brackets (< >) tilde (~), exclamation mark, at (@), pound (#), zero (0), caret (^), asterisk (*), forward slash (/), square brackets ([ ]), question mark (?).<br/>Minimum length =  1
		"""
		try :
			self._organizationname = organizationname
		except Exception as e:
			raise e

	@property
	def organizationunitname(self) :
		r"""Name of the division or section in the organization that will use the certificate.<br/>Minimum length =  1.
		"""
		try :
			return self._organizationunitname
		except Exception as e:
			raise e

	@organizationunitname.setter
	def organizationunitname(self, organizationunitname) :
		r"""Name of the division or section in the organization that will use the certificate.<br/>Minimum length =  1
		"""
		try :
			self._organizationunitname = organizationunitname
		except Exception as e:
			raise e

	@property
	def localityname(self) :
		r"""Name of the city or town in which your organization's head office is located.<br/>Minimum length =  1.
		"""
		try :
			return self._localityname
		except Exception as e:
			raise e

	@localityname.setter
	def localityname(self, localityname) :
		r"""Name of the city or town in which your organization's head office is located.<br/>Minimum length =  1
		"""
		try :
			self._localityname = localityname
		except Exception as e:
			raise e

	@property
	def commonname(self) :
		r"""Fully qualified domain name for the company or web site. The common name must match the name used by DNS servers to do a DNS lookup of your server. Most browsers use this information for authenticating the server's certificate during the SSL handshake. If the server name in the URL does not match the common name as given in the server certificate, the browser terminates the SSL handshake or prompts the user with a warning message. 
		Do not use wildcard characters, such as asterisk (*) or question mark (?), and do not use an IP address as the common name. The common name must not contain the protocol specifier <http://> or <https://>.<br/>Minimum length =  1.
		"""
		try :
			return self._commonname
		except Exception as e:
			raise e

	@commonname.setter
	def commonname(self, commonname) :
		r"""Fully qualified domain name for the company or web site. The common name must match the name used by DNS servers to do a DNS lookup of your server. Most browsers use this information for authenticating the server's certificate during the SSL handshake. If the server name in the URL does not match the common name as given in the server certificate, the browser terminates the SSL handshake or prompts the user with a warning message. 
		Do not use wildcard characters, such as asterisk (*) or question mark (?), and do not use an IP address as the common name. The common name must not contain the protocol specifier <http://> or <https://>.<br/>Minimum length =  1
		"""
		try :
			self._commonname = commonname
		except Exception as e:
			raise e

	@property
	def emailaddress(self) :
		r"""Contact person's e-mail address. This address is publically displayed as part of the certificate. Provide an e-mail address that is monitored by an administrator who can be contacted about the certificate.<br/>Minimum length =  1.
		"""
		try :
			return self._emailaddress
		except Exception as e:
			raise e

	@emailaddress.setter
	def emailaddress(self, emailaddress) :
		r"""Contact person's e-mail address. This address is publically displayed as part of the certificate. Provide an e-mail address that is monitored by an administrator who can be contacted about the certificate.<br/>Minimum length =  1
		"""
		try :
			self._emailaddress = emailaddress
		except Exception as e:
			raise e

	@property
	def challengepassword(self) :
		r"""Pass phrase, embedded in the certificate signing request that is shared only between the client or server requesting the certificate and the SSL certificate issuer (typically the certificate authority). This pass phrase can be used to authenticate a client or server that is requesting a certificate from the certificate authority.<br/>Minimum length =  4.
		"""
		try :
			return self._challengepassword
		except Exception as e:
			raise e

	@challengepassword.setter
	def challengepassword(self, challengepassword) :
		r"""Pass phrase, embedded in the certificate signing request that is shared only between the client or server requesting the certificate and the SSL certificate issuer (typically the certificate authority). This pass phrase can be used to authenticate a client or server that is requesting a certificate from the certificate authority.<br/>Minimum length =  4
		"""
		try :
			self._challengepassword = challengepassword
		except Exception as e:
			raise e

	@property
	def companyname(self) :
		r"""Additional name for the company or web site.<br/>Minimum length =  1.
		"""
		try :
			return self._companyname
		except Exception as e:
			raise e

	@companyname.setter
	def companyname(self, companyname) :
		r"""Additional name for the company or web site.<br/>Minimum length =  1
		"""
		try :
			self._companyname = companyname
		except Exception as e:
			raise e

	@property
	def digestmethod(self) :
		r"""Digest algorithm used in creating CSR.<br/>Possible values = SHA1, SHA256.
		"""
		try :
			return self._digestmethod
		except Exception as e:
			raise e

	@digestmethod.setter
	def digestmethod(self, digestmethod) :
		r"""Digest algorithm used in creating CSR.<br/>Possible values = SHA1, SHA256
		"""
		try :
			self._digestmethod = digestmethod
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertreq_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertreq
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
	def create(cls, client, resource) :
		r""" Use this API to create sslcertreq.
		"""
		try :
			if type(resource) is not list :
				createresource = sslcertreq()
				createresource.reqfile = resource.reqfile
				createresource.keyfile = resource.keyfile
				createresource.fipskeyname = resource.fipskeyname
				createresource.keyform = resource.keyform
				createresource.pempassphrase = resource.pempassphrase
				createresource.countryname = resource.countryname
				createresource.statename = resource.statename
				createresource.organizationname = resource.organizationname
				createresource.organizationunitname = resource.organizationunitname
				createresource.localityname = resource.localityname
				createresource.commonname = resource.commonname
				createresource.emailaddress = resource.emailaddress
				createresource.challengepassword = resource.challengepassword
				createresource.companyname = resource.companyname
				createresource.digestmethod = resource.digestmethod
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	class Digestmethod:
		SHA1 = "SHA1"
		SHA256 = "SHA256"

	class Keyform:
		DER = "DER"
		PEM = "PEM"

class sslcertreq_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertreq = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertreq = [sslcertreq() for _ in range(length)]

