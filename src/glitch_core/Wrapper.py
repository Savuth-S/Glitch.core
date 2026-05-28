import logging
import sys
import datetime
from logging import handlers


class Logger:
    self = None #Static globally shared between instances var

    @staticmethod
    def VCrashHandler(tpException, exception, traceback) -> None:
        Logger().fatal(f"Uncaught exception: {exception}", exc_info=(exception))

        hdlFile = logging.FileHandler(f"crashlog_{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.log")
        hdlFile.setFormatter(Logger().__m_fmtHandlers)

        Logger().__m_hdlMemBuffer.setTarget(hdlFile)
        Logger().__m_hdlMemBuffer.flush()
        hdlFile.close()

    def __new__(clsLogger) -> Logger:
        return clsLogger.self if clsLogger.self is not None else super().__new__(clsLogger)

    def __init__(self, enuLevel = logging.DEBUG):
        if self.self is not None:
            return
        Logger.self = self  #Fix for running multiple times constructor after singleton is made

        self.__m_lgr = logging.getLogger(__name__)
        self.__m_lgr.setLevel(enuLevel)

        self.__VSetUpHandlers()

        sys.excepthook = self.VCrashHandler

    def __VSetUpHandlers(self) -> None:
        self.__m_fmtHandlers = logging.Formatter("[%(levelname)s] (%(threadName)s|%(taskName)s)(%(thread)d)(%(relativeCreated)03d) [%(module)s][%(lineno)d] %(message)s")

        self.__m_hdlStdOut = logging.StreamHandler(sys.stdout)
        self.__m_hdlStdOut.setFormatter(self.__m_fmtHandlers)
        self.__m_lgr.addHandler(self.__m_hdlStdOut)

        self.__m_hdlMemBuffer = handlers.MemoryHandler(capacity=100, flushOnClose=False)
        self.__m_hdlMemBuffer.setFormatter(self.__m_fmtHandlers)
        self.__m_lgr.addHandler(self.__m_hdlMemBuffer)

    def VSetStdOutLevel(self, lvlLogger) -> None:
         self.__m_hdlStdOut.setLevel(lvlLogger)

    def debug(self, msg, *args, **kwargs):
         self.__m_lgr.debug(msg, *args, stacklevel=2, **kwargs)
    def info(self, msg, *args, **kwargs):
         self.__m_lgr.info(msg, *args, stacklevel=2, **kwargs)
    def warning(self, msg, *args, **kwargs):
         self.__m_lgr.warning(msg, *args, stacklevel=2, **kwargs)
    def error(self, msg, exc_info=True, *args, **kwargs):
         self.__m_lgr.error(msg, *args, exc_info=exc_info, **kwargs)
    def fatal(self, msg, *args, **kwargs):
         self.__m_lgr.critical(msg, *args, stacklevel=2, **kwargs)