from django.test import TestCase


class CoursesLinksMicrositeAwareTestCase(TestCase):
    """
    Tests to verify to correct behavior of microsite aware course links
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_get_lms_link_for_item_with_microsite(self):
        """
        Test that function get_lms_link_for_item returns the correct link
        to a course, based on the org of the course and current microsite.
        Where: cms/djangoapps/contentstore/utils.py function
        get_lms_link_for_item
        """
        pass

    def test_get_lms_link_for_item_with_no_microsite(self):
        """
        Test that function get_lms_link_for_item returns the correct link
        to a course when no microsite is requested, so links should start
        with LMS_BASE (platform configuration)
        Where: cms/djangoapps/contentstore/utils.py function
        get_lms_link_for_item
        """
        pass
