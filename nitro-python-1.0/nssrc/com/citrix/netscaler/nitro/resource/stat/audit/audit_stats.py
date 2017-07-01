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

class audit_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._auditsyslogmsgsent = 0
		self._auditsyslogmsgsentrate = 0
		self._auditsyslogmsggen = 0
		self._auditsyslogmsggenrate = 0
		self._auditsyslogmsgsenttcp = 0
		self._auditsyslogmsgsenttcprate = 0
		self._auditnsballocfail = 0
		self._auditnsballocfailrate = 0
		self._auditlog32errsyslogallocnsbfail = 0
		self._auditlog32errsyslogallocnsbfailrate = 0
		self._auditmemallocfail = 0
		self._auditmemallocfailrate = 0
		self._auditportallocfail = 0
		self._auditportallocfailrate = 0
		self._auditcontextnotfound = 0
		self._auditcontextnotfoundrate = 0
		self._nsbchainallocfail = 0
		self._nsbchainallocfailrate = 0
		self._clientconnfail = 0
		self._clientconnfailrate = 0
		self._flushcmdcnt = 0
		self._flushcmdcntrate = 0
		self._systcpconnfail = 0
		self._systcpconnfailrate = 0
		self._logunsentlbsys = 0
		self._logunsentlbsysrate = 0
		self._logsdropped = 0
		self._logsdroppedrate = 0
		self._logsdroppedtxminnsbs = 0
		self._logsdroppedtxminnsbsrate = 0

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
	def auditportallocfailrate(self) :
		r"""Rate (/s) counter for auditportallocfail.
		"""
		try :
			return self._auditportallocfailrate
		except Exception as e:
			raise e

	@property
	def auditnsballocfailrate(self) :
		r"""Rate (/s) counter for auditnsballocfail.
		"""
		try :
			return self._auditnsballocfailrate
		except Exception as e:
			raise e

	@property
	def auditsyslogmsgsenttcprate(self) :
		r"""Rate (/s) counter for auditsyslogmsgsenttcp.
		"""
		try :
			return self._auditsyslogmsgsenttcprate
		except Exception as e:
			raise e

	@property
	def auditcontextnotfoundrate(self) :
		r"""Rate (/s) counter for auditcontextnotfound.
		"""
		try :
			return self._auditcontextnotfoundrate
		except Exception as e:
			raise e

	@property
	def logsdroppedtxminnsbs(self) :
		r"""Total number of log messages dropped by NetScaler when NSBQ length is less than TX min NSBs.
		"""
		try :
			return self._logsdroppedtxminnsbs
		except Exception as e:
			raise e

	@property
	def clientconnfail(self) :
		r"""Failures in establishment of a connection between the NetScaler and the auditserver tool (the Netscaler's custom logging tool).
		"""
		try :
			return self._clientconnfail
		except Exception as e:
			raise e

	@property
	def flushcmdcntrate(self) :
		r"""Rate (/s) counter for flushcmdcnt.
		"""
		try :
			return self._flushcmdcntrate
		except Exception as e:
			raise e

	@property
	def auditlog32errsyslogallocnsbfailrate(self) :
		r"""Rate (/s) counter for auditlog32errsyslogallocnsbfail.
		"""
		try :
			return self._auditlog32errsyslogallocnsbfailrate
		except Exception as e:
			raise e

	@property
	def auditnsballocfail(self) :
		r"""NAT allocation failed.
		"""
		try :
			return self._auditnsballocfail
		except Exception as e:
			raise e

	@property
	def auditsyslogmsgsentrate(self) :
		r"""Rate (/s) counter for auditsyslogmsgsent.
		"""
		try :
			return self._auditsyslogmsgsentrate
		except Exception as e:
			raise e

	@property
	def clientconnfailrate(self) :
		r"""Rate (/s) counter for clientconnfail.
		"""
		try :
			return self._clientconnfailrate
		except Exception as e:
			raise e

	@property
	def auditmemallocfailrate(self) :
		r"""Rate (/s) counter for auditmemallocfail.
		"""
		try :
			return self._auditmemallocfailrate
		except Exception as e:
			raise e

	@property
	def auditlog32errsyslogallocnsbfail(self) :
		r"""Nsb allocation failed.
		"""
		try :
			return self._auditlog32errsyslogallocnsbfail
		except Exception as e:
			raise e

	@property
	def logsdroppedrate(self) :
		r"""Rate (/s) counter for logsdropped.
		"""
		try :
			return self._logsdroppedrate
		except Exception as e:
			raise e

	@property
	def auditportallocfail(self) :
		r"""Number of times the NetScaler failed to allocate a port when sending a syslog message to the syslog server(s).
		"""
		try :
			return self._auditportallocfail
		except Exception as e:
			raise e

	@property
	def nsbchainallocfail(self) :
		r"""Nsb Chain allocation failed.
		"""
		try :
			return self._nsbchainallocfail
		except Exception as e:
			raise e

	@property
	def logunsentlbsys(self) :
		r"""Total auditlog messages which are not delivered to load balanced syslog servers.
		"""
		try :
			return self._logunsentlbsys
		except Exception as e:
			raise e

	@property
	def systcpconnfailrate(self) :
		r"""Rate (/s) counter for systcpconnfail.
		"""
		try :
			return self._systcpconnfailrate
		except Exception as e:
			raise e

	@property
	def systcpconnfail(self) :
		r"""Failures in establishment of a connection between the NetScaler and the syslog server.
		"""
		try :
			return self._systcpconnfail
		except Exception as e:
			raise e

	@property
	def auditmemallocfail(self) :
		r"""Failures in allocation of Access Gateway context structure. When an Access Gateway session is established, the NetScaler creates an internal context structure , which identifies the user and the IP address from which the user has logged in.
		"""
		try :
			return self._auditmemallocfail
		except Exception as e:
			raise e

	@property
	def logunsentlbsysrate(self) :
		r"""Rate (/s) counter for logunsentlbsys.
		"""
		try :
			return self._logunsentlbsysrate
		except Exception as e:
			raise e

	@property
	def auditsyslogmsggenrate(self) :
		r"""Rate (/s) counter for auditsyslogmsggen.
		"""
		try :
			return self._auditsyslogmsggenrate
		except Exception as e:
			raise e

	@property
	def logsdropped(self) :
		r"""Total number of log messages dropped by NetScaler after max hold limit is reached.
		"""
		try :
			return self._logsdropped
		except Exception as e:
			raise e

	@property
	def auditsyslogmsgsent(self) :
		r"""Syslog messages sent to the syslog server(s) over UDP.
		"""
		try :
			return self._auditsyslogmsgsent
		except Exception as e:
			raise e

	@property
	def auditcontextnotfound(self) :
		r"""Failures in finding the context structure for an Access Gateway session during attempts to send session-specific audit messages.
		During an Access Gateway session, audit messages related to the session are queued up in the auditlog buffer for transmission to the audit log server(s). If the session is killed before the messages are sent, the context structure allocated at session creation is removed. This structure is needed for sending the queued auditlog messages. If it is not found, this counter is incremented.
		"""
		try :
			return self._auditcontextnotfound
		except Exception as e:
			raise e

	@property
	def flushcmdcnt(self) :
		r"""Auditlog buffer flushes. In a multiprocessor NetScaler, both the main processor and the co-processor can generate auditlog messages and fill up the auditlog buffers. But only the primary processor can free up the buffers by sending auditlog messages to the auditlog server(s). The number of auditlog buffers is fixed. If the co-processor detects that all the auditlog buffers are full, it issues a flush command to the main processor.
		"""
		try :
			return self._flushcmdcnt
		except Exception as e:
			raise e

	@property
	def logsdroppedtxminnsbsrate(self) :
		r"""Rate (/s) counter for logsdroppedtxminnsbs.
		"""
		try :
			return self._logsdroppedtxminnsbsrate
		except Exception as e:
			raise e

	@property
	def auditsyslogmsggen(self) :
		r"""Syslog messages about to be sent to the syslog server.
		"""
		try :
			return self._auditsyslogmsggen
		except Exception as e:
			raise e

	@property
	def nsbchainallocfailrate(self) :
		r"""Rate (/s) counter for nsbchainallocfail.
		"""
		try :
			return self._nsbchainallocfailrate
		except Exception as e:
			raise e

	@property
	def auditsyslogmsgsenttcp(self) :
		r"""Syslog messages sent to the syslog server(s) over TCP.
		"""
		try :
			return self._auditsyslogmsgsenttcp
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(audit_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.audit
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all audit_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = audit_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class audit_response(base_response) :
	def __init__(self, length=1) :
		self.audit = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.audit = [audit_stats() for _ in range(length)]

