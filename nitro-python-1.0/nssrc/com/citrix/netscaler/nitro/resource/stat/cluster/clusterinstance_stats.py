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

class clusterinstance_stats(base_resource) :
	r""" Statistics for cluster instance resource.
	"""
	def __init__(self) :
		self._clid = None
		self._clearstats = None
		self._clnumnodes = 0
		self._clcurstatus = ""
		self._clviewleader = ""
		self._totsteeredpkts = 0
		self._clbkplanerx = 0
		self._clbkplanerxrate = 0
		self._clbkplanetx = 0
		self._clbkplanetxrate = 0
		self._numdfddroppkts = 0
		self._totpropagationtimeout = 0

	@property
	def clid(self) :
		r"""ID of the cluster instance for which to display statistics.<br/>Minimum value =  1<br/>Maximum value =  16.
		"""
		try :
			return self._clid
		except Exception as e:
			raise e

	@clid.setter
	def clid(self, clid) :
		r"""ID of the cluster instance for which to display statistics.
		"""
		try :
			self._clid = clid
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
	def totpropagationtimeout(self) :
		r"""Number of times the update to the client timed-out.
		"""
		try :
			return self._totpropagationtimeout
		except Exception as e:
			raise e

	@property
	def clbkplanetx(self) :
		r"""Traffic transmitted from backplane (in mbits).
		"""
		try :
			return self._clbkplanetx
		except Exception as e:
			raise e

	@property
	def clbkplanetxrate(self) :
		r"""Rate (/s) counter for clbkplanetx.
		"""
		try :
			return self._clbkplanetxrate
		except Exception as e:
			raise e

	@property
	def totsteeredpkts(self) :
		r"""Total number of packets steered on the cluster backplane.
		"""
		try :
			return self._totsteeredpkts
		except Exception as e:
			raise e

	@property
	def numdfddroppkts(self) :
		r"""Number of steered packets that are dropped.
		"""
		try :
			return self._numdfddroppkts
		except Exception as e:
			raise e

	@property
	def clviewleader(self) :
		r"""NSIP address of the Configuration Coordinator of the cluster.
		"""
		try :
			return self._clviewleader
		except Exception as e:
			raise e

	@property
	def clbkplanerx(self) :
		r"""Traffic received on backplane (in mbits).
		"""
		try :
			return self._clbkplanerx
		except Exception as e:
			raise e

	@property
	def clcurstatus(self) :
		r"""State of the cluster.
		"""
		try :
			return self._clcurstatus
		except Exception as e:
			raise e

	@property
	def clnumnodes(self) :
		r"""Number of nodes in the cluster.
		"""
		try :
			return self._clnumnodes
		except Exception as e:
			raise e

	@property
	def clbkplanerxrate(self) :
		r"""Rate (/s) counter for clbkplanerx.
		"""
		try :
			return self._clbkplanerxrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusterinstance_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusterinstance
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.clid is not None :
				return str(self.clid)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all clusterinstance_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = clusterinstance_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.clid = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class clusterinstance_response(base_response) :
	def __init__(self, length=1) :
		self.clusterinstance = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusterinstance = [clusterinstance_stats() for _ in range(length)]

