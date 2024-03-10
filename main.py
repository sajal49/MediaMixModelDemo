from MMM.OutDetect.lof import identify_outlier
from MMM.DataComms.read_data import return_data

def main():

    path = "Data/MMM_SIM_SMRTPHN_STRTUP_COMPANY.csv"
    X = return_data(path)
    y = identify_outlier(X=X, colnm=['Meta_Impressions', 'Youtube_Impressions'])
    print(y)

main()