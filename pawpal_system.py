from dataclasses import dataclass, field


VALID_PRIORITIES = ["low", "medium", "high"]


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def __post_init__(self):
        if self.duration_minutes <= 0:
            raise ValueError("Duration must be greater than 0 minutes.")
        if self.priority not in VALID_PRIORITIES:
            raise ValueError("Priority must be low, medium, or high.")

    def get_info(self):
        return f"{self.title} ({self.duration_minutes} min, {self.priority} priority)"


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise ValueError("Only Task objects can be added.")
        self.tasks.append(task)

    def view_tasks(self):
        return [task.get_info() for task in self.tasks]


@dataclass
class Owner:
    name: str
    preferences: str = ""
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        if not isinstance(pet, Pet):
            raise ValueError("Only Pet objects can be added.")
        self.pets.append(pet)

    def view_pets(self):
        return [f"{pet.name} ({pet.species})" for pet in self.pets]


@dataclass
class Scheduler:
    tasks: list[Task]
    available_minutes: int

    def sort_tasks(self):
        priority_order = {"high": 3, "medium": 2, "low": 1}
        return sorted(
            self.tasks,
            key=lambda task: priority_order[task.priority],
            reverse=True
        )

    def generate_schedule(self):
        schedule = []
        used_minutes = 0

        for task in self.sort_tasks():
            if used_minutes + task.duration_minutes <= self.available_minutes:
                schedule.append(task)
                used_minutes += task.duration_minutes

        return schedule

    def explain_plan(self):
        schedule = self.generate_schedule()
        total_minutes = sum(task.duration_minutes for task in schedule)

        if not schedule:
            return "No tasks could fit into the available time."

        task_names = ", ".join(task.title for task in schedule)
        return (
            f"The schedule includes {task_names}. "
            f"These tasks take {total_minutes} minutes total and were chosen based on priority "
            f"and the available time limit of {self.available_minutes} minutes."
        )