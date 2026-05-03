# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design for PawPal+ included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class holds basic user information and manages one or more pets. The Pet class represents each pet and keeps a list of its tasks. The Task class represents individual care activities such as feeding, walking, or giving medication, and includes details like duration and priority. The Scheduler class is responsible for organizing tasks into a daily plan based on constraints such as available time and task importance.

Overall, the system is designed to allow users to enter their information, manage pet care tasks, and generate a clear and organized daily schedule.

**b. Design changes**

After asking Copilot to review my class skeleton, I decided to make a few small changes to improve the design. I added type hints so the relationships between Owner, Pet, Task, and Scheduler are clearer. I also decided to add simple validation for task priority and duration so the program can prevent invalid tasks, such as a task with zero minutes or an unsupported priority.

I did not add extra features like recurring tasks, breed, age, or time-of-day scheduling yet because I wanted to keep the first version simple and focused on the main project requirements. These features could be added later if the app is expanded.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff in my scheduler is that the conflict detection only checks for exact time matches. For example, if two tasks are both scheduled at 08:00, the system gives a warning. However, it does not yet detect overlapping durations, such as one task from 08:00–08:30 and another starting at 08:15.

I decided to keep this version because it is simple, readable, and easy to test. A more advanced version could compare start and end times, but that would make the logic more complex. For this project, exact-time conflict detection is enough to show the basic algorithm clearly.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
