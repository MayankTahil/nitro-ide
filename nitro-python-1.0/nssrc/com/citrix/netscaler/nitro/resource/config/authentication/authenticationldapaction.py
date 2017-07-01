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

class authenticationldapaction(base_resource) :
	""" Configuration for LDAP action resource. """
	def __init__(self) :
		self._name = None
		self._serverip = None
		self._servername = None
		self._serverport = None
		self._authtimeout = None
		self._ldapbase = None
		self._ldapbinddn = None
		self._ldapbinddnpassword = None
		self._ldaploginname = None
		self._searchfilter = None
		self._groupattrname = None
		self._subattributename = None
		self._sectype = None
		self._svrtype = None
		self._ssonameattribute = None
		self._authentication = None
		self._requireuser = None
		self._passwdchange = None
		self._nestedgroupextraction = None
		self._maxnestinglevel = None
		self._followreferrals = None
		self._maxldapreferrals = None
		self._referraldnslookup = None
		self._mssrvrecordlocation = None
		self._validateservercert = None
		self._ldaphostname = None
		self._groupnameidentifier = None
		self._groupsearchattribute = None
		self._groupsearchsubattribute = None
		self._groupsearchfilter = None
		self._defaultauthenticationgroup = None
		self._attribute1 = None
		self._attribute2 = None
		self._attribute3 = None
		self._attribute4 = None
		self._attribute5 = None
		self._attribute6 = None
		self._attribute7 = None
		self._attribute8 = None
		self._attribute9 = None
		self._attribute10 = None
		self._attribute11 = None
		self._attribute12 = None
		self._attribute13 = None
		self._attribute14 = None
		self._attribute15 = None
		self._attribute16 = None
		self._success = None
		self._failure = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the new LDAP action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the LDAP action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the new LDAP action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the LDAP action is added.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		r"""IP address assigned to the LDAP server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address assigned to the LDAP server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""LDAP server name as a FQDN.  Mutually exclusive with LDAP IP address.<br/>Minimum length =  1
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port on which the LDAP server accepts connections.<br/>Default value: 389<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port on which the LDAP server accepts connections.<br/>Default value: 389<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		r"""Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		r"""Number of seconds the NetScaler appliance waits for a response from the RADIUS server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def ldapbase(self) :
		r"""Base (node) from which to start LDAP searches. 
		If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
		"""
		try :
			return self._ldapbase
		except Exception as e:
			raise e

	@ldapbase.setter
	def ldapbase(self, ldapbase) :
		r"""Base (node) from which to start LDAP searches. 
		If the LDAP server is running locally, the default value of base is dc=netscaler, dc=com.
		"""
		try :
			self._ldapbase = ldapbase
		except Exception as e:
			raise e

	@property
	def ldapbinddn(self) :
		r"""Full distinguished name (DN) that is used to bind to the LDAP server. 
		Default: cn=Manager,dc=netscaler,dc=com.
		"""
		try :
			return self._ldapbinddn
		except Exception as e:
			raise e

	@ldapbinddn.setter
	def ldapbinddn(self, ldapbinddn) :
		r"""Full distinguished name (DN) that is used to bind to the LDAP server. 
		Default: cn=Manager,dc=netscaler,dc=com.
		"""
		try :
			self._ldapbinddn = ldapbinddn
		except Exception as e:
			raise e

	@property
	def ldapbinddnpassword(self) :
		r"""Password used to bind to the LDAP server.<br/>Minimum length =  1.
		"""
		try :
			return self._ldapbinddnpassword
		except Exception as e:
			raise e

	@ldapbinddnpassword.setter
	def ldapbinddnpassword(self, ldapbinddnpassword) :
		r"""Password used to bind to the LDAP server.<br/>Minimum length =  1
		"""
		try :
			self._ldapbinddnpassword = ldapbinddnpassword
		except Exception as e:
			raise e

	@property
	def ldaploginname(self) :
		r"""LDAP login name attribute. 
		The NetScaler appliance uses the LDAP login name to query external LDAP servers or Active Directories.
		"""
		try :
			return self._ldaploginname
		except Exception as e:
			raise e

	@ldaploginname.setter
	def ldaploginname(self, ldaploginname) :
		r"""LDAP login name attribute. 
		The NetScaler appliance uses the LDAP login name to query external LDAP servers or Active Directories.
		"""
		try :
			self._ldaploginname = ldaploginname
		except Exception as e:
			raise e

	@property
	def searchfilter(self) :
		r"""String to be combined with the default LDAP user search string to form the search value. For example, if the search filter "vpnallowed=true" is combined with the LDAP login name "samaccount" and the user-supplied username is "bob", the result is the LDAP search string ""(&(vpnallowed=true)(samaccount=bob)"" (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).<br/>Minimum length =  1.
		"""
		try :
			return self._searchfilter
		except Exception as e:
			raise e

	@searchfilter.setter
	def searchfilter(self, searchfilter) :
		r"""String to be combined with the default LDAP user search string to form the search value. For example, if the search filter "vpnallowed=true" is combined with the LDAP login name "samaccount" and the user-supplied username is "bob", the result is the LDAP search string ""(&(vpnallowed=true)(samaccount=bob)"" (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).<br/>Minimum length =  1
		"""
		try :
			self._searchfilter = searchfilter
		except Exception as e:
			raise e

	@property
	def groupattrname(self) :
		r"""LDAP group attribute name.
		Used for group extraction on the LDAP server.
		"""
		try :
			return self._groupattrname
		except Exception as e:
			raise e

	@groupattrname.setter
	def groupattrname(self, groupattrname) :
		r"""LDAP group attribute name.
		Used for group extraction on the LDAP server.
		"""
		try :
			self._groupattrname = groupattrname
		except Exception as e:
			raise e

	@property
	def subattributename(self) :
		r"""LDAP group sub-attribute name. 
		Used for group extraction from the LDAP server.
		"""
		try :
			return self._subattributename
		except Exception as e:
			raise e

	@subattributename.setter
	def subattributename(self, subattributename) :
		r"""LDAP group sub-attribute name. 
		Used for group extraction from the LDAP server.
		"""
		try :
			self._subattributename = subattributename
		except Exception as e:
			raise e

	@property
	def sectype(self) :
		r"""Type of security used for communications between the NetScaler appliance and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL.
		"""
		try :
			return self._sectype
		except Exception as e:
			raise e

	@sectype.setter
	def sectype(self, sectype) :
		r"""Type of security used for communications between the NetScaler appliance and the LDAP server. For the PLAINTEXT setting, no encryption is required.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT, TLS, SSL
		"""
		try :
			self._sectype = sectype
		except Exception as e:
			raise e

	@property
	def svrtype(self) :
		r"""The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS.
		"""
		try :
			return self._svrtype
		except Exception as e:
			raise e

	@svrtype.setter
	def svrtype(self, svrtype) :
		r"""The type of LDAP server.<br/>Default value: AAA_LDAP_SERVER_TYPE_DEFAULT<br/>Possible values = AD, NDS
		"""
		try :
			self._svrtype = svrtype
		except Exception as e:
			raise e

	@property
	def ssonameattribute(self) :
		r"""LDAP single signon (SSO) attribute. 
		The NetScaler appliance uses the SSO name attribute to query external LDAP servers or Active Directories for an alternate username.
		"""
		try :
			return self._ssonameattribute
		except Exception as e:
			raise e

	@ssonameattribute.setter
	def ssonameattribute(self, ssonameattribute) :
		r"""LDAP single signon (SSO) attribute. 
		The NetScaler appliance uses the SSO name attribute to query external LDAP servers or Active Directories for an alternate username.
		"""
		try :
			self._ssonameattribute = ssonameattribute
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		r"""Perform LDAP authentication.
		If authentication is disabled, any LDAP authentication attempt returns authentication success if the user is found. 
		CAUTION! Authentication should be disabled only for authorization group extraction or where other (non-LDAP) authentication methods are in use and either bound to a primary list or flagged as secondary.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		r"""Perform LDAP authentication.
		If authentication is disabled, any LDAP authentication attempt returns authentication success if the user is found. 
		CAUTION! Authentication should be disabled only for authorization group extraction or where other (non-LDAP) authentication methods are in use and either bound to a primary list or flagged as secondary.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def requireuser(self) :
		r"""Require a successful user search for authentication.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._requireuser
		except Exception as e:
			raise e

	@requireuser.setter
	def requireuser(self, requireuser) :
		r"""Require a successful user search for authentication.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._requireuser = requireuser
		except Exception as e:
			raise e

	@property
	def passwdchange(self) :
		r"""Allow password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._passwdchange
		except Exception as e:
			raise e

	@passwdchange.setter
	def passwdchange(self, passwdchange) :
		r"""Allow password change requests.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._passwdchange = passwdchange
		except Exception as e:
			raise e

	@property
	def nestedgroupextraction(self) :
		r"""Allow nested group extraction, in which the NetScaler appliance queries external LDAP servers to determine whether a group is part of another group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._nestedgroupextraction
		except Exception as e:
			raise e

	@nestedgroupextraction.setter
	def nestedgroupextraction(self, nestedgroupextraction) :
		r"""Allow nested group extraction, in which the NetScaler appliance queries external LDAP servers to determine whether a group is part of another group.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._nestedgroupextraction = nestedgroupextraction
		except Exception as e:
			raise e

	@property
	def maxnestinglevel(self) :
		r"""If nested group extraction is ON, specifies the number of levels up to which group extraction is performed.<br/>Default value: 2<br/>Minimum length =  2.
		"""
		try :
			return self._maxnestinglevel
		except Exception as e:
			raise e

	@maxnestinglevel.setter
	def maxnestinglevel(self, maxnestinglevel) :
		r"""If nested group extraction is ON, specifies the number of levels up to which group extraction is performed.<br/>Default value: 2<br/>Minimum length =  2
		"""
		try :
			self._maxnestinglevel = maxnestinglevel
		except Exception as e:
			raise e

	@property
	def followreferrals(self) :
		r"""Setting this option to ON enables following LDAP referrals received from the LDAP server.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._followreferrals
		except Exception as e:
			raise e

	@followreferrals.setter
	def followreferrals(self, followreferrals) :
		r"""Setting this option to ON enables following LDAP referrals received from the LDAP server.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._followreferrals = followreferrals
		except Exception as e:
			raise e

	@property
	def maxldapreferrals(self) :
		r"""Specifies the maximum number of nested referrals to follow.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._maxldapreferrals
		except Exception as e:
			raise e

	@maxldapreferrals.setter
	def maxldapreferrals(self, maxldapreferrals) :
		r"""Specifies the maximum number of nested referrals to follow.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._maxldapreferrals = maxldapreferrals
		except Exception as e:
			raise e

	@property
	def referraldnslookup(self) :
		r"""Specifies the DNS Record lookup Type for the referrals.<br/>Default value: A-REC<br/>Possible values = A-REC, SRV-REC, MSSRV-REC.
		"""
		try :
			return self._referraldnslookup
		except Exception as e:
			raise e

	@referraldnslookup.setter
	def referraldnslookup(self, referraldnslookup) :
		r"""Specifies the DNS Record lookup Type for the referrals.<br/>Default value: A-REC<br/>Possible values = A-REC, SRV-REC, MSSRV-REC
		"""
		try :
			self._referraldnslookup = referraldnslookup
		except Exception as e:
			raise e

	@property
	def mssrvrecordlocation(self) :
		r"""MSSRV Specific parameter. Used to locate the DNS node to which the SRV record pertains in the domainname. The domainname is appended to it to form the srv record.
		Example : For "dc._msdcs", the srv record formed is _ldap._tcp.dc._msdcs.<domainname>.
		"""
		try :
			return self._mssrvrecordlocation
		except Exception as e:
			raise e

	@mssrvrecordlocation.setter
	def mssrvrecordlocation(self, mssrvrecordlocation) :
		r"""MSSRV Specific parameter. Used to locate the DNS node to which the SRV record pertains in the domainname. The domainname is appended to it to form the srv record.
		Example : For "dc._msdcs", the srv record formed is _ldap._tcp.dc._msdcs.<domainname>.
		"""
		try :
			self._mssrvrecordlocation = mssrvrecordlocation
		except Exception as e:
			raise e

	@property
	def validateservercert(self) :
		r"""When to validate LDAP server certs.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._validateservercert
		except Exception as e:
			raise e

	@validateservercert.setter
	def validateservercert(self, validateservercert) :
		r"""When to validate LDAP server certs.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._validateservercert = validateservercert
		except Exception as e:
			raise e

	@property
	def ldaphostname(self) :
		r"""Hostname for the LDAP server.  If -validateServerCert is ON then this must be the host name on the certificate from the LDAP server.
		A hostname mismatch will cause a connection failure.
		"""
		try :
			return self._ldaphostname
		except Exception as e:
			raise e

	@ldaphostname.setter
	def ldaphostname(self, ldaphostname) :
		r"""Hostname for the LDAP server.  If -validateServerCert is ON then this must be the host name on the certificate from the LDAP server.
		A hostname mismatch will cause a connection failure.
		"""
		try :
			self._ldaphostname = ldaphostname
		except Exception as e:
			raise e

	@property
	def groupnameidentifier(self) :
		r"""Name that uniquely identifies a group in LDAP or Active Directory.
		"""
		try :
			return self._groupnameidentifier
		except Exception as e:
			raise e

	@groupnameidentifier.setter
	def groupnameidentifier(self, groupnameidentifier) :
		r"""Name that uniquely identifies a group in LDAP or Active Directory.
		"""
		try :
			self._groupnameidentifier = groupnameidentifier
		except Exception as e:
			raise e

	@property
	def groupsearchattribute(self) :
		r"""LDAP group search attribute. 
		Used to determine to which groups a group belongs.
		"""
		try :
			return self._groupsearchattribute
		except Exception as e:
			raise e

	@groupsearchattribute.setter
	def groupsearchattribute(self, groupsearchattribute) :
		r"""LDAP group search attribute. 
		Used to determine to which groups a group belongs.
		"""
		try :
			self._groupsearchattribute = groupsearchattribute
		except Exception as e:
			raise e

	@property
	def groupsearchsubattribute(self) :
		r"""LDAP group search subattribute. 
		Used to determine to which groups a group belongs.
		"""
		try :
			return self._groupsearchsubattribute
		except Exception as e:
			raise e

	@groupsearchsubattribute.setter
	def groupsearchsubattribute(self, groupsearchsubattribute) :
		r"""LDAP group search subattribute. 
		Used to determine to which groups a group belongs.
		"""
		try :
			self._groupsearchsubattribute = groupsearchsubattribute
		except Exception as e:
			raise e

	@property
	def groupsearchfilter(self) :
		r"""String to be combined with the default LDAP group search string to form the search value.  For example, the group search filter ""vpnallowed=true"" when combined with the group identifier ""samaccount"" and the group name ""g1"" yields the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).
		"""
		try :
			return self._groupsearchfilter
		except Exception as e:
			raise e

	@groupsearchfilter.setter
	def groupsearchfilter(self, groupsearchfilter) :
		r"""String to be combined with the default LDAP group search string to form the search value.  For example, the group search filter ""vpnallowed=true"" when combined with the group identifier ""samaccount"" and the group name ""g1"" yields the LDAP search string ""(&(vpnallowed=true)(samaccount=g1)"". (Be sure to enclose the search string in two sets of double quotation marks; both sets are needed.).
		"""
		try :
			self._groupsearchfilter = groupsearchfilter
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		r"""Expression that would be evaluated to extract attribute1 from the ldap response.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		r"""Expression that would be evaluated to extract attribute1 from the ldap response.
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		r"""Expression that would be evaluated to extract attribute2 from the ldap response.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		r"""Expression that would be evaluated to extract attribute2 from the ldap response.
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		r"""Expression that would be evaluated to extract attribute3 from the ldap response.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		r"""Expression that would be evaluated to extract attribute3 from the ldap response.
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		r"""Expression that would be evaluated to extract attribute4 from the ldap response.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		r"""Expression that would be evaluated to extract attribute4 from the ldap response.
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		r"""Expression that would be evaluated to extract attribute5 from the ldap response.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		r"""Expression that would be evaluated to extract attribute5 from the ldap response.
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		r"""Expression that would be evaluated to extract attribute6 from the ldap response.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		r"""Expression that would be evaluated to extract attribute6 from the ldap response.
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		r"""Expression that would be evaluated to extract attribute7 from the ldap response.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		r"""Expression that would be evaluated to extract attribute7 from the ldap response.
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		r"""Expression that would be evaluated to extract attribute8 from the ldap response.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		r"""Expression that would be evaluated to extract attribute8 from the ldap response.
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		r"""Expression that would be evaluated to extract attribute9 from the ldap response.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		r"""Expression that would be evaluated to extract attribute9 from the ldap response.
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		r"""Expression that would be evaluated to extract attribute10 from the ldap response.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		r"""Expression that would be evaluated to extract attribute10 from the ldap response.
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		r"""Expression that would be evaluated to extract attribute11 from the ldap response.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		r"""Expression that would be evaluated to extract attribute11 from the ldap response.
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		r"""Expression that would be evaluated to extract attribute12 from the ldap response.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		r"""Expression that would be evaluated to extract attribute12 from the ldap response.
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		r"""Expression that would be evaluated to extract attribute13 from the ldap response.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		r"""Expression that would be evaluated to extract attribute13 from the ldap response.
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		r"""Expression that would be evaluated to extract attribute14 from the ldap response.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		r"""Expression that would be evaluated to extract attribute14 from the ldap response.
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		r"""Expression that would be evaluated to extract attribute15 from the ldap response.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		r"""Expression that would be evaluated to extract attribute15 from the ldap response.
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		r"""Expression that would be evaluated to extract attribute16 from the ldap response.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		r"""Expression that would be evaluated to extract attribute16 from the ldap response.
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def success(self) :
		try :
			return self._success
		except Exception as e:
			raise e

	@property
	def failure(self) :
		try :
			return self._failure
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationldapaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationldapaction
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
		r""" Use this API to add authenticationldapaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationldapaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.servername = resource.servername
				addresource.serverport = resource.serverport
				addresource.authtimeout = resource.authtimeout
				addresource.ldapbase = resource.ldapbase
				addresource.ldapbinddn = resource.ldapbinddn
				addresource.ldapbinddnpassword = resource.ldapbinddnpassword
				addresource.ldaploginname = resource.ldaploginname
				addresource.searchfilter = resource.searchfilter
				addresource.groupattrname = resource.groupattrname
				addresource.subattributename = resource.subattributename
				addresource.sectype = resource.sectype
				addresource.svrtype = resource.svrtype
				addresource.ssonameattribute = resource.ssonameattribute
				addresource.authentication = resource.authentication
				addresource.requireuser = resource.requireuser
				addresource.passwdchange = resource.passwdchange
				addresource.nestedgroupextraction = resource.nestedgroupextraction
				addresource.maxnestinglevel = resource.maxnestinglevel
				addresource.followreferrals = resource.followreferrals
				addresource.maxldapreferrals = resource.maxldapreferrals
				addresource.referraldnslookup = resource.referraldnslookup
				addresource.mssrvrecordlocation = resource.mssrvrecordlocation
				addresource.validateservercert = resource.validateservercert
				addresource.ldaphostname = resource.ldaphostname
				addresource.groupnameidentifier = resource.groupnameidentifier
				addresource.groupsearchattribute = resource.groupsearchattribute
				addresource.groupsearchsubattribute = resource.groupsearchsubattribute
				addresource.groupsearchfilter = resource.groupsearchfilter
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.attribute1 = resource.attribute1
				addresource.attribute2 = resource.attribute2
				addresource.attribute3 = resource.attribute3
				addresource.attribute4 = resource.attribute4
				addresource.attribute5 = resource.attribute5
				addresource.attribute6 = resource.attribute6
				addresource.attribute7 = resource.attribute7
				addresource.attribute8 = resource.attribute8
				addresource.attribute9 = resource.attribute9
				addresource.attribute10 = resource.attribute10
				addresource.attribute11 = resource.attribute11
				addresource.attribute12 = resource.attribute12
				addresource.attribute13 = resource.attribute13
				addresource.attribute14 = resource.attribute14
				addresource.attribute15 = resource.attribute15
				addresource.attribute16 = resource.attribute16
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationldapaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].servername = resource[i].servername
						addresources[i].serverport = resource[i].serverport
						addresources[i].authtimeout = resource[i].authtimeout
						addresources[i].ldapbase = resource[i].ldapbase
						addresources[i].ldapbinddn = resource[i].ldapbinddn
						addresources[i].ldapbinddnpassword = resource[i].ldapbinddnpassword
						addresources[i].ldaploginname = resource[i].ldaploginname
						addresources[i].searchfilter = resource[i].searchfilter
						addresources[i].groupattrname = resource[i].groupattrname
						addresources[i].subattributename = resource[i].subattributename
						addresources[i].sectype = resource[i].sectype
						addresources[i].svrtype = resource[i].svrtype
						addresources[i].ssonameattribute = resource[i].ssonameattribute
						addresources[i].authentication = resource[i].authentication
						addresources[i].requireuser = resource[i].requireuser
						addresources[i].passwdchange = resource[i].passwdchange
						addresources[i].nestedgroupextraction = resource[i].nestedgroupextraction
						addresources[i].maxnestinglevel = resource[i].maxnestinglevel
						addresources[i].followreferrals = resource[i].followreferrals
						addresources[i].maxldapreferrals = resource[i].maxldapreferrals
						addresources[i].referraldnslookup = resource[i].referraldnslookup
						addresources[i].mssrvrecordlocation = resource[i].mssrvrecordlocation
						addresources[i].validateservercert = resource[i].validateservercert
						addresources[i].ldaphostname = resource[i].ldaphostname
						addresources[i].groupnameidentifier = resource[i].groupnameidentifier
						addresources[i].groupsearchattribute = resource[i].groupsearchattribute
						addresources[i].groupsearchsubattribute = resource[i].groupsearchsubattribute
						addresources[i].groupsearchfilter = resource[i].groupsearchfilter
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute16 = resource[i].attribute16
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationldapaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationldapaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationldapaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationldapaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationldapaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationldapaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.servername = resource.servername
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.ldapbase = resource.ldapbase
				updateresource.ldapbinddn = resource.ldapbinddn
				updateresource.ldapbinddnpassword = resource.ldapbinddnpassword
				updateresource.ldaploginname = resource.ldaploginname
				updateresource.searchfilter = resource.searchfilter
				updateresource.groupattrname = resource.groupattrname
				updateresource.subattributename = resource.subattributename
				updateresource.sectype = resource.sectype
				updateresource.svrtype = resource.svrtype
				updateresource.ssonameattribute = resource.ssonameattribute
				updateresource.authentication = resource.authentication
				updateresource.requireuser = resource.requireuser
				updateresource.passwdchange = resource.passwdchange
				updateresource.validateservercert = resource.validateservercert
				updateresource.ldaphostname = resource.ldaphostname
				updateresource.nestedgroupextraction = resource.nestedgroupextraction
				updateresource.maxnestinglevel = resource.maxnestinglevel
				updateresource.groupnameidentifier = resource.groupnameidentifier
				updateresource.groupsearchattribute = resource.groupsearchattribute
				updateresource.groupsearchsubattribute = resource.groupsearchsubattribute
				updateresource.groupsearchfilter = resource.groupsearchfilter
				updateresource.followreferrals = resource.followreferrals
				updateresource.maxldapreferrals = resource.maxldapreferrals
				updateresource.referraldnslookup = resource.referraldnslookup
				updateresource.mssrvrecordlocation = resource.mssrvrecordlocation
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute16 = resource.attribute16
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationldapaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].servername = resource[i].servername
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].authtimeout = resource[i].authtimeout
						updateresources[i].ldapbase = resource[i].ldapbase
						updateresources[i].ldapbinddn = resource[i].ldapbinddn
						updateresources[i].ldapbinddnpassword = resource[i].ldapbinddnpassword
						updateresources[i].ldaploginname = resource[i].ldaploginname
						updateresources[i].searchfilter = resource[i].searchfilter
						updateresources[i].groupattrname = resource[i].groupattrname
						updateresources[i].subattributename = resource[i].subattributename
						updateresources[i].sectype = resource[i].sectype
						updateresources[i].svrtype = resource[i].svrtype
						updateresources[i].ssonameattribute = resource[i].ssonameattribute
						updateresources[i].authentication = resource[i].authentication
						updateresources[i].requireuser = resource[i].requireuser
						updateresources[i].passwdchange = resource[i].passwdchange
						updateresources[i].validateservercert = resource[i].validateservercert
						updateresources[i].ldaphostname = resource[i].ldaphostname
						updateresources[i].nestedgroupextraction = resource[i].nestedgroupextraction
						updateresources[i].maxnestinglevel = resource[i].maxnestinglevel
						updateresources[i].groupnameidentifier = resource[i].groupnameidentifier
						updateresources[i].groupsearchattribute = resource[i].groupsearchattribute
						updateresources[i].groupsearchsubattribute = resource[i].groupsearchsubattribute
						updateresources[i].groupsearchfilter = resource[i].groupsearchfilter
						updateresources[i].followreferrals = resource[i].followreferrals
						updateresources[i].maxldapreferrals = resource[i].maxldapreferrals
						updateresources[i].referraldnslookup = resource[i].referraldnslookup
						updateresources[i].mssrvrecordlocation = resource[i].mssrvrecordlocation
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute16 = resource[i].attribute16
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationldapaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationldapaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationldapaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationldapaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationldapaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationldapaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationldapaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationldapaction() for _ in range(len(name))]
						obj = [authenticationldapaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationldapaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationldapaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationldapaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationldapaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationldapaction()
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
		r""" Use this API to count filtered the set of authenticationldapaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationldapaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Passwdchange:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sectype:
		PLAINTEXT = "PLAINTEXT"
		TLS = "TLS"
		SSL = "SSL"

	class Authentication:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Requireuser:
		YES = "YES"
		NO = "NO"

	class Validateservercert:
		YES = "YES"
		NO = "NO"

	class Followreferrals:
		ON = "ON"
		OFF = "OFF"

	class Referraldnslookup:
		A_REC = "A-REC"
		SRV_REC = "SRV-REC"
		MSSRV_REC = "MSSRV-REC"

	class Svrtype:
		AD = "AD"
		NDS = "NDS"

	class Nestedgroupextraction:
		ON = "ON"
		OFF = "OFF"

class authenticationldapaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationldapaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationldapaction = [authenticationldapaction() for _ in range(length)]

