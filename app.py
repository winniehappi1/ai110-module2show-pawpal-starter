import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# 🎨 CUSTOM STYLING
st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafb;
    }

    h1 {
        color: #4CAF50;
    }

    h2, h3 {
        color: #2E7D32;
    }

    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #45a049;
    }

    .stTextInput input {
        border-radius: 8px;
    }

    .stNumberInput input {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🐾 HEADER
st.title("🐾 PawPal+")

st.info(
    "This app helps pet owners create a daily care schedule based on task priority and available time."
)

st.divider()

# 🟢 OWNER + PET
st.markdown("## 🟢 Owner and Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=240,
    value=60
)

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name)

st.session_state.owner.name = owner_name

# 🟡 TASKS
st.markdown("## 🟡 Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    task_time = st.text_input("Time", value="08:00")
with col5:
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("➕ Add task"):
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "time": task_time,
            "frequency": frequency
        }
    )
    st.success("Task added!")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# 🔵 SCHEDULE
st.markdown("## 🔵 Build Schedule")

if st.button("🚀 Generate schedule"):
    owner = st.session_state.owner
    owner.pets = []

    pet = Pet(name=pet_name, species=species)
    owner.add_pet(pet)

    for t in st.session_state.tasks:
        task = Task(
            title=t["title"],
            duration_minutes=t["duration_minutes"],
            priority=t["priority"],
            time=t["time"],
            frequency=t["frequency"]
        )
        pet.add_task(task)

    scheduler = Scheduler(owner=owner, available_minutes=int(available_minutes))
    schedule = scheduler.generate_schedule()

    # ⚠️ CONFLICTS
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        st.warning("⚠️ Schedule conflict detected:")
        for conflict in conflicts:
            st.warning(conflict)
    else:
        st.success("✅ No schedule conflicts detected.")

    # 📊 SORTED TASKS
    st.markdown("### 📊 Tasks Sorted by Time")
    st.table(
        [
            {
                "Time": task.time,
                "Task": task.title,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
                "Status": "Complete" if task.completed else "Incomplete",
                "Frequency": task.frequency
            }
            for task in scheduler.sort_by_time()
        ]
    )

    # 📅 TODAY SCHEDULE
    st.markdown("### 📅 Today's Schedule")

    if schedule:
        for task in schedule:
            st.success(task.get_info())
    else:
        st.error("No tasks fit within the available time.")

    # ⛔ UNSCHEDULED
    unscheduled = scheduler.get_unscheduled_tasks()
    if unscheduled:
        st.markdown("### ⛔ Unscheduled Tasks")
        st.warning("Some tasks did not fit within the available time:")
        for task in unscheduled:
            st.warning(task.get_info())

    # 💡 EXPLANATION
    st.markdown("### 💡 Explanation")
    st.info(scheduler.explain_plan())