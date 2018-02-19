class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        for member in self.get_all():
            if member.id == id:
                return member

    def get_by_name(self, name):
        for member in self.get_all():
            if member.name == name:
                return member

    def entity_exists(self, member):
        if self.get_by_id(member.id):
            return True

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, id):
        member = self.get_by_id(id)
        return member


class PostStore:
    posts = []

    def get_all(self):
        for post in self.posts:
            print post

    def add(self, post):
        self.posts.append(post)
