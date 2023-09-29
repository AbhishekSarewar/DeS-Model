# this file contains the regression equations for various scenarios
# aluminium addition is predicted using the mathematical equations

###################################################### CG/CR #######################################################################################
def cgcr_oxygen_tree(row):
    """

    This function will calculate the aluminium material addition using final_o2_ppm as one of the regression
    variables. This is only used when certain conditions are met, and is only called from the cgcr_aluminium_prediction
    function
    """

    al_lsl = 0.030
    fade_rate = 0.004

    if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] <= 0.022) and (row['Al_Bar_lf'] > 15.5):
        row['Node'] = 1
        row['AL_mat'] = 0.0078 * row['final_O2_ppm'] + 0.965 * row['LM_Start_Wt_lf'] + 0.0371 * row['1st_Probe_temp_lf'] + -6.0358 * row['Al_Bar_lf'] + -0.0338 * row['Lime_tap'] + -238.4204 * row['AL_chem_first'] + 2254.8275 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.035):
        row['Node'] = 2
        row['AL_mat'] = -0.0061 * row['final_O2_ppm'] + 0.7951 * row['LM_Start_Wt_lf'] + 0.067 * row['1st_Probe_temp_lf'] + -2.6335 * row['Al_Bar_lf'] + -0.0373 * row['Lime_tap'] + -1883.7621 * row['AL_chem_first'] + 4583.8493 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.035):
        row['Node'] = 3
        row['AL_mat'] = 0.0394 * row['final_O2_ppm'] + 0.4446 * row['LM_Start_Wt_lf'] + 0.0591 * row['1st_Probe_temp_lf'] + -1.131 * row['Al_Bar_lf'] + -0.0342 * row['Lime_tap'] + -1805.4052 * row['AL_chem_first'] + 4872.0171 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.015):
        row['Node'] = 4
        row['AL_mat'] = 0.021 * row['final_O2_ppm'] + 0.5297 * row['LM_Start_Wt_lf'] + 0.054 * row['1st_Probe_temp_lf'] + -0.3041 * row['Al_Bar_lf'] + -0.004 * row['Lime_tap'] + -3664.7478 * row['AL_chem_first'] + 5646.8733 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] <= 0.03):
        row['Node'] = 5
        row['AL_mat'] = 0.0472 * row['final_O2_ppm'] + 0.4099 * row['LM_Start_Wt_lf'] + 0.0752 * row['1st_Probe_temp_lf'] + -1.4064 * row['Al_Bar_lf'] + -0.0045 * row['Lime_tap'] + -2538.0108 * row['AL_chem_first'] + 3874.9522 * row['S_chem_first']
    elif(row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] > 0.022) and (row['AL_chem_first'] > 0.059):
        row['Node'] = 6
        row['AL_mat'] = -0.0099 * row['final_O2_ppm'] + 0.7622 * row['LM_Start_Wt_lf'] + 0.0607 * row['1st_Probe_temp_lf'] + -3.3849 * row['Al_Bar_lf'] + -0.0656 * row['Lime_tap'] + -1057.3001 * row['AL_chem_first'] + 4924.1931 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] > 0.022) and (row['AL_chem_first'] <= 0.059):
        row['Node'] = 7
        row['AL_mat'] = 0.0587 * row['final_O2_ppm'] + -0.0184 * row['LM_Start_Wt_lf'] + 0.007 * row['1st_Probe_temp_lf'] + -2.7345 * row['Al_Bar_lf'] + -0.0025 * row['Lime_tap'] + 818.841 * row['AL_chem_first'] + 4921.6207 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.015):
        row['Node'] = 8
        row['AL_mat'] = 0.077 * row['final_O2_ppm'] + -0.3263 * row['LM_Start_Wt_lf'] + 0.2246 * row['1st_Probe_temp_lf'] + -6.302 * row['Al_Bar_lf'] + -0.0044 * row['Lime_tap'] + -3924.3456 * row['AL_chem_first'] + 3288.5724 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] > 0.02) and (row['LM_Start_Wt_lf'] <= 203.743):
        row['Node'] = 9
        row['AL_mat'] = -0.0114 * row['final_O2_ppm'] + -0.4109 * row['LM_Start_Wt_lf'] + 0.1836 * row['1st_Probe_temp_lf'] + 7.7806 * row['Al_Bar_lf'] + -0.086 * row['Lime_tap'] + 645.4803 * row['AL_chem_first'] + 3057.6657 * row['S_chem_first']
    elif(row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.024) and (row['final_O2_ppm'] > 1016.35):
        row['Node'] = 10
        row['AL_mat'] = 0.0172 * row['final_O2_ppm'] + 0.7945 * row['LM_Start_Wt_lf'] + 0.0299 * row['1st_Probe_temp_lf'] + -0.0299 * row['Al_Bar_lf'] + -0.0134 * row['Lime_tap'] + -2280.7642 * row['AL_chem_first'] + 4619.1716 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] <= 0.02) and (row['Lime_tap'] > 1010.2):
        row['Node'] = 11
        row['AL_mat'] = 0.1627 * row['final_O2_ppm'] + 1.5266 * row['LM_Start_Wt_lf'] + -0.0934 * row['1st_Probe_temp_lf'] + -0.9257 * row['Al_Bar_lf'] + -0.0307 * row['Lime_tap'] + -7940.9991 * row['AL_chem_first'] + 3563.447 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] <= 0.02) and (row['Lime_tap'] <= 1010.2):
        row['Node'] = 12
        row['AL_mat'] = 0.0931 * row['final_O2_ppm'] + 0.5727 * row['LM_Start_Wt_lf'] + -0.0297 * row['1st_Probe_temp_lf'] + -1.7368 * row['Al_Bar_lf'] + 0.2081 * row['Lime_tap'] + 1476.5607 * row['AL_chem_first'] + -454.0645 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] > 0.03):
        row['Node'] = 13
        row['AL_mat'] = -0.0843 * row['final_O2_ppm'] + 1.9108 * row['LM_Start_Wt_lf'] + 0.0295 * row['1st_Probe_temp_lf'] + -5.8736 * row['Al_Bar_lf'] + -0.0418 * row['Lime_tap'] + -757.535 * row['AL_chem_first'] + 3494.3731 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.024) and (row['final_O2_ppm'] <= 1016.35):
        row['Node'] = 14
        row['AL_mat'] = 0.0056 * row['final_O2_ppm'] + 0.8489 * row['LM_Start_Wt_lf'] + 0.1301 * row['1st_Probe_temp_lf'] + -5.7387 * row['Al_Bar_lf'] + -0.0643 * row['Lime_tap'] + -3757.1869 * row['AL_chem_first'] + 5313.2647 * row['S_chem_first']
    elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] <= 0.022) and (row['Al_Bar_lf'] <= 15.5):
        row['Node'] = 15
        row['AL_mat'] = 0.0333 * row['final_O2_ppm'] + 1.9003 * row['LM_Start_Wt_lf'] + 0.4419 * row['1st_Probe_temp_lf'] + -73.0713 * row['Al_Bar_lf'] + -0.025 * row['Lime_tap'] + 1918.4667 * row['AL_chem_first'] + 5078.7158 * row['S_chem_first']
    elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] > 0.02) and (row['LM_Start_Wt_lf'] > 203.743):
        row['Node'] = 16
        row['AL_mat'] = -0.3311 * row['final_O2_ppm'] + -5.3063 * row['LM_Start_Wt_lf'] + 0.5634 * row['1st_Probe_temp_lf'] + 35.0708 * row['Al_Bar_lf'] + -0.0342 * row['Lime_tap'] + 7701.7331 * row['AL_chem_first'] + 10330.0 * row['S_chem_first']
    else:
        print("weak node")
        row['Node'] = 0
        row['AL_mat'] = (10.0 * (row['LM_Start_Wt_lf'] + 1) * (al_lsl - row['AL_chem_first'] + 16 * fade_rate ))/0.6

    return row['AL_mat'], row['Node']


