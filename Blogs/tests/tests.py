import re
from unittest import result
from urllib import response
from rest_framework.test import APITestCase
from BlogApp.models import Post
from django.urls import reverse

class BlogTestCase1(APITestCase):
    def setUp(self):
        Post.objects.create(title="Sriya", author="sri", genre="Romance", description="abc", publish_date="2022-10-13")
        Post.objects.create(title="Charlie", author="chay", genre="comedy", description="xyz", publish_date="2022-10-12")
    
    def test_get_posts(self):
        response=self.client.get(reverse("posts_create"))
        result=response.json()
        print(1)
        print(result)
        l = len(Post.objects.all())
        self.assertEqual(response.status_code,200)
        self.assertEquals(l, 2)
    
    def test_post_posts(self):
        data = {
            "title":"hello",
            "author":"hi",
            "genre":"greet",
            "description":"some",
            "publish_date":"2022-10-10"
        }
        response=self.client.post(reverse("posts_create"),data=data)
        result=response.json()
        print(2)
        print(result)
        l=len(Post.objects.all())
        self.assertEqual(response.status_code,201)
        self.assertEqual(l,3)
        self.assertEqual(result["title"],"hello")
        self.assertEqual(result["author"],"hi")
        self.assertEqual(result["genre"],"greet")
        self.assertEqual(result["description"],"some")
        self.assertEqual(result["publish_date"],"2022-10-10")

class BlogTestCase2(APITestCase):
    def setUp(self):
        Post.objects.create(title="Sriya", author="sri", genre="Romance", description="abc", publish_date="2022-10-13")
        Post.objects.create(title="Charlie", author="chay", genre="comedy", description="xyz", publish_date="2022-10-12")
    
    def test_get_post(self):
        response=self.client.get(reverse("posts_update",args=['Sriya']))
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,200)
        self.assertEquals(result['author'],'sri')
        self.assertEquals(result['genre'],'Romance')
        self.assertEquals(result['description'],'abc')
        self.assertEquals(result['publish_date'],'2022-10-13')
    
    def test_put_post(self):
        data = {
            "title":"Sriya",
            "author" : "hi",
            "genre" : "greet",
            "description" : "some",
        }
        response=self.client.put(reverse("posts_update",args=[data['title']]),data=data)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,200)
        self.assertEquals(result['author'],'hi')
        self.assertEquals(result['genre'],'greet')
        self.assertEquals(result['description'],'some')

    def test_delete_post(self):
        response=self.client.delete(reverse("posts_update",args=['Charlie']))
        self.assertEqual(response.status_code,204)

class BlogTestCase3(APITestCase):
    def setUp(self):
        Post.objects.create(title="Sriya", author="sri", genre="Romance", description="abc", publish_date="2022-10-13")
        Post.objects.create(title="Charlie", author="chay", genre="comedy", description="xyz", publish_date="2022-10-12")
        Post.objects.create(title="anuragh", author="anu", genre="comedy", description="nothing", publish_date="2022-10-11")
        Post.objects.create(title="Arshad", author="sri", genre="action", description="something", publish_date="2022-10-11")
        
    def test_filter_post_genre(self):
        response=self.client.get(reverse("filter_posts_genre",args=['comedy']))
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,200)
        self.assertEquals(len(result),2)
        self.assertEquals(result[0]['author'],'chay')
        self.assertEquals(result[1]['author'],'anu')
        
    def test_filter_post_author(self):
        response=self.client.get(reverse("filter_posts_author",args=['sri']))
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,200)
        self.assertEquals(len(result),2)
        self.assertEquals(result[0]['genre'],'action')
        self.assertEquals(result[1]['genre'],'Romance')
    
    def test_filter_posts_between_dates(self):
        response=self.client.get(reverse("filter_posts_between_dates",args=['2022-10-11','2022-10-12']))
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,200)
        self.assertEquals(len(result),2)
        self.assertEquals(result[0]['author'],'sri')
        self.assertEquals(result[1]['author'],'chay')