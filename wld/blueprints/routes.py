from wld.resources.webhook import WebhookResource


# Link endpoint to a specific resource
def initialize_routes(api):

    api.add_resource(WebhookResource, '/webhook')
