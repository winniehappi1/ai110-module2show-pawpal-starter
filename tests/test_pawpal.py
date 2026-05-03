from pawpal_system import Task, Pet


def test_add_task_to_pet():
    pet = Pet(name="Mochi", species="dog")

    task = Task(title="Walk", duration_minutes=20, priority="high")
    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Walk"


def test_task_validation():
    # valid task
    task = Task(title="Feed", duration_minutes=10, priority="medium")
    assert task.duration_minutes == 10

    # invalid duration
    try:
        Task(title="Bad Task", duration_minutes=0, priority="high")
        assert False
    except ValueError:
        assert True

    # invalid priority
    try:
        Task(title="Bad Task", duration_minutes=10, priority="urgent")
        assert False
    except ValueError:
        assert True