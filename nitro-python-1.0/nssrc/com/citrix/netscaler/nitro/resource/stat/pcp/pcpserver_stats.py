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

class pcpserver_stats(base_resource) :
	r""" Statistics for server resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._pcptotrequests = 0
		self._pcprequestsrate = 0
		self._pcptotresponses = 0
		self._pcpresponsesrate = 0
		self._pcptotmaprequests = 0
		self._pcpmaprequestsrate = 0
		self._pcptotpeerrequests = 0
		self._pcppeerrequestsrate = 0
		self._pcptoterrinrquest = 0
		self._pcperrinrquestrate = 0
		self._pcptoterrinres = 0
		self._pcperrinresrate = 0
		self._pcptotunsuppvers = 0
		self._pcpunsuppversrate = 0
		self._pcptotmalformedreq = 0
		self._pcpmalformedreqrate = 0
		self._pcptotunsuppopcode = 0
		self._pcpunsuppopcoderate = 0
		self._pcptotunsuppoption = 0
		self._pcpunsuppoptionrate = 0
		self._pcptotmalformedoption = 0
		self._pcpmalformedoptionrate = 0
		self._pcptotnetfailure = 0
		self._pcpnetfailurerate = 0
		self._pcptotnoresources = 0
		self._pcpnoresourcesrate = 0
		self._pcptotunsupportedprotocol = 0
		self._pcpunsupportedprotocolrate = 0
		self._pcptotuserexqouta = 0
		self._pcpuserexqoutarate = 0
		self._pcptotnoexternal = 0
		self._pcpnoexternalrate = 0
		self._pcptotaddrmismatch = 0
		self._pcpaddrmismatchrate = 0
		self._pcptotexcesspeers = 0
		self._pcpexcesspeersrate = 0

	@property
	def name(self) :
		r"""PCP Statistics per Server.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""PCP Statistics per Server
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
	def pcpaddrmismatchrate(self) :
		r"""Rate (/s) counter for pcptotaddrmismatch.
		"""
		try :
			return self._pcpaddrmismatchrate
		except Exception as e:
			raise e

	@property
	def pcptotmalformedreq(self) :
		r"""total PCP request having malformed PCP packets.
		"""
		try :
			return self._pcptotmalformedreq
		except Exception as e:
			raise e

	@property
	def pcpnoresourcesrate(self) :
		r"""Rate (/s) counter for pcptotnoresources.
		"""
		try :
			return self._pcpnoresourcesrate
		except Exception as e:
			raise e

	@property
	def pcpunsuppopcoderate(self) :
		r"""Rate (/s) counter for pcptotunsuppopcode.
		"""
		try :
			return self._pcpunsuppopcoderate
		except Exception as e:
			raise e

	@property
	def pcptotpeerrequests(self) :
		r"""PCP PEER Requests received.
		"""
		try :
			return self._pcptotpeerrequests
		except Exception as e:
			raise e

	@property
	def pcpnetfailurerate(self) :
		r"""Rate (/s) counter for pcptotnetfailure.
		"""
		try :
			return self._pcpnetfailurerate
		except Exception as e:
			raise e

	@property
	def pcptoterrinrquest(self) :
		r"""total PCP request with error.
		"""
		try :
			return self._pcptoterrinrquest
		except Exception as e:
			raise e

	@property
	def pcptotmalformedoption(self) :
		r"""total malformed OPTIONS received in requests.
		"""
		try :
			return self._pcptotmalformedoption
		except Exception as e:
			raise e

	@property
	def pcptotresponses(self) :
		r"""Number PCP responces sent.
		"""
		try :
			return self._pcptotresponses
		except Exception as e:
			raise e

	@property
	def pcpunsupportedprotocolrate(self) :
		r"""Rate (/s) counter for pcptotunsupportedprotocol.
		"""
		try :
			return self._pcpunsupportedprotocolrate
		except Exception as e:
			raise e

	@property
	def pcptotnoresources(self) :
		r"""no resources.
		"""
		try :
			return self._pcptotnoresources
		except Exception as e:
			raise e

	@property
	def pcptotnetfailure(self) :
		r"""Total Network Failures.
		"""
		try :
			return self._pcptotnetfailure
		except Exception as e:
			raise e

	@property
	def pcppeerrequestsrate(self) :
		r"""Rate (/s) counter for pcptotpeerrequests.
		"""
		try :
			return self._pcppeerrequestsrate
		except Exception as e:
			raise e

	@property
	def pcptotnoexternal(self) :
		r"""Total responses with opcode can not provide external.
		"""
		try :
			return self._pcptotnoexternal
		except Exception as e:
			raise e

	@property
	def pcperrinresrate(self) :
		r"""Rate (/s) counter for pcptoterrinres.
		"""
		try :
			return self._pcperrinresrate
		except Exception as e:
			raise e

	@property
	def pcptotunsuppopcode(self) :
		r"""total Unsupproted OPCODES received Requests.
		"""
		try :
			return self._pcptotunsuppopcode
		except Exception as e:
			raise e

	@property
	def pcpunsuppversrate(self) :
		r"""Rate (/s) counter for pcptotunsuppvers.
		"""
		try :
			return self._pcpunsuppversrate
		except Exception as e:
			raise e

	@property
	def pcptotuserexqouta(self) :
		r"""Total user ex quota.
		"""
		try :
			return self._pcptotuserexqouta
		except Exception as e:
			raise e

	@property
	def pcptotunsuppvers(self) :
		r"""PCP request with unsupported version.
		"""
		try :
			return self._pcptotunsuppvers
		except Exception as e:
			raise e

	@property
	def pcpuserexqoutarate(self) :
		r"""Rate (/s) counter for pcptotuserexqouta.
		"""
		try :
			return self._pcpuserexqoutarate
		except Exception as e:
			raise e

	@property
	def pcptotunsupportedprotocol(self) :
		r"""Total Unsupported Protocols requests.
		"""
		try :
			return self._pcptotunsupportedprotocol
		except Exception as e:
			raise e

	@property
	def pcpexcesspeersrate(self) :
		r"""Rate (/s) counter for pcptotexcesspeers.
		"""
		try :
			return self._pcpexcesspeersrate
		except Exception as e:
			raise e

	@property
	def pcpmalformedoptionrate(self) :
		r"""Rate (/s) counter for pcptotmalformedoption.
		"""
		try :
			return self._pcpmalformedoptionrate
		except Exception as e:
			raise e

	@property
	def pcptotrequests(self) :
		r"""PCP Request received.
		"""
		try :
			return self._pcptotrequests
		except Exception as e:
			raise e

	@property
	def pcperrinrquestrate(self) :
		r"""Rate (/s) counter for pcptoterrinrquest.
		"""
		try :
			return self._pcperrinrquestrate
		except Exception as e:
			raise e

	@property
	def pcpresponsesrate(self) :
		r"""Rate (/s) counter for pcptotresponses.
		"""
		try :
			return self._pcpresponsesrate
		except Exception as e:
			raise e

	@property
	def pcpunsuppoptionrate(self) :
		r"""Rate (/s) counter for pcptotunsuppoption.
		"""
		try :
			return self._pcpunsuppoptionrate
		except Exception as e:
			raise e

	@property
	def pcpmaprequestsrate(self) :
		r"""Rate (/s) counter for pcptotmaprequests.
		"""
		try :
			return self._pcpmaprequestsrate
		except Exception as e:
			raise e

	@property
	def pcpnoexternalrate(self) :
		r"""Rate (/s) counter for pcptotnoexternal.
		"""
		try :
			return self._pcpnoexternalrate
		except Exception as e:
			raise e

	@property
	def pcptotunsuppoption(self) :
		r"""total Unsupproted OPTIONS received in requests.
		"""
		try :
			return self._pcptotunsuppoption
		except Exception as e:
			raise e

	@property
	def pcptoterrinres(self) :
		r"""Total PCP responses with errors.
		"""
		try :
			return self._pcptoterrinres
		except Exception as e:
			raise e

	@property
	def pcptotmaprequests(self) :
		r"""PCP MAP Requests received.
		"""
		try :
			return self._pcptotmaprequests
		except Exception as e:
			raise e

	@property
	def pcptotexcesspeers(self) :
		r"""Total responses with opcode excessive remote peers.
		"""
		try :
			return self._pcptotexcesspeers
		except Exception as e:
			raise e

	@property
	def pcpmalformedreqrate(self) :
		r"""Rate (/s) counter for pcptotmalformedreq.
		"""
		try :
			return self._pcpmalformedreqrate
		except Exception as e:
			raise e

	@property
	def pcprequestsrate(self) :
		r"""Rate (/s) counter for pcptotrequests.
		"""
		try :
			return self._pcprequestsrate
		except Exception as e:
			raise e

	@property
	def pcptotaddrmismatch(self) :
		r"""Total address mismatch.
		"""
		try :
			return self._pcptotaddrmismatch
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pcpserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pcpserver
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
		r""" Use this API to fetch the statistics of all pcpserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = pcpserver_stats()
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

class pcpserver_response(base_response) :
	def __init__(self, length=1) :
		self.pcpserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pcpserver = [pcpserver_stats() for _ in range(length)]

