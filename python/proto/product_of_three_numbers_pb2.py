# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product_of_three_numbers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='product_of_three_numbers.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'Z\014golang/proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eproduct_of_three_numbers.proto\x12\x05proto\"\x18\n\x07Request\x12\r\n\x05\x61rray\x18\x01 \x01(\t\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32I\n\x17\x43\x61lculateMultiplication\x12.\n\tCalculate\x12\x0e.proto.Request\x1a\x0f.proto.Response\"\x00\x42\x0eZ\x0cgolang/protob\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='proto.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='array', full_name='proto.Request.array', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=65,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='proto.Response.result', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=67,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'product_of_three_numbers_pb2'
  # @@protoc_insertion_point(class_scope:proto.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'product_of_three_numbers_pb2'
  # @@protoc_insertion_point(class_scope:proto.Response)
  })
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None

_CALCULATEMULTIPLICATION = _descriptor.ServiceDescriptor(
  name='CalculateMultiplication',
  full_name='proto.CalculateMultiplication',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=168,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calculate',
    full_name='proto.CalculateMultiplication.Calculate',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATEMULTIPLICATION)

DESCRIPTOR.services_by_name['CalculateMultiplication'] = _CALCULATEMULTIPLICATION

# @@protoc_insertion_point(module_scope)
