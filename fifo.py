
class Process:
    def __init__(self):
        self.arrivalTime = 0
        self.burstTime = 0
        self.startTime = 0
        self.endTime = 0
        self.waitTime = 0
        self.turnaroundTime = 0
        self.id = 0


def calculateTimes(processes, numProcesses):
    # Bubble sort processes based on arrival times
    for i in range(numProcesses - 1):
        for j in range(numProcesses - i - 1):
            if processes[j].arrivalTime > processes[j + 1].arrivalTime:
                processes[j], processes[j + 1] = processes[j + 1], processes[j]

    currentTime = 0

    for i in range(numProcesses):
        if currentTime < processes[i].arrivalTime:
            currentTime = processes[i].arrivalTime

        processes[i].startTime = currentTime
        currentTime = currentTime + processes[i].burstTime
        processes[i].endTime = currentTime

        processes[i].turnaroundTime = processes[i].endTime - processes[i].arrivalTime
        processes[i].waitTime = processes[i].startTime - processes[i].arrivalTime


if __name__ == '__main__':
    numProcesses = int(input("Enter the number of processes: "))

    processes = [Process() for _ in range(numProcesses)]
    totalTurnaroundTime = 0
    totalWaitTime = 0

    for i in range(numProcesses):
        processes[i].arrivalTime = int(input("\nEnter the arrival time for process {}: ".format(i + 1)))
        processes[i].burstTime = int(input("Enter the burst time for process {}: ".format(i + 1)))
        processes[i].id = i + 1

    calculateTimes(processes, numProcesses)

    print("\nProcess\tStart Time\tEnd Time\tTurnaround Time\tWaiting Time")
    for i in range(numProcesses):
        print("{}\t{}\t\t{}\t\t{}\t\t\t{}".format(processes[i].id, processes[i].startTime, processes[i].endTime,
                                                processes[i].turnaroundTime, processes[i].waitTime))
        totalTurnaroundTime = totalTurnaroundTime + processes[i].turnaroundTime
        totalWaitTime = totalWaitTime + processes[i].waitTime

    averageTurnaroundTime = totalTurnaroundTime / numProcesses
    averageWaitTime = totalWaitTime / numProcesses
    print("\nAverage Turnaround Time: {:.2f}".format(averageTurnaroundTime))
    print("Average Waiting Time: {:.2f}".format(averageWaitTime))