# A test file is supplied. No run log or current-revision result is supplied.
from implementation import open_link


def test_open_link_accepts():
    assert open_link({'status': 'draft'})['status'] == 'accepted'
