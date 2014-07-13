from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class UserListTests(APITestCase):

    def test_no_users(self):
        response = self.client.get(reverse("api:user-list"))

        # Users key should be empty but present for consistency
        self.assertTrue("users" in response.data)

        # No pagination links should be included - there are no pages
        self.assertFalse("Link" in response)

        # No unexpected users were returned
        self.assertEqual(len(response.data["users"]), 0)

    def test_users_returned(self):
        from gitview.accounts.models import User

        user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        response = self.client.get(reverse("api:user-list"))

        # Users key is is where the list is returned
        self.assertTrue("users" in response.data)

        # For a single user pagination isn't needed
        self.assertFalse("Link" in response)

        # Make sure a single user was actually returned
        self.assertEqual(len(response.data["users"]), 1)

        # All users should have an id
        self.assertTrue("id" in response.data["users"][0])

        # Confirm the user is the one we created
        self.assertEqual(response.data["users"][0]["id"], user.id)

    def test_pagination(self):
        from gitview.accounts.models import User

        first_user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        second_user = User.objects.create(
            first_name="Another",
            last_name="User",
            username="another",
        )

        url = reverse("api:user-list") + "?per_page=1"

        response = self.client.get(url)

        # Make sure the Link header is returned with the second page
        self.assertTrue("Link" in response)

        # The first user should have been returned still
        self.assertTrue("users" in response.data)

        # Make sure only one user was returned
        self.assertEqual(len(response.data["users"]), 1)

        # Make sure the id key is present
        self.assertTrue("id" in response.data["users"][0])

        # Check that it was the first user
        self.assertEqual(response.data["users"][0]["id"], first_user.id)

    def test_inline_links_repositories(self):
        from gitview.accounts.models import User

        user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        response = self.client.get(reverse("api:user-list"))

        # Test that the user was returned
        self.assertTrue("users" in response.data)

        # Make sure the user was returned
        self.assertEqual(len(response.data["users"]), 1)

        # The repositories should be under the links key
        self.assertTrue("links" in response.data["users"][0])

        # Check that the key was returned
        self.assertTrue("repositories" in response.data["users"][0]["links"])

    def test_root_links_repositories(self):
        from gitview.accounts.models import User

        # A user must exist for the reflection to work
        # jsonapi doesn't require it on empty responses
        user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        response = self.client.get(reverse("api:user-list"))

        # Test that links were returned
        self.assertTrue("links" in response.data)

        # Test that users.repositories is linked
        self.assertTrue("users.repositories" in response.data["links"])

        # Make sure the link object was returned
        self.assertTrue("href" in response.data["links"]["users.repositories"])
        self.assertTrue("type" in response.data["links"]["users.repositories"])

        # Check that the link format is right
        self.assertTrue("/api/repositories/{user.repositories}" in
                        response.data["links"]["users.repositories"]["href"])

        # The repository type should always be "repositories"
        self.assertEqual(response.data["links"]["users.repositories"]["type"],
                         "repositories")

class UserDetailTests(APITestCase):

    def test_user_doesnt_exist(self):
        response = self.client.get(reverse("api:user-detail", args=[404]))

        # Ensure a 404 is returned
        self.assertEqual(response.status_code, 404)

        # Errors key should be returned
        self.assertTrue("errors" in response.data)

        # Users key should not be returned at all
        self.assertFalse("users" in response.data)

        # Only one error should be returned
        self.assertEqual(len(respnse.data["errors"]), 1)

        # "Not found" should be the title
        self.assertEqual(response.data["erorrs"][0]["title"], "Not found")

    def test_user_exists(self):
        from gitview.accounts.models import User

        user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        response = self.client.get(reverse("api:user-detail", args=[user.id]))

        # Ensure a user was returned and not an error
        self.assertTrue("users" in response.data)

        # All users should have an id
        self.assertTrue("id" in response.data["users"])

        # Make sure it was the right user
        self.assertEqual(response.data["id"], user.id)

    def test_root_links_repositories(self):
        from gitview.accounts.models import User

        user = User.objects.create(
            first_name="First",
            last_name="Last",
            username="test",
        )

        response = self.client.get(reverse("api:user-detail", args=[user.id]))

        # Ensure that the links key was returned
        self.assertTrue("links" in response.data)
