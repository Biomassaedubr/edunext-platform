from django.test import TestCase


class UsernameUnicodeTestCase(TestCase):
    """
    Tests to verify the capability to allow unicode usernames for open-edx
    register
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_username_have_to_pass_through_edraak_validator_filter(self):
        """
        validate that, given some correct unicode usernames, it passes successfully
        the validator filter.
        Where: common/djangoapps/student/edraak_validation.py validate_username
        """
        pass

    def test_username_have_to_fail_edraak_validator_filter(self):
        """
        validate that, given some incorrect unicode usernames, it passes successfully
        the validator filter.
        Where: common/djangoapps/student/edraak_validation.py validate_username
        """
        pass
