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


class cacheobject_args :
	r""" Provides additional arguments required for fetching the cacheobject resource.
	"""
	def __init__(self) :
		self._url = None
		self._locator = None
		self._httpstatus = None
		self._host = None
		self._port = None
		self._groupname = None
		self._httpmethod = None
		self._group = None
		self._ignoremarkerobjects = None
		self._includenotreadyobjects = None
		self._nodeid = None

	@property
	def url(self) :
		r"""URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def locator(self) :
		r"""ID of the cached object.
		"""
		try :
			return self._locator
		except Exception as e:
			raise e

	@locator.setter
	def locator(self, locator) :
		r"""ID of the cached object.
		"""
		try :
			self._locator = locator
		except Exception as e:
			raise e

	@property
	def httpstatus(self) :
		r"""HTTP status of the object.
		"""
		try :
			return self._httpstatus
		except Exception as e:
			raise e

	@httpstatus.setter
	def httpstatus(self, httpstatus) :
		r"""HTTP status of the object.
		"""
		try :
			self._httpstatus = httpstatus
		except Exception as e:
			raise e

	@property
	def host(self) :
		r"""Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@host.setter
	def host(self, host) :
		r"""Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1
		"""
		try :
			self._host = host
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum value =  1.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum value =  1
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def groupname(self) :
		r"""Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter.
		"""
		try :
			return self._groupname
		except Exception as e:
			raise e

	@groupname.setter
	def groupname(self, groupname) :
		r"""Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter.
		"""
		try :
			self._groupname = groupname
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def group(self) :
		r"""Name of the content group whose objects should be listed.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		r"""Name of the content group whose objects should be listed.
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

	@property
	def ignoremarkerobjects(self) :
		r"""Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._ignoremarkerobjects
		except Exception as e:
			raise e

	@ignoremarkerobjects.setter
	def ignoremarkerobjects(self, ignoremarkerobjects) :
		r"""Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF
		"""
		try :
			self._ignoremarkerobjects = ignoremarkerobjects
		except Exception as e:
			raise e

	@property
	def includenotreadyobjects(self) :
		r"""Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._includenotreadyobjects
		except Exception as e:
			raise e

	@includenotreadyobjects.setter
	def includenotreadyobjects(self, includenotreadyobjects) :
		r"""Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF
		"""
		try :
			self._includenotreadyobjects = includenotreadyobjects
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	class Includenotreadyobjects:
		ON = "ON"
		OFF = "OFF"

	class Httpmethod:
		GET = "GET"
		POST = "POST"

	class Ignoremarkerobjects:
		ON = "ON"
		OFF = "OFF"

