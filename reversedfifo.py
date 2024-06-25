    print("Average Waiting Time: {:.2f}".format(averageWaitTime))    print("\nAverage Turnaround Time: {:.2f}".format(averageTurnaroundTime))
    averageWaitTime = totalWaitTime / numProcesses
    averageTurnaroundTime = totalTurnaroundTime / numProcesses

        totalWaitTime = totalWaitTime + processes[i].waitTime
        totalTurnaroundTime = totalTurnaroundTime + processes[i].turnaroundTime
                                                processes[i].turnaroundTime, processes[i].waitTime))
        print("{}\t{}\t\t{}\t\t{}\t\t\t{}".format(processes[i].id, processes[i].startTime, processes[i].endTime,
    for i in range(numProcesses):
    print("\nProcess\tStart Time\tEnd Time\tTurnaround Time\tWaiting Time")

    calculateTimes(processes, numProcesses)

        processes[i].id = i + 1
        processes[i].burstTime = int(input("Enter the burst time for process {}: ".format(i + 1)))
        processes[i].arrivalTime = int(input("\nEnter the arrival time for process {}: ".format(i + 1)))
    for i in range(numProcesses):

    totalWaitTime = 0
    totalTurnaroundTime = 0
    processes = [Process() for _ in range(numProcesses)]

    numProcesses = int(input("Enter the number of processes: "))
if __name__ == '__main__':


        processes[i].waitTime = processes[i].startTime - processes[i].arrivalTime
        processes[i].turnaroundTime = processes[i].endTime - processes[i].arrivalTime

        processes[i].endTime = currentTime
        currentTime = currentTime + processes[i].burstTime
        processes[i].startTime = currentTime

            currentTime = processes[i].arrivalTime
        if currentTime < processes[i].arrivalTime:
    for i in range(numProcesses):

    currentTime = 0

                processes[j], processes[j + 1] = processes[j + 1], processes[j]
            if processes[j].arrivalTime > processes[j + 1].arrivalTime:
        for j in range(numProcesses - i - 1):
    for i in range(numProcesses - 1):
    # Bubble sort processes based on arrival times
def calculateTimes(processes, numProcesses):


        self.id = 0
        self.turnaroundTime = 0
        self.waitTime = 0
        self.endTime = 0
        self.startTime = 0
        self.burstTime = 0
        self.arrivalTime = 0
    def __init__(self):
class Process:

