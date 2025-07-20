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