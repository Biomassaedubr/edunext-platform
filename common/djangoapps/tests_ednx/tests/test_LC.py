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
        released languages list.
        Where: microsite_aware_functions/language function ma_language
        """
        pass

    def test_edraak_i18n_middleware(self):
        """
        Make sure that middleware in working as expected
        Where: edraak_18n/middleware.py
        """
        pass

    def test_set_language_edraak_view(self):
        """
        Test that set_language view is working as expected
        where: edraak_18n/views.py set_language view
        """
        pass
