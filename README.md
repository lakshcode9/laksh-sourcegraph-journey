# laksh-sourcegraph-journey
Logging my full grind to break into security engineering. From noob to Sourcegraph. One push at a time 💻🔐
---

## Day 1: Ground Zero

### Tasks Completed:
- Installed Python, Git, VS Code
- Set up SSH and GitHub repo (`laksh-sourcegraph-journey`)
- Wrote and ran first script: `hello_security.py`
- Practiced variables, control flow, and functions
- Committed and pushed all code to GitHub

### What I Learned:
- How to configure a working Python dev environment ( well i already knew but documenting is fun)
- Git basics: add, commit, push, directory navigation
- Python fundamentals and habits (indentation, no semicolons, f-strings)

### Challenges:
- Forgot to save README changes before commit
- Accidentally exited the working directory once
- Realized pasting code ≠ learning it (switched to manual writing)

### How I Fixed Things:
- Took time to slow down and understand the commands
- Rewrote missing commits properly
- Focused on understanding over copying

### Mindset Note:
Security is deep tech — but I am all here for it!!
---
I actually took more time to surf the security space and realized the basics are pretty much the same, so I will  be amping up my approach from tomorrow. EXCITED.
---

##  Day 1 Extended – Network Recon Script

**File:** `day1/day1-extended/port_and_os_scanner.py`

### What This Tool Does:
- Scans a subnet with ARP and asks: “Who’s out there?”
- For each live host, tries every port from 1 to 1024
- Then sends an ICMP ping to guess OS based on TTL (Windows ~128, Linux ~64)

In short: it sniffs, knocks, and guesses.

---

### 💡 What I Actually Learned Doing This:
- How ARP actually finds devices 
- What TTL means, and how OSes expose themselves through it
- Sockets in Python are sneaky simple — open, knock, close, move on
- Git doesn’t care about your feelings (especially when you forget to `git add`)

---

###  Real-World Pain We Solved:
-  Installed Npcap just to make Scapy stop crying
-  Fixed subnet from `192.168.1.0/24` to `192.168.56.0/24` after wondering why no one was “home”
-  Tracked down missing files we never pushed
-  Learned `cd ..` (yet again (sigh))

---

### 🧘 Final Reflection:
Was this “just a scanner”? Nope.

This was my first time writing code that touched the **real network**.  
The moment when “I built this and it worked” collided with “wait, I can see what devices are doing.”  
Feels like the first tool that matters.
I feel good.

