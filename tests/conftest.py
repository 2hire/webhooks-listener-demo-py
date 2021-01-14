import pytest

import flask_be_template

@pytest.fixture(scope='module')
def app():

    app = flask_be_template.create_app()
    return app


@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as c:
        yield c