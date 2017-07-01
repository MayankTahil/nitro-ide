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

class appfwprofile_stats(base_resource) :
	r""" Statistics for application firewall profile resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._appfirewallrequestsperprofile = 0
		self._appfirewallrequestsperprofilerate = 0
		self._appfirewallreqbytesperprofile = 0
		self._appfirewallreqbytesperprofilerate = 0
		self._appfirewallresponsesperprofile = 0
		self._appfirewallresponsesperprofilerate = 0
		self._appfirewallresbytesperprofile = 0
		self._appfirewallresbytesperprofilerate = 0
		self._appfirewallabortsperprofile = 0
		self._appfirewallabortsperprofilerate = 0
		self._appfirewallredirectsperprofile = 0
		self._appfirewallredirectsperprofilerate = 0
		self._appfirewalllongavgresptimeperprofile = 0
		self._appfirewallshortavgresptimeperprofile = 0
		self._appfirewallviolstarturlperprofile = 0
		self._appfirewallviolstarturlperprofilerate = 0
		self._appfirewallvioldenyurlperprofile = 0
		self._appfirewallvioldenyurlperprofilerate = 0
		self._appfirewallviolrefererheaderperprofile = 0
		self._appfirewallviolrefererheaderperprofilerate = 0
		self._appfirewallviolbufferoverflowperprofile = 0
		self._appfirewallviolbufferoverflowperprofilerate = 0
		self._appfirewallviolcookieperprofile = 0
		self._appfirewallviolcookieperprofilerate = 0
		self._appfirewallviolcsrftagperprofile = 0
		self._appfirewallviolcsrftagperprofilerate = 0
		self._appfirewallviolxssperprofile = 0
		self._appfirewallviolxssperprofilerate = 0
		self._appfirewallviolsqlperprofile = 0
		self._appfirewallviolsqlperprofilerate = 0
		self._appfirewallviolfieldformatperprofile = 0
		self._appfirewallviolfieldformatperprofilerate = 0
		self._appfirewallviolfieldconsistencyperprofile = 0
		self._appfirewallviolfieldconsistencyperprofilerate = 0
		self._appfirewallviolcreditcardperprofile = 0
		self._appfirewallviolcreditcardperprofilerate = 0
		self._appfirewallviolsafeobjectperprofile = 0
		self._appfirewallviolsafeobjectperprofilerate = 0
		self._appfirewallviolsignatureperprofile = 0
		self._appfirewallviolsignatureperprofilerate = 0
		self._appfirewallviolcontenttypeperprofile = 0
		self._appfirewallviolcontenttypeperprofilerate = 0
		self._appfirewallviolwellformednessviolationsperprofile = 0
		self._appfirewallviolwellformednessviolationsperprofilerate = 0
		self._appfirewallviolxdosviolationsperprofile = 0
		self._appfirewallviolxdosviolationsperprofilerate = 0
		self._appfirewallviolmsgvalviolationsperprofile = 0
		self._appfirewallviolmsgvalviolationsperprofilerate = 0
		self._appfirewallviolwsiviolationsperprofile = 0
		self._appfirewallviolwsiviolationsperprofilerate = 0
		self._appfirewallviolxmlsqlviolationsperprofile = 0
		self._appfirewallviolxmlsqlviolationsperprofilerate = 0
		self._appfirewallviolxmlxssviolationsperprofile = 0
		self._appfirewallviolxmlxssviolationsperprofilerate = 0
		self._appfirewallviolxmlattachmentviolationsperprofile = 0
		self._appfirewallviolxmlattachmentviolationsperprofilerate = 0
		self._appfirewallviolxmlsoapfaultviolationsperprofile = 0
		self._appfirewallviolxmlsoapfaultviolationsperprofilerate = 0
		self._appfirewallviolxmlgenericviolationsperprofile = 0
		self._appfirewallviolxmlgenericviolationsperprofilerate = 0
		self._appfirewalltotalviolperprofile = 0
		self._appfirewallviolperprofilerate = 0
		self._appfirewalllogstarturlperprofile = 0
		self._appfirewalllogstarturlperprofilerate = 0
		self._appfirewalllogdenyurlperprofile = 0
		self._appfirewalllogdenyurlperprofilerate = 0
		self._appfirewalllogrefererheaderperprofile = 0
		self._appfirewalllogrefererheaderperprofilerate = 0
		self._appfirewalllogbufferoverflowperprofile = 0
		self._appfirewalllogbufferoverflowperprofilerate = 0
		self._appfirewalllogcookieperprofile = 0
		self._appfirewalllogcookieperprofilerate = 0
		self._appfirewalllogcsrftagperprofile = 0
		self._appfirewalllogcsrftagperprofilerate = 0
		self._appfirewalllogxssperprofile = 0
		self._appfirewalllogxssperprofilerate = 0
		self._appfirewalllogxformxssperprofile = 0
		self._appfirewalllogxformxssperprofilerate = 0
		self._appfirewalllogsqlperprofile = 0
		self._appfirewalllogsqlperprofilerate = 0
		self._appfirewalllogxformsqlperprofile = 0
		self._appfirewalllogxformsqlperprofilerate = 0
		self._appfirewalllogfieldformatperprofile = 0
		self._appfirewalllogfieldformatperprofilerate = 0
		self._appfirewalllogfieldconsistencyperprofile = 0
		self._appfirewalllogfieldconsistencyperprofilerate = 0
		self._appfirewalllogcreditcardperprofile = 0
		self._appfirewalllogcreditcardperprofilerate = 0
		self._appfirewallxformlogcreditcardperprofile = 0
		self._appfirewallxformlogcreditcardperprofilerate = 0
		self._appfirewalllogsafeobjectperprofile = 0
		self._appfirewalllogsafeobjectperprofilerate = 0
		self._appfirewalllogcontenttypeperprofile = 0
		self._appfirewalllogcontenttypeperprofilerate = 0
		self._appfirewallwellformednesslogsperprofile = 0
		self._appfirewallwellformednesslogsperprofilerate = 0
		self._appfirewallxdoslogsperprofile = 0
		self._appfirewallxdoslogsperprofilerate = 0
		self._appfirewallmsgvallogsperprofile = 0
		self._appfirewallmsgvallogsperprofilerate = 0
		self._appfirewallwsilogsperprofile = 0
		self._appfirewallwsilogsperprofilerate = 0
		self._appfirewallxmlsqllogsperprofile = 0
		self._appfirewallxmlsqllogsperprofilerate = 0
		self._appfirewallxmlxsslogsperprofile = 0
		self._appfirewallxmlxsslogsperprofilerate = 0
		self._appfirewallxmlattachmentlogsperprofile = 0
		self._appfirewallxmlattachmentlogsperprofilerate = 0
		self._appfirewallxmlsoapfaultlogsperprofile = 0
		self._appfirewallxmlsoapfaultlogsperprofilerate = 0
		self._appfirewallxmlgenericlogsperprofile = 0
		self._appfirewallxmlgenericlogsperprofilerate = 0
		self._appfirewalltotallogperprofile = 0
		self._appfirewalllogperprofilerate = 0
		self._appfirewallret4xxperprofile = 0
		self._appfirewallret4xxperprofilerate = 0
		self._appfirewallret5xxperprofile = 0
		self._appfirewallret5xxperprofilerate = 0

	@property
	def name(self) :
		r"""Name of the application firewall profile.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the application firewall profile.
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
	def appfirewallxmlxsslogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxmlxsslogsperprofile.
		"""
		try :
			return self._appfirewallxmlxsslogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolmsgvalviolationsperprofile(self) :
		r"""Number of XML Message Validation security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolmsgvalviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogcontenttypeperprofile(self) :
		r"""Number of Content type security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcontenttypeperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalltotalviolperprofile.
		"""
		try :
			return self._appfirewallviolperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolstarturlperprofile(self) :
		r"""Number of Start URL security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolstarturlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalltotalviolperprofile(self) :
		r"""Number of violations seen by the application firewall on per profile basis.
		"""
		try :
			return self._appfirewalltotalviolperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallret5xxperprofile(self) :
		r"""Number of requests returning HTTP 5xx from the backend server.
		"""
		try :
			return self._appfirewallret5xxperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolcontenttypeperprofile(self) :
		r"""Number of Content Type security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcontenttypeperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallredirectsperprofile(self) :
		r"""HTTP/HTTPS requests redirected by the Application Firewall to a different Web page or web server. (HTTP 302).
		"""
		try :
			return self._appfirewallredirectsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallresponsesperprofile(self) :
		r"""HTTP/HTTPS responses sent by your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallresponsesperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsqllogsperprofile(self) :
		r"""Number of XML SQL Injection security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlsqllogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallwsilogsperprofile(self) :
		r"""Number of Web Services Interoperability (WS-I) security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallwsilogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallrequestsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallrequestsperprofile.
		"""
		try :
			return self._appfirewallrequestsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsoapfaultviolationsperprofile(self) :
		r"""Number of requests returning soap:fault from the backend server.
		"""
		try :
			return self._appfirewallviolxmlsoapfaultviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogbufferoverflowperprofile(self) :
		r"""Number of Buffer Overflow security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogbufferoverflowperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolwsiviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolwsiviolationsperprofile.
		"""
		try :
			return self._appfirewallviolwsiviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolwellformednessviolationsperprofile(self) :
		r"""Number of XML Format security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolwellformednessviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldformatperprofile(self) :
		r"""Number of Field Format security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolfieldformatperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolcookieperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolcookieperprofile.
		"""
		try :
			return self._appfirewallviolcookieperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallresbytesperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallresbytesperprofile.
		"""
		try :
			return self._appfirewallresbytesperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxformxssperprofile(self) :
		r"""Number of HTML Cross-Site Scripting security check transform log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogxformxssperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogcookieperprofile(self) :
		r"""Number of Cookie Consistency security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcookieperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolcreditcardperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolcreditcardperprofile.
		"""
		try :
			return self._appfirewallviolcreditcardperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsoapfaultlogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxmlsoapfaultlogsperprofile.
		"""
		try :
			return self._appfirewallxmlsoapfaultlogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldconsistencyperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogfieldconsistencyperprofile.
		"""
		try :
			return self._appfirewalllogfieldconsistencyperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogdenyurlperprofile(self) :
		r"""Number of Deny URL security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogdenyurlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallresbytesperprofile(self) :
		r"""Number of bytes transfered for responses.
		"""
		try :
			return self._appfirewallresbytesperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxssperprofile(self) :
		r"""Number of HTML Cross-Site Scripting security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxssperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallmsgvallogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallmsgvallogsperprofile.
		"""
		try :
			return self._appfirewallmsgvallogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsoapfaultviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlsoapfaultviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxmlsoapfaultviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcsrftagperprofile(self) :
		r"""Number of Cross Site Request Forgery form tag security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcsrftagperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolcontenttypeperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolcontenttypeperprofile.
		"""
		try :
			return self._appfirewallviolcontenttypeperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsoapfaultlogsperprofile(self) :
		r"""Number of requests generating soap:fault log messages.
		"""
		try :
			return self._appfirewallxmlsoapfaultlogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallxformlogcreditcardperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxformlogcreditcardperprofile.
		"""
		try :
			return self._appfirewallxformlogcreditcardperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallreqbytesperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallreqbytesperprofile.
		"""
		try :
			return self._appfirewallreqbytesperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolmsgvalviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolmsgvalviolationsperprofile.
		"""
		try :
			return self._appfirewallviolmsgvalviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxdoslogsperprofile(self) :
		r"""Number of XML Denial-of-Service security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxdoslogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldconsistencyperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolfieldconsistencyperprofile.
		"""
		try :
			return self._appfirewallviolfieldconsistencyperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogrefererheaderperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogrefererheaderperprofile.
		"""
		try :
			return self._appfirewalllogrefererheaderperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlattachmentlogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxmlattachmentlogsperprofile.
		"""
		try :
			return self._appfirewallxmlattachmentlogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlxssviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlxssviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxmlxssviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxdoslogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxdoslogsperprofile.
		"""
		try :
			return self._appfirewallxdoslogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlxsslogsperprofile(self) :
		r"""Number of XML Cross-Site Scripting (XSS) security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlxsslogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsqllogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxmlsqllogsperprofile.
		"""
		try :
			return self._appfirewallxmlsqllogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallrequestsperprofile(self) :
		r"""HTTP/HTTPS requests sent to your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallrequestsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolsignatureperprofile(self) :
		r"""Number of Signature violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsignatureperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlattachmentviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlattachmentviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxmlattachmentviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolsqlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolsqlperprofile.
		"""
		try :
			return self._appfirewallviolsqlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcsrftagperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolcsrftagperprofile.
		"""
		try :
			return self._appfirewallviolcsrftagperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolstarturlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolstarturlperprofile.
		"""
		try :
			return self._appfirewallviolstarturlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxformxssperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogxformxssperprofile.
		"""
		try :
			return self._appfirewalllogxformxssperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsqlviolationsperprofile(self) :
		r"""Number of XML SQL Injection security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlsqlviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogsqlperprofile(self) :
		r"""Number of HTML SQL Injection security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogsqlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallvioldenyurlperprofile(self) :
		r"""Number of Deny URL security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallvioldenyurlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallredirectsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallredirectsperprofile.
		"""
		try :
			return self._appfirewallredirectsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogstarturlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogstarturlperprofile.
		"""
		try :
			return self._appfirewalllogstarturlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcsrftagperprofile(self) :
		r"""Number of Cross Site Request Forgery form tag security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcsrftagperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallwellformednesslogsperprofile(self) :
		r"""Number of XML Format security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallwellformednesslogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogdenyurlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogdenyurlperprofile.
		"""
		try :
			return self._appfirewalllogdenyurlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolwsiviolationsperprofile(self) :
		r"""Number of Web Services Interoperability (WS-I) security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolwsiviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallshortavgresptimeperprofile(self) :
		r"""Average backend response time in milliseconds over the last 7 seconds.
		"""
		try :
			return self._appfirewallshortavgresptimeperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolsafeobjectperprofile(self) :
		r"""Number of Safe Object security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsafeobjectperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallresponsesperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallresponsesperprofile.
		"""
		try :
			return self._appfirewallresponsesperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolrefererheaderperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolrefererheaderperprofile.
		"""
		try :
			return self._appfirewallviolrefererheaderperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallvioldenyurlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallvioldenyurlperprofile.
		"""
		try :
			return self._appfirewallvioldenyurlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallabortsperprofile(self) :
		r"""Incomplete HTTP/HTTPS requests aborted by the client before the Application Firewall could finish processing them.
		"""
		try :
			return self._appfirewallabortsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolcookieperprofile(self) :
		r"""Number of Cookie Consistency security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcookieperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogcreditcardperprofile(self) :
		r"""Number of Credit Card security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcreditcardperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogbufferoverflowperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogbufferoverflowperprofile.
		"""
		try :
			return self._appfirewalllogbufferoverflowperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlgenericlogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallxmlgenericlogsperprofile.
		"""
		try :
			return self._appfirewallxmlgenericlogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallret4xxperprofile(self) :
		r"""Number of requests returning HTTP 4xx from the backend server.
		"""
		try :
			return self._appfirewallret4xxperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldformatperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolfieldformatperprofile.
		"""
		try :
			return self._appfirewallviolfieldformatperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxformsqlperprofile(self) :
		r"""Number of HTML SQL Injection security check transform log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogxformsqlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolbufferoverflowperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolbufferoverflowperprofile.
		"""
		try :
			return self._appfirewallviolbufferoverflowperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallmsgvallogsperprofile(self) :
		r"""Number of XML Message Validation security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallmsgvallogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallwsilogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallwsilogsperprofile.
		"""
		try :
			return self._appfirewallwsilogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolsqlperprofile(self) :
		r"""Number of HTML SQL Injection security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsqlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxssperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxssperprofile.
		"""
		try :
			return self._appfirewallviolxssperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlgenericlogsperprofile(self) :
		r"""Number of requests generating XML Generic log messages.
		"""
		try :
			return self._appfirewallxmlgenericlogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalltotallogperprofile.
		"""
		try :
			return self._appfirewalllogperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcreditcardperprofile(self) :
		r"""Number of Credit Card security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcreditcardperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallxmlattachmentlogsperprofile(self) :
		r"""Number of XML Attachment security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlattachmentlogsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldconsistencyperprofile(self) :
		r"""Number of Field Consistency security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolfieldconsistencyperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogcsrftagperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogcsrftagperprofile.
		"""
		try :
			return self._appfirewalllogcsrftagperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallret4xxperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallret4xxperprofile.
		"""
		try :
			return self._appfirewallret4xxperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldformatperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogfieldformatperprofile.
		"""
		try :
			return self._appfirewalllogfieldformatperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolsafeobjectperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolsafeobjectperprofile.
		"""
		try :
			return self._appfirewallviolsafeobjectperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxssperprofile(self) :
		r"""Number of HTML Cross-Site Scripting security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogxssperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlgenericviolationsperprofile(self) :
		r"""Number of requests returning XML generic violation from the backend server.
		"""
		try :
			return self._appfirewallviolxmlgenericviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolsignatureperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolsignatureperprofile.
		"""
		try :
			return self._appfirewallviolsignatureperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllongavgresptimeperprofile(self) :
		r"""Average backend response time in milliseconds since reboot.
		"""
		try :
			return self._appfirewalllongavgresptimeperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldformatperprofile(self) :
		r"""Number of Field Format security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogfieldformatperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallabortsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallabortsperprofile.
		"""
		try :
			return self._appfirewallabortsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcreditcardperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogcreditcardperprofile.
		"""
		try :
			return self._appfirewalllogcreditcardperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogsqlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogsqlperprofile.
		"""
		try :
			return self._appfirewalllogsqlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolbufferoverflowperprofile(self) :
		r"""Number of Buffer Overflow security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolbufferoverflowperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogsafeobjectperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogsafeobjectperprofile.
		"""
		try :
			return self._appfirewalllogsafeobjectperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldconsistencyperprofile(self) :
		r"""Number of Field Consistency security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogfieldconsistencyperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogstarturlperprofile(self) :
		r"""Number of Start URL security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogstarturlperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsqlviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlsqlviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxmlsqlviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxssperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogxssperprofile.
		"""
		try :
			return self._appfirewalllogxssperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcontenttypeperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogcontenttypeperprofile.
		"""
		try :
			return self._appfirewalllogcontenttypeperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallwellformednesslogsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallwellformednesslogsperprofile.
		"""
		try :
			return self._appfirewallwellformednesslogsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallreqbytesperprofile(self) :
		r"""Number of bytes transfered for requests.
		"""
		try :
			return self._appfirewallreqbytesperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogsafeobjectperprofile(self) :
		r"""Number of Safe Object security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogsafeobjectperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlgenericviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlgenericviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxmlgenericviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlattachmentviolationsperprofile(self) :
		r"""Number of XML Attachment security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlattachmentviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogrefererheaderperprofile(self) :
		r"""Number of Referer Header security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogrefererheaderperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallviolxdosviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolxdosviolationsperprofile.
		"""
		try :
			return self._appfirewallviolxdosviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolwellformednessviolationsperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallviolwellformednessviolationsperprofile.
		"""
		try :
			return self._appfirewallviolwellformednessviolationsperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxdosviolationsperprofile(self) :
		r"""Number of XML Denial-of-Service security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxdosviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogxformsqlperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogxformsqlperprofile.
		"""
		try :
			return self._appfirewalllogxformsqlperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlxssviolationsperprofile(self) :
		r"""Number of XML Cross-Site Scripting (XSS) security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlxssviolationsperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalltotallogperprofile(self) :
		r"""Number of log messages generated by the application firewall on per profile basis.
		"""
		try :
			return self._appfirewalltotallogperprofile
		except Exception as e:
			raise e

	@property
	def appfirewalllogcookieperprofilerate(self) :
		r"""Rate (/s) counter for appfirewalllogcookieperprofile.
		"""
		try :
			return self._appfirewalllogcookieperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallret5xxperprofilerate(self) :
		r"""Rate (/s) counter for appfirewallret5xxperprofile.
		"""
		try :
			return self._appfirewallret5xxperprofilerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolrefererheaderperprofile(self) :
		r"""Number of Referer Header security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolrefererheaderperprofile
		except Exception as e:
			raise e

	@property
	def appfirewallxformlogcreditcardperprofile(self) :
		r"""Number of Credit Card security check transform log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxformlogcreditcardperprofile
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile
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
		r""" Use this API to fetch the statistics of all appfwprofile_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = appfwprofile_stats()
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

class appfwprofile_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile = [appfwprofile_stats() for _ in range(length)]

