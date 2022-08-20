from typing import Generator
from data_record import DataRecord

DataRecordGenerator = Generator[DataRecord, None, None]


def read_by_records(source: str) -> DataRecordGenerator:

    header_processed = False

    with open(source) as file:
        for line in file:
            # split the comma seperated line
            record = line.split(sep=',')

            if not header_processed:
                # if it is the first line then
                # process it as a header
                header = [x.rstrip() for x in record]
                yield DataRecord(True, tuple(header))
                header_processed = True
            else:
                # if it is not the first line
                # then process it as floating
                # point data
                data = [float(x) for x in record]
                yield DataRecord(False, tuple(data))
