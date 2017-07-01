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

class servicegroupmember_stats(base_resource) :
	r""" Statistics for service group entity resource.
	"""
	def __init__(self) :
		self._servicegroupname = None
		self._ip = None
		self._servername = None
		self._port = None
		self._clearstats = None
		self._avgsvrttfb = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._servicetype = ""
		self._state = ""
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0
		self._curclntconnections = 0
		self._surgecount = 0
		self._cursrvrconnections = 0
		self._svrestablishedconn = 0
		self._curreusepool = 0
		self._maxclients = 0
		self._totsvrttlbtransactions = 0
		self._toleratingttlbtransactions = 0
		self._frustratingttlbtransactions = 0

	@property
	def servicegroupname(self) :
		r"""Displays statistics for the specified service group.Name of the service group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my servicegroup" or 'my servicegroup').<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Displays statistics for the specified service group.Name of the service group. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. 
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my servicegroup" or 'my servicegroup').
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""IP address of the service group. Mutually exclusive with the server name parameter.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@ip.setter
	def ip(self, ip) :
		r"""IP address of the service group. Mutually exclusive with the server name parameter.
		"""
		try :
			self._ip = ip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the server. Mutually exclusive with the IP address parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the server. Mutually exclusive with the IP address parameter.
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number of the service group member.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number of the service group member.
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def svrestablishedconn(self) :
		r"""Number of server connections in ESTABLISHED state.
		"""
		try :
			return self._svrestablishedconn
		except Exception as e:
			raise e

	@property
	def curclntconnections(self) :
		r"""Number of current client connections.
		"""
		try :
			return self._curclntconnections
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""The service type of this service.Possible values are ADNS, DNS, MYSQL, RTSP, SSL_DIAMETER, ADNS_TCP, DNS_TCP, NNTP, SIP_UDP, SSL_TCP, ANY, FTP, RADIUS, SNMP, TCP, DHCPRA, HTTP, RDP, SSL, TFTP, DIAMETER, MSSQL, RPCSVR, SSL_BRIDGE, UDP.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@property
	def totalrequests(self) :
		r"""Total number of requests received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalrequests
		except Exception as e:
			raise e

	@property
	def surgecount(self) :
		r"""Number of requests in the surge queue.
		"""
		try :
			return self._surgecount
		except Exception as e:
			raise e

	@property
	def responsebytesrate(self) :
		r"""Rate (/s) counter for totalresponsebytes.
		"""
		try :
			return self._responsebytesrate
		except Exception as e:
			raise e

	@property
	def totalresponses(self) :
		r"""Number of responses received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalresponses
		except Exception as e:
			raise e

	@property
	def requestbytesrate(self) :
		r"""Rate (/s) counter for totalrequestbytes.
		"""
		try :
			return self._requestbytesrate
		except Exception as e:
			raise e

	@property
	def cursrvrconnections(self) :
		r"""Number of current connections to the actual servers behind the virtual server.
		"""
		try :
			return self._cursrvrconnections
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		r"""The IP address on which the service is running.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def toleratingttlbtransactions(self) :
		r"""Tolerable transactions based on APDEX threshold (>T && <4T).
		"""
		try :
			return self._toleratingttlbtransactions
		except Exception as e:
			raise e

	@property
	def responsesrate(self) :
		r"""Rate (/s) counter for totalresponses.
		"""
		try :
			return self._responsesrate
		except Exception as e:
			raise e

	@property
	def maxclients(self) :
		r"""Maximum open connections allowed on this service.
		"""
		try :
			return self._maxclients
		except Exception as e:
			raise e

	@property
	def avgsvrttfb(self) :
		r"""Average TTFB between the NetScaler appliance and the server.TTFB is the time interval between sending the request packet to a service and receiving the first response from the service.
		"""
		try :
			return self._avgsvrttfb
		except Exception as e:
			raise e

	@property
	def totalrequestbytes(self) :
		r"""Total number of request bytes received on this service or virtual server.
		"""
		try :
			return self._totalrequestbytes
		except Exception as e:
			raise e

	@property
	def curreusepool(self) :
		r"""Number of requests in the idle queue/reuse pool.
		"""
		try :
			return self._curreusepool
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service).
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def totsvrttlbtransactions(self) :
		r"""Total transactions where server TTLB is calculated.
		"""
		try :
			return self._totsvrttlbtransactions
		except Exception as e:
			raise e

	@property
	def frustratingttlbtransactions(self) :
		r"""Frustrating transactions based on APDEX threshold (>4T).
		"""
		try :
			return self._frustratingttlbtransactions
		except Exception as e:
			raise e

	@property
	def totalresponsebytes(self) :
		r"""Number of response bytes received by this service or virtual server.
		"""
		try :
			return self._totalresponsebytes
		except Exception as e:
			raise e

	@property
	def primaryport(self) :
		r"""The port on which the service is running.
		"""
		try :
			return self._primaryport
		except Exception as e:
			raise e

	@property
	def requestsrate(self) :
		r"""Rate (/s) counter for totalrequests.
		"""
		try :
			return self._requestsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(servicegroupmember_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroupmember
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all servicegroupmember_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = servicegroupmember_stats()
			if not option_ :
				option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(name)
			response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class servicegroupmember_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroupmember = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroupmember = [servicegroupmember_stats() for _ in range(length)]

