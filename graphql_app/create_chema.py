import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


schema = graphene.Schema(query=Query)

result = schema.execute('{ hello ( name: "Test" )}')
print(result.data['hello'])  # "Hello stranger"


class Episode(graphene.Enum):
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        return 'Other episode'


Episode_ = graphene.Enum('Episode', [('NEWHOPE', 4), ('EMPIRE', 5), ('JEDI', 6)])

# graphene.Enum.from_enum(AlreadyExistingPyEnum, description=lambda value: return 'foo' if value == AlreadyExistingPyEnum.Foo else 'bar')

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


Episode__ = graphene.Enum.from_enum(Color)
print(Episode__.get(1))
print(Color.RED)

import datetime
from graphene.types import Scalar
from graphql.language import ast


class DateTime(Scalar):
    '''DateTime Scalar Description'''

    @staticmethod
    def serialize(dt):
        return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def parse_value(value):
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")


dt = DateTime()
print(dt.parse_value("1990-3-2T11:22:22.3"))


class Character(graphene.ObjectType):
    name = graphene.NonNull(graphene.String)


class Character(graphene.ObjectType):
    name = graphene.String(required=True)


ch = Character()

print(ch.name)


# class Query(graphene.ObjectType):
#     hello = Character(name=graphene.String)
#     # User = graphene.Field(User, id=graphene.ID(required=True))
#
#     def resolve_hello(self, info, name):
#         return 'Hello ' + name
#
# schema = graphene.Schema(query=Query)
# result = schema.execute('{ hello ( name: "Test" )}')
# print(result.data['hello'])  # "Hello stranger"
#
# # ch = Character('str')
# # print(ch)
#
# # schema = graphene.Schema(query=Character)
# #
# # result = schema.execute('{ name }')
# # print(result.data['nane'])  # "Hello stranger"
#
#
# class Character(graphene.ObjectType):
#     name = graphene.String(required=True)


class Query(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return info.context.get('name')


schema = graphene.Schema(Query)
result = schema.execute('{ name }', context_value={'name': 'Syrus'})
print(result.data['name'])


# class User(graphene.ObjectType):
#     firstName = graphene.String()
#     lastName = graphene.String()
#     id = graphene.ID()

####################################################################################################################

class User(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    id = graphene.ID()


users = [User(first_name='Peter', last_name='Griffin', id=1), User(first_name='Ivan', last_name='Banan', id=12)]


class Query(graphene.ObjectType):
    user = graphene.List(User, id=graphene.ID())

    def resolve_user(self, info, id):
        return [user for user in users if user.id == int(id)]


schema = graphene.Schema(Query)

result = schema.execute(
    '''query getUser($id: ID) {
        user(id: $id) {
            id
            firstName
            lastName
        }
    }''',
    variable_values={'id': 12}
)
print(result.data['user'])


class Query(graphene.ObjectType):
    user = graphene.List(User, id=graphene.ID())

    def resolve_user(self, info, id):
        return [user for user in info.context if user.id == int(id)]


schema = graphene.Schema(Query)

result = schema.execute(
    '''query getUser($id: ID) {
        user(id: $id) {
            id
            firstName
            lastName
        }
    }''',
    variable_values={'id': 2},
    context_value=[User(first_name='Peter', last_name='Griffin', id=1),
                   User(first_name='Ivan', last_name='Banan', id=12),
                   User(first_name='Stepan', last_name='Orange', id=2)]
)
print(result.data['user'])

####################################################################################################################

# result = schema.execute(
#     '{ user (id: 12)}'
# '''query getUser($id: ID) {
#         user(id: $id)
# }''',
# variable_values={'id': '12'}
# )
# result = schema.execute(
#     '''query getUser($id: ID) {
#         user(id: $id) {
#             id
#             firstName
#             lastName
#         }
#     }''',
#     variable_values={'id': '12'}
# )

# print(result.data)


import graphene


class Query(graphene.ObjectType):
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, info, word):
        return word[::-1]


schema = graphene.Schema(Query)
result = schema.execute('{ reverse (word: "полиндром")}')
print(result.data['reverse'])



class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        if info.field_name == 'user':
            return None
        return next(root, info, **args)

result = schema.execute('THE QUERY', middleware=[AuthorizationMiddleware()])
print(result.data)

from time import time as timer


# def timing_middleware(next, root, info, **args):
#     start = timer()
#     return_value = next(root, info, **args)
#     duration = timer() - start
#     logger.debug("{parent_type}.{field_name}: {duration} ms".format(
#         parent_type=root._meta.name if root and hasattr(root, '_meta') else '',
#         field_name=info.field_name,
#         duration=round(duration * 1000, 2)
#     ))
#     return return_value