from django.test import SimpleTestCase

from app_two import views


class ViewsTests(SimpleTestCase):
    def test_make_list_unique(self):
        """Test making a list unique."""
        sample_items = [1, 1, 2, 2, 3, 4, 5, 5]

        res = views.remove_duplicates(sample_items)

        self.assertEqual(res, [1, 2, 3, 4, 5])
