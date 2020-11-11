class Logger(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance
    
    def write_logs(self, log_msg: str):
        with open('ITStepTutorials\\OOP\\heroes_game\\battles.log', 'a') as file:
            file.write(log_msg + '\n')
