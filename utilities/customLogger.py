import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\patilraj\Desktop\Framework\nopCommerceProject\Logs\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger