from django.test import TestCase


class NotFoundResponseWhenMicrositeIsNotFoundTestCase(TestCase):
    """
    Tests to check that the platform is responding with 404 error when a
    domain that does not match with any existent microsite is requested,
    or loading the default microsite if the appropriate raw ip is requested.
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_set_config_by_domain_return_http_404_for_unknown_domain(self):
        """
        Test that, given a domain that does not match with any existent
        microsite, function set_config_by_domain return a http 404 response
        Where: microsite_configuration/backends/database.py methods
        set_config_by_domain of DatabaseMicrositeBackend class
        """
        pass

    def test_set_config_by_domain_load_default_microsite_if_domain_is_ip(self):
        """
        Test that, given a domain that is a raw ip, function set_config_by_domain
        load successfully the defualt microsite (if it exists).
        Where: microsite_configuration/backends/database.py methods
        set_config_by_domain of DatabaseMicrositeBackend class
        """
        pass
