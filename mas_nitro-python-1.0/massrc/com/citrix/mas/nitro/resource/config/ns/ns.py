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

from massrc.com.citrix.mas.nitro.resource.config.mps.vm_device import vm_device

'''
Configuration for NetScaler resource
'''

class ns(vm_device):
	_if_0_2= ""
	_disksize= ""
	_if_0_3= ""
	_backplane= ""
	_clusterid= ""
	_nodeid= ""
	_diskused= ""
	_instance_name= ""
	_if_0_1= ""
	_task_id= ""
	_state= ""
	_ns_ip_address= ""
	_password= ""
	_is_clip= ""
	_customid= ""
	_http_req= ""
	_pre_auth_key= ""
	_ns_total_tx= ""
	_username= ""
	_diskavail= ""
	_ns_cpu_usage= ""
	_number_of_ssl_cards= ""
	_ns_observationdomainid= ""
	_ns_rx= ""
	_node_state= ""
	_plugin_ip_address= ""
	_vlan_type= ""
	_nsvlan_id= ""
	_cmd_policy= ""
	_ns_memory_usage= ""
	_nsvlan_tagged= ""
	_clip= ""
	_iscco= ""
	_ns_mgmt_cpu_usage= ""
	_diskperusage= ""
	_num_pes= ""
	_port_range= ""
	_instance_id= ""
	_plugin_netmask= ""
	_pps= ""
	_system_hardwareversion= ""
	_license= ""
	_ns_tx= ""
	_health= ""
	_ns_total_rx= ""
	_number_of_ssl_cores_up= ""
	_EULA= ""
	_num_ports= ""
	_save_config= ""
	_LS_IP= ""
	_diff_exists= ""
	_start_port= ""
	_nsvlan_interfaces=[]
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
			return "ns"
		except Exception as e :
			raise e

	'''
	Returns the value of object identifier argument.
	'''
	def get_object_id(self) :
		try:
			return super(ns,self).get_object_id()
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
			return "nss"
		except Exception as e :
			raise e



	'''
	get Network 0/2 on VM Instance
	'''
	@property
	def if_0_2(self) :
		try:
			return self._if_0_2
		except Exception as e :
			raise e
	'''
	set Network 0/2 on VM Instance
	'''
	@if_0_2.setter
	def if_0_2(self,if_0_2):
		try :
			if not isinstance(if_0_2,bool):
				raise TypeError("if_0_2 must be set to bool value")
			self._if_0_2 = if_0_2
		except Exception as e :
			raise e


	'''
	get NS Disk Size(MB)
	'''
	@property
	def disksize(self) :
		try:
			return self._disksize
		except Exception as e :
			raise e


	'''
	get Network 0/3 on VM Instance
	'''
	@property
	def if_0_3(self) :
		try:
			return self._if_0_3
		except Exception as e :
			raise e


	'''
	get Backplane Interface
	'''
	@property
	def backplane(self) :
		try:
			return self._backplane
		except Exception as e :
			raise e
	'''
	set Backplane Interface
	'''
	@backplane.setter
	def backplane(self,backplane):
		try :
			if not isinstance(backplane,str):
				raise TypeError("backplane must be set to str value")
			self._backplane = backplane
		except Exception as e :
			raise e


	'''
	get Cluster Id
	'''
	@property
	def clusterid(self) :
		try:
			return self._clusterid
		except Exception as e :
			raise e
	'''
	set Cluster Id
	'''
	@clusterid.setter
	def clusterid(self,clusterid):
		try :
			if not isinstance(clusterid,int):
				raise TypeError("clusterid must be set to int value")
			self._clusterid = clusterid
		except Exception as e :
			raise e


	'''
	get Node Id
	'''
	@property
	def nodeid(self) :
		try:
			return self._nodeid
		except Exception as e :
			raise e
	'''
	set Node Id
	'''
	@nodeid.setter
	def nodeid(self,nodeid):
		try :
			if not isinstance(nodeid,int):
				raise TypeError("nodeid must be set to int value")
			self._nodeid = nodeid
		except Exception as e :
			raise e


	'''
	get NS Disk Used(MB)
	'''
	@property
	def diskused(self) :
		try:
			return self._diskused
		except Exception as e :
			raise e


	'''
	get NetScaler CPX Instance Name
	'''
	@property
	def instance_name(self) :
		try:
			return self._instance_name
		except Exception as e :
			raise e
	'''
	set NetScaler CPX Instance Name
	'''
	@instance_name.setter
	def instance_name(self,instance_name):
		try :
			if not isinstance(instance_name,str):
				raise TypeError("instance_name must be set to str value")
			self._instance_name = instance_name
		except Exception as e :
			raise e


	'''
	get Network 0/1 on VM Instance
	'''
	@property
	def if_0_1(self) :
		try:
			return self._if_0_1
		except Exception as e :
			raise e
	'''
	set Network 0/1 on VM Instance
	'''
	@if_0_1.setter
	def if_0_1(self,if_0_1):
		try :
			if not isinstance(if_0_1,bool):
				raise TypeError("if_0_1 must be set to bool value")
			self._if_0_1 = if_0_1
		except Exception as e :
			raise e


	'''
	get Task Id used by Triton to identify NS
	'''
	@property
	def task_id(self) :
		try:
			return self._task_id
		except Exception as e :
			raise e
	'''
	set Task Id used by Triton to identify NS
	'''
	@task_id.setter
	def task_id(self,task_id):
		try :
			if not isinstance(task_id,str):
				raise TypeError("task_id must be set to str value")
			self._task_id = task_id
		except Exception as e :
			raise e


	'''
	get Node State
	'''
	@property
	def state(self) :
		try:
			return self._state
		except Exception as e :
			raise e
	'''
	set Node State
	'''
	@state.setter
	def state(self,state):
		try :
			if not isinstance(state,str):
				raise TypeError("state must be set to str value")
			self._state = state
		except Exception as e :
			raise e


	'''
	get NS IP Address for this managed device
	'''
	@property
	def ns_ip_address(self) :
		try:
			return self._ns_ip_address
		except Exception as e :
			raise e
	'''
	set NS IP Address for this managed device
	'''
	@ns_ip_address.setter
	def ns_ip_address(self,ns_ip_address):
		try :
			if not isinstance(ns_ip_address,str):
				raise TypeError("ns_ip_address must be set to str value")
			self._ns_ip_address = ns_ip_address
		except Exception as e :
			raise e


	'''
	get Password for specified user on NetScaler Instance
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password for specified user on NetScaler Instance
	'''
	@password.setter
	def password(self,password):
		try :
			if not isinstance(password,str):
				raise TypeError("password must be set to str value")
			self._password = password
		except Exception as e :
			raise e


	'''
	get Is Clip
	'''
	@property
	def is_clip(self) :
		try:
			return self._is_clip
		except Exception as e :
			raise e
	'''
	set Is Clip
	'''
	@is_clip.setter
	def is_clip(self,is_clip):
		try :
			if not isinstance(is_clip,bool):
				raise TypeError("is_clip must be set to bool value")
			self._is_clip = is_clip
		except Exception as e :
			raise e


	'''
	get Custom ID
	'''
	@property
	def customid(self) :
		try:
			return self._customid
		except Exception as e :
			raise e
	'''
	set Custom ID
	'''
	@customid.setter
	def customid(self,customid):
		try :
			if not isinstance(customid,str):
				raise TypeError("customid must be set to str value")
			self._customid = customid
		except Exception as e :
			raise e


	'''
	get HTTP Requests/second
	'''
	@property
	def http_req(self) :
		try:
			return self._http_req
		except Exception as e :
			raise e


	'''
	get Shared secret that used for orchestration deployment
	'''
	@property
	def pre_auth_key(self) :
		try:
			return self._pre_auth_key
		except Exception as e :
			raise e
	'''
	set Shared secret that used for orchestration deployment
	'''
	@pre_auth_key.setter
	def pre_auth_key(self,pre_auth_key):
		try :
			if not isinstance(pre_auth_key,str):
				raise TypeError("pre_auth_key must be set to str value")
			self._pre_auth_key = pre_auth_key
		except Exception as e :
			raise e


	'''
	get Total Tx of NetScaler Instance in Mbits
	'''
	@property
	def ns_total_tx(self) :
		try:
			return self._ns_total_tx
		except Exception as e :
			raise e


	'''
	get User Name (except nsroot) to be configured on NetScaler Instance
	'''
	@property
	def username(self) :
		try:
			return self._username
		except Exception as e :
			raise e
	'''
	set User Name (except nsroot) to be configured on NetScaler Instance
	'''
	@username.setter
	def username(self,username):
		try :
			if not isinstance(username,str):
				raise TypeError("username must be set to str value")
			self._username = username
		except Exception as e :
			raise e


	'''
	get NS Disk Available(MB)
	'''
	@property
	def diskavail(self) :
		try:
			return self._diskavail
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of NetScaler Instance
	'''
	@property
	def ns_cpu_usage(self) :
		try:
			return self._ns_cpu_usage
		except Exception as e :
			raise e


	'''
	get Number of SSL Cards
	'''
	@property
	def number_of_ssl_cards(self) :
		try:
			return self._number_of_ssl_cards
		except Exception as e :
			raise e
	'''
	set Number of SSL Cards
	'''
	@number_of_ssl_cards.setter
	def number_of_ssl_cards(self,number_of_ssl_cards):
		try :
			if not isinstance(number_of_ssl_cards,int):
				raise TypeError("number_of_ssl_cards must be set to int value")
			self._number_of_ssl_cards = number_of_ssl_cards
		except Exception as e :
			raise e


	'''
	get ns_observationdomainid
	'''
	@property
	def ns_observationdomainid(self) :
		try:
			return self._ns_observationdomainid
		except Exception as e :
			raise e
	'''
	set ns_observationdomainid
	'''
	@ns_observationdomainid.setter
	def ns_observationdomainid(self,ns_observationdomainid):
		try :
			if not isinstance(ns_observationdomainid,str):
				raise TypeError("ns_observationdomainid must be set to str value")
			self._ns_observationdomainid = ns_observationdomainid
		except Exception as e :
			raise e


	'''
	get In Throughput of NetScaler Instance in Mbps
	'''
	@property
	def ns_rx(self) :
		try:
			return self._ns_rx
		except Exception as e :
			raise e


	'''
	get Node State of NetScaler Instance
	'''
	@property
	def node_state(self) :
		try:
			return self._node_state
		except Exception as e :
			raise e


	'''
	get Signaling IP Address
	'''
	@property
	def plugin_ip_address(self) :
		try:
			return self._plugin_ip_address
		except Exception as e :
			raise e
	'''
	set Signaling IP Address
	'''
	@plugin_ip_address.setter
	def plugin_ip_address(self,plugin_ip_address):
		try :
			if not isinstance(plugin_ip_address,str):
				raise TypeError("plugin_ip_address must be set to str value")
			self._plugin_ip_address = plugin_ip_address
		except Exception as e :
			raise e


	'''
	get VLAN Type, NS or L2 VLAN
	'''
	@property
	def vlan_type(self) :
		try:
			return self._vlan_type
		except Exception as e :
			raise e
	'''
	set VLAN Type, NS or L2 VLAN
	'''
	@vlan_type.setter
	def vlan_type(self,vlan_type):
		try :
			if not isinstance(vlan_type,int):
				raise TypeError("vlan_type must be set to int value")
			self._vlan_type = vlan_type
		except Exception as e :
			raise e


	'''
	get VLAN Id
	'''
	@property
	def nsvlan_id(self) :
		try:
			return self._nsvlan_id
		except Exception as e :
			raise e
	'''
	set VLAN Id
	'''
	@nsvlan_id.setter
	def nsvlan_id(self,nsvlan_id):
		try :
			if not isinstance(nsvlan_id,int):
				raise TypeError("nsvlan_id must be set to int value")
			self._nsvlan_id = nsvlan_id
		except Exception as e :
			raise e


	'''
	get true if you want to allow shell/sftp/scp access to NetScaler Instance administrator
	'''
	@property
	def cmd_policy(self) :
		try:
			return self._cmd_policy
		except Exception as e :
			raise e
	'''
	set true if you want to allow shell/sftp/scp access to NetScaler Instance administrator
	'''
	@cmd_policy.setter
	def cmd_policy(self,cmd_policy):
		try :
			if not isinstance(cmd_policy,str):
				raise TypeError("cmd_policy must be set to str value")
			self._cmd_policy = cmd_policy
		except Exception as e :
			raise e


	'''
	get Memory Usage (%)
	'''
	@property
	def ns_memory_usage(self) :
		try:
			return self._ns_memory_usage
		except Exception as e :
			raise e


	'''
	get NSVLAN Tagged
	'''
	@property
	def nsvlan_tagged(self) :
		try:
			return self._nsvlan_tagged
		except Exception as e :
			raise e
	'''
	set NSVLAN Tagged
	'''
	@nsvlan_tagged.setter
	def nsvlan_tagged(self,nsvlan_tagged):
		try :
			if not isinstance(nsvlan_tagged,bool):
				raise TypeError("nsvlan_tagged must be set to bool value")
			self._nsvlan_tagged = nsvlan_tagged
		except Exception as e :
			raise e


	'''
	get Cluster IP Address
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IP Address
	'''
	@clip.setter
	def clip(self,clip):
		try :
			if not isinstance(clip,str):
				raise TypeError("clip must be set to str value")
			self._clip = clip
		except Exception as e :
			raise e


	'''
	get Is CCO
	'''
	@property
	def iscco(self) :
		try:
			return self._iscco
		except Exception as e :
			raise e
	'''
	set Is CCO
	'''
	@iscco.setter
	def iscco(self,iscco):
		try :
			if not isinstance(iscco,bool):
				raise TypeError("iscco must be set to bool value")
			self._iscco = iscco
		except Exception as e :
			raise e


	'''
	get Management CPU Usage (%)
	'''
	@property
	def ns_mgmt_cpu_usage(self) :
		try:
			return self._ns_mgmt_cpu_usage
		except Exception as e :
			raise e


	'''
	get NS Disk Utilization (%)
	'''
	@property
	def diskperusage(self) :
		try:
			return self._diskperusage
		except Exception as e :
			raise e


	'''
	get Total number of PEs
	'''
	@property
	def num_pes(self) :
		try:
			return self._num_pes
		except Exception as e :
			raise e
	'''
	set Total number of PEs
	'''
	@num_pes.setter
	def num_pes(self,num_pes):
		try :
			if not isinstance(num_pes,int):
				raise TypeError("num_pes must be set to int value")
			self._num_pes = num_pes
		except Exception as e :
			raise e


	'''
	get NetScaler CPX Exposed Port Range
	'''
	@property
	def port_range(self) :
		try:
			return self._port_range
		except Exception as e :
			raise e


	'''
	get Id of CPX instance
	'''
	@property
	def instance_id(self) :
		try:
			return self._instance_id
		except Exception as e :
			raise e


	'''
	get Signaling Netmask
	'''
	@property
	def plugin_netmask(self) :
		try:
			return self._plugin_netmask
		except Exception as e :
			raise e
	'''
	set Signaling Netmask
	'''
	@plugin_netmask.setter
	def plugin_netmask(self,plugin_netmask):
		try :
			if not isinstance(plugin_netmask,str):
				raise TypeError("plugin_netmask must be set to str value")
			self._plugin_netmask = plugin_netmask
		except Exception as e :
			raise e


	'''
	get Assign packets per seconds to NetScaler Instance
	'''
	@property
	def pps(self) :
		try:
			return self._pps
		except Exception as e :
			raise e
	'''
	set Assign packets per seconds to NetScaler Instance
	'''
	@pps.setter
	def pps(self,pps):
		try :
			if not isinstance(pps,float):
				raise TypeError("pps must be set to float value")
			self._pps = pps
		except Exception as e :
			raise e


	'''
	get System Hardware Version
	'''
	@property
	def system_hardwareversion(self) :
		try:
			return self._system_hardwareversion
		except Exception as e :
			raise e


	'''
	get Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@property
	def license(self) :
		try:
			return self._license
		except Exception as e :
			raise e
	'''
	set Feature License for NetScaler Instance, needs to be set while provisioning (standard, enterprise, platinum)
	'''
	@license.setter
	def license(self,license):
		try :
			if not isinstance(license,str):
				raise TypeError("license must be set to str value")
			self._license = license
		except Exception as e :
			raise e


	'''
	get Out Throughput of NetScaler Instance in Mbps
	'''
	@property
	def ns_tx(self) :
		try:
			return self._ns_tx
		except Exception as e :
			raise e


	'''
	get Node Health
	'''
	@property
	def health(self) :
		try:
			return self._health
		except Exception as e :
			raise e


	'''
	get Total Rx of NetScaler Instance in Mbits
	'''
	@property
	def ns_total_rx(self) :
		try:
			return self._ns_total_rx
		except Exception as e :
			raise e


	'''
	get Number of SSL Cores Up
	'''
	@property
	def number_of_ssl_cores_up(self) :
		try:
			return self._number_of_ssl_cores_up
		except Exception as e :
			raise e
	'''
	set Number of SSL Cores Up
	'''
	@number_of_ssl_cores_up.setter
	def number_of_ssl_cores_up(self,number_of_ssl_cores_up):
		try :
			if not isinstance(number_of_ssl_cores_up,int):
				raise TypeError("number_of_ssl_cores_up must be set to int value")
			self._number_of_ssl_cores_up = number_of_ssl_cores_up
		except Exception as e :
			raise e

	'''
	Value will be set to true if end user accepts EULA
	'''
	@property
	def EULA(self):
		try:
			return self._EULA
		except Exception as e :
			raise e
	'''
	Value will be set to true if end user accepts EULA
	'''
	@EULA.setter
	def EULA(self,EULA):
		try :
			if not isinstance(EULA,bool):
				raise TypeError("EULA must be set to bool value")
			self._EULA = EULA
		except Exception as e :
			raise e

	'''
	Number of CPX Ports to be exposed
	'''
	@property
	def num_ports(self):
		try:
			return self._num_ports
		except Exception as e :
			raise e
	'''
	Number of CPX Ports to be exposed
	'''
	@num_ports.setter
	def num_ports(self,num_ports):
		try :
			if not isinstance(num_ports,int):
				raise TypeError("num_ports must be set to int value")
			self._num_ports = num_ports
		except Exception as e :
			raise e

	'''
	Should config be saved first in case instance is rebooted while modify
	'''
	@property
	def save_config(self):
		try:
			return self._save_config
		except Exception as e :
			raise e
	'''
	Should config be saved first in case instance is rebooted while modify
	'''
	@save_config.setter
	def save_config(self,save_config):
		try :
			if not isinstance(save_config,bool):
				raise TypeError("save_config must be set to bool value")
			self._save_config = save_config
		except Exception as e :
			raise e

	'''
	License server IP address
	'''
	@property
	def LS_IP(self):
		try:
			return self._LS_IP
		except Exception as e :
			raise e
	'''
	License server IP address
	'''
	@LS_IP.setter
	def LS_IP(self,LS_IP):
		try :
			if not isinstance(LS_IP,str):
				raise TypeError("LS_IP must be set to str value")
			self._LS_IP = LS_IP
		except Exception as e :
			raise e

	'''
	Indicates whether config diff exists for this instances or not
	'''
	@property
	def diff_exists(self):
		try:
			return self._diff_exists
		except Exception as e :
			raise e

	'''
	Port assignment will be started from this value
	'''
	@property
	def start_port(self):
		try:
			return self._start_port
		except Exception as e :
			raise e
	'''
	Port assignment will be started from this value
	'''
	@start_port.setter
	def start_port(self,start_port):
		try :
			if not isinstance(start_port,int):
				raise TypeError("start_port must be set to int value")
			self._start_port = start_port
		except Exception as e :
			raise e

	'''
	VLAN Interfaces
	'''
	@property
	def nsvlan_interfaces(self) :
		try:
			return self._nsvlan_interfaces
		except Exception as e :
			raise e
	'''
	VLAN Interfaces
	'''
	@nsvlan_interfaces.setter
	def nsvlan_interfaces(self,nsvlan_interfaces) :
		try :
			if not isinstance(nsvlan_interfaces,list):
				raise TypeError("nsvlan_interfaces must be set to array of str value")
			for item in nsvlan_interfaces :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._nsvlan_interfaces = nsvlan_interfaces
		except Exception as e :
			raise e

	'''
	Use this operation to reboot NetScaler Instance.
	'''

	'''
	Use this operation to reboot NetScaler Instance.
	'''
	@classmethod
	def reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"reboot")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"reboot", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to stop NetScaler Instance.
	'''

	'''
	Use this operation to stop NetScaler Instance.
	'''
	@classmethod
	def stop(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"stop")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"stop", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to add NetScaler Instance.
	'''
	@classmethod
	def add(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"add")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"add", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to provision CPX.
	'''
	@classmethod
	def provision_cpx(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"provision_cpx")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"provision_cpx", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to unmanage NetScaler Instance.
	'''

	'''
	Use this operation to unmanage NetScaler Instance.
	'''
	@classmethod
	def unmanage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"unmanage")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"unmanage", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to force reboot NetScaler Instance.
	'''

	'''
	Use this operation to force reboot NetScaler Instance.
	'''
	@classmethod
	def force_reboot(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"force_reboot")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"force_reboot", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get NetScaler Instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_obj=ns()
				response = ns_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to delete NetScaler Instances.
	'''
	@classmethod
	def delete(cls,client=None,resource=None): 
		try :
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.delete_resource(client)
			else :
					ns_obj=ns()
					return cls.delete_bulk_request(client,resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to modify NetScaler Instance.
	'''
	@classmethod
	def update(cls,client=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.update_resource(client)
			else :
				ns_obj=ns()
				return cls.update_bulk_request(client,resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to force stop NetScaler Instance.
	'''

	'''
	Use this operation to force stop NetScaler Instance.
	'''
	@classmethod
	def force_stop(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"force_stop")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"force_stop", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to manage NetScaler Instance.
	'''

	'''
	Use this operation to manage NetScaler Instance.
	'''
	@classmethod
	def manage(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"manage")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"manage", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to start NetScaler Instance.
	'''

	'''
	Use this operation to start NetScaler Instance.
	'''
	@classmethod
	def start(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"start")
			else : 
				ns_obj= ns()
				return cls.perform_operation_bulk_request(service,"start", resource,ns_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_obj = ns()
			option_ = options()
			option_._filter=filter_
			return ns_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_obj = ns()
			option_ = options()
			option_._count=True
			response = ns_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_obj = ns()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_responses, response, "ns_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_response_array
				i=0
				error = [ns() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_response_array
			i=0
			ns_objs = [ns() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns'):
					for props in obj._ns:
						result = service.payload_formatter.string_to_bulk_resource(ns_response,self.__class__.__name__,props)
						ns_objs[i] = result.ns
						i=i+1
			return ns_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_response(base_response):
	def __init__(self,length=1) :
		self.ns= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns= [ ns() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_responses(base_response):
	def __init__(self,length=1) :
		self.ns_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_response_array = [ ns() for _ in range(length)]
