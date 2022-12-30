import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_descriptions():

    detector = launch_ros.actions.Node(
      package='mypkg',
      executable='detector',
    )
    return launch.LaunchDescription([detector])
