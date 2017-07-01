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

class authenticationtacacsaction(base_resource) :
	""" Configuration for TACACS action resource. """
	def __init__(self) :
		self._name = None
		self._serverip = None
		self._serverport = None
		self._authtimeout = None
		self._tacacssecret = None
		self._authorization = None
		self._accounting = None
		self._auditfailedcmds = None
		self._groupattrname = None
		self._defaultauthenticationgroup = None
		self._attribute1 = None
		self._attribute2 = None
		self._attribute3 = None
		self._attribute4 = None
		self._attribute5 = None
		self._attribute6 = None
		self._attribute7 = None
		self._attribute8 = None
		self._attribute9 = None
		self._attribute10 = None
		self._attribute11 = None
		self._attribute12 = None
		self._attribute13 = None
		self._attribute14 = None
		self._attribute15 = None
		self._attribute16 = None
		self._success = None
		self._failure = None
		self.___count = 0

	@property
	def name(self) :
		r"""Name for the TACACS+ profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after TACACS profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'y authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the TACACS+ profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after TACACS profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'y authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		r"""IP address assigned to the TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address assigned to the TACACS+ server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port number on which the TACACS+ server listens for connections.<br/>Default value: 49<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def authtimeout(self) :
		r"""Number of seconds the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1.
		"""
		try :
			return self._authtimeout
		except Exception as e:
			raise e

	@authtimeout.setter
	def authtimeout(self, authtimeout) :
		r"""Number of seconds the NetScaler appliance waits for a response from the TACACS+ server.<br/>Default value: 3<br/>Minimum length =  1
		"""
		try :
			self._authtimeout = authtimeout
		except Exception as e:
			raise e

	@property
	def tacacssecret(self) :
		r"""Key shared between the TACACS+ server and the NetScaler appliance. 
		Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1.
		"""
		try :
			return self._tacacssecret
		except Exception as e:
			raise e

	@tacacssecret.setter
	def tacacssecret(self, tacacssecret) :
		r"""Key shared between the TACACS+ server and the NetScaler appliance. 
		Required for allowing the NetScaler appliance to communicate with the TACACS+ server.<br/>Minimum length =  1
		"""
		try :
			self._tacacssecret = tacacssecret
		except Exception as e:
			raise e

	@property
	def authorization(self) :
		r"""Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._authorization
		except Exception as e:
			raise e

	@authorization.setter
	def authorization(self, authorization) :
		r"""Use streaming authorization on the TACACS+ server.<br/>Possible values = ON, OFF
		"""
		try :
			self._authorization = authorization
		except Exception as e:
			raise e

	@property
	def accounting(self) :
		r"""Whether the TACACS+ server is currently accepting accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._accounting
		except Exception as e:
			raise e

	@accounting.setter
	def accounting(self, accounting) :
		r"""Whether the TACACS+ server is currently accepting accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._accounting = accounting
		except Exception as e:
			raise e

	@property
	def auditfailedcmds(self) :
		r"""The state of the TACACS+ server that will receive accounting messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._auditfailedcmds
		except Exception as e:
			raise e

	@auditfailedcmds.setter
	def auditfailedcmds(self, auditfailedcmds) :
		r"""The state of the TACACS+ server that will receive accounting messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._auditfailedcmds = auditfailedcmds
		except Exception as e:
			raise e

	@property
	def groupattrname(self) :
		r"""TACACS+ group attribute name.
		Used for group extraction on the TACACS+ server.
		"""
		try :
			return self._groupattrname
		except Exception as e:
			raise e

	@groupattrname.setter
	def groupattrname(self, groupattrname) :
		r"""TACACS+ group attribute name.
		Used for group extraction on the TACACS+ server.
		"""
		try :
			self._groupattrname = groupattrname
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '1' (where '1' changes for each attribute).
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		r"""Name of the custom attribute to be extracted from server and stored at index '1' (where '1' changes for each attribute).
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '2' (where '2' changes for each attribute).
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		r"""Name of the custom attribute to be extracted from server and stored at index '2' (where '2' changes for each attribute).
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '3' (where '3' changes for each attribute).
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		r"""Name of the custom attribute to be extracted from server and stored at index '3' (where '3' changes for each attribute).
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '4' (where '4' changes for each attribute).
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		r"""Name of the custom attribute to be extracted from server and stored at index '4' (where '4' changes for each attribute).
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '5' (where '5' changes for each attribute).
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		r"""Name of the custom attribute to be extracted from server and stored at index '5' (where '5' changes for each attribute).
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '6' (where '6' changes for each attribute).
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		r"""Name of the custom attribute to be extracted from server and stored at index '6' (where '6' changes for each attribute).
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '7' (where '7' changes for each attribute).
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		r"""Name of the custom attribute to be extracted from server and stored at index '7' (where '7' changes for each attribute).
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '8' (where '8' changes for each attribute).
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		r"""Name of the custom attribute to be extracted from server and stored at index '8' (where '8' changes for each attribute).
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '9' (where '9' changes for each attribute).
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		r"""Name of the custom attribute to be extracted from server and stored at index '9' (where '9' changes for each attribute).
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '10' (where '10' changes for each attribute).
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		r"""Name of the custom attribute to be extracted from server and stored at index '10' (where '10' changes for each attribute).
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '11' (where '11' changes for each attribute).
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		r"""Name of the custom attribute to be extracted from server and stored at index '11' (where '11' changes for each attribute).
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '12' (where '12' changes for each attribute).
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		r"""Name of the custom attribute to be extracted from server and stored at index '12' (where '12' changes for each attribute).
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '13' (where '13' changes for each attribute).
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		r"""Name of the custom attribute to be extracted from server and stored at index '13' (where '13' changes for each attribute).
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '14' (where '14' changes for each attribute).
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		r"""Name of the custom attribute to be extracted from server and stored at index '14' (where '14' changes for each attribute).
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '15' (where '15' changes for each attribute).
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		r"""Name of the custom attribute to be extracted from server and stored at index '15' (where '15' changes for each attribute).
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		r"""Name of the custom attribute to be extracted from server and stored at index '16' (where '16' changes for each attribute).
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		r"""Name of the custom attribute to be extracted from server and stored at index '16' (where '16' changes for each attribute).
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def success(self) :
		try :
			return self._success
		except Exception as e:
			raise e

	@property
	def failure(self) :
		try :
			return self._failure
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationtacacsaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationtacacsaction
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
		r""" Use this API to add authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationtacacsaction()
				addresource.name = resource.name
				addresource.serverip = resource.serverip
				addresource.serverport = resource.serverport
				addresource.authtimeout = resource.authtimeout
				addresource.tacacssecret = resource.tacacssecret
				addresource.authorization = resource.authorization
				addresource.accounting = resource.accounting
				addresource.auditfailedcmds = resource.auditfailedcmds
				addresource.groupattrname = resource.groupattrname
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.attribute1 = resource.attribute1
				addresource.attribute2 = resource.attribute2
				addresource.attribute3 = resource.attribute3
				addresource.attribute4 = resource.attribute4
				addresource.attribute5 = resource.attribute5
				addresource.attribute6 = resource.attribute6
				addresource.attribute7 = resource.attribute7
				addresource.attribute8 = resource.attribute8
				addresource.attribute9 = resource.attribute9
				addresource.attribute10 = resource.attribute10
				addresource.attribute11 = resource.attribute11
				addresource.attribute12 = resource.attribute12
				addresource.attribute13 = resource.attribute13
				addresource.attribute14 = resource.attribute14
				addresource.attribute15 = resource.attribute15
				addresource.attribute16 = resource.attribute16
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationtacacsaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].serverip = resource[i].serverip
						addresources[i].serverport = resource[i].serverport
						addresources[i].authtimeout = resource[i].authtimeout
						addresources[i].tacacssecret = resource[i].tacacssecret
						addresources[i].authorization = resource[i].authorization
						addresources[i].accounting = resource[i].accounting
						addresources[i].auditfailedcmds = resource[i].auditfailedcmds
						addresources[i].groupattrname = resource[i].groupattrname
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute16 = resource[i].attribute16
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationtacacsaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationtacacsaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationtacacsaction()
				updateresource.name = resource.name
				updateresource.serverip = resource.serverip
				updateresource.serverport = resource.serverport
				updateresource.authtimeout = resource.authtimeout
				updateresource.tacacssecret = resource.tacacssecret
				updateresource.authorization = resource.authorization
				updateresource.accounting = resource.accounting
				updateresource.auditfailedcmds = resource.auditfailedcmds
				updateresource.groupattrname = resource.groupattrname
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute16 = resource.attribute16
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationtacacsaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].serverip = resource[i].serverip
						updateresources[i].serverport = resource[i].serverport
						updateresources[i].authtimeout = resource[i].authtimeout
						updateresources[i].tacacssecret = resource[i].tacacssecret
						updateresources[i].authorization = resource[i].authorization
						updateresources[i].accounting = resource[i].accounting
						updateresources[i].auditfailedcmds = resource[i].auditfailedcmds
						updateresources[i].groupattrname = resource[i].groupattrname
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute16 = resource[i].attribute16
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationtacacsaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationtacacsaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationtacacsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationtacacsaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationtacacsaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationtacacsaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationtacacsaction() for _ in range(len(name))]
						obj = [authenticationtacacsaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationtacacsaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationtacacsaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationtacacsaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationtacacsaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationtacacsaction()
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
		r""" Use this API to count filtered the set of authenticationtacacsaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationtacacsaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Auditfailedcmds:
		ON = "ON"
		OFF = "OFF"

	class Authorization:
		ON = "ON"
		OFF = "OFF"

	class Accounting:
		ON = "ON"
		OFF = "OFF"

class authenticationtacacsaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationtacacsaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationtacacsaction = [authenticationtacacsaction() for _ in range(length)]

