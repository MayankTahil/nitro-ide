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

class dnsparameter(base_resource) :
	""" Configuration for DNS parameter resource. """
	def __init__(self) :
		self._retries = None
		self._minttl = None
		self._maxttl = None
		self._cacherecords = None
		self._namelookuppriority = None
		self._recursion = None
		self._resolutionorder = None
		self._dnssec = None
		self._maxpipeline = None
		self._dnsrootreferral = None
		self._dns64timeout = None
		self._ecsmaxsubnets = None
		self._maxnegcachettl = None
		self._cachehitbypass = None
		self._maxcachesize = None
		self._maxnegativecachesize = None
		self._cachenoexpire = None
		self._splitpktqueryprocessing = None
		self._cacheecszeroprefix = None

	@property
	def retries(self) :
		r"""Maximum number of retry attempts when no response is received for a query sent to a name server. Applies to end resolver and forwarder configurations.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  5.
		"""
		try :
			return self._retries
		except Exception as e:
			raise e

	@retries.setter
	def retries(self, retries) :
		r"""Maximum number of retry attempts when no response is received for a query sent to a name server. Applies to end resolver and forwarder configurations.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  5
		"""
		try :
			self._retries = retries
		except Exception as e:
			raise e

	@property
	def minttl(self) :
		r"""Minimum permissible time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is lower than the value configured for minTTL, the TTL of the record is set to the value of minTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Maximum length =  604800.
		"""
		try :
			return self._minttl
		except Exception as e:
			raise e

	@minttl.setter
	def minttl(self, minttl) :
		r"""Minimum permissible time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is lower than the value configured for minTTL, the TTL of the record is set to the value of minTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Maximum length =  604800
		"""
		try :
			self._minttl = minttl
		except Exception as e:
			raise e

	@property
	def maxttl(self) :
		r"""Maximum time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxTTL, the TTL of the record is set to the value of maxTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800.
		"""
		try :
			return self._maxttl
		except Exception as e:
			raise e

	@maxttl.setter
	def maxttl(self, maxttl) :
		r"""Maximum time to live (TTL) for all records cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxTTL, the TTL of the record is set to the value of maxTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800
		"""
		try :
			self._maxttl = maxttl
		except Exception as e:
			raise e

	@property
	def cacherecords(self) :
		r"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacherecords
		except Exception as e:
			raise e

	@cacherecords.setter
	def cacherecords(self, cacherecords) :
		r"""Cache resource records in the DNS cache. Applies to resource records obtained through proxy configurations only. End resolver and forwarder configurations always cache records in the DNS cache, and you cannot disable this behavior. When you disable record caching, the appliance stops caching server responses. However, cached records are not flushed. The appliance does not serve requests from the cache until record caching is enabled again.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._cacherecords = cacherecords
		except Exception as e:
			raise e

	@property
	def namelookuppriority(self) :
		r"""Type of lookup (DNS or WINS) to attempt first. If the first-priority lookup fails, the second-priority lookup is attempted. Used only by the SSL VPN feature.<br/>Default value: WINS<br/>Possible values = WINS, DNS.
		"""
		try :
			return self._namelookuppriority
		except Exception as e:
			raise e

	@namelookuppriority.setter
	def namelookuppriority(self, namelookuppriority) :
		r"""Type of lookup (DNS or WINS) to attempt first. If the first-priority lookup fails, the second-priority lookup is attempted. Used only by the SSL VPN feature.<br/>Default value: WINS<br/>Possible values = WINS, DNS
		"""
		try :
			self._namelookuppriority = namelookuppriority
		except Exception as e:
			raise e

	@property
	def recursion(self) :
		r"""Function as an end resolver and recursively resolve queries for domains that are not hosted on the NetScaler appliance. Also resolve queries recursively when the external name servers configured on the appliance (for a forwarder configuration) are unavailable. When external name servers are unavailable, the appliance queries a root server and resolves the request recursively, as it does for an end resolver configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._recursion
		except Exception as e:
			raise e

	@recursion.setter
	def recursion(self, recursion) :
		r"""Function as an end resolver and recursively resolve queries for domains that are not hosted on the NetScaler appliance. Also resolve queries recursively when the external name servers configured on the appliance (for a forwarder configuration) are unavailable. When external name servers are unavailable, the appliance queries a root server and resolves the request recursively, as it does for an end resolver configuration.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._recursion = recursion
		except Exception as e:
			raise e

	@property
	def resolutionorder(self) :
		r"""Type of DNS queries (A, AAAA, or both) to generate during the routine functioning of certain NetScaler features, such as SSL VPN, cache redirection, and the integrated cache. The queries are sent to the external name servers that are configured for the forwarder function. If you specify both query types, you can also specify the order. Available settings function as follows:
		* OnlyAQuery. Send queries for IPv4 address records (A records) only. 
		* OnlyAAAAQuery. Send queries for IPv6 address records (AAAA records) instead of queries for IPv4 address records (A records).
		* AThenAAAAQuery. Send a query for an A record, and then send a query for an AAAA record if the query for the A record results in a NODATA response from the name server.
		* AAAAThenAQuery. Send a query for an AAAA record, and then send a query for an A record if the query for the AAAA record results in a NODATA response from the name server.<br/>Default value: OnlyAQuery<br/>Possible values = OnlyAQuery, OnlyAAAAQuery, AThenAAAAQuery, AAAAThenAQuery.
		"""
		try :
			return self._resolutionorder
		except Exception as e:
			raise e

	@resolutionorder.setter
	def resolutionorder(self, resolutionorder) :
		r"""Type of DNS queries (A, AAAA, or both) to generate during the routine functioning of certain NetScaler features, such as SSL VPN, cache redirection, and the integrated cache. The queries are sent to the external name servers that are configured for the forwarder function. If you specify both query types, you can also specify the order. Available settings function as follows:
		* OnlyAQuery. Send queries for IPv4 address records (A records) only. 
		* OnlyAAAAQuery. Send queries for IPv6 address records (AAAA records) instead of queries for IPv4 address records (A records).
		* AThenAAAAQuery. Send a query for an A record, and then send a query for an AAAA record if the query for the A record results in a NODATA response from the name server.
		* AAAAThenAQuery. Send a query for an AAAA record, and then send a query for an A record if the query for the AAAA record results in a NODATA response from the name server.<br/>Default value: OnlyAQuery<br/>Possible values = OnlyAQuery, OnlyAAAAQuery, AThenAAAAQuery, AAAAThenAQuery
		"""
		try :
			self._resolutionorder = resolutionorder
		except Exception as e:
			raise e

	@property
	def dnssec(self) :
		r"""Enable or disable the Domain Name System Security Extensions (DNSSEC) feature on the appliance. Note: Even when the DNSSEC feature is enabled, forwarder configurations (used by internal NetScaler features such as SSL VPN and Cache Redirection for name resolution) do not support the DNSSEC OK (DO) bit in the EDNS0 OPT header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnssec
		except Exception as e:
			raise e

	@dnssec.setter
	def dnssec(self, dnssec) :
		r"""Enable or disable the Domain Name System Security Extensions (DNSSEC) feature on the appliance. Note: Even when the DNSSEC feature is enabled, forwarder configurations (used by internal NetScaler features such as SSL VPN and Cache Redirection for name resolution) do not support the DNSSEC OK (DO) bit in the EDNS0 OPT header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnssec = dnssec
		except Exception as e:
			raise e

	@property
	def maxpipeline(self) :
		r"""Maximum number of concurrent DNS requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. A value of 0 (zero) applies no limit to the number of concurrent DNS requests allowed on a single client connection.
		"""
		try :
			return self._maxpipeline
		except Exception as e:
			raise e

	@maxpipeline.setter
	def maxpipeline(self, maxpipeline) :
		r"""Maximum number of concurrent DNS requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. A value of 0 (zero) applies no limit to the number of concurrent DNS requests allowed on a single client connection.
		"""
		try :
			self._maxpipeline = maxpipeline
		except Exception as e:
			raise e

	@property
	def dnsrootreferral(self) :
		r"""Send a root referral if a client queries a domain name that is unrelated to the domains configured/cached on the NetScaler appliance. If the setting is disabled, the appliance sends a blank response instead of a root referral. Applicable to domains for which the appliance is authoritative. Disable the parameter when the appliance is under attack from a client that is sending a flood of queries for unrelated domains.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dnsrootreferral
		except Exception as e:
			raise e

	@dnsrootreferral.setter
	def dnsrootreferral(self, dnsrootreferral) :
		r"""Send a root referral if a client queries a domain name that is unrelated to the domains configured/cached on the NetScaler appliance. If the setting is disabled, the appliance sends a blank response instead of a root referral. Applicable to domains for which the appliance is authoritative. Disable the parameter when the appliance is under attack from a client that is sending a flood of queries for unrelated domains.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dnsrootreferral = dnsrootreferral
		except Exception as e:
			raise e

	@property
	def dns64timeout(self) :
		r"""While doing DNS64 resolution, this parameter specifies the time to wait before sending an A query if no response is received from backend DNS server for AAAA query.<br/>Maximum length =  10000.
		"""
		try :
			return self._dns64timeout
		except Exception as e:
			raise e

	@dns64timeout.setter
	def dns64timeout(self, dns64timeout) :
		r"""While doing DNS64 resolution, this parameter specifies the time to wait before sending an A query if no response is received from backend DNS server for AAAA query.<br/>Maximum length =  10000
		"""
		try :
			self._dns64timeout = dns64timeout
		except Exception as e:
			raise e

	@property
	def ecsmaxsubnets(self) :
		r"""Maximum number of subnets that can be cached corresponding to a single domain. Subnet caching will occur for responses with EDNS Client Subnet (ECS) option. Caching of such responses can be disabled using DNS profile settings. A value of zero indicates that the number of subnets cached is limited only by existing memory constraints. The default value is zero.<br/>Default value: 0<br/>Maximum length =  1280.
		"""
		try :
			return self._ecsmaxsubnets
		except Exception as e:
			raise e

	@ecsmaxsubnets.setter
	def ecsmaxsubnets(self, ecsmaxsubnets) :
		r"""Maximum number of subnets that can be cached corresponding to a single domain. Subnet caching will occur for responses with EDNS Client Subnet (ECS) option. Caching of such responses can be disabled using DNS profile settings. A value of zero indicates that the number of subnets cached is limited only by existing memory constraints. The default value is zero.<br/>Default value: 0<br/>Maximum length =  1280
		"""
		try :
			self._ecsmaxsubnets = ecsmaxsubnets
		except Exception as e:
			raise e

	@property
	def maxnegcachettl(self) :
		r"""Maximum time to live (TTL) for all negative records ( NXDONAIN and NODATA ) cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxnegcacheTTL, the TTL of the record is set to the value of maxnegcacheTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800.
		"""
		try :
			return self._maxnegcachettl
		except Exception as e:
			raise e

	@maxnegcachettl.setter
	def maxnegcachettl(self, maxnegcachettl) :
		r"""Maximum time to live (TTL) for all negative records ( NXDONAIN and NODATA ) cached in the DNS cache by DNS proxy, end resolver, and forwarder configurations. If the TTL of a record that is to be cached is higher than the value configured for maxnegcacheTTL, the TTL of the record is set to the value of maxnegcacheTTL before caching. When you modify this setting, the new value is applied only to those records that are cached after the modification. The TTL values of existing records are not changed.<br/>Default value: 604800<br/>Minimum length =  1<br/>Maximum length =  604800
		"""
		try :
			self._maxnegcachettl = maxnegcachettl
		except Exception as e:
			raise e

	@property
	def cachehitbypass(self) :
		r"""This parameter is applicable only in proxy mode and if this parameter is enabled  we will forward all the client requests to the backend DNS server and the response served will be cached on netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cachehitbypass
		except Exception as e:
			raise e

	@cachehitbypass.setter
	def cachehitbypass(self, cachehitbypass) :
		r"""This parameter is applicable only in proxy mode and if this parameter is enabled  we will forward all the client requests to the backend DNS server and the response served will be cached on netscaler.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cachehitbypass = cachehitbypass
		except Exception as e:
			raise e

	@property
	def maxcachesize(self) :
		r"""Maximum memory, in megabytes, that can be used for dns caching per Packet Engine.
		"""
		try :
			return self._maxcachesize
		except Exception as e:
			raise e

	@maxcachesize.setter
	def maxcachesize(self, maxcachesize) :
		r"""Maximum memory, in megabytes, that can be used for dns caching per Packet Engine.
		"""
		try :
			self._maxcachesize = maxcachesize
		except Exception as e:
			raise e

	@property
	def maxnegativecachesize(self) :
		r"""Maximum memory, in megabytes, that can be used for caching of negative DNS responses per packet engine.
		"""
		try :
			return self._maxnegativecachesize
		except Exception as e:
			raise e

	@maxnegativecachesize.setter
	def maxnegativecachesize(self, maxnegativecachesize) :
		r"""Maximum memory, in megabytes, that can be used for caching of negative DNS responses per packet engine.
		"""
		try :
			self._maxnegativecachesize = maxnegativecachesize
		except Exception as e:
			raise e

	@property
	def cachenoexpire(self) :
		r"""If this flag is set to YES, the existing entries in cache do not age out. On reaching the max limit the cache records are frozen.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cachenoexpire
		except Exception as e:
			raise e

	@cachenoexpire.setter
	def cachenoexpire(self, cachenoexpire) :
		r"""If this flag is set to YES, the existing entries in cache do not age out. On reaching the max limit the cache records are frozen.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cachenoexpire = cachenoexpire
		except Exception as e:
			raise e

	@property
	def splitpktqueryprocessing(self) :
		r"""Processing requests split across multiple packets.<br/>Default value: ALLOW<br/>Possible values = ALLOW, DROP.
		"""
		try :
			return self._splitpktqueryprocessing
		except Exception as e:
			raise e

	@splitpktqueryprocessing.setter
	def splitpktqueryprocessing(self, splitpktqueryprocessing) :
		r"""Processing requests split across multiple packets.<br/>Default value: ALLOW<br/>Possible values = ALLOW, DROP
		"""
		try :
			self._splitpktqueryprocessing = splitpktqueryprocessing
		except Exception as e:
			raise e

	@property
	def cacheecszeroprefix(self) :
		r"""Cache ECS responses with a Scope Prefix length of zero. Such a cached response will be used for all queries with this domain name and any subnet. When disabled, ECS responses with Scope Prefix length of zero will be cached, but not tied to any subnet. This option has no effect if caching of ECS responses is disabled in the corresponding DNS profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cacheecszeroprefix
		except Exception as e:
			raise e

	@cacheecszeroprefix.setter
	def cacheecszeroprefix(self, cacheecszeroprefix) :
		r"""Cache ECS responses with a Scope Prefix length of zero. Such a cached response will be used for all queries with this domain name and any subnet. When disabled, ECS responses with Scope Prefix length of zero will be cached, but not tied to any subnet. This option has no effect if caching of ECS responses is disabled in the corresponding DNS profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cacheecszeroprefix = cacheecszeroprefix
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsparameter
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
		r""" Use this API to update dnsparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = dnsparameter()
				updateresource.retries = resource.retries
				updateresource.minttl = resource.minttl
				updateresource.maxttl = resource.maxttl
				updateresource.cacherecords = resource.cacherecords
				updateresource.namelookuppriority = resource.namelookuppriority
				updateresource.recursion = resource.recursion
				updateresource.resolutionorder = resource.resolutionorder
				updateresource.dnssec = resource.dnssec
				updateresource.maxpipeline = resource.maxpipeline
				updateresource.dnsrootreferral = resource.dnsrootreferral
				updateresource.dns64timeout = resource.dns64timeout
				updateresource.ecsmaxsubnets = resource.ecsmaxsubnets
				updateresource.maxnegcachettl = resource.maxnegcachettl
				updateresource.cachehitbypass = resource.cachehitbypass
				updateresource.maxcachesize = resource.maxcachesize
				updateresource.maxnegativecachesize = resource.maxnegativecachesize
				updateresource.cachenoexpire = resource.cachenoexpire
				updateresource.splitpktqueryprocessing = resource.splitpktqueryprocessing
				updateresource.cacheecszeroprefix = resource.cacheecszeroprefix
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnsparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnsparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Recursion:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Namelookuppriority:
		WINS = "WINS"
		DNS = "DNS"

	class Cacheecszeroprefix:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Resolutionorder:
		OnlyAQuery = "OnlyAQuery"
		OnlyAAAAQuery = "OnlyAAAAQuery"
		AThenAAAAQuery = "AThenAAAAQuery"
		AAAAThenAQuery = "AAAAThenAQuery"

	class Cacherecords:
		YES = "YES"
		NO = "NO"

	class Splitpktqueryprocessing:
		ALLOW = "ALLOW"
		DROP = "DROP"

	class Dnsrootreferral:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachenoexpire:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dnssec:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachehitbypass:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class dnsparameter_response(base_response) :
	def __init__(self, length=1) :
		self.dnsparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsparameter = [dnsparameter() for _ in range(length)]

