# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial UML design for PawPal+ included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class stores user information and manages pets. The Pet class represents each pet and keeps a list of its tasks. The Task class represents care activities like feeding or walking and includes attributes such as duration, priority, time, and frequency. The Scheduler class is responsible for organizing tasks into a daily plan based on available time and importance.

The goal of the system was to allow users to input their pet information, create tasks, and generate a clear daily schedule.

---

### b. Design changes

As I worked on the project and used Copilot, I made several improvements to my design.

I added:
- Type hints to make relationships clearer  
- Validation for task duration and priority  
- New attributes like time, frequency, and completion status  

I also added new methods for:
- Sorting tasks by priority and time  
- Filtering tasks by pet and status  
- Detecting scheduling conflicts  
- Handling recurring tasks  

At first, I wanted to keep the system simple, but I gradually added features once the base system was working correctly.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers:
- Available time (minutes)
- Task priority (high, medium, low)
- Task duration
- Completion status

Priority and duration are the most important. High-priority and shorter tasks are scheduled first to make sure the most important tasks are completed within the time limit.

---

### b. Tradeoffs

One tradeoff in my scheduler is conflict detection.

Right now, it only checks if two tasks have the exact same time (for example, both at 08:00). It does not detect overlapping tasks like one from 08:00–08:30 and another at 08:15.

I chose this approach because it is simple and easy to understand. A more advanced solution would require tracking start and end times, which would make the logic more complex.

---

## 3. AI Collaboration

### a. How I used AI

I used Copilot throughout the project for:
- Writing class methods  
- Debugging errors  
- Generating test cases  
- Improving scheduling logic  

The most helpful prompts were specific ones like:
- "Improve this sorting logic"
- "Add conflict detection to my scheduler"
- "Write simple pytest tests for this method"

---

### b. Judgment and verification

One example where I modified an AI suggestion was conflict detection.

Copilot suggested a more advanced approach using grouping and data structures, but I simplified it to a basic check for duplicate times. This made the code easier to read and better for my current level.

I verified AI suggestions by:
- Running the code  
- Writing tests with pytest  
- Checking if the output matched expected behavior  

---

## 4. Testing and Verification

### a. What I tested

I tested:
- Sorting by priority and time  
- Filtering tasks by pet and completion status  
- Recurring task creation  
- Conflict detection  
- Schedule generation within time limits  

These tests were important to make sure each feature worked correctly and handled basic edge cases.

---

### b. Confidence

I am very confident in my scheduler.

All tests passed successfully, and the system works correctly for normal use cases.

If I had more time, I would test:
- Overlapping time conflicts  
- Invalid time formats  
- Multiple pets with many tasks  

---

## 5. Reflection

### a. What went well

I am most satisfied with the scheduling logic and how everything connects together. The system can now sort, filter, detect conflicts, and handle recurring tasks.

---

### b. What I would improve

If I had more time, I would:
- Improve conflict detection to handle overlapping times  
- Add a better UI (like checkboxes to mark tasks complete)  
- Allow multiple pets in the Streamlit interface  

---

### c. Key takeaway

One important thing I learned is that AI is a tool, not a replacement for thinking.

Even though Copilot helped generate code, I still had to:
- Understand the logic  
- Decide what to keep or simplify  
- Test everything  

I learned how to act as the "lead architect" by guiding the AI and making final design decisions.