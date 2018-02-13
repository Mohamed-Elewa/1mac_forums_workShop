from models import *

member1 = Member('user 1', '10')
member2 = Member('user 2', '20')
Member.info(member1)
Member.info(member2)
seperator(35)

post1 = Post('post title 1', 'post 1 content', 'user 1')
post2 = Post('post title 2', 'post 2 content', 'user 1')
post3 = Post('post title 3', 'post 3 content', 'user 2')

posts_list = [post1, post2, post3]
for post in posts_list:
    Post.info(post)
    Post.content(post)
    seperator(10)
