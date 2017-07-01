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
from massrc.com.citrix.mas.nitro.resource.config.mps.entity_tags import entity_tags


'''
Configuration for Managed Device resource
'''

class managed_device(base_resource):
	_hostname= ""
	_std_bw_config= ""
	_gateway_deployment= ""
	_gateway_ipv6= ""
	_ha_master_state= ""
	_instance_available= ""
	_device_finger_print= ""
	_instance_state= ""
	_reason= ""
	_name= ""
	_ent_bw_available= ""
	_description= ""
	_geo_support= ""
	_upsince= ""
	_sslvpn_config= ""
	_model_id= ""
	_sysservices= ""
	_ent_bw_total= ""
	_tenant_id= ""
	_netmask= ""
	_ent_bw_config= ""
	_version= ""
	_instance_config= ""
	_is_managed= ""
	_instance_mode= ""
	_tags=[]
	_instance_total= ""
	_is_ha_configured= ""
	_nexthop_v6= ""
	_trust_id= ""
	_ipv4_address= ""
	_profile_name= ""
	_std_bw_available= ""
	_sysid= ""
	_last_updated_time= ""
	_encoded_serialnumber= ""
	_plt_bw_total= ""
	_uptime= ""
	_id= ""
	_mgmt_ip_address= ""
	_ipv6_address= ""
	_partition_id= ""
	_plt_bw_available= ""
	_device_family= ""
	_location= ""
	_contactperson= ""
	_ha_sync= ""
	_ha_ip_address= ""
	_type= ""
	_gateway= ""
	_status= ""
	_systemname= ""
	_config_type= ""
	_node_id= ""
	_ip_address= ""
	_std_bw_total= ""
	_display_name= ""
	_nexthop= ""
	_plt_bw_config= ""
	_partition_name= ""
	_agent_id= ""
	_sslvpn_total= ""
	_serialnumber= ""
	_file_location_path= ""
	_file_name= ""
	_act_id= ""
	_profile_username= ""
	_profile_password= ""
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
			return "managed_device"
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
			return "managed_device"
		except Exception as e :
			raise e



	'''
	get Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@property
	def hostname(self) :
		try:
			return self._hostname
		except Exception as e :
			raise e
	'''
	set Assign hostname to managed device, if this is not provided, name will be set as host name 
	'''
	@hostname.setter
	def hostname(self,hostname):
		try :
			if not isinstance(hostname,str):
				raise TypeError("hostname must be set to str value")
			self._hostname = hostname
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth running
	'''
	@property
	def std_bw_config(self) :
		try:
			return self._std_bw_config
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth running
	'''
	@std_bw_config.setter
	def std_bw_config(self,std_bw_config):
		try :
			if not isinstance(std_bw_config,int):
				raise TypeError("std_bw_config must be set to int value")
			self._std_bw_config = std_bw_config
		except Exception as e :
			raise e


	'''
	get Is this device acting as Gateway.
	'''
	@property
	def gateway_deployment(self) :
		try:
			return self._gateway_deployment
		except Exception as e :
			raise e
	'''
	set Is this device acting as Gateway.
	'''
	@gateway_deployment.setter
	def gateway_deployment(self,gateway_deployment):
		try :
			if not isinstance(gateway_deployment,bool):
				raise TypeError("gateway_deployment must be set to bool value")
			self._gateway_deployment = gateway_deployment
		except Exception as e :
			raise e


	'''
	get Gateway IPv6 Address
	'''
	@property
	def gateway_ipv6(self) :
		try:
			return self._gateway_ipv6
		except Exception as e :
			raise e
	'''
	set Gateway IPv6 Address
	'''
	@gateway_ipv6.setter
	def gateway_ipv6(self,gateway_ipv6):
		try :
			if not isinstance(gateway_ipv6,str):
				raise TypeError("gateway_ipv6 must be set to str value")
			self._gateway_ipv6 = gateway_ipv6
		except Exception as e :
			raise e


	'''
	get Master State (Primary/Secondary)
	'''
	@property
	def ha_master_state(self) :
		try:
			return self._ha_master_state
		except Exception as e :
			raise e


	'''
	get Instance license available
	'''
	@property
	def instance_available(self) :
		try:
			return self._instance_available
		except Exception as e :
			raise e
	'''
	set Instance license available
	'''
	@instance_available.setter
	def instance_available(self,instance_available):
		try :
			if not isinstance(instance_available,int):
				raise TypeError("instance_available must be set to int value")
			self._instance_available = instance_available
		except Exception as e :
			raise e


	'''
	get Fingerprint/thumb-print from UMS public certificate for SSL communication
	'''
	@property
	def device_finger_print(self) :
		try:
			return self._device_finger_print
		except Exception as e :
			raise e
	'''
	set Fingerprint/thumb-print from UMS public certificate for SSL communication
	'''
	@device_finger_print.setter
	def device_finger_print(self,device_finger_print):
		try :
			if not isinstance(device_finger_print,str):
				raise TypeError("device_finger_print must be set to str value")
			self._device_finger_print = device_finger_print
		except Exception as e :
			raise e


	'''
	get State of device, UP only if device accessible
	'''
	@property
	def instance_state(self) :
		try:
			return self._instance_state
		except Exception as e :
			raise e


	'''
	get Reason of failure for this managed device
	'''
	@property
	def reason(self) :
		try:
			return self._reason
		except Exception as e :
			raise e


	'''
	get Name of managed device
	'''
	@property
	def name(self) :
		try:
			return self._name
		except Exception as e :
			raise e
	'''
	set Name of managed device
	'''
	@name.setter
	def name(self,name):
		try :
			if not isinstance(name,str):
				raise TypeError("name must be set to str value")
			self._name = name
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth configured
	'''
	@property
	def ent_bw_available(self) :
		try:
			return self._ent_bw_available
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth configured
	'''
	@ent_bw_available.setter
	def ent_bw_available(self,ent_bw_available):
		try :
			if not isinstance(ent_bw_available,int):
				raise TypeError("ent_bw_available must be set to int value")
			self._ent_bw_available = ent_bw_available
		except Exception as e :
			raise e


	'''
	get Description of managed device
	'''
	@property
	def description(self) :
		try:
			return self._description
		except Exception as e :
			raise e
	'''
	set Description of managed device
	'''
	@description.setter
	def description(self,description):
		try :
			if not isinstance(description,str):
				raise TypeError("description must be set to str value")
			self._description = description
		except Exception as e :
			raise e


	'''
	get Is this device configured to support GEO location.
	'''
	@property
	def geo_support(self) :
		try:
			return self._geo_support
		except Exception as e :
			raise e
	'''
	set Is this device configured to support GEO location.
	'''
	@geo_support.setter
	def geo_support(self,geo_support):
		try :
			if not isinstance(geo_support,bool):
				raise TypeError("geo_support must be set to bool value")
			self._geo_support = geo_support
		except Exception as e :
			raise e


	'''
	get Upsince of managed device
	'''
	@property
	def upsince(self) :
		try:
			return self._upsince
		except Exception as e :
			raise e


	'''
	get sslvpn license maximum
	'''
	@property
	def sslvpn_config(self) :
		try:
			return self._sslvpn_config
		except Exception as e :
			raise e
	'''
	set sslvpn license maximum
	'''
	@sslvpn_config.setter
	def sslvpn_config(self,sslvpn_config):
		try :
			if not isinstance(sslvpn_config,int):
				raise TypeError("sslvpn_config must be set to int value")
			self._sslvpn_config = sslvpn_config
		except Exception as e :
			raise e


	'''
	get Device Model Id
	'''
	@property
	def model_id(self) :
		try:
			return self._model_id
		except Exception as e :
			raise e


	'''
	get System Services
	'''
	@property
	def sysservices(self) :
		try:
			return self._sysservices
		except Exception as e :
			raise e
	'''
	set System Services
	'''
	@sysservices.setter
	def sysservices(self,sysservices):
		try :
			if not isinstance(sysservices,long):
				raise TypeError("sysservices must be set to long value")
			self._sysservices = sysservices
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth Total
	'''
	@property
	def ent_bw_total(self) :
		try:
			return self._ent_bw_total
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth Total
	'''
	@ent_bw_total.setter
	def ent_bw_total(self,ent_bw_total):
		try :
			if not isinstance(ent_bw_total,int):
				raise TypeError("ent_bw_total must be set to int value")
			self._ent_bw_total = ent_bw_total
		except Exception as e :
			raise e


	'''
	get Tenant ID
	'''
	@property
	def tenant_id(self) :
		try:
			return self._tenant_id
		except Exception as e :
			raise e


	'''
	get Netmask of managed device
	'''
	@property
	def netmask(self) :
		try:
			return self._netmask
		except Exception as e :
			raise e
	'''
	set Netmask of managed device
	'''
	@netmask.setter
	def netmask(self,netmask):
		try :
			if not isinstance(netmask,str):
				raise TypeError("netmask must be set to str value")
			self._netmask = netmask
		except Exception as e :
			raise e


	'''
	get Enterprise Bandwidth configured
	'''
	@property
	def ent_bw_config(self) :
		try:
			return self._ent_bw_config
		except Exception as e :
			raise e
	'''
	set Enterprise Bandwidth configured
	'''
	@ent_bw_config.setter
	def ent_bw_config(self,ent_bw_config):
		try :
			if not isinstance(ent_bw_config,int):
				raise TypeError("ent_bw_config must be set to int value")
			self._ent_bw_config = ent_bw_config
		except Exception as e :
			raise e


	'''
	get Device Version
	'''
	@property
	def version(self) :
		try:
			return self._version
		except Exception as e :
			raise e


	'''
	get Instance license running
	'''
	@property
	def instance_config(self) :
		try:
			return self._instance_config
		except Exception as e :
			raise e
	'''
	set Instance license running
	'''
	@instance_config.setter
	def instance_config(self,instance_config):
		try :
			if not isinstance(instance_config,int):
				raise TypeError("instance_config must be set to int value")
			self._instance_config = instance_config
		except Exception as e :
			raise e


	'''
	get Is Managed
	'''
	@property
	def is_managed(self) :
		try:
			return self._is_managed
		except Exception as e :
			raise e
	'''
	set Is Managed
	'''
	@is_managed.setter
	def is_managed(self,is_managed):
		try :
			if not isinstance(is_managed,bool):
				raise TypeError("is_managed must be set to bool value")
			self._is_managed = is_managed
		except Exception as e :
			raise e


	'''
	get Denotes state- primary,secondary,clip,clusternode
	'''
	@property
	def instance_mode(self) :
		try:
			return self._instance_mode
		except Exception as e :
			raise e
	'''
	set Denotes state- primary,secondary,clip,clusternode
	'''
	@instance_mode.setter
	def instance_mode(self,instance_mode):
		try :
			if not isinstance(instance_mode,str):
				raise TypeError("instance_mode must be set to str value")
			self._instance_mode = instance_mode
		except Exception as e :
			raise e


	'''
	get Tags
	'''
	@property
	def tags(self) :
		try:
			return self._tags
		except Exception as e :
			raise e
	'''
	set Tags
	'''
	@tags.setter
	def tags(self,tags) :
		try :
			if not isinstance(tags,list):
				raise TypeError("tags must be set to array of entity_tags value")
			for item in tags :
				if not isinstance(item,entity_tags):
					raise TypeError("item must be set to entity_tags value")
			self._tags = tags
		except Exception as e :
			raise e


	'''
	get Instance license
	'''
	@property
	def instance_total(self) :
		try:
			return self._instance_total
		except Exception as e :
			raise e
	'''
	set Instance license
	'''
	@instance_total.setter
	def instance_total(self,instance_total):
		try :
			if not isinstance(instance_total,int):
				raise TypeError("instance_total must be set to int value")
			self._instance_total = instance_total
		except Exception as e :
			raise e


	'''
	get Is HA configured
	'''
	@property
	def is_ha_configured(self) :
		try:
			return self._is_ha_configured
		except Exception as e :
			raise e
	'''
	set Is HA configured
	'''
	@is_ha_configured.setter
	def is_ha_configured(self,is_ha_configured):
		try :
			if not isinstance(is_ha_configured,bool):
				raise TypeError("is_ha_configured must be set to bool value")
			self._is_ha_configured = is_ha_configured
		except Exception as e :
			raise e


	'''
	get Next Hop IPv6 Address
	'''
	@property
	def nexthop_v6(self) :
		try:
			return self._nexthop_v6
		except Exception as e :
			raise e
	'''
	set Next Hop IPv6 Address
	'''
	@nexthop_v6.setter
	def nexthop_v6(self,nexthop_v6):
		try :
			if not isinstance(nexthop_v6,str):
				raise TypeError("nexthop_v6 must be set to str value")
			self._nexthop_v6 = nexthop_v6
		except Exception as e :
			raise e


	'''
	get Device ID obtained from trust service
	'''
	@property
	def trust_id(self) :
		try:
			return self._trust_id
		except Exception as e :
			raise e
	'''
	set Device ID obtained from trust service
	'''
	@trust_id.setter
	def trust_id(self,trust_id):
		try :
			if not isinstance(trust_id,str):
				raise TypeError("trust_id must be set to str value")
			self._trust_id = trust_id
		except Exception as e :
			raise e


	'''
	get IPv4 Address
	'''
	@property
	def ipv4_address(self) :
		try:
			return self._ipv4_address
		except Exception as e :
			raise e
	'''
	set IPv4 Address
	'''
	@ipv4_address.setter
	def ipv4_address(self,ipv4_address):
		try :
			if not isinstance(ipv4_address,str):
				raise TypeError("ipv4_address must be set to str value")
			self._ipv4_address = ipv4_address
		except Exception as e :
			raise e


	'''
	get Device Profile Name that is attached with this managed device
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Device Profile Name that is attached with this managed device
	'''
	@profile_name.setter
	def profile_name(self,profile_name):
		try :
			if not isinstance(profile_name,str):
				raise TypeError("profile_name must be set to str value")
			self._profile_name = profile_name
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth Available
	'''
	@property
	def std_bw_available(self) :
		try:
			return self._std_bw_available
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth Available
	'''
	@std_bw_available.setter
	def std_bw_available(self,std_bw_available):
		try :
			if not isinstance(std_bw_available,int):
				raise TypeError("std_bw_available must be set to int value")
			self._std_bw_available = std_bw_available
		except Exception as e :
			raise e


	'''
	get System ID
	'''
	@property
	def sysid(self) :
		try:
			return self._sysid
		except Exception as e :
			raise e


	'''
	get Last Updated Time
	'''
	@property
	def last_updated_time(self) :
		try:
			return self._last_updated_time
		except Exception as e :
			raise e
	'''
	set Last Updated Time
	'''
	@last_updated_time.setter
	def last_updated_time(self,last_updated_time):
		try :
			if not isinstance(last_updated_time,long):
				raise TypeError("last_updated_time must be set to long value")
			self._last_updated_time = last_updated_time
		except Exception as e :
			raise e


	'''
	get Encoded Serial Number
	'''
	@property
	def encoded_serialnumber(self) :
		try:
			return self._encoded_serialnumber
		except Exception as e :
			raise e


	'''
	get Total Platinum Bandwidth
	'''
	@property
	def plt_bw_total(self) :
		try:
			return self._plt_bw_total
		except Exception as e :
			raise e
	'''
	set Total Platinum Bandwidth
	'''
	@plt_bw_total.setter
	def plt_bw_total(self,plt_bw_total):
		try :
			if not isinstance(plt_bw_total,int):
				raise TypeError("plt_bw_total must be set to int value")
			self._plt_bw_total = plt_bw_total
		except Exception as e :
			raise e


	'''
	get Uptime of device
	'''
	@property
	def uptime(self) :
		try:
			return self._uptime
		except Exception as e :
			raise e


	'''
	get Id is system generated key for all the managed devices
	'''
	@property
	def id(self) :
		try:
			return self._id
		except Exception as e :
			raise e
	'''
	set Id is system generated key for all the managed devices
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
	get Management IP Address for this Managed Device
	'''
	@property
	def mgmt_ip_address(self) :
		try:
			return self._mgmt_ip_address
		except Exception as e :
			raise e
	'''
	set Management IP Address for this Managed Device
	'''
	@mgmt_ip_address.setter
	def mgmt_ip_address(self,mgmt_ip_address):
		try :
			if not isinstance(mgmt_ip_address,str):
				raise TypeError("mgmt_ip_address must be set to str value")
			self._mgmt_ip_address = mgmt_ip_address
		except Exception as e :
			raise e


	'''
	get IPv6 Address
	'''
	@property
	def ipv6_address(self) :
		try:
			return self._ipv6_address
		except Exception as e :
			raise e
	'''
	set IPv6 Address
	'''
	@ipv6_address.setter
	def ipv6_address(self,ipv6_address):
		try :
			if not isinstance(ipv6_address,str):
				raise TypeError("ipv6_address must be set to str value")
			self._ipv6_address = ipv6_address
		except Exception as e :
			raise e


	'''
	get ID of admin partition
	'''
	@property
	def partition_id(self) :
		try:
			return self._partition_id
		except Exception as e :
			raise e
	'''
	set ID of admin partition
	'''
	@partition_id.setter
	def partition_id(self,partition_id):
		try :
			if not isinstance(partition_id,str):
				raise TypeError("partition_id must be set to str value")
			self._partition_id = partition_id
		except Exception as e :
			raise e


	'''
	get Platinum Bandwidth Available
	'''
	@property
	def plt_bw_available(self) :
		try:
			return self._plt_bw_available
		except Exception as e :
			raise e
	'''
	set Platinum Bandwidth Available
	'''
	@plt_bw_available.setter
	def plt_bw_available(self,plt_bw_available):
		try :
			if not isinstance(plt_bw_available,int):
				raise TypeError("plt_bw_available must be set to int value")
			self._plt_bw_available = plt_bw_available
		except Exception as e :
			raise e


	'''
	get Device Family
	'''
	@property
	def device_family(self) :
		try:
			return self._device_family
		except Exception as e :
			raise e
	'''
	set Device Family
	'''
	@device_family.setter
	def device_family(self,device_family):
		try :
			if not isinstance(device_family,str):
				raise TypeError("device_family must be set to str value")
			self._device_family = device_family
		except Exception as e :
			raise e


	'''
	get Device Location
	'''
	@property
	def location(self) :
		try:
			return self._location
		except Exception as e :
			raise e


	'''
	get Device contact person
	'''
	@property
	def contactperson(self) :
		try:
			return self._contactperson
		except Exception as e :
			raise e


	'''
	get HA Synchronization State
	'''
	@property
	def ha_sync(self) :
		try:
			return self._ha_sync
		except Exception as e :
			raise e


	'''
	get Peer IP Address
	'''
	@property
	def ha_ip_address(self) :
		try:
			return self._ha_ip_address
		except Exception as e :
			raise e


	'''
	get Type of device, (Xen | NS)
	'''
	@property
	def type(self) :
		try:
			return self._type
		except Exception as e :
			raise e
	'''
	set Type of device, (Xen | NS)
	'''
	@type.setter
	def type(self,type):
		try :
			if not isinstance(type,str):
				raise TypeError("type must be set to str value")
			self._type = type
		except Exception as e :
			raise e


	'''
	get Default Gateway of managed device
	'''
	@property
	def gateway(self) :
		try:
			return self._gateway
		except Exception as e :
			raise e
	'''
	set Default Gateway of managed device
	'''
	@gateway.setter
	def gateway(self,gateway):
		try :
			if not isinstance(gateway,str):
				raise TypeError("gateway must be set to str value")
			self._gateway = gateway
		except Exception as e :
			raise e


	'''
	get Status of managed device
	'''
	@property
	def status(self) :
		try:
			return self._status
		except Exception as e :
			raise e


	'''
	get Device System Name
	'''
	@property
	def systemname(self) :
		try:
			return self._systemname
		except Exception as e :
			raise e


	'''
	get Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@property
	def config_type(self) :
		try:
			return self._config_type
		except Exception as e :
			raise e
	'''
	set Configuration Type. Values: 0: IPv4, 1: IPv6, 2: Both
	'''
	@config_type.setter
	def config_type(self,config_type):
		try :
			if not isinstance(config_type,int):
				raise TypeError("config_type must be set to int value")
			self._config_type = config_type
		except Exception as e :
			raise e


	'''
	get Node identification of a device
	'''
	@property
	def node_id(self) :
		try:
			return self._node_id
		except Exception as e :
			raise e
	'''
	set Node identification of a device
	'''
	@node_id.setter
	def node_id(self,node_id):
		try :
			if not isinstance(node_id,str):
				raise TypeError("node_id must be set to str value")
			self._node_id = node_id
		except Exception as e :
			raise e


	'''
	get IP Address for this managed device
	'''
	@property
	def ip_address(self) :
		try:
			return self._ip_address
		except Exception as e :
			raise e
	'''
	set IP Address for this managed device
	'''
	@ip_address.setter
	def ip_address(self,ip_address):
		try :
			if not isinstance(ip_address,str):
				raise TypeError("ip_address must be set to str value")
			self._ip_address = ip_address
		except Exception as e :
			raise e


	'''
	get Standard Bandwidth
	'''
	@property
	def std_bw_total(self) :
		try:
			return self._std_bw_total
		except Exception as e :
			raise e
	'''
	set Standard Bandwidth
	'''
	@std_bw_total.setter
	def std_bw_total(self,std_bw_total):
		try :
			if not isinstance(std_bw_total,int):
				raise TypeError("std_bw_total must be set to int value")
			self._std_bw_total = std_bw_total
		except Exception as e :
			raise e


	'''
	get Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP
	'''
	@property
	def display_name(self) :
		try:
			return self._display_name
		except Exception as e :
			raise e
	'''
	set Display Name for this managed device. For HA pair it will be A-B, and for Cluster it will be CLIP
	'''
	@display_name.setter
	def display_name(self,display_name):
		try :
			if not isinstance(display_name,str):
				raise TypeError("display_name must be set to str value")
			self._display_name = display_name
		except Exception as e :
			raise e


	'''
	get Next Hop IP address
	'''
	@property
	def nexthop(self) :
		try:
			return self._nexthop
		except Exception as e :
			raise e
	'''
	set Next Hop IP address
	'''
	@nexthop.setter
	def nexthop(self,nexthop):
		try :
			if not isinstance(nexthop,str):
				raise TypeError("nexthop must be set to str value")
			self._nexthop = nexthop
		except Exception as e :
			raise e


	'''
	get Platinum Bandwidth configured
	'''
	@property
	def plt_bw_config(self) :
		try:
			return self._plt_bw_config
		except Exception as e :
			raise e
	'''
	set Platinum Bandwidth configured
	'''
	@plt_bw_config.setter
	def plt_bw_config(self,plt_bw_config):
		try :
			if not isinstance(plt_bw_config,int):
				raise TypeError("plt_bw_config must be set to int value")
			self._plt_bw_config = plt_bw_config
		except Exception as e :
			raise e


	'''
	get NS Admin Partition Name
	'''
	@property
	def partition_name(self) :
		try:
			return self._partition_name
		except Exception as e :
			raise e
	'''
	set NS Admin Partition Name
	'''
	@partition_name.setter
	def partition_name(self,partition_name):
		try :
			if not isinstance(partition_name,str):
				raise TypeError("partition_name must be set to str value")
			self._partition_name = partition_name
		except Exception as e :
			raise e


	'''
	get Agent Id
	'''
	@property
	def agent_id(self) :
		try:
			return self._agent_id
		except Exception as e :
			raise e
	'''
	set Agent Id
	'''
	@agent_id.setter
	def agent_id(self,agent_id):
		try :
			if not isinstance(agent_id,str):
				raise TypeError("agent_id must be set to str value")
			self._agent_id = agent_id
		except Exception as e :
			raise e


	'''
	get sslvpn license
	'''
	@property
	def sslvpn_total(self) :
		try:
			return self._sslvpn_total
		except Exception as e :
			raise e
	'''
	set sslvpn license
	'''
	@sslvpn_total.setter
	def sslvpn_total(self,sslvpn_total):
		try :
			if not isinstance(sslvpn_total,int):
				raise TypeError("sslvpn_total must be set to int value")
			self._sslvpn_total = sslvpn_total
		except Exception as e :
			raise e


	'''
	get Device Serial Number
	'''
	@property
	def serialnumber(self) :
		try:
			return self._serialnumber
		except Exception as e :
			raise e

	'''
	File Location on Client for upload/download
	'''
	@property
	def file_location_path(self):
		try:
			return self._file_location_path
		except Exception as e :
			raise e
	'''
	File Location on Client for upload/download
	'''
	@file_location_path.setter
	def file_location_path(self,file_location_path):
		try :
			if not isinstance(file_location_path,str):
				raise TypeError("file_location_path must be set to str value")
			self._file_location_path = file_location_path
		except Exception as e :
			raise e

	'''
	File name which contains comma separated instances to be  discovered
	'''
	@property
	def file_name(self):
		try:
			return self._file_name
		except Exception as e :
			raise e
	'''
	File name which contains comma separated instances to be  discovered
	'''
	@file_name.setter
	def file_name(self,file_name):
		try :
			if not isinstance(file_name,str):
				raise TypeError("file_name must be set to str value")
			self._file_name = file_name
		except Exception as e :
			raise e

	'''
	Activity Id
	'''
	@property
	def act_id(self):
		try:
			return self._act_id
		except Exception as e :
			raise e

	'''
	User Name specified by the user for this Netscaler Instance.
	'''
	@property
	def profile_username(self):
		try:
			return self._profile_username
		except Exception as e :
			raise e
	'''
	User Name specified by the user for this Netscaler Instance.
	'''
	@profile_username.setter
	def profile_username(self,profile_username):
		try :
			if not isinstance(profile_username,str):
				raise TypeError("profile_username must be set to str value")
			self._profile_username = profile_username
		except Exception as e :
			raise e

	'''
	Password specified by the user for this Netscaler.
	'''
	@property
	def profile_password(self):
		try:
			return self._profile_password
		except Exception as e :
			raise e
	'''
	Password specified by the user for this Netscaler.
	'''
	@profile_password.setter
	def profile_password(self,profile_password):
		try :
			if not isinstance(profile_password,str):
				raise TypeError("profile_password must be set to str value")
			self._profile_password = profile_password
		except Exception as e :
			raise e

	'''
	Use this operation to add managed device.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"add", resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to upload build file.
	'''

	'''
	Use this operation to upload build file.
	'''
	@classmethod
	def upload(cls,service=None,resource=None) :
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if resource :
				return cls.upload_resources(service,resource)
			else :
				raise Exception("File Object Not Found")
		except Exception as e :
			raise e

	'''
	Use this operation to delete managed device.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					managed_device_obj=managed_device()
					return cls.delete_bulk_request(client,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get managed devices.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				managed_device_obj=managed_device()
				response = managed_device_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to update managed device.
	'''
	@classmethod
	def modify(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				managed_device_obj=managed_device()
				return cls.update_bulk_request(client,resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to annotate managed device.
	'''

	'''
	Use this operation to annotate managed device.
	'''
	@classmethod
	def annotate(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"annotate")
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"annotate", resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add managed device using csv file.
	'''
	@classmethod
	def add_device(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add_device")
			else : 
				managed_device_obj= managed_device()
				return cls.perform_operation_bulk_request(service,"add_device", resource,managed_device_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of managed_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._filter=filter_
			return managed_device_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the managed_device resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._count=True
			response = managed_device_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of managed_device resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			managed_device_obj = managed_device()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = managed_device_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(managed_device_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.managed_device
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(managed_device_responses, response, "managed_device_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.managed_device_response_array
				i=0
				error = [managed_device() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.managed_device_response_array
			i=0
			managed_device_objs = [managed_device() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_managed_device'):
					for props in obj._managed_device:
						result = service.payload_formatter.string_to_bulk_resource(managed_device_response,self.__class__.__name__,props)
						managed_device_objs[i] = result.managed_device
						i=i+1
			return managed_device_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(managed_device,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class managed_device_response(base_response):
	def __init__(self,length=1) :
		self.managed_device= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.managed_device= [ managed_device() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class managed_device_responses(base_response):
	def __init__(self,length=1) :
		self.managed_device_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.managed_device_response_array = [ managed_device() for _ in range(length)]
