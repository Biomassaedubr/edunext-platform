from django.test import TestCase


class ManagementApiTestCase(TestCase):
    """
    Tests related to microsite aware calls to settings across the platform
    """
    def setUp(self):
        """
        setup variables for every test case
        """
