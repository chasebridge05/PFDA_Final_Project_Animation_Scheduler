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