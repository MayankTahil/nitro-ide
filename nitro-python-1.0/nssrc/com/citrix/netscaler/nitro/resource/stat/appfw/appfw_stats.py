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

class appfw_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._appfirewalltotallog = 0
		self._appfirewalllograte = 0
		self._appfirewalltotalviol = 0
		self._appfirewallviolrate = 0
		self._appfirewallshortavgresptime = 0
		self._appfirewalllongavgresptime = 0
		self._appfirewallrequests = 0
		self._appfirewallrequestsrate = 0
		self._appfirewallreqbytes = 0
		self._appfirewallreqbytesrate = 0
		self._appfirewallresponses = 0
		self._appfirewallresponsesrate = 0
		self._appfirewallresbytes = 0
		self._appfirewallresbytesrate = 0
		self._appfirewallaborts = 0
		self._appfirewallabortsrate = 0
		self._appfirewallredirects = 0
		self._appfirewallredirectsrate = 0
		self._appfirewalltrapsdropped = 0
		self._appfirewallviolstarturl = 0
		self._appfirewallviolstarturlrate = 0
		self._appfirewallvioldenyurl = 0
		self._appfirewallvioldenyurlrate = 0
		self._appfirewallviolrefererheader = 0
		self._appfirewallviolrefererheaderrate = 0
		self._appfirewallviolbufferoverflow = 0
		self._appfirewallviolbufferoverflowrate = 0
		self._appfirewallviolcookie = 0
		self._appfirewallviolcookierate = 0
		self._appfirewallviolcsrftag = 0
		self._appfirewallviolcsrftagrate = 0
		self._appfirewallviolxss = 0
		self._appfirewallviolxssrate = 0
		self._appfirewallviolsql = 0
		self._appfirewallviolsqlrate = 0
		self._appfirewallviolfieldformat = 0
		self._appfirewallviolfieldformatrate = 0
		self._appfirewallviolfieldconsistency = 0
		self._appfirewallviolfieldconsistencyrate = 0
		self._appfirewallviolcreditcard = 0
		self._appfirewallviolcreditcardrate = 0
		self._appfirewallviolsafeobject = 0
		self._appfirewallviolsafeobjectrate = 0
		self._appfirewallviolsignature = 0
		self._appfirewallviolsignaturerate = 0
		self._appfirewallviolcontenttype = 0
		self._appfirewallviolcontenttyperate = 0
		self._appfirewallviolwellformednessviolations = 0
		self._appfirewallviolwellformednessviolationsrate = 0
		self._appfirewallviolxdosviolations = 0
		self._appfirewallviolxdosviolationsrate = 0
		self._appfirewallviolmsgvalviolations = 0
		self._appfirewallviolmsgvalviolationsrate = 0
		self._appfirewallviolwsiviolations = 0
		self._appfirewallviolwsiviolationsrate = 0
		self._appfirewallviolxmlsqlviolations = 0
		self._appfirewallviolxmlsqlviolationsrate = 0
		self._appfirewallviolxmlxssviolations = 0
		self._appfirewallviolxmlxssviolationsrate = 0
		self._appfirewallviolxmlattachmentviolations = 0
		self._appfirewallviolxmlattachmentviolationsrate = 0
		self._appfirewallviolxmlsoapfaultviolations = 0
		self._appfirewallviolxmlsoapfaultviolationsrate = 0
		self._appfirewallviolxmlgenviolations = 0
		self._appfirewallviolxmlgenviolationsrate = 0
		self._appfirewalllogstarturl = 0
		self._appfirewalllogstarturlrate = 0
		self._appfirewalllogdenyurl = 0
		self._appfirewalllogdenyurlrate = 0
		self._appfirewalllogrefererheader = 0
		self._appfirewalllogrefererheaderrate = 0
		self._appfirewalllogbufferoverflow = 0
		self._appfirewalllogbufferoverflowrate = 0
		self._appfirewalllogcookie = 0
		self._appfirewalllogcookierate = 0
		self._appfirewalllogcsrftag = 0
		self._appfirewalllogcsrftagrate = 0
		self._appfirewalllogxss = 0
		self._appfirewalllogxssrate = 0
		self._appfirewalllogtransformxss = 0
		self._appfirewalllogtransformxssrate = 0
		self._appfirewalllogsql = 0
		self._appfirewalllogsqlrate = 0
		self._appfirewalllogtransformsql = 0
		self._appfirewalllogtransformsqlrate = 0
		self._appfirewalllogfieldformat = 0
		self._appfirewalllogfieldformatrate = 0
		self._appfirewalllogfieldconsistency = 0
		self._appfirewalllogfieldconsistencyrate = 0
		self._appfirewalllogcreditcard = 0
		self._appfirewalllogcreditcardrate = 0
		self._appfirewalllogsafeobject = 0
		self._appfirewalllogsafeobjectrate = 0
		self._appfirewallsignaturelogs = 0
		self._appfirewallsignaturelogsrate = 0
		self._appfirewalllogcontenttype = 0
		self._appfirewalllogcontenttyperate = 0
		self._appfirewallwellformednesslogs = 0
		self._appfirewallwellformednesslogsrate = 0
		self._appfirewallxdoslogs = 0
		self._appfirewallxdoslogsrate = 0
		self._appfirewallmsgvallogs = 0
		self._appfirewallmsgvallogsrate = 0
		self._appfirewallwsilogs = 0
		self._appfirewallwsilogsrate = 0
		self._appfirewallxmlsqllogs = 0
		self._appfirewallxmlsqllogsrate = 0
		self._appfirewallxmlxsslogs = 0
		self._appfirewallxmlxsslogsrate = 0
		self._appfirewallxmlattachmentlogs = 0
		self._appfirewallxmlattachmentlogsrate = 0
		self._appfirewallxmlsoapfaultlogs = 0
		self._appfirewallxmlsoapfaultlogsrate = 0
		self._appfirewallxmlgenlogs = 0
		self._appfirewallxmlgenlogsrate = 0
		self._appfirewallret4xx = 0
		self._appfirewallret4xxrate = 0
		self._appfirewallret5xx = 0
		self._appfirewallret5xxrate = 0

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
	def appfirewallredirectsrate(self) :
		r"""Rate (/s) counter for appfirewallredirects.
		"""
		try :
			return self._appfirewallredirectsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcookierate(self) :
		r"""Rate (/s) counter for appfirewallviolcookie.
		"""
		try :
			return self._appfirewallviolcookierate
		except Exception as e:
			raise e

	@property
	def appfirewallsignaturelogs(self) :
		r"""Number of Signature logs generated by the Application Firewall.
		"""
		try :
			return self._appfirewallsignaturelogs
		except Exception as e:
			raise e

	@property
	def appfirewalllogdenyurl(self) :
		r"""Number of Deny URL security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogdenyurl
		except Exception as e:
			raise e

	@property
	def appfirewalllogsqlrate(self) :
		r"""Rate (/s) counter for appfirewalllogsql.
		"""
		try :
			return self._appfirewalllogsqlrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldconsistency(self) :
		r"""Number of Field Consistency security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolfieldconsistency
		except Exception as e:
			raise e

	@property
	def appfirewallviolbufferoverflowrate(self) :
		r"""Rate (/s) counter for appfirewallviolbufferoverflow.
		"""
		try :
			return self._appfirewallviolbufferoverflowrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogtransformsql(self) :
		r"""Number of HTML SQL Injection security check transform log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogtransformsql
		except Exception as e:
			raise e

	@property
	def appfirewallviolxssrate(self) :
		r"""Rate (/s) counter for appfirewallviolxss.
		"""
		try :
			return self._appfirewallviolxssrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogtransformsqlrate(self) :
		r"""Rate (/s) counter for appfirewalllogtransformsql.
		"""
		try :
			return self._appfirewalllogtransformsqlrate
		except Exception as e:
			raise e

	@property
	def appfirewalltotalviol(self) :
		r"""Total number of security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewalltotalviol
		except Exception as e:
			raise e

	@property
	def appfirewallwellformednesslogs(self) :
		r"""Number of XML Format security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallwellformednesslogs
		except Exception as e:
			raise e

	@property
	def appfirewallviolsafeobjectrate(self) :
		r"""Rate (/s) counter for appfirewallviolsafeobject.
		"""
		try :
			return self._appfirewallviolsafeobjectrate
		except Exception as e:
			raise e

	@property
	def appfirewallresponsesrate(self) :
		r"""Rate (/s) counter for appfirewallresponses.
		"""
		try :
			return self._appfirewallresponsesrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlxssviolations(self) :
		r"""Number of XML Cross-Site Scripting (XSS) security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlxssviolations
		except Exception as e:
			raise e

	@property
	def appfirewallresponses(self) :
		r"""HTTP/HTTPS responses sent by your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallresponses
		except Exception as e:
			raise e

	@property
	def appfirewallviolsignature(self) :
		r"""Number of Signature violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsignature
		except Exception as e:
			raise e

	@property
	def appfirewalllogbufferoverflow(self) :
		r"""Number of Buffer Overflow security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogbufferoverflow
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlgenviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlgenviolations.
		"""
		try :
			return self._appfirewallviolxmlgenviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolrate(self) :
		r"""Rate (/s) counter for appfirewalltotalviol.
		"""
		try :
			return self._appfirewallviolrate
		except Exception as e:
			raise e

	@property
	def appfirewallabortsrate(self) :
		r"""Rate (/s) counter for appfirewallaborts.
		"""
		try :
			return self._appfirewallabortsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsoapfaultviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlsoapfaultviolations.
		"""
		try :
			return self._appfirewallviolxmlsoapfaultviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallrequestsrate(self) :
		r"""Rate (/s) counter for appfirewallrequests.
		"""
		try :
			return self._appfirewallrequestsrate
		except Exception as e:
			raise e

	@property
	def appfirewallwsilogs(self) :
		r"""Number of Web Services Interoperability (WS-I) security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallwsilogs
		except Exception as e:
			raise e

	@property
	def appfirewallredirects(self) :
		r"""HTTP/HTTPS requests redirected by the Application Firewall to a different Web page or web server. (HTTP 302).
		"""
		try :
			return self._appfirewallredirects
		except Exception as e:
			raise e

	@property
	def appfirewallsignaturelogsrate(self) :
		r"""Rate (/s) counter for appfirewallsignaturelogs.
		"""
		try :
			return self._appfirewallsignaturelogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallxdoslogsrate(self) :
		r"""Rate (/s) counter for appfirewallxdoslogs.
		"""
		try :
			return self._appfirewallxdoslogsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogtransformxss(self) :
		r"""Number of HTML Cross-Site Scripting security check transform log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogtransformxss
		except Exception as e:
			raise e

	@property
	def appfirewallxmlattachmentlogsrate(self) :
		r"""Rate (/s) counter for appfirewallxmlattachmentlogs.
		"""
		try :
			return self._appfirewallxmlattachmentlogsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogrefererheaderrate(self) :
		r"""Rate (/s) counter for appfirewalllogrefererheader.
		"""
		try :
			return self._appfirewalllogrefererheaderrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcookie(self) :
		r"""Number of Cookie Consistency security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcookie
		except Exception as e:
			raise e

	@property
	def appfirewallviolcreditcardrate(self) :
		r"""Rate (/s) counter for appfirewallviolcreditcard.
		"""
		try :
			return self._appfirewallviolcreditcardrate
		except Exception as e:
			raise e

	@property
	def appfirewallret5xx(self) :
		r"""Number of requests returning HTTP 5xx from the backend server.
		"""
		try :
			return self._appfirewallret5xx
		except Exception as e:
			raise e

	@property
	def appfirewallviolmsgvalviolations(self) :
		r"""Number of XML Message Validation security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolmsgvalviolations
		except Exception as e:
			raise e

	@property
	def appfirewalllongavgresptime(self) :
		r"""Average backend response time in milliseconds since reboot.
		"""
		try :
			return self._appfirewalllongavgresptime
		except Exception as e:
			raise e

	@property
	def appfirewalllogstarturl(self) :
		r"""Number of Start URL security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogstarturl
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlgenviolations(self) :
		r"""Number of requests returning XML generic error from the backend server.
		"""
		try :
			return self._appfirewallviolxmlgenviolations
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsoapfaultviolations(self) :
		r"""Number of requests returning soap:fault from the backend server.
		"""
		try :
			return self._appfirewallviolxmlsoapfaultviolations
		except Exception as e:
			raise e

	@property
	def appfirewallviolsafeobject(self) :
		r"""Number of Safe Object security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsafeobject
		except Exception as e:
			raise e

	@property
	def appfirewalllogxssrate(self) :
		r"""Rate (/s) counter for appfirewalllogxss.
		"""
		try :
			return self._appfirewalllogxssrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolsql(self) :
		r"""Number of HTML SQL Injection security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolsql
		except Exception as e:
			raise e

	@property
	def appfirewallviolxdosviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxdosviolations.
		"""
		try :
			return self._appfirewallviolxdosviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcreditcardrate(self) :
		r"""Rate (/s) counter for appfirewalllogcreditcard.
		"""
		try :
			return self._appfirewalllogcreditcardrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogsql(self) :
		r"""Number of HTML SQL Injection security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogsql
		except Exception as e:
			raise e

	@property
	def appfirewalllogdenyurlrate(self) :
		r"""Rate (/s) counter for appfirewalllogdenyurl.
		"""
		try :
			return self._appfirewalllogdenyurlrate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsoapfaultlogs(self) :
		r"""Number of requests generating soap:fault log messages.
		"""
		try :
			return self._appfirewallxmlsoapfaultlogs
		except Exception as e:
			raise e

	@property
	def appfirewalllogcontenttyperate(self) :
		r"""Rate (/s) counter for appfirewalllogcontenttype.
		"""
		try :
			return self._appfirewalllogcontenttyperate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlattachmentviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlattachmentviolations.
		"""
		try :
			return self._appfirewallviolxmlattachmentviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogbufferoverflowrate(self) :
		r"""Rate (/s) counter for appfirewalllogbufferoverflow.
		"""
		try :
			return self._appfirewalllogbufferoverflowrate
		except Exception as e:
			raise e

	@property
	def appfirewallret5xxrate(self) :
		r"""Rate (/s) counter for appfirewallret5xx.
		"""
		try :
			return self._appfirewallret5xxrate
		except Exception as e:
			raise e

	@property
	def appfirewalltotallog(self) :
		r"""Total number of security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalltotallog
		except Exception as e:
			raise e

	@property
	def appfirewalllogcookierate(self) :
		r"""Rate (/s) counter for appfirewalllogcookie.
		"""
		try :
			return self._appfirewalllogcookierate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcsrftag(self) :
		r"""Number of Cross Site Request Forgery form tag security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcsrftag
		except Exception as e:
			raise e

	@property
	def appfirewallviolxss(self) :
		r"""Number of HTML Cross-Site Scripting security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxss
		except Exception as e:
			raise e

	@property
	def appfirewallviolwellformednessviolations(self) :
		r"""Number of XML Format security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolwellformednessviolations
		except Exception as e:
			raise e

	@property
	def appfirewallreqbytes(self) :
		r"""Number of bytes transfered for requests.
		"""
		try :
			return self._appfirewallreqbytes
		except Exception as e:
			raise e

	@property
	def appfirewallxmlattachmentlogs(self) :
		r"""Number of XML Attachment security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlattachmentlogs
		except Exception as e:
			raise e

	@property
	def appfirewalllogcsrftagrate(self) :
		r"""Rate (/s) counter for appfirewalllogcsrftag.
		"""
		try :
			return self._appfirewalllogcsrftagrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolmsgvalviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolmsgvalviolations.
		"""
		try :
			return self._appfirewallviolmsgvalviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcontenttyperate(self) :
		r"""Rate (/s) counter for appfirewallviolcontenttype.
		"""
		try :
			return self._appfirewallviolcontenttyperate
		except Exception as e:
			raise e

	@property
	def appfirewalllograte(self) :
		r"""Rate (/s) counter for appfirewalltotallog.
		"""
		try :
			return self._appfirewalllograte
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsqllogsrate(self) :
		r"""Rate (/s) counter for appfirewallxmlsqllogs.
		"""
		try :
			return self._appfirewallxmlsqllogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlgenlogs(self) :
		r"""Number of requests generating XML generic error log messages.
		"""
		try :
			return self._appfirewallxmlgenlogs
		except Exception as e:
			raise e

	@property
	def appfirewallreqbytesrate(self) :
		r"""Rate (/s) counter for appfirewallreqbytes.
		"""
		try :
			return self._appfirewallreqbytesrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogsafeobject(self) :
		r"""Number of Safe Object security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogsafeobject
		except Exception as e:
			raise e

	@property
	def appfirewallviolcreditcard(self) :
		r"""Number of Credit Card security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcreditcard
		except Exception as e:
			raise e

	@property
	def appfirewalllogrefererheader(self) :
		r"""Number of Referer Header security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogrefererheader
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsqlviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlsqlviolations.
		"""
		try :
			return self._appfirewallviolxmlsqlviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallaborts(self) :
		r"""Incomplete HTTP/HTTPS requests aborted by the client before the Application Firewall could finish processing them.
		"""
		try :
			return self._appfirewallaborts
		except Exception as e:
			raise e

	@property
	def appfirewallviolcsrftagrate(self) :
		r"""Rate (/s) counter for appfirewallviolcsrftag.
		"""
		try :
			return self._appfirewallviolcsrftagrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogstarturlrate(self) :
		r"""Rate (/s) counter for appfirewalllogstarturl.
		"""
		try :
			return self._appfirewalllogstarturlrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolcookie(self) :
		r"""Number of Cookie Consistency security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcookie
		except Exception as e:
			raise e

	@property
	def appfirewallxmlxsslogs(self) :
		r"""Number of XML Cross-Site Scripting (XSS) security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlxsslogs
		except Exception as e:
			raise e

	@property
	def appfirewallmsgvallogs(self) :
		r"""Number of XML Message Validation security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallmsgvallogs
		except Exception as e:
			raise e

	@property
	def appfirewallviolwsiviolations(self) :
		r"""Number of Web Services Interoperability (WS-I) security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolwsiviolations
		except Exception as e:
			raise e

	@property
	def appfirewallviolcsrftag(self) :
		r"""Number of Cross Site Request Forgery form tag security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcsrftag
		except Exception as e:
			raise e

	@property
	def appfirewallrequests(self) :
		r"""HTTP/HTTPS requests sent to your protected web servers via the Application Firewall.
		"""
		try :
			return self._appfirewallrequests
		except Exception as e:
			raise e

	@property
	def appfirewallresbytes(self) :
		r"""Number of bytes transfered for responses.
		"""
		try :
			return self._appfirewallresbytes
		except Exception as e:
			raise e

	@property
	def appfirewallviolbufferoverflow(self) :
		r"""Number of Buffer Overflow security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolbufferoverflow
		except Exception as e:
			raise e

	@property
	def appfirewallviolsignaturerate(self) :
		r"""Rate (/s) counter for appfirewallviolsignature.
		"""
		try :
			return self._appfirewallviolsignaturerate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlxssviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolxmlxssviolations.
		"""
		try :
			return self._appfirewallviolxmlxssviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxdosviolations(self) :
		r"""Number of XML Denial-of-Service security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxdosviolations
		except Exception as e:
			raise e

	@property
	def appfirewalllogsafeobjectrate(self) :
		r"""Rate (/s) counter for appfirewalllogsafeobject.
		"""
		try :
			return self._appfirewalllogsafeobjectrate
		except Exception as e:
			raise e

	@property
	def appfirewallxdoslogs(self) :
		r"""Number of XML Denial-of-Service security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxdoslogs
		except Exception as e:
			raise e

	@property
	def appfirewallviolcontenttype(self) :
		r"""Number of Content type security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolcontenttype
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldconsistencyrate(self) :
		r"""Rate (/s) counter for appfirewallviolfieldconsistency.
		"""
		try :
			return self._appfirewallviolfieldconsistencyrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogtransformxssrate(self) :
		r"""Rate (/s) counter for appfirewalllogtransformxss.
		"""
		try :
			return self._appfirewalllogtransformxssrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldformatrate(self) :
		r"""Rate (/s) counter for appfirewalllogfieldformat.
		"""
		try :
			return self._appfirewalllogfieldformatrate
		except Exception as e:
			raise e

	@property
	def appfirewallwellformednesslogsrate(self) :
		r"""Rate (/s) counter for appfirewallwellformednesslogs.
		"""
		try :
			return self._appfirewallwellformednesslogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolwsiviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolwsiviolations.
		"""
		try :
			return self._appfirewallviolwsiviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcreditcard(self) :
		r"""Number of Credit Card security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcreditcard
		except Exception as e:
			raise e

	@property
	def appfirewallviolwellformednessviolationsrate(self) :
		r"""Rate (/s) counter for appfirewallviolwellformednessviolations.
		"""
		try :
			return self._appfirewallviolwellformednessviolationsrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldformatrate(self) :
		r"""Rate (/s) counter for appfirewallviolfieldformat.
		"""
		try :
			return self._appfirewallviolfieldformatrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldconsistencyrate(self) :
		r"""Rate (/s) counter for appfirewalllogfieldconsistency.
		"""
		try :
			return self._appfirewalllogfieldconsistencyrate
		except Exception as e:
			raise e

	@property
	def appfirewallvioldenyurl(self) :
		r"""Number of Deny URL security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallvioldenyurl
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlattachmentviolations(self) :
		r"""Number of XML Attachment security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlattachmentviolations
		except Exception as e:
			raise e

	@property
	def appfirewallviolsqlrate(self) :
		r"""Rate (/s) counter for appfirewallviolsql.
		"""
		try :
			return self._appfirewallviolsqlrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolstarturlrate(self) :
		r"""Rate (/s) counter for appfirewallviolstarturl.
		"""
		try :
			return self._appfirewallviolstarturlrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolxmlsqlviolations(self) :
		r"""Number of XML SQL Injection security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolxmlsqlviolations
		except Exception as e:
			raise e

	@property
	def appfirewallshortavgresptime(self) :
		r"""Average backend response time in milliseconds over the last 7 seconds.
		"""
		try :
			return self._appfirewallshortavgresptime
		except Exception as e:
			raise e

	@property
	def appfirewallxmlgenlogsrate(self) :
		r"""Rate (/s) counter for appfirewallxmlgenlogs.
		"""
		try :
			return self._appfirewallxmlgenlogsrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldformat(self) :
		r"""Number of Field Format security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogfieldformat
		except Exception as e:
			raise e

	@property
	def appfirewallxmlxsslogsrate(self) :
		r"""Rate (/s) counter for appfirewallxmlxsslogs.
		"""
		try :
			return self._appfirewallxmlxsslogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallresbytesrate(self) :
		r"""Rate (/s) counter for appfirewallresbytes.
		"""
		try :
			return self._appfirewallresbytesrate
		except Exception as e:
			raise e

	@property
	def appfirewallviolrefererheader(self) :
		r"""Number of Referer Header security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolrefererheader
		except Exception as e:
			raise e

	@property
	def appfirewallviolrefererheaderrate(self) :
		r"""Rate (/s) counter for appfirewallviolrefererheader.
		"""
		try :
			return self._appfirewallviolrefererheaderrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogxss(self) :
		r"""Number of HTML Cross-Site Scripting security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogxss
		except Exception as e:
			raise e

	@property
	def appfirewalltrapsdropped(self) :
		r"""AppFirewall SNMP traps dropped due to time limit.
		"""
		try :
			return self._appfirewalltrapsdropped
		except Exception as e:
			raise e

	@property
	def appfirewallviolstarturl(self) :
		r"""Number of Start URL security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolstarturl
		except Exception as e:
			raise e

	@property
	def appfirewallret4xxrate(self) :
		r"""Rate (/s) counter for appfirewallret4xx.
		"""
		try :
			return self._appfirewallret4xxrate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsqllogs(self) :
		r"""Number of XML SQL Injection security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewallxmlsqllogs
		except Exception as e:
			raise e

	@property
	def appfirewallwsilogsrate(self) :
		r"""Rate (/s) counter for appfirewallwsilogs.
		"""
		try :
			return self._appfirewallwsilogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallxmlsoapfaultlogsrate(self) :
		r"""Rate (/s) counter for appfirewallxmlsoapfaultlogs.
		"""
		try :
			return self._appfirewallxmlsoapfaultlogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallvioldenyurlrate(self) :
		r"""Rate (/s) counter for appfirewallvioldenyurl.
		"""
		try :
			return self._appfirewallvioldenyurlrate
		except Exception as e:
			raise e

	@property
	def appfirewalllogcontenttype(self) :
		r"""Number of content type security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogcontenttype
		except Exception as e:
			raise e

	@property
	def appfirewallmsgvallogsrate(self) :
		r"""Rate (/s) counter for appfirewallmsgvallogs.
		"""
		try :
			return self._appfirewallmsgvallogsrate
		except Exception as e:
			raise e

	@property
	def appfirewallret4xx(self) :
		r"""Number of requests returning HTTP 4xx from the backend server.
		"""
		try :
			return self._appfirewallret4xx
		except Exception as e:
			raise e

	@property
	def appfirewallviolfieldformat(self) :
		r"""Number of Field Format security check violations seen by the Application Firewall.
		"""
		try :
			return self._appfirewallviolfieldformat
		except Exception as e:
			raise e

	@property
	def appfirewalllogfieldconsistency(self) :
		r"""Number of Field Consistency security check log messages generated by the Application Firewall.
		"""
		try :
			return self._appfirewalllogfieldconsistency
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfw_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfw
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
		r""" Use this API to fetch the statistics of all appfw_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = appfw_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class appfw_response(base_response) :
	def __init__(self, length=1) :
		self.appfw = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfw = [appfw_stats() for _ in range(length)]

