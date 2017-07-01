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

class cmp_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._delbwsaving = 0
		self._delcmpratio = 0
		self._decomptcpratio = 0
		self._decomptcpbandwidthsaving = 0
		self._comptcpratio = 0
		self._comptcpbandwidthsaving = 0
		self._comptotaldatacompressionratio = 0
		self._comphttpbandwidthsaving = 0
		self._compratio = 0
		self._comptotalrequests = 0
		self._comprequestsrate = 0
		self._comptotalrxbytes = 0
		self._comprxbytesrate = 0
		self._comptotaltxbytes = 0
		self._comptxbytesrate = 0
		self._comptotalrxpackets = 0
		self._comprxpacketsrate = 0
		self._comptotaltxpackets = 0
		self._comptxpacketsrate = 0
		self._comptcptotalrxbytes = 0
		self._comptcprxbytesrate = 0
		self._comptcptotalrxpackets = 0
		self._comptcprxpacketsrate = 0
		self._comptcptotaltxbytes = 0
		self._comptcptxbytesrate = 0
		self._comptcptotaltxpackets = 0
		self._comptcptxpacketsrate = 0
		self._comptcptotalquantum = 0
		self._comptcpquantumrate = 0
		self._comptcptotalpush = 0
		self._comptcppushrate = 0
		self._comptcptotaleoi = 0
		self._comptcpeoirate = 0
		self._comptcptotaltimer = 0
		self._comptcptimerrate = 0
		self._decomptcprxbytes = 0
		self._decomptcprxbytesrate = 0
		self._decomptcprxpackets = 0
		self._decomptcprxpacketsrate = 0
		self._decomptcptxbytes = 0
		self._decomptcptxbytesrate = 0
		self._decomptcptxpackets = 0
		self._decomptcptxpacketsrate = 0
		self._decomptcperrdata = 0
		self._decomptcperrdatarate = 0
		self._decomptcperrlessdata = 0
		self._decomptcperrlessdatarate = 0
		self._decomptcperrmoredata = 0
		self._decomptcperrmoredatarate = 0
		self._decomptcperrmemory = 0
		self._decomptcperrmemoryrate = 0
		self._decomptcperrunknown = 0
		self._decomptcperrunknownrate = 0
		self._delcomptotalrequests = 0
		self._delcomprequestsrate = 0
		self._delcompdone = 0
		self._delcompdonerate = 0
		self._delcomptcprxbytes = 0
		self._delcomptcprxbytesrate = 0
		self._delcomptcptxbytes = 0
		self._delcomptcptxbytesrate = 0
		self._delcompfirstaccess = 0
		self._delcompfirstaccessrate = 0
		self._delcomptcprxpackets = 0
		self._delcomptcprxpacketsrate = 0
		self._delcomptcptxpackets = 0
		self._delcomptcptxpacketsrate = 0
		self._delcompbaseserved = 0
		self._delcompbaseservedrate = 0
		self._delcompbasetcptxbytes = 0
		self._delcompbasetcptxbytesrate = 0
		self._delcomperrbypassed = 0
		self._delcomperrbypassedrate = 0
		self._delcomperrbfilewhdrfailed = 0
		self._delcomperrbfilewhdrfailedrate = 0
		self._delcomperrnostoremiss = 0
		self._delcomperrnostoremissrate = 0
		self._delcomperrreqinfotoobig = 0
		self._delcomperrreqinfotoobigrate = 0
		self._delcomperrreqinfoallocfail = 0
		self._delcomperrreqinfoallocfailrate = 0
		self._delcomperrsessallocfail = 0
		self._delcomperrsessallocfailrate = 0

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
	def comphttpbandwidthsaving(self) :
		r"""Bandwidth saving from TCP compression expressed as percentage.
		"""
		try :
			return self._comphttpbandwidthsaving
		except Exception as e:
			raise e

	@property
	def decomptcptxpacketsrate(self) :
		r"""Rate (/s) counter for decomptcptxpackets.
		"""
		try :
			return self._decomptcptxpacketsrate
		except Exception as e:
			raise e

	@property
	def delcompbasetcptxbytesrate(self) :
		r"""Rate (/s) counter for delcompbasetcptxbytes.
		"""
		try :
			return self._delcompbasetcptxbytesrate
		except Exception as e:
			raise e

	@property
	def comptotaltxbytes(self) :
		r"""Number of bytes the NetScaler sends to the client after compressing the response from the server.
		"""
		try :
			return self._comptotaltxbytes
		except Exception as e:
			raise e

	@property
	def comptcpeoirate(self) :
		r"""Rate (/s) counter for comptcptotaleoi.
		"""
		try :
			return self._comptcpeoirate
		except Exception as e:
			raise e

	@property
	def delcomperrbypassedrate(self) :
		r"""Rate (/s) counter for delcomperrbypassed.
		"""
		try :
			return self._delcomperrbypassedrate
		except Exception as e:
			raise e

	@property
	def delcmpratio(self) :
		r"""Ratio of compressible data received to compressed data transmitted.If this ratio is one (uncmp:1.0) that means compression is disabled or we are not able to compress even a single compressible packet.
		"""
		try :
			return self._delcmpratio
		except Exception as e:
			raise e

	@property
	def delcomprequestsrate(self) :
		r"""Rate (/s) counter for delcomptotalrequests.
		"""
		try :
			return self._delcomprequestsrate
		except Exception as e:
			raise e

	@property
	def delcomptcprxpacketsrate(self) :
		r"""Rate (/s) counter for delcomptcprxpackets.
		"""
		try :
			return self._delcomptcprxpacketsrate
		except Exception as e:
			raise e

	@property
	def decomptcperrmemory(self) :
		r"""Number of times memory failures occurred while decompressing.
		"""
		try :
			return self._decomptcperrmemory
		except Exception as e:
			raise e

	@property
	def comptotaldatacompressionratio(self) :
		r"""Ratio of total HTTP data received to total HTTP data transmitted.
		"""
		try :
			return self._comptotaldatacompressionratio
		except Exception as e:
			raise e

	@property
	def comprxbytesrate(self) :
		r"""Rate (/s) counter for comptotalrxbytes.
		"""
		try :
			return self._comprxbytesrate
		except Exception as e:
			raise e

	@property
	def delcomperrsessallocfailrate(self) :
		r"""Rate (/s) counter for delcomperrsessallocfail.
		"""
		try :
			return self._delcomperrsessallocfailrate
		except Exception as e:
			raise e

	@property
	def delcomptcptxpacketsrate(self) :
		r"""Rate (/s) counter for delcomptcptxpackets.
		"""
		try :
			return self._delcomptcptxpacketsrate
		except Exception as e:
			raise e

	@property
	def decomptcperrmemoryrate(self) :
		r"""Rate (/s) counter for decomptcperrmemory.
		"""
		try :
			return self._decomptcperrmemoryrate
		except Exception as e:
			raise e

	@property
	def decomptcperrmoredata(self) :
		r"""Number of times NetScaler received more data than declared by protocol.
		"""
		try :
			return self._decomptcperrmoredata
		except Exception as e:
			raise e

	@property
	def delcompfirstaccessrate(self) :
		r"""Rate (/s) counter for delcompfirstaccess.
		"""
		try :
			return self._delcompfirstaccessrate
		except Exception as e:
			raise e

	@property
	def comprxpacketsrate(self) :
		r"""Rate (/s) counter for comptotalrxpackets.
		"""
		try :
			return self._comprxpacketsrate
		except Exception as e:
			raise e

	@property
	def decomptcprxpacketsrate(self) :
		r"""Rate (/s) counter for decomptcprxpackets.
		"""
		try :
			return self._decomptcprxpacketsrate
		except Exception as e:
			raise e

	@property
	def comptcpquantumrate(self) :
		r"""Rate (/s) counter for comptcptotalquantum.
		"""
		try :
			return self._comptcpquantumrate
		except Exception as e:
			raise e

	@property
	def comptxbytesrate(self) :
		r"""Rate (/s) counter for comptotaltxbytes.
		"""
		try :
			return self._comptxbytesrate
		except Exception as e:
			raise e

	@property
	def delcompbaseservedrate(self) :
		r"""Rate (/s) counter for delcompbaseserved.
		"""
		try :
			return self._delcompbaseservedrate
		except Exception as e:
			raise e

	@property
	def comptcptxbytesrate(self) :
		r"""Rate (/s) counter for comptcptotaltxbytes.
		"""
		try :
			return self._comptcptxbytesrate
		except Exception as e:
			raise e

	@property
	def delcomptcprxpackets(self) :
		r"""Number of delta-compressible packets received.
		"""
		try :
			return self._delcomptcprxpackets
		except Exception as e:
			raise e

	@property
	def delcomperrbfilewhdrfailed(self) :
		r"""Number of times basefile could not be updated in NetScaler cache.
		"""
		try :
			return self._delcomperrbfilewhdrfailed
		except Exception as e:
			raise e

	@property
	def decomptcperrmoredatarate(self) :
		r"""Rate (/s) counter for decomptcperrmoredata.
		"""
		try :
			return self._decomptcperrmoredatarate
		except Exception as e:
			raise e

	@property
	def delcompbaseserved(self) :
		r"""Total number of basefile requests served by NetScaler.
		"""
		try :
			return self._delcompbaseserved
		except Exception as e:
			raise e

	@property
	def compratio(self) :
		r"""Ratio of the compressible data received from the server to the compressed data sent to the client.
		"""
		try :
			return self._compratio
		except Exception as e:
			raise e

	@property
	def decomptcperrlessdata(self) :
		r"""Number of times NetScaler received less data than declared by protocol.
		"""
		try :
			return self._decomptcperrlessdata
		except Exception as e:
			raise e

	@property
	def comptcprxbytesrate(self) :
		r"""Rate (/s) counter for comptcptotalrxbytes.
		"""
		try :
			return self._comptcprxbytesrate
		except Exception as e:
			raise e

	@property
	def comptcprxpacketsrate(self) :
		r"""Rate (/s) counter for comptcptotalrxpackets.
		"""
		try :
			return self._comptcprxpacketsrate
		except Exception as e:
			raise e

	@property
	def delcomptcptxbytesrate(self) :
		r"""Rate (/s) counter for delcomptcptxbytes.
		"""
		try :
			return self._delcomptcptxbytesrate
		except Exception as e:
			raise e

	@property
	def decomptcperrdatarate(self) :
		r"""Rate (/s) counter for decomptcperrdata.
		"""
		try :
			return self._decomptcperrdatarate
		except Exception as e:
			raise e

	@property
	def delcompdonerate(self) :
		r"""Rate (/s) counter for delcompdone.
		"""
		try :
			return self._delcompdonerate
		except Exception as e:
			raise e

	@property
	def decomptcpratio(self) :
		r"""Ratio of decompressed data transmitted to compressed data received.
		"""
		try :
			return self._decomptcpratio
		except Exception as e:
			raise e

	@property
	def decomptcperrlessdatarate(self) :
		r"""Rate (/s) counter for decomptcperrlessdata.
		"""
		try :
			return self._decomptcperrlessdatarate
		except Exception as e:
			raise e

	@property
	def comptcptotaltxbytes(self) :
		r"""Number of bytes that the NetScaler sends to the client after compressing the response from the server.
		"""
		try :
			return self._comptcptotaltxbytes
		except Exception as e:
			raise e

	@property
	def delcomptotalrequests(self) :
		r"""Total number of delta compression requests received by NetScaler.
		"""
		try :
			return self._delcomptotalrequests
		except Exception as e:
			raise e

	@property
	def delcomperrreqinfoallocfailrate(self) :
		r"""Rate (/s) counter for delcomperrreqinfoallocfail.
		"""
		try :
			return self._delcomperrreqinfoallocfailrate
		except Exception as e:
			raise e

	@property
	def delcomperrnostoremiss(self) :
		r"""Number of times basefile was not found in NetScaler cache.
		"""
		try :
			return self._delcomperrnostoremiss
		except Exception as e:
			raise e

	@property
	def delcompbasetcptxbytes(self) :
		r"""Number of basefile bytes transmitted by NetScaler.
		"""
		try :
			return self._delcompbasetcptxbytes
		except Exception as e:
			raise e

	@property
	def comptcptotalpush(self) :
		r"""Number of times the NetScaler compresses data on receiving a TCP PUSH flag from the server. The PUSH flag ensures that data is compressed immediately without waiting for the buffered data size to reach the quantum size.
		"""
		try :
			return self._comptcptotalpush
		except Exception as e:
			raise e

	@property
	def delcompfirstaccess(self) :
		r"""Total number of delta compression first accesses.
		"""
		try :
			return self._delcompfirstaccess
		except Exception as e:
			raise e

	@property
	def delcompdone(self) :
		r"""Total number of delta compressions done by NetScaler.
		"""
		try :
			return self._delcompdone
		except Exception as e:
			raise e

	@property
	def comptcptotalrxpackets(self) :
		r"""Total number of compressible packets received by NetScaler.
		"""
		try :
			return self._comptcptotalrxpackets
		except Exception as e:
			raise e

	@property
	def delcomperrbypassed(self) :
		r"""Number of times delta-compression bypassed by NetScaler.
		"""
		try :
			return self._delcomperrbypassed
		except Exception as e:
			raise e

	@property
	def delbwsaving(self) :
		r"""Bandwidth saving from delta compression expressed as percentage.
		"""
		try :
			return self._delbwsaving
		except Exception as e:
			raise e

	@property
	def comprequestsrate(self) :
		r"""Rate (/s) counter for comptotalrequests.
		"""
		try :
			return self._comprequestsrate
		except Exception as e:
			raise e

	@property
	def delcomptcptxbytes(self) :
		r"""Total number of delta-compressed bytes transmitted by NetScaler.
		"""
		try :
			return self._delcomptcptxbytes
		except Exception as e:
			raise e

	@property
	def delcomperrreqinfoallocfail(self) :
		r"""Number of times requested basefile could not be allocated.
		"""
		try :
			return self._delcomperrreqinfoallocfail
		except Exception as e:
			raise e

	@property
	def delcomperrreqinfotoobig(self) :
		r"""Number of times basefile request URL was too large.
		"""
		try :
			return self._delcomperrreqinfotoobig
		except Exception as e:
			raise e

	@property
	def decomptcprxbytes(self) :
		r"""Total number of compressed bytes received by NetScaler.
		"""
		try :
			return self._decomptcprxbytes
		except Exception as e:
			raise e

	@property
	def comptcptxpacketsrate(self) :
		r"""Rate (/s) counter for comptcptotaltxpackets.
		"""
		try :
			return self._comptcptxpacketsrate
		except Exception as e:
			raise e

	@property
	def comptcptotaleoi(self) :
		r"""Number of times the NetScaler compresses data on receiving End Of Input (FIN packet).  When the NetScaler receives End Of Input (FIN packet), it compresses the buffered data immediately without waiting for the buffered data size to reach the quantum size.
		"""
		try :
			return self._comptcptotaleoi
		except Exception as e:
			raise e

	@property
	def comptcppushrate(self) :
		r"""Rate (/s) counter for comptcptotalpush.
		"""
		try :
			return self._comptcppushrate
		except Exception as e:
			raise e

	@property
	def decomptcperrunknownrate(self) :
		r"""Rate (/s) counter for decomptcperrunknown.
		"""
		try :
			return self._decomptcperrunknownrate
		except Exception as e:
			raise e

	@property
	def comptcpbandwidthsaving(self) :
		r"""Bandwidth saving from TCP compression expressed as percentage.
		"""
		try :
			return self._comptcpbandwidthsaving
		except Exception as e:
			raise e

	@property
	def comptotalrxbytes(self) :
		r"""Number of bytes that can be compressed, which the NetScaler receives from the server. This gives the content length of the response that the NetScaler receives from server.
		"""
		try :
			return self._comptotalrxbytes
		except Exception as e:
			raise e

	@property
	def decomptcptxbytes(self) :
		r"""Total number of decompressed bytes transmitted by NetScaler.
		"""
		try :
			return self._decomptcptxbytes
		except Exception as e:
			raise e

	@property
	def decomptcprxpackets(self) :
		r"""Total number of compressed packets received by NetScaler.
		"""
		try :
			return self._decomptcprxpackets
		except Exception as e:
			raise e

	@property
	def comptcptotaltimer(self) :
		r"""Number of times the NetScaler compresses data on expiration of data accumulation timer. The timer expires if the server response is very slow and consequently, the NetScaler does not receive response for a certain amount of time.  Under such a condition, the NetScaler compresses the buffered data immediately without waiting for the buffered data size to reach the quantum size.
		"""
		try :
			return self._comptcptotaltimer
		except Exception as e:
			raise e

	@property
	def delcomperrnostoremissrate(self) :
		r"""Rate (/s) counter for delcomperrnostoremiss.
		"""
		try :
			return self._delcomperrnostoremissrate
		except Exception as e:
			raise e

	@property
	def decomptcpbandwidthsaving(self) :
		r"""Bandwidth saving from TCP compression expressed as percentage.
		"""
		try :
			return self._decomptcpbandwidthsaving
		except Exception as e:
			raise e

	@property
	def delcomperrsessallocfail(self) :
		r"""Number of times delta compression session could not be allocated.
		"""
		try :
			return self._delcomperrsessallocfail
		except Exception as e:
			raise e

	@property
	def decomptcptxbytesrate(self) :
		r"""Rate (/s) counter for decomptcptxbytes.
		"""
		try :
			return self._decomptcptxbytesrate
		except Exception as e:
			raise e

	@property
	def comptxpacketsrate(self) :
		r"""Rate (/s) counter for comptotaltxpackets.
		"""
		try :
			return self._comptxpacketsrate
		except Exception as e:
			raise e

	@property
	def comptotaltxpackets(self) :
		r"""Number of HTTP packets that the NetScaler sends to the client after compressing the response from the server.
		"""
		try :
			return self._comptotaltxpackets
		except Exception as e:
			raise e

	@property
	def delcomperrreqinfotoobigrate(self) :
		r"""Rate (/s) counter for delcomperrreqinfotoobig.
		"""
		try :
			return self._delcomperrreqinfotoobigrate
		except Exception as e:
			raise e

	@property
	def decomptcprxbytesrate(self) :
		r"""Rate (/s) counter for decomptcprxbytes.
		"""
		try :
			return self._decomptcprxbytesrate
		except Exception as e:
			raise e

	@property
	def comptotalrequests(self) :
		r"""Number of HTTP compression requests the NetScaler receives for which the response is successfully compressed. For example, after you enable compression and configure services, if you send HTTP requests to the NetScaler using a HTTP client that supports compression, and NetScaler compresses the corresponding response, this counter is incremented.
		"""
		try :
			return self._comptotalrequests
		except Exception as e:
			raise e

	@property
	def decomptcperrunknown(self) :
		r"""Number of times unknown errors occurred while decompressing.
		"""
		try :
			return self._decomptcperrunknown
		except Exception as e:
			raise e

	@property
	def comptotalrxpackets(self) :
		r"""Number of HTTP packets that can be compressed, which the NetScaler receives from the server.
		"""
		try :
			return self._comptotalrxpackets
		except Exception as e:
			raise e

	@property
	def delcomptcprxbytes(self) :
		r"""Total number of delta-compressible bytes received by NetScaler.
		"""
		try :
			return self._delcomptcprxbytes
		except Exception as e:
			raise e

	@property
	def comptcptimerrate(self) :
		r"""Rate (/s) counter for comptcptotaltimer.
		"""
		try :
			return self._comptcptimerrate
		except Exception as e:
			raise e

	@property
	def comptcptotalquantum(self) :
		r"""Number of times the NetScaler compresses a quantum of data.  NetScaler buffers the data received from the server till it reaches the quantum size and then compresses the buffered data and transmits to the client.
		"""
		try :
			return self._comptcptotalquantum
		except Exception as e:
			raise e

	@property
	def comptcptotaltxpackets(self) :
		r"""Number of TCP packets that the NetScaler sends to the client after compressing the response from the server.
		"""
		try :
			return self._comptcptotaltxpackets
		except Exception as e:
			raise e

	@property
	def delcomptcptxpackets(self) :
		r"""Total number of delta-compressed packets transmitted by NetScaler.
		"""
		try :
			return self._delcomptcptxpackets
		except Exception as e:
			raise e

	@property
	def comptcptotalrxbytes(self) :
		r"""Number of bytes that can be compressed, which the NetScaler receives from the server. This gives the content length of the response that the NetScaler receives from server.
		"""
		try :
			return self._comptcptotalrxbytes
		except Exception as e:
			raise e

	@property
	def delcomptcprxbytesrate(self) :
		r"""Rate (/s) counter for delcomptcprxbytes.
		"""
		try :
			return self._delcomptcprxbytesrate
		except Exception as e:
			raise e

	@property
	def decomptcptxpackets(self) :
		r"""Total number of decompressed packets transmitted by NetScaler.
		"""
		try :
			return self._decomptcptxpackets
		except Exception as e:
			raise e

	@property
	def delcomperrbfilewhdrfailedrate(self) :
		r"""Rate (/s) counter for delcomperrbfilewhdrfailed.
		"""
		try :
			return self._delcomperrbfilewhdrfailedrate
		except Exception as e:
			raise e

	@property
	def comptcpratio(self) :
		r"""Ratio of compressible data received to compressed data transmitted.If this ratio is one (uncmp:1.0) that means compression is disabled or we are not able to compress even a single compressible packet.
		"""
		try :
			return self._comptcpratio
		except Exception as e:
			raise e

	@property
	def decomptcperrdata(self) :
		r"""Number of data errors encountered while decompressing.
		"""
		try :
			return self._decomptcperrdata
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cmp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cmp
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
		r""" Use this API to fetch the statistics of all cmp_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = cmp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class cmp_response(base_response) :
	def __init__(self, length=1) :
		self.cmp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cmp = [cmp_stats() for _ in range(length)]

