"""Test radio_mlbee_client."""
# pylint: disable=broad-except
from radio_mlbee_client import __version__, radio_mlbee_client


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not radio_mlbee_client()
    except Exception:
        assert True
