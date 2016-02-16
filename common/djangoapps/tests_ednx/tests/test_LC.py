from django.test import TestCase


class MicrositeLangSelectionTestCase(TestCase):
    """
    This class is intended to test the language selection for a microsite
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_request_language_in_released_languages_list(self):
        """
        ma_language function has to return the request language if it's in
        released languages list
        """
        pass
