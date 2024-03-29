# address_json
Returns separated street and number in JSON fromat from an address string.
For this case I opted for not using APIs or modules and use regular expressions 
(which surely have limitations and don't cover many edge cases, but for the input we have and scope I figured it would be a good start and can be built on using libraries, or the google geocoding api).
Currently when executing the task sample addresses are used (which for example can be changed connecting to a DB and parsing the query results).

## Directory Layout
```
bin/
	get_street_and_number_docker.sh         --> Execution script to trigger the task from the container
    	test_street_and_number_docker.sh        --> Execution script to trigger the tests from the container

Dockerfile                      			--> The Dockerfile used to build the container (here for being pushed to AWS ECR)
get_street_and_number.py				--> Orchestrates the task returning address street and number using sample cases 
Pipfile                          			--> Package requirements for pipenv
README.md                        			--> This README
test_street_and_number.py				--> Tests the task returning address street and number using sample cases 
```

## Input and Output Data

Input: string of address

Output: string of street and string of street-number as JSON object

## Deployment

The master branch is used to build a container and is uploaded to AWS ECR by Github Actions (as an example, we could deploy the container to many other services). The AWS parameters would be defined as Secrets in the project (here I did not set up any secrets).


## Execution

Running the script `./bin/get_street_and_number.sh` (in the container `/app/bin/get_street_and_number_docker.sh`) will start the process.
