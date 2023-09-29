import pandas as pd
import numpy as np
import pyodbc
import warnings
import datetime
from datetime import timedelta
import logging
from node_rules import cgcr_oxygen_tree, cgcr_aluminium_prediction, vag_aluminium_prediction

warnings.filterwarnings('ignore')

# for logging purposes
now = datetime.datetime.now()
print("Start Time : ", now)


####################################################################################

def call_prediction_function(row):

    """
    This function calls either the cgcr/vag prediction function based on the grade type for each heat
    """

    if row['GRADE_TYPE'] == 'CG/CR':
        return cgcr_aluminium_prediction(row)

    elif row['GRADE_TYPE'] == 'VAG':
        return vag_aluminium_prediction(row)

    else:
        print("Unknown Grade")
        return None


def find_latest_heats(conn):
    """
    This function checks the SQL server and finds the list of heats for which AL Prediction is to be done.
    If this list is empty, then the predictive model is not run

    :param conn: SQL server connection client
    """
    # reading the table which has information regarding sample chemistry
    sample_chemistry_data= pd.read_sql("SELECT TOP(1000) * FROM heat_analysis order by SAMPLE_TIME desc", conn)

    # keeping only data points from the last 3 hours
    # window selected based on analysis
    sample_chemistry_data = sample_chemistry_data[sample_chemistry_data['SAMPLE_TIME']>= now - timedelta(minutes = 180)]

    # first we remove all records of LF5, as we are not predicting for that LF
    sample_chemistry_data = sample_chemistry_data[sample_chemistry_data['AGGREGATE'] != 'LF5']

    # for this, first we have to find the heats which have the latest sample information as first sample
    sample_latest = sample_chemistry_data.groupby('HEAT_NUMBER').agg({'SAMPLE_CODE':'max'})
    sample_latest = sample_latest[sample_latest['SAMPLE_CODE'].isin(['25101','25201'])]
    sample_latest.reset_index(inplace = True)

    # getting the latest heat numbers from master_output_table
    # we've already predicted the outputs for this heat, so we don't need to predict again
    previous_heats = pd.read_sql("SELECT TOP(1000) HEAT_NUMBER FROM dbo.output_table ORDER BY MSG_TIME_STAMP desc",conn)
    previous_heats = list(previous_heats['HEAT_NUMBER'])
    previous_heats = [str(x) for x in previous_heats]

    # we will only run for any new heats that have been found
    latest_heats = sample_latest['HEAT_NUMBER'].unique()
    run_heats = [x for x in latest_heats if x not in previous_heats]

    return run_heats


def main():
    """
    Main function that is called whenever predictions are to be made
    """
    ######################### Connecting to SQL Server ##############################

    conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=STEELDNA;'
                         'Database=DeS;'
                         'UID=sa;'
                         'PWD=admin@123;'
                         'Trusted_Connection=no;')

    cursor = conn.cursor()

    ######################### checking if model needs to be run #####################

    # getting list of heats for which model has not yet been run
    run_heats = find_latest_heats(conn)
    print(run_heats)

    run_heats=['22301446','22301445','22101414']
    # if not empty, model is to be run
    if len(run_heats) != 0:

        # importing heat_analysis
        heat_analysis = pd.read_sql("select TOP(1000) * from heat_analysis order by MSG_TIME_STAMP desc", conn)
#         heat_analysis = pd.read_sql("select * from heat_analysis where HEAT_NUMBER in ('22200172','22400185','22200161') order by MSG_TIME_STAMP desc", conn)

        heat_analysis = heat_analysis[heat_analysis['HEAT_NUMBER'].isin(run_heats)]
        # importing lf_heat_data
        lf_heat_data = pd.read_sql("select TOP(1000) * from lf_heat_data order by MSG_TIME_STAMP desc", conn)
        lf_heat_data = pd.read_sql("select TOP(1000) * from lf_heat_data where ALBAR <> 0 order by MSG_TIME_STAMP desc", conn)
