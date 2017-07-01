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

class ca_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._caaunindentifiedbyteshr = 0
		self._caiosbyteshr = 0
		self._caotherbyteshr = 0
		self._calaptpdsktpbyteshr = 0
		self._caandroidbyteshr = 0
		self._ca3gpvidcachebyteshr = 0
		self._camp4vidcachebyteshr = 0
		self._caflvvidcachebyteshr = 0
		self._caaacaudiocachebyteshr = 0
		self._caadtsaudiocachebyteshr = 0
		self._caaplelivestrmngplvidcachebyteshr = 0
		self._caapplelivestrmngvidcachebyteshr = 0
		self._camsftsmthstrmngplvidcabyteshr = 0
		self._camsftsmthstrmngvidcabyteshr = 0
		self._caunidentifiedhr = 0
		self._caioshr = 0
		self._caotherhr = 0
		self._calaptopdesktphr = 0
		self._caandroidhr = 0
		self._ca3gpvidhr = 0
		self._cacmp4vidhr = 0
		self._cacflvvidhr = 0
		self._cacaacaudiohr = 0
		self._cacadtsaudiohr = 0
		self._cacapplelivestreamingplaylistvidhr = 0
		self._cacapplelivestreamingvidhr = 0
		self._cacmsftsmthstrmplvidhr = 0
		self._camsftsmthstrmvidhr = 0
		self._catotother = 0
		self._catoherrate = 0
		self._catotvideo = 0
		self._cavideorate = 0
		self._catotaudio = 0
		self._caaudiorate = 0
		self._catotobjstored = 0
		self._catotlookuphit = 0
		self._calookuphitrate = 0
		self._catotgetobjreq = 0
		self._cagetobjreqrate = 0
		self._catotrequests = 0
		self._carequestsrate = 0
		self._camsftsmthstrmvid = 0
		self._camsftsmthstrmvidrate = 0
		self._cacmsftsmthstrmvid = 0
		self._cacmsftsmthstrmvidrate = 0
		self._camsftsmthstrvid = 0
		self._camsftsmthstrvidrate = 0
		self._cacmsftsmthstrmplvid = 0
		self._cacmsftsmthstrmplvidrate = 0
		self._cacaplelivestrmngvid = 0
		self._cacaplelivestrmngvidrate = 0
		self._cacapplelivestreamingvid = 0
		self._cacapplelivestreamingvidrate = 0
		self._cacapplelivestrmngvid = 0
		self._cacapplelivestrmngvidrate = 0
		self._cacapplelivestreamingplaylistvid = 0
		self._cacapplelivestreamingplaylistvidrate = 0
		self._caadtsaudio = 0
		self._caadtsaudiorate = 0
		self._cacadtsaudio = 0
		self._cacadtsaudiorate = 0
		self._caaacaudio = 0
		self._caaacaudiorate = 0
		self._cacaacaudio = 0
		self._cacaacaudiorate = 0
		self._caflvvid = 0
		self._caflvvidrate = 0
		self._cacflvvid = 0
		self._cacflvvidrate = 0
		self._camp4vid = 0
		self._camp4vidrate = 0
		self._cacmp4vid = 0
		self._cacmp4vidrate = 0
		self._ca3pvid = 0
		self._ca3pvidrate = 0
		self._ca3gpvid = 0
		self._ca3gpvidrate = 0
		self._camsftsmthstrmvidbytes = 0
		self._camsftsmthstrmvidbytesrate = 0
		self._camicrosoftsmoothstreamingvidcachebytes = 0
		self._camicrosoftsmoothstreamingvidcachebytesrate = 0
		self._camsftsmthstrmplvidbytes = 0
		self._camsftsmthstrmplvidbytesrate = 0
		self._camicrosoftsmoothstreamingplaylistvidcachebytes = 0
		self._camicrosoftsmoothstreamingplaylistvidcachebytesrate = 0
		self._caapplelivestreamingvidbytes = 0
		self._caapplelivestreamingvidbytesrate = 0
		self._caapplelivestreamingvidcachebytes = 0
		self._caapplelivestreamingvidcachebytesrate = 0
		self._caapplelivestreamingplaylistvidbytes = 0
		self._caapplelivestreamingplaylistvidbytesrate = 0
		self._caapplelivestreamingplaylistvidcachebytes = 0
		self._caapplelivestreamingplaylistvidcachebytesrate = 0
		self._caadtsaudiobytes = 0
		self._caadtsaudiobytesrate = 0
		self._caadtsaudiocachebytes = 0
		self._caadtsaudiocachebytesrate = 0
		self._caaacaudiobytes = 0
		self._caaacaudiobytesrate = 0
		self._caaacaudiocachebytes = 0
		self._caaacaudiocachebytesrate = 0
		self._caflvvidbytes = 0
		self._caflvvidbytesrate = 0
		self._caflvvidcachebytes = 0
		self._caflvvidcachebytesrate = 0
		self._camp4vidbytes = 0
		self._camp4vidbytesrate = 0
		self._camp4vidcachebytes = 0
		self._camp4vidcachebytesrate = 0
		self._ca3gpvidbytes = 0
		self._ca3gpvidbytesrate = 0
		self._ca3gpvidcachebytes = 0
		self._ca3gpvidcachebytesrate = 0
		self._caandroid = 0
		self._caandroidrate = 0
		self._calaptopdesktp = 0
		self._calaptopdesktprate = 0
		self._caios = 0
		self._caiosrate = 0
		self._caother = 0
		self._caotherrate = 0
		self._caunidentified = 0
		self._caunidentifiedrate = 0
		self._caandroidcache = 0
		self._caandroidcacherate = 0
		self._caioscache = 0
		self._caioscacherate = 0
		self._caothercache = 0
		self._caothercacherate = 0
		self._calaptopdesktpcache = 0
		self._calaptopdesktpcacherate = 0
		self._caunidentifiedcache = 0
		self._caunidentifiedcacherate = 0
		self._caandroidbytes = 0
		self._caandroidbytesrate = 0
		self._caiosbytes = 0
		self._caiosbytesrate = 0
		self._caotherbytes = 0
		self._caotherbytesrate = 0
		self._caalptopdsktpbytes = 0
		self._caalptopdsktpbytesrate = 0
		self._caunidentifiedbytes = 0
		self._caunidentifiedbytesrate = 0
		self._caandroididcachebytes = 0
		self._caandroididcachebytesrate = 0
		self._caiosidcachebytes = 0
		self._caiosidcachebytesrate = 0
		self._caotherididcachebytes = 0
		self._caotherididcachebytesrate = 0
		self._calaptpdektpbytes = 0
		self._calaptpdektpbytesrate = 0
		self._caaunindentifiedbytes = 0
		self._caaunindentifiedbytesrate = 0

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
	def caaacaudiocachebytes(self) :
		r"""This tells the total number of AAC bytes served from cache.
		"""
		try :
			return self._caaacaudiocachebytes
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmvidhr(self) :
		r"""This tells the hit ratio of MicrosoftSmoothStreaming requests.
		"""
		try :
			return self._camsftsmthstrmvidhr
		except Exception as e:
			raise e

	@property
	def caflvvidrate(self) :
		r"""Rate (/s) counter for caflvvid.
		"""
		try :
			return self._caflvvidrate
		except Exception as e:
			raise e

	@property
	def cacmsftsmthstrmplvid(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming Playlist requests served from cache.
		"""
		try :
			return self._cacmsftsmthstrmplvid
		except Exception as e:
			raise e

	@property
	def camp4vidbytesrate(self) :
		r"""Rate (/s) counter for camp4vidbytes.
		"""
		try :
			return self._camp4vidbytesrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmngplvidcabyteshr(self) :
		r"""This tells the byte hit ratio of MicrosoftSmoothStreaming Playlist bytes .
		"""
		try :
			return self._camsftsmthstrmngplvidcabyteshr
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingplaylistvidbytesrate(self) :
		r"""Rate (/s) counter for caapplelivestreamingplaylistvidbytes.
		"""
		try :
			return self._caapplelivestreamingplaylistvidbytesrate
		except Exception as e:
			raise e

	@property
	def catotvideo(self) :
		try :
			return self._catotvideo
		except Exception as e:
			raise e

	@property
	def caaacaudiobytes(self) :
		r"""This tells the total number of AAC bytes served by NS .
		"""
		try :
			return self._caaacaudiobytes
		except Exception as e:
			raise e

	@property
	def calookuphitrate(self) :
		r"""Rate (/s) counter for catotlookuphit.
		"""
		try :
			return self._calookuphitrate
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingplaylistvid(self) :
		r"""This tells the total number of AppleLive Playlist requests served from cache.
		"""
		try :
			return self._cacapplelivestreamingplaylistvid
		except Exception as e:
			raise e

	@property
	def cacmp4vidhr(self) :
		r"""This tells the hit ratio of MP4 requests.
		"""
		try :
			return self._cacmp4vidhr
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingvidhr(self) :
		r"""This tells the hit ratio of AppleLive requests.
		"""
		try :
			return self._cacapplelivestreamingvidhr
		except Exception as e:
			raise e

	@property
	def caflvvidbytesrate(self) :
		r"""Rate (/s) counter for caflvvidbytes.
		"""
		try :
			return self._caflvvidbytesrate
		except Exception as e:
			raise e

	@property
	def catotobjstored(self) :
		try :
			return self._catotobjstored
		except Exception as e:
			raise e

	@property
	def ca3gpvidcachebytesrate(self) :
		r"""Rate (/s) counter for ca3gpvidcachebytes.
		"""
		try :
			return self._ca3gpvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def caaacaudiocachebyteshr(self) :
		r"""This tells the hit ratio AAC bytes served.
		"""
		try :
			return self._caaacaudiocachebyteshr
		except Exception as e:
			raise e

	@property
	def caadtsaudiobytes(self) :
		r"""This tells the total number of ADTS bytes served by NS .
		"""
		try :
			return self._caadtsaudiobytes
		except Exception as e:
			raise e

	@property
	def cacadtsaudio(self) :
		r"""This tells the total number of ADTS requests served from cache.
		"""
		try :
			return self._cacadtsaudio
		except Exception as e:
			raise e

	@property
	def caaudiorate(self) :
		r"""Rate (/s) counter for catotaudio.
		"""
		try :
			return self._caaudiorate
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingplaylistvidrate(self) :
		r"""Rate (/s) counter for cacapplelivestreamingplaylistvid.
		"""
		try :
			return self._cacapplelivestreamingplaylistvidrate
		except Exception as e:
			raise e

	@property
	def caaplelivestrmngplvidcachebyteshr(self) :
		r"""This tells the byte hit ratio of AppleLive Playlist bytes .
		"""
		try :
			return self._caaplelivestrmngplvidcachebyteshr
		except Exception as e:
			raise e

	@property
	def caotherididcachebytes(self) :
		r"""This tells the total number of other device bytes served from cache.
		"""
		try :
			return self._caotherididcachebytes
		except Exception as e:
			raise e

	@property
	def calaptpdsktpbyteshr(self) :
		r"""This tells the hit ratio of laptop_desktop bytes.
		"""
		try :
			return self._calaptpdsktpbyteshr
		except Exception as e:
			raise e

	@property
	def caflvvidcachebytes(self) :
		r"""This tells the total number of FLV bytes served from cache.
		"""
		try :
			return self._caflvvidcachebytes
		except Exception as e:
			raise e

	@property
	def caalptopdsktpbytesrate(self) :
		r"""Rate (/s) counter for caalptopdsktpbytes.
		"""
		try :
			return self._caalptopdsktpbytesrate
		except Exception as e:
			raise e

	@property
	def cacflvvidrate(self) :
		r"""Rate (/s) counter for cacflvvid.
		"""
		try :
			return self._cacflvvidrate
		except Exception as e:
			raise e

	@property
	def caaunindentifiedbyteshr(self) :
		r"""This tells the hit ratio of unindentified bytes.
		"""
		try :
			return self._caaunindentifiedbyteshr
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingplaylistvidcachebytes(self) :
		r"""This tells the total number of AppleLive Playlist bytes served from cache.
		"""
		try :
			return self._caapplelivestreamingplaylistvidcachebytes
		except Exception as e:
			raise e

	@property
	def catotrequests(self) :
		try :
			return self._catotrequests
		except Exception as e:
			raise e

	@property
	def cacflvvidhr(self) :
		r"""This tells the hit ratio of FLV requests.
		"""
		try :
			return self._cacflvvidhr
		except Exception as e:
			raise e

	@property
	def caadtsaudiocachebyteshr(self) :
		r"""This tells the byte hit ratio of ADTS bytes .
		"""
		try :
			return self._caadtsaudiocachebyteshr
		except Exception as e:
			raise e

	@property
	def caiosbytesrate(self) :
		r"""Rate (/s) counter for caiosbytes.
		"""
		try :
			return self._caiosbytesrate
		except Exception as e:
			raise e

	@property
	def cacmp4vidrate(self) :
		r"""Rate (/s) counter for cacmp4vid.
		"""
		try :
			return self._cacmp4vidrate
		except Exception as e:
			raise e

	@property
	def catotlookuphit(self) :
		r"""This number should be close to the number of hits being served currently.
		"""
		try :
			return self._catotlookuphit
		except Exception as e:
			raise e

	@property
	def caadtsaudiobytesrate(self) :
		r"""Rate (/s) counter for caadtsaudiobytes.
		"""
		try :
			return self._caadtsaudiobytesrate
		except Exception as e:
			raise e

	@property
	def ca3pvid(self) :
		r"""This tells the total number of 3GP requests served by NS.
		"""
		try :
			return self._ca3pvid
		except Exception as e:
			raise e

	@property
	def calaptopdesktpcache(self) :
		r"""This tells laptop/desktop requests served from cache.
		"""
		try :
			return self._calaptopdesktpcache
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmplvidbytes(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming Playlist bytes served by NS .
		"""
		try :
			return self._camsftsmthstrmplvidbytes
		except Exception as e:
			raise e

	@property
	def caiosidcachebytesrate(self) :
		r"""Rate (/s) counter for caiosidcachebytes.
		"""
		try :
			return self._caiosidcachebytesrate
		except Exception as e:
			raise e

	@property
	def ca3gpvidbytesrate(self) :
		r"""Rate (/s) counter for ca3gpvidbytes.
		"""
		try :
			return self._ca3gpvidbytesrate
		except Exception as e:
			raise e

	@property
	def caunidentifiedcache(self) :
		r"""This tells unidentified device requests served from cache.
		"""
		try :
			return self._caunidentifiedcache
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingvidcachebytesrate(self) :
		r"""Rate (/s) counter for caapplelivestreamingvidcachebytes.
		"""
		try :
			return self._caapplelivestreamingvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingvidbytes(self) :
		r"""This tells the total number of AppleLive bytes served by NS .
		"""
		try :
			return self._caapplelivestreamingvidbytes
		except Exception as e:
			raise e

	@property
	def caflvvidcachebyteshr(self) :
		r"""This tells the hit ratio of FLV bytes.
		"""
		try :
			return self._caflvvidcachebyteshr
		except Exception as e:
			raise e

	@property
	def caaunindentifiedbytesrate(self) :
		r"""Rate (/s) counter for caaunindentifiedbytes.
		"""
		try :
			return self._caaunindentifiedbytesrate
		except Exception as e:
			raise e

	@property
	def caios(self) :
		r"""Total number of iOs requests to netscaler.
		"""
		try :
			return self._caios
		except Exception as e:
			raise e

	@property
	def caiosrate(self) :
		r"""Rate (/s) counter for caios.
		"""
		try :
			return self._caiosrate
		except Exception as e:
			raise e

	@property
	def caandroidbytes(self) :
		r"""This tells the total number of Android bytes served by NS .
		"""
		try :
			return self._caandroidbytes
		except Exception as e:
			raise e

	@property
	def caotherrate(self) :
		r"""Rate (/s) counter for caother.
		"""
		try :
			return self._caotherrate
		except Exception as e:
			raise e

	@property
	def caflvvidbytes(self) :
		r"""This tells the total number of FLV bytes served by NS .
		"""
		try :
			return self._caflvvidbytes
		except Exception as e:
			raise e

	@property
	def calaptpdektpbytes(self) :
		r"""This tells the total number of Laptop/desktop bytes served from cache.
		"""
		try :
			return self._calaptpdektpbytes
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingplaylistvidcachebytesrate(self) :
		r"""Rate (/s) counter for caapplelivestreamingplaylistvidcachebytes.
		"""
		try :
			return self._caapplelivestreamingplaylistvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmplvidbytesrate(self) :
		r"""Rate (/s) counter for camsftsmthstrmplvidbytes.
		"""
		try :
			return self._camsftsmthstrmplvidbytesrate
		except Exception as e:
			raise e

	@property
	def caaacaudiorate(self) :
		r"""Rate (/s) counter for caaacaudio.
		"""
		try :
			return self._caaacaudiorate
		except Exception as e:
			raise e

	@property
	def ca3gpvidhr(self) :
		r"""This tells the total number of 3GP requests.
		"""
		try :
			return self._ca3gpvidhr
		except Exception as e:
			raise e

	@property
	def calaptopdesktprate(self) :
		r"""Rate (/s) counter for calaptopdesktp.
		"""
		try :
			return self._calaptopdesktprate
		except Exception as e:
			raise e

	@property
	def camp4vidrate(self) :
		r"""Rate (/s) counter for camp4vid.
		"""
		try :
			return self._camp4vidrate
		except Exception as e:
			raise e

	@property
	def cacadtsaudiohr(self) :
		r"""This tells the Hit Ratio of ADTS requests.
		"""
		try :
			return self._cacadtsaudiohr
		except Exception as e:
			raise e

	@property
	def cacapplelivestrmngvid(self) :
		r"""This tells the total number of AppleLive Playlist requests served by NS.
		"""
		try :
			return self._cacapplelivestrmngvid
		except Exception as e:
			raise e

	@property
	def caaacaudiocachebytesrate(self) :
		r"""Rate (/s) counter for caaacaudiocachebytes.
		"""
		try :
			return self._caaacaudiocachebytesrate
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingvidbytesrate(self) :
		r"""Rate (/s) counter for caapplelivestreamingvidbytes.
		"""
		try :
			return self._caapplelivestreamingvidbytesrate
		except Exception as e:
			raise e

	@property
	def cacaplelivestrmngvidrate(self) :
		r"""Rate (/s) counter for cacaplelivestrmngvid.
		"""
		try :
			return self._cacaplelivestrmngvidrate
		except Exception as e:
			raise e

	@property
	def caunidentifiedhr(self) :
		r"""This tells the hit ratio of android requests.
		"""
		try :
			return self._caunidentifiedhr
		except Exception as e:
			raise e

	@property
	def cagetobjreqrate(self) :
		r"""Rate (/s) counter for catotgetobjreq.
		"""
		try :
			return self._cagetobjreqrate
		except Exception as e:
			raise e

	@property
	def camp4vidcachebyteshr(self) :
		r"""This tells the hit ratio of MP4 bytes.
		"""
		try :
			return self._camp4vidcachebyteshr
		except Exception as e:
			raise e

	@property
	def calaptopdesktphr(self) :
		r"""This tells the hit ratio of laptop/desktop requests.
		"""
		try :
			return self._calaptopdesktphr
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmvidbytesrate(self) :
		r"""Rate (/s) counter for camsftsmthstrmvidbytes.
		"""
		try :
			return self._camsftsmthstrmvidbytesrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmngvidcabyteshr(self) :
		r"""This tells the Bytes hit ratio of MicrosoftSmoothStreaming bytes .
		"""
		try :
			return self._camsftsmthstrmngvidcabyteshr
		except Exception as e:
			raise e

	@property
	def camicrosoftsmoothstreamingplaylistvidcachebytes(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming Playlist bytes served from cache.
		"""
		try :
			return self._camicrosoftsmoothstreamingplaylistvidcachebytes
		except Exception as e:
			raise e

	@property
	def caiosbytes(self) :
		r"""This tells the total number of IOS bytes served by NS .
		"""
		try :
			return self._caiosbytes
		except Exception as e:
			raise e

	@property
	def calaptopdesktp(self) :
		r"""Total number of laptop/desktop requests to netscaler.
		"""
		try :
			return self._calaptopdesktp
		except Exception as e:
			raise e

	@property
	def caothercacherate(self) :
		r"""Rate (/s) counter for caothercache.
		"""
		try :
			return self._caothercacherate
		except Exception as e:
			raise e

	@property
	def camp4vidcachebytesrate(self) :
		r"""Rate (/s) counter for camp4vidcachebytes.
		"""
		try :
			return self._camp4vidcachebytesrate
		except Exception as e:
			raise e

	@property
	def cacaacaudiohr(self) :
		r"""This tells the hit ratio of AAC requests.
		"""
		try :
			return self._cacaacaudiohr
		except Exception as e:
			raise e

	@property
	def caotherididcachebytesrate(self) :
		r"""Rate (/s) counter for caotherididcachebytes.
		"""
		try :
			return self._caotherididcachebytesrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmvidbytes(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming bytes served by NS .
		"""
		try :
			return self._camsftsmthstrmvidbytes
		except Exception as e:
			raise e

	@property
	def cacmsftsmthstrmplvidhr(self) :
		r"""This tells the hit ratio of MicrosoftSmoothStreaming Playlist requests.
		"""
		try :
			return self._cacmsftsmthstrmplvidhr
		except Exception as e:
			raise e

	@property
	def calaptopdesktpcacherate(self) :
		r"""Rate (/s) counter for calaptopdesktpcache.
		"""
		try :
			return self._calaptopdesktpcacherate
		except Exception as e:
			raise e

	@property
	def ca3gpvidbytes(self) :
		r"""This tells the total number of 3GP bytes served by NS .
		"""
		try :
			return self._ca3gpvidbytes
		except Exception as e:
			raise e

	@property
	def caotherbytes(self) :
		r"""This tells the total number of Other mobile device bytes served by NS .
		"""
		try :
			return self._caotherbytes
		except Exception as e:
			raise e

	@property
	def carequestsrate(self) :
		r"""Rate (/s) counter for catotrequests.
		"""
		try :
			return self._carequestsrate
		except Exception as e:
			raise e

	@property
	def caunidentifiedbytesrate(self) :
		r"""Rate (/s) counter for caunidentifiedbytes.
		"""
		try :
			return self._caunidentifiedbytesrate
		except Exception as e:
			raise e

	@property
	def ca3gpvidcachebyteshr(self) :
		r"""This tells the hit ratio of 3GP bytes.
		"""
		try :
			return self._ca3gpvidcachebyteshr
		except Exception as e:
			raise e

	@property
	def caadtsaudiocachebytes(self) :
		r"""This tells the total number of ADTS bytes served from cache.
		"""
		try :
			return self._caadtsaudiocachebytes
		except Exception as e:
			raise e

	@property
	def caadtsaudio(self) :
		r"""This tells the total number of ADTS requests served by NS.
		"""
		try :
			return self._caadtsaudio
		except Exception as e:
			raise e

	@property
	def caadtsaudiocachebytesrate(self) :
		r"""Rate (/s) counter for caadtsaudiocachebytes.
		"""
		try :
			return self._caadtsaudiocachebytesrate
		except Exception as e:
			raise e

	@property
	def ca3gpvidrate(self) :
		r"""Rate (/s) counter for ca3gpvid.
		"""
		try :
			return self._ca3gpvidrate
		except Exception as e:
			raise e

	@property
	def caioscache(self) :
		r"""This tells iOS requests served from cache.
		"""
		try :
			return self._caioscache
		except Exception as e:
			raise e

	@property
	def caaunindentifiedbytes(self) :
		r"""This tells the total number of unindentified device bytes served from cache.
		"""
		try :
			return self._caaunindentifiedbytes
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingplaylistvidhr(self) :
		r"""This tells the hit ratio of AppleLive Playlist requests.
		"""
		try :
			return self._cacapplelivestreamingplaylistvidhr
		except Exception as e:
			raise e

	@property
	def caunidentified(self) :
		r"""Total number of unidentified requests to netscaler.
		"""
		try :
			return self._caunidentified
		except Exception as e:
			raise e

	@property
	def caandroid(self) :
		r"""Total number of android requests to netscaler.
		"""
		try :
			return self._caandroid
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingplaylistvidbytes(self) :
		r"""This tells the total number of AppleLive Playlist bytes served by NS .
		"""
		try :
			return self._caapplelivestreamingplaylistvidbytes
		except Exception as e:
			raise e

	@property
	def camp4vidbytes(self) :
		r"""This tells the total number of MP4 bytes served by NS .
		"""
		try :
			return self._camp4vidbytes
		except Exception as e:
			raise e

	@property
	def caunidentifiedrate(self) :
		r"""Rate (/s) counter for caunidentified.
		"""
		try :
			return self._caunidentifiedrate
		except Exception as e:
			raise e

	@property
	def cacaacaudio(self) :
		r"""This tells the total number of AAC requests served from cache.
		"""
		try :
			return self._cacaacaudio
		except Exception as e:
			raise e

	@property
	def cacflvvid(self) :
		r"""This tells the total number of FLV requests served from cache.
		"""
		try :
			return self._cacflvvid
		except Exception as e:
			raise e

	@property
	def catotgetobjreq(self) :
		try :
			return self._catotgetobjreq
		except Exception as e:
			raise e

	@property
	def caotherbyteshr(self) :
		r"""This tells the hit ratio of Other device.
		"""
		try :
			return self._caotherbyteshr
		except Exception as e:
			raise e

	@property
	def caioshr(self) :
		r"""This tells the hit ratio of ios requests.
		"""
		try :
			return self._caioshr
		except Exception as e:
			raise e

	@property
	def calaptpdektpbytesrate(self) :
		r"""Rate (/s) counter for calaptpdektpbytes.
		"""
		try :
			return self._calaptpdektpbytesrate
		except Exception as e:
			raise e

	@property
	def caandroididcachebytes(self) :
		r"""This tells the total number of Android bytes served from cache.
		"""
		try :
			return self._caandroididcachebytes
		except Exception as e:
			raise e

	@property
	def caflvvid(self) :
		r"""This tells the total number of FLV requests served by NS.
		"""
		try :
			return self._caflvvid
		except Exception as e:
			raise e

	@property
	def cacadtsaudiorate(self) :
		r"""Rate (/s) counter for cacadtsaudio.
		"""
		try :
			return self._cacadtsaudiorate
		except Exception as e:
			raise e

	@property
	def caandroidbyteshr(self) :
		r"""This tells the hit ratio of 3GP bytes.
		"""
		try :
			return self._caandroidbyteshr
		except Exception as e:
			raise e

	@property
	def caandroididcachebytesrate(self) :
		r"""Rate (/s) counter for caandroididcachebytes.
		"""
		try :
			return self._caandroididcachebytesrate
		except Exception as e:
			raise e

	@property
	def cacmp4vid(self) :
		r"""This tells the total number of MP4 requests served from cache.
		"""
		try :
			return self._cacmp4vid
		except Exception as e:
			raise e

	@property
	def caandroidbytesrate(self) :
		r"""Rate (/s) counter for caandroidbytes.
		"""
		try :
			return self._caandroidbytesrate
		except Exception as e:
			raise e

	@property
	def cacmsftsmthstrmplvidrate(self) :
		r"""Rate (/s) counter for cacmsftsmthstrmplvid.
		"""
		try :
			return self._cacmsftsmthstrmplvidrate
		except Exception as e:
			raise e

	@property
	def caadtsaudiorate(self) :
		r"""Rate (/s) counter for caadtsaudio.
		"""
		try :
			return self._caadtsaudiorate
		except Exception as e:
			raise e

	@property
	def camp4vid(self) :
		r"""This tells the total number of MP4 requests served by NS.
		"""
		try :
			return self._camp4vid
		except Exception as e:
			raise e

	@property
	def caunidentifiedcacherate(self) :
		r"""Rate (/s) counter for caunidentifiedcache.
		"""
		try :
			return self._caunidentifiedcacherate
		except Exception as e:
			raise e

	@property
	def caandroidcacherate(self) :
		r"""Rate (/s) counter for caandroidcache.
		"""
		try :
			return self._caandroidcacherate
		except Exception as e:
			raise e

	@property
	def cavideorate(self) :
		r"""Rate (/s) counter for catotvideo.
		"""
		try :
			return self._cavideorate
		except Exception as e:
			raise e

	@property
	def camicrosoftsmoothstreamingplaylistvidcachebytesrate(self) :
		r"""Rate (/s) counter for camicrosoftsmoothstreamingplaylistvidcachebytes.
		"""
		try :
			return self._camicrosoftsmoothstreamingplaylistvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def caaacaudio(self) :
		r"""This tells the total number of AAC requests served by NS.
		"""
		try :
			return self._caaacaudio
		except Exception as e:
			raise e

	@property
	def catotother(self) :
		try :
			return self._catotother
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingvidrate(self) :
		r"""Rate (/s) counter for cacapplelivestreamingvid.
		"""
		try :
			return self._cacapplelivestreamingvidrate
		except Exception as e:
			raise e

	@property
	def cacapplelivestreamingvid(self) :
		r"""This tells the total number of AppleLive requests served from cache.
		"""
		try :
			return self._cacapplelivestreamingvid
		except Exception as e:
			raise e

	@property
	def caandroidhr(self) :
		r"""This tells the hit ratio of android requests .
		"""
		try :
			return self._caandroidhr
		except Exception as e:
			raise e

	@property
	def cacmsftsmthstrmvidrate(self) :
		r"""Rate (/s) counter for cacmsftsmthstrmvid.
		"""
		try :
			return self._cacmsftsmthstrmvidrate
		except Exception as e:
			raise e

	@property
	def caioscacherate(self) :
		r"""Rate (/s) counter for caioscache.
		"""
		try :
			return self._caioscacherate
		except Exception as e:
			raise e

	@property
	def caunidentifiedbytes(self) :
		r"""This tells the total number of unidentified device bytes served by NS .
		"""
		try :
			return self._caunidentifiedbytes
		except Exception as e:
			raise e

	@property
	def caandroidrate(self) :
		r"""Rate (/s) counter for caandroid.
		"""
		try :
			return self._caandroidrate
		except Exception as e:
			raise e

	@property
	def cacaacaudiorate(self) :
		r"""Rate (/s) counter for cacaacaudio.
		"""
		try :
			return self._cacaacaudiorate
		except Exception as e:
			raise e

	@property
	def cacmsftsmthstrmvid(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming requests served from cache.
		"""
		try :
			return self._cacmsftsmthstrmvid
		except Exception as e:
			raise e

	@property
	def camicrosoftsmoothstreamingvidcachebytes(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming bytes served from cache.
		"""
		try :
			return self._camicrosoftsmoothstreamingvidcachebytes
		except Exception as e:
			raise e

	@property
	def caother(self) :
		r"""Total number of other mobile device requests to netscaler.
		"""
		try :
			return self._caother
		except Exception as e:
			raise e

	@property
	def caalptopdsktpbytes(self) :
		r"""This tells the total number of Laptop/desktop bytes served by NS .
		"""
		try :
			return self._caalptopdsktpbytes
		except Exception as e:
			raise e

	@property
	def caothercache(self) :
		r"""This tells Other device requests served from cache.
		"""
		try :
			return self._caothercache
		except Exception as e:
			raise e

	@property
	def camsftsmthstrvid(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming Playlist requests served by NS.
		"""
		try :
			return self._camsftsmthstrvid
		except Exception as e:
			raise e

	@property
	def camp4vidcachebytes(self) :
		r"""This tells the total number of MP4 bytes served from cache.
		"""
		try :
			return self._camp4vidcachebytes
		except Exception as e:
			raise e

	@property
	def ca3gpvid(self) :
		r"""This tells the hit ratio of 3GP requests served from cache.
		"""
		try :
			return self._ca3gpvid
		except Exception as e:
			raise e

	@property
	def cacapplelivestrmngvidrate(self) :
		r"""Rate (/s) counter for cacapplelivestrmngvid.
		"""
		try :
			return self._cacapplelivestrmngvidrate
		except Exception as e:
			raise e

	@property
	def camicrosoftsmoothstreamingvidcachebytesrate(self) :
		r"""Rate (/s) counter for camicrosoftsmoothstreamingvidcachebytes.
		"""
		try :
			return self._camicrosoftsmoothstreamingvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def catoherrate(self) :
		r"""Rate (/s) counter for catotother.
		"""
		try :
			return self._catoherrate
		except Exception as e:
			raise e

	@property
	def caotherhr(self) :
		r"""This tells the hit ratio of other mobile device requests .
		"""
		try :
			return self._caotherhr
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmvidrate(self) :
		r"""Rate (/s) counter for camsftsmthstrmvid.
		"""
		try :
			return self._camsftsmthstrmvidrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrvidrate(self) :
		r"""Rate (/s) counter for camsftsmthstrvid.
		"""
		try :
			return self._camsftsmthstrvidrate
		except Exception as e:
			raise e

	@property
	def ca3gpvidcachebytes(self) :
		r"""This tells the total number of 3GP bytes served from cache.
		"""
		try :
			return self._ca3gpvidcachebytes
		except Exception as e:
			raise e

	@property
	def caaacaudiobytesrate(self) :
		r"""Rate (/s) counter for caaacaudiobytes.
		"""
		try :
			return self._caaacaudiobytesrate
		except Exception as e:
			raise e

	@property
	def camsftsmthstrmvid(self) :
		r"""This tells the total number of MicrosoftSmoothStreaming requests served by NS.
		"""
		try :
			return self._camsftsmthstrmvid
		except Exception as e:
			raise e

	@property
	def cacaplelivestrmngvid(self) :
		r"""This tells the total number of AppleLive requests served by NS.
		"""
		try :
			return self._cacaplelivestrmngvid
		except Exception as e:
			raise e

	@property
	def caapplelivestrmngvidcachebyteshr(self) :
		r"""This tells the total number of AppleLive bytes .
		"""
		try :
			return self._caapplelivestrmngvidcachebyteshr
		except Exception as e:
			raise e

	@property
	def ca3pvidrate(self) :
		r"""Rate (/s) counter for ca3pvid.
		"""
		try :
			return self._ca3pvidrate
		except Exception as e:
			raise e

	@property
	def caandroidcache(self) :
		r"""This tells android requests served from cache.
		"""
		try :
			return self._caandroidcache
		except Exception as e:
			raise e

	@property
	def caflvvidcachebytesrate(self) :
		r"""Rate (/s) counter for caflvvidcachebytes.
		"""
		try :
			return self._caflvvidcachebytesrate
		except Exception as e:
			raise e

	@property
	def caiosidcachebytes(self) :
		r"""This tells the total number of IOS bytes served from cache.
		"""
		try :
			return self._caiosidcachebytes
		except Exception as e:
			raise e

	@property
	def caotherbytesrate(self) :
		r"""Rate (/s) counter for caotherbytes.
		"""
		try :
			return self._caotherbytesrate
		except Exception as e:
			raise e

	@property
	def caapplelivestreamingvidcachebytes(self) :
		r"""This tells the total number of AppleLive bytes served from cache.
		"""
		try :
			return self._caapplelivestreamingvidcachebytes
		except Exception as e:
			raise e

	@property
	def caiosbyteshr(self) :
		r"""This tells the hit ratio of IOS bytes.
		"""
		try :
			return self._caiosbyteshr
		except Exception as e:
			raise e

	@property
	def catotaudio(self) :
		try :
			return self._catotaudio
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ca_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ca
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
		r""" Use this API to fetch the statistics of all ca_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = ca_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class ca_response(base_response) :
	def __init__(self, length=1) :
		self.ca = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ca = [ca_stats() for _ in range(length)]

