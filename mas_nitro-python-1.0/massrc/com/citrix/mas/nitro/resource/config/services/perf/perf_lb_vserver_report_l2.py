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
Configuration for LBVServer resource
'''

class perf_lb_vserver_report_l2(base_resource):
	_requestbytesrate= ""
	_pktssentrate= ""
	_responsebytesrate= ""
	_curclntconnections= ""
	_svcsurgecount= ""
	_cursrvrconnections= ""
	_vsvrsurgecount= ""
	_device_ip_address= ""
	_vsvrName= ""
	_timestamp= ""
	_totalresponsebytes= ""
	_totalrequestbytes= ""
	_pktsrecvdrate= ""
	_hitsrate= ""
	_surgecount= ""
	_throughput_avg= ""
	_apps_count= ""
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
			return "perf_lb_vserver_report_l2"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return None
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
			return "perf_lb_vserver_report_l2s"
		except Exception as e :
			raise e



	'''
	get requestbytesrate Value
	'''
	@property
	def requestbytesrate(self) :
		try:
			return self._requestbytesrate
		except Exception as e :
			raise e
	'''
	set requestbytesrate Value
	'''
	@requestbytesrate.setter
	def requestbytesrate(self,requestbytesrate):
		try :
			if not isinstance(requestbytesrate,float):
				raise TypeError("requestbytesrate must be set to float value")
			self._requestbytesrate = requestbytesrate
		except Exception as e :
			raise e


	'''
	get pktssentrate Value
	'''
	@property
	def pktssentrate(self) :
		try:
			return self._pktssentrate
		except Exception as e :
			raise e
	'''
	set pktssentrate Value
	'''
	@pktssentrate.setter
	def pktssentrate(self,pktssentrate):
		try :
			if not isinstance(pktssentrate,float):
				raise TypeError("pktssentrate must be set to float value")
			self._pktssentrate = pktssentrate
		except Exception as e :
			raise e


	'''
	get responsebytesrate Value
	'''
	@property
	def responsebytesrate(self) :
		try:
			return self._responsebytesrate
		except Exception as e :
			raise e
	'''
	set responsebytesrate Value
	'''
	@responsebytesrate.setter
	def responsebytesrate(self,responsebytesrate):
		try :
			if not isinstance(responsebytesrate,float):
				raise TypeError("responsebytesrate must be set to float value")
			self._responsebytesrate = responsebytesrate
		except Exception as e :
			raise e


	'''
	get curclntconnections Value
	'''
	@property
	def curclntconnections(self) :
		try:
			return self._curclntconnections
		except Exception as e :
			raise e
	'''
	set curclntconnections Value
	'''
	@curclntconnections.setter
	def curclntconnections(self,curclntconnections):
		try :
			if not isinstance(curclntconnections,float):
				raise TypeError("curclntconnections must be set to float value")
			self._curclntconnections = curclntconnections
		except Exception as e :
			raise e


	'''
	get svcsurgecount Value
	'''
	@property
	def svcsurgecount(self) :
		try:
			return self._svcsurgecount
		except Exception as e :
			raise e
	'''
	set svcsurgecount Value
	'''
	@svcsurgecount.setter
	def svcsurgecount(self,svcsurgecount):
		try :
			if not isinstance(svcsurgecount,float):
				raise TypeError("svcsurgecount must be set to float value")
			self._svcsurgecount = svcsurgecount
		except Exception as e :
			raise e


	'''
	get cursrvrconnections Value
	'''
	@property
	def cursrvrconnections(self) :
		try:
			return self._cursrvrconnections
		except Exception as e :
			raise e
	'''
	set cursrvrconnections Value
	'''
	@cursrvrconnections.setter
	def cursrvrconnections(self,cursrvrconnections):
		try :
			if not isinstance(cursrvrconnections,float):
				raise TypeError("cursrvrconnections must be set to float value")
			self._cursrvrconnections = cursrvrconnections
		except Exception as e :
			raise e


	'''
	get vsvrsurgecount Value
	'''
	@property
	def vsvrsurgecount(self) :
		try:
			return self._vsvrsurgecount
		except Exception as e :
			raise e
	'''
	set vsvrsurgecount Value
	'''
	@vsvrsurgecount.setter
	def vsvrsurgecount(self,vsvrsurgecount):
		try :
			if not isinstance(vsvrsurgecount,float):
				raise TypeError("vsvrsurgecount must be set to float value")
			self._vsvrsurgecount = vsvrsurgecount
		except Exception as e :
			raise e


	'''
	get Device IP Address
	'''
	@property
	def device_ip_address(self) :
		try:
			return self._device_ip_address
		except Exception as e :
			raise e
	'''
	set Device IP Address
	'''
	@device_ip_address.setter
	def device_ip_address(self,device_ip_address):
		try :
			if not isinstance(device_ip_address,str):
				raise TypeError("device_ip_address must be set to str value")
			self._device_ip_address = device_ip_address
		except Exception as e :
			raise e


	'''
	get vsvrName Value
	'''
	@property
	def vsvrName(self) :
		try:
			return self._vsvrName
		except Exception as e :
			raise e
	'''
	set vsvrName Value
	'''
	@vsvrName.setter
	def vsvrName(self,vsvrName):
		try :
			if not isinstance(vsvrName,str):
				raise TypeError("vsvrName must be set to str value")
			self._vsvrName = vsvrName
		except Exception as e :
			raise e


	'''
	get timestamp in milliseconds
	'''
	@property
	def timestamp(self) :
		try:
			return self._timestamp
		except Exception as e :
			raise e
	'''
	set timestamp in milliseconds
	'''
	@timestamp.setter
	def timestamp(self,timestamp):
		try :
			if not isinstance(timestamp,float):
				raise TypeError("timestamp must be set to float value")
			self._timestamp = timestamp
		except Exception as e :
			raise e


	'''
	get Total Response Bytes Value
	'''
	@property
	def totalresponsebytes(self) :
		try:
			return self._totalresponsebytes
		except Exception as e :
			raise e
	'''
	set Total Response Bytes Value
	'''
	@totalresponsebytes.setter
	def totalresponsebytes(self,totalresponsebytes):
		try :
			if not isinstance(totalresponsebytes,float):
				raise TypeError("totalresponsebytes must be set to float value")
			self._totalresponsebytes = totalresponsebytes
		except Exception as e :
			raise e


	'''
	get Total Request Bytes Value
	'''
	@property
	def totalrequestbytes(self) :
		try:
			return self._totalrequestbytes
		except Exception as e :
			raise e
	'''
	set Total Request Bytes Value
	'''
	@totalrequestbytes.setter
	def totalrequestbytes(self,totalrequestbytes):
		try :
			if not isinstance(totalrequestbytes,float):
				raise TypeError("totalrequestbytes must be set to float value")
			self._totalrequestbytes = totalrequestbytes
		except Exception as e :
			raise e


	'''
	get pktsrecvdrate Value
	'''
	@property
	def pktsrecvdrate(self) :
		try:
			return self._pktsrecvdrate
		except Exception as e :
			raise e
	'''
	set pktsrecvdrate Value
	'''
	@pktsrecvdrate.setter
	def pktsrecvdrate(self,pktsrecvdrate):
		try :
			if not isinstance(pktsrecvdrate,float):
				raise TypeError("pktsrecvdrate must be set to float value")
			self._pktsrecvdrate = pktsrecvdrate
		except Exception as e :
			raise e


	'''
	get Hits Rate Value
	'''
	@property
	def hitsrate(self) :
		try:
			return self._hitsrate
		except Exception as e :
			raise e
	'''
	set Hits Rate Value
	'''
	@hitsrate.setter
	def hitsrate(self,hitsrate):
		try :
			if not isinstance(hitsrate,float):
				raise TypeError("hitsrate must be set to float value")
			self._hitsrate = hitsrate
		except Exception as e :
			raise e


	'''
	get surgecount Value
	'''
	@property
	def surgecount(self) :
		try:
			return self._surgecount
		except Exception as e :
			raise e
	'''
	set surgecount Value
	'''
	@surgecount.setter
	def surgecount(self,surgecount):
		try :
			if not isinstance(surgecount,float):
				raise TypeError("surgecount must be set to float value")
			self._surgecount = surgecount
		except Exception as e :
			raise e

	'''
	Average of throughput across all apps which have same IP address and Vserver name
	'''
	@property
	def throughput_avg(self):
		try:
			return self._throughput_avg
		except Exception as e :
			raise e
	'''
	Average of throughput across all apps which have same IP address and Vserver name
	'''
	@throughput_avg.setter
	def throughput_avg(self,throughput_avg):
		try :
			if not isinstance(throughput_avg,float):
				raise TypeError("throughput_avg must be set to float value")
			self._throughput_avg = throughput_avg
		except Exception as e :
			raise e

	'''
	No of apps associated with a LB Vserver
	'''
	@property
	def apps_count(self):
		try:
			return self._apps_count
		except Exception as e :
			raise e
	'''
	No of apps associated with a LB Vserver
	'''
	@apps_count.setter
	def apps_count(self,apps_count):
		try :
			if not isinstance(apps_count,int):
				raise TypeError("apps_count must be set to int value")
			self._apps_count = apps_count
		except Exception as e :
			raise e

	'''
	Use this operation to get LB Vserver Information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				perf_lb_vserver_report_l2_obj=perf_lb_vserver_report_l2()
				response = perf_lb_vserver_report_l2_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of perf_lb_vserver_report_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			perf_lb_vserver_report_l2_obj = perf_lb_vserver_report_l2()
			option_ = options()
			option_._filter=filter_
			return perf_lb_vserver_report_l2_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the perf_lb_vserver_report_l2 resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			perf_lb_vserver_report_l2_obj = perf_lb_vserver_report_l2()
			option_ = options()
			option_._count=True
			response = perf_lb_vserver_report_l2_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of perf_lb_vserver_report_l2 resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			perf_lb_vserver_report_l2_obj = perf_lb_vserver_report_l2()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = perf_lb_vserver_report_l2_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(perf_lb_vserver_report_l2_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.perf_lb_vserver_report_l2
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(perf_lb_vserver_report_l2_responses, response, "perf_lb_vserver_report_l2_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.perf_lb_vserver_report_l2_response_array
				i=0
				error = [perf_lb_vserver_report_l2() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.perf_lb_vserver_report_l2_response_array
			i=0
			perf_lb_vserver_report_l2_objs = [perf_lb_vserver_report_l2() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_perf_lb_vserver_report_l2'):
					for props in obj._perf_lb_vserver_report_l2:
						result = service.payload_formatter.string_to_bulk_resource(perf_lb_vserver_report_l2_response,self.__class__.__name__,props)
						perf_lb_vserver_report_l2_objs[i] = result.perf_lb_vserver_report_l2
						i=i+1
			return perf_lb_vserver_report_l2_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(perf_lb_vserver_report_l2,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class perf_lb_vserver_report_l2_response(base_response):
	def __init__(self,length=1) :
		self.perf_lb_vserver_report_l2= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.perf_lb_vserver_report_l2= [ perf_lb_vserver_report_l2() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class perf_lb_vserver_report_l2_responses(base_response):
	def __init__(self,length=1) :
		self.perf_lb_vserver_report_l2_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.perf_lb_vserver_report_l2_response_array = [ perf_lb_vserver_report_l2() for _ in range(length)]
