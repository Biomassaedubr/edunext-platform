from mock import patch

from django.test import TestCase

from branding import get_logo_url


class PatchStaticUrlsTestCase(TestCase):
    """
    Tests related to microsite aware calls to settings across the platform
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    @patch('microsite_configuration.microsite.get_value', call_args=("logo_image_url",), return_value="http://edx-test.org/image.jpg")
    def test_image_exists_and_is_returned_with_http(self, get_value):

        logo_url = get_logo_url()
        self.assertEqual(logo_url, "http://edx-test.org/image.jpg")
