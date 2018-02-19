import models
import utils
import stores


def create_members():
    member1 = models.Member("user 1", 10)
    member2 = models.Member("user 2", 20)
    member3 = models.Member("user 3", 25)

    return member1, member2, member3


def store_members(members_instances, member_store):
    print 'Storing Members'

    for member in members_instances:
        member_store.add(member)

    utils.separator(30)


def print_all_members(member_store):
    print('All Members:')

    for member in member_store.get_all():
        print(member.name)

    utils.separator(30)


def get_by_id(id):
    print'Getting member By ID:', id

    print member_store.get_by_id(id).name

    utils.separator(30)


def get_by_name(name):
    print'Getting member By Name:', name

    print member_store.get_by_name(name).id

    utils.separator(30)


def delete(id):
    print 'Deleting ID:', id

    try:
        member_store.delete(id)
    except ValueError:
        print("It should be an existence entity before deleting !")

    utils.separator(30)


def update(id):
    print 'Updating ID:', id

    member = member_store.update(id)
    member.name += ' edited'

    utils.separator(30)


members_instances = create_members()
member1, member2, member3 = members_instances

member_store = stores.MemberStore()
store_members(members_instances, member_store)

print_all_members(member_store)

get_by_id(2)

delete(2)

print_all_members(member_store)

update(3)

print_all_members(member_store)

get_by_name('user 1')
