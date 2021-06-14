# WorkGenius Web Developer test exercise

### Context
We have a web-application where our admins can see/review/manage users.

### Challenge
Our customer-success department are missing functionality to group users based on their skills.

### User story
- As CS-manager, I want to **attach skills to users**, so I can easily **filter list of users by skill**.

### Acceptance criteria (happy flow)
1. I choose user
2. I attach skill "javascript" to the user
3. I filter list of users by skill "javascript"
4. I see result 1 row with user from 2nd step


## Setup & run project
### Backend
> Assumption is that you working under ubuntu and have set up python3.8 
```shell
cd backend

# Install virtual environment
python3.8 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
flask run --reload
```
