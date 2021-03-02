# Largely inspired by https://github.com/ros2/rosbag2/blob/master/rosbag2_py/test/test_sequential_reader.py,
# which is APACHE... licence as follows:
#
# Copyright 2020 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import os
from pathlib import Path
import sys

from rcl_interfaces.msg import Log
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message

import rosbag2_py

def get_rosbag_options(path, serialization_format='cdr'):
    storage_options = rosbag2_py.StorageOptions(uri=path, storage_id='sqlite3')

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format=serialization_format,
        output_serialization_format=serialization_format)

    return storage_options, converter_options

def main():
    # hardcoded bag path is bad, but ok since main reccomended running path is Dockerfile
    bag_path = "/bag.db3"
    storage_options, converter_options = get_rosbag_options(bag_path)
    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    topic_types = reader.get_all_topics_and_types()
    # Create a map for quicker lookup
    type_map = {topic_types[i].name: topic_types[i].type for i in range(len(topic_types))}

    msg_counter = 0
    while reader.has_next():
            print("\n-----------------")
            print("msg id {}".format(msg_counter))
            (topic, data, t) = reader.read_next()
            print(topic)
            msg_type = get_message(type_map[topic])
            msg = deserialize_message(data, msg_type)
            print(msg)
            msg_counter += 1

if __name__ == '__main__':
    main()
