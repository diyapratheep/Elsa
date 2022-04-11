import logging


class Log:
    def __init__(self):
        logging.basicConfig(filename = 'Elsa.log', filemode = 'a', format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)

    def print(self, msg):
        print(" ".join(msg))

    def error(self, msg):
        msg = " ".join(msg) if len(msg) > 1 else msg
        logging.error(msg)
        self.print(msg)

    def info(self, *msg):
        msg = " ".join(msg) if len(msg) > 1 else msg
        logging.info(" ".join(msg))
        self.print(msg)


log = Log()
