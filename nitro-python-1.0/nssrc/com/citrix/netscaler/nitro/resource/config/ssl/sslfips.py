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

class sslfips(base_resource) :
	""" Configuration for fips resource. """
	def __init__(self) :
		self._inithsm = None
		self._sopassword = None
		self._oldsopassword = None
		self._userpassword = None
		self._hsmlabel = None
		self._fipsfw = None
		self._erasedata = None
		self._serial = None
		self._majorversion = None
		self._minorversion = None
		self._fipshwmajorversion = None
		self._fipshwminorversion = None
		self._fipshwversionstring = None
		self._flashmemorytotal = None
		self._flashmemoryfree = None
		self._sramtotal = None
		self._sramfree = None
		self._status = None
		self._flag = None
		self._serialno = None
		self._model = None
		self._state = None
		self._firmwarereleasedate = None
		self._coresmax = None
		self._coresenabled = None

	@property
	def inithsm(self) :
		r"""FIPS initialization level. The appliance currently supports Level-2 (FIPS 140-2).<br/>Possible values = Level-2.
		"""
		try :
			return self._inithsm
		except Exception as e:
			raise e

	@inithsm.setter
	def inithsm(self, inithsm) :
		r"""FIPS initialization level. The appliance currently supports Level-2 (FIPS 140-2).<br/>Possible values = Level-2
		"""
		try :
			self._inithsm = inithsm
		except Exception as e:
			raise e

	@property
	def sopassword(self) :
		r"""Security officer password that will be in effect after you have configured the HSM.<br/>Minimum length =  1.
		"""
		try :
			return self._sopassword
		except Exception as e:
			raise e

	@sopassword.setter
	def sopassword(self, sopassword) :
		r"""Security officer password that will be in effect after you have configured the HSM.<br/>Minimum length =  1
		"""
		try :
			self._sopassword = sopassword
		except Exception as e:
			raise e

	@property
	def oldsopassword(self) :
		r"""Old password for the security officer.<br/>Minimum length =  1.
		"""
		try :
			return self._oldsopassword
		except Exception as e:
			raise e

	@oldsopassword.setter
	def oldsopassword(self, oldsopassword) :
		r"""Old password for the security officer.<br/>Minimum length =  1
		"""
		try :
			self._oldsopassword = oldsopassword
		except Exception as e:
			raise e

	@property
	def userpassword(self) :
		r"""The Hardware Security Module's (HSM) User password.<br/>Minimum length =  1.
		"""
		try :
			return self._userpassword
		except Exception as e:
			raise e

	@userpassword.setter
	def userpassword(self, userpassword) :
		r"""The Hardware Security Module's (HSM) User password.<br/>Minimum length =  1
		"""
		try :
			self._userpassword = userpassword
		except Exception as e:
			raise e

	@property
	def hsmlabel(self) :
		r"""Label to identify the Hardware Security Module (HSM).<br/>Minimum length =  1.
		"""
		try :
			return self._hsmlabel
		except Exception as e:
			raise e

	@hsmlabel.setter
	def hsmlabel(self, hsmlabel) :
		r"""Label to identify the Hardware Security Module (HSM).<br/>Minimum length =  1
		"""
		try :
			self._hsmlabel = hsmlabel
		except Exception as e:
			raise e

	@property
	def fipsfw(self) :
		r"""Path to the FIPS firmware file.<br/>Minimum length =  1.
		"""
		try :
			return self._fipsfw
		except Exception as e:
			raise e

	@fipsfw.setter
	def fipsfw(self, fipsfw) :
		r"""Path to the FIPS firmware file.<br/>Minimum length =  1
		"""
		try :
			self._fipsfw = fipsfw
		except Exception as e:
			raise e

	@property
	def erasedata(self) :
		r"""Erase data.<br/>Default value: FIPS_ERASE<br/>Minimum length =  1.
		"""
		try :
			return self._erasedata
		except Exception as e:
			raise e

	@property
	def serial(self) :
		r"""FIPS card serial number.
		"""
		try :
			return self._serial
		except Exception as e:
			raise e

	@property
	def majorversion(self) :
		r"""Firmware major version.
		"""
		try :
			return self._majorversion
		except Exception as e:
			raise e

	@property
	def minorversion(self) :
		r"""Firmware minor version.
		"""
		try :
			return self._minorversion
		except Exception as e:
			raise e

	@property
	def fipshwmajorversion(self) :
		r"""FIPS card hardware major version.
		"""
		try :
			return self._fipshwmajorversion
		except Exception as e:
			raise e

	@property
	def fipshwminorversion(self) :
		r"""FIPS card hardware minor version.
		"""
		try :
			return self._fipshwminorversion
		except Exception as e:
			raise e

	@property
	def fipshwversionstring(self) :
		r"""FIPS card hardware extended version string.
		"""
		try :
			return self._fipshwversionstring
		except Exception as e:
			raise e

	@property
	def flashmemorytotal(self) :
		r"""Total size of the flash memory on card.
		"""
		try :
			return self._flashmemorytotal
		except Exception as e:
			raise e

	@property
	def flashmemoryfree(self) :
		r"""Total size of free flash memory.
		"""
		try :
			return self._flashmemoryfree
		except Exception as e:
			raise e

	@property
	def sramtotal(self) :
		r"""Total size of the SRAM memory on card.
		"""
		try :
			return self._sramtotal
		except Exception as e:
			raise e

	@property
	def sramfree(self) :
		r"""Total size of free SRAM memory.
		"""
		try :
			return self._sramfree
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Status.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def flag(self) :
		r"""Internal Flags.
		"""
		try :
			return self._flag
		except Exception as e:
			raise e

	@property
	def serialno(self) :
		r"""FIPS card serial number.
		"""
		try :
			return self._serialno
		except Exception as e:
			raise e

	@property
	def model(self) :
		r"""FIPS card model info.
		"""
		try :
			return self._model
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""FIPS card state.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def firmwarereleasedate(self) :
		r"""FIPS card firmware revision date.
		"""
		try :
			return self._firmwarereleasedate
		except Exception as e:
			raise e

	@property
	def coresmax(self) :
		r"""Maximum number of crypto cores present in the FIPS card.
		"""
		try :
			return self._coresmax
		except Exception as e:
			raise e

	@property
	def coresenabled(self) :
		r"""Number of crypto cores enabled in the FIPS card.
		"""
		try :
			return self._coresenabled
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslfips_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslfips
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
		r""" Use this API to update sslfips.
		"""
		try :
			if type(resource) is not list :
				updateresource = sslfips()
				updateresource.inithsm = resource.inithsm
				updateresource.sopassword = resource.sopassword
				updateresource.oldsopassword = resource.oldsopassword
				updateresource.userpassword = resource.userpassword
				updateresource.hsmlabel = resource.hsmlabel
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslfips resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslfips()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def reset(cls, client, resource) :
		r""" Use this API to reset sslfips.
		"""
		try :
			if type(resource) is not list :
				resetresource = sslfips()
				return resetresource.perform_operation(client,"reset")
		except Exception as e :
			raise e

	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change sslfips.
		"""
		try :
			if type(resource) is not list :
				changeresource = sslfips()
				changeresource.fipsfw = resource.fipsfw
				return changeresource.perform_operation(client,"update")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslfips resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslfips()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Inithsm:
		Level_2 = "Level-2"

class sslfips_response(base_response) :
	def __init__(self, length=1) :
		self.sslfips = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslfips = [sslfips() for _ in range(length)]

