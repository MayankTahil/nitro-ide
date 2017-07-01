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

class nslicenseserverpool(base_resource) :
	""" Configuration for licenseserver resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._instancetotal = None
		self._instanceavailable = None
		self._standardbandwidthtotal = None
		self._standardbandwidthavailable = None
		self._enterprisebandwidthtotal = None
		self._enterprisebandwidthavailable = None
		self._platinumbandwidthtotal = None
		self._platinumbandwidthavailable = None
		self._cpxinstancetotal = None
		self._cpxinstanceavailable = None
		self._vpx1stotal = None
		self._vpx1savailable = None
		self._vpx1ptotal = None
		self._vpx1pavailable = None
		self._vpx5stotal = None
		self._vpx5savailable = None
		self._vpx5ptotal = None
		self._vpx5pavailable = None
		self._vpx10stotal = None
		self._vpx10savailable = None
		self._vpx10etotal = None
		self._vpx10eavailable = None
		self._vpx10ptotal = None
		self._vpx10pavailable = None
		self._vpx25stotal = None
		self._vpx25savailable = None
		self._vpx25etotal = None
		self._vpx25eavailable = None
		self._vpx25ptotal = None
		self._vpx25pavailable = None
		self._vpx50stotal = None
		self._vpx50savailable = None
		self._vpx50etotal = None
		self._vpx50eavailable = None
		self._vpx50ptotal = None
		self._vpx50pavailable = None
		self._vpx100stotal = None
		self._vpx100savailable = None
		self._vpx100etotal = None
		self._vpx100eavailable = None
		self._vpx100ptotal = None
		self._vpx100pavailable = None
		self._vpx200stotal = None
		self._vpx200savailable = None
		self._vpx200etotal = None
		self._vpx200eavailable = None
		self._vpx200ptotal = None
		self._vpx200pavailable = None
		self._vpx500stotal = None
		self._vpx500savailable = None
		self._vpx500etotal = None
		self._vpx500eavailable = None
		self._vpx500ptotal = None
		self._vpx500pavailable = None
		self._vpx1000stotal = None
		self._vpx1000savailable = None
		self._vpx1000etotal = None
		self._vpx1000eavailable = None
		self._vpx1000ptotal = None
		self._vpx1000pavailable = None
		self._vpx2000ptotal = None
		self._vpx2000pavailable = None
		self._vpx3000stotal = None
		self._vpx3000savailable = None
		self._vpx3000etotal = None
		self._vpx3000eavailable = None
		self._vpx3000ptotal = None
		self._vpx3000pavailable = None
		self._vpx4000ptotal = None
		self._vpx4000pavailable = None
		self._vpx5000stotal = None
		self._vpx5000savailable = None
		self._vpx5000etotal = None
		self._vpx5000eavailable = None
		self._vpx5000ptotal = None
		self._vpx5000pavailable = None
		self._vpx8000stotal = None
		self._vpx8000savailable = None
		self._vpx8000etotal = None
		self._vpx8000eavailable = None
		self._vpx8000ptotal = None
		self._vpx8000pavailable = None

	@property
	def instancetotal(self) :
		r"""Instance Total.
		"""
		try :
			return self._instancetotal
		except Exception as e:
			raise e

	@property
	def instanceavailable(self) :
		r"""Instance Available.
		"""
		try :
			return self._instanceavailable
		except Exception as e:
			raise e

	@property
	def standardbandwidthtotal(self) :
		r"""Standard Bandwidth Total.
		"""
		try :
			return self._standardbandwidthtotal
		except Exception as e:
			raise e

	@property
	def standardbandwidthavailable(self) :
		r"""Standard Bandwidth Available.
		"""
		try :
			return self._standardbandwidthavailable
		except Exception as e:
			raise e

	@property
	def enterprisebandwidthtotal(self) :
		r"""Enterprise Bandwidth Total.
		"""
		try :
			return self._enterprisebandwidthtotal
		except Exception as e:
			raise e

	@property
	def enterprisebandwidthavailable(self) :
		r"""Enterprise Bandwidth Available.
		"""
		try :
			return self._enterprisebandwidthavailable
		except Exception as e:
			raise e

	@property
	def platinumbandwidthtotal(self) :
		r"""Platinum Bandwidth Total.
		"""
		try :
			return self._platinumbandwidthtotal
		except Exception as e:
			raise e

	@property
	def platinumbandwidthavailable(self) :
		r"""Platinum Bandwidth Available.
		"""
		try :
			return self._platinumbandwidthavailable
		except Exception as e:
			raise e

	@property
	def cpxinstancetotal(self) :
		r"""CP1000 Instance Total.
		"""
		try :
			return self._cpxinstancetotal
		except Exception as e:
			raise e

	@property
	def cpxinstanceavailable(self) :
		r"""CP1000 Instance Available.
		"""
		try :
			return self._cpxinstanceavailable
		except Exception as e:
			raise e

	@property
	def vpx1stotal(self) :
		r"""VPX1S Total.
		"""
		try :
			return self._vpx1stotal
		except Exception as e:
			raise e

	@property
	def vpx1savailable(self) :
		r"""VPX1S Available.
		"""
		try :
			return self._vpx1savailable
		except Exception as e:
			raise e

	@property
	def vpx1ptotal(self) :
		r"""VPX1P Total.
		"""
		try :
			return self._vpx1ptotal
		except Exception as e:
			raise e

	@property
	def vpx1pavailable(self) :
		r"""VPX1P Available.
		"""
		try :
			return self._vpx1pavailable
		except Exception as e:
			raise e

	@property
	def vpx5stotal(self) :
		r"""VPX5S Total.
		"""
		try :
			return self._vpx5stotal
		except Exception as e:
			raise e

	@property
	def vpx5savailable(self) :
		r"""VPX5S Available.
		"""
		try :
			return self._vpx5savailable
		except Exception as e:
			raise e

	@property
	def vpx5ptotal(self) :
		r"""VPX5P Total.
		"""
		try :
			return self._vpx5ptotal
		except Exception as e:
			raise e

	@property
	def vpx5pavailable(self) :
		r"""VPX5P Available.
		"""
		try :
			return self._vpx5pavailable
		except Exception as e:
			raise e

	@property
	def vpx10stotal(self) :
		r"""VPX10S Total.
		"""
		try :
			return self._vpx10stotal
		except Exception as e:
			raise e

	@property
	def vpx10savailable(self) :
		r"""VPX10S Available.
		"""
		try :
			return self._vpx10savailable
		except Exception as e:
			raise e

	@property
	def vpx10etotal(self) :
		r"""VPX10E Total.
		"""
		try :
			return self._vpx10etotal
		except Exception as e:
			raise e

	@property
	def vpx10eavailable(self) :
		r"""VPX10E Available.
		"""
		try :
			return self._vpx10eavailable
		except Exception as e:
			raise e

	@property
	def vpx10ptotal(self) :
		r"""VPX10P Total.
		"""
		try :
			return self._vpx10ptotal
		except Exception as e:
			raise e

	@property
	def vpx10pavailable(self) :
		r"""VPX10P Available.
		"""
		try :
			return self._vpx10pavailable
		except Exception as e:
			raise e

	@property
	def vpx25stotal(self) :
		r"""VPX25S Total.
		"""
		try :
			return self._vpx25stotal
		except Exception as e:
			raise e

	@property
	def vpx25savailable(self) :
		r"""VPX25S Available.
		"""
		try :
			return self._vpx25savailable
		except Exception as e:
			raise e

	@property
	def vpx25etotal(self) :
		r"""VPX25E Total.
		"""
		try :
			return self._vpx25etotal
		except Exception as e:
			raise e

	@property
	def vpx25eavailable(self) :
		r"""VPX25E Available.
		"""
		try :
			return self._vpx25eavailable
		except Exception as e:
			raise e

	@property
	def vpx25ptotal(self) :
		r"""VPX25P Total.
		"""
		try :
			return self._vpx25ptotal
		except Exception as e:
			raise e

	@property
	def vpx25pavailable(self) :
		r"""VPX25P Available.
		"""
		try :
			return self._vpx25pavailable
		except Exception as e:
			raise e

	@property
	def vpx50stotal(self) :
		r"""VPX50S Total.
		"""
		try :
			return self._vpx50stotal
		except Exception as e:
			raise e

	@property
	def vpx50savailable(self) :
		r"""VPX50S Available.
		"""
		try :
			return self._vpx50savailable
		except Exception as e:
			raise e

	@property
	def vpx50etotal(self) :
		r"""VPX50E Total.
		"""
		try :
			return self._vpx50etotal
		except Exception as e:
			raise e

	@property
	def vpx50eavailable(self) :
		r"""VPX50E Available.
		"""
		try :
			return self._vpx50eavailable
		except Exception as e:
			raise e

	@property
	def vpx50ptotal(self) :
		r"""VPX50P Total.
		"""
		try :
			return self._vpx50ptotal
		except Exception as e:
			raise e

	@property
	def vpx50pavailable(self) :
		r"""VPX50P Available.
		"""
		try :
			return self._vpx50pavailable
		except Exception as e:
			raise e

	@property
	def vpx100stotal(self) :
		r"""VPX100S Total.
		"""
		try :
			return self._vpx100stotal
		except Exception as e:
			raise e

	@property
	def vpx100savailable(self) :
		r"""VPX100S Available.
		"""
		try :
			return self._vpx100savailable
		except Exception as e:
			raise e

	@property
	def vpx100etotal(self) :
		r"""VPX100E Total.
		"""
		try :
			return self._vpx100etotal
		except Exception as e:
			raise e

	@property
	def vpx100eavailable(self) :
		r"""VPX100E Available.
		"""
		try :
			return self._vpx100eavailable
		except Exception as e:
			raise e

	@property
	def vpx100ptotal(self) :
		r"""VPX100P Total.
		"""
		try :
			return self._vpx100ptotal
		except Exception as e:
			raise e

	@property
	def vpx100pavailable(self) :
		r"""VPX100P Available.
		"""
		try :
			return self._vpx100pavailable
		except Exception as e:
			raise e

	@property
	def vpx200stotal(self) :
		r"""VPX200S Total.
		"""
		try :
			return self._vpx200stotal
		except Exception as e:
			raise e

	@property
	def vpx200savailable(self) :
		r"""VPX200S Available.
		"""
		try :
			return self._vpx200savailable
		except Exception as e:
			raise e

	@property
	def vpx200etotal(self) :
		r"""VPX200E Total.
		"""
		try :
			return self._vpx200etotal
		except Exception as e:
			raise e

	@property
	def vpx200eavailable(self) :
		r"""VPX200E Available.
		"""
		try :
			return self._vpx200eavailable
		except Exception as e:
			raise e

	@property
	def vpx200ptotal(self) :
		r"""VPX200P Total.
		"""
		try :
			return self._vpx200ptotal
		except Exception as e:
			raise e

	@property
	def vpx200pavailable(self) :
		r"""VPX200P Available.
		"""
		try :
			return self._vpx200pavailable
		except Exception as e:
			raise e

	@property
	def vpx500stotal(self) :
		r"""VPX500S Total.
		"""
		try :
			return self._vpx500stotal
		except Exception as e:
			raise e

	@property
	def vpx500savailable(self) :
		r"""VPX500S Available.
		"""
		try :
			return self._vpx500savailable
		except Exception as e:
			raise e

	@property
	def vpx500etotal(self) :
		r"""VPX500E Total.
		"""
		try :
			return self._vpx500etotal
		except Exception as e:
			raise e

	@property
	def vpx500eavailable(self) :
		r"""VPX500E Available.
		"""
		try :
			return self._vpx500eavailable
		except Exception as e:
			raise e

	@property
	def vpx500ptotal(self) :
		r"""VPX500P Total.
		"""
		try :
			return self._vpx500ptotal
		except Exception as e:
			raise e

	@property
	def vpx500pavailable(self) :
		r"""VPX500P Available.
		"""
		try :
			return self._vpx500pavailable
		except Exception as e:
			raise e

	@property
	def vpx1000stotal(self) :
		r"""VPX1000S Total.
		"""
		try :
			return self._vpx1000stotal
		except Exception as e:
			raise e

	@property
	def vpx1000savailable(self) :
		r"""VPX1000S Available.
		"""
		try :
			return self._vpx1000savailable
		except Exception as e:
			raise e

	@property
	def vpx1000etotal(self) :
		r"""VPX1000E Total.
		"""
		try :
			return self._vpx1000etotal
		except Exception as e:
			raise e

	@property
	def vpx1000eavailable(self) :
		r"""VPX1000E Available.
		"""
		try :
			return self._vpx1000eavailable
		except Exception as e:
			raise e

	@property
	def vpx1000ptotal(self) :
		r"""VPX1000P Total.
		"""
		try :
			return self._vpx1000ptotal
		except Exception as e:
			raise e

	@property
	def vpx1000pavailable(self) :
		r"""VPX1000P Available.
		"""
		try :
			return self._vpx1000pavailable
		except Exception as e:
			raise e

	@property
	def vpx2000ptotal(self) :
		r"""VPX2000P Total.
		"""
		try :
			return self._vpx2000ptotal
		except Exception as e:
			raise e

	@property
	def vpx2000pavailable(self) :
		r"""VPX2000P Available.
		"""
		try :
			return self._vpx2000pavailable
		except Exception as e:
			raise e

	@property
	def vpx3000stotal(self) :
		r"""VPX3000S Total.
		"""
		try :
			return self._vpx3000stotal
		except Exception as e:
			raise e

	@property
	def vpx3000savailable(self) :
		r"""VPX3000S Available.
		"""
		try :
			return self._vpx3000savailable
		except Exception as e:
			raise e

	@property
	def vpx3000etotal(self) :
		r"""VPX3000E Total.
		"""
		try :
			return self._vpx3000etotal
		except Exception as e:
			raise e

	@property
	def vpx3000eavailable(self) :
		r"""VPX3000E Available.
		"""
		try :
			return self._vpx3000eavailable
		except Exception as e:
			raise e

	@property
	def vpx3000ptotal(self) :
		r"""VPX3000P Total.
		"""
		try :
			return self._vpx3000ptotal
		except Exception as e:
			raise e

	@property
	def vpx3000pavailable(self) :
		r"""VPX3000P Available.
		"""
		try :
			return self._vpx3000pavailable
		except Exception as e:
			raise e

	@property
	def vpx4000ptotal(self) :
		r"""VPX4000P Total.
		"""
		try :
			return self._vpx4000ptotal
		except Exception as e:
			raise e

	@property
	def vpx4000pavailable(self) :
		r"""VPX4000P Available.
		"""
		try :
			return self._vpx4000pavailable
		except Exception as e:
			raise e

	@property
	def vpx5000stotal(self) :
		r"""VPX5000S Total.
		"""
		try :
			return self._vpx5000stotal
		except Exception as e:
			raise e

	@property
	def vpx5000savailable(self) :
		r"""VPX5000S Available.
		"""
		try :
			return self._vpx5000savailable
		except Exception as e:
			raise e

	@property
	def vpx5000etotal(self) :
		r"""VPX5000E Total.
		"""
		try :
			return self._vpx5000etotal
		except Exception as e:
			raise e

	@property
	def vpx5000eavailable(self) :
		r"""VPX5000E Available.
		"""
		try :
			return self._vpx5000eavailable
		except Exception as e:
			raise e

	@property
	def vpx5000ptotal(self) :
		r"""VPX5000P Total.
		"""
		try :
			return self._vpx5000ptotal
		except Exception as e:
			raise e

	@property
	def vpx5000pavailable(self) :
		r"""VPX5000P Available.
		"""
		try :
			return self._vpx5000pavailable
		except Exception as e:
			raise e

	@property
	def vpx8000stotal(self) :
		r"""VPX8000S Total.
		"""
		try :
			return self._vpx8000stotal
		except Exception as e:
			raise e

	@property
	def vpx8000savailable(self) :
		r"""VPX8000S Available.
		"""
		try :
			return self._vpx8000savailable
		except Exception as e:
			raise e

	@property
	def vpx8000etotal(self) :
		r"""VPX8000E Total.
		"""
		try :
			return self._vpx8000etotal
		except Exception as e:
			raise e

	@property
	def vpx8000eavailable(self) :
		r"""VPX8000E Available.
		"""
		try :
			return self._vpx8000eavailable
		except Exception as e:
			raise e

	@property
	def vpx8000ptotal(self) :
		r"""VPX8000P Total.
		"""
		try :
			return self._vpx8000ptotal
		except Exception as e:
			raise e

	@property
	def vpx8000pavailable(self) :
		r"""VPX8000P Available.
		"""
		try :
			return self._vpx8000pavailable
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslicenseserverpool_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslicenseserverpool
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nslicenseserverpool resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslicenseserverpool()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nslicenseserverpool_response(base_response) :
	def __init__(self, length=1) :
		self.nslicenseserverpool = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslicenseserverpool = [nslicenseserverpool() for _ in range(length)]

