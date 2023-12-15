// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice

#ifndef IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_HPP_
#define IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__image_msg__msg__CameraImage __attribute__((deprecated))
#else
# define DEPRECATED__image_msg__msg__CameraImage __declspec(deprecated)
#endif

namespace image_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CameraImage_
{
  using Type = CameraImage_<ContainerAllocator>;

  explicit CameraImage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->width = 0ul;
      this->height = 0ul;
      this->channel = 0ul;
      this->fps = 0ul;
    }
  }

  explicit CameraImage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->width = 0ul;
      this->height = 0ul;
      this->channel = 0ul;
      this->fps = 0ul;
    }
  }

  // field types and members
  using _data_type =
    std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>>;
  _data_type data;
  using _width_type =
    uint32_t;
  _width_type width;
  using _height_type =
    uint32_t;
  _height_type height;
  using _channel_type =
    uint32_t;
  _channel_type channel;
  using _fps_type =
    uint32_t;
  _fps_type fps;

  // setters for named parameter idiom
  Type & set__data(
    const std::vector<uint8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint8_t>> & _arg)
  {
    this->data = _arg;
    return *this;
  }
  Type & set__width(
    const uint32_t & _arg)
  {
    this->width = _arg;
    return *this;
  }
  Type & set__height(
    const uint32_t & _arg)
  {
    this->height = _arg;
    return *this;
  }
  Type & set__channel(
    const uint32_t & _arg)
  {
    this->channel = _arg;
    return *this;
  }
  Type & set__fps(
    const uint32_t & _arg)
  {
    this->fps = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    image_msg::msg::CameraImage_<ContainerAllocator> *;
  using ConstRawPtr =
    const image_msg::msg::CameraImage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<image_msg::msg::CameraImage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<image_msg::msg::CameraImage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      image_msg::msg::CameraImage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<image_msg::msg::CameraImage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      image_msg::msg::CameraImage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<image_msg::msg::CameraImage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<image_msg::msg::CameraImage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<image_msg::msg::CameraImage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__image_msg__msg__CameraImage
    std::shared_ptr<image_msg::msg::CameraImage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__image_msg__msg__CameraImage
    std::shared_ptr<image_msg::msg::CameraImage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CameraImage_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    if (this->width != other.width) {
      return false;
    }
    if (this->height != other.height) {
      return false;
    }
    if (this->channel != other.channel) {
      return false;
    }
    if (this->fps != other.fps) {
      return false;
    }
    return true;
  }
  bool operator!=(const CameraImage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CameraImage_

// alias to use template instance with default allocator
using CameraImage =
  image_msg::msg::CameraImage_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace image_msg

#endif  // IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__STRUCT_HPP_
