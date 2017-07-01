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

class dnssubnetcache(base_resource) :
	""" Configuration for subnet cache resource. """
	def __init__(self) :
		self._ecssubnet = None
		self._all = None
		self._nodeid = None
		self._hostname = None
		self._nextrecs = []
		self.___count = 0

	@property
	def ecssubnet(self) :
		r"""ECS Subnet.
		"""
		try :
			return self._ecssubnet
		except Exception as e:
			raise e

	@ecssubnet.setter
	def ecssubnet(self, ecssubnet) :
		r"""ECS Subnet.
		"""
		try :
			self._ecssubnet = ecssubnet
		except Exception as e:
			raise e

	@property
	def all(self) :
		r"""Flush all the ECS subnets from the DNS cache.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Flush all the ECS subnets from the DNS cache.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def hostname(self) :
		r"""Domain name.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@property
	def nextrecs(self) :
		r"""An array of record types associated with the domain name.<br/>Possible values = A, NS, CNAME, SOA, MX, AAAA, SRV, RRSIG, NSEC, DNSKEY, PTR, TXT, NAPTR.
		"""
		try :
			return self._nextrecs
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnssubnetcache_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnssubnetcache
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ecssubnet is not None :
				return str(self.ecssubnet)
			return None
		except Exception as e :
			raise e



	@classmethod
	def flush(cls, client, resource) :
		r""" Use this API to flush dnssubnetcache.
		"""
		try :
			if type(resource) is not list :
				flushresource = dnssubnetcache()
				flushresource.ecssubnet = resource.ecssubnet
				flushresource.all = resource.all
				return flushresource.perform_operation(client,"flush")
			else :
				if (resource and len(resource) > 0) :
					flushresources = [ dnssubnetcache() for _ in range(len(resource))]
					for i in range(len(resource)) :
						flushresources[i].ecssubnet = resource[i].ecssubnet
						flushresources[i].all = resource[i].all
				result = cls.perform_operation_bulk_request(client, flushresources,"flush")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnssubnetcache resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnssubnetcache()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnssubnetcache()
					obj.ecssubnet = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnssubnetcache() for _ in range(len(name))]
						obj = [dnssubnetcache() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnssubnetcache()
							obj[i].ecssubnet = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the dnssubnetcache resources that are configured on netscaler.
	# This uses dnssubnetcache_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnssubnetcache()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnssubnetcache resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssubnetcache()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnssubnetcache resources configured on NetScaler.
		"""
		try :
			obj = dnssubnetcache()
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
		r""" Use this API to count filtered the set of dnssubnetcache resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnssubnetcache()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Nextrecs:
		A = "A"
		NS = "NS"
		CNAME = "CNAME"
		SOA = "SOA"
		MX = "MX"
		AAAA = "AAAA"
		SRV = "SRV"
		RRSIG = "RRSIG"
		NSEC = "NSEC"
		DNSKEY = "DNSKEY"
		PTR = "PTR"
		TXT = "TXT"
		NAPTR = "NAPTR"

class dnssubnetcache_response(base_response) :
	def __init__(self, length=1) :
		self.dnssubnetcache = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnssubnetcache = [dnssubnetcache() for _ in range(length)]

