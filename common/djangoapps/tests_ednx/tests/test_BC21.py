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
        settings.
        Where: microsite_configuration/microsite function get_backend
        """
        pass

    def test_get_backend_from_non_existent_module_in_settings_configuration(self):
        """
        get_backend function raise a exception if microsite backend in settings does
        not exist.
        Where: microsite_configuration/microsite function get_backend
        """
        pass

    def test_enable_microsites_in_backend(self):
        """
        Test if microsites are initialized correctly with function enable_microsites
        in backends.
        Where: microsite_configuration/backends/base function enable_microsites
        """
        pass

    def test_microsite_template_backend(self):
        """
        Test that the template backend for microsites is working properly.
        Where: microsite_configuration/backends function get_template_path over existent
        backends (mainly database backends as it's the ours)
        """
        pass

    def test_get_organizations_microsite_model(self):
        """
        Test the get_organization function  in Microsite model in order to make sure that
        it's working properly selecting the right organization for a microsite.
        Where: microsite_configuration/models function get_organizations in Microsite model
        """
        pass

    def test_get_microsite_for_domain_microsite_model(self):
        """
        verify that the right microsite is selected according a specific domain. Test happy
        and sad paths.
        Where: microsite_configuration/models function get_microsite_for_domain in Microsite model
        """
        pass

    def test_get_organizations_for_microsite_by_pk_micrositeorganizationmapping_model(self):
        """
        Test that organizations are correctly filtered by a microsite pk.
        Where: microsite_configuration/models function get_organizations_for_microsite_by_pk in
        MicrositeOrganizationMapping model
        """
        pass

    def test_get_microsite_for_organization_micrositeorganizationmapping_model(self):
        """
        verify that the correct microsite microsite is fetcched given an organization
        Where: microsite_configuration/models function get_microsite_for_organization in
        MicrositeOrganizationMapping model
        """
        pass

    def test_get_templete_for_microsite_micrositetemplate_model(self):
        """
        Test that a correct template is selected for a specific microsite
        Where: microsite_configuration/models function get_templete_for_microsite in
        MicrositeTemplate model
        """
        pass
