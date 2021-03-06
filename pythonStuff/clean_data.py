#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:17:23 2018

@author: gtcbh
"""
import os
import sys
import argparse
import pandas as pd
import pdb


def clean(filename):
    # Data file to read (relative path w/o the .csv)
    # filename = "../../alldata"
    df = pd.read_csv(filename + ".csv", index_col=0)

    columns = df.columns
    for col in columns:
        if "~" in col:
            print(col)
            newcol = col.replace("~", "_")
            df.rename(columns={col: newcol}, inplace=True)
            print(df.columns)

    #  Unimportant columns
    df.drop(columns=[ \
            "autonomy_t_1", \
            "autonomy_t_2_predator", \
            "autonomy_t_3_predator", \
            "motion_model_predator", \
            "motion_model_t_1", \
            # "results_dir",  # actually want this one so we can show where the raw data is
            "entity_count", \
            "flight_time", \
            "flight_time_norm", \
            "non_team_coll", \
            "team_coll", \
            "ground_coll", \
            # Score is a duplicate of NonTeamCaptures, our output metric
            "score", \
            # TeamCaptures is irrelevant for this simulation
            "TeamCaptures", \
            # Other things to remove
            "max_pred_speed_t_1", \
            "align_weight_t_2_predator", \
            "avoid_nonteam_weight_t_2_predator", \
            "avoid_team_weight_t_2_predator", \
            "centroid_weight_t_2_predator", \
            "comms_range_t_2_predator", \
            "max_speed_t_2_predator", \
            "align_weight_t_3_predator", \
            "avoid_nonteam_weight_t_3_predator", \
            "avoid_team_weight_t_3_predator", \
            "centroid_weight_t_3_predator", \
            "comms_range_t_3_predator", \
            "max_speed_t_3_predator" \
            ], \
            inplace=True, errors='ignore')
    df = df.drop([0, 1]).reset_index(drop=True)
        
        
    #Theoretically this data is more ready now
    df = df[pd.notnull(df["NonTeamCapture"])]

    #File to write to
    df.to_csv(filename + "_clean.csv", index=0)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Relative path to csv file, no extension')
    args = parser.parse_args()

    clean(args.path)




if __name__ == '__main__':
    sys.exit(main())

