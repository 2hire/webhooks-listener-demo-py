from wld.resources.listener import ListenerResource


# Link endpoint to a specific resource
def initialize_routes(api):

    api.add_resource(ListenerResource, '/listener')
