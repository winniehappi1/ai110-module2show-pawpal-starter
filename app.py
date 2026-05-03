import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app helps pet owners create a daily care schedule based on task priority and available time.
"""
)

st.divider()

st.subheader("Owner and Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=240,
    value=60
)

# Store owner in Streamlit session memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name)

st.session_state.owner.name = owner_name

st.markdown("### Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority
        }
    )
    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    owner = st.session_state.owner

    # Reset pet list so the same pet is not duplicated each time
    owner.pets = []

    pet = Pet(name=pet_name, species=species)
    owner.add_pet(pet)

    for t in st.session_state.tasks:
        task = Task(
            title=t["title"],
            duration_minutes=t["duration_minutes"],
            priority=t["priority"]
        )
        pet.add_task(task)

    scheduler = Scheduler(owner=owner, available_minutes=int(available_minutes))
    schedule = scheduler.generate_schedule()

    st.markdown("### Today's Schedule")

    if schedule:
        for task in schedule:
            st.write(f"- {task.get_info()}")
    else:
        st.warning("No tasks fit within the available time.")

    st.markdown("### Explanation")
    st.write(scheduler.explain_plan())