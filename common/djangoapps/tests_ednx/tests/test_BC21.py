from django.test import TestCase


class MicrositeBackendInterfaceTestCase(TestCase):
    """
    Microsite backend interface unit tests
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_get_backend_from_existent_module_in_settings_configuration(self):
        """
        validates that function get_backend select an existent microsite backend from
        settings
        """
        pass

    def test_get_backend_from_non_existent_module_in_settings_configuration(self):
        """
        get_backend function raise a exception if microsite backend in settings does
        not exist
        """
        pass
