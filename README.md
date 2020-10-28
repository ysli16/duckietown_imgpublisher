## Execution
### Build docker image
Run command

`dts devel build -f -H <robot_name>.local`

Replace `<robot_name>` with name of your duckiebot.

### Run container
Run command

`dts devel run -H <robot_name>.local -- --privileged`

Replace `<robot_name>` with name of your duckiebot.
