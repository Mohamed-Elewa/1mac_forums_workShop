import models

member1 = models.Member('user 1', '10')
member2 = models.Member('user 2', '20')

member_store = models.MemberStore()
member_store.add(member1.name)
member_store.add(member2.name)

member_store.get_all()
models.separator(35)

post1 = models.Post('post title 1', 'post 1 content', 'user 1')
post2 = models.Post('post title 2', 'post 2 content', 'user 1')
post3 = models.Post('post title 3', 'post 3 content', 'user 2')

posts_list = [post1, post2, post3]
posts_store = models.PostStore()

for post in posts_list:
    posts_store.add(post.title)

posts_store.get_all()
