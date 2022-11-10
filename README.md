# Prefect 

[Prefect](https://www.prefect.io/) is an interesting dataflow tool that takes the concept of split orchestration and agent runner all the way to its logical conclusion. They can be made completely seperate and the orchestrator needs to know very little about the agent runners. The agent runners connect to work queues and poll the server for work that is scheduled in the queue. The agent runners then execute the workflows / dataflows / programs locally and report back the progress to the orchestrator - but crucially don't send any of the results or any of the code. This allows Prefect to propose a cloud hosted Orchestrator as a very lightweight service for you to connect your agent runners to, without exposing any internal knowledge of your infrastructure, data, code or algorithms.

In playing around with it (see [commands.md](./commands.md) ), I was able to install, run flows and get the system operational within a few minutes.

It seems to be an extremely efficient implementation of a workflow orchestration tool.