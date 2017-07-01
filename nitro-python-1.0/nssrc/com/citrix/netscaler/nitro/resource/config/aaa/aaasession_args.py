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


class aaasession_args :
	r""" Provides additional arguments required for fetching the aaasession resource.
	"""
	def __init__(self) :
		self._username = None
		self._groupname = None
		self._iip = None
		self._netmask = None
		self._nodeid = None

	@property
	def username(self) :
		r"""Name of the AAA user.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""Name of the AAA user.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		r"""Name of the AAA group.<br/>Minimum length =  1.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		r"""Name of the AAA group.<br/>Minimum length =  1
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def iip(self) :
		r"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._iip
		except Exception as e:
			raise e

	@iip.setter
	def iip(self, iip) :
		r"""IP address or the first address in the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._iip = iip
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Subnet mask for the intranet IP range.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Subnet mask for the intranet IP range.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

