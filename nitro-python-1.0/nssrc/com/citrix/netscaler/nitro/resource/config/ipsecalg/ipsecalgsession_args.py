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


class ipsecalgsession_args :
	r""" Provides additional arguments required for fetching the ipsecalgsession resource.
	"""
	def __init__(self) :
		self._sourceip_alg = None
		self._natip_alg = None
		self._destip_alg = None

	@property
	def sourceip_alg(self) :
		r"""Original Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._sourceip_alg
		except Exception as e:
			raise e

	@sourceip_alg.setter
	def sourceip_alg(self, sourceip_alg) :
		r"""Original Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._sourceip_alg = sourceip_alg
		except Exception as e:
			raise e

	@property
	def natip_alg(self) :
		r"""Natted Source IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._natip_alg
		except Exception as e:
			raise e

	@natip_alg.setter
	def natip_alg(self, natip_alg) :
		r"""Natted Source IP address.<br/>Minimum length =  1
		"""
		try :
			self._natip_alg = natip_alg
		except Exception as e:
			raise e

	@property
	def destip_alg(self) :
		r"""Destination IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._destip_alg
		except Exception as e:
			raise e

	@destip_alg.setter
	def destip_alg(self, destip_alg) :
		r"""Destination IP address.<br/>Minimum length =  1
		"""
		try :
			self._destip_alg = destip_alg
		except Exception as e:
			raise e

