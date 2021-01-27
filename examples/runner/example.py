from softnanotools.runner import Runner

class Job(Runner):

    def __init__(self, x):
        self.x = x
        super().__init__()

    @property
    def tasks(self):
        return super().__tasks__
        
    @Runner.task(0)
    def step_1(self):
        print(f'Since x={self.x}, running {self.x} times:')
        for i in range(self.x):
            print(f'Hello - {i}!')
        return self.x

    @Runner.task(1)
    def step_2(self):
        print('Finished')
        return "Step 2"

class JobSquared(Job):

    def __init__(self, x):
        super().__init__(x**2)

if __name__ == '__main__':
    job = Job(2)
    job2 = JobSquared(3)
    job2.execute()
    print('Done 1')
    job.execute()
    job.execute(skip=1)