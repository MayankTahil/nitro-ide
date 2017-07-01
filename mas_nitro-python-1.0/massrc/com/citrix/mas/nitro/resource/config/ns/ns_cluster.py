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
from massrc.com.citrix.mas.nitro.resource.config.ns.ns_clag_node import ns_clag_node


'''
Configuration for ns_cluster resource.
'''

class ns_cluster(base_resource):
	_add_nodegroup= ""
	_mgmt_cpu_usage= ""
	_backplane= ""
	_clusterid= ""
	_nodeid= ""
	_state= ""
	_channel_interface_list=[]
	_totpropagationtimeout= ""
	_totsteeredpkts= ""
	_password= ""
	_clag_intf_list=[]
	_process_local= ""
	_act_id= ""
	_numdfddroppkts= ""
	_clviewleader= ""
	_inc_mode= ""
	_clnumnodes= ""
	_http_req= ""
	_cpu_usage= ""
	_clbkplanerx= ""
	_clnodes= ""
	_clbkplanetx= ""
	_preemption= ""
	_iscco= ""
	_clip= ""
	_operationalstate= ""
	_tx= ""
	_clcurstatus= ""
	_rx= ""
	_memory_usage= ""
	_node_group= ""
	_clbkplanetxrate= ""
	_health= ""
	_clbkplanerxrate= ""
	_nodegroup_list=[]
	_ipaddress= ""
	_profile_name= ""
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
			return "ns_cluster"
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
			return "ns_clusters"
		except Exception as e :
			raise e



	'''
	get Add Node group in cluster instance if this property is true
	'''
	@property
	def add_nodegroup(self) :
		try:
			return self._add_nodegroup
		except Exception as e :
			raise e
	'''
	set Add Node group in cluster instance if this property is true
	'''
	@add_nodegroup.setter
	def add_nodegroup(self,add_nodegroup):
		try :
			if not isinstance(add_nodegroup,bool):
				raise TypeError("add_nodegroup must be set to bool value")
			self._add_nodegroup = add_nodegroup
		except Exception as e :
			raise e


	'''
	get Management CPU Usage (%) of Cluster Instance
	'''
	@property
	def mgmt_cpu_usage(self) :
		try:
			return self._mgmt_cpu_usage
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
	get Array of CLAG nodes that are part of this channel (10/1, 10/4)
	'''
	@property
	def channel_interface_list(self) :
		try:
			return self._channel_interface_list
		except Exception as e :
			raise e
	'''
	set Array of CLAG nodes that are part of this channel (10/1, 10/4)
	'''
	@channel_interface_list.setter
	def channel_interface_list(self,channel_interface_list) :
		try :
			if not isinstance(channel_interface_list,list):
				raise TypeError("channel_interface_list must be set to array of ns_clag_node value")
			for item in channel_interface_list :
				if not isinstance(item,ns_clag_node):
					raise TypeError("item must be set to ns_clag_node value")
			self._channel_interface_list = channel_interface_list
		except Exception as e :
			raise e


	'''
	get Number of times the update to the client timed-out
	'''
	@property
	def totpropagationtimeout(self) :
		try:
			return self._totpropagationtimeout
		except Exception as e :
			raise e


	'''
	get Total number of packets steered on the cluster backplane
	'''
	@property
	def totsteeredpkts(self) :
		try:
			return self._totsteeredpkts
		except Exception as e :
			raise e


	'''
	get Password of the Configuration Coordinator node(Cluster IP)
	'''
	@property
	def password(self) :
		try:
			return self._password
		except Exception as e :
			raise e
	'''
	set Password of the Configuration Coordinator node(Cluster IP)
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
	get CLAG Interface List containing interfaces which aren't shared across nodes and aren't backplanes
	'''
	@property
	def clag_intf_list(self) :
		try:
			return self._clag_intf_list
		except Exception as e :
			raise e
	'''
	set CLAG Interface List containing interfaces which aren't shared across nodes and aren't backplanes
	'''
	@clag_intf_list.setter
	def clag_intf_list(self,clag_intf_list) :
		try :
			if not isinstance(clag_intf_list,list):
				raise TypeError("clag_intf_list must be set to array of str value")
			for item in clag_intf_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._clag_intf_list = clag_intf_list
		except Exception as e :
			raise e


	'''
	get Process Local
	'''
	@property
	def process_local(self) :
		try:
			return self._process_local
		except Exception as e :
			raise e
	'''
	set Process Local
	'''
	@process_local.setter
	def process_local(self,process_local):
		try :
			if not isinstance(process_local,bool):
				raise TypeError("process_local must be set to bool value")
			self._process_local = process_local
		except Exception as e :
			raise e


	'''
	get Activity Id
	'''
	@property
	def act_id(self) :
		try:
			return self._act_id
		except Exception as e :
			raise e


	'''
	get Total number of packets steered on the cluster backplane
	'''
	@property
	def numdfddroppkts(self) :
		try:
			return self._numdfddroppkts
		except Exception as e :
			raise e


	'''
	get Cluster CCO NSIP
	'''
	@property
	def clviewleader(self) :
		try:
			return self._clviewleader
		except Exception as e :
			raise e
	'''
	set Cluster CCO NSIP
	'''
	@clviewleader.setter
	def clviewleader(self,clviewleader):
		try :
			if not isinstance(clviewleader,str):
				raise TypeError("clviewleader must be set to str value")
			self._clviewleader = clviewleader
		except Exception as e :
			raise e


	'''
	get Inc Mode
	'''
	@property
	def inc_mode(self) :
		try:
			return self._inc_mode
		except Exception as e :
			raise e
	'''
	set Inc Mode
	'''
	@inc_mode.setter
	def inc_mode(self,inc_mode):
		try :
			if not isinstance(inc_mode,bool):
				raise TypeError("inc_mode must be set to bool value")
			self._inc_mode = inc_mode
		except Exception as e :
			raise e


	'''
	get Cluster ID
	'''
	@property
	def clnumnodes(self) :
		try:
			return self._clnumnodes
		except Exception as e :
			raise e
	'''
	set Cluster ID
	'''
	@clnumnodes.setter
	def clnumnodes(self,clnumnodes):
		try :
			if not isinstance(clnumnodes,int):
				raise TypeError("clnumnodes must be set to int value")
			self._clnumnodes = clnumnodes
		except Exception as e :
			raise e


	'''
	get HTTP Requests/second on Cluster Instance
	'''
	@property
	def http_req(self) :
		try:
			return self._http_req
		except Exception as e :
			raise e


	'''
	get CPU Usage (%) of Cluster Instance
	'''
	@property
	def cpu_usage(self) :
		try:
			return self._cpu_usage
		except Exception as e :
			raise e


	'''
	get Traffic received on backplane (in mbits)
	'''
	@property
	def clbkplanerx(self) :
		try:
			return self._clbkplanerx
		except Exception as e :
			raise e


	'''
	get List of Nodes part of Cluster
	'''
	@property
	def clnodes(self) :
		try:
			return self._clnodes
		except Exception as e :
			raise e
	'''
	set List of Nodes part of Cluster
	'''
	@clnodes.setter
	def clnodes(self,clnodes):
		try :
			if not isinstance(clnodes,str):
				raise TypeError("clnodes must be set to str value")
			self._clnodes = clnodes
		except Exception as e :
			raise e


	'''
	get Traffic transmitted from backplane (in mbits)
	'''
	@property
	def clbkplanetx(self) :
		try:
			return self._clbkplanetx
		except Exception as e :
			raise e


	'''
	get Preemption
	'''
	@property
	def preemption(self) :
		try:
			return self._preemption
		except Exception as e :
			raise e
	'''
	set Preemption
	'''
	@preemption.setter
	def preemption(self,preemption):
		try :
			if not isinstance(preemption,bool):
				raise TypeError("preemption must be set to bool value")
			self._preemption = preemption
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
	get Cluster IPAddress
	'''
	@property
	def clip(self) :
		try:
			return self._clip
		except Exception as e :
			raise e
	'''
	set Cluster IPAddress
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
	get Cluster Operational State
	'''
	@property
	def operationalstate(self) :
		try:
			return self._operationalstate
		except Exception as e :
			raise e


	'''
	get Out Throughput of Cluster Instance in Mbps
	'''
	@property
	def tx(self) :
		try:
			return self._tx
		except Exception as e :
			raise e


	'''
	get State of the cluster
	'''
	@property
	def clcurstatus(self) :
		try:
			return self._clcurstatus
		except Exception as e :
			raise e


	'''
	get In Throughput of Cluster Instance in Mbps
	'''
	@property
	def rx(self) :
		try:
			return self._rx
		except Exception as e :
			raise e


	'''
	get Memory Usage (%) of Cluster Instance
	'''
	@property
	def memory_usage(self) :
		try:
			return self._memory_usage
		except Exception as e :
			raise e


	'''
	get Node group
	'''
	@property
	def node_group(self) :
		try:
			return self._node_group
		except Exception as e :
			raise e
	'''
	set Node group
	'''
	@node_group.setter
	def node_group(self,node_group):
		try :
			if not isinstance(node_group,str):
				raise TypeError("node_group must be set to str value")
			self._node_group = node_group
		except Exception as e :
			raise e


	'''
	get Traffic rate transmitted from backplane (in mbits)
	'''
	@property
	def clbkplanetxrate(self) :
		try:
			return self._clbkplanetxrate
		except Exception as e :
			raise e


	'''
	get Node Health State
	'''
	@property
	def health(self) :
		try:
			return self._health
		except Exception as e :
			raise e


	'''
	get Traffic rate received on backplane (in mbits)
	'''
	@property
	def clbkplanerxrate(self) :
		try:
			return self._clbkplanerxrate
		except Exception as e :
			raise e


	'''
	get Available Node group list on this cluster
	'''
	@property
	def nodegroup_list(self) :
		try:
			return self._nodegroup_list
		except Exception as e :
			raise e
	'''
	set Available Node group list on this cluster
	'''
	@nodegroup_list.setter
	def nodegroup_list(self,nodegroup_list) :
		try :
			if not isinstance(nodegroup_list,list):
				raise TypeError("nodegroup_list must be set to array of str value")
			for item in nodegroup_list :
				if not isinstance(item,str):
					raise TypeError("item must be set to str value")
			self._nodegroup_list = nodegroup_list
		except Exception as e :
			raise e


	'''
	get NS ipaddress
	'''
	@property
	def ipaddress(self) :
		try:
			return self._ipaddress
		except Exception as e :
			raise e
	'''
	set NS ipaddress
	'''
	@ipaddress.setter
	def ipaddress(self,ipaddress):
		try :
			if not isinstance(ipaddress,str):
				raise TypeError("ipaddress must be set to str value")
			self._ipaddress = ipaddress
		except Exception as e :
			raise e


	'''
	get Profile Name
	'''
	@property
	def profile_name(self) :
		try:
			return self._profile_name
		except Exception as e :
			raise e
	'''
	set Profile Name
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
	Use this operation to remove entire Cluster Instance.
	'''
	@classmethod
	def remove(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"remove")
			else : 
				ns_cluster_obj= ns_cluster()
				return cls.perform_operation_bulk_request(service,"remove", resource,ns_cluster_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to get ns cluster instance.
	'''
	@classmethod
	def get(cls,client = None,resource="",option_=""): 
		try:
			response=""
			if not resource :
				ns_cluster_obj=ns_cluster()
				response = ns_cluster_obj.get_resources(client,option_)
			else:
				response = resource.get_resource(client, option_)
			return response
		except Exception as e :
			raise e

	'''
	Use this operation to modify Cluster IP admin ns password.
	'''
	@classmethod
	def modify_password(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"modify_password")
			else : 
				ns_cluster_obj= ns_cluster()
				return cls.perform_operation_bulk_request(service,"modify_password", resource,ns_cluster_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to form one node cluster from NetScaler Instance.
	'''
	@classmethod
	def form_cluster(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"form_cluster")
			else : 
				ns_cluster_obj= ns_cluster()
				return cls.perform_operation_bulk_request(service,"form_cluster", resource,ns_cluster_obj)
		except Exception as e :
			raise e

	'''
	Use this operation to join NetScaler Instance to existing cluster.
	'''
	@classmethod
	def join(cls,service=None,resource=None):
		try:
			if resource is None :
				raise Exception("Resource Object Not Found")
			if type(resource) is not list :
				return resource.perform_operation(service,"join")
			else : 
				ns_cluster_obj= ns_cluster()
				return cls.perform_operation_bulk_request(service,"join", resource,ns_cluster_obj)
		except Exception as e :
			raise e

	'''
	Use this API to fetch filtered set of ns_cluster resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def get_filtered(cls,service,filter_) :
		try:
			ns_cluster_obj = ns_cluster()
			option_ = options()
			option_._filter=filter_
			return ns_cluster_obj.getfiltered(service, option_)
		except Exception as e :
			raise e

	'''
	* Use this API to count the ns_cluster resources.
	'''
	@classmethod
	def count(cls,service) :
		try:
			ns_cluster_obj = ns_cluster()
			option_ = options()
			option_._count=True
			response = ns_cluster_obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	'''
	Use this API to count the filtered set of ns_cluster resources.
	filter string should be in JSON format.eg: "vm_state:DOWN,name:[a-z]+"
	'''
	@classmethod
	def count_filtered(cls,service,filter_):
		try:
			ns_cluster_obj = ns_cluster()
			option_ = options()
			option_._count=True
			option_._filter=filter_
			response = ns_cluster_obj.getfiltered(service, option_)
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
			result=service.payload_formatter.string_to_resource(ns_cluster_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ns_cluster
		except Exception as e :
			raise e


	'''
	Converts API response into object and returns the object array .
	'''
	def get_nitro_bulk_response(self,service ,response):
		try :
			result=service.payload_formatter.string_to_resource(ns_cluster_responses, response, "ns_cluster_response_array")
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				response = result.ns_cluster_response_array
				i=0
				error = [ns_cluster() for _ in range(len(response))]
				for obj in response :
					error[i]= obj._message
					i=i+1
				raise nitro_exception(result.errorcode, str(result.message), error)
			response = result.ns_cluster_response_array
			i=0
			ns_cluster_objs = [ns_cluster() for _ in range(len(response))]
			for obj in response :
				if hasattr(obj,'_ns_cluster'):
					for props in obj._ns_cluster:
						result = service.payload_formatter.string_to_bulk_resource(ns_cluster_response,self.__class__.__name__,props)
						ns_cluster_objs[i] = result.ns_cluster
						i=i+1
			return ns_cluster_objs
		except Exception as e :
			raise e


	'''
	Performs generic data validation for the operation to be performed
	'''
	def validate(self,operationType):
		try:
			super(ns_cluster,self).validate()
		except Exception as e :
			raise e

'''
Forms the proper response.
'''
class ns_cluster_response(base_response):
	def __init__(self,length=1) :
		self.ns_cluster= []
		self.errorcode = 0 
		self.message = "" 
		self.severity = "" 
		self.ns_cluster= [ ns_cluster() for _ in range(length)]
'''
Forms the proper response for bulk operation.
'''
class ns_cluster_responses(base_response):
	def __init__(self,length=1) :
		self.ns_cluster_response_array = []
		self.errorcode = 0 
		self.message = "" 
		self.ns_cluster_response_array = [ ns_cluster() for _ in range(length)]
