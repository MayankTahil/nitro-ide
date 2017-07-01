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
Configuration for MAS License Information resource
'''

class mas_license(base_resource):
	_cpx_lic= ""
	_max_vips= ""
	_analytics= ""
	_adv_analytics= ""
	_perf= ""
	_node_id= ""
	_vpx_lic= ""
	_max_tp_vservers= ""
	_syslog= ""
	_id= ""
	_rpt_sampletime= ""
	_pooled_lic= ""
	_snmp_traps= ""
	_total_managed_vips= ""
	_total_managed_tp_vservers= ""
	_total_allowed_tp_vservers= ""
	_total_discovered_vips= ""
	_total_allowed_vips= ""
	_total_discovered_tp_vservers= ""
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
			return "mas_license"
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
			return "mas_licenses"
		except Exception as e :
			raise e



	'''
	get CPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def cpx_lic(self) :
		try:
			return self._cpx_lic
		except Exception as e :
			raise e
	'''
	set CPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@cpx_lic.setter
	def cpx_lic(self,cpx_lic):
		try :
			if not isinstance(cpx_lic,int):
				raise TypeError("cpx_lic must be set to int value")
			self._cpx_lic = cpx_lic
		except Exception as e :
			raise e


	'''
	get Maximum VIPs
	'''
	@property
	def max_vips(self) :
		try:
			return self._max_vips
		except Exception as e :
			raise e


	'''
	get Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def analytics(self) :
		try:
			return self._analytics
		except Exception as e :
			raise e
	'''
	set Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@analytics.setter
	def analytics(self,analytics):
		try :
			if not isinstance(analytics,int):
				raise TypeError("analytics must be set to int value")
			self._analytics = analytics
		except Exception as e :
			raise e


	'''
	get Advanced Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def adv_analytics(self) :
		try:
			return self._adv_analytics
		except Exception as e :
			raise e
	'''
	set Advanced Analytics, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@adv_analytics.setter
	def adv_analytics(self,adv_analytics):
		try :
			if not isinstance(adv_analytics,int):
				raise TypeError("adv_analytics must be set to int value")
			self._adv_analytics = adv_analytics
		except Exception as e :
			raise e


	'''
	get Perf, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def perf(self) :
		try:
			return self._perf
		except Exception as e :
			raise e
	'''
	set Perf, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@perf.setter
	def perf(self,perf):
		try :
			if not isinstance(perf,int):
				raise TypeError("perf must be set to int value")
			self._perf = perf
		except Exception as e :
			raise e


	'''
	get Node ID
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e


	'''
	get VPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def vpx_lic(self) :
		try:
			return self._vpx_lic
		except Exception as e :
			raise e
	'''
	set VPX Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@vpx_lic.setter
	def vpx_lic(self,vpx_lic):
		try :
			if not isinstance(vpx_lic,int):
				raise TypeError("vpx_lic must be set to int value")
			self._vpx_lic = vpx_lic
		except Exception as e :
			raise e


	'''
	get Maximum Third Party Vservers
	'''
	@property
	def max_tp_vservers(self) :
		try:
			return self._max_tp_vservers
		except Exception as e :
			raise e


	'''
	get Syslog, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def syslog(self) :
		try:
			return self._syslog
		except Exception as e :
			raise e
	'''
	set Syslog, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@syslog.setter
	def syslog(self,syslog):
		try :
			if not isinstance(syslog,int):
				raise TypeError("syslog must be set to int value")
			self._syslog = syslog
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
	get Time Stamp
	'''
	@property
	def rpt_sampletime(self) :
		try:
			return self._rpt_sampletime
		except Exception as e :
			raise e


	'''
	get Pooled Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def pooled_lic(self) :
		try:
			return self._pooled_lic
		except Exception as e :
			raise e
	'''
	set Pooled Licenses, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@pooled_lic.setter
	def pooled_lic(self,pooled_lic):
		try :
			if not isinstance(pooled_lic,int):
				raise TypeError("pooled_lic must be set to int value")
			self._pooled_lic = pooled_lic
		except Exception as e :
			raise e


	'''
	get SNMP Traps, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@property
	def snmp_traps(self) :
		try:
			return self._snmp_traps
		except Exception as e :
			raise e
	'''
	set SNMP Traps, 0=Unlicensed/Disabled, 1=Unlicensed/Enabled, 2=Licensed/Disabled, 3=Licensed/Enabled
	'''
	@snmp_traps.setter
	def snmp_traps(self,snmp_traps):
		try :
			if not isinstance(snmp_traps,int):
				raise TypeError("snmp_traps must be set to int value")
			self._snmp_traps = snmp_traps
		except Exception as e :
			raise e

	'''
	Total managed VIPs
	'''
	@property
	def total_managed_vips(self):
		try:
			return self._total_managed_vips
		except Exception as e :
			raise e

	'''
	Total managed Third Party Vservers
	'''
	@property
	def total_managed_tp_vservers(self):
		try:
			return self._total_managed_tp_vservers
		except Exception as e :
			raise e

	'''
	Total Allowed Third Party Vservres
	'''
	@property
	def total_allowed_tp_vservers(self):
		try:
			return self._total_allowed_tp_vservers
		except Exception as e :
			raise e

	'''
	Total discovered VIPs
	'''
	@property
	def total_discovered_vips(self):
		try:
			return self._total_discovered_vips
		except Exception as e :
			raise e

	'''
	Total Allowed VIPs
	'''
	@property
	def total_allowed_vips(self):
		try:
			return self._total_allowed_vips
		except Exception as e :
			raise e

	'''
	Total discovered Third Party Vservres
	'''
	@property
	def total_discovered_tp_vservers(self):
		try:
			return self._total_discovered_tp_vservers
		except Exception as e :
			raise e

	'''
	Use this operation to get MAS license information.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				mas_license_obj=mas_license()
				response = mas_license_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to enable/disable MAS system features.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of mas_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._filter=filter_
			return mas_license_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the mas_license resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._count=True
			response = mas_license_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of mas_license resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			mas_license_obj = mas_license()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = mas_license_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(mas_license_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mas_license
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(mas_license_responses, response, "mas_license_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.mas_license_response_array
				i=0
				error = [mas_license() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.mas_license_response_array
			i=0
			mas_license_objs = [mas_license() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_mas_license'):
					for props in obj._mas_license:
						result = service.payload_formatter.string_to_bulk_resource(mas_license_response,self.__class__.__name__,props)
						mas_license_objs[i] = result.mas_license
						i=i+1
			return mas_license_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(mas_license,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class mas_license_response(base_response):
	def __init__(self,length=1) :
		self.mas_license= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.mas_license= [ mas_license() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class mas_license_responses(base_response):
	def __init__(self,length=1) :
		self.mas_license_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.mas_license_response_array = [ mas_license() for _ in range(length)]
