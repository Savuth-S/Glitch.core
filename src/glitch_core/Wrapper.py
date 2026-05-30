import sys
import tkinter
import logging
import datetime
from logging import handlers


class Logger:
    self = None #Static globally shared between instances var

    @staticmethod
    def VCrashHandler(xtpCrash, xCrash, tbCrash) -> None:
        if xtpCrash is KeyboardInterrupt:
            return

        lgr = Logger() 
        lgr.fatal(f"Uncaught exception: {xCrash}", exc_info=(xtpCrash, xCrash, tbCrash))

        lgCrashDump = None
        try:
            lgCrashDump = logging.FileHandler(f"crashlog_{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log")
            lgCrashDump.setFormatter(lgr.__m_fmtLog)

            lgr.__m_bufLogHistory.setTarget(lgCrashDump)
            lgr.__m_bufLogHistory.flush()
        finally:
            if lgCrashDump is not None:
                lgCrashDump.close()

    def __new__(clsSelf) -> Logger:
        return clsSelf.self if clsSelf.self is not None else super().__new__(clsSelf)

    def __init__(self, lvlLog = logging.DEBUG) -> None:
        if type(self).self is not None:
            return
        type(self).self = self  # Fix for running multiple times constructor after singleton is made

        self.__m_lgr = logging.getLogger(__name__)
        self.__m_lgr.setLevel(lvlLog)

        self.__m_fmtLog = logging.Formatter("[%(levelname)s] (%(threadName)s|%(taskName)s)(%(thread)d)(%(relativeCreated)03d) [%(module)s][%(lineno)d] %(message)s")
        if not self.__m_lgr.handlers:
            self.__VSetUpHandlers()

        # Logger is ready for crash handling, must be after initialization
        sys.excepthook = self.VCrashHandler
        tkinter.Tk.report_callback_exception = self.VCrashHandler

    def __VSetUpHandlers(self) -> None:
        self.__m_stLogOutput = logging.StreamHandler(sys.stdout)
        self.__m_stLogOutput.setFormatter(self.__m_fmtLog)
        self.__m_lgr.addHandler(self.__m_stLogOutput)

        self.__m_bufLogHistory = handlers.MemoryHandler(capacity=10,
                                                       flushLevel=logging.CRITICAL+1,
                                                       flushOnClose=False)
        self.__m_bufLogHistory.setFormatter(self.__m_fmtLog)
        self.__m_lgr.addHandler(self.__m_bufLogHistory)

    def VSetLoggerLevel(self, lvlLog) -> None:
         self.__m_lgr.setLevel(lvlLog)

    def VSetStdOutLevel(self, lvlLog) -> None:
         self.__m_stLogOutput.setLevel(lvlLog)

    def debug(self, msg, *args, **kwargs) -> None:
         self.__m_lgr.debug(msg, *args, stacklevel=2, **kwargs)
    def info(self, msg, *args, **kwargs) -> None:
         self.__m_lgr.info(msg, *args, stacklevel=2, **kwargs)
    def warning(self, msg, *args, **kwargs) -> None:
         self.__m_lgr.warning(msg, *args, stacklevel=2, **kwargs)
    def error(self, msg, exc_info=True, *args, **kwargs) -> None:
         self.__m_lgr.error(msg, *args, exc_info=exc_info, stacklevel=2, **kwargs)
    def fatal(self, msg, exc_info=True, *args, **kwargs) -> None:
         self.__m_lgr.critical(msg, *args, exc_info=exc_info, stacklevel=2, **kwargs)