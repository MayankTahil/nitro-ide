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

class lsnnat64_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._lsncurnat64sessions = 0
		self._lsncurnat64sessionsrate = 0
		self._lsnnat64cursubscribers = 0
		self._lsnnat64cursubscribersrate = 0
		self._lsntotnat64rxpkts = 0
		self._lsnnat64rxpktsrate = 0
		self._lsntotnat64rxbytes = 0
		self._lsnnat64rxbytesrate = 0
		self._lsntotnat64txpkts = 0
		self._lsnnat64txpktsrate = 0
		self._lsntotnat64txbytes = 0
		self._lsnnat64txbytesrate = 0
		self._lsncurnat64tcpsessions = 0
		self._lsncurnat64tcpsessionsrate = 0
		self._lsntotnat64tcprxpkts = 0
		self._lsnnat64tcprxpktsrate = 0
		self._lsntotnat64tcprxbytes = 0
		self._lsnnat64tcprxbytesrate = 0
		self._lsntotnat64tcptxpkts = 0
		self._lsnnat64tcptxpktsrate = 0
		self._lsntotnat64tcptxbytes = 0
		self._lsnnat64tcptxbytesrate = 0
		self._lsntotnat64tcpdrppkts = 0
		self._lsnnat64tcpdrppktsrate = 0
		self._lsncurnat64udpsessions = 0
		self._lsncurnat64udpsessionsrate = 0
		self._lsntotnat64udprxpkts = 0
		self._lsnnat64udprxpktsrate = 0
		self._lsntotnat64udprxbytes = 0
		self._lsnnat64udprxbytesrate = 0
		self._lsntotnat64udptxpkts = 0
		self._lsnnat64udptxpktsrate = 0
		self._lsntotnat64udptxbytes = 0
		self._lsnnat64udptxbytesrate = 0
		self._lsntotnat64udpdrppkts = 0
		self._lsnnat64udpdrppktsrate = 0
		self._lsncurnat64icmpsessions = 0
		self._lsncurnat64icmpsessionsrate = 0
		self._lsntotnat64icmprxpkts = 0
		self._lsnnat64icmprxpktsrate = 0
		self._lsntotnat64icmprxbytes = 0
		self._lsnnat64icmprxbytesrate = 0
		self._lsntotnat64icmptxpkts = 0
		self._lsnnat64icmptxpktsrate = 0
		self._lsntotnat64icmptxbytes = 0
		self._lsnnat64icmptxbytesrate = 0
		self._lsntotnat64icmpdrppkts = 0
		self._lsnnat64icmpdrppktsrate = 0

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
	def lsnnat64icmptxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64icmptxbytes.
		"""
		try :
			return self._lsnnat64icmptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64icmprxpkts(self) :
		r"""Number of LSN NAT64 ICMP Received packets.
		"""
		try :
			return self._lsntotnat64icmprxpkts
		except Exception as e:
			raise e

	@property
	def lsnnat64tcptxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64tcptxpkts.
		"""
		try :
			return self._lsnnat64tcptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsncurnat64icmpsessions(self) :
		r"""Number of LSN NAT64 ICMP Current Sessions.
		"""
		try :
			return self._lsncurnat64icmpsessions
		except Exception as e:
			raise e

	@property
	def lsnnat64rxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64rxpkts.
		"""
		try :
			return self._lsnnat64rxpktsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64udptxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64udptxbytes.
		"""
		try :
			return self._lsnnat64udptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64udprxbytes(self) :
		r"""Number of LSN NAT64 UDP Received bytes.
		"""
		try :
			return self._lsntotnat64udprxbytes
		except Exception as e:
			raise e

	@property
	def lsntotnat64rxpkts(self) :
		r"""Total number of LSN NAT64 rx pkts.
		"""
		try :
			return self._lsntotnat64rxpkts
		except Exception as e:
			raise e

	@property
	def lsnnat64txpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64txpkts.
		"""
		try :
			return self._lsnnat64txpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64icmptxpkts(self) :
		r"""Number of LSN NAT64 ICMP Transmitted packets.
		"""
		try :
			return self._lsntotnat64icmptxpkts
		except Exception as e:
			raise e

	@property
	def lsntotnat64udpdrppkts(self) :
		r"""Number of LSN NAT64 UDP Dropped packets.
		"""
		try :
			return self._lsntotnat64udpdrppkts
		except Exception as e:
			raise e

	@property
	def lsncurnat64udpsessionsrate(self) :
		r"""Rate (/s) counter for lsncurnat64udpsessions.
		"""
		try :
			return self._lsncurnat64udpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsncurnat64tcpsessions(self) :
		r"""Number of LSN NAT64 TCP Current Sessions.
		"""
		try :
			return self._lsncurnat64tcpsessions
		except Exception as e:
			raise e

	@property
	def lsntotnat64tcptxbytes(self) :
		r"""Number of LSN NAT64 TCP Transmitted bytes.
		"""
		try :
			return self._lsntotnat64tcptxbytes
		except Exception as e:
			raise e

	@property
	def lsntotnat64txbytes(self) :
		r"""Total number of LSN NAT64 tx bytes.
		"""
		try :
			return self._lsntotnat64txbytes
		except Exception as e:
			raise e

	@property
	def lsnnat64txbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64txbytes.
		"""
		try :
			return self._lsnnat64txbytesrate
		except Exception as e:
			raise e

	@property
	def lsncurnat64sessions(self) :
		r"""Current number of LSN NAT64 sessions.
		"""
		try :
			return self._lsncurnat64sessions
		except Exception as e:
			raise e

	@property
	def lsnnat64icmpdrppktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64icmpdrppkts.
		"""
		try :
			return self._lsnnat64icmpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64udptxbytes(self) :
		r"""Number of LSN NAT64 UDP Transmitted bytes.
		"""
		try :
			return self._lsntotnat64udptxbytes
		except Exception as e:
			raise e

	@property
	def lsncurnat64icmpsessionsrate(self) :
		r"""Rate (/s) counter for lsncurnat64icmpsessions.
		"""
		try :
			return self._lsncurnat64icmpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64tcprxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64tcprxpkts.
		"""
		try :
			return self._lsnnat64tcprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64icmptxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64icmptxpkts.
		"""
		try :
			return self._lsnnat64icmptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64udpdrppktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64udpdrppkts.
		"""
		try :
			return self._lsnnat64udpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64txpkts(self) :
		r"""Total number of LSN NAT64 tx pkts.
		"""
		try :
			return self._lsntotnat64txpkts
		except Exception as e:
			raise e

	@property
	def lsncurnat64udpsessions(self) :
		r"""Number of LSN NAT64 UDP Current Sessions.
		"""
		try :
			return self._lsncurnat64udpsessions
		except Exception as e:
			raise e

	@property
	def lsntotnat64tcprxpkts(self) :
		r"""Number of LSN NAT64 TCP Received packets.
		"""
		try :
			return self._lsntotnat64tcprxpkts
		except Exception as e:
			raise e

	@property
	def lsnnat64tcpdrppktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64tcpdrppkts.
		"""
		try :
			return self._lsnnat64tcpdrppktsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64tcptxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64tcptxbytes.
		"""
		try :
			return self._lsnnat64tcptxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64icmptxbytes(self) :
		r"""Number of LSN NAT64 ICMP Transmitted bytes.
		"""
		try :
			return self._lsntotnat64icmptxbytes
		except Exception as e:
			raise e

	@property
	def lsnnat64udptxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64udptxpkts.
		"""
		try :
			return self._lsnnat64udptxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64tcptxpkts(self) :
		r"""Number of LSN NAT64 TCP Transmitted packets.
		"""
		try :
			return self._lsntotnat64tcptxpkts
		except Exception as e:
			raise e

	@property
	def lsnnat64tcprxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64tcprxbytes.
		"""
		try :
			return self._lsnnat64tcprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsnnat64icmprxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64icmprxpkts.
		"""
		try :
			return self._lsnnat64icmprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64udprxpkts(self) :
		r"""Number of LSN NAT64 UDP Received packets.
		"""
		try :
			return self._lsntotnat64udprxpkts
		except Exception as e:
			raise e

	@property
	def lsntotnat64tcpdrppkts(self) :
		r"""Number of LSN NAT64 TCP Dropped packets.
		"""
		try :
			return self._lsntotnat64tcpdrppkts
		except Exception as e:
			raise e

	@property
	def lsncurnat64tcpsessionsrate(self) :
		r"""Rate (/s) counter for lsncurnat64tcpsessions.
		"""
		try :
			return self._lsncurnat64tcpsessionsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64udprxpktsrate(self) :
		r"""Rate (/s) counter for lsntotnat64udprxpkts.
		"""
		try :
			return self._lsnnat64udprxpktsrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64icmpdrppkts(self) :
		r"""Number of LSN NAT64 ICMP Dropped packets.
		"""
		try :
			return self._lsntotnat64icmpdrppkts
		except Exception as e:
			raise e

	@property
	def lsnnat64udprxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64udprxbytes.
		"""
		try :
			return self._lsnnat64udprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsnnat64icmprxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64icmprxbytes.
		"""
		try :
			return self._lsnnat64icmprxbytesrate
		except Exception as e:
			raise e

	@property
	def lsncurnat64sessionsrate(self) :
		r"""Rate (/s) counter for lsncurnat64sessions.
		"""
		try :
			return self._lsncurnat64sessionsrate
		except Exception as e:
			raise e

	@property
	def lsnnat64rxbytesrate(self) :
		r"""Rate (/s) counter for lsntotnat64rxbytes.
		"""
		try :
			return self._lsnnat64rxbytesrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64icmprxbytes(self) :
		r"""Number of LSN NAT64 ICMP Received bytes.
		"""
		try :
			return self._lsntotnat64icmprxbytes
		except Exception as e:
			raise e

	@property
	def lsnnat64cursubscribers(self) :
		r"""Current number of LSN NAT64 subscribers.
		"""
		try :
			return self._lsnnat64cursubscribers
		except Exception as e:
			raise e

	@property
	def lsnnat64cursubscribersrate(self) :
		r"""Rate (/s) counter for lsnnat64cursubscribers.
		"""
		try :
			return self._lsnnat64cursubscribersrate
		except Exception as e:
			raise e

	@property
	def lsntotnat64udptxpkts(self) :
		r"""Number of LSN NAT64 UDP Transmitted packets.
		"""
		try :
			return self._lsntotnat64udptxpkts
		except Exception as e:
			raise e

	@property
	def lsntotnat64rxbytes(self) :
		r"""Total number of LSN NAT64 rx bytes.
		"""
		try :
			return self._lsntotnat64rxbytes
		except Exception as e:
			raise e

	@property
	def lsntotnat64tcprxbytes(self) :
		r"""Number of LSN NAT64 TCP Received bytes.
		"""
		try :
			return self._lsntotnat64tcprxbytes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnnat64_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnnat64
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all lsnnat64_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = lsnnat64_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lsnnat64_response(base_response) :
	def __init__(self, length=1) :
		self.lsnnat64 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnnat64 = [lsnnat64_stats() for _ in range(length)]

