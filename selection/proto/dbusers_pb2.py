# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='dbusers.proto',
  package='messages',
  serialized_pb='\n\rdbusers.proto\x12\x08messages\"F\n\nUserGroups\x12\x11\n\tgroupName\x18\x01 \x02(\t\x12\x12\n\ngroupSysId\x18\x02 \x02(\x05\x12\x11\n\tgroupList\x18\x03 \x03(\x05\"\x16\n\x14GetUserGroupsRequest\"A\n\x15GetUserGroupsResponse\x12(\n\nuserGroups\x18\x01 \x03(\x0b\x32\x14.messages.UserGroups\"^\n\x06\x44\x42User\x12\x10\n\x08userName\x18\x01 \x02(\t\x12\r\n\x05sysId\x18\x02 \x02(\x05\x12\x10\n\x08\x63reateDB\x18\x03 \x02(\x08\x12\x11\n\tsuperUser\x18\x04 \x02(\x08\x12\x0e\n\x06\x63\x61tupd\x18\x05 \x02(\x08\"\x13\n\x11GetDBUsersRequest\"5\n\x12GetDBUsersResponse\x12\x1f\n\x05users\x18\x01 \x03(\x0b\x32\x10.messages.DBUserB/\n\x1eru.nicetu.integration.messagesB\rDBUsersProtos')




_USERGROUPS = descriptor.Descriptor(
  name='UserGroups',
  full_name='messages.UserGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='groupName', full_name='messages.UserGroups.groupName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupSysId', full_name='messages.UserGroups.groupSysId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupList', full_name='messages.UserGroups.groupList', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=97,
)


_GETUSERGROUPSREQUEST = descriptor.Descriptor(
  name='GetUserGroupsRequest',
  full_name='messages.GetUserGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=99,
  serialized_end=121,
)


_GETUSERGROUPSRESPONSE = descriptor.Descriptor(
  name='GetUserGroupsResponse',
  full_name='messages.GetUserGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userGroups', full_name='messages.GetUserGroupsResponse.userGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=123,
  serialized_end=188,
)


_DBUSER = descriptor.Descriptor(
  name='DBUser',
  full_name='messages.DBUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userName', full_name='messages.DBUser.userName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sysId', full_name='messages.DBUser.sysId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='createDB', full_name='messages.DBUser.createDB', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='superUser', full_name='messages.DBUser.superUser', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='catupd', full_name='messages.DBUser.catupd', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=190,
  serialized_end=284,
)


_GETDBUSERSREQUEST = descriptor.Descriptor(
  name='GetDBUsersRequest',
  full_name='messages.GetDBUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=286,
  serialized_end=305,
)


_GETDBUSERSRESPONSE = descriptor.Descriptor(
  name='GetDBUsersResponse',
  full_name='messages.GetDBUsersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='users', full_name='messages.GetDBUsersResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=307,
  serialized_end=360,
)

_GETUSERGROUPSRESPONSE.fields_by_name['userGroups'].message_type = _USERGROUPS
_GETDBUSERSRESPONSE.fields_by_name['users'].message_type = _DBUSER
DESCRIPTOR.message_types_by_name['UserGroups'] = _USERGROUPS
DESCRIPTOR.message_types_by_name['GetUserGroupsRequest'] = _GETUSERGROUPSREQUEST
DESCRIPTOR.message_types_by_name['GetUserGroupsResponse'] = _GETUSERGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['DBUser'] = _DBUSER
DESCRIPTOR.message_types_by_name['GetDBUsersRequest'] = _GETDBUSERSREQUEST
DESCRIPTOR.message_types_by_name['GetDBUsersResponse'] = _GETDBUSERSRESPONSE

class UserGroups(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERGROUPS
  
  # @@protoc_insertion_point(class_scope:messages.UserGroups)

class GetUserGroupsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETUSERGROUPSREQUEST
  
  # @@protoc_insertion_point(class_scope:messages.GetUserGroupsRequest)

class GetUserGroupsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETUSERGROUPSRESPONSE
  
  # @@protoc_insertion_point(class_scope:messages.GetUserGroupsResponse)

class DBUser(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DBUSER
  
  # @@protoc_insertion_point(class_scope:messages.DBUser)

class GetDBUsersRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDBUSERSREQUEST
  
  # @@protoc_insertion_point(class_scope:messages.GetDBUsersRequest)

class GetDBUsersResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETDBUSERSRESPONSE
  
  # @@protoc_insertion_point(class_scope:messages.GetDBUsersResponse)

# @@protoc_insertion_point(module_scope)