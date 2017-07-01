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

class authenticationvserver_stats(base_resource) :
	r""" Statistics for authentication virtual server resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
		self._totalrequests = 0
		self._requestsrate = 0
		self._totalresponses = 0
		self._responsesrate = 0
		self._totalrequestbytes = 0
		self._requestbytesrate = 0
		self._totalresponsebytes = 0
		self._responsebytesrate = 0

		self.authenticationloginschemapolicy = []
		self.authenticationsamlidppolicy = []
		self.authenticationpolicy = []
		self.tmsessionpolicy = []
	@property
	def name(self) :
		r"""Name of the authentication virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the authentication virtual server.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def totalrequests(self) :
		r"""Total number of requests received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalrequests
		except Exception as e:
			raise e

	@property
	def responsebytesrate(self) :
		r"""Rate (/s) counter for totalresponsebytes.
		"""
		try :
			return self._responsebytesrate
		except Exception as e:
			raise e

	@property
	def requestbytesrate(self) :
		r"""Rate (/s) counter for totalrequestbytes.
		"""
		try :
			return self._requestbytesrate
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Protocol associated with the vserver.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		r"""The IP address on which the service is running.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def responsesrate(self) :
		r"""Rate (/s) counter for totalresponses.
		"""
		try :
			return self._responsesrate
		except Exception as e:
			raise e

	@property
	def totalrequestbytes(self) :
		r"""Total number of request bytes received on this service or virtual server.
		"""
		try :
			return self._totalrequestbytes
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current state of the server. Possible values are UP, DOWN, UNKNOWN, OFS(Out of Service), TROFS(Transition Out of Service), TROFS_DOWN(Down When going Out of Service).
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def totalresponses(self) :
		r"""Number of responses received on this service or virtual server. (This applies to HTTP/SSL services and servers.).
		"""
		try :
			return self._totalresponses
		except Exception as e:
			raise e

	@property
	def totalresponsebytes(self) :
		r"""Number of response bytes received by this service or virtual server.
		"""
		try :
			return self._totalresponsebytes
		except Exception as e:
			raise e

	@property
	def primaryport(self) :
		r"""The port on which the service is running.
		"""
		try :
			return self._primaryport
		except Exception as e:
			raise e

	@property
	def requestsrate(self) :
		r"""Rate (/s) counter for totalrequests.
		"""
		try :
			return self._requestsrate
		except Exception as e:
			raise e

	@property
	def authenticationpolicy(self) :
		r"""authenticationpolicy that are bound to authenticationvserver.
		"""
		try :
			return self._authenticationpolicy
		except Exception as e:
			raise e

	@authenticationpolicy.setter
	def authenticationpolicy(self, authenticationpolicy) :
		r"""authenticationpolicy that are bound to authenticationvserver.
		"""
		try :
			self._authenticationpolicy = authenticationpolicy
		except Exception as e:
			raise e

	@property
	def authenticationsamlidppolicy(self) :
		r"""authenticationsamlidppolicy that are bound to authenticationvserver.
		"""
		try :
			return self._authenticationsamlidppolicy
		except Exception as e:
			raise e

	@authenticationsamlidppolicy.setter
	def authenticationsamlidppolicy(self, authenticationsamlidppolicy) :
		r"""authenticationsamlidppolicy that are bound to authenticationvserver.
		"""
		try :
			self._authenticationsamlidppolicy = authenticationsamlidppolicy
		except Exception as e:
			raise e

	@property
	def authenticationloginschemapolicy(self) :
		r"""authenticationloginschemapolicy that are bound to authenticationvserver.
		"""
		try :
			return self._authenticationloginschemapolicy
		except Exception as e:
			raise e

	@authenticationloginschemapolicy.setter
	def authenticationloginschemapolicy(self, authenticationloginschemapolicy) :
		r"""authenticationloginschemapolicy that are bound to authenticationvserver.
		"""
		try :
			self._authenticationloginschemapolicy = authenticationloginschemapolicy
		except Exception as e:
			raise e

	@property
	def tmsessionpolicy(self) :
		r"""tmsessionpolicy that are bound to authenticationvserver.
		"""
		try :
			return self._tmsessionpolicy
		except Exception as e:
			raise e

	@tmsessionpolicy.setter
	def tmsessionpolicy(self, tmsessionpolicy) :
		r"""tmsessionpolicy that are bound to authenticationvserver.
		"""
		try :
			self._tmsessionpolicy = tmsessionpolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all authenticationvserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = authenticationvserver_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class authenticationvserver_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationvserver = [authenticationvserver_stats() for _ in range(length)]

