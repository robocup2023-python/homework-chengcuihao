// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice

#ifndef IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_H_
#define IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/CameraImage in the package image_msg.
typedef struct image_msg__msg__CameraImage
{
  rosidl_runtime_c__uint8__Sequence data;
  uint32_t width;
  uint32_t height;
  uint32_t channel;
  uint32_t fps;
} image_msg__msg__CameraImage;

// Struct for a sequence of image_msg__msg__CameraImage.
typedef struct image_msg__msg__CameraImage__Sequence
{
  image_msg__msg__CameraImage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} image_msg__msg__CameraImage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_H_