def cgcr_aluminium_prediction(row):
    """

    This function will calculate the aluminium material addition for CG/CR grades
    # the "node" columns are only for debugging purposes
    """

    al_lsl = 0.030
    fade_rate = 0.004

    # initializing to 0, will get replaced if we use oxygen tree
    row['Oxygen Node'] = 0

    if (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] > 0.05) and (row['SI_chem_first'] > 0.004) and (row['S_chem_first'] <= 0.02):

        row['Carbon Node'] = 1

        c = 0.2798 * row['LM_Start_Wt_lf'] + 0.1403 * row['1st_Probe_temp_lf'] + -5.0366 * row['Al_Bar_lf'] + -0.0289 * row['Lime_tap'] + -764.6388 * row['AL_chem_first'] + 2453.4545 * row['S_chem_first'] + -0.0004 * row['LTA_lf'] + 0.0223 * row['SiMn_tap'] + -4409.1428 * row['SI_chem_first'] + 43.3277 * row['C_chem_first']


        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] <= 0.022) and (row['Al_Bar_lf'] > 15.5):

            row['Oxygen Node'] = 1

            row['AL_mat'] = 0.2798 * row['LM_Start_Wt_lf'] + 0.1403 * row['1st_Probe_temp_lf'] + -5.0366 * row['Al_Bar_lf'] + -0.0289 * row['Lime_tap'] + -764.6388 * row['AL_chem_first'] + 2453.4545 * row['S_chem_first'] + -0.0004 * row['LTA_lf'] + 0.0223 * row['SiMn_tap'] + -4409.1428 * row['SI_chem_first'] + 43.3277 * row['C_chem_first'] - 16

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] <= 0.022) and (row['Al_Bar_lf'] <= 15.5):

            row['Oxygen Node'] = 15

            o = 0.0333 * row['final_O2_ppm'] + 1.9003 * row['LM_Start_Wt_lf'] + 0.4419 * row['1st_Probe_temp_lf'] + -73.0713 * row['Al_Bar_lf'] + -0.025 * row['Lime_tap'] + 1918.4667 * row['AL_chem_first'] + 5078.7158 * row['S_chem_first']

            row['AL_mat'] = (c+o)/2

        else:

            row['AL_mat'] = c


    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.021) and (row['SI_chem_first'] > 0.004):

        row['Carbon Node'] = 2

        c = 0.5261 * row['LM_Start_Wt_lf'] + 0.0791 * row['1st_Probe_temp_lf'] + -1.3498 * row['Al_Bar_lf'] + -0.0258 * row['Lime_tap'] + -1708.4114 * row['AL_chem_first'] + 5901.3276 * row['S_chem_first'] + -1.061e-05 * row['LTA_lf'] + -0.0293 * row['SiMn_tap'] + -4352.8933 * row['SI_chem_first'] + -314.14 * row['C_chem_first']


        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.035):

            row['Oxygen Node'] = 2

            o = -0.0061 * row['final_O2_ppm'] + 0.7951 * row['LM_Start_Wt_lf'] + 0.067 * row['1st_Probe_temp_lf'] + -2.6335 * row['Al_Bar_lf'] + -0.0373 * row['Lime_tap'] + -1883.7621 * row['AL_chem_first'] + 4583.8493 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.035):

            row['Oxygen Node'] = 3

            o = 0.0394 * row['final_O2_ppm'] + 0.4446 * row['LM_Start_Wt_lf'] + 0.0591 * row['1st_Probe_temp_lf'] + -1.131 * row['Al_Bar_lf'] + -0.0342 * row['Lime_tap'] + -1805.4052 * row['AL_chem_first'] + 4872.0171 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] > 0.05) and (row['SI_chem_first'] > 0.004) and (row['S_chem_first'] > 0.02):

        row['Carbon Node'] = 3

        c = 0.0285 * row['LM_Start_Wt_lf'] + 0.1877 * row['1st_Probe_temp_lf'] + -3.4885 * row['Al_Bar_lf'] + -0.0269 * row['Lime_tap'] + -2018.3323 * row['AL_chem_first'] + 4606.0664 * row['S_chem_first'] + -0.0003 * row['LTA_lf'] + 0.0123 * row['SiMn_tap'] + -4181.5531 * row['SI_chem_first'] + -268.2512 * row['C_chem_first']


        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] > 0.022) and (row['AL_chem_first'] <= 0.059):

            row['Oxygen Node'] = 7

            o = 0.0587 * row['final_O2_ppm'] + -0.0184 * row['LM_Start_Wt_lf'] + 0.007 * row['1st_Probe_temp_lf'] + -2.7345 * row['Al_Bar_lf'] + -0.0025 * row['Lime_tap'] + 818.841 * row['AL_chem_first'] + 4921.6207 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] > 0.05) and (row['SI_chem_first'] <= 0.004) and (row['SiMn_tap'] <= 170.119):

        row['Carbon Node'] = 4

        c = 0.855 * row['LM_Start_Wt_lf'] + 0.0838 * row['1st_Probe_temp_lf'] + -1.3642 * row['Al_Bar_lf'] + -0.036 * row['Lime_tap'] + -1413.6468 * row['AL_chem_first'] + 4535.899 * row['S_chem_first'] + -0.0013 * row['LTA_lf'] + 0.1752 * row['SiMn_tap'] + -17950.0 * row['SI_chem_first'] + -1058.9498 * row['C_chem_first']


        if(row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] > 0.022) and (row['AL_chem_first'] > 0.059):

            row['Oxygen Node'] = 6

            o = -0.0099 * row['final_O2_ppm'] + 0.7622 * row['LM_Start_Wt_lf'] + 0.0607 * row['1st_Probe_temp_lf'] + -3.3849 * row['Al_Bar_lf'] + -0.0656 * row['Lime_tap'] + -1057.3001 * row['AL_chem_first'] + 4924.1931 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] > 0.022) and (row['AL_chem_first'] <= 0.059):

            row['Oxygen Node'] = 7

            o = 0.0587 * row['final_O2_ppm'] + -0.0184 * row['LM_Start_Wt_lf'] + 0.007 * row['1st_Probe_temp_lf'] + -2.7345 * row['Al_Bar_lf'] + -0.0025 * row['Lime_tap'] + 818.841 * row['AL_chem_first'] + 4921.6207 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] > 0.05) and (row['S_chem_first'] <= 0.022) and (row['Al_Bar_lf'] <= 15.5):

            row['Oxygen Node'] = 15

            o = 0.0333 * row['final_O2_ppm'] + 1.9003 * row['LM_Start_Wt_lf'] + 0.4419 * row['1st_Probe_temp_lf'] + -73.0713 * row['Al_Bar_lf'] + -0.025 * row['Lime_tap'] + 1918.4667 * row['AL_chem_first'] + 5078.7158 * row['S_chem_first']

            row['AL_mat'] = o

        else:

            row['AL_mat'] = c


        row['AL_mat'] = 0.855 * row['LM_Start_Wt_lf'] + 0.0838 * row['1st_Probe_temp_lf'] + -1.3642 * row['Al_Bar_lf'] + -0.036 * row['Lime_tap'] + -1413.6468 * row['AL_chem_first'] + 4535.899 * row['S_chem_first'] + -0.0013 * row['LTA_lf'] + 0.1752 * row['SiMn_tap'] + -17950.0 * row['SI_chem_first'] + -1058.9498 * row['C_chem_first']

    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.021) and (row['S_chem_first'] <= 0.029):

        row['Carbon Node'] = 5

        c = 0.3657 * row['LM_Start_Wt_lf'] + 0.1113 * row['1st_Probe_temp_lf'] + -0.9966 * row['Al_Bar_lf'] + 0.0054 * row['Lime_tap'] + -2055.9061 * row['AL_chem_first'] + 4510.7115 * row['S_chem_first'] + 0.0002 * row['LTA_lf'] + -0.0406 * row['SiMn_tap'] + -3218.7582 * row['SI_chem_first'] + -854.3342 * row['C_chem_first']

        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.035):

            row['Oxygen Node'] = 2

            o = -0.0061 * row['final_O2_ppm'] + 0.7951 * row['LM_Start_Wt_lf'] + 0.067 * row['1st_Probe_temp_lf'] + -2.6335 * row['Al_Bar_lf'] + -0.0373 * row['Lime_tap'] + -1883.7621 * row['AL_chem_first'] + 4583.8493 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.035):

            row['Oxygen Node'] = 3

            o = 0.0394 * row['final_O2_ppm'] + 0.4446 * row['LM_Start_Wt_lf'] + 0.0591 * row['1st_Probe_temp_lf'] + -1.131 * row['Al_Bar_lf'] + -0.0342 * row['Lime_tap'] + -1805.4052 * row['AL_chem_first'] + 4872.0171 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] <= 0.03):

            row['Oxygen Node'] = 5

            o = 0.0472 * row['final_O2_ppm'] + 0.4099 * row['LM_Start_Wt_lf'] + 0.0752 * row['1st_Probe_temp_lf'] + -1.4064 * row['Al_Bar_lf'] + -0.0045 * row['Lime_tap'] + -2538.0108 * row['AL_chem_first'] + 3874.9522 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:
            row['AL_mat'] = c

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] > 0.015) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.024):

        row['Carbon Node'] = 6

        c = 0.3412 * row['LM_Start_Wt_lf'] + 0.1243 * row['1st_Probe_temp_lf'] + -2.3149 * row['Al_Bar_lf'] + 0.0026 * row['Lime_tap'] + -707.5725 * row['AL_chem_first'] + 4396.2823 * row['S_chem_first'] + 0.0043 * row['LTA_lf'] + 0.0328 * row['SiMn_tap'] + -5089.7416 * row['SI_chem_first'] + -1601.3223 * row['C_chem_first']

        row['AL_mat'] = c


    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] > 0.015) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.024):

        row['Carbon Node'] = 7

        c = 0.3115 * row['LM_Start_Wt_lf'] + 0.1151 * row['1st_Probe_temp_lf'] + -0.3084 * row['Al_Bar_lf'] + 0.0033 * row['Lime_tap'] + -2436.6049 * row['AL_chem_first'] + 5896.8806 * row['S_chem_first'] + -0.0009 * row['LTA_lf'] + -0.0042 * row['SiMn_tap'] + -5288.325 * row['SI_chem_first'] + -1067.7573 * row['C_chem_first']

        if (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.015):

            row['Oxygen Node'] = 4

            o = 0.021 * row['final_O2_ppm'] + 0.5297 * row['LM_Start_Wt_lf'] + 0.054 * row['1st_Probe_temp_lf'] + -0.3041 * row['Al_Bar_lf'] + -0.004 * row['Lime_tap'] + -3664.7478 * row['AL_chem_first'] + 5646.8733 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c


    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.021) and (row['SI_chem_first'] <= 0.004):

        row['Carbon Node'] = 8

        c = 0.609 * row['LM_Start_Wt_lf'] + 0.1795 * row['1st_Probe_temp_lf'] + -4.7042 * row['Al_Bar_lf'] + -0.0518 * row['Lime_tap'] + -1385.7228 * row['AL_chem_first'] + 2071.0482 * row['S_chem_first'] + 0.0011 * row['LTA_lf'] + 0.2036 * row['SiMn_tap'] + -23180.0 * row['SI_chem_first'] + 466.3279 * row['C_chem_first']

        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] > 0.035):

            row['Oxygen Node'] = 2

            o = -0.0061 * row['final_O2_ppm'] + 0.7951 * row['LM_Start_Wt_lf'] + 0.067 * row['1st_Probe_temp_lf'] + -2.6335 * row['Al_Bar_lf'] + -0.0373 * row['Lime_tap'] + -1883.7621 * row['AL_chem_first'] + 4583.8493 * row['S_chem_first']

            row['AL_mat'] = o

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] <= 0.024) and (row['AL_chem_first'] <= 0.035):

            row['Oxygen Node'] = 3

            o = 0.0394 * row['final_O2_ppm'] + 0.4446 * row['LM_Start_Wt_lf'] + 0.0591 * row['1st_Probe_temp_lf'] + -1.131 * row['Al_Bar_lf'] + -0.0342 * row['Lime_tap'] + -1805.4052 * row['AL_chem_first'] + 4872.0171 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] <= 0.015) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] <= 0.02):

        row['Carbon Node'] = 9

        c = 0.5809 * row['LM_Start_Wt_lf'] + 0.1717 * row['1st_Probe_temp_lf'] + 2.4264 * row['Al_Bar_lf'] + -0.0341 * row['Lime_tap'] + -3285.9989 * row['AL_chem_first'] + 3091.3112 * row['S_chem_first'] + -0.0017 * row['LTA_lf'] + -0.117 * row['SiMn_tap'] + -4937.5203 * row['SI_chem_first'] + -2871.3224 * row['C_chem_first']

        if (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] <= 0.02) and (row['Lime_tap'] <= 1010.2):

            row['Oxygen Node'] = 12

            o = 0.0931 * row['final_O2_ppm'] + 0.5727 * row['LM_Start_Wt_lf'] + -0.0297 * row['1st_Probe_temp_lf'] + -1.7368 * row['Al_Bar_lf'] + 0.2081 * row['Lime_tap'] + 1476.5607 * row['AL_chem_first'] + -454.0645 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] <= 0.015) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] > 0.02):

        row['Carbon Node'] = 10

        c = 0.2572 * row['LM_Start_Wt_lf'] + 0.2498 * row['1st_Probe_temp_lf'] + -1.0351 * row['Al_Bar_lf'] + -0.0559 * row['Lime_tap'] + -3959.3532 * row['AL_chem_first'] + 4823.2363 * row['S_chem_first'] + 0.0095 * row['LTA_lf'] + -0.0664 * row['SiMn_tap'] + -8553.5977 * row['SI_chem_first'] + -2432.6962 * row['C_chem_first']

        if (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] <= 0.01) and (row['S_chem_first'] > 0.02) and (row['LM_Start_Wt_lf'] <= 203.743):

            row['Oxygen Node'] = 9

            o = -0.0114 * row['final_O2_ppm'] + -0.4109 * row['LM_Start_Wt_lf'] + 0.1836 * row['1st_Probe_temp_lf'] + 7.7806 * row['Al_Bar_lf'] + -0.086 * row['Lime_tap'] + 645.4803 * row['AL_chem_first'] + 3057.6657 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.021) and (row['S_chem_first'] > 0.029):

        row['Carbon Node'] = 11

        c = 0.7856 * row['LM_Start_Wt_lf'] + -0.0129 * row['1st_Probe_temp_lf'] + 4.362 * row['Al_Bar_lf'] + -0.0659 * row['Lime_tap'] + -1992.4572 * row['AL_chem_first'] + 7477.7345 * row['S_chem_first'] + -0.0007 * row['LTA_lf'] + 0.0208 * row['SiMn_tap'] + -2220.0319 * row['SI_chem_first'] + -1081.9221 * row['C_chem_first']

        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] <= 0.03):

            row['Oxygen Node'] = 5

            o = 0.0472 * row['final_O2_ppm'] + 0.4099 * row['LM_Start_Wt_lf'] + 0.0752 * row['1st_Probe_temp_lf'] + -1.4064 * row['Al_Bar_lf'] + -0.0045 * row['Lime_tap'] + -2538.0108 * row['AL_chem_first'] + 3874.9522 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] > 0.03):

            row['Oxygen Node'] = 13

            o = -0.0843 * row['final_O2_ppm'] + 1.9108 * row['LM_Start_Wt_lf'] + 0.0295 * row['1st_Probe_temp_lf'] + -5.8736 * row['Al_Bar_lf'] + -0.0418 * row['Lime_tap'] + -757.535 * row['AL_chem_first'] + 3494.3731 * row['S_chem_first']

            row['AL_mat'] = o

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] <= 0.015) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.016):

        row['Carbon Node'] = 12
        c = 0.1261 * row['LM_Start_Wt_lf'] + 0.1722 * row['1st_Probe_temp_lf'] + 1.0519 * row['Al_Bar_lf'] + -0.016 * row['Lime_tap'] + -1284.3628 * row['AL_chem_first'] + 4291.4388 * row['S_chem_first'] + -0.01 * row['LTA_lf'] + -0.0203 * row['SiMn_tap'] + -3953.4701 * row['SI_chem_first'] + -2227.1677 * row['C_chem_first']

        if (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.024) and (row['final_O2_ppm'] <= 1016.35):

            row['Oxygen Node'] = 14

            o = 0.0056 * row['final_O2_ppm'] + 0.8489 * row['LM_Start_Wt_lf'] + 0.1301 * row['1st_Probe_temp_lf'] + -5.7387 * row['Al_Bar_lf'] + -0.0643 * row['Lime_tap'] + -3757.1869 * row['AL_chem_first'] + 5313.2647 * row['S_chem_first']

            row['AL_mat'] = o

        else:

            row['AL_mat'] = c

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] > 0.015) and (row['S_chem_first'] > 0.024) and (row['AL_chem_first'] > 0.022):

        row['Carbon Node'] = 13
        c = 0.5743 * row['LM_Start_Wt_lf'] + 0.0822 * row['1st_Probe_temp_lf'] + -1.4686 * row['Al_Bar_lf'] + 0.0017 * row['Lime_tap'] + -1187.9995 * row['AL_chem_first'] + 4171.1597 * row['S_chem_first'] + 0.0015 * row['LTA_lf'] + -0.1217 * row['SiMn_tap'] + 1952.4868 * row['SI_chem_first'] + -1138.2887 * row['C_chem_first']

        if (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] <= 0.03):

            row['Oxygen Node'] = 5

            o = 0.0472 * row['final_O2_ppm'] + 0.4099 * row['LM_Start_Wt_lf'] + 0.0752 * row['1st_Probe_temp_lf'] + -1.4064 * row['Al_Bar_lf'] + -0.0045 * row['Lime_tap'] + -2538.0108 * row['AL_chem_first'] + 3874.9522 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] > 0.027) and (row['AL_chem_first'] <= 0.05) and (row['S_chem_first'] > 0.024) and (row['S_chem_first'] > 0.03):

            row['Oxygen Node'] = 13

            o = -0.0843 * row['final_O2_ppm'] + 1.9108 * row['LM_Start_Wt_lf'] + 0.0295 * row['1st_Probe_temp_lf'] + -5.8736 * row['Al_Bar_lf'] + -0.0418 * row['Lime_tap'] + -757.535 * row['AL_chem_first'] + 3494.3731 * row['S_chem_first']

            row['AL_mat'] = min(c,o)

        elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.024) and (row['final_O2_ppm'] > 1016.35):

            row['Oxygen Node'] = 10

            o = 0.0172 * row['final_O2_ppm'] + 0.7945 * row['LM_Start_Wt_lf'] + 0.0299 * row['1st_Probe_temp_lf'] + -0.0299 * row['Al_Bar_lf'] + -0.0134 * row['Lime_tap'] + -2280.7642 * row['AL_chem_first'] + 4619.1716 * row['S_chem_first']

            row['AL_mat'] = min(c,o) - 33

        elif (row['AL_chem_first'] <= 0.027) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] > 0.024) and (row['final_O2_ppm'] <= 1016.35):

            row['Oxygen Node'] = 14

            o = 0.0056 * row['final_O2_ppm'] + 0.8489 * row['LM_Start_Wt_lf'] + 0.1301 * row['1st_Probe_temp_lf'] + -5.7387 * row['Al_Bar_lf'] + -0.0643 * row['Lime_tap'] + -3757.1869 * row['AL_chem_first'] + 5313.2647 * row['S_chem_first']

            row['AL_mat'] = min(c,o) - 33

        else:

            row['AL_mat'] = c


    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] > 0.015) and (row['S_chem_first'] > 0.024) and (row['AL_chem_first'] <= 0.022):
        row['Carbon Node'] = 14
        c = -0.1188 * row['LM_Start_Wt_lf'] + 0.2324 * row['1st_Probe_temp_lf'] + 7.6551 * row['Al_Bar_lf'] + -0.1695 * row['Lime_tap'] + 5022.7992 * row['AL_chem_first'] + 666.7963 * row['S_chem_first'] + -0.0046 * row['LTA_lf'] + 0.1344 * row['SiMn_tap'] + -10060.0 * row['SI_chem_first'] + -2723.9295 * row['C_chem_first']

        o, node = cgcr_oxygen_tree(row)

        row['Oxygen Node'] = node
        row['AL_mat'] = min(c,o)

    elif (row['AL_chem_first'] > 0.03) and (row['AL_chem_first'] > 0.05) and (row['SI_chem_first'] <= 0.004) and (row['SiMn_tap'] > 170.119):

        row['Carbon Node'] = 15

        o, node = cgcr_oxygen_tree(row)

        row['Oxygen Node'] = node
        row['AL_mat'] = o

    elif (row['AL_chem_first'] <= 0.03) and (row['AL_chem_first'] <= 0.015) and (row['AL_chem_first'] > 0.01) and (row['S_chem_first'] <= 0.016):

        row['Carbon Node'] = 16

        c = -1.0917 * row['LM_Start_Wt_lf'] + 0.5701 * row['1st_Probe_temp_lf'] + -21.2452 * row['Al_Bar_lf'] + -0.0651 * row['Lime_tap'] + 476.5523 * row['AL_chem_first'] + 6669.1629 * row['S_chem_first'] + -0.0036 * row['LTA_lf'] + 0.1242 * row['SiMn_tap'] + -5196.6844 * row['SI_chem_first'] + -2299.668 * row['C_chem_first']

        o, node = cgcr_oxygen_tree(row)

        row['Oxygen Node'] = node
        row['AL_mat'] = min(c,o)

    else:
        print("weak node")
        row['Carbon Node'] = 0
        row['Oxygen Node'] = 0
        row['AL_mat'] = (10.0 * (row['LM_Start_Wt_lf'] + 1) * (al_lsl - row['AL_chem_first'] + 16 * fade_rate ))/0.6

    return [row['AL_mat'], row['Carbon Node'], row['Oxygen Node']]

