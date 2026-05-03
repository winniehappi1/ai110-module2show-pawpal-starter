from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def get_info(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass

    def view_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    preferences: str = ""
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def view_pets(self):
        pass


@dataclass
class Scheduler:
    tasks: list
    available_minutes: int

    def sort_tasks(self):
        pass

    def generate_schedule(self):
        pass

    def explain_plan(self):
        pass