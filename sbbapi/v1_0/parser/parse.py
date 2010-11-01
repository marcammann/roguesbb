from lxml import etree
from datetime import datetime, time, date


def time_from_sbbtime(sbbtime):
	return datetime.strptime(sbbtime, '00d%H:%M:%S')

def date_from_sbbdate(sbbdate):
	return datetime.strptime(sbbdate, '%Y%m%d')


def station_from_node(node):
	station = {
		'station_name': node.get("name"),
		'station_coordinates': {
			'type': 'WGS',
			'latitude': node.get("x")[:-6] + '.' + node.get("x")[-6:-1],
			'longitude': node.get("y")[:-6] + '.' + node.get("y")[-6:-1],
		},
		'station_id': node.get("externalStationNr"),
		'station_type': node.tag,
	}

	return station
	
	
def platformtime_from_node(node):
	sbbtime = node.find(".//Time").text.strip()
	platform = node.find(".//Platform/Text").text
	if platform:
		platform = platform.strip()
	else:
		platform = ''
		
	retval = {
		'time': time_from_sbbtime(sbbtime).strftime('%H:%M:%S'),
		'platform': platform,
	}
	
	return retval
	
	
def stop_from_node(node, subgroup=False):	
	retval = {}
	
	station_node = node.find(".//Station")
	if station_node is not None:
		station = station_from_node(station_node)
		retval['station'] = station
	
	dep_node = node.find(".//Dep")
	arr_node = node.find(".//Arr")
	if arr_node is not None and dep_node is not None:
		retval['departure'] = platformtime_from_node(dep_node)
		retval['arrival'] = platformtime_from_node(arr_node)
	elif arr_node is not None:
		pt = platformtime_from_node(arr_node)
		if subgroup:
			retval['arrival'] = pt
		else:
			retval['time'] = pt['time']
			retval['platform'] = pt['platform']
	elif dep_node is not None:
		pt = platformtime_from_node(dep_node)
		if subgroup:
			retval['departure'] = pt
		else:
			retval['time'] = pt['time']
			retval['platform'] = pt['platform']
	else:
		return None
	
	return retval
	

def segments_from_node(node):
	# Segments (crazy stuff... whoever did this at Hacon was an asshole)
	unique_nodes = node.xpath('./JourneyAttributeList/JourneyAttribute[Attribute/@type="NAME"]')
	segments = [(int(n.get('from')), int(n.get('to'))) for n in unique_nodes]
	
	stop_nodes = node.findall('./PassList/BasicStop')
	stops = [stop_from_node(n, subgroup=True) for n in stop_nodes]
	stops = filter(lambda x:x is not None, stops)
	
	segment_data = []
	for s in segments:
		name = node.find('./JourneyAttributeList/JourneyAttribute[@from="{from_index}"]/Attribute[@type="NAME"]/AttributeVariant[@type="NORMAL"]/Text'.format(from_index=s[0])).text.strip()
		category = node.find('./JourneyAttributeList/JourneyAttribute[@from="{from_index}"]/Attribute[@type="CATEGORY"]/AttributeVariant[@type="NORMAL"]/Text'.format(from_index=s[0])).text.strip() 
		
		item = {
			'vehicle': {
				'name': name,
				'category': category,
			},
			'stops': stops
		}
		
		segment_data.append(item)
		
	return segment_data
		
		
def connection_from_node(node, extensive):
	date = date_from_sbbdate(node.find(".//Overview/Date").text).strftime('%Y-%m-%d')
	
	print repr(node.find(".//Overview/Departure/BasicStop"))
	
	departure_info = stop_from_node(node.find(".//Overview/Departure/BasicStop"))
	arrival_info = stop_from_node(node.find(".//Overview/Arrival/BasicStop"))
	
	duration = time_from_sbbtime(node.find(".//Overview/Duration/Time").text).strftime('%H:%M:%S')
	transfers = node.find(".//Overview/Transfers").text
	
	product_nodes = node.findall(".//Overview/Products/Product")
	products = [p.get('cat').strip() for p in product_nodes]
	
	
	conn = {
		'date': date,
		'departure': departure_info,
		'arrival': arrival_info,
		'duration': duration,
		'transfers': transfers,
		'products': products,
	}
	
	if (extensive):
		fragment_nodes = node.findall('.//ConSectionList/ConSection')
		fragments = [fragment_from_node(n) for n in fragment_nodes]
		conn['fragments'] = fragments
	
	
	return conn


def fragment_from_node(node):
	departure_info = stop_from_node(node.find("./Departure/BasicStop"))
	arrival_info = stop_from_node(node.find("./Arrival/BasicStop"))
	
	#vehicles = vehicles_from_node(node.find("./Journey"))
	segments = segments_from_node(node.find("./Journey"))
	
	return segments
	
	retval = {
		'departure': departure_info,
		'arrival': arrival_info,
		'segments': segments,
	}
	
	return retval
	


class StationsParser(object):
	def __init__(self, content):
		self.root = etree.fromstring(content)
		
		
	def stations(self):
		results = self.root.findall(".//LocValRes/*")

		stations = []
		for result in results:
			if result.tag == 'Station':
				station = station_from_node(result)
				stations.append(station)
		
		return stations
		
		
class SchedulesParser(object):
	def __init__(self, content):
		self.root = etree.fromstring(content)
		
		
	def connections(self, extensive=False):
		connection_nodes = self.root.findall(".//ConnectionList/Connection")
		connections = []
		for node in connection_nodes:
			conn = connection_from_node(node, extensive=extensive)
			connections.append(conn)
		
		return connections
		
		
	def request_id(self):
		request_id = self.root.find(".//ConResCtxt").text
		
		return request_id
		