from pawpal_system import Owner, Pet, Task, Scheduler


def setup_sample():
    owner = Owner(name="Test")
    dog = Pet(name="Buddy", species="dog")
    owner.add_pet(dog)

    t1 = Task("Task A", 20, "high", time="08:00")
    t2 = Task("Task B", 10, "medium", time="07:00")
    t3 = Task("Task C", 15, "low", time="09:00")

    dog.add_task(t1)
    dog.add_task(t2)
    dog.add_task(t3)

    scheduler = Scheduler(owner=owner, available_minutes=60)
    return scheduler, dog, t1, t2, t3


#  1. Sorting correctness
def test_sort_by_time():
    scheduler, _, t1, t2, t3 = setup_sample()
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].time == "07:00"
    assert sorted_tasks[1].time == "08:00"
    assert sorted_tasks[2].time == "09:00"


#  2. Recurring logic
def test_recurring_task_creation():
    scheduler, dog, t1, _, _ = setup_sample()

    t1.frequency = "daily"
    next_task = scheduler.complete_task(t1)

    assert next_task is not None
    assert next_task.frequency == "daily"
    assert next_task.completed is False


#  3. Conflict detection
def test_conflict_detection():
    owner = Owner(name="Test")
    dog = Pet(name="Buddy", species="dog")
    owner.add_pet(dog)

    t1 = Task("Task A", 20, "high", time="08:00")
    t2 = Task("Task B", 10, "medium", time="08:00")  # same time

    dog.add_task(t1)
    dog.add_task(t2)

    scheduler = Scheduler(owner=owner, available_minutes=60)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) > 0
    assert "Conflict" in conflicts[0]