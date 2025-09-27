cmake_minimum_required(VERSION 3.8)
project(cpp_talk)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(cpp_pub src/cpp_pub.cpp)
ament_target_dependencies(cpp_pub rclcpp std_msgs)

add_executable(cpp_sub src/cpp_sub.cpp)
ament_target_dependencies(cpp_sub rclcpp std_msgs)

install(TARGETS cpp_pub cpp_sub DESTINATION lib/${PROJECT_NAME})

ament_package()
