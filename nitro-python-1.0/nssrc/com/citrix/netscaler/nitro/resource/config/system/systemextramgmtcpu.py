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

class systemextramgmtcpu(base_resource) :

		#------- Read only Parameter ---------

	def __init__(self) :
		self._configuredstate = None
		self._effectivestate = None

	@property
	def configuredstate(self) :
		r"""Get the configured state of extra manahement cpu.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._configuredstate
		except Exception as e:
			raise e

	@property
	def effectivestate(self) :
		r"""Get the current running state of extra management cpu.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._effectivestate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemextramgmtcpu_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemextramgmtcpu
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
	def enable(cls, client, resource="") :
		r""" Use this API to enable systemextramgmtcpu.
		"""
		try :
			if type(resource) is not list :
				enableresource = systemextramgmtcpu()
				return enableresource.perform_operation(client,"enable")
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource="") :
		r""" Use this API to disable systemextramgmtcpu.
		"""
		try :
			if type(resource) is not list :
				disableresource = systemextramgmtcpu()
				return disableresource.perform_operation(client,"disable")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the systemextramgmtcpu resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemextramgmtcpu()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Effectivestate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Configuredstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class systemextramgmtcpu_response(base_response) :
	def __init__(self, length=1) :
		self.systemextramgmtcpu = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemextramgmtcpu = [systemextramgmtcpu() for _ in range(length)]

