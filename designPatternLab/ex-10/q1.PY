from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def read(self, context):
        pass

    @abstractmethod
    def write(self, context):
        pass

class ReadingState(State):
    def read(self, context):
        context.reader_count += 1
        print(f"Reader {context.reader_count} is reading.")
    
    def write(self, context):
        print("Writers must wait, currently readers are reading.")

class WritingState(State):
    def read(self, context):
        print("Readers must wait, a writer is writing.")

    def write(self, context):
        print("A writer is already writing.")

class IdleState(State):
    def read(self, context):
        context.set_state(ReadingState())
        context.reader_count += 1
        print(f"Reader {context.reader_count} started reading.")

    def write(self, context):
        context.set_state(WritingState())
        print("Writer started writing.")

class ReaderWriterContext:
    def __init__(self):
        self.state = IdleState()
        self.reader_count = 0

    def set_state(self, state: State):
        self.state = state

    def read(self):
        self.state.read(self)

    def write(self):
        self.state.write(self)

    def finish_reading(self):
        if self.reader_count > 0:
            self.reader_count -= 1
        if self.reader_count == 0:
            self.set_state(IdleState())
            print("All readers finished. Back to idle state.")

    def finish_writing(self):
        self.set_state(IdleState())
        print("Writer finished. Back to idle state.")

context = ReaderWriterContext()

context.read()
context.read()
context.write()
context.finish_reading()
context.finish_reading()
context.write()
context.finish_writing()
context.read()
