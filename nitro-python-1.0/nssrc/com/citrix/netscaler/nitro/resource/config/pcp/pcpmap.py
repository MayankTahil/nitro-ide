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

class pcpmap(base_resource) :
	""" Configuration for server resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._pcpsrcip = None
		self._pcpsrcport = None
		self._pcpdstip = None
		self._pcpdstport = None
		self._pcpnatip = None
		self._pcpnatport = None
		self._pcpprotocol = None
		self._pcpaddr = None
		self._pcpnounce = None
		self._pcprefcnt = None
		self._pcpnattype = None
		self._pcplifetime = None
		self.___count = 0

	@property
	def pcpsrcip(self) :
		r"""Internal IP address.
		"""
		try :
			return self._pcpsrcip
		except Exception as e:
			raise e

	@property
	def pcpsrcport(self) :
		r"""Internal Port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._pcpsrcport
		except Exception as e:
			raise e

	@property
	def pcpdstip(self) :
		r"""Remote PEER IP address.
		"""
		try :
			return self._pcpdstip
		except Exception as e:
			raise e

	@property
	def pcpdstport(self) :
		r"""Remote PEER Port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._pcpdstport
		except Exception as e:
			raise e

	@property
	def pcpnatip(self) :
		r"""External IP address.
		"""
		try :
			return self._pcpnatip
		except Exception as e:
			raise e

	@property
	def pcpnatport(self) :
		r"""External Port Number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._pcpnatport
		except Exception as e:
			raise e

	@property
	def pcpprotocol(self) :
		r"""Protocol of the PCP mapping.<br/>Possible values = HopOpt, icmp, igmp, ggp, ipv4, st, tcp, udp.
		"""
		try :
			return self._pcpprotocol
		except Exception as e:
			raise e

	@property
	def pcpaddr(self) :
		r"""Address of PCP Map entity.
		"""
		try :
			return self._pcpaddr
		except Exception as e:
			raise e

	@property
	def pcpnounce(self) :
		r"""PCP Mapping Nounce.
		"""
		try :
			return self._pcpnounce
		except Exception as e:
			raise e

	@property
	def pcprefcnt(self) :
		r"""Refcount, which indicates how many session is active.
		"""
		try :
			return self._pcprefcnt
		except Exception as e:
			raise e

	@property
	def pcpnattype(self) :
		r"""Type of sessions to be displayed.<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite, NAT64.
		"""
		try :
			return self._pcpnattype
		except Exception as e:
			raise e

	@property
	def pcplifetime(self) :
		r"""Integer value that shows the requested lifetime.
		"""
		try :
			return self._pcplifetime
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(pcpmap_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.pcpmap
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the pcpmap resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = pcpmap()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of pcpmap resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = pcpmap()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the pcpmap resources configured on NetScaler.
		"""
		try :
			obj = pcpmap()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of pcpmap resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = pcpmap()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Pcpprotocol:
		HopOpt = "HopOpt"
		icmp = "icmp"
		igmp = "igmp"
		ggp = "ggp"
		ipv4 = "ipv4"
		st = "st"
		tcp = "tcp"
		udp = "udp"

	class Pcpnattype:
		NAT44 = "NAT44"
		DS_Lite = "DS-Lite"
		NAT64 = "NAT64"

class pcpmap_response(base_response) :
	def __init__(self, length=1) :
		self.pcpmap = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.pcpmap = [pcpmap() for _ in range(length)]

