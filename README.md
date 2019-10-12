Run Tests in Pycharm using docker compose interpreter
=====================================================

After opening the project in Pycharm create a new DockerCompose Interpreter:

`File > Settings > Project > Project Interpreter`

From the interpreter drop down select `show all` and then click on `+`. 

If docker is correctly installed the server option in the new window will be automatically fill. 
Select `docker-compose.yml` as `Configuration file` and `python env` as service

From the root of the project right-click `hello_world.py` and run the app that will produce an output as:
```bash
Recreating test_python_in_doker_python_env_1 ... 
Attaching to test_python_in_doker_python_env_1
python_env_1  | Hello world Sarah Williams
test_python_in_doker_python_env_1 exited with code 0
Aborting on container exit...

Process finished with exit code 0
```

Open `test_hello_world.py` and put a breakpoint in one off the functions and then run the tests. Pycharm will
automatically stop at the correct position.