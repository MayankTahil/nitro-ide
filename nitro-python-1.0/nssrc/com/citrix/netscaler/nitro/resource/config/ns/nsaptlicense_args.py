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


class nsaptlicense_args :
	r""" Provides additional arguments required for fetching the nsaptlicense resource.
	"""
	def __init__(self) :
		self._serialno = None
		self._useproxy = None

	@property
	def serialno(self) :
		r"""Hardware Serial Number/License Activation Code(LAC).
		"""
		try :
			return self._serialno
		except Exception as e:
			raise e

	@serialno.setter
	def serialno(self, serialno) :
		r"""Hardware Serial Number/License Activation Code(LAC).
		"""
		try :
			self._serialno = serialno
		except Exception as e:
			raise e

	@property
	def useproxy(self) :
		r"""Specifies whether to use the licenseproxyserver to reach the internet. Make sure to configure licenseproxyserver to use this option.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._useproxy
		except Exception as e:
			raise e

	@useproxy.setter
	def useproxy(self, useproxy) :
		r"""Specifies whether to use the licenseproxyserver to reach the internet. Make sure to configure licenseproxyserver to use this option.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._useproxy = useproxy
		except Exception as e:
			raise e

	class Useproxy:
		YES = "YES"
		NO = "NO"

