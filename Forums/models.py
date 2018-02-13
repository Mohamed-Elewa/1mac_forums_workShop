class Member:
    """ Creates a new member """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print 'User Name:', self.name, '- Age:', self.age


class Post:
    """ Creates a new post """
    def __init__(self, title, content, creator):
        self.title = title
        self.content = content
        self.creator = creator

    def info(self):
        print 'Post Title:', self.title, 'By:', self.creator

    def content(self):
        print 'Post Content:', self.content


def seperator(i):
    print '-' * i
