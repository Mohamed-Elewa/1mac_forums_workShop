import models
import utils
import stores

member1 = models.Member('user 1', '10')
member2 = models.Member('user 2', '20')

member_store = stores.MemberStore()
member_store.add(member1)
member_store.add(member2)

print 'All users'
member_store.get_all()
utils.separator(35)

print 'get name by id:',member_store.get_by_id(2).name
utils.separator(35)

print 'is member exists'
print(member_store.entity_exists(member1))
utils.separator(35)

print 'Deleting user'
member_store.delete(2)
utils.separator(35)

print 'All users'
member_store.get_all()
utils.separator(35)

post1 = models.Post('post title 1', 'post 1 content', 'user 1')
post2 = models.Post('post title 2', 'post 2 content', 'user 1')
post3 = models.Post('post title 3', 'post 3 content', 'user 2')

posts_list = [post1, post2, post3]
posts_store = stores.PostStore()

for post in posts_list:
    posts_store.add(post.title)

print 'All Posts'
posts_store.get_all()
