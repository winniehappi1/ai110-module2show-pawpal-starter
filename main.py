from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(name="Jordan")

    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Luna", species="cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Evening walk", 30, "medium", time="18:00"))
    dog.add_task(Task("Morning walk", 20, "high", time="08:00", frequency="daily"))
    cat.add_task(Task("Feed Luna", 10, "high", time="07:30"))
    cat.add_task(Task("Play time", 15, "low", time="16:00"))

    scheduler = Scheduler(owner=owner, available_minutes=40)

    print("\nTasks Sorted by Time:")
    for task in scheduler.sort_by_time():
        print("-", task.get_info())

    print("\nIncomplete Tasks:")
    for task in scheduler.filter_tasks_by_status(False):
        print("-", task.get_info())

    print("\nTasks for Mochi:")
    for task in scheduler.filter_tasks_by_pet("Mochi"):
        print("-", task.get_info())

    print("\nToday's Schedule:")
    for task in scheduler.generate_schedule():
        print("-", task.get_info())

    print("\nCompleting recurring task:")
    next_task = scheduler.complete_task(dog.tasks[1])
    if next_task:
        print("Next occurrence created:", next_task.get_info())

    print("\nExplanation:")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()