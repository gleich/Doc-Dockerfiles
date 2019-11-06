import request_utils
import json

def test_get_image_meta():
    """Tests the get_image_meta function
    """
    working_instance = request_utils.get_image_meta("mattgleich", "fib-calc-client")
    expected_response = {
        "user": "mattgleich",
        "name": "fib-calc-client",
        "namespace": "mattgleich",
        "repository_type": "image",
        "status": 1,
        "description": "",
        "is_private": False,
        "is_automated": False,
        "can_edit": False,
        "star_count": 0,
        "pull_count": 7,
        "last_updated": "2019-09-29T18:52:43.923069Z",
        "is_migrated": False,
        "has_starred": False,
        "full_description": None,
        "affiliation": None,
        "permissions": {
            "read": True,
            "write": False,
            "admin": False
        }
    }
    assert working_instance == expected_response
    failing_instance = request_utils.get_image_meta("mattgleich", "fakeImageName")
    assert failing_instance == None
