## Install prefect 
```
sudo apt-get update
sudo apt-get install python3.11
sudo apt-get install python3-pip
sudo apt-get install sqlite3
pip install -U prefect

# make sure the PATH contains the PATH to prefect binaries
PATH=/home/eric/.local/bin:$PATH

prefect config view --show-defaults

prefect config set PREFECT_API_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```


Run the server 

```
prefect orion start
``` 

Run a worker 
```
prefect agent start -q dev-queue1
```

Create the deployment for the python task 
```
prefect deployment build ./first-deployed-flow.py:log_flow -n first-simple-log -q dev-queue1
```

Configure the yaml file that is generated for the deployment, then deploy the flow. 

```bash
prefect deployment apply log_flow-deployment.yaml
```
