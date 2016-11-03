import string
import random
from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from student.forms import AccountCreationForm
from student.views import _do_create_account
from student.roles import OrgRerunCreatorRole, OrgCourseCreatorRole
from student.models import create_comments_service_user
from manage_api.utils import add_organization_from_short_name
from microsite_configuration.models import Microsite


class Command(BaseCommand):
    help = """
    This command creates a new user, org and microsite in the platform.
    Permissions for course creation and rerunning courses are given for the new user
    based on the new org.
    The new microsite uses the new org as its course_org_filter value.

    example:
        manage.py ... create_microsite -u username -p insecure -o a_new_org --platform-name="My incredible site"
    """

    option_list = BaseCommand.option_list + (
        make_option('-u', '--username',
                    metavar='USERNAME',
                    dest='username',
                    default=None,
                    help='Username, defaults to "user_{last_user_id + 1}"'),
        make_option('-n', '--name',
                    metavar='NAME',
                    dest='name',
                    default=None,
                    help='Name, defaults to username'),
        make_option('-p', '--password',
                    metavar='PASSWORD',
                    dest='password',
                    default=None,
                    help='Password for user, defualt to "edx"'),
        make_option('-e', '--email',
                    metavar='EMAIL',
                    dest='email',
                    default=None,
                    help='Email for user, default to "{username}@fake.dev"'),
        make_option('-o', '--organization',
                    metavar='ORGANIZATION',
                    dest='organization',
                    default=None,
                    help='Microsite organization, default to "org_{username}"'),
        make_option('--forum-user',
                    action="store_true",
                    metavar='FORUM USER',
                    dest='forum_user',
                    default=False,
                    help='If present, the forum user is created'),
        make_option('--platform-name',
                    metavar='PLATFORM NAME',
                    dest='platform_name',
                    default=None,
                    help='Display name of the microsite, default to "Platform {username}"'),
        make_option('--subdomain',
                    metavar='SUBDOMAIN',
                    dest='subdomain',
                    default=None,
                    help='subdomain of the microsite, default to "site_{username}.local"'),
    )

    def handle(self, *args, **options):

        # Getting all the needed data to create user and microsite
        final_data = self.get_final_data_from_options(options)

        # Doing user account creation
        form = AccountCreationForm(
            data=final_data["user_data"],
            tos_required=False
        )
        (user, profile, registration) = _do_create_account(form)
        user.is_active = True
        user.save()

        # Creation course creator role for user
        org_short_name = final_data["org_short_name"]
        creator_role = OrgCourseCreatorRole(org_short_name)
        creator_role.add_users(user)
        rerun_role = OrgRerunCreatorRole(org_short_name)
        rerun_role.add_users(user)

        user.is_active = False
        user.save()

        registration.activate()
        print "Created new user " + user.username

        # Creating the new org
        add_organization_from_short_name(org_short_name)

        # Try to create forum user
        if options["forum_user"]:
            create_comments_service_user(user)

        # Creating a new microsite
        new_microsite = Microsite.objects.create(**final_data["microsite_data"])
        print "Created new microsite " + new_microsite.subdomain

        return

    def get_final_data_from_options(self, options):

        # User data
        username = options["username"] or self.generate_username()
        email = options["email"] or username + "@fake.dev"
        password = options["password"] or "edx"
        name = options["name"] or username

        # Org data
        org_short_name = options["organization"] or "org_" + username

        # Microsite data
        platform_name = options["platform_name"] or "Platform " + username
        microsite_subdomain = options["subdomain"] or slugify("site_" + username) + ".local"

        def_microsite_config = {
            "PLATFORM_NAME": platform_name,
            "css_overrides_file": "site-assets/aegir/css/identity.css",
            "template_dir": "templates/aegir",
            "course_org_filter": org_short_name,
            "SITE_NAME": microsite_subdomain
        }
        microsite_key = ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(10)
        )

        return {
            "user_data": {
                "username": username,
                "email": email,
                "password": password,
                "name": name
            },
            "org_short_name": org_short_name,
            "microsite_data": {
                "key": microsite_key,
                "subdomain": microsite_subdomain,
                "values": def_microsite_config
            }
        }

    def generate_username(self):

        last_user = User.objects.all().last()
        return "user_" + unicode(last_user.id + 1)
