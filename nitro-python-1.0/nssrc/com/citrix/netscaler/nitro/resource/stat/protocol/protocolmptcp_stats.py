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

class protocolmptcp_stats(base_resource) :
	r""" Statistics for mptcp protocol resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._mptcptotmpcapsession = 0
		self._mptcpmpcapsessionrate = 0
		self._mptcptotsfconn = 0
		self._mptcpsfconnrate = 0
		self._mptcpcurmpcapablesessions = 0
		self._mptcpcursfconnections = 0
		self._mptcpcurpendingjoin = 0
		self._mptcpcursesswithoutsfs = 0
		self._mptcptotmpcapsyn = 0
		self._mptcpmpcapsynrate = 0
		self._mptcptotmpcapsteered = 0
		self._mptcpmpcapsteeredrate = 0
		self._mptcptotconnest = 0
		self._mptcpconnestrate = 0
		self._mptcptotmpcapsynacksent = 0
		self._mptcpmpcapsynacksentrate = 0
		self._mptcptotmpcapfackrecvd = 0
		self._mptcpmpcapfackrecvdrate = 0
		self._mptcptotmpjoinsyn = 0
		self._mptcpmpjoinsynrate = 0
		self._mptcptotmpjoinsteered = 0
		self._mptcpmpjoinsteeredrate = 0
		self._mptcptotmpjoinsynacksent = 0
		self._mptcpmpjoinsynacksentrate = 0
		self._mptcptotmpjoinfackrecvd = 0
		self._mptcpmpjoinfackrecvdrate = 0
		self._mptcptotmpjoin4thacksent = 0
		self._mptcpmpjoin4thacksentrate = 0
		self._mptcptotestsfreplaced = 0
		self._mptcpestsfreplacedrate = 0
		self._mptcptotpendsfreplaced = 0
		self._mptcppendsfreplacedrate = 0
		self._mptcptotfreshackfrwd = 0
		self._mptcpfreshackfrwdrate = 0
		self._mptcpplainackfallback = 0
		self._mptcpplainackfallbackrate = 0
		self._mptcpinfinitemaprecvd = 0
		self._mptcpinfinitemaprecvdrate = 0
		self._mptcptotaddrremoved = 0
		self._mptcpaddrremovedrate = 0
		self._mptcptotdss = 0
		self._mptcpdssrate = 0
		self._mptcptotrxdss = 0
		self._mptcprxdssrate = 0
		self._mptcptottxdss = 0
		self._mptcptxdssrate = 0
		self._mptcptotdssa = 0
		self._mptcpdssarate = 0
		self._mptcptotdssfreshack = 0
		self._mptcpdssfreshackrate = 0
		self._mptcptotdssm = 0
		self._mptcpdssmrate = 0
		self._mptcptotinfinitemapfrwd = 0
		self._mptcpinfinitemapfrwdrate = 0
		self._mptcptotdatalessthandatalen = 0
		self._mptcpdatalessthandatalenrate = 0
		self._mptcppriobackuprx = 0
		self._mptcppriobackuprxrate = 0
		self._mptcpprioclearbackuprx = 0
		self._mptcpprioclearbackuprxrate = 0
		self._mptcptottxdatafin = 0
		self._mptcptxdatafinrate = 0
		self._mptcptotrxdatafin = 0
		self._mptcprxdatafinrate = 0
		self._mptcptottxsffin = 0
		self._mptcptxsffinrate = 0
		self._mptcperrinvalcookie = 0
		self._mptcperrinvalcookierate = 0
		self._mptcperrextnflagset = 0
		self._mptcperrextnflagsetrate = 0
		self._mptcperrresflagset = 0
		self._mptcperrresflagsetrate = 0
		self._mptcperrunknowntoken = 0
		self._mptcperrunknowntokenrate = 0
		self._mptcperraddridexist = 0
		self._mptcperraddridexistrate = 0
		self._mptcperraddrid0 = 0
		self._mptcperraddrid0rate = 0
		self._mptcperrmaxsf = 0
		self._mptcperrmaxsfrate = 0
		self._mptcperrjointhreshold = 0
		self._mptcperrjointhresholdrate = 0
		self._mptcperrjoinafterfallback = 0
		self._mptcperrjoinafterfallbackrate = 0
		self._mptcperrinvalmac = 0
		self._mptcperrinvalmacrate = 0
		self._mptcperrinvalopts = 0
		self._mptcperrinvaloptsrate = 0
		self._mptcperroptiondiscarded = 0
		self._mptcperroptiondiscardedrate = 0
		self._mptcperroptsnosession = 0
		self._mptcperroptsnosessionrate = 0
		self._mptcperrinvalremaddr = 0
		self._mptcperrinvalremaddrrate = 0
		self._mptcperroptssendrst = 0
		self._mptcperroptssendrstrate = 0
		self._mptcperrremaddrself = 0
		self._mptcperrremaddrselfrate = 0
		self._mptcperrrssffail = 0
		self._mptcperrrssffailrate = 0
		self._mptcperrnopayloadlenpkt = 0
		self._mptcperrnopayloadlenpktrate = 0
		self._mptcperrunsupportedmssnegotiated = 0
		self._mptcperrunsupportedmssnegotiatedrate = 0
		self._mptcperrbadcksum = 0
		self._mptcperrbadcksumrate = 0
		self._mptcperrcryptonotsupported = 0
		self._mptcperrcryptonotsupportedrate = 0
		self._mptcperrversionnotsupported = 0
		self._mptcperrversionnotsupportedrate = 0
		self._mptcpplainackrst = 0
		self._mptcpplainackrstrate = 0
		self._mptcperrdatafinpassive = 0
		self._mptcperrdatafinpassiverate = 0
		self._mptcperrfastclose = 0
		self._mptcperrfastcloserate = 0
		self._mptcperrfastclosepassive = 0
		self._mptcperrfastclosepassiverate = 0
		self._mptcperrfastclosekey = 0
		self._mptcperrfastclosekeyrate = 0
		self._mptcpmpfailsent = 0
		self._mptcpmpfailsentrate = 0
		self._mptcpmpfailrecvd = 0
		self._mptcpmpfailrecvdrate = 0
		self._mptcperrnomappktrcvd = 0
		self._mptcperrnomappktrcvdrate = 0
		self._mptcptotmoredatarcvd = 0
		self._mptcpmoredatarcvdrate = 0
		self._mptcperrbadmapconndrop = 0
		self._mptcperrbadmapconndroprate = 0
		self._mptcperrdupmaprecvd = 0
		self._mptcperrdupmaprecvdrate = 0
		self._mptcperrinvalidsfn = 0
		self._mptcperrinvalidsfnrate = 0
		self._mptcperrmapexists = 0
		self._mptcperrmapexistsrate = 0
		self._mptcperrretxpktrcvd = 0
		self._mptcperrretxpktrcvdrate = 0
		self._mptcperrsfsessionallocfail = 0
		self._mptcperrsfsessionallocfailrate = 0
		self._mptcperrmpcapsessionallocfail = 0
		self._mptcperrmpcapsessionallocfailrate = 0
		self._mptcptotmpcapsfpcballoc = 0
		self._mptcpmpcapsfpcballocrate = 0
		self._mptcptotmpcballocfailed = 0
		self._mptcpmpcballocfailedrate = 0
		self._mptcperrnsballocfailed = 0
		self._mptcperrnsballocfailedrate = 0
		self._mptcperrnosffreensb = 0
		self._mptcperrnosffreensbrate = 0

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
	def mptcperrinvalopts(self) :
		r"""MPTCP invalid mptcp option is received and is dropped.
		"""
		try :
			return self._mptcperrinvalopts
		except Exception as e:
			raise e

	@property
	def mptcperraddrid0rate(self) :
		r"""Rate (/s) counter for mptcperraddrid0.
		"""
		try :
			return self._mptcperraddrid0rate
		except Exception as e:
			raise e

	@property
	def mptcpplainackfallbackrate(self) :
		r"""Rate (/s) counter for mptcpplainackfallback.
		"""
		try :
			return self._mptcpplainackfallbackrate
		except Exception as e:
			raise e

	@property
	def mptcperrbadmapconndroprate(self) :
		r"""Rate (/s) counter for mptcperrbadmapconndrop.
		"""
		try :
			return self._mptcperrbadmapconndroprate
		except Exception as e:
			raise e

	@property
	def mptcperrrssffailrate(self) :
		r"""Rate (/s) counter for mptcperrrssffail.
		"""
		try :
			return self._mptcperrrssffailrate
		except Exception as e:
			raise e

	@property
	def mptcperrremaddrselfrate(self) :
		r"""Rate (/s) counter for mptcperrremaddrself.
		"""
		try :
			return self._mptcperrremaddrselfrate
		except Exception as e:
			raise e

	@property
	def mptcpsfconnrate(self) :
		r"""Rate (/s) counter for mptcptotsfconn.
		"""
		try :
			return self._mptcpsfconnrate
		except Exception as e:
			raise e

	@property
	def mptcperroptiondiscardedrate(self) :
		r"""Rate (/s) counter for mptcperroptiondiscarded.
		"""
		try :
			return self._mptcperroptiondiscardedrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpjoinsynacksent(self) :
		r"""Total MP_JOIN SYN/ACKs sent.
		"""
		try :
			return self._mptcptotmpjoinsynacksent
		except Exception as e:
			raise e

	@property
	def mptcperrfastclose(self) :
		r"""MPTCP FAST CLOSE sent.
		"""
		try :
			return self._mptcperrfastclose
		except Exception as e:
			raise e

	@property
	def mptcperrremaddrself(self) :
		r"""MPTCP remove address request for self address.
		"""
		try :
			return self._mptcperrremaddrself
		except Exception as e:
			raise e

	@property
	def mptcperraddridexist(self) :
		r"""MPTCP MP_JOIN request on existing address id.
		"""
		try :
			return self._mptcperraddridexist
		except Exception as e:
			raise e

	@property
	def mptcpfreshackfrwdrate(self) :
		r"""Rate (/s) counter for mptcptotfreshackfrwd.
		"""
		try :
			return self._mptcpfreshackfrwdrate
		except Exception as e:
			raise e

	@property
	def mptcperrunsupportedmssnegotiatedrate(self) :
		r"""Rate (/s) counter for mptcperrunsupportedmssnegotiated.
		"""
		try :
			return self._mptcperrunsupportedmssnegotiatedrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpjoin4thacksent(self) :
		r"""Total number of Subflow final ACK from peer in 3 way handshake validated with 4th ACK.
		"""
		try :
			return self._mptcptotmpjoin4thacksent
		except Exception as e:
			raise e

	@property
	def mptcperrinvalcookie(self) :
		r"""MPTCP invalid cookie received on MP_CAPABLE final ACK.
		"""
		try :
			return self._mptcperrinvalcookie
		except Exception as e:
			raise e

	@property
	def mptcpmpjoinsteeredrate(self) :
		r"""Rate (/s) counter for mptcptotmpjoinsteered.
		"""
		try :
			return self._mptcpmpjoinsteeredrate
		except Exception as e:
			raise e

	@property
	def mptcptotaddrremoved(self) :
		r"""Total number of addresses removed from MPTCP connection with REMOVE_ADDR option.
		"""
		try :
			return self._mptcptotaddrremoved
		except Exception as e:
			raise e

	@property
	def mptcpplainackrstrate(self) :
		r"""Rate (/s) counter for mptcpplainackrst.
		"""
		try :
			return self._mptcpplainackrstrate
		except Exception as e:
			raise e

	@property
	def mptcperrinvalidsfnrate(self) :
		r"""Rate (/s) counter for mptcperrinvalidsfn.
		"""
		try :
			return self._mptcperrinvalidsfnrate
		except Exception as e:
			raise e

	@property
	def mptcpmpcapfackrecvdrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapfackrecvd.
		"""
		try :
			return self._mptcpmpcapfackrecvdrate
		except Exception as e:
			raise e

	@property
	def mptcperraddrid0(self) :
		r"""MPTCP MP_JOIN request on address id 0.
		"""
		try :
			return self._mptcperraddrid0
		except Exception as e:
			raise e

	@property
	def mptcptotrxdss(self) :
		r"""MPTCP Total Data Sequence Signal packets received.
		"""
		try :
			return self._mptcptotrxdss
		except Exception as e:
			raise e

	@property
	def mptcperrfastclosekey(self) :
		r"""MPTCP FAST_CLOSE received with invalid key and the packet is dropped.
		"""
		try :
			return self._mptcperrfastclosekey
		except Exception as e:
			raise e

	@property
	def mptcpmpfailsentrate(self) :
		r"""Rate (/s) counter for mptcpmpfailsent.
		"""
		try :
			return self._mptcpmpfailsentrate
		except Exception as e:
			raise e

	@property
	def mptcperrinvaloptsrate(self) :
		r"""Rate (/s) counter for mptcperrinvalopts.
		"""
		try :
			return self._mptcperrinvaloptsrate
		except Exception as e:
			raise e

	@property
	def mptcpcurmpcapablesessions(self) :
		r"""The number of current mptcp sessions.
		"""
		try :
			return self._mptcpcurmpcapablesessions
		except Exception as e:
			raise e

	@property
	def mptcprxdssrate(self) :
		r"""Rate (/s) counter for mptcptotrxdss.
		"""
		try :
			return self._mptcprxdssrate
		except Exception as e:
			raise e

	@property
	def mptcperrdatafinpassiverate(self) :
		r"""Rate (/s) counter for mptcperrdatafinpassive.
		"""
		try :
			return self._mptcperrdatafinpassiverate
		except Exception as e:
			raise e

	@property
	def mptcperrjoinafterfallbackrate(self) :
		r"""Rate (/s) counter for mptcperrjoinafterfallback.
		"""
		try :
			return self._mptcperrjoinafterfallbackrate
		except Exception as e:
			raise e

	@property
	def mptcpconnestrate(self) :
		r"""Rate (/s) counter for mptcptotconnest.
		"""
		try :
			return self._mptcpconnestrate
		except Exception as e:
			raise e

	@property
	def mptcperrcryptonotsupportedrate(self) :
		r"""Rate (/s) counter for mptcperrcryptonotsupported.
		"""
		try :
			return self._mptcperrcryptonotsupportedrate
		except Exception as e:
			raise e

	@property
	def mptcperrmaxsf(self) :
		r"""MPTCP new MP_JOIN request after maximum configured subflows are established.
		"""
		try :
			return self._mptcperrmaxsf
		except Exception as e:
			raise e

	@property
	def mptcperrinvalremaddr(self) :
		r"""MPTCP remove address request received on invalid/unknown address id.
		"""
		try :
			return self._mptcperrinvalremaddr
		except Exception as e:
			raise e

	@property
	def mptcperrinvalidsfn(self) :
		r"""MPTCP subflow map doesn't exactly match MPTCP session mapping.
		"""
		try :
			return self._mptcperrinvalidsfn
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapsyn(self) :
		r"""MPTCP total MP_CAPABLE received.
		"""
		try :
			return self._mptcptotmpcapsyn
		except Exception as e:
			raise e

	@property
	def mptcpcursesswithoutsfs(self) :
		r"""Current Multipath TCP sessions without any subflows.
		"""
		try :
			return self._mptcpcursesswithoutsfs
		except Exception as e:
			raise e

	@property
	def mptcpprioclearbackuprxrate(self) :
		r"""Rate (/s) counter for mptcpprioclearbackuprx.
		"""
		try :
			return self._mptcpprioclearbackuprxrate
		except Exception as e:
			raise e

	@property
	def mptcperrversionnotsupportedrate(self) :
		r"""Rate (/s) counter for mptcperrversionnotsupported.
		"""
		try :
			return self._mptcperrversionnotsupportedrate
		except Exception as e:
			raise e

	@property
	def mptcpprioclearbackuprx(self) :
		r"""Subflow earlier used only as a backup subflow, changes to regular subflow with MP_PRIO option.
		"""
		try :
			return self._mptcpprioclearbackuprx
		except Exception as e:
			raise e

	@property
	def mptcperrmapexistsrate(self) :
		r"""Rate (/s) counter for mptcperrmapexists.
		"""
		try :
			return self._mptcperrmapexistsrate
		except Exception as e:
			raise e

	@property
	def mptcpmoredatarcvdrate(self) :
		r"""Rate (/s) counter for mptcptotmoredatarcvd.
		"""
		try :
			return self._mptcpmoredatarcvdrate
		except Exception as e:
			raise e

	@property
	def mptcpmpfailsent(self) :
		r"""MPTCP Total MP_FAIL sent due to checksum failure.
		"""
		try :
			return self._mptcpmpfailsent
		except Exception as e:
			raise e

	@property
	def mptcpmpfailrecvdrate(self) :
		r"""Rate (/s) counter for mptcpmpfailrecvd.
		"""
		try :
			return self._mptcpmpfailrecvdrate
		except Exception as e:
			raise e

	@property
	def mptcptotdssa(self) :
		r"""Total Data Sequence Signal packets during data transfer with DATA_ACK.
		"""
		try :
			return self._mptcptotdssa
		except Exception as e:
			raise e

	@property
	def mptcptotdss(self) :
		r"""Total number of Data Sequence Signal packets.
		"""
		try :
			return self._mptcptotdss
		except Exception as e:
			raise e

	@property
	def mptcperrfastclosekeyrate(self) :
		r"""Rate (/s) counter for mptcperrfastclosekey.
		"""
		try :
			return self._mptcperrfastclosekeyrate
		except Exception as e:
			raise e

	@property
	def mptcperrrssffail(self) :
		r"""Add RSS filter to steer traffic to right node on established MPTCP session failed.
		"""
		try :
			return self._mptcperrrssffail
		except Exception as e:
			raise e

	@property
	def mptcperrnsballocfailed(self) :
		r"""Failed to allocate memory to output MPTCP packet.
		"""
		try :
			return self._mptcperrnsballocfailed
		except Exception as e:
			raise e

	@property
	def mptcpmpjoinfackrecvdrate(self) :
		r"""Rate (/s) counter for mptcptotmpjoinfackrecvd.
		"""
		try :
			return self._mptcpmpjoinfackrecvdrate
		except Exception as e:
			raise e

	@property
	def mptcpinfinitemaprecvdrate(self) :
		r"""Rate (/s) counter for mptcpinfinitemaprecvd.
		"""
		try :
			return self._mptcpinfinitemaprecvdrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapsfpcballoc(self) :
		r"""Allocating memory to TCP protocol control block(PCB) for subflow failed.
		"""
		try :
			return self._mptcptotmpcapsfpcballoc
		except Exception as e:
			raise e

	@property
	def mptcperrunsupportedmssnegotiated(self) :
		r"""MPTCP Unsupported MSS negotiated error.
		"""
		try :
			return self._mptcperrunsupportedmssnegotiated
		except Exception as e:
			raise e

	@property
	def mptcperrmapexists(self) :
		r"""MPTCP sequence map already exists.
		"""
		try :
			return self._mptcperrmapexists
		except Exception as e:
			raise e

	@property
	def mptcpmpjoin4thacksentrate(self) :
		r"""Rate (/s) counter for mptcptotmpjoin4thacksent.
		"""
		try :
			return self._mptcpmpjoin4thacksentrate
		except Exception as e:
			raise e

	@property
	def mptcperrnsballocfailedrate(self) :
		r"""Rate (/s) counter for mptcperrnsballocfailed.
		"""
		try :
			return self._mptcperrnsballocfailedrate
		except Exception as e:
			raise e

	@property
	def mptcppriobackuprx(self) :
		r"""MPTCP Subflow used as backup path.
		"""
		try :
			return self._mptcppriobackuprx
		except Exception as e:
			raise e

	@property
	def mptcpdssmrate(self) :
		r"""Rate (/s) counter for mptcptotdssm.
		"""
		try :
			return self._mptcpdssmrate
		except Exception as e:
			raise e

	@property
	def mptcperroptssendrst(self) :
		r"""MPTCP sent RST on receiving improper option field.
		"""
		try :
			return self._mptcperroptssendrst
		except Exception as e:
			raise e

	@property
	def mptcperrnomappktrcvdrate(self) :
		r"""Rate (/s) counter for mptcperrnomappktrcvd.
		"""
		try :
			return self._mptcperrnomappktrcvdrate
		except Exception as e:
			raise e

	@property
	def mptcpmpcballocfailedrate(self) :
		r"""Rate (/s) counter for mptcptotmpcballocfailed.
		"""
		try :
			return self._mptcpmpcballocfailedrate
		except Exception as e:
			raise e

	@property
	def mptcpinfinitemaprecvd(self) :
		r"""MPTCP Received and set infinite map and fallen back to regular TCP.
		"""
		try :
			return self._mptcpinfinitemaprecvd
		except Exception as e:
			raise e

	@property
	def mptcperrnopayloadlenpktrate(self) :
		r"""Rate (/s) counter for mptcperrnopayloadlenpkt.
		"""
		try :
			return self._mptcperrnopayloadlenpktrate
		except Exception as e:
			raise e

	@property
	def mptcpmpjoinsynacksentrate(self) :
		r"""Rate (/s) counter for mptcptotmpjoinsynacksent.
		"""
		try :
			return self._mptcpmpjoinsynacksentrate
		except Exception as e:
			raise e

	@property
	def mptcperrsfsessionallocfail(self) :
		r"""Attaching the subflow to MPTCP session failed due to failure in allocating memory to subflow map table.
		"""
		try :
			return self._mptcperrsfsessionallocfail
		except Exception as e:
			raise e

	@property
	def mptcperroptsnosessionrate(self) :
		r"""Rate (/s) counter for mptcperroptsnosession.
		"""
		try :
			return self._mptcperroptsnosessionrate
		except Exception as e:
			raise e

	@property
	def mptcpcurpendingjoin(self) :
		r"""The number of current mptcp subflow connections in pending state.
		"""
		try :
			return self._mptcpcurpendingjoin
		except Exception as e:
			raise e

	@property
	def mptcperrjoinafterfallback(self) :
		r"""MPTCP New MP_JOIN request received after fallback to regular tcp.
		"""
		try :
			return self._mptcperrjoinafterfallback
		except Exception as e:
			raise e

	@property
	def mptcperrinvalmacrate(self) :
		r"""Rate (/s) counter for mptcperrinvalmac.
		"""
		try :
			return self._mptcperrinvalmacrate
		except Exception as e:
			raise e

	@property
	def mptcperrretxpktrcvdrate(self) :
		r"""Rate (/s) counter for mptcperrretxpktrcvd.
		"""
		try :
			return self._mptcperrretxpktrcvdrate
		except Exception as e:
			raise e

	@property
	def mptcpdssarate(self) :
		r"""Rate (/s) counter for mptcptotdssa.
		"""
		try :
			return self._mptcpdssarate
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapfackrecvd(self) :
		r"""Total number of MP_CAPABLE Final ACKs received.
		"""
		try :
			return self._mptcptotmpcapfackrecvd
		except Exception as e:
			raise e

	@property
	def mptcpmpcapsessionrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapsession.
		"""
		try :
			return self._mptcpmpcapsessionrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapsynacksent(self) :
		r"""Total number of MP_CAPABLE SYN/ACKs sent.
		"""
		try :
			return self._mptcptotmpcapsynacksent
		except Exception as e:
			raise e

	@property
	def mptcperrextnflagset(self) :
		r"""Extension flag is set on MP_CAPABLE request.
		"""
		try :
			return self._mptcperrextnflagset
		except Exception as e:
			raise e

	@property
	def mptcptotsfconn(self) :
		r"""MPTCP total Subflow connections created.
		"""
		try :
			return self._mptcptotsfconn
		except Exception as e:
			raise e

	@property
	def mptcptotconnest(self) :
		r"""Total MP_CAPABLE sessions created.
		"""
		try :
			return self._mptcptotconnest
		except Exception as e:
			raise e

	@property
	def mptcptotmoredatarcvd(self) :
		r"""MPTCP More data received than the available Data Sequence Mapping.
		"""
		try :
			return self._mptcptotmoredatarcvd
		except Exception as e:
			raise e

	@property
	def mptcptotmpjoinsteered(self) :
		r"""Total MP_JOIN subflows steered.
		"""
		try :
			return self._mptcptotmpjoinsteered
		except Exception as e:
			raise e

	@property
	def mptcppriobackuprxrate(self) :
		r"""Rate (/s) counter for mptcppriobackuprx.
		"""
		try :
			return self._mptcppriobackuprxrate
		except Exception as e:
			raise e

	@property
	def mptcprxdatafinrate(self) :
		r"""Rate (/s) counter for mptcptotrxdatafin.
		"""
		try :
			return self._mptcprxdatafinrate
		except Exception as e:
			raise e

	@property
	def mptcperrunknowntokenrate(self) :
		r"""Rate (/s) counter for mptcperrunknowntoken.
		"""
		try :
			return self._mptcperrunknowntokenrate
		except Exception as e:
			raise e

	@property
	def mptcperrfastcloserate(self) :
		r"""Rate (/s) counter for mptcperrfastclose.
		"""
		try :
			return self._mptcperrfastcloserate
		except Exception as e:
			raise e

	@property
	def mptcptotrxdatafin(self) :
		r"""Total MPTCP connection close(DATA_FIN) requests received.
		"""
		try :
			return self._mptcptotrxdatafin
		except Exception as e:
			raise e

	@property
	def mptcpplainackrst(self) :
		r"""MPTCP Sent RST on receiving plain ACK for DSS.
		"""
		try :
			return self._mptcpplainackrst
		except Exception as e:
			raise e

	@property
	def mptcpaddrremovedrate(self) :
		r"""Rate (/s) counter for mptcptotaddrremoved.
		"""
		try :
			return self._mptcpaddrremovedrate
		except Exception as e:
			raise e

	@property
	def mptcperrinvalcookierate(self) :
		r"""Rate (/s) counter for mptcperrinvalcookie.
		"""
		try :
			return self._mptcperrinvalcookierate
		except Exception as e:
			raise e

	@property
	def mptcppendsfreplacedrate(self) :
		r"""Rate (/s) counter for mptcptotpendsfreplaced.
		"""
		try :
			return self._mptcppendsfreplacedrate
		except Exception as e:
			raise e

	@property
	def mptcperrfastclosepassiverate(self) :
		r"""Rate (/s) counter for mptcperrfastclosepassive.
		"""
		try :
			return self._mptcperrfastclosepassiverate
		except Exception as e:
			raise e

	@property
	def mptcperrnosffreensb(self) :
		r"""MPTCP output a packet without any subflow PCB.
		"""
		try :
			return self._mptcperrnosffreensb
		except Exception as e:
			raise e

	@property
	def mptcpdssrate(self) :
		r"""Rate (/s) counter for mptcptotdss.
		"""
		try :
			return self._mptcpdssrate
		except Exception as e:
			raise e

	@property
	def mptcpmpcapsynrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapsyn.
		"""
		try :
			return self._mptcpmpcapsynrate
		except Exception as e:
			raise e

	@property
	def mptcptxdssrate(self) :
		r"""Rate (/s) counter for mptcptottxdss.
		"""
		try :
			return self._mptcptxdssrate
		except Exception as e:
			raise e

	@property
	def mptcperrbadmapconndrop(self) :
		r"""MPTCP Drop the session incase of invalid Data Sequence map.
		"""
		try :
			return self._mptcperrbadmapconndrop
		except Exception as e:
			raise e

	@property
	def mptcpmpcapsteeredrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapsteered.
		"""
		try :
			return self._mptcpmpcapsteeredrate
		except Exception as e:
			raise e

	@property
	def mptcptxsffinrate(self) :
		r"""Rate (/s) counter for mptcptottxsffin.
		"""
		try :
			return self._mptcptxsffinrate
		except Exception as e:
			raise e

	@property
	def mptcpmpfailrecvd(self) :
		r"""MPTCP Total MP_FAIL received and fallback to regular TCP.
		"""
		try :
			return self._mptcpmpfailrecvd
		except Exception as e:
			raise e

	@property
	def mptcperrresflagsetrate(self) :
		r"""Rate (/s) counter for mptcperrresflagset.
		"""
		try :
			return self._mptcperrresflagsetrate
		except Exception as e:
			raise e

	@property
	def mptcpmpcapsfpcballocrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapsfpcballoc.
		"""
		try :
			return self._mptcpmpcapsfpcballocrate
		except Exception as e:
			raise e

	@property
	def mptcptotinfinitemapfrwd(self) :
		r"""MPTCP received Data Sequence Signal with  infinite map flag (Fallback to regular TCP).
		"""
		try :
			return self._mptcptotinfinitemapfrwd
		except Exception as e:
			raise e

	@property
	def mptcptottxdss(self) :
		r"""MMPTCP Total Data Sequence Signal packets sent.
		"""
		try :
			return self._mptcptottxdss
		except Exception as e:
			raise e

	@property
	def mptcperrdupmaprecvd(self) :
		r"""MPTCP Duplicate maps in Data Sequence map table.
		"""
		try :
			return self._mptcperrdupmaprecvd
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapsteered(self) :
		r"""Total MP_CAPABLE sessions steered.
		"""
		try :
			return self._mptcptotmpcapsteered
		except Exception as e:
			raise e

	@property
	def mptcperrretxpktrcvd(self) :
		r"""Retransmitted Data Recevied on MPTCP session.
		"""
		try :
			return self._mptcperrretxpktrcvd
		except Exception as e:
			raise e

	@property
	def mptcperrnopayloadlenpkt(self) :
		r"""MPTCP Payload length not specified in packet.
		"""
		try :
			return self._mptcperrnopayloadlenpkt
		except Exception as e:
			raise e

	@property
	def mptcptotmpcapsession(self) :
		r"""MPTCP total sessions created.
		"""
		try :
			return self._mptcptotmpcapsession
		except Exception as e:
			raise e

	@property
	def mptcpplainackfallback(self) :
		r"""MPTCP Fallback to regular tcp on receiving plain ACK for DSS.
		"""
		try :
			return self._mptcpplainackfallback
		except Exception as e:
			raise e

	@property
	def mptcpdatalessthandatalenrate(self) :
		r"""Rate (/s) counter for mptcptotdatalessthandatalen.
		"""
		try :
			return self._mptcpdatalessthandatalenrate
		except Exception as e:
			raise e

	@property
	def mptcperrunknowntoken(self) :
		r"""MPTCP invalid token received on MP_JOIN request.
		"""
		try :
			return self._mptcperrunknowntoken
		except Exception as e:
			raise e

	@property
	def mptcptotmpcballocfailed(self) :
		r"""Allocating memory to MPTCP protocol control block failed.
		"""
		try :
			return self._mptcptotmpcballocfailed
		except Exception as e:
			raise e

	@property
	def mptcptotdatalessthandatalen(self) :
		r"""MPTCP Map amount of data not yet received.
		"""
		try :
			return self._mptcptotdatalessthandatalen
		except Exception as e:
			raise e

	@property
	def mptcperrfastclosepassive(self) :
		r"""MPTCP Fast close received on passive subflow.
		"""
		try :
			return self._mptcperrfastclosepassive
		except Exception as e:
			raise e

	@property
	def mptcperrextnflagsetrate(self) :
		r"""Rate (/s) counter for mptcperrextnflagset.
		"""
		try :
			return self._mptcperrextnflagsetrate
		except Exception as e:
			raise e

	@property
	def mptcperrinvalremaddrrate(self) :
		r"""Rate (/s) counter for mptcperrinvalremaddr.
		"""
		try :
			return self._mptcperrinvalremaddrrate
		except Exception as e:
			raise e

	@property
	def mptcptottxsffin(self) :
		r"""MPTCP total subflow close requests.
		"""
		try :
			return self._mptcptottxsffin
		except Exception as e:
			raise e

	@property
	def mptcperrsfsessionallocfailrate(self) :
		r"""Rate (/s) counter for mptcperrsfsessionallocfail.
		"""
		try :
			return self._mptcperrsfsessionallocfailrate
		except Exception as e:
			raise e

	@property
	def mptcptotfreshackfrwd(self) :
		r"""Fresh ACK recieved on a subflow.
		"""
		try :
			return self._mptcptotfreshackfrwd
		except Exception as e:
			raise e

	@property
	def mptcperrjointhresholdrate(self) :
		r"""Rate (/s) counter for mptcperrjointhreshold.
		"""
		try :
			return self._mptcperrjointhresholdrate
		except Exception as e:
			raise e

	@property
	def mptcperrnosffreensbrate(self) :
		r"""Rate (/s) counter for mptcperrnosffreensb.
		"""
		try :
			return self._mptcperrnosffreensbrate
		except Exception as e:
			raise e

	@property
	def mptcperrresflagset(self) :
		r"""MPTCP One or more reserved bits are set on MP_CAPABLE request.
		"""
		try :
			return self._mptcperrresflagset
		except Exception as e:
			raise e

	@property
	def mptcperrnomappktrcvd(self) :
		r"""MPTCP Packet received with no Data Sequence Mapping.
		"""
		try :
			return self._mptcperrnomappktrcvd
		except Exception as e:
			raise e

	@property
	def mptcpestsfreplacedrate(self) :
		r"""Rate (/s) counter for mptcptotestsfreplaced.
		"""
		try :
			return self._mptcpestsfreplacedrate
		except Exception as e:
			raise e

	@property
	def mptcperraddridexistrate(self) :
		r"""Rate (/s) counter for mptcperraddridexist.
		"""
		try :
			return self._mptcperraddridexistrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpjoinfackrecvd(self) :
		r"""Total number of MP_JOIN Final ACKs.
		"""
		try :
			return self._mptcptotmpjoinfackrecvd
		except Exception as e:
			raise e

	@property
	def mptcpcursfconnections(self) :
		r"""The number of current mptcp subflow connections.
		"""
		try :
			return self._mptcpcursfconnections
		except Exception as e:
			raise e

	@property
	def mptcpinfinitemapfrwdrate(self) :
		r"""Rate (/s) counter for mptcptotinfinitemapfrwd.
		"""
		try :
			return self._mptcpinfinitemapfrwdrate
		except Exception as e:
			raise e

	@property
	def mptcperrjointhreshold(self) :
		r"""MPTCP Global pending MP_JOIN threshold limit is reached, new MP_JOIN request will be dropped sending RST.
		"""
		try :
			return self._mptcperrjointhreshold
		except Exception as e:
			raise e

	@property
	def mptcpmpcapsynacksentrate(self) :
		r"""Rate (/s) counter for mptcptotmpcapsynacksent.
		"""
		try :
			return self._mptcpmpcapsynacksentrate
		except Exception as e:
			raise e

	@property
	def mptcperrinvalmac(self) :
		r"""MPTCP invalid MAC on MP_JOIN final ACK.
		"""
		try :
			return self._mptcperrinvalmac
		except Exception as e:
			raise e

	@property
	def mptcptotpendsfreplaced(self) :
		r"""MPTCP Total pending subflows replaced due to new MP_JOIN.
		"""
		try :
			return self._mptcptotpendsfreplaced
		except Exception as e:
			raise e

	@property
	def mptcptotdssm(self) :
		r"""MPTCP total data Sequence Signal packets with Data Sequence Mapping and checksum.
		"""
		try :
			return self._mptcptotdssm
		except Exception as e:
			raise e

	@property
	def mptcperrversionnotsupported(self) :
		r"""MPTCP MP_CAPABLE request from unsupported mptcp client.
		"""
		try :
			return self._mptcperrversionnotsupported
		except Exception as e:
			raise e

	@property
	def mptcperrmpcapsessionallocfail(self) :
		r"""Creating a MPTCP connection failed due to failure in allocating memory to MPTCP connection management structure.
		"""
		try :
			return self._mptcperrmpcapsessionallocfail
		except Exception as e:
			raise e

	@property
	def mptcperrdupmaprecvdrate(self) :
		r"""Rate (/s) counter for mptcperrdupmaprecvd.
		"""
		try :
			return self._mptcperrdupmaprecvdrate
		except Exception as e:
			raise e

	@property
	def mptcperroptssendrstrate(self) :
		r"""Rate (/s) counter for mptcperroptssendrst.
		"""
		try :
			return self._mptcperroptssendrstrate
		except Exception as e:
			raise e

	@property
	def mptcpmpjoinsynrate(self) :
		r"""Rate (/s) counter for mptcptotmpjoinsyn.
		"""
		try :
			return self._mptcpmpjoinsynrate
		except Exception as e:
			raise e

	@property
	def mptcperroptsnosession(self) :
		r"""MPTCP options sent on non existing connection/subflow PCBs.
		"""
		try :
			return self._mptcperroptsnosession
		except Exception as e:
			raise e

	@property
	def mptcptottxdatafin(self) :
		r"""Total MPTCP connection close requests sent.
		"""
		try :
			return self._mptcptottxdatafin
		except Exception as e:
			raise e

	@property
	def mptcperrcryptonotsupported(self) :
		r"""MPTCP client crypto algorithm not supported.
		"""
		try :
			return self._mptcperrcryptonotsupported
		except Exception as e:
			raise e

	@property
	def mptcptotestsfreplaced(self) :
		r"""MPTCP Total established subflows replaced due to new MP_JOIN.
		"""
		try :
			return self._mptcptotestsfreplaced
		except Exception as e:
			raise e

	@property
	def mptcperroptiondiscarded(self) :
		r"""Invalid subtype in MPTCP option field and hence discarded.
		"""
		try :
			return self._mptcperroptiondiscarded
		except Exception as e:
			raise e

	@property
	def mptcperrbadcksumrate(self) :
		r"""Rate (/s) counter for mptcperrbadcksum.
		"""
		try :
			return self._mptcperrbadcksumrate
		except Exception as e:
			raise e

	@property
	def mptcperrmaxsfrate(self) :
		r"""Rate (/s) counter for mptcperrmaxsf.
		"""
		try :
			return self._mptcperrmaxsfrate
		except Exception as e:
			raise e

	@property
	def mptcptxdatafinrate(self) :
		r"""Rate (/s) counter for mptcptottxdatafin.
		"""
		try :
			return self._mptcptxdatafinrate
		except Exception as e:
			raise e

	@property
	def mptcpdssfreshackrate(self) :
		r"""Rate (/s) counter for mptcptotdssfreshack.
		"""
		try :
			return self._mptcpdssfreshackrate
		except Exception as e:
			raise e

	@property
	def mptcperrmpcapsessionallocfailrate(self) :
		r"""Rate (/s) counter for mptcperrmpcapsessionallocfail.
		"""
		try :
			return self._mptcperrmpcapsessionallocfailrate
		except Exception as e:
			raise e

	@property
	def mptcptotmpjoinsyn(self) :
		r"""MPTCP total MP_JOIN syn received.
		"""
		try :
			return self._mptcptotmpjoinsyn
		except Exception as e:
			raise e

	@property
	def mptcperrbadcksum(self) :
		r"""MPTCP checksum failed. Connection will fallback to regular tcp.
		"""
		try :
			return self._mptcperrbadcksum
		except Exception as e:
			raise e

	@property
	def mptcperrdatafinpassive(self) :
		r"""MPTCP Data FIN received on passive subflow.
		"""
		try :
			return self._mptcperrdatafinpassive
		except Exception as e:
			raise e

	@property
	def mptcptotdssfreshack(self) :
		r"""MPTCP total Data Sequence Signal packets during  data transfer with fresh ACK.
		"""
		try :
			return self._mptcptotdssfreshack
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolmptcp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolmptcp
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
		r""" Use this API to fetch the statistics of all protocolmptcp_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolmptcp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolmptcp_response(base_response) :
	def __init__(self, length=1) :
		self.protocolmptcp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolmptcp = [protocolmptcp_stats() for _ in range(length)]

