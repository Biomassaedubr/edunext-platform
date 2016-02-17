from django.test import TestCase


class CourseAndOrgLevelRerunPermissionsTestCase(TestCase):
    """
    Tests for new student roles with rerun permissions
    """
    def setUp(self):
        """
        setup variables for every test case
        """

    def test_granted_permissions_to_rerun_courses_for_custom_roles(self):
        """
        Test that only the roles CourseRerunCreatorRole, CourseRerunCreatorRole,
        and OrgCourseCreatorRole have the permission to rerun courses
        """
        pass
