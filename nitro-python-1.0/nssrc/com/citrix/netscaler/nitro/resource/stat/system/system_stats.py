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

class system_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._voltagev12n = 0
		self._voltagev5n = 0
		self._cpuusage = 0
		self._rescpuusage = 0
		self._slavecpuusage = 0
		self._mastercpuusage = 0
		self._auxvolt7 = 0
		self._auxvolt6 = 0
		self._auxvolt5 = 0
		self._auxvolt4 = 0
		self._auxvolt3 = 0
		self._auxvolt2 = 0
		self._auxvolt1 = 0
		self._auxvolt0 = 0
		self._voltagevsen2 = 0
		self._voltagev5sb = 0
		self._voltagevtt = 0
		self._voltagevbat = 0
		self._voltagev12p = 0
		self._voltagev5p = 0
		self._voltagev33stby = 0
		self._voltagev33main = 0
		self._voltagevcc1 = 0
		self._voltagevcc0 = 0
		self._numcpus = 0
		self._memusagepcnt = 0
		self._memuseinmb = 0
		self._addimgmtcpuusagepcnt = 0
		self._mgmtcpu0usagepcnt = 0
		self._mgmtcpuusagepcnt = 0
		self._pktcpuusagepcnt = 0
		self._cpuusagepcnt = 0
		self._rescpuusagepcnt = 0
		self._starttime = ""
		self._disk0perusage = 0
		self._disk1perusage = 0
		self._cpufan0speed = 0
		self._cpufan1speed = 0
		self._systemfanspeed = 0
		self._fan0speed = 0
		self._fanspeed = 0
		self._cpu0temp = 0
		self._cpu1temp = 0
		self._internaltemp = 0
		self._powersupply1status = ""
		self._powersupply2status = ""
		self._powersupply3status = ""
		self._powersupply4status = ""
		self._disk0size = 0
		self._disk0used = 0
		self._disk0avail = 0
		self._disk1size = 0
		self._disk1used = 0
		self._disk1avail = 0
		self._fan2speed = 0
		self._fan3speed = 0
		self._fan4speed = 0
		self._fan5speed = 0
		self._auxtemp0 = 0
		self._auxtemp1 = 0
		self._auxtemp2 = 0
		self._auxtemp3 = 0
		self._timesincestart = ""
		self._memsizemb = 0

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
	def voltagevbat(self) :
		r"""Onboard battery power supply output. 9800 and 9950 platforms display standard value of 5.0V.
		"""
		try :
			return self._voltagevbat
		except Exception as e:
			raise e

	@property
	def auxvolt2(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 2.
		"""
		try :
			return self._auxvolt2
		except Exception as e:
			raise e

	@property
	def addimgmtcpuusagepcnt(self) :
		r""" Additonal Management CPU utilization percentage.
		"""
		try :
			return self._addimgmtcpuusagepcnt
		except Exception as e:
			raise e

	@property
	def voltagev5n(self) :
		r"""Power supply -5V output. Acceptable range is -5.50 through -4.50 volts. 9800 and 9960 platforms display standard value of -5.0V.
		"""
		try :
			return self._voltagev5n
		except Exception as e:
			raise e

	@property
	def auxvolt7(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 7.
		"""
		try :
			return self._auxvolt7
		except Exception as e:
			raise e

	@property
	def cpu0temp(self) :
		r"""CPU 0 temperature. 9800 and 9960 platforms display internal chip temperature. This is a critical counter.
		You can configure CPU 0 Temperature by using the Set snmp alarm TEMPERATURE-HIGH command to set the upper limit.
		.
		"""
		try :
			return self._cpu0temp
		except Exception as e:
			raise e

	@property
	def fan0speed(self) :
		r"""System fan 1 speed. For new platforms associated pin is connected to CPU supporting fans. For platforms in which it is not connected, it will point to System Fan.
		"""
		try :
			return self._fan0speed
		except Exception as e:
			raise e

	@property
	def disk1perusage(self) :
		r"""Used space in /var partition of the disk, as a percentage. This is a critical counter. You can configure /var Used (%) by using the Set snmp alarm DISK-USAGE-HIGH command.
		"""
		try :
			return self._disk1perusage
		except Exception as e:
			raise e

	@property
	def rescpuusagepcnt(self) :
		r"""Average CPU utilization percentage. Not applicable for a single-CPU system.
		"""
		try :
			return self._rescpuusagepcnt
		except Exception as e:
			raise e

	@property
	def disk1used(self) :
		r"""Used space in /var partition of the hard disk.
		"""
		try :
			return self._disk1used
		except Exception as e:
			raise e

	@property
	def disk1avail(self) :
		r"""Available space in /var partition of the hard disk.
		"""
		try :
			return self._disk1avail
		except Exception as e:
			raise e

	@property
	def fan4speed(self) :
		r"""Speed of Fan 2 if associated pin is connected to health monitoring chip.
		"""
		try :
			return self._fan4speed
		except Exception as e:
			raise e

	@property
	def rescpuusage(self) :
		r"""Shows average CPU utilization percentage if more than 1 CPU is present.
		"""
		try :
			return self._rescpuusage
		except Exception as e:
			raise e

	@property
	def powersupply3status(self) :
		r"""Power supply 3 failure status.
		"""
		try :
			return self._powersupply3status
		except Exception as e:
			raise e

	@property
	def auxvolt5(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 5.
		"""
		try :
			return self._auxvolt5
		except Exception as e:
			raise e

	@property
	def auxvolt3(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 3.
		"""
		try :
			return self._auxvolt3
		except Exception as e:
			raise e

	@property
	def disk0perusage(self) :
		r"""Used space in /flash partition of the disk, as a percentage. This is a critical counter.
		You can configure /flash Used (%) by using the Set snmp alarm DISK-USAGE-HIGH command.
		.
		"""
		try :
			return self._disk0perusage
		except Exception as e:
			raise e

	@property
	def fan2speed(self) :
		r"""Speed of Fan 0 if associated pin is connected to health monitoring chip.
		"""
		try :
			return self._fan2speed
		except Exception as e:
			raise e

	@property
	def powersupply4status(self) :
		r"""Power supply 4 failure status.
		"""
		try :
			return self._powersupply4status
		except Exception as e:
			raise e

	@property
	def auxvolt1(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 1.
		"""
		try :
			return self._auxvolt1
		except Exception as e:
			raise e

	@property
	def fanspeed(self) :
		r"""System fan 2 speed. For new platforms associated pin is connected to CPU supporting fans. For platforms in which it is not connected, it will point to System Fan.
		"""
		try :
			return self._fanspeed
		except Exception as e:
			raise e

	@property
	def fan5speed(self) :
		r"""Speed of Fan 3 if associated pin is connected to health monitoring chip.
		"""
		try :
			return self._fan5speed
		except Exception as e:
			raise e

	@property
	def disk0size(self) :
		r"""Size of /flash partition of the hard disk.
		"""
		try :
			return self._disk0size
		except Exception as e:
			raise e

	@property
	def mgmtcpuusagepcnt(self) :
		r"""Average Management CPU utilization percentage.
		"""
		try :
			return self._mgmtcpuusagepcnt
		except Exception as e:
			raise e

	@property
	def cpuusage(self) :
		r"""CPU utilization percentage.
		"""
		try :
			return self._cpuusage
		except Exception as e:
			raise e

	@property
	def voltagev5sb(self) :
		r"""Power Supply 5V Standby Voltage. Currently only 13k Platforms will have valid value for this counter and for older platforms this will be 0.
		"""
		try :
			return self._voltagev5sb
		except Exception as e:
			raise e

	@property
	def disk0used(self) :
		r"""Used space in /flash partition of the hard disk.
		"""
		try :
			return self._disk0used
		except Exception as e:
			raise e

	@property
	def powersupply1status(self) :
		r"""Power supply 1 failure status.
		"""
		try :
			return self._powersupply1status
		except Exception as e:
			raise e

	@property
	def cpufan0speed(self) :
		r"""CPU Fan 0 speed. Acceptable range is 3000 through 6000 RPM. This is a critical counter.
		You can configure CPU Fan 0 Speed by using the Set snmp alarm FAN-SPEED-LOW command to set the lower limit.
		.
		"""
		try :
			return self._cpufan0speed
		except Exception as e:
			raise e

	@property
	def disk1size(self) :
		r"""Size of /var partition of the hard disk.
		"""
		try :
			return self._disk1size
		except Exception as e:
			raise e

	@property
	def auxtemp1(self) :
		r"""Temperature of a device connected to health monitoring chip through pin 1.
		"""
		try :
			return self._auxtemp1
		except Exception as e:
			raise e

	@property
	def numcpus(self) :
		r"""The number of CPUs on the NetScaler appliance.
		"""
		try :
			return self._numcpus
		except Exception as e:
			raise e

	@property
	def pktcpuusagepcnt(self) :
		r"""Average CPU utilization percentage for all packet engines excluding management PE.
		"""
		try :
			return self._pktcpuusagepcnt
		except Exception as e:
			raise e

	@property
	def voltagev5p(self) :
		r"""Power supply +5V output. Acceptable range is 4.50 through 5.50 volts.
		"""
		try :
			return self._voltagev5p
		except Exception as e:
			raise e

	@property
	def voltagevsen2(self) :
		r"""Voltage Sensor 2 Input. Currently only 13k Platforms will have valid value for this counter and for older platforms this will be 0.
		"""
		try :
			return self._voltagevsen2
		except Exception as e:
			raise e

	@property
	def auxvolt0(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 0.
		"""
		try :
			return self._auxvolt0
		except Exception as e:
			raise e

	@property
	def auxtemp2(self) :
		r"""Temperature of a device connected to health monitoring chip through pin 2.
		"""
		try :
			return self._auxtemp2
		except Exception as e:
			raise e

	@property
	def memsizemb(self) :
		r"""Total amount of system memory, in megabytes.
		"""
		try :
			return self._memsizemb
		except Exception as e:
			raise e

	@property
	def voltagev33main(self) :
		r"""Main power supply +3.3V output. Acceptable range is 2.970 through 3.630 volts. This is a critical counter.
		You can configure Main 3.3V Supply Voltage, by using the Set snmp alarm VOLTAGE-LOW command to set the lower limit and the Set snmp alarm VOLTAGE-HIGH command to set the upper limit.
		.
		"""
		try :
			return self._voltagev33main
		except Exception as e:
			raise e

	@property
	def cpu1temp(self) :
		r"""CPU 1 temperature. 9800 and 9960 platforms display internal chip temperature. 7000, 9010 and 10010 platforms display CPU 0 temperature. This is a critical counter.
		You can configure CPU 1 Temperature by using the Set snmp alarm TEMPERATURE-HIGH command to set the upper limit.
		.
		"""
		try :
			return self._cpu1temp
		except Exception as e:
			raise e

	@property
	def voltagev12n(self) :
		r"""Power supply -12V output. Acceptable range is -13.20 through -10.80 volts. 9800 and 9960 platforms display standard value of -12.0V.
		"""
		try :
			return self._voltagev12n
		except Exception as e:
			raise e

	@property
	def memuseinmb(self) :
		r"""Main memory currently in use, in megabytes.
		"""
		try :
			return self._memuseinmb
		except Exception as e:
			raise e

	@property
	def auxtemp3(self) :
		r"""Temperature of a device connected to health monitoring chip through pin 3.
		"""
		try :
			return self._auxtemp3
		except Exception as e:
			raise e

	@property
	def internaltemp(self) :
		r"""Internal temperature of health monitoring chip. This is a critical counter.
		You can configure Internal Temperature by using the Set snmp alarm TEMPERATURE-HIGH command to set the upper limit.
		.
		"""
		try :
			return self._internaltemp
		except Exception as e:
			raise e

	@property
	def voltagev12p(self) :
		r"""Power supply +12V output. Acceptable range is 10.80 through 13.20 volts.
		"""
		try :
			return self._voltagev12p
		except Exception as e:
			raise e

	@property
	def disk0avail(self) :
		r"""Available space in /flash partition of the hard disk.
		"""
		try :
			return self._disk0avail
		except Exception as e:
			raise e

	@property
	def voltagev33stby(self) :
		r"""Standby power supply +3.3V output. Acceptable range is 2.970 through 3.630 volts. 9800 and 9960 platforms display standard value of 3.3V.
		You can configure Standby 3.3V Supply Voltage by using the Set snmp alarm VOLTAGE-LOW command to set the lower limit and the Set snmp alarm VOLTAGE-HIGH command to set the upper limit.
		.
		"""
		try :
			return self._voltagev33stby
		except Exception as e:
			raise e

	@property
	def voltagevcc1(self) :
		r"""CPU core 1 voltage. Acceptable range is 1.080 through 1.650 volts. If CPU 1 is not connected to the health monitoring chip, display shows voltage of CPU 0.
		"""
		try :
			return self._voltagevcc1
		except Exception as e:
			raise e

	@property
	def fan3speed(self) :
		r"""Speed of Fan 1 if associated pin is connected to health monitoring chip.
		"""
		try :
			return self._fan3speed
		except Exception as e:
			raise e

	@property
	def voltagevtt(self) :
		r"""Intel CPU Vtt power. Currently only 13k Platforms will have valid value for this counter and for older platforms this will be 0.
		"""
		try :
			return self._voltagevtt
		except Exception as e:
			raise e

	@property
	def auxtemp0(self) :
		r"""Temperature of a device connected to health monitoring chip through pin 0.
		"""
		try :
			return self._auxtemp0
		except Exception as e:
			raise e

	@property
	def cpufan1speed(self) :
		r"""CPU Fan 1 speed. Acceptable range is 3000 through 6000 RPM. 7000 platform displays speed of CPU fan 0. This is a critical counter.
		You can configure CPU Fan 1 Speed by using the Set snmp alarm FAN-SPEED-LOW command to set the lower limit.
		.
		"""
		try :
			return self._cpufan1speed
		except Exception as e:
			raise e

	@property
	def voltagevcc0(self) :
		r"""CPU core 0 voltage. Acceptable range is 1.080 through 1.650 volts.
		"""
		try :
			return self._voltagevcc0
		except Exception as e:
			raise e

	@property
	def auxvolt4(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 4.
		"""
		try :
			return self._auxvolt4
		except Exception as e:
			raise e

	@property
	def starttime(self) :
		r"""Time when the NetScaler appliance was last started.
		"""
		try :
			return self._starttime
		except Exception as e:
			raise e

	@property
	def systemfanspeed(self) :
		r"""System fan speed. Acceptable range is 3000 through 6000 RPM. This is a critical counter.
		You can configure System Fan Speed by using the Set snmp alarm FAN-SPEED-LOW command to set the lower limit.
		.
		"""
		try :
			return self._systemfanspeed
		except Exception as e:
			raise e

	@property
	def cpuusagepcnt(self) :
		r"""CPU utilization percentage.
		"""
		try :
			return self._cpuusagepcnt
		except Exception as e:
			raise e

	@property
	def mastercpuusage(self) :
		r"""CPU 0 (currently the master CPU) utilization, as percentage of capacity.
		"""
		try :
			return self._mastercpuusage
		except Exception as e:
			raise e

	@property
	def timesincestart(self) :
		r"""Seconds since the NetScaler appliance started.
		"""
		try :
			return self._timesincestart
		except Exception as e:
			raise e

	@property
	def mgmtcpu0usagepcnt(self) :
		r"""Management CPU-0 utilization percentage.
		"""
		try :
			return self._mgmtcpu0usagepcnt
		except Exception as e:
			raise e

	@property
	def auxvolt6(self) :
		r"""Voltage of a device connected to health monitoring chip through pin 6.
		"""
		try :
			return self._auxvolt6
		except Exception as e:
			raise e

	@property
	def slavecpuusage(self) :
		r"""CPU 1 (currently the slave CPU) utilization, as percentage of capacity. Not applicable for a single-CPU system.
		"""
		try :
			return self._slavecpuusage
		except Exception as e:
			raise e

	@property
	def memusagepcnt(self) :
		r"""Percentage of memory utilization on NetScaler.
		"""
		try :
			return self._memusagepcnt
		except Exception as e:
			raise e

	@property
	def powersupply2status(self) :
		r"""Power supply 2 failure status.
		"""
		try :
			return self._powersupply2status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(system_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.system
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
		r""" Use this API to fetch the statistics of all system_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = system_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class system_response(base_response) :
	def __init__(self, length=1) :
		self.system = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.system = [system_stats() for _ in range(length)]

