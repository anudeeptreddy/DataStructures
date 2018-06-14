# python2
import Queue


class JobQueue:
    def __init__(self):
        self.num_workers = 0
        self.m = 0
        self.jobs = []
        self.assigned_workers = []
        self.start_times = []

    def read_data(self):
        self.num_workers, m = map(int, raw_input().split())
        self.jobs = list(map(int, raw_input().split()))
        # self.num_workers, m = 2, 5
        # self.jobs = [1, 2, 3, 4, 5]
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print self.assigned_workers[i], self.start_times[i]

    def assign_jobs(self):
        # Optimal algorithm to assign jobs using priority queue provide below
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    class WorkerThread(object):

        def __init__(self, id):
            self.id = id
            self.nextFreeTime = 0

        def __cmp__(self, other):
            if self.nextFreeTime == other.nextFreeTime:
                return cmp(self.id, other.id)
            else:
                return cmp(self.nextFreeTime, other.nextFreeTime)

    def assign_jobs_queue(self):
        # Algorithm to assign jobs from a priority queue
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        queue = Queue.PriorityQueue()
        for i in range(self.num_workers):
            queue.put(self.WorkerThread(i))
        for i in range(len(self.jobs)):
            free_thread = queue.get()
            self.assigned_workers[i] = free_thread.id
            self.start_times[i] = free_thread.nextFreeTime
            free_thread.nextFreeTime += self.jobs[i]
            queue.put(free_thread);

    def solve(self):
        self.read_data()
        self.assign_jobs_queue()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

