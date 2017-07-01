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

class gslbvserver_stats(base_resource) :
	r""" Statistics for Global Server Load Balancing Virtual Server resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._establishedconn = 0
		self._inactsvcs = 0
		self._vslbhealth = 0
		self._type = ""
		self._state = ""
		self._actsvcs = 0
		self._tothits = 0
		self._hitsrate = 0
		self._curpersistencesessions = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0
		self._sothreshold = 0
		self._totspillovers = 0
		self._totvserverdownbackuphits = 0
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._curclntconnections = 0
		self._cursrvrconnections = 0

		self.gslbservice = []
		self.spilloverpolicy = []
	@property
	def name(self) :
		r"""Name of the GSLB virtual server for which to display statistics. If you do not specify a name, statistics are displayed for all GSLB virtual servers.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the GSLB virtual server for which to display statistics. If you do not specify a name, statistics are displayed for all GSLB virtual servers.
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
	def responsesrate(self) :
		r"""Rate (/s) counter for totalresponses.
		"""
		try :
			return self._responsesrate
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
	def totalrequestbytes(self) :
		r"""Total number of request bytes received on this service or virtual server.
		"""
		try :
			return self._totalrequestbytes
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
	def actsvcs(self) :
		r"""number of ACTIVE services bound to a vserver.
		"""
		try :
			return self._actsvcs
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
		r"""spilloverpolicy that are bound to gslbvserver.
		"""
		try :
			return self._spilloverpolicy
		except Exception as e:
			raise e

	@spilloverpolicy.setter
	def spilloverpolicy(self, spilloverpolicy) :
		r"""spilloverpolicy that are bound to gslbvserver.
		"""
		try :
			self._spilloverpolicy = spilloverpolicy
		except Exception as e:
			raise e

	@property
	def gslbservice(self) :
		r"""gslbservice that are bound to gslbvserver.
		"""
		try :
			return self._gslbservice
		except Exception as e:
			raise e

	@gslbservice.setter
	def gslbservice(self, gslbservice) :
		r"""gslbservice that are bound to gslbvserver.
		"""
		try :
			self._gslbservice = gslbservice
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbvserver
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
		r""" Use this API to fetch the statistics of all gslbvserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = gslbvserver_stats()
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

class gslbvserver_response(base_response) :
	def __init__(self, length=1) :
		self.gslbvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbvserver = [gslbvserver_stats() for _ in range(length)]

