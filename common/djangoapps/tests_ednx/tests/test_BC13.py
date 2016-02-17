from django.test import TestCase


class MicrositeApiTestCase(TestCase):
    """
    Testing the microsite api Edunext module. We could find some inspiration
    by seeing http://www.django-rest-framework.org/api-guide/testing/.
    Need to test that, for different requests we get the expected responses.
    """
    def setUp(self):
        """
        setup variables for every test case
        """
