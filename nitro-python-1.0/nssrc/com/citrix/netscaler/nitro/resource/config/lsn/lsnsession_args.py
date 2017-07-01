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


class lsnsession_args :
	r""" Provides additional arguments required for fetching the lsnsession resource.
	"""
	def __init__(self) :
		self._nattype = None
		self._clientname = None
		self._network = None
		self._netmask = None
		self._network6 = None
		self._td = None
		self._natip = None

	@property
	def nattype(self) :
		r"""Type of sessions to be displayed.<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite, NAT64.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		r"""Type of sessions to be displayed.<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite, NAT64
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	@property
	def clientname(self) :
		r"""Name of the LSN Client entity.
		"""
		try :
			return self._clientname
		except Exception as e:
			raise e

	@clientname.setter
	def clientname(self, clientname) :
		r"""Name of the LSN Client entity.
		"""
		try :
			self._clientname = clientname
		except Exception as e:
			raise e

	@property
	def network(self) :
		r"""IP address or network address of subscriber(s).
		"""
		try :
			return self._network
		except Exception as e:
			raise e

	@network.setter
	def network(self, network) :
		r"""IP address or network address of subscriber(s).
		"""
		try :
			self._network = network
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Subnet mask for the IP address specified by the network parameter.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Subnet mask for the IP address specified by the network parameter.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def network6(self) :
		r"""IPv6 address of the LSN subscriber or B4 device.
		"""
		try :
			return self._network6
		except Exception as e:
			raise e

	@network6.setter
	def network6(self, network6) :
		r"""IPv6 address of the LSN subscriber or B4 device.
		"""
		try :
			self._network6 = network6
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Traffic domain ID of the LSN client entity.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Traffic domain ID of the LSN client entity.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def natip(self) :
		r"""Mapped NAT IP address used in LSN sessions.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		r"""Mapped NAT IP address used in LSN sessions.
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

	class Nattype:
		NAT44 = "NAT44"
		DS_Lite = "DS-Lite"
		NAT64 = "NAT64"

