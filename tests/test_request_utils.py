import request_utils
import json

def test_get_image_meta():
    """Tests the get_image_meta function
    """
    working_instance = request_utils.get_image_meta("mattgleich", "fib-calc-client")
    assert type(working_instance) == type({})
    failing_instance = request_utils.get_image_meta("mattgleich", "fakeImageName")
    assert failing_instance == None
