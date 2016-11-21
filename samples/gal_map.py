import pygal
from world_population import WorldPopulation

wp = WorldPopulation()
wm = pygal.maps.world.World()
wm.force_uri_protocol = 'http'

wm.add("2k", wp.pop_of(2000))

wm.render_to_file('us.svg')