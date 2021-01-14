from flask_be_template.resources.examples import ExamplesResource


# Link endpoint to a specific resource
def initialize_routes(api):

    api.add_resource(ExamplesResource, '/examples')
