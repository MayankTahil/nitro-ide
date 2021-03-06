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


class aaagroup_args :
	r""" Provides additional arguments required for fetching the aaagroup resource.
	"""
	def __init__(self) :
		self._loggedin = None
		self._weight = None

	@property
	def loggedin(self) :
		r"""Display only the group members who are currently logged in.
		"""
		try :
			return self._loggedin
		except Exception as e:
			raise e

	@loggedin.setter
	def loggedin(self, loggedin) :
		r"""Display only the group members who are currently logged in.
		"""
		try :
			self._loggedin = loggedin
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight of this group with respect to other configured aaa groups (lower the number higher the weight).<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  65535.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight of this group with respect to other configured aaa groups (lower the number higher the weight).<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  65535
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

