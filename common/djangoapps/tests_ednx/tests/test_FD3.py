from mock import patch

from django.test import TestCase

from branding import get_logo_url


class PatchStaticUrlsTestCase(TestCase):
    """
    Tests related to the patch applied to handle static urls
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    @patch('microsite_configuration.microsite.get_value', call_args=("logo_image_url",), return_value="http://edx-test.org/image.jpg")
    def test_microsite_logo_image_url_exists_and_starts_with_http(self, get_value):
        """
        testing that function get_logo_url from branding module simply return the passed
        image url when the value 'logo_image_url' of the current microsite starts with
        'http'.
        Where: branding/__init__.py function get_logo_url
        """

        logo_url = get_logo_url()
        self.assertEqual(logo_url, "http://edx-test.org/image.jpg")

    def test_microsite_logo_image_url_exists_but_does_not_start_with_http(self):
        """
        testing that function get_logo_url from branding module returns the relative
        url of the image when the value 'logo_image_url' of the current microsite does
        not start with 'http'.
        Where: branding/__init__.py function get_logo_url
        """
        pass

    def test_microsite_logo_image_url_does_not_exist(self):
        """
        testing that function get_logo_url from branding module returns the right
        url of the image when the value 'logo_image_url' of the current microsite does
        not exist.
        Where: branding/__init__.py function get_logo_url
        """
        pass
