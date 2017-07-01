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

class mapdomain_stats(base_resource) :
	r""" Statistics for MAP-T Map Domain resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._maptotv6rxpktstcp = 0
		self._mapv6rxpktstcprate = 0
		self._maptotv6txpktstcp = 0
		self._mapv6txpktstcprate = 0
		self._maptotv6rxbytestcp = 0
		self._mapv6rxbytestcprate = 0
		self._maptotv6txbytestcp = 0
		self._mapv6txbytestcprate = 0
		self._maptotv4rxpktstcp = 0
		self._mapv4rxpktstcprate = 0
		self._maptotv4txpktstcp = 0
		self._mapv4txpktstcprate = 0
		self._maptotv4rxbytestcp = 0
		self._mapv4rxbytestcprate = 0
		self._maptotv4txbytestcp = 0
		self._mapv4txbytestcprate = 0
		self._maptotv6rxpktsudp = 0
		self._mapv6rxpktsudprate = 0
		self._maptotv6txpktsudp = 0
		self._mapv6txpktsudprate = 0
		self._maptotv6rxbytesudp = 0
		self._mapv6rxbytesudprate = 0
		self._maptotv6txbytesudp = 0
		self._mapv6txbytesudprate = 0
		self._maptotv4rxpktsudp = 0
		self._mapv4rxpktsudprate = 0
		self._maptotv4txpktsudp = 0
		self._mapv4txpktsudprate = 0
		self._maptotv4rxbytesudp = 0
		self._mapv4rxbytesudprate = 0
		self._maptotv4txbytesudp = 0
		self._mapv4txbytesudprate = 0
		self._maptotv6rxpktsicmp = 0
		self._mapv6rxpktsicmprate = 0
		self._maptotv6txpktsicmp = 0
		self._mapv6txpktsicmprate = 0
		self._maptotv6rxbytesicmp = 0
		self._mapv6rxbytesicmprate = 0
		self._maptotv6txbytesicmp = 0
		self._mapv6txbytesicmprate = 0
		self._maptotv4rxpktsicmp = 0
		self._mapv4rxpktsicmprate = 0
		self._maptotv4txpktsicmp = 0
		self._mapv4txpktsicmprate = 0
		self._maptotv4rxbytesicmp = 0
		self._mapv4rxbytesicmprate = 0
		self._maptotv4txbytesicmp = 0
		self._mapv4txbytesicmprate = 0
		self._maptotv6rxpkts = 0
		self._mapv6rxpktsrate = 0
		self._maptotv6txpkts = 0
		self._mapv6txpktsrate = 0
		self._maptotv4rxpkts = 0
		self._mapv4rxpktsrate = 0
		self._maptotv4txpkts = 0
		self._mapv4txpktsrate = 0

	@property
	def name(self) :
		r"""An integer specifying the VLAN identification number (VID). Possible values: 1 through 4094.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""An integer specifying the VLAN identification number (VID). Possible values: 1 through 4094.
		"""
		try :
			self._name = name
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
	def mapv6rxpktsrate(self) :
		r"""Rate (/s) counter for maptotv6rxpkts.
		"""
		try :
			return self._mapv6rxpktsrate
		except Exception as e:
			raise e

	@property
	def mapv6txbytesicmprate(self) :
		r"""Rate (/s) counter for maptotv6txbytesicmp.
		"""
		try :
			return self._mapv6txbytesicmprate
		except Exception as e:
			raise e

	@property
	def mapv6rxbytesicmprate(self) :
		r"""Rate (/s) counter for maptotv6rxbytesicmp.
		"""
		try :
			return self._mapv6rxbytesicmprate
		except Exception as e:
			raise e

	@property
	def maptotv4txbytesudp(self) :
		r"""Total number of MAP-T IPv4 UDP Transmitted Bytes.
		"""
		try :
			return self._maptotv4txbytesudp
		except Exception as e:
			raise e

	@property
	def mapv4txbytestcprate(self) :
		r"""Rate (/s) counter for maptotv4txbytestcp.
		"""
		try :
			return self._mapv4txbytestcprate
		except Exception as e:
			raise e

	@property
	def mapv4txpktsrate(self) :
		r"""Rate (/s) counter for maptotv4txpkts.
		"""
		try :
			return self._mapv4txpktsrate
		except Exception as e:
			raise e

	@property
	def mapv4rxbytesicmprate(self) :
		r"""Rate (/s) counter for maptotv4rxbytesicmp.
		"""
		try :
			return self._mapv4rxbytesicmprate
		except Exception as e:
			raise e

	@property
	def mapv4txbytesudprate(self) :
		r"""Rate (/s) counter for maptotv4txbytesudp.
		"""
		try :
			return self._mapv4txbytesudprate
		except Exception as e:
			raise e

	@property
	def maptotv4txpktstcp(self) :
		r"""Total number of MAP-T IPv4 TCP Transmitted packets.
		"""
		try :
			return self._maptotv4txpktstcp
		except Exception as e:
			raise e

	@property
	def maptotv6txbytestcp(self) :
		r"""Total number of MAP-T IPv6 TCP Transmitted Bytes.
		"""
		try :
			return self._maptotv6txbytestcp
		except Exception as e:
			raise e

	@property
	def mapv4rxpktsrate(self) :
		r"""Rate (/s) counter for maptotv4rxpkts.
		"""
		try :
			return self._mapv4rxpktsrate
		except Exception as e:
			raise e

	@property
	def maptotv6txbytesudp(self) :
		r"""Total number of MAP-T IPv6 UDP Transmitted Bytes.
		"""
		try :
			return self._maptotv6txbytesudp
		except Exception as e:
			raise e

	@property
	def maptotv4rxbytesicmp(self) :
		r"""Total number of MAP-T IPv4 ICMP Recieved Bytes.
		"""
		try :
			return self._maptotv4rxbytesicmp
		except Exception as e:
			raise e

	@property
	def maptotv4txpktsicmp(self) :
		r"""Total number of MAP-T IPv4 ICMP Transmitted packets.
		"""
		try :
			return self._maptotv4txpktsicmp
		except Exception as e:
			raise e

	@property
	def maptotv4rxpktsudp(self) :
		r"""Total number of MAP-T IPv4 UDP Recieved packets.
		"""
		try :
			return self._maptotv4rxpktsudp
		except Exception as e:
			raise e

	@property
	def maptotv6txpkts(self) :
		r"""Total number of MAP-T V6 Transmitted packets.
		"""
		try :
			return self._maptotv6txpkts
		except Exception as e:
			raise e

	@property
	def maptotv4rxbytestcp(self) :
		r"""Total number of MAP-T IPv4 TCP Recieved Bytes.
		"""
		try :
			return self._maptotv4rxbytestcp
		except Exception as e:
			raise e

	@property
	def mapv4txbytesicmprate(self) :
		r"""Rate (/s) counter for maptotv4txbytesicmp.
		"""
		try :
			return self._mapv4txbytesicmprate
		except Exception as e:
			raise e

	@property
	def maptotv6rxbytesudp(self) :
		r"""Total number of MAP-T IPv6 UDP Recieved Bytes.
		"""
		try :
			return self._maptotv6rxbytesudp
		except Exception as e:
			raise e

	@property
	def maptotv6rxbytestcp(self) :
		r"""Total number of MAP-T IPv6 TCP Recieved Bytes.
		"""
		try :
			return self._maptotv6rxbytestcp
		except Exception as e:
			raise e

	@property
	def mapv6rxbytestcprate(self) :
		r"""Rate (/s) counter for maptotv6rxbytestcp.
		"""
		try :
			return self._mapv6rxbytestcprate
		except Exception as e:
			raise e

	@property
	def maptotv6rxpkts(self) :
		r"""Total number of MAP-T V6 Recieved packets.
		"""
		try :
			return self._maptotv6rxpkts
		except Exception as e:
			raise e

	@property
	def maptotv6rxpktstcp(self) :
		r"""Total number of MAP-T IPv6 TCP Recieved packets.
		"""
		try :
			return self._maptotv6rxpktstcp
		except Exception as e:
			raise e

	@property
	def maptotv4txpktsudp(self) :
		r"""Total number of MAP-T IPv4 UDP Transmitted packets.
		"""
		try :
			return self._maptotv4txpktsudp
		except Exception as e:
			raise e

	@property
	def maptotv6txpktsudp(self) :
		r"""Total number of MAP-T IPv6 UDP Transmitted packets.
		"""
		try :
			return self._maptotv6txpktsudp
		except Exception as e:
			raise e

	@property
	def mapv4rxbytestcprate(self) :
		r"""Rate (/s) counter for maptotv4rxbytestcp.
		"""
		try :
			return self._mapv4rxbytestcprate
		except Exception as e:
			raise e

	@property
	def mapv4rxpktsicmprate(self) :
		r"""Rate (/s) counter for maptotv4rxpktsicmp.
		"""
		try :
			return self._mapv4rxpktsicmprate
		except Exception as e:
			raise e

	@property
	def maptotv4rxpkts(self) :
		r"""Total number of MAP-T V4 Recieved packets.
		"""
		try :
			return self._maptotv4rxpkts
		except Exception as e:
			raise e

	@property
	def maptotv6rxpktsicmp(self) :
		r"""Total number of MAP-T IPv6 ICMP Recieved packets.
		"""
		try :
			return self._maptotv6rxpktsicmp
		except Exception as e:
			raise e

	@property
	def maptotv6rxbytesicmp(self) :
		r"""Total number of MAP-T IPv6 ICMP Recieved Bytes.
		"""
		try :
			return self._maptotv6rxbytesicmp
		except Exception as e:
			raise e

	@property
	def mapv6rxpktsudprate(self) :
		r"""Rate (/s) counter for maptotv6rxpktsudp.
		"""
		try :
			return self._mapv6rxpktsudprate
		except Exception as e:
			raise e

	@property
	def maptotv4txbytesicmp(self) :
		r"""Total number of MAP-T IPv4 ICMP Transmitted Bytes.
		"""
		try :
			return self._maptotv4txbytesicmp
		except Exception as e:
			raise e

	@property
	def mapv4txpktsicmprate(self) :
		r"""Rate (/s) counter for maptotv4txpktsicmp.
		"""
		try :
			return self._mapv4txpktsicmprate
		except Exception as e:
			raise e

	@property
	def maptotv6txpktstcp(self) :
		r"""Total number of MAP-T IPv6 TCP Transmitted packets.
		"""
		try :
			return self._maptotv6txpktstcp
		except Exception as e:
			raise e

	@property
	def mapv6txpktsrate(self) :
		r"""Rate (/s) counter for maptotv6txpkts.
		"""
		try :
			return self._mapv6txpktsrate
		except Exception as e:
			raise e

	@property
	def mapv6rxpktsicmprate(self) :
		r"""Rate (/s) counter for maptotv6rxpktsicmp.
		"""
		try :
			return self._mapv6rxpktsicmprate
		except Exception as e:
			raise e

	@property
	def maptotv4txpkts(self) :
		r"""Total number of MAP-T V4 Transmitted packets.
		"""
		try :
			return self._maptotv4txpkts
		except Exception as e:
			raise e

	@property
	def mapv6txpktsudprate(self) :
		r"""Rate (/s) counter for maptotv6txpktsudp.
		"""
		try :
			return self._mapv6txpktsudprate
		except Exception as e:
			raise e

	@property
	def maptotv6txpktsicmp(self) :
		r"""Total number of MAP-T IPv6 ICMP Transmitted packets.
		"""
		try :
			return self._maptotv6txpktsicmp
		except Exception as e:
			raise e

	@property
	def mapv6txbytestcprate(self) :
		r"""Rate (/s) counter for maptotv6txbytestcp.
		"""
		try :
			return self._mapv6txbytestcprate
		except Exception as e:
			raise e

	@property
	def maptotv4rxpktstcp(self) :
		r"""Total number of MAP-T IPv4 TCP Recieved packets.
		"""
		try :
			return self._maptotv4rxpktstcp
		except Exception as e:
			raise e

	@property
	def mapv4rxpktstcprate(self) :
		r"""Rate (/s) counter for maptotv4rxpktstcp.
		"""
		try :
			return self._mapv4rxpktstcprate
		except Exception as e:
			raise e

	@property
	def mapv4rxpktsudprate(self) :
		r"""Rate (/s) counter for maptotv4rxpktsudp.
		"""
		try :
			return self._mapv4rxpktsudprate
		except Exception as e:
			raise e

	@property
	def maptotv4rxpktsicmp(self) :
		r"""Total number of MAP-T IPv4 ICMP Recieved packets.
		"""
		try :
			return self._maptotv4rxpktsicmp
		except Exception as e:
			raise e

	@property
	def mapv4txpktsudprate(self) :
		r"""Rate (/s) counter for maptotv4txpktsudp.
		"""
		try :
			return self._mapv4txpktsudprate
		except Exception as e:
			raise e

	@property
	def maptotv6txbytesicmp(self) :
		r"""Total number of MAP-T IPv6 ICMP Transmitted Bytes.
		"""
		try :
			return self._maptotv6txbytesicmp
		except Exception as e:
			raise e

	@property
	def mapv4txpktstcprate(self) :
		r"""Rate (/s) counter for maptotv4txpktstcp.
		"""
		try :
			return self._mapv4txpktstcprate
		except Exception as e:
			raise e

	@property
	def maptotv6rxpktsudp(self) :
		r"""Total number of MAP-T IPv6 UDP Recieved packets.
		"""
		try :
			return self._maptotv6rxpktsudp
		except Exception as e:
			raise e

	@property
	def maptotv4txbytestcp(self) :
		r"""Total number of MAP-T IPv4 TCP Transmitted Bytes.
		"""
		try :
			return self._maptotv4txbytestcp
		except Exception as e:
			raise e

	@property
	def maptotv4rxbytesudp(self) :
		r"""Total number of MAP-T IPv4 UDP Recieved Bytes.
		"""
		try :
			return self._maptotv4rxbytesudp
		except Exception as e:
			raise e

	@property
	def mapv6txpktstcprate(self) :
		r"""Rate (/s) counter for maptotv6txpktstcp.
		"""
		try :
			return self._mapv6txpktstcprate
		except Exception as e:
			raise e

	@property
	def mapv6rxbytesudprate(self) :
		r"""Rate (/s) counter for maptotv6rxbytesudp.
		"""
		try :
			return self._mapv6rxbytesudprate
		except Exception as e:
			raise e

	@property
	def mapv4rxbytesudprate(self) :
		r"""Rate (/s) counter for maptotv4rxbytesudp.
		"""
		try :
			return self._mapv4rxbytesudprate
		except Exception as e:
			raise e

	@property
	def mapv6txbytesudprate(self) :
		r"""Rate (/s) counter for maptotv6txbytesudp.
		"""
		try :
			return self._mapv6txbytesudprate
		except Exception as e:
			raise e

	@property
	def mapv6rxpktstcprate(self) :
		r"""Rate (/s) counter for maptotv6rxpktstcp.
		"""
		try :
			return self._mapv6rxpktstcprate
		except Exception as e:
			raise e

	@property
	def mapv6txpktsicmprate(self) :
		r"""Rate (/s) counter for maptotv6txpktsicmp.
		"""
		try :
			return self._mapv6txpktsicmprate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(mapdomain_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mapdomain
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all mapdomain_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = mapdomain_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class mapdomain_response(base_response) :
	def __init__(self, length=1) :
		self.mapdomain = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.mapdomain = [mapdomain_stats() for _ in range(length)]

