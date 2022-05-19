import unittest
from app.models import Post, User
from app import db

class PostModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_wam = User(username='wambui',password='1234', email='wambui@gmail.com')
        self.Post = Post(title='Travel', Post='Travel the world!', user=self.user_wam)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.Post.title, 'Travel')
        self.assertEquals(self.Post.Post, 'Travel the world!')
        self.assertEquals(self.Post.User, self.user_wam)

    def test_save_Post(self):
        self.Post.save_Post()
        self.assertTrue(len(Post.query.all()) > 0)