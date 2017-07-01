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


class service_args :
	r""" Provides additional arguments required for fetching the service resource.
	"""
	def __init__(self) :
		self._all = None
		self._Internal = None

	@property
	def all(self) :
		r"""Display both user-configured and dynamically learned services.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Display both user-configured and dynamically learned services.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def Internal(self) :
		r"""Display only dynamically learned services.
		"""
		try :
			return self._Internal
		except Exception as e:
			raise e

	@Internal.setter
	def Internal(self, Internal) :
		r"""Display only dynamically learned services.
		"""
		try :
			self._Internal = Internal
		except Exception as e:
			raise e

