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

class lbgroup(base_resource) :
	""" Configuration for LB group resource. """
	def __init__(self) :
		self._name = None
		self._persistencetype = None
		self._persistencebackup = None
		self._backuppersistencetimeout = None
		self._persistmask = None
		self._cookiename = None
		self._v6persistmasklen = None
		self._cookiedomain = None
		self._timeout = None
		self._rule = None
		self._usevserverpersistency = None
		self._mastervserver = None
		self._newname = None
		self._td = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name of the load balancing virtual server group.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the load balancing virtual server group.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def persistencetype(self) :
		r"""Type of persistence for the group. Available settings function as follows:
		* SOURCEIP - Create persistence sessions based on the client IP.
		* COOKIEINSERT - Create persistence sessions based on a cookie in client requests. The cookie is inserted by a Set-Cookie directive from the server, in its first response to a client.
		* RULE - Create persistence sessions based on a user defined rule.
		* NONE - Disable persistence for the group.<br/>Possible values = SOURCEIP, COOKIEINSERT, RULE, NONE.
		"""
		try :
			return self._persistencetype
		except Exception as e:
			raise e

	@persistencetype.setter
	def persistencetype(self, persistencetype) :
		r"""Type of persistence for the group. Available settings function as follows:
		* SOURCEIP - Create persistence sessions based on the client IP.
		* COOKIEINSERT - Create persistence sessions based on a cookie in client requests. The cookie is inserted by a Set-Cookie directive from the server, in its first response to a client.
		* RULE - Create persistence sessions based on a user defined rule.
		* NONE - Disable persistence for the group.<br/>Possible values = SOURCEIP, COOKIEINSERT, RULE, NONE
		"""
		try :
			self._persistencetype = persistencetype
		except Exception as e:
			raise e

	@property
	def persistencebackup(self) :
		r"""Type of backup persistence for the group.<br/>Possible values = SOURCEIP, NONE.
		"""
		try :
			return self._persistencebackup
		except Exception as e:
			raise e

	@persistencebackup.setter
	def persistencebackup(self, persistencebackup) :
		r"""Type of backup persistence for the group.<br/>Possible values = SOURCEIP, NONE
		"""
		try :
			self._persistencebackup = persistencebackup
		except Exception as e:
			raise e

	@property
	def backuppersistencetimeout(self) :
		r"""Time period, in minutes, for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._backuppersistencetimeout
		except Exception as e:
			raise e

	@backuppersistencetimeout.setter
	def backuppersistencetimeout(self, backuppersistencetimeout) :
		r"""Time period, in minutes, for which backup persistence is in effect.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._backuppersistencetimeout = backuppersistencetimeout
		except Exception as e:
			raise e

	@property
	def persistmask(self) :
		r"""Persistence mask to apply to source IPv4 addresses when creating source IP based persistence sessions.<br/>Minimum length =  1.
		"""
		try :
			return self._persistmask
		except Exception as e:
			raise e

	@persistmask.setter
	def persistmask(self, persistmask) :
		r"""Persistence mask to apply to source IPv4 addresses when creating source IP based persistence sessions.<br/>Minimum length =  1
		"""
		try :
			self._persistmask = persistmask
		except Exception as e:
			raise e

	@property
	def cookiename(self) :
		r"""Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			return self._cookiename
		except Exception as e:
			raise e

	@cookiename.setter
	def cookiename(self, cookiename) :
		r"""Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			self._cookiename = cookiename
		except Exception as e:
			raise e

	@property
	def v6persistmasklen(self) :
		r"""Persistence mask to apply to source IPv6 addresses when creating source IP based persistence sessions.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6persistmasklen
		except Exception as e:
			raise e

	@v6persistmasklen.setter
	def v6persistmasklen(self, v6persistmasklen) :
		r"""Persistence mask to apply to source IPv6 addresses when creating source IP based persistence sessions.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6persistmasklen = v6persistmasklen
		except Exception as e:
			raise e

	@property
	def cookiedomain(self) :
		r"""Domain attribute for the HTTP cookie.<br/>Minimum length =  1.
		"""
		try :
			return self._cookiedomain
		except Exception as e:
			raise e

	@cookiedomain.setter
	def cookiedomain(self, cookiedomain) :
		r"""Domain attribute for the HTTP cookie.<br/>Minimum length =  1
		"""
		try :
			self._cookiedomain = cookiedomain
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		r"""Time period for which a persistence session is in effect.<br/>Default value: 2<br/>Maximum length =  1440
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "None".
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		r"""Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.
		Note:
		Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
		The following requirements apply only to the NetScaler CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "None"
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def usevserverpersistency(self) :
		r""".<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usevserverpersistency
		except Exception as e:
			raise e

	@usevserverpersistency.setter
	def usevserverpersistency(self, usevserverpersistency) :
		r""".<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usevserverpersistency = usevserverpersistency
		except Exception as e:
			raise e

	@property
	def mastervserver(self) :
		try :
			return self._mastervserver
		except Exception as e:
			raise e

	@mastervserver.setter
	def mastervserver(self, mastervserver) :
		try :
			self._mastervserver = mastervserver
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the load balancing virtual server group.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the load balancing virtual server group.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbgroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbgroup
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
	def add(cls, client, resource) :
		r""" Use this API to add lbgroup.
		"""
		try :
			if type(resource) is not list :
				addresource = lbgroup()
				addresource.name = resource.name
				addresource.persistencetype = resource.persistencetype
				addresource.persistencebackup = resource.persistencebackup
				addresource.backuppersistencetimeout = resource.backuppersistencetimeout
				addresource.persistmask = resource.persistmask
				addresource.cookiename = resource.cookiename
				addresource.v6persistmasklen = resource.v6persistmasklen
				addresource.cookiedomain = resource.cookiedomain
				addresource.timeout = resource.timeout
				addresource.rule = resource.rule
				addresource.usevserverpersistency = resource.usevserverpersistency
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].persistencetype = resource[i].persistencetype
						addresources[i].persistencebackup = resource[i].persistencebackup
						addresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
						addresources[i].persistmask = resource[i].persistmask
						addresources[i].cookiename = resource[i].cookiename
						addresources[i].v6persistmasklen = resource[i].v6persistmasklen
						addresources[i].cookiedomain = resource[i].cookiedomain
						addresources[i].timeout = resource[i].timeout
						addresources[i].rule = resource[i].rule
						addresources[i].usevserverpersistency = resource[i].usevserverpersistency
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lbgroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbgroup()
				updateresource.name = resource.name
				updateresource.persistencetype = resource.persistencetype
				updateresource.persistencebackup = resource.persistencebackup
				updateresource.backuppersistencetimeout = resource.backuppersistencetimeout
				updateresource.persistmask = resource.persistmask
				updateresource.cookiename = resource.cookiename
				updateresource.v6persistmasklen = resource.v6persistmasklen
				updateresource.cookiedomain = resource.cookiedomain
				updateresource.timeout = resource.timeout
				updateresource.rule = resource.rule
				updateresource.usevserverpersistency = resource.usevserverpersistency
				updateresource.mastervserver = resource.mastervserver
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbgroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].persistencetype = resource[i].persistencetype
						updateresources[i].persistencebackup = resource[i].persistencebackup
						updateresources[i].backuppersistencetimeout = resource[i].backuppersistencetimeout
						updateresources[i].persistmask = resource[i].persistmask
						updateresources[i].cookiename = resource[i].cookiename
						updateresources[i].v6persistmasklen = resource[i].v6persistmasklen
						updateresources[i].cookiedomain = resource[i].cookiedomain
						updateresources[i].timeout = resource[i].timeout
						updateresources[i].rule = resource[i].rule
						updateresources[i].usevserverpersistency = resource[i].usevserverpersistency
						updateresources[i].mastervserver = resource[i].mastervserver
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lbgroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbgroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lbgroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbgroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbgroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a lbgroup resource.
		"""
		try :
			renameresource = lbgroup()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbgroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbgroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lbgroup()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lbgroup() for _ in range(len(name))]
						obj = [lbgroup() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lbgroup()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lbgroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbgroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lbgroup resources configured on NetScaler.
		"""
		try :
			obj = lbgroup()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of lbgroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbgroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Usevserverpersistency:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Persistencebackup:
		SOURCEIP = "SOURCEIP"
		NONE = "NONE"

	class Persistencetype:
		SOURCEIP = "SOURCEIP"
		COOKIEINSERT = "COOKIEINSERT"
		RULE = "RULE"
		NONE = "NONE"

class lbgroup_response(base_response) :
	def __init__(self, length=1) :
		self.lbgroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbgroup = [lbgroup() for _ in range(length)]

