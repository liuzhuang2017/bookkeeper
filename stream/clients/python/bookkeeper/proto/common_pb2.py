# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='bookkeeper.proto.common',
  syntax='proto3',
  serialized_options=_b('\n)org.apache.bookkeeper.stream.proto.commonP\001'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x17\x62ookkeeper.proto.common\"*\n\x08\x45ndpoint\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x42-\n)org.apache.bookkeeper.stream.proto.commonP\x01\x62\x06proto3')
)




_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='bookkeeper.proto.common.Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='bookkeeper.proto.common.Endpoint.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='bookkeeper.proto.common.Endpoint.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), dict(
  DESCRIPTOR = _ENDPOINT,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:bookkeeper.proto.common.Endpoint)
  ))
_sym_db.RegisterMessage(Endpoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)