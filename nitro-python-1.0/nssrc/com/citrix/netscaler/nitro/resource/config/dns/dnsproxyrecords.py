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

class dnsproxyrecords(base_resource) :
	""" Configuration for proxy record resource. """
	def __init__(self) :
		self._type = None
		self._negrectype = None

	@property
	def type(self) :
		r"""Filter the DNS records to be flushed.e.g flush dns proxyRecords -type A   will flush only the A records from the cache. .<br/>Possible values = A, NS, CNAME, SOA, MX, AAAA, SRV, RRSIG, NSEC, DNSKEY, PTR, TXT, NAPTR.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Filter the DNS records to be flushed.e.g flush dns proxyRecords -type A   will flush only the A records from the cache. .<br/>Possible values = A, NS, CNAME, SOA, MX, AAAA, SRV, RRSIG, NSEC, DNSKEY, PTR, TXT, NAPTR
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def negrectype(self) :
		r"""Filter the Negative DNS records i.e NXDOMAIN and NODATA entries to be flushed. e.g flush dns proxyRecords NXDOMAIN will flush only the NXDOMAIN entries from the cache.<br/>Possible values = NXDOMAIN, NODATA.
		"""
		try :
			return self._negrectype
		except Exception as e:
			raise e

	@negrectype.setter
	def negrectype(self, negrectype) :
		r"""Filter the Negative DNS records i.e NXDOMAIN and NODATA entries to be flushed. e.g flush dns proxyRecords NXDOMAIN will flush only the NXDOMAIN entries from the cache.<br/>Possible values = NXDOMAIN, NODATA
		"""
		try :
			self._negrectype = negrectype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsproxyrecords_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsproxyrecords
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
	def flush(cls, client, resource) :
		r""" Use this API to flush dnsproxyrecords.
		"""
		try :
			if type(resource) is not list :
				flushresource = dnsproxyrecords()
				flushresource.type = resource.type
				flushresource.negrectype = resource.negrectype
				return flushresource.perform_operation(client,"flush")
		except Exception as e :
			raise e

	class Negrectype:
		NXDOMAIN = "NXDOMAIN"
		NODATA = "NODATA"

	class Type:
		A = "A"
		NS = "NS"
		CNAME = "CNAME"
		SOA = "SOA"
		MX = "MX"
		AAAA = "AAAA"
		SRV = "SRV"
		RRSIG = "RRSIG"
		NSEC = "NSEC"
		DNSKEY = "DNSKEY"
		PTR = "PTR"
		TXT = "TXT"
		NAPTR = "NAPTR"

class dnsproxyrecords_response(base_response) :
	def __init__(self, length=1) :
		self.dnsproxyrecords = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsproxyrecords = [dnsproxyrecords() for _ in range(length)]

