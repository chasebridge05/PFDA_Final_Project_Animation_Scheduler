import pandas as pd
from datetime import datetime, timedelta

class Worker:
    def __init__(self, name, availability, aspect):
        self.name = name
        self.availability = availability
        self.aspect = aspect

class Project:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

def main():
    workers = []
    projects = []

    while True:
        print("\n1. Add worker\n2. Add project\n3. Schedule\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            worker = add_worker()
            workers.append(worker)
        elif choice == '2':
            project = add_project()
            projects.append(project)
        elif choice == '3':
            if not workers:
                print("Please add workers first!")
                continue
            if not projects:
                print("Please add projects first!")
                continue
            generate_schedule(workers, projects)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()