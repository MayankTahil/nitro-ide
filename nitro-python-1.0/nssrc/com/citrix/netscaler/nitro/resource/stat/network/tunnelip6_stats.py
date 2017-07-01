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

class tunnelip6_stats(base_resource) :
	r""" Statistics for TUNNEL Remote ip6address resource.
	"""
	def __init__(self) :
		self._tunnelip6 = None
		self._clearstats = None
		self._tnltotrxpkts = 0
		self._tnlrxpktsrate = 0
		self._tnltottxpkts = 0
		self._tnltxpktsrate = 0
		self._tnltotrxbytes = 0
		self._tnlrxbytesrate = 0
		self._tnltottxbytes = 0
		self._tnltxbytesrate = 0

	@property
	def tunnelip6(self) :
		r"""remote IPv6 address of the configured tunnel.<br/>Minimum length =  1.
		"""
		try :
			return self._tunnelip6
		except Exception as e:
			raise e

	@tunnelip6.setter
	def tunnelip6(self, tunnelip6) :
		r"""remote IPv6 address of the configured tunnel.
		"""
		try :
			self._tunnelip6 = tunnelip6
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
	def tnltxbytesrate(self) :
		r"""Rate (/s) counter for tnltottxbytes.
		"""
		try :
			return self._tnltxbytesrate
		except Exception as e:
			raise e

	@property
	def tnltotrxpkts(self) :
		r"""Total number of packets received on the tunnel.
		"""
		try :
			return self._tnltotrxpkts
		except Exception as e:
			raise e

	@property
	def tnltottxbytes(self) :
		r"""Total number of bytes transmitted on the tunnel.
		"""
		try :
			return self._tnltottxbytes
		except Exception as e:
			raise e

	@property
	def tnlrxbytesrate(self) :
		r"""Rate (/s) counter for tnltotrxbytes.
		"""
		try :
			return self._tnlrxbytesrate
		except Exception as e:
			raise e

	@property
	def tnltotrxbytes(self) :
		r"""Total number of bytes received on the tunnel.
		"""
		try :
			return self._tnltotrxbytes
		except Exception as e:
			raise e

	@property
	def tnltxpktsrate(self) :
		r"""Rate (/s) counter for tnltottxpkts.
		"""
		try :
			return self._tnltxpktsrate
		except Exception as e:
			raise e

	@property
	def tnlrxpktsrate(self) :
		r"""Rate (/s) counter for tnltotrxpkts.
		"""
		try :
			return self._tnlrxpktsrate
		except Exception as e:
			raise e

	@property
	def tnltottxpkts(self) :
		r"""Total number of packets transmitted on the tunnel.
		"""
		try :
			return self._tnltottxpkts
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(tunnelip6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.tunnelip6
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.tunnelip6 is not None :
				return str(self.tunnelip6)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all tunnelip6_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = tunnelip6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.tunnelip6 = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class tunnelip6_response(base_response) :
	def __init__(self, length=1) :
		self.tunnelip6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.tunnelip6 = [tunnelip6_stats() for _ in range(length)]

