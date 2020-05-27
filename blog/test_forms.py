from django.test import TestCase
from .forms import BlogPostForm


class TestBlogPostForm(TestCase):

    def test_cannot_create_a_blog_post_without_content(self):
        form = BlogPostForm({"content": ""})
        self.assertFalse(form.is_valid())

    def test_can_create_a_blog_post(self):
        form = BlogPostForm(
            {
                "title": "TestTitle",
                "animal_name": "TestName",
                "content": "TestContent"
            }
        )
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_title(self):
        form = BlogPostForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["title"],
            [u'This field is required.']
        )