################################################## VAG #################################################################################

def vag_aluminium_prediction(row):
    """

    This function will calculate the aluminium material addition for CG/CR grades
    # the "node" columns are only for debugging purposes
    """

    al_lsl = 0.030
    fade_rate = 0.004

    # initializing to 0, will get replaced if we use oxygen tree
    row['Oxygen Node'] = 0

    if (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] > 0.046) and (row['Lime_tap'] <= 2927.5) and (row['S_chem_first'] <= 0.027):
        row['AL_mat'] = -0.0324 * row['final_O2_ppm'] + 0.7724 * row['LM_Start_Wt_lf'] + 0.0168 * row['1st_Probe_temp_lf'] + 1.231 * row['Al_Bar_lf'] + 0.0402 * row['Lime_tap'] + -1515.8216 * row['AL_chem_first'] + 1878.593 * row['S_chem_first']
        row['node'] = 1
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] <= 0.046) and (row['S_chem_first'] > 0.02) and (row['final_O2_ppm'] > 980.5):
        row['AL_mat'] = -0.0825 * row['final_O2_ppm'] + 0.8239 * row['LM_Start_Wt_lf'] + 0.0801 * row['1st_Probe_temp_lf'] + 2.2775 * row['Al_Bar_lf'] + -0.0011 * row['Lime_tap'] + -1947.7474 * row['AL_chem_first'] + 2673.3038 * row['S_chem_first']
        row['node'] = 2
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] <= 0.032) and (row['S_chem_first'] > 0.027) and (row['S_chem_first'] <= 0.035):
        row['AL_mat'] = 0.0438 * row['final_O2_ppm'] + 0.6855 * row['LM_Start_Wt_lf'] + 0.3155 * row['1st_Probe_temp_lf'] + -47.4434 * row['Al_Bar_lf'] + 0.0242 * row['Lime_tap'] + 1995.5641 * row['AL_chem_first'] + 2986.0422 * row['S_chem_first']
        row['node'] = 3
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] <= 0.046) and (row['S_chem_first'] <= 0.02) and (row['Lime_tap'] <= 3088.5):
        row['AL_mat'] = 0.0555 * row['final_O2_ppm'] + 0.3062 * row['LM_Start_Wt_lf'] + -0.0246 * row['1st_Probe_temp_lf'] + -0.3171 * row['Al_Bar_lf'] + 0.0154 * row['Lime_tap'] + 746.5366 * row['AL_chem_first'] + 3383.4895 * row['S_chem_first']
        row['node'] = 4
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] <= 0.032) and (row['S_chem_first'] <= 0.027) and (row['final_O2_ppm'] <= 1144.5):
        row['AL_mat'] = 0.0382 * row['final_O2_ppm'] + 0.3324 * row['LM_Start_Wt_lf'] + 0.0252 * row['1st_Probe_temp_lf'] + -10.1441 * row['Al_Bar_lf'] + 0.0239 * row['Lime_tap'] + 920.4385 * row['AL_chem_first'] + 896.9098 * row['S_chem_first']
        row['node'] = 5
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] <= 0.032) and (row['S_chem_first'] > 0.027) and (row['S_chem_first'] > 0.035):
        row['AL_mat'] = 0.0176 * row['final_O2_ppm'] + 0.1702 * row['LM_Start_Wt_lf'] + -0.2343 * row['1st_Probe_temp_lf'] + 22.0835 * row['Al_Bar_lf'] + 0.004 * row['Lime_tap'] + 839.7014 * row['AL_chem_first'] + 1598.1017 * row['S_chem_first']
        row['node'] = 6
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] > 0.046) and (row['Lime_tap'] <= 2927.5) and (row['S_chem_first'] > 0.027):
        row['AL_mat'] = -0.0547 * row['final_O2_ppm'] + 1.4363 * row['LM_Start_Wt_lf'] + -0.089 * row['1st_Probe_temp_lf'] + 2.528 * row['Al_Bar_lf'] + 0.0229 * row['Lime_tap'] + -1716.6099 * row['AL_chem_first'] + 4898.4014 * row['S_chem_first']
        row['node'] = 7
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] > 0.032) and (row['Lime_tap'] > 995.5) and (row['S_chem_first'] <= 0.029):
        row['AL_mat'] = 0.0525 * row['final_O2_ppm'] + -0.5727 * row['LM_Start_Wt_lf'] + -0.5461 * row['1st_Probe_temp_lf'] + 69.4802 * row['Al_Bar_lf'] + 0.0088 * row['Lime_tap'] + 455.8244 * row['AL_chem_first'] + -366.027 * row['S_chem_first']
        row['node'] = 8
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] <= 0.046) and (row['S_chem_first'] > 0.02) and (row['final_O2_ppm'] <= 980.5):
        row['AL_mat'] = -0.2894 * row['final_O2_ppm'] + 1.25 * row['LM_Start_Wt_lf'] + 0.0502 * row['1st_Probe_temp_lf'] + -0.0683 * row['Al_Bar_lf'] + -0.0091 * row['Lime_tap'] + 3294.5118 * row['AL_chem_first'] + 3035.8515 * row['S_chem_first']
        row['node'] = 9
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] <= 0.032) and (row['S_chem_first'] <= 0.027) and (row['final_O2_ppm'] > 1144.5):
        row['AL_mat'] = -0.0417 * row['final_O2_ppm'] + -0.1288 * row['LM_Start_Wt_lf'] + 0.9894 * row['1st_Probe_temp_lf'] + -103.7983 * row['Al_Bar_lf'] + 0.0911 * row['Lime_tap'] + 1693.7519 * row['AL_chem_first'] + 4085.8512 * row['S_chem_first']
        row['node'] = 10
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] > 0.032) and (row['Lime_tap'] <= 995.5) and (row['LM_Start_Wt_lf'] > 185.5):
        row['AL_mat'] = -0.0592 * row['final_O2_ppm'] + 0.5833 * row['LM_Start_Wt_lf'] + 1.1643 * row['1st_Probe_temp_lf'] + -119.9933 * row['Al_Bar_lf'] + 0.0059 * row['Lime_tap'] + 406.2502 * row['AL_chem_first'] + 453.8333 * row['S_chem_first']
        row['node'] = 11
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] > 0.032) and (row['Lime_tap'] > 995.5) and (row['S_chem_first'] > 0.029):
        row['AL_mat'] = -0.95 * row['final_O2_ppm'] + 0.4265 * row['LM_Start_Wt_lf'] + -2.3793 * row['1st_Probe_temp_lf'] + 449.1525 * row['Al_Bar_lf'] + -0.2327 * row['Lime_tap'] + 4141.8124 * row['AL_chem_first'] + -51050.0 * row['S_chem_first']
        row['node'] = 12
    elif (row['Al_Bar_lf'] <= 15.026) and (row['AL_chem_first'] > 0.032) and (row['Lime_tap'] <= 995.5) and (row['LM_Start_Wt_lf'] <= 185.5):
        row['AL_mat'] = 0.1307 * row['final_O2_ppm'] + 5.0999 * row['LM_Start_Wt_lf'] + 0.5949 * row['1st_Probe_temp_lf'] + -133.0633 * row['Al_Bar_lf'] + -0.1308 * row['Lime_tap'] + 4123.9197 * row['AL_chem_first'] + 2242.8091 * row['S_chem_first']
        row['node'] = 13
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] > 0.046) and (row['AL_chem_first'] > 0.046) and (row['Lime_tap'] > 2927.5):
        row['AL_mat'] = -0.891 * row['final_O2_ppm'] + -2.3266 * row['LM_Start_Wt_lf'] + 1.5258 * row['1st_Probe_temp_lf'] + 13.1046 * row['Al_Bar_lf'] + -0.2811 * row['Lime_tap'] + 603.2872 * row['AL_chem_first'] + -5683.1937 * row['S_chem_first']
        row['node'] = 14
    elif (row['Al_Bar_lf'] > 15.026) and (row['AL_chem_first'] <= 0.046) and (row['S_chem_first'] <= 0.02) and (row['Lime_tap'] > 3088.5):
        row['AL_mat'] = 0.5715 * row['final_O2_ppm'] + 0.4728 * row['LM_Start_Wt_lf'] + 0.2037 * row['1st_Probe_temp_lf'] + 8.4861 * row['Al_Bar_lf'] + -0.1905 * row['Lime_tap'] + -10340.0 * row['AL_chem_first'] + -9121.9165 * row['S_chem_first']
        row['node'] = 15
    else:
#         print("weak node")
        row['node'] = 0
        row['AL_mat'] = (10.0 * (row['LM_Start_Wt_lf'] + 1) * (al_lsl - row['AL_chem_first'] + 16 * fade_rate ))/0.6

    return [row['AL_mat'], row['node'], row['Oxygen Node']]

######################## End Code ###########################################
