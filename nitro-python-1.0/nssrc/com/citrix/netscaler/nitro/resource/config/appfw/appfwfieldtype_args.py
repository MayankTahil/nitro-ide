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


class appfwfieldtype_args :
	r""" Provides additional arguments required for fetching the appfwfieldtype resource.
	"""
	def __init__(self) :
		self._nocharmaps = None

	@property
	def nocharmaps(self) :
		r"""will not show internal field types added as part of FieldFormat learn rules deployment.
		"""
		try :
			return self._nocharmaps
		except Exception as e:
			raise e

	@nocharmaps.setter
	def nocharmaps(self, nocharmaps) :
		r"""will not show internal field types added as part of FieldFormat learn rules deployment.
		"""
		try :
			self._nocharmaps = nocharmaps
		except Exception as e:
			raise e

