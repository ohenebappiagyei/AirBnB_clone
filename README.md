# AirBnB Clone Command Interpreter

This project implements a command-line interpreter for an AirBnB clone. The interpreter allows users to interact with and manage instances of different classes (e.g., BaseModel, User, State) through various commands.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone <repository-url>

2. **Navigate to the project directory:**
	```bash 
	cd AirBnB_clone

3. **Run the command interpreter:**
	``` ./console.py

4. ## Commands
	### create:
		create <class_name>

	### show:
		show <class_name> <instance_id>
	
	### destroy:
		destroy <class_name> <instance_id>

	### all:
		all [<class_name>]

	### count:
		count <class_name>

	### update
	update <class_name> <instance_id> <attribute_name> <attribute_value>

	### quit or EOF:
	quit

	./console.py

	(hbnb) create BaseModel
	<new_instance_id>
	(hbnb) show BaseModel <new_instance_id>
	<BaseModel instance representation>
	(hbnb) all
	<all instances representation>
	(hbnb) quit

