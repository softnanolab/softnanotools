from softnanotools.runner import Runner

def test_Runner():

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

    job = Job(5)
    job.execute()
    job.execute(skip=1)
    return