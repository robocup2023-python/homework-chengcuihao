// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice

#ifndef IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__BUILDER_HPP_
#define IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "image_msg/msg/detail/camera_image__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace image_msg
{

namespace msg
{

namespace builder
{

class Init_CameraImage_fps
{
public:
  explicit Init_CameraImage_fps(::image_msg::msg::CameraImage & msg)
  : msg_(msg)
  {}
  ::image_msg::msg::CameraImage fps(::image_msg::msg::CameraImage::_fps_type arg)
  {
    msg_.fps = std::move(arg);
    return std::move(msg_);
  }

private:
  ::image_msg::msg::CameraImage msg_;
};

class Init_CameraImage_channel
{
public:
  explicit Init_CameraImage_channel(::image_msg::msg::CameraImage & msg)
  : msg_(msg)
  {}
  Init_CameraImage_fps channel(::image_msg::msg::CameraImage::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return Init_CameraImage_fps(msg_);
  }

private:
  ::image_msg::msg::CameraImage msg_;
};

class Init_CameraImage_height
{
public:
  explicit Init_CameraImage_height(::image_msg::msg::CameraImage & msg)
  : msg_(msg)
  {}
  Init_CameraImage_channel height(::image_msg::msg::CameraImage::_height_type arg)
  {
    msg_.height = std::move(arg);
    return Init_CameraImage_channel(msg_);
  }

private:
  ::image_msg::msg::CameraImage msg_;
};

class Init_CameraImage_width
{
public:
  explicit Init_CameraImage_width(::image_msg::msg::CameraImage & msg)
  : msg_(msg)
  {}
  Init_CameraImage_height width(::image_msg::msg::CameraImage::_width_type arg)
  {
    msg_.width = std::move(arg);
    return Init_CameraImage_height(msg_);
  }

private:
  ::image_msg::msg::CameraImage msg_;
};

class Init_CameraImage_data
{
public:
  Init_CameraImage_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CameraImage_width data(::image_msg::msg::CameraImage::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_CameraImage_width(msg_);
  }

private:
  ::image_msg::msg::CameraImage msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::image_msg::msg::CameraImage>()
{
  return image_msg::msg::builder::Init_CameraImage_data();
}

}  // namespace image_msg

#endif  // IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__BUILDER_HPP_
