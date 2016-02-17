from django.test import TestCase


class MicrositeMultiorgDatabaseBackendTestCase(TestCase):
    """
    Tests concerning to microsite multiorg feature on top of database microsite
    backend
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_get_course_enrollments_multiorg_branding_microsite(self):
        """
        verify that get_course_enrollments function is returning the correct
        enrollments according to the organizations a specific microsite belongs to.
        Where: branding/views.py get_course_enrollments function
        """
        pass

    def test_get_course_enrollments_multiorg_student_microsite(self):
        """
        verify that get_course_enrollments function is returning the correct
        enrollments according to the organizations a specific microsite belongs to.
        Where: student/views.py get_course_enrollments function
        """
        pass

    def test_get_value_for_org_database_microsite_backend(self):
        """
        Test that function get_value_for_org is returning the right value of a config,
        based on a passed organization who has to match with org filter parameter of any
        existent microsite.
        Where: microsite_configuration/backends/database.py get_value_for_org method
        """
        pass

    def test_get_all_orgs_database_microsite_backend(self):
        """
        Test that function get_all_orgs is returning all existent organizations regardless of
        the type of data stored in 'course_org_filter' key (string or array).
        Where: microsite_configuration/backends/database.py get_all_orgs method
        """
        pass

    def test_MicrositeCrossBrandingFilterMiddleware_multiorg(self):
        """
        verify that middleware is working properly, just letting pass requests for courses branded
        with orgs that match with the 'course_org_filter' value of the current microsite, and rising
        a http 404 response otherwise.
        Where: microsite_configuration/middleware.py MicrositeCrossBrandingFilterMiddleware class
        """
        pass
