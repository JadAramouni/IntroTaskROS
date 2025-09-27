#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <chrono>
using namespace std::chrono_literals;

class CppPublisher : public rclcpp::Node {
public:
  CppPublisher() : Node("cpp_publisher"), count_(0) {
    pub_ = create_publisher<std_msgs::msg::String>("chatter", 10);
    timer_ = create_wall_timer(500ms, [this]{
      std_msgs::msg::String msg;
      msg.data = "Hello from ROS2 (C++)! #" + std::to_string(count_++);
      RCLCPP_INFO(get_logger(), "Published: '%s'", msg.data.c_str());
      pub_->publish(msg);
    });
  }
private:
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
  rclcpp::TimerBase::SharedPtr timer_;
  int count_;
};

int main(int argc, char** argv){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CppPublisher>());
  rclcpp::shutdown();
  return 0;
}
