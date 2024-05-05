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

def add_worker():
    name = input("Enter worker's name: ")
    availability = float(input("Enter worker's availability in hours per week: "))
    aspect = input("Enter the aspect of the animation pipeline: ")
    worker = Worker(name, availability, aspect)
    return worker

def add_project():
    name = input("Enter project name: ")
    start_date = input("Enter project start date (MM/DD/YYYY): ")
    end_date = input("Enter project end date (MM/DD/YYYY): ")
    start_date = datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.strptime(end_date, "%m/%d/%Y")
    project = Project(name, start_date, end_date)
    return project

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

def generate_schedule(workers, projects):
    pipeline_order = ['modeling', 'rigging', 'surfacing', 'layout', 'animation', 'cfx', 'matte painting', 'lighting', 'sound design']
    schedule_data = []

    for project in projects:
        scheduled_workers = {aspect: [] for aspect in pipeline_order}
        for aspect in pipeline_order:
            for worker in workers:
                if worker.aspect == aspect:
                    scheduled_workers[aspect].append(worker)

if __name__ == "__main__":
    main()