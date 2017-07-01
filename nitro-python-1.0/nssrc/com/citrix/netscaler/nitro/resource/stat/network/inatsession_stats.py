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

class inatsession_stats(base_resource) :
	r""" Statistics for stateful INAT resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._globalinathits = 0
		self._globalinathitsrate = 0
		self._globalinatcursessions = 0
		self._globalinatcursessionsrate = 0
		self._globalinatreceivebytes = 0
		self._globalinatreceivebytesrate = 0
		self._globalinattotsentbytes = 0
		self._globalinatsentbytesrate = 0
		self._globalinatpktreceived = 0
		self._globalinatpktreceivedrate = 0
		self._globalinatpktsent = 0
		self._globalinatpktsentrate = 0
		self._inattothits = 0
		self._inathitsrate = 0
		self._inatcursessions = 0
		self._inatcursessionsrate = 0
		self._inattotreceivebytes = 0
		self._inatreceivebytesrate = 0
		self._inattotsentbytes = 0
		self._inatsentbytesrate = 0
		self._inattotpktreceived = 0
		self._inatpktreceivedrate = 0
		self._inattotpktsent = 0
		self._inatpktsentrate = 0

	@property
	def name(self) :
		r"""INAT name.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""INAT name
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
	def globalinatreceivebytes(self) :
		r"""Total INAT Received Bytes.
		"""
		try :
			return self._globalinatreceivebytes
		except Exception as e:
			raise e

	@property
	def globalinatcursessions(self) :
		r"""Total INAT current sessions.
		"""
		try :
			return self._globalinatcursessions
		except Exception as e:
			raise e

	@property
	def inattotsentbytes(self) :
		r"""INAT total Sent Bytes.
		"""
		try :
			return self._inattotsentbytes
		except Exception as e:
			raise e

	@property
	def globalinatpktsent(self) :
		r"""Total INAT Packets Sent.
		"""
		try :
			return self._globalinatpktsent
		except Exception as e:
			raise e

	@property
	def inatreceivebytesrate(self) :
		r"""Rate (/s) counter for inattotreceivebytes.
		"""
		try :
			return self._inatreceivebytesrate
		except Exception as e:
			raise e

	@property
	def globalinatsentbytesrate(self) :
		r"""Rate (/s) counter for globalinattotsentbytes.
		"""
		try :
			return self._globalinatsentbytesrate
		except Exception as e:
			raise e

	@property
	def globalinatcursessionsrate(self) :
		r"""Rate (/s) counter for globalinatcursessions.
		"""
		try :
			return self._globalinatcursessionsrate
		except Exception as e:
			raise e

	@property
	def inathitsrate(self) :
		r"""Rate (/s) counter for inattothits.
		"""
		try :
			return self._inathitsrate
		except Exception as e:
			raise e

	@property
	def inattotreceivebytes(self) :
		r"""INAT total Received Bytes.
		"""
		try :
			return self._inattotreceivebytes
		except Exception as e:
			raise e

	@property
	def inatcursessionsrate(self) :
		r"""Rate (/s) counter for inatcursessions.
		"""
		try :
			return self._inatcursessionsrate
		except Exception as e:
			raise e

	@property
	def globalinatreceivebytesrate(self) :
		r"""Rate (/s) counter for globalinatreceivebytes.
		"""
		try :
			return self._globalinatreceivebytesrate
		except Exception as e:
			raise e

	@property
	def globalinatpktsentrate(self) :
		r"""Rate (/s) counter for globalinatpktsent.
		"""
		try :
			return self._globalinatpktsentrate
		except Exception as e:
			raise e

	@property
	def inatcursessions(self) :
		r"""INAT current sessions.
		"""
		try :
			return self._inatcursessions
		except Exception as e:
			raise e

	@property
	def inatsentbytesrate(self) :
		r"""Rate (/s) counter for inattotsentbytes.
		"""
		try :
			return self._inatsentbytesrate
		except Exception as e:
			raise e

	@property
	def globalinattotsentbytes(self) :
		r"""Total INAT Sent Bytes.
		"""
		try :
			return self._globalinattotsentbytes
		except Exception as e:
			raise e

	@property
	def globalinathits(self) :
		r"""Total INAT Session hits.
		"""
		try :
			return self._globalinathits
		except Exception as e:
			raise e

	@property
	def globalinathitsrate(self) :
		r"""Rate (/s) counter for globalinathits.
		"""
		try :
			return self._globalinathitsrate
		except Exception as e:
			raise e

	@property
	def inatpktsentrate(self) :
		r"""Rate (/s) counter for inattotpktsent.
		"""
		try :
			return self._inatpktsentrate
		except Exception as e:
			raise e

	@property
	def globalinatpktreceived(self) :
		r"""Total INAT Packets Received.
		"""
		try :
			return self._globalinatpktreceived
		except Exception as e:
			raise e

	@property
	def globalinatpktreceivedrate(self) :
		r"""Rate (/s) counter for globalinatpktreceived.
		"""
		try :
			return self._globalinatpktreceivedrate
		except Exception as e:
			raise e

	@property
	def inattotpktreceived(self) :
		r"""INAT total Packets Received.
		"""
		try :
			return self._inattotpktreceived
		except Exception as e:
			raise e

	@property
	def inattothits(self) :
		r"""INAT total sessions.
		"""
		try :
			return self._inattothits
		except Exception as e:
			raise e

	@property
	def inattotpktsent(self) :
		r"""INAT total Packets Sent.
		"""
		try :
			return self._inattotpktsent
		except Exception as e:
			raise e

	@property
	def inatpktreceivedrate(self) :
		r"""Rate (/s) counter for inattotpktreceived.
		"""
		try :
			return self._inatpktreceivedrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(inatsession_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.inatsession
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
		r""" Use this API to fetch the statistics of all inatsession_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = inatsession_stats()
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

class inatsession_response(base_response) :
	def __init__(self, length=1) :
		self.inatsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.inatsession = [inatsession_stats() for _ in range(length)]

