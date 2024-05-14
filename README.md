# Disk-Scheduling algorthms (Operating System)
This repository contains Python implementation of three disk scheduling algorithms: FCFS (First-Come, First-Served), SCAN, and C-SCAN.

### Algorithms Explanation
- FCFS: FCFS is the simplest disk scheduling algorithm. This algorithm accepts requests in disk queue order, as its name implies. Although the algorithm is fair and all requests are served consecutively, it is not the fastest.
- SCAN: In the SCAN disk scheduling algorithm, the head starts at one end of the disk and serves requests one by one until it reaches the other end. Then the head reverses direction and scans back and forth to access the disk. This technique is called the elevator algorithm because it acts like an elevator. Thus, middle requests are prioritized and those behind the disk arm must wait.
- C-SCAN: In SCAN algorithm, the disk arm reverses direction and scans the path again. Thus, too many requests may be queued at the other end or none at the scanned area. CSCAN method avoids these circumstances by having the disk arm go to the other end of the disk and serve requests there. C-SCAN is named because the disk arm moves circularly and this algorithm is comparable to SCAN.

### File Structure
- `generate.py`: generates a text file containing random cylinder requests.
- `cylinder_requests.txt`: text file that contains the generated random cylinder requests.
- `disk_scheduling.py`: contains the implementation of FCFS, SCAN, and C-SCAN algorithms along with their optimized versions.

### How to Run The Program
1. Generate cylinder requests by running the `generate.py` file to get a file named `cylinder_requests.txt` in the repository directory.
2. Run the `disk_scheduling.py` file to execute the three disk scheduling algorithms on the generated cylinder requests.

### Program Documentation
![Output](/Output.png)


