def create_project_plan(name, problem, users):
    return f"""
PROJECT: {name}

PROBLEM
{problem}

TARGET USERS
{users}

MVP PLAN
1. Define the core user problem
2. Build one working end-to-end scenario
3. Create a simple interface
4. Test the main workflow
5. Prepare a demo and README

GOAL
Create a working prototype that demonstrates the main value of the idea.
"""


def main():
    print("=== Hackathon Project Planner ===\n")

    name = input("Project name: ")
    problem = input("What problem does it solve? ")
    users = input("Who are the target users? ")

    plan = create_project_plan(name, problem, users)

    print("\n" + plan)


if __name__ == "__main__":
    main()
