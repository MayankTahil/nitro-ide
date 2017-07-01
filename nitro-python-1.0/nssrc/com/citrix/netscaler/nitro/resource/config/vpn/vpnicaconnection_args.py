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


class vpnicaconnection_args :
	r""" Provides additional arguments required for fetching the vpnicaconnection resource.
	"""
	def __init__(self) :
		self._username = None
		self._transproto = None
		self._nodeid = None

	@property
	def username(self) :
		r"""User name for which to display connections.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""User name for which to display connections.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def transproto(self) :
		r"""Transport type for the existing Existing ICA conenction.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._transproto
		except Exception as e:
			raise e

	@transproto.setter
	def transproto(self, transproto) :
		r"""Transport type for the existing Existing ICA conenction.<br/>Possible values = TCP, UDP
		"""
		try :
			self._transproto = transproto
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

	class Transproto:
		TCP = "TCP"
		UDP = "UDP"

