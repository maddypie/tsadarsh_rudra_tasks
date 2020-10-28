import sys

import program_A


def main(parse):
    """Method sys.exc_info returns a tuple (type, value, traceback). The tuple
    holds information of the exception being handled. The exception information
    except the traceback is written to `log.txt` with the help of `program_A`.
    """

    try:
        data = eval(parse)
        print(data)
    except:
        print('error occured; see `log.txt`')
        exception = ' '.join([str(i) for i in sys.exc_info()[:-1]])
        program_A.write_exception(exception)


if __name__ == '__main__':
    data = ' '.join(sys.argv[1:])
    main(data)

