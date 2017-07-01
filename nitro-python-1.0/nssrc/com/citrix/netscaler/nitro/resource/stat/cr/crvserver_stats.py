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

class crvserver_stats(base_resource) :
	r""" Statistics for CR virtual server resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
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
		self._invalidrequestresponse = 0
		self._invalidrequestresponsedropped = 0

		self.appfwpolicy = []
		self.cmppolicy = []
		self.responderpolicy = []
		self.rewritepolicy = []
		self.spilloverpolicy = []
		self.cachepolicy = []
		self.lbvserver = []
		self.icapolicy = []
		self.appqoepolicy = []
	@property
	def name(self) :
		r"""Name of a specific cache redirection virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of a specific cache redirection virtual server.
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
	def totalpktssent(self) :
		r"""Total number of packets sent.
		"""
		try :
			return self._totalpktssent
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
	def pktsrecvdrate(self) :
		r"""Rate (/s) counter for totalpktsrecvd.
		"""
		try :
			return self._pktsrecvdrate
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
	def responsesrate(self) :
		r"""Rate (/s) counter for totalresponses.
		"""
		try :
			return self._responsesrate
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
	def spilloverpolicy(self) :
		r"""spilloverpolicy that are bound to crvserver.
		"""
		try :
			return self._spilloverpolicy
		except Exception as e:
			raise e

	@spilloverpolicy.setter
	def spilloverpolicy(self, spilloverpolicy) :
		r"""spilloverpolicy that are bound to crvserver.
		"""
		try :
			self._spilloverpolicy = spilloverpolicy
		except Exception as e:
			raise e

	@property
	def icapolicy(self) :
		r"""icapolicy that are bound to crvserver.
		"""
		try :
			return self._icapolicy
		except Exception as e:
			raise e

	@icapolicy.setter
	def icapolicy(self, icapolicy) :
		r"""icapolicy that are bound to crvserver.
		"""
		try :
			self._icapolicy = icapolicy
		except Exception as e:
			raise e

	@property
	def cachepolicy(self) :
		r"""cachepolicy that are bound to crvserver.
		"""
		try :
			return self._cachepolicy
		except Exception as e:
			raise e

	@cachepolicy.setter
	def cachepolicy(self, cachepolicy) :
		r"""cachepolicy that are bound to crvserver.
		"""
		try :
			self._cachepolicy = cachepolicy
		except Exception as e:
			raise e

	@property
	def rewritepolicy(self) :
		r"""rewritepolicy that are bound to crvserver.
		"""
		try :
			return self._rewritepolicy
		except Exception as e:
			raise e

	@rewritepolicy.setter
	def rewritepolicy(self, rewritepolicy) :
		r"""rewritepolicy that are bound to crvserver.
		"""
		try :
			self._rewritepolicy = rewritepolicy
		except Exception as e:
			raise e

	@property
	def cmppolicy(self) :
		r"""cmppolicy that are bound to crvserver.
		"""
		try :
			return self._cmppolicy
		except Exception as e:
			raise e

	@cmppolicy.setter
	def cmppolicy(self, cmppolicy) :
		r"""cmppolicy that are bound to crvserver.
		"""
		try :
			self._cmppolicy = cmppolicy
		except Exception as e:
			raise e

	@property
	def appqoepolicy(self) :
		r"""appqoepolicy that are bound to crvserver.
		"""
		try :
			return self._appqoepolicy
		except Exception as e:
			raise e

	@appqoepolicy.setter
	def appqoepolicy(self, appqoepolicy) :
		r"""appqoepolicy that are bound to crvserver.
		"""
		try :
			self._appqoepolicy = appqoepolicy
		except Exception as e:
			raise e

	@property
	def lbvserver(self) :
		r"""lbvserver that are bound to crvserver.
		"""
		try :
			return self._lbvserver
		except Exception as e:
			raise e

	@lbvserver.setter
	def lbvserver(self, lbvserver) :
		r"""lbvserver that are bound to crvserver.
		"""
		try :
			self._lbvserver = lbvserver
		except Exception as e:
			raise e

	@property
	def responderpolicy(self) :
		r"""responderpolicy that are bound to crvserver.
		"""
		try :
			return self._responderpolicy
		except Exception as e:
			raise e

	@responderpolicy.setter
	def responderpolicy(self, responderpolicy) :
		r"""responderpolicy that are bound to crvserver.
		"""
		try :
			self._responderpolicy = responderpolicy
		except Exception as e:
			raise e

	@property
	def appfwpolicy(self) :
		r"""appfwpolicy that are bound to crvserver.
		"""
		try :
			return self._appfwpolicy
		except Exception as e:
			raise e

	@appfwpolicy.setter
	def appfwpolicy(self, appfwpolicy) :
		r"""appfwpolicy that are bound to crvserver.
		"""
		try :
			self._appfwpolicy = appfwpolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(crvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.crvserver
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
		r""" Use this API to fetch the statistics of all crvserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = crvserver_stats()
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

class crvserver_response(base_response) :
	def __init__(self, length=1) :
		self.crvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.crvserver = [crvserver_stats() for _ in range(length)]

