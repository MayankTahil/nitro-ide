'''
Copyright (c) 2008-2015 Citrix Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from massrc.com.citrix.mas.nitro.resource.Base import *
from massrc.com.citrix.mas.nitro.service.options import options
from massrc.com.citrix.mas.nitro.exception.nitro_exception import nitro_exception
from massrc.com.citrix.mas.nitro.util.filtervalue import filtervalue
from massrc.com.citrix.mas.nitro.resource.Base.base_resource import base_resource
from massrc.com.citrix.mas.nitro.resource.Base.base_response import base_response


'''
Configuration for HAProxy frontend stats information resource
'''

class haproxy_frontend_stats(base_resource):
	_req_rate= ""
	_bin= ""
	_hrsp_1xx= ""
	_bout= ""
	_hrsp_other= ""
	_ereq= ""
	_dresp= ""
	_req_tot= ""
	_scur= ""
	_id= ""
	_eresp= ""
	_hrsp_2xx= ""
	_dreq= ""
	_frontend_id= ""
	_svname= ""
	_hrsp_4xx= ""
	_hrsp_3xx= ""
	_stot= ""
	_hrsp_5xx= ""
	__count=""
	'''
	get the resource id
	'''
	def get_resource_id(self) :
		try:
			if hasattr(self, 'id'):
				return self.id 
			else:
				return None 
		except Exception as e :
			raise e

	'''
	get the resource type
	'''
	def get_object_type(self) :
		try:
			return "haproxy_frontend_stats"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return self._id
		except Exception as e :
			raise e

	'''
	Returns the value of object file path argument.
	'''
	@property
	def file_path_value(self) :
		try:
			return None
		except Exception as e :
			raise e

	'''
	Returns the value of object file component name.
	'''
	@property
	def file_component_value(self) :
		try :
			return "haproxy_frontend_statss"
		except Exception as e :
			raise e



	'''
	get HTTP Reqrate/Sec
	'''
	@property
	def req_rate(self) :
		try:
			return self._req_rate
		except Exception as e :
			raise e


	'''
	get Bytes of date in
	'''
	@property
	def bin(self) :
		try:
			return self._bin
		except Exception as e :
			raise e
	'''
	set Bytes of date in
	'''
	@bin.setter
	def bin(self,bin):
		try :
			if not isinstance(bin,long):
				raise TypeError("bin must be set to long value")
			self._bin = bin
		except Exception as e :
			raise e


	'''
	get No of request with response code 1XX
	'''
	@property
	def hrsp_1xx(self) :
		try:
			return self._hrsp_1xx
		except Exception as e :
			raise e
	'''
	set No of request with response code 1XX
	'''
	@hrsp_1xx.setter
	def hrsp_1xx(self,hrsp_1xx):
		try :
			if not isinstance(hrsp_1xx,long):
				raise TypeError("hrsp_1xx must be set to long value")
			self._hrsp_1xx = hrsp_1xx
		except Exception as e :
			raise e


	'''
	get Bytes of data out
	'''
	@property
	def bout(self) :
		try:
			return self._bout
		except Exception as e :
			raise e
	'''
	set Bytes of data out
	'''
	@bout.setter
	def bout(self,bout):
		try :
			if not isinstance(bout,long):
				raise TypeError("bout must be set to long value")
			self._bout = bout
		except Exception as e :
			raise e


	'''
	get No of request with other response code
	'''
	@property
	def hrsp_other(self) :
		try:
			return self._hrsp_other
		except Exception as e :
			raise e
	'''
	set No of request with other response code
	'''
	@hrsp_other.setter
	def hrsp_other(self,hrsp_other):
		try :
			if not isinstance(hrsp_other,long):
				raise TypeError("hrsp_other must be set to long value")
			self._hrsp_other = hrsp_other
		except Exception as e :
			raise e


	'''
	get Number of error requests
	'''
	@property
	def ereq(self) :
		try:
			return self._ereq
		except Exception as e :
			raise e


	'''
	get No of response denied
	'''
	@property
	def dresp(self) :
		try:
			return self._dresp
		except Exception as e :
			raise e
	'''
	set No of response denied
	'''
	@dresp.setter
	def dresp(self,dresp):
		try :
			if not isinstance(dresp,long):
				raise TypeError("dresp must be set to long value")
			self._dresp = dresp
		except Exception as e :
			raise e


	'''
	get Total number of requests
	'''
	@property
	def req_tot(self) :
		try:
			return self._req_tot
		except Exception as e :
			raise e


	'''
	get Current Session
	'''
	@property
	def scur(self) :
		try:
			return self._scur
		except Exception as e :
			raise e
	'''
	set Current Session
	'''
	@scur.setter
	def scur(self,scur):
		try :
			if not isinstance(scur,long):
				raise TypeError("scur must be set to long value")
			self._scur = scur
		except Exception as e :
			raise e


	'''
	get Id is system generated key
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key
	'''
	@id.setter
	def id(self,id):
		try :
			if not isinstance(id,str):
				raise TypeError("id must be set to str value")
			self._id = id
		except Exception as e :
			raise e


	'''
	get Number of error responses
	'''
	@property
	def eresp(self) :
		try:
			return self._eresp
		except Exception as e :
			raise e


	'''
	get No of request with response code 2XX
	'''
	@property
	def hrsp_2xx(self) :
		try:
			return self._hrsp_2xx
		except Exception as e :
			raise e
	'''
	set No of request with response code 2XX
	'''
	@hrsp_2xx.setter
	def hrsp_2xx(self,hrsp_2xx):
		try :
			if not isinstance(hrsp_2xx,long):
				raise TypeError("hrsp_2xx must be set to long value")
			self._hrsp_2xx = hrsp_2xx
		except Exception as e :
			raise e


	'''
	get No of denied requests
	'''
	@property
	def dreq(self) :
		try:
			return self._dreq
		except Exception as e :
			raise e
	'''
	set No of denied requests
	'''
	@dreq.setter
	def dreq(self,dreq):
		try :
			if not isinstance(dreq,long):
				raise TypeError("dreq must be set to long value")
			self._dreq = dreq
		except Exception as e :
			raise e


	'''
	get Frontend ID
	'''
	@property
	def frontend_id(self) :
		try:
			return self._frontend_id
		except Exception as e :
			raise e
	'''
	set Frontend ID
	'''
	@frontend_id.setter
	def frontend_id(self,frontend_id):
		try :
			if not isinstance(frontend_id,str):
				raise TypeError("frontend_id must be set to str value")
			self._frontend_id = frontend_id
		except Exception as e :
			raise e


	'''
	get Service Name
	'''
	@property
	def svname(self) :
		try:
			return self._svname
		except Exception as e :
			raise e
	'''
	set Service Name
	'''
	@svname.setter
	def svname(self,svname):
		try :
			if not isinstance(svname,str):
				raise TypeError("svname must be set to str value")
			self._svname = svname
		except Exception as e :
			raise e


	'''
	get No of request with response code 4XX
	'''
	@property
	def hrsp_4xx(self) :
		try:
			return self._hrsp_4xx
		except Exception as e :
			raise e
	'''
	set No of request with response code 4XX
	'''
	@hrsp_4xx.setter
	def hrsp_4xx(self,hrsp_4xx):
		try :
			if not isinstance(hrsp_4xx,long):
				raise TypeError("hrsp_4xx must be set to long value")
			self._hrsp_4xx = hrsp_4xx
		except Exception as e :
			raise e


	'''
	get No of request with response code 3XX
	'''
	@property
	def hrsp_3xx(self) :
		try:
			return self._hrsp_3xx
		except Exception as e :
			raise e
	'''
	set No of request with response code 3XX
	'''
	@hrsp_3xx.setter
	def hrsp_3xx(self,hrsp_3xx):
		try :
			if not isinstance(hrsp_3xx,long):
				raise TypeError("hrsp_3xx must be set to long value")
			self._hrsp_3xx = hrsp_3xx
		except Exception as e :
			raise e


	'''
	get Total number of sessions
	'''
	@property
	def stot(self) :
		try:
			return self._stot
		except Exception as e :
			raise e


	'''
	get No of request with response code 5XX
	'''
	@property
	def hrsp_5xx(self) :
		try:
			return self._hrsp_5xx
		except Exception as e :
			raise e
	'''
	set No of request with response code 5XX
	'''
	@hrsp_5xx.setter
	def hrsp_5xx(self,hrsp_5xx):
		try :
			if not isinstance(hrsp_5xx,long):
				raise TypeError("hrsp_5xx must be set to long value")
			self._hrsp_5xx = hrsp_5xx
		except Exception as e :
			raise e

	'''
	Operation to get HAProxy frontend stats..
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				haproxy_frontend_stats_obj=haproxy_frontend_stats()
				response = haproxy_frontend_stats_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of haproxy_frontend_stats resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			haproxy_frontend_stats_obj = haproxy_frontend_stats()
			option_ = options()
			option_._filter=filter_
			return haproxy_frontend_stats_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the haproxy_frontend_stats resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			haproxy_frontend_stats_obj = haproxy_frontend_stats()
			option_ = options()
			option_._count=True
			response = haproxy_frontend_stats_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of haproxy_frontend_stats resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			haproxy_frontend_stats_obj = haproxy_frontend_stats()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = haproxy_frontend_stats_obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['_count']
			return 0;
		except Exception as e :
			raise e

	'''
	Converts API response into object and returns the object array in case of get request.
	'''
	def get_nitro_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxy_frontend_stats_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.haproxy_frontend_stats
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(haproxy_frontend_stats_responses, response, "haproxy_frontend_stats_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.haproxy_frontend_stats_response_array
				i=0
				error = [haproxy_frontend_stats() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.haproxy_frontend_stats_response_array
			i=0
			haproxy_frontend_stats_objs = [haproxy_frontend_stats() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_haproxy_frontend_stats'):
					for props in obj._haproxy_frontend_stats:
						result = service.payload_formatter.string_to_bulk_resource(haproxy_frontend_stats_response,self.__class__.__name__,props)
						haproxy_frontend_stats_objs[i] = result.haproxy_frontend_stats
						i=i+1
			return haproxy_frontend_stats_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(haproxy_frontend_stats,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class haproxy_frontend_stats_response(base_response):
	def __init__(self,length=1) :
		self.haproxy_frontend_stats= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.haproxy_frontend_stats= [ haproxy_frontend_stats() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class haproxy_frontend_stats_responses(base_response):
	def __init__(self,length=1) :
		self.haproxy_frontend_stats_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.haproxy_frontend_stats_response_array = [ haproxy_frontend_stats() for _ in range(length)]