#         lf_heat_data = pd.read_sql("select * from lf_heat_data where HEAT_NUMBER in ('22200172','22400185','22200161') order by MSG_TIME_STAMP desc", conn)

        lf_heat_backup=lf_heat_data[['HEAT_NUMBER','GRADE_TYPE']].rename(columns={'HEAT_NUMBER':'PREV_HEAT_NUMBER'})
        lf_heat_data = lf_heat_data[lf_heat_data['HEAT_NUMBER'].isin(run_heats)]

        prev_grade_flag=lf_heat_data[['HEAT_NUMBER','PREV_HEAT_NUMBER']].drop_duplicates(subset=['HEAT_NUMBER'])
        prev_grade_flag=prev_grade_flag.merge(lf_heat_backup,on=['PREV_HEAT_NUMBER'], how='left')
        # importing the grade mapping fact table
        print(prev_grade_flag)

        # importing the grade mapping fact table
        grade_mapping = pd.read_sql("select * from grade_mapping", conn)

        ######################### data processing ##############################

#         print(heat_analysis)
#         print(lf_heat_data)

        # calculating required columns
        lf_heat_data['final_O2_ppm'] = lf_heat_data['TAP_O2'] + lf_heat_data['O2AFTERCELOX']

        # converting ALBAR to tons
        lf_heat_data['ALBAR'] = lf_heat_data['ALBAR']/19

        # renaming the required columns
        lf_heat_data.rename(columns = {
            'GRADE_TYPE':'GRADE',
            'LM_START_WT':'LM_Start_Wt_lf',
            'FIRSTMEASTEMP':'1st_Probe_temp_lf',
            'ALBAR':'Al_Bar_lf',
            'LIME':'Lime_tap',
            'SIMN':'SiMn_tap',
            'LTA':'LTA_lf'
        }, inplace = True)

        # keeping only the required rows
        lf_heat_data = lf_heat_data.groupby(['HEAT_NUMBER','STATION']).agg({'MSG_TIME_STAMP':'max','GRADE': 'first','1st_Probe_temp_lf':'max', 'Al_Bar_lf':'max','LM_Start_Wt_lf':'max','LTA_lf':'max','Lime_tap':'max','SiMn_tap':'max','final_O2_ppm':'max'})
        lf_heat_data.reset_index(inplace = True)
        lf_heat_data.sort_values(by = ['MSG_TIME_STAMP'], ascending = False, inplace = True)
        lf_heat_data.drop_duplicates(subset = ['HEAT_NUMBER'], keep = 'first', inplace = True)

        # preprocessing heat_analysis
        # if there are multiple records for a heat, keeping only the latest one
        heat_analysis.drop_duplicates(subset = ['HEAT_NUMBER'], keep = 'first', inplace = True)

        # keeping only required columns
        heat_analysis = heat_analysis[['HEAT_NUMBER','AGGREGATE','AL_TOTAL','S','C','SI']]

        # renaming columns as per requirement
        heat_analysis.rename(columns = {'AL_TOTAL':'AL_chem_first', 'S':'S_chem_first','SI':'SI_chem_first','C':'C_chem_first'}, inplace = True)


        # merging sample chemistry data with lf data
        ads = heat_analysis.merge(lf_heat_data, on = ['HEAT_NUMBER'], how = 'inner')

        # filling nulls with zeros
        # these will get clipped in the next step
        ads.fillna(0, inplace = True)

        # ads preprocessing

        # constraints to avoid cases with data issues
        # constraint no.1
        # al_bar range is 15-25
        ads['Al_Bar_lf'] = ads['Al_Bar_lf'].clip(15,25)
        # constraint no.2
        # lm weight is between 170 - 205
        ads['LM_Start_Wt_lf'] = ads['LM_Start_Wt_lf'].clip(170,205)

        # these are the caps for each column
        # TODO: add SiMn capping as well
        ads['LTA_lf'] = ads['LTA_lf'].clip(60)
        ads['Lime_tap'] = ads['Lime_tap'].clip(500)
        ads['1st_Probe_temp_lf'] = ads['1st_Probe_temp_lf'].clip(1550)
        ads['final_O2_ppm'] = ads['final_O2_ppm'].clip(750)

        # adding loi perc as a column
        # this is a fixed value
        ads['LOI_perc'] = 6
        print(len(ads))

        print(ads['GRADE'])

        # mapping the grades to their grade type (CG/CR or VAG)
        # the grades that don't get mapped are billet heats, and so will not be run in this model
        ads = ads.merge(grade_mapping, on = ['GRADE'], how = 'inner')

        ################ AL Prediction #################################
        print(len(ads))

        # dont predict if ads is empty
        if len(ads) > 0:

            # predicting aluminium material
            ads['al_predictions'] =  ads.apply(call_prediction_function, axis = 1)

            # splitting the list of outputs into separate columns
            ads['AL_KGS'] = ads['al_predictions'].apply(lambda x: x[0])
            ads['Carbon Node'] = ads['al_predictions'].apply(lambda x: x[1])
            ads['Oxygen Node'] = ads['al_predictions'].apply(lambda x:x[2])
            del ads['al_predictions']

            # replacing -ve predictions as 0
            ads['AL_KGS'][ads['AL_KGS']<0]=0

            #Correction for Al first Chemistry
            ads['AL_KGS'][ads['AL_chem_first']>.07]=ads['AL_KGS']-35
            #Correction for Opening Temp
            ads['AL_KGS'][(ads['1st_Probe_temp_lf']>1600) & (ads['GRADE_TYPE']=='CG/CR')]=ads['AL_KGS']-10
            #Correction for Opening Temp
            ######

            grade_constraints = pd.read_sql("select * from grade_constraints", conn)
            prev_grade_flag=prev_grade_flag.merge(grade_constraints[['Grade','Si_min']].rename(columns={'Grade':'GRADE_TYPE'}),on=['GRADE_TYPE'], how='left')
            prev_grade_flag['si_kill_flag']=0
            prev_grade_flag['si_kill_flag'][prev_grade_flag['Si_min']>0]=1
            print(prev_grade_flag)
            ads=pd.merge(ads,prev_grade_flag[['HEAT_NUMBER','si_kill_flag']], how='left', on=['HEAT_NUMBER'])

            ads['AL_KGS'][(ads['si_kill_flag']==1) & (ads['GRADE_TYPE']=='VAG')]=ads['AL_KGS']-15

            # predicting aluminium material in meters
            ads['AL_MTS'] = ads['AL_KGS'] * (3)



            # storing the interim output in a sql output_table
            # for index, row in ads.iterrows():
            #     cursor.execute(
            #     "INSERT INTO DeS.dbo.interim_outputs (HEAT_NUMBER, GRADE, GRADE_TYPE, AGGREGATE, STATION, AL_chem_first, S_chem_first, C_chem_first, SI_chem_first, First_Probe_temp_lf, Al_Bar_lf, LM_Start_Wt_lf, LTA_lf, Lime_tap, Simn_tap, final_O2_ppm, LOI_perc, AL_KGS, AL_MTS, Carbon_Node, Oxygen_Node) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            #     row['HEAT_NUMBER'],
            #     row['GRADE'],
            #     row['GRADE_TYPE'],
            #     row['AGGREGATE'],
            #     row['STATION'],
            #     row['AL_chem_first'],
            #     row['S_chem_first'],
            #     row['C_chem_first'],
            #     row['SI_chem_first'],
            #     row['1st_Probe_temp_lf'],
            #     row['Al_Bar_lf'],
            #     row['LM_Start_Wt_lf'],
            #     row['LTA_lf'],
            #     row['Lime_tap'],
            #     row['SiMn_tap'],
            #     row['final_O2_ppm'],
            #     row['LOI_perc'],
            #     row['AL_KGS'],
            #     row['AL_MTS'],
            #     row['Carbon Node'],
            #     row['Oxygen Node']
            #     )
            #
            #
            # # keeping only required columns
            # ads = ads[['HEAT_NUMBER','AGGREGATE','AL_KGS','AL_MTS']]
            #
            # # storing in SQL Server
            # # this is the main output table that gets pulled into the L2 system
            # for index, row in ads.iterrows():
            #     cursor.execute("INSERT INTO DeS.dbo.output_table (HEAT_NUMBER, AGGREGATE, AL_KGS, AL_MTS) values (?,?,?,?)", row['HEAT_NUMBER'], row['AGGREGATE'], row['AL_KGS'], row['AL_MTS'])

    # commiting any changes made and closing the cursor
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    main()
