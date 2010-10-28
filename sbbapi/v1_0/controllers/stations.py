from sbbapi.v1_0.controllers.base import *

from httplib2 import Http
from urllib import urlencode

from lxml import etree

class StationsController(BaseController):
	entry_url = 'http://xmlfahrplan.sbb.ch/bin/extxml.exe/'
	
	def getFromString(self, request):
		param_station_query = request.GET.get('station_query', None)
		
		request_content = """<?xml version="1.0" encoding="utf-8"?>
<ReqC lang="EN" prod="iPhone3.1" ver="2.3" accessId="MJXZ841ZfsmqqmSymWhBPy5dMNoqoGsHInHbWJQ5PTUZOJ1rLTkn8vVZOZDFfSe">
	<LocValReq id="toInput" sMode="1">
		<ReqLoc match="{station_string}" type="ALLTYPE" />
	</LocValReq>
</ReqC>""".format(station_string=param_station_query)
		
		h = Http()
		resp, content = h.request(self.entry_url, "POST", request_content)
		if resp['status'] != '200':
			# TODO: Error Handling Here!
			return
		
		root = etree.fromstring(content)
		results = root.findall(".//LocValRes/*")
		
		stations = []
		for result in results:
			if result.tag == 'Station':
				station = {
					'station_name': result.get("name"),
					'station_coordinate': {
						'latitude': result.get("x"),
						'longitude': result.get("y"),
					},
					'station_id': result.get("externalId"),
					'station_type': 'Station',
				}
				
				stations.append(station)
		
		if len(stations) == 0:
			# TODO: Error Handling Here!
			return
		
		return stations
		