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

class nsratecontrol(base_resource) :
	""" Configuration for rate control resource. """
	def __init__(self) :
		self._tcpthreshold = None
		self._udpthreshold = None
		self._icmpthreshold = None
		self._tcprstthreshold = None

	@property
	def tcpthreshold(self) :
		r"""Number of SYNs permitted per 10 milliseconds.
		"""
		try :
			return self._tcpthreshold
		except Exception as e:
			raise e

	@tcpthreshold.setter
	def tcpthreshold(self, tcpthreshold) :
		r"""Number of SYNs permitted per 10 milliseconds.
		"""
		try :
			self._tcpthreshold = tcpthreshold
		except Exception as e:
			raise e

	@property
	def udpthreshold(self) :
		r"""Number of UDP packets permitted per 10 milliseconds.
		"""
		try :
			return self._udpthreshold
		except Exception as e:
			raise e

	@udpthreshold.setter
	def udpthreshold(self, udpthreshold) :
		r"""Number of UDP packets permitted per 10 milliseconds.
		"""
		try :
			self._udpthreshold = udpthreshold
		except Exception as e:
			raise e

	@property
	def icmpthreshold(self) :
		r"""Number of ICMP packets permitted per 10 milliseconds.<br/>Default value: 100.
		"""
		try :
			return self._icmpthreshold
		except Exception as e:
			raise e

	@icmpthreshold.setter
	def icmpthreshold(self, icmpthreshold) :
		r"""Number of ICMP packets permitted per 10 milliseconds.<br/>Default value: 100
		"""
		try :
			self._icmpthreshold = icmpthreshold
		except Exception as e:
			raise e

	@property
	def tcprstthreshold(self) :
		r"""The number of TCP RST packets permitted per 10 milli second. zero means rate control is disabled and 0xffffffff means every thing is rate controlled.<br/>Default value: 100.
		"""
		try :
			return self._tcprstthreshold
		except Exception as e:
			raise e

	@tcprstthreshold.setter
	def tcprstthreshold(self, tcprstthreshold) :
		r"""The number of TCP RST packets permitted per 10 milli second. zero means rate control is disabled and 0xffffffff means every thing is rate controlled.<br/>Default value: 100
		"""
		try :
			self._tcprstthreshold = tcprstthreshold
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsratecontrol_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsratecontrol
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
	def update(cls, client, resource) :
		r""" Use this API to update nsratecontrol.
		"""
		try :
			if type(resource) is not list :
				updateresource = nsratecontrol()
				updateresource.tcpthreshold = resource.tcpthreshold
				updateresource.udpthreshold = resource.udpthreshold
				updateresource.icmpthreshold = resource.icmpthreshold
				updateresource.tcprstthreshold = resource.tcprstthreshold
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsratecontrol resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsratecontrol()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsratecontrol resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsratecontrol()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nsratecontrol_response(base_response) :
	def __init__(self, length=1) :
		self.nsratecontrol = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsratecontrol = [nsratecontrol() for _ in range(length)]

