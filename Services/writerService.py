from Models.writer import Writer

class WriterService:
    def create_writer(self,writer):
        return Writer(writer)
    
    def delete_writer(self):
        pass