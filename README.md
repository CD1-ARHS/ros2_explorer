# ROS 2 Turtlebot 3 Map Explorer
## Description
In this package we use Turtlebot 3 to explore an unknown csv environment generated from an image, navigate through it and create a map.

>**Wanderer Exploration** explores the map doing random turns when it detects an obstacle. It's a convenient way to explore small maps but time consuming for bigger ones.
  
>**Discoverer Exploration** prioritizes specific unknown hotspots of the map convoluting the occupancy grid. It's a better way to explore bigger maps in exchange of a higher computational cost.

Include the following lines in ~/.bashrc:
```
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=~/sim_ws/src/ros2_explorer/explorer_gazebo/models
```
## Setup Instructions

### 1. Prepare Floorplan Image

Place your floorplan image (e.g., `ahsr.png`) in the following directory:

```
sim_ws/src/ros2_explorer/explorer_gazebo
```

### 2. Convert Floorplan to CSV

Run the `floorplan2csv.py` script to convert the floorplan image to a CSV file. Ensure the script is located in the same directory as your floorplan image:

```bash
python3 floorplan2csv.py
```

### 3. Move CSV File

After conversion, move the generated CSV file into the `maps` folder:

```
sim_ws/src/ros2_explorer/explorer_gazebo/maps
```

### 4. Generate Gazebo World

Navigate to the `explorer_gazebo` directory and run the script to generate the Gazebo world:

```bash
cd ~/sim_ws/src/ros2_explorer/explorer_gazebo/
python3 gazebo-map-from-csv.py
```

### 5. Run Gazebo Simulation

Launch the Gazebo environment with the generated map:

```bash
ros2 launch explorer_bringup explorer.launch.py map_name:=ahsr
```

### 6. Start Mapping

Run the mapper to begin mapping the environment:

```bash
ros2 run explorer_bringup manager
```
Maps will be converted to Gazebo format in `/explorer_gazebo/models` folder. Create a new .world.xml file in `/explorer_gazebo/worlds` and modify the name of the map you want to use:
```
<include>
  <uri>model://map1</uri>
</include>
```
## Package structure
![image](https://github.com/DaniGarciaLopez/ros2_explorer/blob/main/explorer_bringup/data/explorer_graph.png)
![image](https://github.com/DaniGarciaLopez/ros2_explorer/blob/main/explorer_bringup/data/rosgraph.png)
