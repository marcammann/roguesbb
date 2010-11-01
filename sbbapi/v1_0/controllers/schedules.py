from sbbapi.v1_0.controllers.base import *
from sbbapi.error import *

from datetime import datetime

from httplib2 import Http
from urllib import urlencode

from lxml import etree

"""
<ReqC lang="EN" prod="iPhone3.1" ver="2.3" accessId="MJXZ841ZfsmqqmSymWhBPy5dMNoqoGsHInHbWJQ5PTUZOJ1rLTkn8vVZOZDFfSe">
	<ConReq>
		<Start>
			<Station name="Zrich Hardbrcke" externalId="008503020#95" />
			<Prod prod="1111111111000000" />
		</Start>
		<Dest>
			<Station name="Winterthur" externalId="008506000#85" />
		</Dest>
		<ReqT a="0" date="20101027" time="11:44" />
		<RFlags b="0" f="4" sMode="N" />
	</ConReq>
</ReqC>
"""

class SchedulesController(BaseController):
	entry_url = 'http://xmlfahrplan.sbb.ch/bin/extxml.exe/'
	
	@GET
	def query(self, request):		
		param_means_mask = request.GET.get('means_mask', '1111111111000000')
		param_departure_id = request.GET.get('departure_id', None)
		param_arrival_id = request.GET.get('arrival_id', None)
		param_departure_time = request.GET.get('departure_time', None)
		param_arrival_time = request.GET.get('arrival_time', None)
		param_extensive = bool(request.GET.get('extensive', False))
		
		if param_departure_time is None and param_arrival_time is None:
			is_arrival_time = False
			request_time = datetime.now()
		elif param_departure_time:
			is_arrival_time = False
			request_time = datetime.utcfromtimestamp(float(param_departure_time))
		else:
			is_arrival_time = True
			request_time = datetime.utcfromtimestamp(float(param_arrival_time))
		
		print repr(request_time)
		
		if param_arrival_id is None or param_departure_id is None:
			if param_arrival_id is None:
				raise MissingParameter('arrival_id')
			if param_departure_id is None:
				raise MissingParameter('departure_id')
			return False
			
		formatted_date = request_time.strftime('%Y%m%d')
		formatted_time = request_time.strftime('%H:%M')
		
		request_content = """<?xml version="1.0" encoding="iso-8859-1"?>
<ReqC lang="EN" prod="iPhone3.1" ver="2.3" accessId="MJXZ841ZfsmqqmSymWhBPy5dMNoqoGsHInHbWJQ5PTUZOJ1rLTkn8vVZOZDFfSe">
	<ConReq>
		<Start>
			<Station externalId="{departure_id}" />
			<Prod prod="{means_mask}" />
		</Start>
		<Dest>
			<Station externalId="{arrival_id}" />
		</Dest>
		<ReqT a="{is_arrival_time}" date="{formatted_date}" time="{formatted_time}" />
		<RFlags b="0" f="6" sMode="N" />
	</ConReq>
</ReqC>""".format(departure_id=param_departure_id, arrival_id=param_arrival_id, is_arrival_time='%i' % (is_arrival_time), formatted_date=formatted_date, formatted_time=formatted_time, means_mask=param_means_mask)


		print request_content

		h = Http()
		resp, content = h.request(self.entry_url, "POST", request_content)
		if resp['status'] != '200':
			# TODO: Error Handling Here!
			return
		
		root = etree.fromstring(content)
		request_id = root.find(".//ConResCtxt").text
		
		connection_nodes = root.findall(".//ConnectionList/Connection")
		connections = []
		for node in connection_nodes:
			date = node.find(".//Overview/Date").text
			departure_node = node.find(".//Overview/Departure/BasicStop/Station")
			departure = {
				'station_name': departure_node.get('name')
			}
			departure_time = node.find(".//Overview/Departure/BasicStop/Dep/Time").text
			departure_platform = node.find(".//Overview/Departure/BasicStop/Dep/Platform/Text").text
			
			arrival_node = node.find(".//Overview/Arrival/BasicStop/Station")
			arrival = {
				'station_name': arrival_node.get('name')
			}
			arrival_time = node.find(".//Overview/Arrival/BasicStop/Arr/Time").text
			arrival_platform = node.find(".//Overview/Arrival/BasicStop/Arr/Platform/Text").text
			
			duration = node.find(".//Overview/Duration/Time").text
			transfers = node.find(".//Overview/Transfers").text
			
			conn = {
				'connection_date': date,
				'departure_station': departure,
				'departure_time': departure_time,
				'departure_platform': departure_platform,
				'arrival_station': arrival,
				'arrival_time': arrival_time,
				'arrival_platform': arrival_platform,
				'connection_duration': duration,
				'connection_transfers': transfers,
			}
			
			connections.append(conn)
		
		
		return {
			'request_id':request_id,
			'connections':connections,
		}
		
		
	@GET
	def getLater(self, params):
		pass
	
	
	@GET
	def getEarlier(self, params):
		pass
	
	
	