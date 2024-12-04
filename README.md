# DevuAI assessment
This code is just for demonstration purpose.

## Key tasks:
Please see the problem statement below and submit by EOD Thursday (Dec 5). 
Provide time availability (week of December 9) to review your code with the team.
The problem statement
1. We have a stack running apache-airflow to manage, schedule and run jobs. Airflow has an interface as well as an api to manage these jobs. Each job is represented by a direct acyclic graph (DAG). The goal is to implement an interface to create DAGs. In your implementation, mock the create DAG endpoint and use it to implement the interface. [Here's the link to the documentation] (https://airflow.apache.org/docs/apache-airflow/1.10.14/rest-api-ref.html#post--api-experimental-dags--DAG_ID--dag_runs)

2. Share your implementation in a github repository with a clear instructions to run your code.

3. Use either python or java as your programming language.

4. The goal of this exercise is to demonstrate the ability to understand business requirements and software documentation and create clear documentation. Keep your implementation as simple and clear as possible.


## Implementation Requirement
1. Python 3.7+
2. Uvicorn (for running the API)
3. FastAPI
4. Pytest

## Installation
- Run `pip install -r requirements.txt`

## Exexution
- Run `uvicorn app.main:app --reload`
- If you get "uvicorn not install" run `sudo apt install uvicorn` on linux terminal and try again

## Run Test Cases
- Run `pytest tests/`
