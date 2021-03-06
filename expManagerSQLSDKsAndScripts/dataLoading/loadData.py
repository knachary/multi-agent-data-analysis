#!/usr/bin/env python3

import csv
import argparse
from authentication import *

#params
serverDomain = 'http://localhost:8080'
user = 'admin'
password = 'admin'

def loadCsv(csvFilePath):
    authRes = authenticate(user,password,serverDomain)
    with open(csvFilePath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['index'], row['NonTeamCapture'], type(row['NonTeamCapture']))
            simulationRun = {
                'index': row['index'],
                'nonTeamCapture': int(float(row['NonTeamCapture'].strip() or 0))
            }
            authorizedPost(serverDomain, '/api/simulation-runs', {}, simulationRun, authRes)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csvFile", help="The CSV file to load.")
    args = parser.parse_args()
    loadCsv(args.csvFile)

if __name__ == "__main__":
    main()
