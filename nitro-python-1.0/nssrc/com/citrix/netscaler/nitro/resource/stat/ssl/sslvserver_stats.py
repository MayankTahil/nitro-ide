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

class sslvserver_stats(base_resource) :
	r""" Statistics for SSL virtual server resource.
	"""
	def __init__(self) :
		self._vservername = None
		self._clearstats = None
		self._vslbhealth = 0
		self._primaryipaddress = ""
		self._primaryport = 0
		self._type = ""
		self._state = ""
		self._actsvcs = 0
		self._ssltotclientauthsuccess = 0
		self._sslclientauthsuccessrate = 0
		self._ssltotclientauthfailure = 0
		self._sslclientauthfailurerate = 0
		self._sslctxtotencbytes = 0
		self._sslctxencbytesrate = 0
		self._sslctxtotdecbytes = 0
		self._sslctxdecbytesrate = 0
		self._sslctxtothwencbytes = 0
		self._sslctxhwencbytesrate = 0
		self._sslctxtothwdec_bytes = 0
		self._sslctxhwdec_bytesrate = 0
		self._sslctxtotsessionnew = 0
		self._sslctxsessionnewrate = 0
		self._sslctxtotsessionhits = 0
		self._sslctxsessionhitsrate = 0

		self.scpolicy = []
		self.appfwpolicy = []
		self.cmppolicy = []
		self.responderpolicy = []
		self.pqpolicy = []
		self.rewritepolicy = []
		self.cachepolicy = []
	@property
	def vservername(self) :
		r"""Name of the SSL virtual server for which to show detailed statistics.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		r"""Name of the SSL virtual server for which to show detailed statistics
		"""
		try :
			self._vservername = vservername
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
	def sslclientauthsuccessrate(self) :
		r"""Rate (/s) counter for ssltotclientauthsuccess.
		"""
		try :
			return self._sslclientauthsuccessrate
		except Exception as e:
			raise e

	@property
	def sslctxtothwdec_bytes(self) :
		r"""Number of hw decrypted bytes per SSL vserver.
		"""
		try :
			return self._sslctxtothwdec_bytes
		except Exception as e:
			raise e

	@property
	def sslctxtotencbytes(self) :
		r"""Number of encrypted bytes per SSL vserver.
		"""
		try :
			return self._sslctxtotencbytes
		except Exception as e:
			raise e

	@property
	def sslctxtotsessionnew(self) :
		r"""Number of new sessions created.
		"""
		try :
			return self._sslctxtotsessionnew
		except Exception as e:
			raise e

	@property
	def ssltotclientauthfailure(self) :
		r"""Number of failure client authentication on this vserver.
		"""
		try :
			return self._ssltotclientauthfailure
		except Exception as e:
			raise e

	@property
	def sslctxdecbytesrate(self) :
		r"""Rate (/s) counter for sslctxtotdecbytes.
		"""
		try :
			return self._sslctxdecbytesrate
		except Exception as e:
			raise e

	@property
	def sslctxsessionnewrate(self) :
		r"""Rate (/s) counter for sslctxtotsessionnew.
		"""
		try :
			return self._sslctxsessionnewrate
		except Exception as e:
			raise e

	@property
	def sslclientauthfailurerate(self) :
		r"""Rate (/s) counter for ssltotclientauthfailure.
		"""
		try :
			return self._sslclientauthfailurerate
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
	def sslctxencbytesrate(self) :
		r"""Rate (/s) counter for sslctxtotencbytes.
		"""
		try :
			return self._sslctxencbytesrate
		except Exception as e:
			raise e

	@property
	def sslctxhwencbytesrate(self) :
		r"""Rate (/s) counter for sslctxtothwencbytes.
		"""
		try :
			return self._sslctxhwencbytesrate
		except Exception as e:
			raise e

	@property
	def sslctxtotdecbytes(self) :
		r"""Number of decrypted bytes per SSL vserver.
		"""
		try :
			return self._sslctxtotdecbytes
		except Exception as e:
			raise e

	@property
	def primaryipaddress(self) :
		r"""IP address of the vserver.
		"""
		try :
			return self._primaryipaddress
		except Exception as e:
			raise e

	@property
	def sslctxtotsessionhits(self) :
		r"""Number of session hits.
		"""
		try :
			return self._sslctxtotsessionhits
		except Exception as e:
			raise e

	@property
	def sslctxtothwencbytes(self) :
		r"""Number of hardware encrypted bytes per SSL vserver.
		"""
		try :
			return self._sslctxtothwencbytes
		except Exception as e:
			raise e

	@property
	def sslctxsessionhitsrate(self) :
		r"""Rate (/s) counter for sslctxtotsessionhits.
		"""
		try :
			return self._sslctxsessionhitsrate
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
	def vslbhealth(self) :
		r"""Health of the vserver. This gives percentage of UP services bound to this vserver.
		"""
		try :
			return self._vslbhealth
		except Exception as e:
			raise e

	@property
	def actsvcs(self) :
		r"""number of ACTIVE services bound to a vserver.
		"""
		try :
			return self._actsvcs
		except Exception as e:
			raise e

	@property
	def sslctxhwdec_bytesrate(self) :
		r"""Rate (/s) counter for sslctxtothwdec_bytes.
		"""
		try :
			return self._sslctxhwdec_bytesrate
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
	def ssltotclientauthsuccess(self) :
		r"""Number of successful client authentication on this vserver.
		"""
		try :
			return self._ssltotclientauthsuccess
		except Exception as e:
			raise e

	@property
	def responderpolicy(self) :
		r"""responderpolicy that are bound to sslvserver.
		"""
		try :
			return self._responderpolicy
		except Exception as e:
			raise e

	@responderpolicy.setter
	def responderpolicy(self, responderpolicy) :
		r"""responderpolicy that are bound to sslvserver.
		"""
		try :
			self._responderpolicy = responderpolicy
		except Exception as e:
			raise e

	@property
	def cachepolicy(self) :
		r"""cachepolicy that are bound to sslvserver.
		"""
		try :
			return self._cachepolicy
		except Exception as e:
			raise e

	@cachepolicy.setter
	def cachepolicy(self, cachepolicy) :
		r"""cachepolicy that are bound to sslvserver.
		"""
		try :
			self._cachepolicy = cachepolicy
		except Exception as e:
			raise e

	@property
	def rewritepolicy(self) :
		r"""rewritepolicy that are bound to sslvserver.
		"""
		try :
			return self._rewritepolicy
		except Exception as e:
			raise e

	@rewritepolicy.setter
	def rewritepolicy(self, rewritepolicy) :
		r"""rewritepolicy that are bound to sslvserver.
		"""
		try :
			self._rewritepolicy = rewritepolicy
		except Exception as e:
			raise e

	@property
	def pqpolicy(self) :
		r"""pqpolicy that are bound to sslvserver.
		"""
		try :
			return self._pqpolicy
		except Exception as e:
			raise e

	@pqpolicy.setter
	def pqpolicy(self, pqpolicy) :
		r"""pqpolicy that are bound to sslvserver.
		"""
		try :
			self._pqpolicy = pqpolicy
		except Exception as e:
			raise e

	@property
	def appfwpolicy(self) :
		r"""appfwpolicy that are bound to sslvserver.
		"""
		try :
			return self._appfwpolicy
		except Exception as e:
			raise e

	@appfwpolicy.setter
	def appfwpolicy(self, appfwpolicy) :
		r"""appfwpolicy that are bound to sslvserver.
		"""
		try :
			self._appfwpolicy = appfwpolicy
		except Exception as e:
			raise e

	@property
	def scpolicy(self) :
		r"""scpolicy that are bound to sslvserver.
		"""
		try :
			return self._scpolicy
		except Exception as e:
			raise e

	@scpolicy.setter
	def scpolicy(self, scpolicy) :
		r"""scpolicy that are bound to sslvserver.
		"""
		try :
			self._scpolicy = scpolicy
		except Exception as e:
			raise e

	@property
	def cmppolicy(self) :
		r"""cmppolicy that are bound to sslvserver.
		"""
		try :
			return self._cmppolicy
		except Exception as e:
			raise e

	@cmppolicy.setter
	def cmppolicy(self, cmppolicy) :
		r"""cmppolicy that are bound to sslvserver.
		"""
		try :
			self._cmppolicy = cmppolicy
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.vservername is not None :
				return str(self.vservername)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all sslvserver_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = sslvserver_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.vservername = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class sslvserver_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver = [sslvserver_stats() for _ in range(length)]

