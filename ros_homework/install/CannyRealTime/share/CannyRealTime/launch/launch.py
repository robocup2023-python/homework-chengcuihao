from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    LD = LaunchDescription()
    camera = Node(
        package='CannyRealTime',
        executable='camera',
        name='camera'
    )
    LD.add_action(camera)

    fsm = Node(
        package='CannyRealTime',
        executable='fsm',
        name='fsm'
    )
    LD.add_action(fsm)
    return LD