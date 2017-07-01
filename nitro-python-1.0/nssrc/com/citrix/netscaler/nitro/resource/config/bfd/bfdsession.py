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

class bfdsession(base_resource) :
	""" Configuration for BFD configuration resource. """
	def __init__(self) :
		self._localip = None
		self._remoteip = None
		self._state = None
		self._localport = None
		self._remoteport = None
		self._minimumtransmitinterval = None
		self._negotiatedminimumtransmitinterval = None
		self._minimumreceiveinterval = None
		self._negotiatedminimumreceiveinterval = None
		self._multiplier = None
		self._remotemultiplier = None
		self._vlan = None
		self._localdiagnotic = None
		self._localdiscriminator = None
		self._remotediscriminator = None
		self._passive = None
		self._multihop = None
		self._admindown = None
		self._originalownerpe = None
		self._currentownerpe = None
		self._ownernode = None
		self.___count = 0

	@property
	def localip(self) :
		r"""IPV4 or IPV6 Address of Local Node.
		"""
		try :
			return self._localip
		except Exception as e:
			raise e

	@localip.setter
	def localip(self, localip) :
		r"""IPV4 or IPV6 Address of Local Node.
		"""
		try :
			self._localip = localip
		except Exception as e:
			raise e

	@property
	def remoteip(self) :
		r"""IPV4 or IPV6 Address of Remote Node.
		"""
		try :
			return self._remoteip
		except Exception as e:
			raise e

	@remoteip.setter
	def remoteip(self, remoteip) :
		r"""IPV4 or IPV6 Address of Remote Node.
		"""
		try :
			self._remoteip = remoteip
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current state of the BFD session.<br/>Possible values = ADMIN DOWN, DOWN, INIT, UP.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def localport(self) :
		r"""Source Port used by Local node to send Control packets for the BFD session.
		"""
		try :
			return self._localport
		except Exception as e:
			raise e

	@property
	def remoteport(self) :
		r"""Source Port used by Remote node to send Control packets for the BFD session.
		"""
		try :
			return self._remoteport
		except Exception as e:
			raise e

	@property
	def minimumtransmitinterval(self) :
		r"""Minimum trasmit interval, in milliseconds, the local node would like to use when transmitting BFD Control packets.
		"""
		try :
			return self._minimumtransmitinterval
		except Exception as e:
			raise e

	@property
	def negotiatedminimumtransmitinterval(self) :
		r"""Negotiated Minimum Transmit Interval. This is the interval at which the local node will be sending out BFD control packets.
		"""
		try :
			return self._negotiatedminimumtransmitinterval
		except Exception as e:
			raise e

	@property
	def minimumreceiveinterval(self) :
		r"""Minimum receive interval, in milliseconds, between received BFD Control packets that the local node is capable of supporting.
		"""
		try :
			return self._minimumreceiveinterval
		except Exception as e:
			raise e

	@property
	def negotiatedminimumreceiveinterval(self) :
		r"""Negotiated Minimum Receive Interval. This is the interval at which the local node will be expecting BFD control packets.
		"""
		try :
			return self._negotiatedminimumreceiveinterval
		except Exception as e:
			raise e

	@property
	def multiplier(self) :
		r"""Detection Multiplier. The negotiated transmit interval multiplied by Detection multiplier provides the Detection Time for the remote node for the BFD session.
		"""
		try :
			return self._multiplier
		except Exception as e:
			raise e

	@property
	def remotemultiplier(self) :
		r"""Your Multiplier. The negotiated receive interval multiplied by Your Multiplier provides the Detection Time for the local node for the BFD session.
		"""
		try :
			return self._remotemultiplier
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""VLAN ID on which the BDS session is configured.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@property
	def localdiagnotic(self) :
		r"""Diagnostic Code specifying the local system's reason for the last change in session state.
		"""
		try :
			return self._localdiagnotic
		except Exception as e:
			raise e

	@property
	def localdiscriminator(self) :
		r"""A unique discriminator value generated by the local node for the session.
		"""
		try :
			return self._localdiscriminator
		except Exception as e:
			raise e

	@property
	def remotediscriminator(self) :
		r"""A unique discriminator value as received from the remote node for the session.
		"""
		try :
			return self._remotediscriminator
		except Exception as e:
			raise e

	@property
	def passive(self) :
		r"""Flag indicating that the session is passive.
		"""
		try :
			return self._passive
		except Exception as e:
			raise e

	@property
	def multihop(self) :
		r"""Flag indicating if the session is multihop.
		"""
		try :
			return self._multihop
		except Exception as e:
			raise e

	@property
	def admindown(self) :
		r"""Flag indicating if admin down is being sent.
		"""
		try :
			return self._admindown
		except Exception as e:
			raise e

	@property
	def originalownerpe(self) :
		r"""Original Owner PE of the BFD session.
		"""
		try :
			return self._originalownerpe
		except Exception as e:
			raise e

	@property
	def currentownerpe(self) :
		r"""Current Owner PE of the BFD session.
		"""
		try :
			return self._currentownerpe
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""The owner node in a Cluster for this BFD session. Owner node can vary from 0 to 31. If ownernode is not specified then the session is treated as Striped session.<br/>Default value: 255.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bfdsession_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bfdsession
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
		r""" Use this API to fetch all the bfdsession resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = bfdsession()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the bfdsession resources that are configured on netscaler.
	# This uses bfdsession_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = bfdsession()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of bfdsession resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bfdsession()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the bfdsession resources configured on NetScaler.
		"""
		try :
			obj = bfdsession()
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
		r""" Use this API to count filtered the set of bfdsession resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = bfdsession()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		ADMIN_DOWN = "ADMIN DOWN"
		DOWN = "DOWN"
		INIT = "INIT"
		UP = "UP"

class bfdsession_response(base_response) :
	def __init__(self, length=1) :
		self.bfdsession = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bfdsession = [bfdsession() for _ in range(length)]

