from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner(name="Jordan")

    # Create pets
    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Luna", species="cat")

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks
    task1 = Task(title="Morning walk", duration_minutes=20, priority="high")
    task2 = Task(title="Feed", duration_minutes=10, priority="medium")
    task3 = Task(title="Play time", duration_minutes=15, priority="low")

    # Assign tasks to pets
    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)

    # Create scheduler (it now gets tasks from owner automatically)
    scheduler = Scheduler(owner=owner, available_minutes=40)

    # Generate schedule
    schedule = scheduler.generate_schedule()

    # Print schedule
    print("\nToday's Schedule:")
    for task in schedule:
        print("-", task.get_info())

    # Print explanation
    print("\nExplanation:")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()