# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rank.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rank.proto',
  package='contest_rank',
  serialized_pb='\n\nrank.proto\x12\x0c\x63ontest_rank\":\n\x06Submit\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\r\n\x05runID\x18\x03 \x01(\t\"\x81\x01\n\x07Problem\x12\x11\n\tproblemID\x18\x01 \x01(\x05\x12$\n\x06submit\x18\x02 \x03(\x0b\x32\x14.contest_rank.Submit\x12\x0f\n\x07\x61\x63index\x18\x03 \x01(\x05\x12\x12\n\ntotalindex\x18\x04 \x01(\x05\x12\x0c\n\x04time\x18\x05 \x01(\x05\x12\n\n\x02\x46\x42\x18\x06 \x01(\x05\"}\n\x04Rank\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x11\n\tcontestID\x18\x02 \x01(\t\x12&\n\x07problem\x18\x03 \x03(\x0b\x32\x15.contest_rank.Problem\x12\x0f\n\x07penalty\x18\x04 \x01(\x05\x12\n\n\x02\x61\x63\x18\x05 \x01(\x05\x12\r\n\x05total\x18\x06 \x01(\x05\"F\n\x0f\x43ontestRankList\x12\x11\n\tcontestID\x18\x01 \x01(\t\x12 \n\x04rank\x18\x02 \x03(\x0b\x32\x12.contest_rank.Rank')




_SUBMIT = _descriptor.Descriptor(
  name='Submit',
  full_name='contest_rank.Submit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='contest_rank.Submit.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='contest_rank.Submit.date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runID', full_name='contest_rank.Submit.runID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=28,
  serialized_end=86,
)


_PROBLEM = _descriptor.Descriptor(
  name='Problem',
  full_name='contest_rank.Problem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='problemID', full_name='contest_rank.Problem.problemID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submit', full_name='contest_rank.Problem.submit', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acindex', full_name='contest_rank.Problem.acindex', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalindex', full_name='contest_rank.Problem.totalindex', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='contest_rank.Problem.time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FB', full_name='contest_rank.Problem.FB', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=89,
  serialized_end=218,
)


_RANK = _descriptor.Descriptor(
  name='Rank',
  full_name='contest_rank.Rank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='contest_rank.Rank.userID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contestID', full_name='contest_rank.Rank.contestID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='problem', full_name='contest_rank.Rank.problem', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='penalty', full_name='contest_rank.Rank.penalty', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ac', full_name='contest_rank.Rank.ac', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='contest_rank.Rank.total', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=220,
  serialized_end=345,
)


_CONTESTRANKLIST = _descriptor.Descriptor(
  name='ContestRankList',
  full_name='contest_rank.ContestRankList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contestID', full_name='contest_rank.ContestRankList.contestID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='contest_rank.ContestRankList.rank', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=347,
  serialized_end=417,
)

_PROBLEM.fields_by_name['submit'].message_type = _SUBMIT
_RANK.fields_by_name['problem'].message_type = _PROBLEM
_CONTESTRANKLIST.fields_by_name['rank'].message_type = _RANK
DESCRIPTOR.message_types_by_name['Submit'] = _SUBMIT
DESCRIPTOR.message_types_by_name['Problem'] = _PROBLEM
DESCRIPTOR.message_types_by_name['Rank'] = _RANK
DESCRIPTOR.message_types_by_name['ContestRankList'] = _CONTESTRANKLIST

class Submit(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBMIT

  # @@protoc_insertion_point(class_scope:contest_rank.Submit)

class Problem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROBLEM

  # @@protoc_insertion_point(class_scope:contest_rank.Problem)

class Rank(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANK

  # @@protoc_insertion_point(class_scope:contest_rank.Rank)

class ContestRankList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTESTRANKLIST

  # @@protoc_insertion_point(class_scope:contest_rank.ContestRankList)


# @@protoc_insertion_point(module_scope)