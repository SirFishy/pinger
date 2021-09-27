from processor import ProcessorType, PingProcessor
from processors.multiprocess import MultiProcessPingProcessor
from processors.multithread import MultiThreadPingProcessor


class ProcessorFactory:

    @staticmethod
    def get_processor(processor_type: ProcessorType, pool_size: int) -> PingProcessor:
        if processor_type == ProcessorType.PROCESS:
            return MultiProcessPingProcessor(pool_size)

        if processor_type == ProcessorType.THREAD:
            return MultiThreadPingProcessor(pool_size)

        raise ValueError(f"{processor_type} is not a supported type")

