# -- FILE: loan_etl/run.py
'''
Entry point into the ETL which can be called directly 
or run via a job scheduler.
'''
from   argparse import ArgumentParser
import loan_etl.app.pipeline as etl

def main():
    parser = ArgumentParser(description="Run ETL pipeline.")
    parser.add_argument("dirPath", type=str,
                        help="The path of the directory holding configuration json files")
    args = parser.parse_args()
    etl.run(args.dirPath)

if __name__ == "__main__":
    main()