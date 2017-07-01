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

class qos_stats(base_resource) :
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._snmpqosqos_packets_received = 0
		self._snmpqosqos_packets_receivedrate = 0
		self._snmpqosqos_packets_sent = 0
		self._snmpqosqos_packets_sentrate = 0
		self._snmpqosqos_packets_bypassed = 0
		self._snmpqosqos_packets_bypassedrate = 0
		self._snmpqosqos_packets_dropped = 0
		self._snmpqosqos_packets_droppedrate = 0
		self._snmpqosqos_bytes_rx = 0
		self._snmpqosqos_bytes_rxrate = 0
		self._snmpqosqos_bytes_tx = 0
		self._snmpqosqos_bytes_txrate = 0
		self._snmpqosqos_lazy_bytes = 0
		self._snmpqosqos_lazy_bytesrate = 0
		self._snmpqosqos_real_bytes = 0
		self._snmpqosqos_real_bytesrate = 0
		self._snmpqosqos_packets_filtered = 0
		self._snmpqosqos_packets_filteredrate = 0
		self._snmpqosqos_packets_classified = 0
		self._snmpqosqos_packets_classifiedrate = 0
		self._snmpqosqos_flows = 0
		self._snmpqosqos_flowsrate = 0
		self._snmpqosqos_flow_recycles = 0
		self._snmpqosqos_flow_recyclesrate = 0
		self._snmpqosqos_session_recycle_failure = 0
		self._snmpqosqos_session_recycle_failurerate = 0
		self._snmpqosqos_sessions_ignored = 0
		self._snmpqosqos_sessions_ignoredrate = 0
		self._snmpqosqos_sessions_consumed = 0
		self._snmpqosqos_sessions_consumedrate = 0
		self._snmpqosqos_actions_created = 0
		self._snmpqosqos_actions_createdrate = 0
		self._snmpqosqos_policy_reeval = 0
		self._snmpqosqos_policy_reevalrate = 0
		self._snmpqosqos_cfy_tcp_unknown = 0
		self._snmpqosqos_cfy_tcp_unknownrate = 0
		self._snmpqosqos_cfy_udp_unknown = 0
		self._snmpqosqos_cfy_udp_unknownrate = 0
		self._snmpqosqos_sch_leafs = 0
		self._snmpqosqos_sch_leafsrate = 0
		self._snmpqosqos_session_mem = 0
		self._snmpqosqos_session_memrate = 0
		self._snmpqosqos_sch_virtual_packets = 0
		self._snmpqosqos_sch_virtual_packetsrate = 0
		self._snmpqosqos_sch_virtual_bytes_accepted = 0
		self._snmpqosqos_sch_virtual_bytes_acceptedrate = 0
		self._snmpqosqos_sch_leaf_recycle_failures = 0
		self._snmpqosqos_sch_leaf_recycle_failuresrate = 0
		self._snmpqosqos_sch_node_regulated_count = 0
		self._snmpqosqos_sch_node_regulated_countrate = 0
		self._snmpqosqos_sch_sessions_created = 0
		self._snmpqosqos_sch_sessions_createdrate = 0
		self._snmpqosqos_sch_sessions_deleted = 0
		self._snmpqosqos_sch_sessions_deletedrate = 0
		self._snmpqosqos_sch_sdrr_nodes = 0
		self._snmpqosqos_sch_sdrr_nodesrate = 0
		self._snmpqosqos_sch_session_conns = 0
		self._snmpqosqos_sch_session_connsrate = 0
		self._snmpqosqos_sch_session_conns_removed = 0
		self._snmpqosqos_sch_session_conns_removedrate = 0
		self._snmpqosqos_sch_sessions_regulated_count = 0
		self._snmpqosqos_sch_sessions_regulated_countrate = 0
		self._snmpqosqos_sch_sessions_byte_count = 0
		self._snmpqosqos_sch_sessions_byte_countrate = 0
		self._snmpqosqos_sch_regulated_count = 0
		self._snmpqosqos_sch_regulated_countrate = 0
		self._snmpqosqos_sch_links_created = 0
		self._snmpqosqos_sch_links_createdrate = 0
		self._snmpqosqos_sch_links_deleted = 0
		self._snmpqosqos_sch_links_deletedrate = 0
		self._snmpqosqos_sch_links_updated = 0
		self._snmpqosqos_sch_links_updatedrate = 0
		self._snmpqosqos_sch_poll_count = 0
		self._snmpqosqos_sch_poll_countrate = 0
		self._snmpqosqos_sch_peer_msgs = 0
		self._snmpqosqos_sch_peer_msgsrate = 0
		self._snmpqosqos_error_ipc = 0
		self._snmpqosqos_error_ipcrate = 0
		self._snmpqosqos_flow_mem = 0
		self._snmpqosqos_flow_memrate = 0
		self._snmpqosqos_recycle_failed_backlog = 0
		self._snmpqosqos_recycle_failed_backlograte = 0
		self._snmpqosqos_recycle_failed_session = 0
		self._snmpqosqos_recycle_failed_sessionrate = 0
		self._snmpqosqos_error_create_action_failed = 0
		self._snmpqosqos_error_create_action_failedrate = 0
		self._snmpqosqos_error_modify_action_failed = 0
		self._snmpqosqos_error_modify_action_failedrate = 0
		self._snmpqosqos_error_remove_action_failed = 0
		self._snmpqosqos_error_remove_action_failedrate = 0
		self._snmpqosqos_error_cli_unknown = 0
		self._snmpqosqos_error_cli_unknownrate = 0
		self._snmpqosqos_error_rename_not_implemented = 0
		self._snmpqosqos_error_rename_not_implementedrate = 0
		self._snmpqosqos_error_remove_policy_failed = 0
		self._snmpqosqos_error_remove_policy_failedrate = 0
		self._snmpqosqos_error_create_policy_failed = 0
		self._snmpqosqos_error_create_policy_failedrate = 0
		self._snmpqosqos_error_libqos_api_failures = 0
		self._snmpqosqos_error_libqos_api_failuresrate = 0
		self._snmpqosqos_error_api_ses_invalidpcb = 0
		self._snmpqosqos_error_api_ses_invalidpcbrate = 0
		self._snmpqosqos_error_api_ses_notready = 0
		self._snmpqosqos_error_api_ses_notreadyrate = 0
		self._snmpqosqos_error_api_ses_add_insession = 0
		self._snmpqosqos_error_api_ses_add_insessionrate = 0
		self._snmpqosqos_error_api_ses_add_other = 0
		self._snmpqosqos_error_api_ses_add_otherrate = 0
		self._snmpqosqos_error_api_ses_rem_notinsession = 0
		self._snmpqosqos_error_api_ses_rem_notinsessionrate = 0
		self._snmpqosqos_error_api_ses_rem_other = 0
		self._snmpqosqos_error_api_ses_rem_otherrate = 0
		self._snmpqosqos_error_api_ses_del = 0
		self._snmpqosqos_error_api_ses_delrate = 0

	@property
	def name(self) :
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def snmpqosqos_cfy_udp_unknownrate(self) :
		r"""Rate (/s) counter for snmpqosqos_cfy_udp_unknown.
		"""
		try :
			return self._snmpqosqos_cfy_udp_unknownrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flow_memrate(self) :
		r"""Rate (/s) counter for snmpqosqos_flow_mem.
		"""
		try :
			return self._snmpqosqos_flow_memrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_createdrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_sessions_created.
		"""
		try :
			return self._snmpqosqos_sch_sessions_createdrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_peer_msgs(self) :
		r"""Scheduler peer messages received.
		"""
		try :
			return self._snmpqosqos_sch_peer_msgs
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_classified(self) :
		r"""Total packets classified by QoS.
		"""
		try :
			return self._snmpqosqos_packets_classified
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_session_conns_removed(self) :
		r"""Scheduler session connections removed.
		"""
		try :
			return self._snmpqosqos_sch_session_conns_removed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_regulated_countrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_regulated_count.
		"""
		try :
			return self._snmpqosqos_sch_regulated_countrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_actions_createdrate(self) :
		r"""Rate (/s) counter for snmpqosqos_actions_created.
		"""
		try :
			return self._snmpqosqos_actions_createdrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_virtual_bytes_acceptedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_virtual_bytes_accepted.
		"""
		try :
			return self._snmpqosqos_sch_virtual_bytes_acceptedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flowsrate(self) :
		r"""Rate (/s) counter for snmpqosqos_flows.
		"""
		try :
			return self._snmpqosqos_flowsrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_droppedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_dropped.
		"""
		try :
			return self._snmpqosqos_packets_droppedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_lazy_bytesrate(self) :
		r"""Rate (/s) counter for snmpqosqos_lazy_bytes.
		"""
		try :
			return self._snmpqosqos_lazy_bytesrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_remove_policy_failed(self) :
		r"""Failed attempts to remove qos policy.
		"""
		try :
			return self._snmpqosqos_error_remove_policy_failed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_deleted(self) :
		r"""Scheduler links deleted.
		"""
		try :
			return self._snmpqosqos_sch_links_deleted
		except Exception as e:
			raise e

	@property
	def snmpqosqos_recycle_failed_backlograte(self) :
		r"""Rate (/s) counter for snmpqosqos_recycle_failed_backlog.
		"""
		try :
			return self._snmpqosqos_recycle_failed_backlograte
		except Exception as e:
			raise e

	@property
	def snmpqosqos_real_bytesrate(self) :
		r"""Rate (/s) counter for snmpqosqos_real_bytes.
		"""
		try :
			return self._snmpqosqos_real_bytesrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_session_recycle_failurerate(self) :
		r"""Rate (/s) counter for snmpqosqos_session_recycle_failure.
		"""
		try :
			return self._snmpqosqos_session_recycle_failurerate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_cfy_tcp_unknown(self) :
		r"""Connections unable to be classified beyond TCP.
		"""
		try :
			return self._snmpqosqos_cfy_tcp_unknown
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_rename_not_implementedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_rename_not_implemented.
		"""
		try :
			return self._snmpqosqos_error_rename_not_implementedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sessions_ignoredrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sessions_ignored.
		"""
		try :
			return self._snmpqosqos_sessions_ignoredrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_bytes_rx(self) :
		r"""Received bytes processed by QoS.
		"""
		try :
			return self._snmpqosqos_bytes_rx
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_remove_action_failed(self) :
		r"""Failed attempts to remove actions.
		"""
		try :
			return self._snmpqosqos_error_remove_action_failed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_filtered(self) :
		r"""Total packets filtered by QoS.
		"""
		try :
			return self._snmpqosqos_packets_filtered
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_add_insessionrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_add_insession.
		"""
		try :
			return self._snmpqosqos_error_api_ses_add_insessionrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_notready(self) :
		r"""Libqos api qos_session_add_pcb/natpcb() failed for reason QS_ENOTREADY.
		"""
		try :
			return self._snmpqosqos_error_api_ses_notready
		except Exception as e:
			raise e

	@property
	def snmpqosqos_recycle_failed_backlog(self) :
		r"""recycle failed backlog.
		"""
		try :
			return self._snmpqosqos_recycle_failed_backlog
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_session_connsrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_session_conns.
		"""
		try :
			return self._snmpqosqos_sch_session_connsrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_create_action_failed(self) :
		r"""Failed attempts to create actions.
		"""
		try :
			return self._snmpqosqos_error_create_action_failed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_virtual_packets(self) :
		r"""Scheduler virtual packets constructed.
		"""
		try :
			return self._snmpqosqos_sch_virtual_packets
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_sent(self) :
		r"""Send direction packets processed by QoS.
		"""
		try :
			return self._snmpqosqos_packets_sent
		except Exception as e:
			raise e

	@property
	def snmpqosqos_session_memrate(self) :
		r"""Rate (/s) counter for snmpqosqos_session_mem.
		"""
		try :
			return self._snmpqosqos_session_memrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_invalidpcb(self) :
		r"""Libqos api qos_session_add_pcb/natpcb() failed for reason QS_EINVALIDPCB.
		"""
		try :
			return self._snmpqosqos_error_api_ses_invalidpcb
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_rename_not_implemented(self) :
		r"""qos action rename not yet implemented.
		"""
		try :
			return self._snmpqosqos_error_rename_not_implemented
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_createdrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_links_created.
		"""
		try :
			return self._snmpqosqos_sch_links_createdrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_bytes_rxrate(self) :
		r"""Rate (/s) counter for snmpqosqos_bytes_rx.
		"""
		try :
			return self._snmpqosqos_bytes_rxrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_invalidpcbrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_invalidpcb.
		"""
		try :
			return self._snmpqosqos_error_api_ses_invalidpcbrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_leaf_recycle_failures(self) :
		r"""Scheduler Failures to recycle QoS flows.
		"""
		try :
			return self._snmpqosqos_sch_leaf_recycle_failures
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_modify_action_failed(self) :
		r"""Failed attempts to modify actions.
		"""
		try :
			return self._snmpqosqos_error_modify_action_failed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_create_policy_failed(self) :
		r"""Failed attempts to create qos policy.
		"""
		try :
			return self._snmpqosqos_error_create_policy_failed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_receivedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_received.
		"""
		try :
			return self._snmpqosqos_packets_receivedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_deletedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_links_deleted.
		"""
		try :
			return self._snmpqosqos_sch_links_deletedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_policy_reeval(self) :
		r"""Policies re-evaluated due to cli change.
		"""
		try :
			return self._snmpqosqos_policy_reeval
		except Exception as e:
			raise e

	@property
	def snmpqosqos_real_bytes(self) :
		r"""QoS actual bytes scheduled.
		"""
		try :
			return self._snmpqosqos_real_bytes
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_add_insession(self) :
		r"""Libqos api qos_session_add_pcb/natpcb() failed for reason QS_EINSESSION.
		"""
		try :
			return self._snmpqosqos_error_api_ses_add_insession
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_add_other(self) :
		r"""Libqos api qos_session_add_pcb/natpcb() failed.
		"""
		try :
			return self._snmpqosqos_error_api_ses_add_other
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_deleted(self) :
		r"""Scheduler session classes constructed.
		"""
		try :
			return self._snmpqosqos_sch_sessions_deleted
		except Exception as e:
			raise e

	@property
	def snmpqosqos_bytes_tx(self) :
		r"""Sent bytes processed by QoS.
		"""
		try :
			return self._snmpqosqos_bytes_tx
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_classifiedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_classified.
		"""
		try :
			return self._snmpqosqos_packets_classifiedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_libqos_api_failures(self) :
		r"""Libqos api failures.
		"""
		try :
			return self._snmpqosqos_error_libqos_api_failures
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_create_action_failedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_create_action_failed.
		"""
		try :
			return self._snmpqosqos_error_create_action_failedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_del(self) :
		r"""Libqos api qos_session_delete faled.
		"""
		try :
			return self._snmpqosqos_error_api_ses_del
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_filteredrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_filtered.
		"""
		try :
			return self._snmpqosqos_packets_filteredrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_session_recycle_failure(self) :
		r"""QoS Flow Recycle failures.
		"""
		try :
			return self._snmpqosqos_session_recycle_failure
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_virtual_packetsrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_virtual_packets.
		"""
		try :
			return self._snmpqosqos_sch_virtual_packetsrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_bytes_txrate(self) :
		r"""Rate (/s) counter for snmpqosqos_bytes_tx.
		"""
		try :
			return self._snmpqosqos_bytes_txrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_bypassed(self) :
		r"""Packets bypassing QoS.
		"""
		try :
			return self._snmpqosqos_packets_bypassed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_cfy_udp_unknown(self) :
		r"""Connections unable to be classified beyond UDP.
		"""
		try :
			return self._snmpqosqos_cfy_udp_unknown
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_received(self) :
		r"""Receive direction packets processed by QoS.
		"""
		try :
			return self._snmpqosqos_packets_received
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_create_policy_failedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_create_policy_failed.
		"""
		try :
			return self._snmpqosqos_error_create_policy_failedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_delrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_del.
		"""
		try :
			return self._snmpqosqos_error_api_ses_delrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flow_mem(self) :
		r"""DPI inspection state invalid.
		"""
		try :
			return self._snmpqosqos_flow_mem
		except Exception as e:
			raise e

	@property
	def snmpqosqos_session_mem(self) :
		r"""Scheduler nodes constructed.
		"""
		try :
			return self._snmpqosqos_session_mem
		except Exception as e:
			raise e

	@property
	def snmpqosqos_recycle_failed_sessionrate(self) :
		r"""Rate (/s) counter for snmpqosqos_recycle_failed_session.
		"""
		try :
			return self._snmpqosqos_recycle_failed_sessionrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_poll_count(self) :
		r"""Scheduler calls to poll_libqos.
		"""
		try :
			return self._snmpqosqos_sch_poll_count
		except Exception as e:
			raise e

	@property
	def snmpqosqos_lazy_bytes(self) :
		r"""QoS lazy byte optimization rate.
		"""
		try :
			return self._snmpqosqos_lazy_bytes
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_remove_action_failedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_remove_action_failed.
		"""
		try :
			return self._snmpqosqos_error_remove_action_failedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_regulated_count(self) :
		r"""Scheduler regulated sessions count.
		"""
		try :
			return self._snmpqosqos_sch_sessions_regulated_count
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_add_otherrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_add_other.
		"""
		try :
			return self._snmpqosqos_error_api_ses_add_otherrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_rem_otherrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_rem_other.
		"""
		try :
			return self._snmpqosqos_error_api_ses_rem_otherrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_recycle_failed_session(self) :
		r"""qos recycle failures because of associated session.
		"""
		try :
			return self._snmpqosqos_recycle_failed_session
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_byte_countrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_sessions_byte_count.
		"""
		try :
			return self._snmpqosqos_sch_sessions_byte_countrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_updated(self) :
		r"""Scheduler links updated.
		"""
		try :
			return self._snmpqosqos_sch_links_updated
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sdrr_nodes(self) :
		r"""Scheduler sdrr nodes constructed.
		"""
		try :
			return self._snmpqosqos_sch_sdrr_nodes
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_peer_msgsrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_peer_msgs.
		"""
		try :
			return self._snmpqosqos_sch_peer_msgsrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_session_conns(self) :
		r"""Scheduler session connections created.
		"""
		try :
			return self._snmpqosqos_sch_session_conns
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_libqos_api_failuresrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_libqos_api_failures.
		"""
		try :
			return self._snmpqosqos_error_libqos_api_failuresrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_cli_unknownrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_cli_unknown.
		"""
		try :
			return self._snmpqosqos_error_cli_unknownrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_actions_created(self) :
		r"""Uneque qos action objects created.
		"""
		try :
			return self._snmpqosqos_actions_created
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_virtual_bytes_accepted(self) :
		r"""Scheduler bytes accepted.
		"""
		try :
			return self._snmpqosqos_sch_virtual_bytes_accepted
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sessions_consumed(self) :
		r"""sessions manually consumed.
		"""
		try :
			return self._snmpqosqos_sessions_consumed
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_remove_policy_failedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_remove_policy_failed.
		"""
		try :
			return self._snmpqosqos_error_remove_policy_failedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_cli_unknown(self) :
		r"""Internal CLI error.
		"""
		try :
			return self._snmpqosqos_error_cli_unknown
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flow_recycles(self) :
		r"""Recycled QoS flows.
		"""
		try :
			return self._snmpqosqos_flow_recycles
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_deletedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_sessions_deleted.
		"""
		try :
			return self._snmpqosqos_sch_sessions_deletedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_poll_countrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_poll_count.
		"""
		try :
			return self._snmpqosqos_sch_poll_countrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_node_regulated_countrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_node_regulated_count.
		"""
		try :
			return self._snmpqosqos_sch_node_regulated_countrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_rem_notinsession(self) :
		r"""Libqos api qos_session_rem_pcb/natpcb() failed for reason QS_ENOTINSESSION.
		"""
		try :
			return self._snmpqosqos_error_api_ses_rem_notinsession
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flows(self) :
		r"""New QoS flows.
		"""
		try :
			return self._snmpqosqos_flows
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_regulated_countrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_sessions_regulated_count.
		"""
		try :
			return self._snmpqosqos_sch_sessions_regulated_countrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_session_conns_removedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_session_conns_removed.
		"""
		try :
			return self._snmpqosqos_sch_session_conns_removedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_byte_count(self) :
		r"""Scheduler session bytes total.
		"""
		try :
			return self._snmpqosqos_sch_sessions_byte_count
		except Exception as e:
			raise e

	@property
	def snmpqosqos_flow_recyclesrate(self) :
		r"""Rate (/s) counter for snmpqosqos_flow_recycles.
		"""
		try :
			return self._snmpqosqos_flow_recyclesrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_leafs(self) :
		r"""Scheduler leaf nodes constructed.
		"""
		try :
			return self._snmpqosqos_sch_leafs
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_rem_other(self) :
		r"""Libqos api qos_session_rem_pcb/natpcb() failed.
		"""
		try :
			return self._snmpqosqos_error_api_ses_rem_other
		except Exception as e:
			raise e

	@property
	def snmpqosqos_policy_reevalrate(self) :
		r"""Rate (/s) counter for snmpqosqos_policy_reeval.
		"""
		try :
			return self._snmpqosqos_policy_reevalrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_created(self) :
		r"""Scheduler links created.
		"""
		try :
			return self._snmpqosqos_sch_links_created
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_notreadyrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_notready.
		"""
		try :
			return self._snmpqosqos_error_api_ses_notreadyrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_ipcrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_ipc.
		"""
		try :
			return self._snmpqosqos_error_ipcrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_modify_action_failedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_modify_action_failed.
		"""
		try :
			return self._snmpqosqos_error_modify_action_failedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_regulated_count(self) :
		r"""Scheduler regulated node count.
		"""
		try :
			return self._snmpqosqos_sch_regulated_count
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sessions_created(self) :
		r"""Scheduler session classes constructed.
		"""
		try :
			return self._snmpqosqos_sch_sessions_created
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_api_ses_rem_notinsessionrate(self) :
		r"""Rate (/s) counter for snmpqosqos_error_api_ses_rem_notinsession.
		"""
		try :
			return self._snmpqosqos_error_api_ses_rem_notinsessionrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_leafsrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_leafs.
		"""
		try :
			return self._snmpqosqos_sch_leafsrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_node_regulated_count(self) :
		r"""Scheduler Regulated node count.
		"""
		try :
			return self._snmpqosqos_sch_node_regulated_count
		except Exception as e:
			raise e

	@property
	def snmpqosqos_error_ipc(self) :
		r"""IPC failed for QoS messages.
		"""
		try :
			return self._snmpqosqos_error_ipc
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_leaf_recycle_failuresrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_leaf_recycle_failures.
		"""
		try :
			return self._snmpqosqos_sch_leaf_recycle_failuresrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_dropped(self) :
		r"""Total packets dropped.
		"""
		try :
			return self._snmpqosqos_packets_dropped
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sessions_consumedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sessions_consumed.
		"""
		try :
			return self._snmpqosqos_sessions_consumedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sessions_ignored(self) :
		r"""Sessions manually ignored.
		"""
		try :
			return self._snmpqosqos_sessions_ignored
		except Exception as e:
			raise e

	@property
	def snmpqosqos_cfy_tcp_unknownrate(self) :
		r"""Rate (/s) counter for snmpqosqos_cfy_tcp_unknown.
		"""
		try :
			return self._snmpqosqos_cfy_tcp_unknownrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_sdrr_nodesrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_sdrr_nodes.
		"""
		try :
			return self._snmpqosqos_sch_sdrr_nodesrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_sch_links_updatedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_sch_links_updated.
		"""
		try :
			return self._snmpqosqos_sch_links_updatedrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_sentrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_sent.
		"""
		try :
			return self._snmpqosqos_packets_sentrate
		except Exception as e:
			raise e

	@property
	def snmpqosqos_packets_bypassedrate(self) :
		r"""Rate (/s) counter for snmpqosqos_packets_bypassed.
		"""
		try :
			return self._snmpqosqos_packets_bypassedrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(qos_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.qos
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all qos_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = qos_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class qos_response(base_response) :
	def __init__(self, length=1) :
		self.qos = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.qos = [qos_stats() for _ in range(length)]

