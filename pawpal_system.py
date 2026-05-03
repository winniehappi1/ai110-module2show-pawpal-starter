from dataclasses import dataclass, field
from typing import List
from datetime import date, timedelta


VALID_PRIORITIES = ["low", "medium", "high"]
VALID_FREQUENCIES = ["once", "daily", "weekly"]


@dataclass
class Task:
    """Represents one pet care task."""

    title: str
    duration_minutes: int
    priority: str
    time: str = "09:00"
    completed: bool = False
    frequency: str = "once"
    due_date: date = field(default_factory=date.today)

    def __post_init__(self):
        """Validate task information after creation."""
        if self.duration_minutes <= 0:
            raise ValueError("Duration must be greater than 0 minutes.")
        if self.priority not in VALID_PRIORITIES:
            raise ValueError("Priority must be low, medium, or high.")
        if self.frequency not in VALID_FREQUENCIES:
            raise ValueError("Frequency must be once, daily, or weekly.")

    def get_info(self) -> str:
        """Return a formatted description of the task."""
        status = "complete" if self.completed else "incomplete"
        return (
            f"{self.time} - {self.title} "
            f"({self.duration_minutes} min, {self.priority} priority, "
            f"{status}, {self.frequency})"
        )

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def create_next_occurrence(self):
        """Create the next task if this task repeats."""
        if self.frequency == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            title=self.title,
            duration_minutes=self.duration_minutes,
            priority=self.priority,
            time=self.time,
            frequency=self.frequency,
            due_date=next_date
        )


@dataclass
class Pet:
    """Represents a pet and its care tasks."""

    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        if not isinstance(task, Task):
            raise ValueError("Only Task objects can be added.")
        self.tasks.append(task)

    def view_tasks(self) -> List[str]:
        """Return all task descriptions for this pet."""
        return [task.get_info() for task in self.tasks]


@dataclass
class Owner:
    """Represents an owner with one or more pets."""

    name: str
    preferences: str = ""
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner."""
        if not isinstance(pet, Pet):
            raise ValueError("Only Pet objects can be added.")
        self.pets.append(pet)

    def view_pets(self) -> List[str]:
        """Return all pets owned by the owner."""
        return [f"{pet.name} ({pet.species})" for pet in self.pets]


@dataclass
class Scheduler:
    """Creates a daily plan from an owner's pet tasks."""

    owner: Owner
    available_minutes: int
    tasks: List[Task] = field(init=False)

    def __post_init__(self):
        """Collect and sort tasks after the scheduler is created."""
        self.tasks = self._get_all_tasks()
        self.sort_tasks()

    def _get_all_tasks(self) -> List[Task]:
        """Get all tasks from all pets owned by the owner."""
        all_tasks = []
        for pet in self.owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def sort_tasks(self) -> None:
        """Sort tasks by priority and duration."""
        priority_order = {"high": 0, "medium": 1, "low": 2}
        self.tasks.sort(key=lambda t: (priority_order[t.priority], t.duration_minutes))

    def sort_by_time(self) -> List[Task]:
        """Return tasks sorted by time."""
        return sorted(self.tasks, key=lambda task: task.time)

    def filter_tasks_by_status(self, completed: bool) -> List[Task]:
        """Return tasks based on completion status."""
        return [task for task in self.tasks if task.completed == completed]

    def filter_tasks_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks for one pet."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                return pet.tasks
        return []

    def generate_schedule(self) -> List[Task]:
        """Generate a schedule based on priority, duration, and time limit."""
        schedule = []
        total_time = 0

        for task in self.tasks:
            if task.completed:
                continue

            if total_time + task.duration_minutes <= self.available_minutes:
                schedule.append(task)
                total_time += task.duration_minutes

        return schedule

    def get_unscheduled_tasks(self) -> List[Task]:
        """Return incomplete tasks that could not fit in the schedule."""
        schedule = self.generate_schedule()
        scheduled_titles = [task.title for task in schedule]

        return [
            task for task in self.tasks
            if not task.completed and task.title not in scheduled_titles
        ]

    def complete_task(self, task: Task):
        """Complete a task and create the next one if it repeats."""
        task.mark_complete()
        next_task = task.create_next_occurrence()

        if next_task:
            for pet in self.owner.pets:
                if task in pet.tasks:
                    pet.add_task(next_task)
                    self.tasks = self._get_all_tasks()
                    self.sort_tasks()
                    return next_task

        return None

    def explain_plan(self) -> str:
        """Explain why the schedule was created."""
        schedule = self.generate_schedule()
        total_time = sum(task.duration_minutes for task in schedule)

        if not schedule:
            return f"No tasks could be scheduled within your {self.available_minutes} minute limit."

        return (
            f"Selected {len(schedule)} task(s) totaling {total_time} minutes because they fit "
            f"within your {self.available_minutes} minute limit, prioritizing high-priority "
            f"and shorter tasks first."
        )
    from collections import defaultdict

    def detect_conflicts(self) -> List[str]:
        """Return warning messages for tasks scheduled at the same time."""
        # Step 1: Group tasks by their time
        time_groups = defaultdict(list)
        for task in self.tasks:
            time_groups[task.time].append(task)
        
        # Step 2: Check for conflicts (more than one task per time)
        conflicts = []
        for time, tasks_at_time in time_groups.items():
            if len(tasks_at_time) > 1:
                # List all conflicting task titles
                task_titles = [task.title for task in tasks_at_time]
                conflicts.append(
                    f"Conflict at {time}: Tasks {', '.join(task_titles)} are scheduled at the same time."
                )
        
        return conflicts