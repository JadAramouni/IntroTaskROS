#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class CppSubscriber : public rclcpp::Node {
public:
  CppSubscriber() : Node("cpp_subscriber") {
    sub_ = create_subscription<std_msgs::msg::String>(
      "chatter", 10,
      [this](const std_msgs::msg::String & msg){
        RCLCPP_INFO(get_logger(), "Received: '%s'", msg.data.c_str());
      });
  }
private:
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
};

int main(int argc, char** argv){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CppSubscriber>());
  rclcpp::shutdown();
  return 0;
}
