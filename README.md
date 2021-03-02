# rosbag2-deserializer
A simple deserializer for rosbag2s. Used to debug complex rosbag2 api. 

## Build
`docker build . -t deserialize`

## Run
`docker run -v <absolue_path_to_input_bag>:/bag.db3 deserialize python3 /opt/deserialize.py`