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

class lbprofile(base_resource) :
	""" Configuration for LB profile resource. """
	def __init__(self) :
		self._lbprofilename = None
		self._dbslb = None
		self._processlocal = None
		self._httponlycookieflag = None
		self._cookiepassphrase = None
		self._usesecuredpersistencecookie = None
		self._useencryptedpersistencecookie = None
		self._vsvrcount = None
		self.___count = 0

	@property
	def lbprofilename(self) :
		r"""Name of the LB profile.<br/>Minimum length =  1.
		"""
		try :
			return self._lbprofilename
		except Exception as e:
			raise e

	@lbprofilename.setter
	def lbprofilename(self, lbprofilename) :
		r"""Name of the LB profile.<br/>Minimum length =  1
		"""
		try :
			self._lbprofilename = lbprofilename
		except Exception as e:
			raise e

	@property
	def dbslb(self) :
		r"""Enable database specific load balancing for MySQL and MSSQL service types.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dbslb
		except Exception as e:
			raise e

	@dbslb.setter
	def dbslb(self, dbslb) :
		r"""Enable database specific load balancing for MySQL and MSSQL service types.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dbslb = dbslb
		except Exception as e:
			raise e

	@property
	def processlocal(self) :
		r"""By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single pa
		cket request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._processlocal
		except Exception as e:
			raise e

	@processlocal.setter
	def processlocal(self, processlocal) :
		r"""By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single pa
		cket request response mode or when the upstream device is performing a proper RSS for connection based distribution.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._processlocal = processlocal
		except Exception as e:
			raise e

	@property
	def httponlycookieflag(self) :
		r"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httponlycookieflag
		except Exception as e:
			raise e

	@httponlycookieflag.setter
	def httponlycookieflag(self, httponlycookieflag) :
		r"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httponlycookieflag = httponlycookieflag
		except Exception as e:
			raise e

	@property
	def cookiepassphrase(self) :
		r"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			return self._cookiepassphrase
		except Exception as e:
			raise e

	@cookiepassphrase.setter
	def cookiepassphrase(self, cookiepassphrase) :
		r"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			self._cookiepassphrase = cookiepassphrase
		except Exception as e:
			raise e

	@property
	def usesecuredpersistencecookie(self) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usesecuredpersistencecookie
		except Exception as e:
			raise e

	@usesecuredpersistencecookie.setter
	def usesecuredpersistencecookie(self, usesecuredpersistencecookie) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usesecuredpersistencecookie = usesecuredpersistencecookie
		except Exception as e:
			raise e

	@property
	def useencryptedpersistencecookie(self) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._useencryptedpersistencecookie
		except Exception as e:
			raise e

	@useencryptedpersistencecookie.setter
	def useencryptedpersistencecookie(self, useencryptedpersistencecookie) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._useencryptedpersistencecookie = useencryptedpersistencecookie
		except Exception as e:
			raise e

	@property
	def vsvrcount(self) :
		r"""Total number of vservers , the profile is bound to.
		"""
		try :
			return self._vsvrcount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.lbprofilename is not None :
				return str(self.lbprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lbprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = lbprofile()
				addresource.lbprofilename = resource.lbprofilename
				addresource.dbslb = resource.dbslb
				addresource.processlocal = resource.processlocal
				addresource.httponlycookieflag = resource.httponlycookieflag
				addresource.cookiepassphrase = resource.cookiepassphrase
				addresource.usesecuredpersistencecookie = resource.usesecuredpersistencecookie
				addresource.useencryptedpersistencecookie = resource.useencryptedpersistencecookie
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].lbprofilename = resource[i].lbprofilename
						addresources[i].dbslb = resource[i].dbslb
						addresources[i].processlocal = resource[i].processlocal
						addresources[i].httponlycookieflag = resource[i].httponlycookieflag
						addresources[i].cookiepassphrase = resource[i].cookiepassphrase
						addresources[i].usesecuredpersistencecookie = resource[i].usesecuredpersistencecookie
						addresources[i].useencryptedpersistencecookie = resource[i].useencryptedpersistencecookie
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lbprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.lbprofilename = resource
				else :
					deleteresource.lbprofilename = resource.lbprofilename
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].lbprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].lbprofilename = resource[i].lbprofilename
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lbprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = lbprofile()
				updateresource.lbprofilename = resource.lbprofilename
				updateresource.dbslb = resource.dbslb
				updateresource.processlocal = resource.processlocal
				updateresource.httponlycookieflag = resource.httponlycookieflag
				updateresource.cookiepassphrase = resource.cookiepassphrase
				updateresource.usesecuredpersistencecookie = resource.usesecuredpersistencecookie
				updateresource.useencryptedpersistencecookie = resource.useencryptedpersistencecookie
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].lbprofilename = resource[i].lbprofilename
						updateresources[i].dbslb = resource[i].dbslb
						updateresources[i].processlocal = resource[i].processlocal
						updateresources[i].httponlycookieflag = resource[i].httponlycookieflag
						updateresources[i].cookiepassphrase = resource[i].cookiepassphrase
						updateresources[i].usesecuredpersistencecookie = resource[i].usesecuredpersistencecookie
						updateresources[i].useencryptedpersistencecookie = resource[i].useencryptedpersistencecookie
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lbprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.lbprofilename = resource
				else :
					unsetresource.lbprofilename = resource.lbprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].lbprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].lbprofilename = resource[i].lbprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lbprofile()
					obj.lbprofilename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lbprofile() for _ in range(len(name))]
						obj = [lbprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lbprofile()
							obj[i].lbprofilename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lbprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lbprofile resources configured on NetScaler.
		"""
		try :
			obj = lbprofile()
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
		r""" Use this API to count filtered the set of lbprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Usesecuredpersistencecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httponlycookieflag:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dbslb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Processlocal:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Useencryptedpersistencecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lbprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lbprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbprofile = [lbprofile() for _ in range(length)]

