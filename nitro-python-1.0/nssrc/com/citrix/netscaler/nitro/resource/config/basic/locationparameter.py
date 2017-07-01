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

class locationparameter(base_resource) :
	""" Configuration for location parameter resource. """
	def __init__(self) :
		self._context = None
		self._q1label = None
		self._q2label = None
		self._q3label = None
		self._q4label = None
		self._q5label = None
		self._q6label = None
		self._Locationfile = None
		self._format = None
		self._custom = None
		self._Static = None
		self._lines = None
		self._errors = None
		self._warnings = None
		self._entries = None
		self._locationfile6 = None
		self._format6 = None
		self._custom6 = None
		self._static6 = None
		self._lines6 = None
		self._errors6 = None
		self._warnings6 = None
		self._entries6 = None
		self._flags = None
		self._status = None
		self._databasemode = None
		self._flushing = None
		self._loading = None
		self._matchwildcardtoany = None

	@property
	def context(self) :
		r"""Context for describing locations. In geographic context, qualifier labels are assigned by default in the following sequence: Continent.Country.Region.City.ISP.Organization. In custom context, the qualifiers labels can have any meaning that you designate.<br/>Possible values = geographic, custom.
		"""
		try :
			return self._context
		except Exception as e:
			raise e

	@context.setter
	def context(self, context) :
		r"""Context for describing locations. In geographic context, qualifier labels are assigned by default in the following sequence: Continent.Country.Region.City.ISP.Organization. In custom context, the qualifiers labels can have any meaning that you designate.<br/>Possible values = geographic, custom
		"""
		try :
			self._context = context
		except Exception as e:
			raise e

	@property
	def q1label(self) :
		r"""Label specifying the meaning of the first qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q1label
		except Exception as e:
			raise e

	@q1label.setter
	def q1label(self, q1label) :
		r"""Label specifying the meaning of the first qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q1label = q1label
		except Exception as e:
			raise e

	@property
	def q2label(self) :
		r"""Label specifying the meaning of the second qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q2label
		except Exception as e:
			raise e

	@q2label.setter
	def q2label(self, q2label) :
		r"""Label specifying the meaning of the second qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q2label = q2label
		except Exception as e:
			raise e

	@property
	def q3label(self) :
		r"""Label specifying the meaning of the third qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q3label
		except Exception as e:
			raise e

	@q3label.setter
	def q3label(self, q3label) :
		r"""Label specifying the meaning of the third qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q3label = q3label
		except Exception as e:
			raise e

	@property
	def q4label(self) :
		r"""Label specifying the meaning of the fourth qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q4label
		except Exception as e:
			raise e

	@q4label.setter
	def q4label(self, q4label) :
		r"""Label specifying the meaning of the fourth qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q4label = q4label
		except Exception as e:
			raise e

	@property
	def q5label(self) :
		r"""Label specifying the meaning of the fifth qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q5label
		except Exception as e:
			raise e

	@q5label.setter
	def q5label(self, q5label) :
		r"""Label specifying the meaning of the fifth qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q5label = q5label
		except Exception as e:
			raise e

	@property
	def q6label(self) :
		r"""Label specifying the meaning of the sixth qualifier. Can be specified for custom context only.<br/>Minimum length =  1.
		"""
		try :
			return self._q6label
		except Exception as e:
			raise e

	@q6label.setter
	def q6label(self, q6label) :
		r"""Label specifying the meaning of the sixth qualifier. Can be specified for custom context only.<br/>Minimum length =  1
		"""
		try :
			self._q6label = q6label
		except Exception as e:
			raise e

	@property
	def Locationfile(self) :
		r"""Currently loaded location database file.
		"""
		try :
			return self._Locationfile
		except Exception as e:
			raise e

	@property
	def format(self) :
		r"""Location file format.<br/>Possible values = netscaler, ip-country, ip-country-isp, ip-country-region-city, ip-country-region-city-isp, geoip-country, geoip-region, geoip-city, geoip-country-org, geoip-country-isp, geoip-city-isp-org.
		"""
		try :
			return self._format
		except Exception as e:
			raise e

	@property
	def custom(self) :
		r"""Number of configured custom locations.
		"""
		try :
			return self._custom
		except Exception as e:
			raise e

	@property
	def Static(self) :
		r"""Number of configured locations in the database file (static locations).
		"""
		try :
			return self._Static
		except Exception as e:
			raise e

	@property
	def lines(self) :
		r"""Number of lines in the databse files.
		"""
		try :
			return self._lines
		except Exception as e:
			raise e

	@property
	def errors(self) :
		r"""Number of errros encountered while reading the database file.
		"""
		try :
			return self._errors
		except Exception as e:
			raise e

	@property
	def warnings(self) :
		r"""Number of warnings encountered while reading the database file.
		"""
		try :
			return self._warnings
		except Exception as e:
			raise e

	@property
	def entries(self) :
		r"""Number of successfully added entries.
		"""
		try :
			return self._entries
		except Exception as e:
			raise e

	@property
	def locationfile6(self) :
		r"""Currently loaded location database file.
		"""
		try :
			return self._locationfile6
		except Exception as e:
			raise e

	@property
	def format6(self) :
		r"""Location file format.<br/>Possible values = netscaler6, geoip-country6.
		"""
		try :
			return self._format6
		except Exception as e:
			raise e

	@property
	def custom6(self) :
		r"""Number of configured custom locations.
		"""
		try :
			return self._custom6
		except Exception as e:
			raise e

	@property
	def static6(self) :
		r"""Number of configured locations in the database file (static locations).
		"""
		try :
			return self._static6
		except Exception as e:
			raise e

	@property
	def lines6(self) :
		r"""Number of lines in the databse files.
		"""
		try :
			return self._lines6
		except Exception as e:
			raise e

	@property
	def errors6(self) :
		r"""Number of errros encountered while reading the database file.
		"""
		try :
			return self._errors6
		except Exception as e:
			raise e

	@property
	def warnings6(self) :
		r"""Number of warnings encountered while reading the database file.
		"""
		try :
			return self._warnings6
		except Exception as e:
			raise e

	@property
	def entries6(self) :
		r"""Number of successfully added entries.
		"""
		try :
			return self._entries6
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Information needed for display. This argument passes information from the kernel to the user space.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""This argument displays when the status (success or failure) of database loading.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def databasemode(self) :
		r"""This argument displays the database mode.<br/>Possible values = File, Internal, Not applicable.
		"""
		try :
			return self._databasemode
		except Exception as e:
			raise e

	@property
	def flushing(self) :
		r"""This argument displays the state of flushing.<br/>Possible values = In progress, Idle.
		"""
		try :
			return self._flushing
		except Exception as e:
			raise e

	@property
	def loading(self) :
		r"""This argument displays the state of loading.<br/>Possible values = In progress, Idle.
		"""
		try :
			return self._loading
		except Exception as e:
			raise e

	@property
	def matchwildcardtoany(self) :
		r"""Indicates whether wildcard qualifiers should match any other qualifier including non-wildcard. Option to fallback after default behavior changes to not match.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._matchwildcardtoany
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(locationparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.locationparameter
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
		r""" Use this API to update locationparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = locationparameter()
				updateresource.context = resource.context
				updateresource.q1label = resource.q1label
				updateresource.q2label = resource.q2label
				updateresource.q3label = resource.q3label
				updateresource.q4label = resource.q4label
				updateresource.q5label = resource.q5label
				updateresource.q6label = resource.q6label
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of locationparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = locationparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the locationparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = locationparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Matchwildcardtoany:
		YES = "YES"
		NO = "NO"

	class Loading:
		In_progress = "In progress"
		Idle = "Idle"

	class Databasemode:
		File = "File"
		Internal = "Internal"
		Not_applicable = "Not applicable"

	class Context:
		geographic = "geographic"
		custom = "custom"

	class Flushing:
		In_progress = "In progress"
		Idle = "Idle"

	class Format:
		netscaler = "netscaler"
		ip_country = "ip-country"
		ip_country_isp = "ip-country-isp"
		ip_country_region_city = "ip-country-region-city"
		ip_country_region_city_isp = "ip-country-region-city-isp"
		geoip_country = "geoip-country"
		geoip_region = "geoip-region"
		geoip_city = "geoip-city"
		geoip_country_org = "geoip-country-org"
		geoip_country_isp = "geoip-country-isp"
		geoip_city_isp_org = "geoip-city-isp-org"

	class Format6:
		netscaler6 = "netscaler6"
		geoip_country6 = "geoip-country6"

class locationparameter_response(base_response) :
	def __init__(self, length=1) :
		self.locationparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.locationparameter = [locationparameter() for _ in range(length)]

