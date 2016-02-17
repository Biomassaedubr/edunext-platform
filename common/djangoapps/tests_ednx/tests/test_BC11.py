from django.test import TestCase


class MicrositeAwareSettingsCallsTestCase(TestCase):
    """
    Tests related to microsite aware calls to settings across the platform.
    Maybe is enough just testing the get_value function and the proxy object
    created in openedx.conf (those tests should be implemented in other files,
    so reimplement them here could be redundant)
    """
    def setUp(self):
        """
        setup variables for every test case
        """
