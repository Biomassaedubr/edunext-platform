from django.test import TestCase


class CourseAboutLinksMicrositeAwareTestCase(TestCase):
    """
    Tests to verify to correct behavior of microsite aware course about links
    TBD if these tests should be migrated to test_LD7 file
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_get_lms_link_for_about_page_with_microsite(self):
        """
        Test that function get_lms_link_for_about_page returns the correct link
        to a course about page, based on the org of the course and current
        microsite.
        Where: cms/djangoapps/contentstore/utils.py function
        get_lms_link_for_about_page
        """
        pass

    def test_get_lms_link_for_about_page_with_no_microsite(self):
        """
        Test that function get_lms_link_for_item returns the correct link
        to a course about page when no microsite is requested, so links should start
        with LMS_BASE (platform configuration)
        Where: cms/djangoapps/contentstore/utils.py function
        get_lms_link_for_about_page
        """
        pass
