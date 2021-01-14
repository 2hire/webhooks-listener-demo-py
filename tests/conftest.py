import pytest

import wld

@pytest.fixture(scope='module')
def app():

    app = wld.create_app()
    return app


@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as c:
        yield c