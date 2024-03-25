

def U_ratio_calculate(Bed_Distance): 

  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import math


  #data = pd.read_csv('average_max_result.txt',sep='\s+',header=None)
  data_bottom = pd.read_csv('prob_bottom.csv')

  data_bottom = pd.DataFrame(data_bottom)

  data_mid = pd.read_csv('prob_mid.csv')

  data_mid = pd.DataFrame(data_mid)

  data_up = pd.read_csv('prob_up.csv')

  data_up = pd.DataFrame(data_up)
  
  
  data_0 = pd.read_csv('prob_0.csv')

  data_0 = pd.DataFrame(data_0)



  U_mag_bottom =data_bottom['U_Magnitude']
  U_x_bottom =data_bottom['U_0']
  U_y_bottom =data_bottom['U_1']
  U_z_bottom =data_bottom['U_2']

  U_mag_mid =data_mid['U_Magnitude']
  U_x_mid =data_mid['U_0']
  U_y_mid =data_mid['U_1']
  U_z_mid =data_mid['U_2']

  U_mag_up =data_up['U_Magnitude']
  U_x_up =data_up['U_0']
  U_y_up =data_up['U_1']
  U_z_up =data_up['U_2']
  
  
  U_mag_0 =data_0['U_Magnitude']
  U_x_0 =data_0['U_0']
  U_y_0 =data_0['U_1']
  U_z_0 =data_0['U_2']


  U_mag_up_to_bot=float(U_mag_up/U_mag_bottom)
  U_mag_up_to_mid=float(U_mag_up/U_mag_mid)
  U_mag_mid_to_bot=float(U_mag_mid/U_mag_bottom)

  U_x_up_to_bot=float(U_x_up/U_x_bottom)
  U_x_up_to_mid=float(U_x_up/U_x_mid)
  U_x_mid_to_bot=float(U_x_mid/U_x_bottom)

  U_y_up_to_bot=float(U_y_up/U_y_bottom)
  U_y_up_to_mid=float(U_y_up/U_y_mid)
  U_y_mid_to_bot=float(U_y_mid/U_y_bottom)

  U_z_up_to_bot=float(U_z_up/U_mag_bottom)
  U_z_up_to_mid=float(U_z_up/U_mag_mid)
  U_z_mid_to_bot=float(U_z_mid/U_mag_bottom)
  
  
  direct_velocity_up = math.atan(U_z_up/U_x_up)*(180/math.pi)
  direct_velocity_mid = math.atan(U_z_mid/U_x_mid)*(180/math.pi)
  direct_velocity_bottom = math.atan(U_z_bottom/U_x_bottom)*(180/math.pi)


  file_name_U_mag="../prob_U_ratio/U_mag_ratio"+str(Bed_Distance)+".txt"

  file = open (file_name_U_mag, "a")
  #file.write ("U_mag_up_to_bot U_mag_up_to_mid U_mag_mid_to_bot\n")
  file.write ("{}\t{}\t{} \n".format(U_mag_up_to_bot, U_mag_up_to_mid, U_mag_mid_to_bot))

  file.close()


  file_name_U_x="../prob_U_ratio/U_x_ratio"+str(Bed_Distance)+".txt"

  file = open (file_name_U_x, "a")
  #file.write ("U_mag_up_to_bot U_mag_up_to_mid U_mag_mid_to_bot\n")
  file.write ("{}\t{}\t{} \n".format(U_x_up_to_bot, U_x_up_to_mid, U_x_mid_to_bot))

  file.close()

  file_name_U_y="../prob_U_ratio/U_y_ratio"+str(Bed_Distance)+".txt"

  file = open (file_name_U_y, "a")
  #file.write ("U_mag_up_to_bot U_mag_up_to_mid U_mag_mid_to_bot\n")
  file.write ("{}\t{}\t{} \n".format(U_y_up_to_bot, U_y_up_to_mid, U_y_mid_to_bot))

  file.close()

  file_name_U_z="../prob_U_ratio/U_z_ratio"+str(Bed_Distance)+".txt"

  file = open (file_name_U_z, "a")
  #file.write ("U_mag_up_to_bot U_mag_up_to_mid U_mag_mid_to_bot\n")
  file.write ("{}\t{}\t{} \n".format(U_z_up_to_bot, U_z_up_to_mid, U_z_mid_to_bot))
  
  
  file.close()
  
  
  
  
  file_name_U_direct="../prob_U_ratio/U_direct"+str(Bed_Distance)+".txt"

  file = open (file_name_U_direct, "a")
  
  file.write ("{}\t{}\t{} \n".format(direct_velocity_up, direct_velocity_mid, direct_velocity_bottom))

  file.close()
  
  
  file_name_U_0="../prob_U_ratio/U_0-"+str(Bed_Distance)+".txt"

  file = open (file_name_U_0, "a")
  
  file.write ("{}\t{}\t{} \n".format(float(U_mag_0), float(U_x_0), float(U_z_0)))

  file.close()
  
  
  

  #-----------------------------write in excel file ------------------------------
  #import csv

  #df2 = pd.DataFrame([[U_z_up_to_bot,U_z_up_to_mid,U_z_mid_to_bot]], columns=['U_mag_up_to_bot', 'U_mag_up_to_mid', 'U_mag_mid_to_bot'])

  #df2.to_excel('../prob_U_ratio/U_ratio_excel.xlsx', sheet_name='new_sheet_name')

  #df2.to_csv ("../prob_U_ratio/U_ratio_excel.csv", index = None, header=True)




