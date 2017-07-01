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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class install(base_resource) :
	def __init__(self) :
		self._url = None
		self._y = None
		self._l = None
		self._enhancedupgrade = None
		self._resizeswapvar = None

	@property
	def url(self) :
		r"""Url for the build file. Must be in the following formats:
		http://[user]:[password]@host/path/to/file
		https://[user]:[password]@host/path/to/file
		sftp://[user]:[password]@host/path/to/file
		scp://[user]:[password]@host/path/to/file
		ftp://[user]:[password]@host/path/to/file
		file://path/to/file.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""Url for the build file. Must be in the following formats:
		http://[user]:[password]@host/path/to/file
		https://[user]:[password]@host/path/to/file
		sftp://[user]:[password]@host/path/to/file
		scp://[user]:[password]@host/path/to/file
		ftp://[user]:[password]@host/path/to/file
		file://path/to/file.
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def y(self) :
		r"""Do not prompt for yes/no before rebooting.
		"""
		try :
			return self._y
		except Exception as e:
			raise e

	@y.setter
	def y(self, y) :
		r"""Do not prompt for yes/no before rebooting.
		"""
		try :
			self._y = y
		except Exception as e:
			raise e

	@property
	def l(self) :
		r"""Use this flag to enable callhome.
		"""
		try :
			return self._l
		except Exception as e:
			raise e

	@l.setter
	def l(self, l) :
		r"""Use this flag to enable callhome.
		"""
		try :
			self._l = l
		except Exception as e:
			raise e

	@property
	def enhancedupgrade(self) :
		r"""Use this flag for upgrading from/to enhancement mode.
		"""
		try :
			return self._enhancedupgrade
		except Exception as e:
			raise e

	@enhancedupgrade.setter
	def enhancedupgrade(self, enhancedupgrade) :
		r"""Use this flag for upgrading from/to enhancement mode.
		"""
		try :
			self._enhancedupgrade = enhancedupgrade
		except Exception as e:
			raise e

	@property
	def resizeswapvar(self) :
		r"""Use this flag to change swap size on ONLY 64bit nCore/MCNS/VMPE systems NON-VPX systems.
		"""
		try :
			return self._resizeswapvar
		except Exception as e:
			raise e

	@resizeswapvar.setter
	def resizeswapvar(self, resizeswapvar) :
		r"""Use this flag to change swap size on ONLY 64bit nCore/MCNS/VMPE systems NON-VPX systems.
		"""
		try :
			self._resizeswapvar = resizeswapvar
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(install_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.install
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def Install(cls, client, resource) :
		r""" Use this API to Install install.
		"""
		try :
			if type(resource) is not list :
				Installresource = install()
				Installresource.url = resource.url
				Installresource.y = resource.y
				Installresource.l = resource.l
				Installresource.enhancedupgrade = resource.enhancedupgrade
				Installresource.resizeswapvar = resource.resizeswapvar
				return Installresource.perform_operation(client)
		except Exception as e :
			raise e

class install_response(base_response) :
	def __init__(self, length=1) :
		self.install = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.install = [install() for _ in range(length)]

