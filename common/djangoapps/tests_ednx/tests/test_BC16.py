from django.test import TestCase


class SettingsProxyObjectTestCase(TestCase):
    """
    Tests for settings proxy object
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_call_settings_with_value_present_in_microsite(self):
        """
        check that using the proxy object, a call to a specific settings value returns
        the right answer if value is present in microsite settings (should return the
        microsite value)
        """
        pass

    def test_call_settings_with_value_not_present_in_microsite(self):
        """
        check that using the proxy object, a call to a specific settings value returns
        the right answer if value is not present in microsite settings (should return the
        platform value)
        """
        pass

    def test_get_dict_for_microsite(self):
        """
        test that function get_dict is working as expected returning a merge of microsite
        settings values and platform settings values
        Where: microsite_configuration/backends get_dict function in backends who have this
        method implemented
        """
        pass
