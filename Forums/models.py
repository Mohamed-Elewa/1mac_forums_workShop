class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Post:
    def __init__(self, title, content, creator):
        self.title = title
        self.content = content
        self.creator = creator


class MemberStore:
    members = []

    def get_all(self):
        for member in self.members:
            print member

    def add(self, member):
        self.members.append(member)


class PostStore:
    posts = []

    def get_all(self):
        for post in self.posts:
            print post

    def add(self, post):
        self.posts.append(post)


def separator(i):
    print '-' * i
