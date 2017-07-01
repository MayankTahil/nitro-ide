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


class bfdsession_args :
	r""" Provides additional arguments required for fetching the bfdsession resource.
	"""
	def __init__(self) :
		self._localip = None
		self._remoteip = None

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

