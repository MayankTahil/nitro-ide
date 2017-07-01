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

class lbvserver_stats(base_resource) :
	r""" Statistics for Load Balancing Virtual Server resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._sortby = None
		self._sortorder = None
		self._avgcltttlb = 0
		self._cltresponsetimeapdex = 0
		self._vsvrsurgecount = 0
		self._establishedconn = 0
		self._inactsvcs = 0
		self._vslbhealth = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
		self._actsvcs = 0
		self._tothits = 0
		self._hitsrate = 0
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0
		self._totalpktsrecvd = 0
		self._pktsrecvdrate = 0
		self._totalpktssent = 0
		self._pktssentrate = 0
		self._curclntconnections = 0
		self._cursrvrconnections = 0
		self._curpersistencesessions = 0
		self._surgecount = 0
		self._svcsurgecount = 0
		self._sothreshold = 0
		self._totspillovers = 0
		self._labelledconn = 0
		self._pushlabel = 0
		self._deferredreq = 0
		self._deferredreqrate = 0
		self._invalidrequestresponse = 0
		self._invalidrequestresponsedropped = 0
		self._totvserverdownbackuphits = 0
		self._curmptcpsessions = 0
		self._cursubflowconn = 0
		self._totcltttlbtransactions = 0
		self._toleratingttlbtransactions = 0
		self._frustratingttlbtransactions = 0

		self.scpolicy = []
		self.service = []
		self.transformpolicy = []
		self.appfwpolicy = []
		self.cmppolicy = []
		self.responderpolicy = []
		self.videooptimizationpolicy = []
		self.tmtrafficpolicy = []
		self.pqpolicy = []
		self.rewritepolicy = []
		self.spilloverpolicy = []
		self.cachepolicy = []
		self.servicegroup = []
		self.appqoepolicy = []
	@property
	def name(self) :
		r"""Name of the virtual server. If no name is provided, statistical data of all configured virtual servers is displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the virtual server. If no name is provided, statistical data of all configured virtual servers is displayed.
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
	def sortby(self) :
		r"""use this argument to sort by specific key.<br/>Possible values = .
		"""
		try :
			return self._sortby
		except Exception as e:
			raise e

	@sortby.setter
	def sortby(self, sortby) :
		r"""use this argument to sort by specific key
		"""
		try :
			self._sortby = sortby
		except Exception as e:
			raise e

	@property
	def sortorder(self) :
		r"""use this argument to specify sort order.<br/>Default value: SORT_DESCENDING<br/>Possible values = ascending, descending.
		"""
		try :
			return self._sortorder
		except Exception as e:
			raise e

	@sortorder.setter
	def sortorder(self, sortorder) :
		r"""use this argument to specify sort order
		"""
		try :
			self._sortorder = sortorder
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
	def establishedconn(self) :
		r"""Number of client connections in ESTABLISHED state.
		"""
		try :
			return self._establishedconn
		except Exception as e:
			raise e

	@property
	def totalpktssent(self) :
		r"""Total number of packets sent.
		"""
		try :
			return self._totalpktssent
		except Exception as e:
			raise e

	@property
	def labelledconn(self) :
		r"""Number of Labeled connection on this vserver.
		"""
		try :
			return self._labelledconn
		except Exception as e:
			raise e

	@property
	def tothits(self) :
		r"""Total vserver hits.
		"""
		try :
			return self._tothits
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
	def sothreshold(self) :
		r"""Spill Over Threshold set on the VServer.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@property
	def cursubflowconn(self) :
		r"""Current Multipath TCP subflows.
		"""
		try :
			return self._cursubflowconn
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
	def invalidrequestresponsedropped(self) :
		r"""Number invalid requests/responses dropped on this vserver.
		"""
		try :
			return self._invalidrequestresponsedropped
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
	def curpersistencesessions(self) :
		r"""current vserver owned persistence sessions.
		"""
		try :
			return self._curpersistencesessions
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
	def avgcltttlb(self) :
		r"""Average TTLB between the client and the server. TTLB is the time interval between sending the request packet to a service and receiving the ACK for response from client.
		"""
		try :
			return self._avgcltttlb
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Protocol associated with the vserver.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def hitsrate(self) :
		r"""Rate (/s) counter for tothits.
		"""
		try :
			return self._hitsrate
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
	def cltresponsetimeapdex(self) :
		r"""Vserver APDEX index based on client response times.
		"""
		try :
			return self._cltresponsetimeapdex
		except Exception as e:
			raise e

	@property
	def totcltttlbtransactions(self) :
		r"""Total transactions where client TTLB is calculated.
		"""
		try :
			return self._totcltttlbtransactions
		except Exception as e:
			raise e

	@property
	def pktsrecvdrate(self) :
		r"""Rate (/s) counter for totalpktsrecvd.
		"""
		try :
			return self._pktsrecvdrate
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		r"""IP address of the vserver.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def vsvrsurgecount(self) :
		r"""Number of requests waiting on this vserver. .
		"""
		try :
			return self._vsvrsurgecount
		except Exception as e:
			raise e

	@property
	def pushlabel(self) :
		r"""Number of labels for this push vserver.
		"""
		try :
			return self._pushlabel
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
	def deferredreq(self) :
		r"""Number of deferred request on this vserver.
		"""
		try :
			return self._deferredreq
		except Exception as e:
			raise e

	@property
	def curmptcpsessions(self) :
		r"""Current Multipath TCP sessions.
		"""
		try :
			return self._curmptcpsessions
		except Exception as e:
			raise e

	@property
	def totspillovers(self) :
		r"""Number of times vserver experienced spill over.
		"""
		try :
			return self._totspillovers
		except Exception as e:
			raise e

	@property
	def svcsurgecount(self) :
		r"""Total number of requests in the surge queues of all the services bound to this LB-vserver.
		"""
		try :
			return self._svcsurgecount
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
	def invalidrequestresponse(self) :
		r"""Number invalid requests/responses on this vserver.
		"""
		try :
			return self._invalidrequestresponse
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
	def vslbhealth(self) :
		r"""Health of the vserver. This gives percentage of UP services bound to this vserver.
		"""
		try :
			return self._vslbhealth
		except Exception as e:
			raise e

	@property
	def deferredreqrate(self) :
		r"""Rate (/s) counter for deferredreq.
		"""
		try :
			return self._deferredreqrate
		except Exception as e:
			raise e

	@property
	def actsvcs(self) :
		r"""number of ACTIVE services bound to a vserver.
		"""
		try :
			return self._actsvcs
		except Exception as e:
			raise e

	@property
	def totalpktsrecvd(self) :
		r"""Total number of packets received by this service or virtual server.
		"""
		try :
			return self._totalpktsrecvd
		except Exception as e:
			raise e

	@property
	def pktssentrate(self) :
		r"""Rate (/s) counter for totalpktssent.
		"""
		try :
			return self._pktssentrate
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

	@property
	def totvserverdownbackuphits(self) :
		r"""Number of times traffic was diverted to backup vserver since primary vserver was DOWN.
		"""
		try :
			return self._totvserverdownbackuphits
		except Exception as e:
			raise e

	@property
	def inactsvcs(self) :
		r"""number of INACTIVE services bound to a vserver.
		"""
		try :
			return self._inactsvcs
		except Exception as e:
			raise e

	@property
	def spilloverpolicy(self) :
		r"""spilloverpolicy that are bound to lbvserver.
		"""
		try :
			return self._spilloverpolicy
		except Exception as e:
			raise e

	@spilloverpolicy.setter
	def spilloverpolicy(self, spilloverpolicy) :
		r"""spilloverpolicy that are bound to lbvserver.
		"""
		try :
			self._spilloverpolicy = spilloverpolicy
		except Exception as e:
			raise e

	@property
	def cachepolicy(self) :
		r"""cachepolicy that are bound to lbvserver.
		"""
		try :
			return self._cachepolicy
		except Exception as e:
			raise e

	@cachepolicy.setter
	def cachepolicy(self, cachepolicy) :
		r"""cachepolicy that are bound to lbvserver.
		"""
		try :
			self._cachepolicy = cachepolicy
		except Exception as e:
			raise e

	@property
	def rewritepolicy(self) :
		r"""rewritepolicy that are bound to lbvserver.
		"""
		try :
			return self._rewritepolicy
		except Exception as e:
			raise e

	@rewritepolicy.setter
	def rewritepolicy(self, rewritepolicy) :
		r"""rewritepolicy that are bound to lbvserver.
		"""
		try :
			self._rewritepolicy = rewritepolicy
		except Exception as e:
			raise e

	@property
	def pqpolicy(self) :
		r"""pqpolicy that are bound to lbvserver.
		"""
		try :
			return self._pqpolicy
		except Exception as e:
			raise e

	@pqpolicy.setter
	def pqpolicy(self, pqpolicy) :
		r"""pqpolicy that are bound to lbvserver.
		"""
		try :
			self._pqpolicy = pqpolicy
		except Exception as e:
			raise e

	@property
	def scpolicy(self) :
		r"""scpolicy that are bound to lbvserver.
		"""
		try :
			return self._scpolicy
		except Exception as e:
			raise e

	@scpolicy.setter
	def scpolicy(self, scpolicy) :
		r"""scpolicy that are bound to lbvserver.
		"""
		try :
			self._scpolicy = scpolicy
		except Exception as e:
			raise e

	@property
	def servicegroup(self) :
		r"""servicegroup that are bound to lbvserver.
		"""
		try :
			return self._servicegroup
		except Exception as e:
			raise e

	@servicegroup.setter
	def servicegroup(self, servicegroup) :
		r"""servicegroup that are bound to lbvserver.
		"""
		try :
			self._servicegroup = servicegroup
		except Exception as e:
			raise e

	@property
	def service(self) :
		r"""service that are bound to lbvserver.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@service.setter
	def service(self, service) :
		r"""service that are bound to lbvserver.
		"""
		try :
			self._service = service
		except Exception as e:
			raise e

	@property
	def cmppolicy(self) :
		r"""cmppolicy that are bound to lbvserver.
		"""
		try :
			return self._cmppolicy
		except Exception as e:
			raise e

	@cmppolicy.setter
	def cmppolicy(self, cmppolicy) :
		r"""cmppolicy that are bound to lbvserver.
		"""
		try :
			self._cmppolicy = cmppolicy
		except Exception as e:
			raise e

	@property
	def appqoepolicy(self) :
		r"""appqoepolicy that are bound to lbvserver.
		"""
		try :
			return self._appqoepolicy
		except Exception as e:
			raise e

	@appqoepolicy.setter
	def appqoepolicy(self, appqoepolicy) :
		r"""appqoepolicy that are bound to lbvserver.
		"""
		try :
			self._appqoepolicy = appqoepolicy
		except Exception as e:
			raise e

	@property
	def tmtrafficpolicy(self) :
		r"""tmtrafficpolicy that are bound to lbvserver.
		"""
		try :
			return self._tmtrafficpolicy
		except Exception as e:
			raise e

	@tmtrafficpolicy.setter
	def tmtrafficpolicy(self, tmtrafficpolicy) :
		r"""tmtrafficpolicy that are bound to lbvserver.
		"""
		try :
			self._tmtrafficpolicy = tmtrafficpolicy
		except Exception as e:
			raise e

	@property
	def responderpolicy(self) :
		r"""responderpolicy that are bound to lbvserver.
		"""
		try :
			return self._responderpolicy
		except Exception as e:
			raise e

	@responderpolicy.setter
	def responderpolicy(self, responderpolicy) :
		r"""responderpolicy that are bound to lbvserver.
		"""
		try :
			self._responderpolicy = responderpolicy
		except Exception as e:
			raise e

	@property
	def transformpolicy(self) :
		r"""transformpolicy that are bound to lbvserver.
		"""
		try :
			return self._transformpolicy
		except Exception as e:
			raise e

	@transformpolicy.setter
	def transformpolicy(self, transformpolicy) :
		r"""transformpolicy that are bound to lbvserver.
		"""
		try :
			self._transformpolicy = transformpolicy
		except Exception as e:
			raise e

	@property
	def appfwpolicy(self) :
		r"""appfwpolicy that are bound to lbvserver.
		"""
		try :
			return self._appfwpolicy
		except Exception as e:
			raise e

	@appfwpolicy.setter
	def appfwpolicy(self, appfwpolicy) :
		r"""appfwpolicy that are bound to lbvserver.
		"""
		try :
			self._appfwpolicy = appfwpolicy
		except Exception as e:
			raise e

	@property
	def videooptimizationpolicy(self) :
		r"""videooptimizationpolicy that are bound to lbvserver.
		"""
		try :
			return self._videooptimizationpolicy
		except Exception as e:
			raise e

	@videooptimizationpolicy.setter
	def videooptimizationpolicy(self, videooptimizationpolicy) :
		r"""videooptimizationpolicy that are bound to lbvserver.
		"""
		try :
			self._videooptimizationpolicy = videooptimizationpolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbvserver
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
		r""" Use this API to fetch the statistics of all lbvserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = lbvserver_stats()
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

	class Sortorder:
		ascending = "ascending"
		descending = "descending"

class lbvserver_response(base_response) :
	def __init__(self, length=1) :
		self.lbvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbvserver = [lbvserver_stats() for _ in range(length)]

