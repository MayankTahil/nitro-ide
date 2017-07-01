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


class vpnstoreinfo_args :
	r""" Provides additional arguments required for fetching the vpnstoreinfo resource.
	"""
	def __init__(self) :
		self._url = None

	@property
	def url(self) :
		r"""StoreFront URL to be scanned.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""StoreFront URL to be scanned.
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

