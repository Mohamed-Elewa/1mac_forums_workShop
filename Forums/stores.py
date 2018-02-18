class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        for member in MemberStore.members:
            print member.id, member.name, member.age

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        for member in MemberStore.members:
            if member.id == id:
                return member

    def entity_exists(self, member):
        if self.get_by_id(member.id):
            return True

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)



class PostStore:
    posts = []

    def get_all(self):
        for post in self.posts:
            print post

    def add(self, post):
        self.posts.append(post)
