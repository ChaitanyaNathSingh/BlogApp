from unittest import result
from rest_framework.test import APITestCase
from BlogApp.models import Post
from django.urls import reverse

class BlogTestCase1(APITestCase):
    def setUp(self):
        Post.objects.create(title="Sriya", author="sri", genre="Romance", description="abc", publish_date="2022-10-13")
        Post.objects.create(title="Charlie", author="chay", genre="comedy", description="xyz", publish_date="2022-10-12")
    
    def test_posts(self):
        response=self.client.get(reverse("posts_create"))
        l = len(Post.objects.all())
        self.assertEqual(response.status_code,200)
        self.assertEquals(l, 2)
    
    def test_author_details(self):
        t = Post.objects.get(title="Sriya")
        self.assertEquals(t.author, "sri")
    
    def test_post(self):
        data = {
            "title":"hello",
            "author":"hi",
            "genre":"greet",
            "description":"some",
            "publish_date":"2022-10-10"
        }
        response=self.client.post(reverse("posts_create"),data=data)
        l=len(Post.objects.all())
        self.assertEqual(response.status_code,201)
        self.assertEqual(l,3)

class BlogTestCase2(APITestCase):
    def setUp(self):
        Post.objects.create(title="Sriya", author="sri", genre="Romance", description="abc", publish_date="2022-10-13")
        Post.objects.create(title="Charlie", author="chay", genre="comedy", description="xyz", publish_date="2022-10-12")
    
    def test_post(self):
        data = {
            "author":"hi",
            "genre":"greet",
            "description":"some",
            "publish_date":"2022-10-10"
        }
        response=self.client.get(reverse("posts_update",args=['Sriya']))
        self.assertEqual(response.status_code,200)
    