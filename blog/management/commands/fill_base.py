
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

from blog.models import Comment, Post

fake = Faker()
UserModel = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(10, 500), help='Number of records for Users'
                                                                            '(from 10 to 500)')

    def handle(self, *args, **options):
        count = options['count']

        for i in range(count):
            User.objects.create(username=fake.name(), password=make_password('password'))

        posts = []
        for el in UserModel.objects.all():
            for i in range(5):
                posts.append(Post(title=fake.sentence(nb_words=2), breif_description=fake.sentence(nb_words=5),
                                  full_description=fake.text(), author=el))
        Post.objects.bulk_create(posts)

        comments = []
        for el in Post.objects.all():
            for i in range(7):
                comments.append(Comment(username=fake.name(), text=fake.sentence(nb_words=4), post=el))
        Comment.objects.bulk_create(comments)

        self.stdout.write(self.style.SUCCESS('Successfully filled database'))
