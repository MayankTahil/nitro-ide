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


class systementitydata_args :
	r""" Provides additional arguments required for fetching the systementitydata resource.
	"""
	def __init__(self) :
		self._type = None
		self._name = None
		self._counters = None
		self._starttime = None
		self._endtime = None
		self._last = None
		self._unit = None
		self._datasource = None
		self._core = None

	@property
	def type(self) :
		r"""Specify the entity type.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Specify the entity type.
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Specify the entity name.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Specify the entity name.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def counters(self) :
		r"""Specify the counters to be collected.
		"""
		try :
			return self._counters
		except Exception as e:
			raise e

	@counters.setter
	def counters(self, counters) :
		r"""Specify the counters to be collected.
		"""
		try :
			self._counters = counters
		except Exception as e:
			raise e

	@property
	def starttime(self) :
		r"""Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.
		"""
		try :
			return self._starttime
		except Exception as e:
			raise e

	@starttime.setter
	def starttime(self, starttime) :
		r"""Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.
		"""
		try :
			self._starttime = starttime
		except Exception as e:
			raise e

	@property
	def endtime(self) :
		r"""Specify end time in mmddyyyyhhmm upto which values have to be collected.
		"""
		try :
			return self._endtime
		except Exception as e:
			raise e

	@endtime.setter
	def endtime(self, endtime) :
		r"""Specify end time in mmddyyyyhhmm upto which values have to be collected.
		"""
		try :
			self._endtime = endtime
		except Exception as e:
			raise e

	@property
	def last(self) :
		r"""Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1.
		"""
		try :
			return self._last
		except Exception as e:
			raise e

	@last.setter
	def last(self, last) :
		r"""Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1
		"""
		try :
			self._last = last
		except Exception as e:
			raise e

	@property
	def unit(self) :
		r"""Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@unit.setter
	def unit(self, unit) :
		r"""Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS
		"""
		try :
			self._unit = unit
		except Exception as e:
			raise e

	@property
	def datasource(self) :
		r"""Specifies the source which contains all the stored counter values.
		"""
		try :
			return self._datasource
		except Exception as e:
			raise e

	@datasource.setter
	def datasource(self, datasource) :
		r"""Specifies the source which contains all the stored counter values.
		"""
		try :
			self._datasource = datasource
		except Exception as e:
			raise e

	@property
	def core(self) :
		r"""Specify core ID of the PE in nCore.
		"""
		try :
			return self._core
		except Exception as e:
			raise e

	@core.setter
	def core(self, core) :
		r"""Specify core ID of the PE in nCore.
		"""
		try :
			self._core = core
		except Exception as e:
			raise e

	class Unit:
		HOURS = "HOURS"
		DAYS = "DAYS"
		MONTHS = "MONTHS"

