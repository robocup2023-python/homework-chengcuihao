// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from image_msg:msg/CameraImage.idl
// generated code does not contain a copyright notice

#ifndef IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__TRAITS_HPP_
#define IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "image_msg/msg/detail/camera_image__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace image_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const CameraImage & msg,
  std::ostream & out)
{
  out << "{";
  // member: data
  {
    if (msg.data.size() == 0) {
      out << "data: []";
    } else {
      out << "data: [";
      size_t pending_items = msg.data.size();
      for (auto item : msg.data) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: width
  {
    out << "width: ";
    rosidl_generator_traits::value_to_yaml(msg.width, out);
    out << ", ";
  }

  // member: height
  {
    out << "height: ";
    rosidl_generator_traits::value_to_yaml(msg.height, out);
    out << ", ";
  }

  // member: channel
  {
    out << "channel: ";
    rosidl_generator_traits::value_to_yaml(msg.channel, out);
    out << ", ";
  }

  // member: fps
  {
    out << "fps: ";
    rosidl_generator_traits::value_to_yaml(msg.fps, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CameraImage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data.size() == 0) {
      out << "data: []\n";
    } else {
      out << "data:\n";
      for (auto item : msg.data) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: width
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "width: ";
    rosidl_generator_traits::value_to_yaml(msg.width, out);
    out << "\n";
  }

  // member: height
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "height: ";
    rosidl_generator_traits::value_to_yaml(msg.height, out);
    out << "\n";
  }

  // member: channel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "channel: ";
    rosidl_generator_traits::value_to_yaml(msg.channel, out);
    out << "\n";
  }

  // member: fps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fps: ";
    rosidl_generator_traits::value_to_yaml(msg.fps, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CameraImage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace image_msg

namespace rosidl_generator_traits
{

[[deprecated("use image_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const image_msg::msg::CameraImage & msg,
  std::ostream & out, size_t indentation = 0)
{
  image_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use image_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const image_msg::msg::CameraImage & msg)
{
  return image_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<image_msg::msg::CameraImage>()
{
  return "image_msg::msg::CameraImage";
}

template<>
inline const char * name<image_msg::msg::CameraImage>()
{
  return "image_msg/msg/CameraImage";
}

template<>
struct has_fixed_size<image_msg::msg::CameraImage>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<image_msg::msg::CameraImage>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<image_msg::msg::CameraImage>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMAGE_MSG__MSG__DETAIL__CAMERA_IMAGE__TRAITS_HPP_
