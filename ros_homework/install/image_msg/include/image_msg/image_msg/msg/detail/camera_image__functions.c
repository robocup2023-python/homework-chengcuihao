// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice
#include "image_msg/msg/detail/camera_image__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
image_msg__msg__CameraImage__init(image_msg__msg__CameraImage * msg)
{
  if (!msg) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__uint8__Sequence__init(&msg->data, 0)) {
    image_msg__msg__CameraImage__fini(msg);
    return false;
  }
  // width
  // height
  // channel
  // fps
  return true;
}

void
image_msg__msg__CameraImage__fini(image_msg__msg__CameraImage * msg)
{
  if (!msg) {
    return;
  }
  // data
  rosidl_runtime_c__uint8__Sequence__fini(&msg->data);
  // width
  // height
  // channel
  // fps
}

bool
image_msg__msg__CameraImage__are_equal(const image_msg__msg__CameraImage * lhs, const image_msg__msg__CameraImage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__uint8__Sequence__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  // width
  if (lhs->width != rhs->width) {
    return false;
  }
  // height
  if (lhs->height != rhs->height) {
    return false;
  }
  // channel
  if (lhs->channel != rhs->channel) {
    return false;
  }
  // fps
  if (lhs->fps != rhs->fps) {
    return false;
  }
  return true;
}

bool
image_msg__msg__CameraImage__copy(
  const image_msg__msg__CameraImage * input,
  image_msg__msg__CameraImage * output)
{
  if (!input || !output) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__uint8__Sequence__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  // width
  output->width = input->width;
  // height
  output->height = input->height;
  // channel
  output->channel = input->channel;
  // fps
  output->fps = input->fps;
  return true;
}

image_msg__msg__CameraImage *
image_msg__msg__CameraImage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  image_msg__msg__CameraImage * msg = (image_msg__msg__CameraImage *)allocator.allocate(sizeof(image_msg__msg__CameraImage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(image_msg__msg__CameraImage));
  bool success = image_msg__msg__CameraImage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
image_msg__msg__CameraImage__destroy(image_msg__msg__CameraImage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    image_msg__msg__CameraImage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
image_msg__msg__CameraImage__Sequence__init(image_msg__msg__CameraImage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  image_msg__msg__CameraImage * data = NULL;

  if (size) {
    data = (image_msg__msg__CameraImage *)allocator.zero_allocate(size, sizeof(image_msg__msg__CameraImage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = image_msg__msg__CameraImage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        image_msg__msg__CameraImage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
image_msg__msg__CameraImage__Sequence__fini(image_msg__msg__CameraImage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      image_msg__msg__CameraImage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

image_msg__msg__CameraImage__Sequence *
image_msg__msg__CameraImage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  image_msg__msg__CameraImage__Sequence * array = (image_msg__msg__CameraImage__Sequence *)allocator.allocate(sizeof(image_msg__msg__CameraImage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = image_msg__msg__CameraImage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
image_msg__msg__CameraImage__Sequence__destroy(image_msg__msg__CameraImage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    image_msg__msg__CameraImage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
image_msg__msg__CameraImage__Sequence__are_equal(const image_msg__msg__CameraImage__Sequence * lhs, const image_msg__msg__CameraImage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!image_msg__msg__CameraImage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
image_msg__msg__CameraImage__Sequence__copy(
  const image_msg__msg__CameraImage__Sequence * input,
  image_msg__msg__CameraImage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(image_msg__msg__CameraImage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    image_msg__msg__CameraImage * data =
      (image_msg__msg__CameraImage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!image_msg__msg__CameraImage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          image_msg__msg__CameraImage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!image_msg__msg__CameraImage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
