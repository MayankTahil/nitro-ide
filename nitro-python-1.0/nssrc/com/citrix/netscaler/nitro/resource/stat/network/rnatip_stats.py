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

class rnatip_stats(base_resource) :
	r""" Statistics for RNAT ipaddress resource.
	"""
	def __init__(self) :
		self._Rnatip = None
		self._clearstats = None
		self._iptd = 0
		self._iprnattotrxbytes = 0
		self._iprnatrxbytesrate = 0
		self._iprnattottxbytes = 0
		self._iprnattxbytesrate = 0
		self._iprnattotrxpkts = 0
		self._iprnatrxpktsrate = 0
		self._iprnattottxpkts = 0
		self._iprnattxpktsrate = 0
		self._iprnattottxsyn = 0
		self._iprnattxsynrate = 0
		self._iprnatcursessions = 0

	@property
	def Rnatip(self) :
		r"""Specifies the NAT IP address of the configured RNAT entry for which you want to see the statistics. If you do not specify an IP address, this displays the statistics for all the configured RNAT entries.<br/>Minimum length =  1.
		"""
		try :
			return self._Rnatip
		except Exception as e:
			raise e

	@Rnatip.setter
	def Rnatip(self, Rnatip) :
		r"""Specifies the NAT IP address of the configured RNAT entry for which you want to see the statistics. If you do not specify an IP address, this displays the statistics for all the configured RNAT entries.
		"""
		try :
			self._Rnatip = Rnatip
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
	def iprnatrxpktsrate(self) :
		r"""Rate (/s) counter for iprnattotrxpkts.
		"""
		try :
			return self._iprnatrxpktsrate
		except Exception as e:
			raise e

	@property
	def iprnattxpktsrate(self) :
		r"""Rate (/s) counter for iprnattottxpkts.
		"""
		try :
			return self._iprnattxpktsrate
		except Exception as e:
			raise e

	@property
	def iprnattottxpkts(self) :
		r"""Packets sent from this IP address during RNAT sessions.
		"""
		try :
			return self._iprnattottxpkts
		except Exception as e:
			raise e

	@property
	def iptd(self) :
		r"""Traffic domain for ipaddr.
		"""
		try :
			return self._iptd
		except Exception as e:
			raise e

	@property
	def iprnattottxbytes(self) :
		r"""Bytes sent from this IP address during RNAT sessions.
		"""
		try :
			return self._iprnattottxbytes
		except Exception as e:
			raise e

	@property
	def iprnatcursessions(self) :
		r"""Currently active RNAT sessions started from this IP address.
		"""
		try :
			return self._iprnatcursessions
		except Exception as e:
			raise e

	@property
	def iprnatrxbytesrate(self) :
		r"""Rate (/s) counter for iprnattotrxbytes.
		"""
		try :
			return self._iprnatrxbytesrate
		except Exception as e:
			raise e

	@property
	def iprnattotrxbytes(self) :
		r"""Bytes received on this IP address during RNAT sessions.
		"""
		try :
			return self._iprnattotrxbytes
		except Exception as e:
			raise e

	@property
	def iprnattxsynrate(self) :
		r"""Rate (/s) counter for iprnattottxsyn.
		"""
		try :
			return self._iprnattxsynrate
		except Exception as e:
			raise e

	@property
	def iprnattxbytesrate(self) :
		r"""Rate (/s) counter for iprnattottxbytes.
		"""
		try :
			return self._iprnattxbytesrate
		except Exception as e:
			raise e

	@property
	def iprnattotrxpkts(self) :
		r"""Packets received on this IP address during RNAT sessions.
		"""
		try :
			return self._iprnattotrxpkts
		except Exception as e:
			raise e

	@property
	def iprnattottxsyn(self) :
		r"""Requests for connections sent from this IP address during RNAT sessions.
		"""
		try :
			return self._iprnattottxsyn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnatip_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnatip
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.Rnatip is not None :
				return str(self.Rnatip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all rnatip_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = rnatip_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.Rnatip = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class rnatip_response(base_response) :
	def __init__(self, length=1) :
		self.rnatip = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnatip = [rnatip_stats() for _ in range(length)]

