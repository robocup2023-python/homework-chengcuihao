// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "image_msg/msg/detail/camera_image__rosidl_typesupport_introspection_c.h"
#include "image_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "image_msg/msg/detail/camera_image__functions.h"
#include "image_msg/msg/detail/camera_image__struct.h"


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  image_msg__msg__CameraImage__init(message_memory);
}

void image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_fini_function(void * message_memory)
{
  image_msg__msg__CameraImage__fini(message_memory);
}

size_t image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__size_function__CameraImage__data(
  const void * untyped_member)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return member->size;
}

const void * image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_const_function__CameraImage__data(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__uint8__Sequence * member =
    (const rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void * image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_function__CameraImage__data(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  return &member->data[index];
}

void image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__fetch_function__CameraImage__data(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const uint8_t * item =
    ((const uint8_t *)
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_const_function__CameraImage__data(untyped_member, index));
  uint8_t * value =
    (uint8_t *)(untyped_value);
  *value = *item;
}

void image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__assign_function__CameraImage__data(
  void * untyped_member, size_t index, const void * untyped_value)
{
  uint8_t * item =
    ((uint8_t *)
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_function__CameraImage__data(untyped_member, index));
  const uint8_t * value =
    (const uint8_t *)(untyped_value);
  *item = *value;
}

bool image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__resize_function__CameraImage__data(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__uint8__Sequence * member =
    (rosidl_runtime_c__uint8__Sequence *)(untyped_member);
  rosidl_runtime_c__uint8__Sequence__fini(member);
  return rosidl_runtime_c__uint8__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_member_array[5] = {
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(image_msg__msg__CameraImage, data),  // bytes offset in struct
    NULL,  // default value
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__size_function__CameraImage__data,  // size() function pointer
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_const_function__CameraImage__data,  // get_const(index) function pointer
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__get_function__CameraImage__data,  // get(index) function pointer
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__fetch_function__CameraImage__data,  // fetch(index, &value) function pointer
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__assign_function__CameraImage__data,  // assign(index, value) function pointer
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__resize_function__CameraImage__data  // resize(index) function pointer
  },
  {
    "width",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(image_msg__msg__CameraImage, width),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "height",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(image_msg__msg__CameraImage, height),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "channel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(image_msg__msg__CameraImage, channel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "fps",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(image_msg__msg__CameraImage, fps),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_members = {
  "image_msg__msg",  // message namespace
  "CameraImage",  // message name
  5,  // number of fields
  sizeof(image_msg__msg__CameraImage),
  image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_member_array,  // message members
  image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_init_function,  // function to initialize message memory (memory has to be allocated)
  image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_type_support_handle = {
  0,
  &image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_image_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, image_msg, msg, CameraImage)() {
  if (!image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_type_support_handle.typesupport_identifier) {
    image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &image_msg__msg__CameraImage__rosidl_typesupport_introspection_c__CameraImage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
