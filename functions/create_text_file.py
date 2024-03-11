import io
node_mapping = {
    "SMSC/SMSR": "SM",
    "GCS": "GC",
    "GMSC": "GM",
    "HLR": "HL",
    "IN/SCP": "IN",
    "SGSN": "SG",
    "CMM": "CM",
    "MSC": "MC",
    "MSS": "MS",
    "PR/RTSP": "PR/RT",
    "USSD": "US",
    "EIR": "EI",
    "SRS": "SR",
    "FIREWALL": "FW",
    "IPS": "IP",
    "SCL": "SC",
    "VHE": "VH",
    "STP": "ST",
    "IRTMS": "IR",
    "CCN": "CN",
    "NGN": "SS",
    "UCC": "UC",
    "RECC": "RE",
    "LBS": "LB",
    "CDR": "CD",
    "FM/SIS": "FM",
    "MNP": "MN",
    "LDAP": "LD",
    "Test Bed STP": "TB",
    "Test SMSC": "TS",
    "Test IN": "TI",
    "Test HLR": "TH",
    "Test MSC": "TM",
    "Test CCN": "TC",
    "Test SGSN": "TG",
    "Welcome Handler Server/Roamware": "WS",
    "Tanla SMSC": "TN",
    "SINCH SMSC": "SN",
    "Telenity SMSC": "TE",
    "Prudent SMSC": "PD",
    "RML SMSC FW": "RS",
    "RML ILD HUB": "RH",
    "Enterprise SMSC": "ES",
    "Comviva SMSC": "CV",
    "Teledna SMSC": "TD",
    "CMS One97 Voice mail": "VO",
    "BSMART": "BS",
    "NT HLR": "NT",
    "DSR": "DS",
    "SDS": "SS",
    "PCC": "PC",
    "TAS": "TA/TS",
    "SGU": "SU",
    "SDC": "SD",
    "VMS": "VM",
    "SDP": "SP",
    "AIR": "AR",
    "BC": "BC",
    "SOFTX": "SX",
    "TEST AIR": "TR",
    "TEST SDP": "TP",
    "Ieocn": "EC",
    "SMSC HUB": "HB",
    "PRUTECH SERVER": "PS",
    "IVR": "IV",
    "DSA Server": "DA",
    "sICR": "IC",
    "WIFI Server": "WF",
    "SS7 FW Node": "SF",
    "CLI Spoofing IODB": "CS"
}

circle_mapping = {
    "DELHI": "DEL",
    "PUNJAB": "PUN",
    "HARYANA": "HAR",
    "RAJASTHAN": "RAJ",
    "UP WEST": "UPW",
    "MAHARASHTRA": "MAH",
    "MUMBAI": "MUM",
    "GUJARAT": "GUJ",
    "UP EAST": "UPE",
    "KOLKATA": "KOL",
    "WEST BENGAL": "WBL",
    "KERALA": "KEL",
    "CHENNAI": "CHN",
    "TAMIL NADU": "TMN",
    "KARNATAKA": "KAR",
    "ANDHRA PRADESH": "APR",
    "HIMACHAL PRADESH": "HPR",
    "ORISSA": "ORS",
    "ASSAM": "ASM",
    "NORTH EAST": "NES",
    "J&K": "JNK",
    "MADHYA PRADESH": "MPC",
    "BIHAR": "BIH",
    "Singapore Tanla": "TAN",
    "Singapore": "SGP",
    "BELGACOM": "BIC",
    "Spain Madrid": "SPM",
    "Spain Barcelona": "SPB",
    "France Telecom Paris": "FRP",
    "France Telecom": "FRR"
}


secondary_route_mapping = {
    "RAJ": "vpunst01i3",
    "NTD": "vkolstn2i3",
    "NTK": "vdelstn2i3",
    "PNB": "vrajst01i3",
    "ROB": ["vasmst02i3", "vkolst04i3"],
    "UPE": "vbihs002i3",
    "UPW": "vdelst01i3",
    "ASM": "vwblst02i3",
    "BIH": "vupest02i3",
    "CHN": "vkelstr1i3",
    "DEL": "vupwst01i3",
    "GUJ": "vmpcst02i3",
    "HYD": "vkarst02i3",
    "KAR": "vaprst02i3",
    "KEL": "vchnstr1i3",
    "KOL": "vwblst02i3",
    "MAH": "vmumst02i3",
    "MP": "vgujst02i3",
    "MUM": "vmahst05i3",
    "NTC": "vmumstn1i3"
}

reverse_circle_mapping = {
    'DEL': 'DELHI',
    'PUN': 'PUNJAB',
    'HAR': 'HARYANA',
    'RAJ': 'RAJASTHAN',
    'UPW': 'UP WEST',
    'MAH': 'MAHARASHTRA',
    'MUM': 'MUMBAI',
    'GUJ': 'GUJARAT',
    'UPE': 'UP EAST',
    'KOL': 'KOLKATA',
    'WBL': 'WEST BENGAL',
    'KEL': 'KERALA',
    'CHN': 'CHENNAI',
    'TMN': 'TAMIL NADU',
    'KAR': 'KARNATAKA',
    'APR': 'ANDHRA PRADESH',
    'HPR': 'HIMACHAL PRADESH',
    'ORS': 'ORISSA',
    'ASM': 'ASSAM',
    'NES': 'NORTH EAST',
    'JNK': 'J&K',
    'MPC': 'MADHYA PRADESH',
    'BIH': 'BIHAR',
    'TAN': 'Singapore Tanla',
    'SGP': 'Singapore',
    'BIC': 'BELGACOM',
    'SPM': 'Spain Madrid',
    'SPB': 'Spain Barcelona',
    'FRP': 'France Telecom Paris',
    'FRR': 'France Telecom'
}

reverse_node_mapping = {
    'SM': 'SMSC/SMSR',
    'GC': 'GCS',
    'GM': 'GMSC',
    'HL': 'HLR',
    'IN': 'IN/SCP',
    'SG': 'SGSN',
    'CM': 'CMM',
    'MC': 'MSC',
    'MS': 'MSS',
    'PR/RT': 'PR/RTSP',
    'US': 'USSD',
    'EI': 'EIR',
    'SR': 'SRS',
    'FW': 'FIREWALL',
    'IP': 'IPS',
    'SC': 'SCL',
    'VH': 'VHE',
    'ST': 'STP',
    'IR': 'IRTMS',
    'CN': 'CCN',
    'SS': 'SDS',
    'UC': 'UCC',
    'RE': 'RECC',
    'LB': 'LBS',
    'CD': 'CDR',
    'FM': 'FM/SIS',
    'MN': 'MNP',
    'LD': 'LDAP',
    'TB': 'Test Bed STP',
    'TS': 'Test SMSC',
    'TI': 'Test IN',
    'TH': 'Test HLR',
    'TM': 'Test MSC',
    'TC': 'Test CCN',
    'TG': 'Test SGSN',
    'WS': 'Welcome Handler Server/Roamware',
    'TN': 'Tanla SMSC',
    'SN': 'SINCH SMSC',
    'TE': 'Telenity SMSC',
    'PD': 'Prudent SMSC',
    'RS': 'RML SMSC FW',
    'RH': 'RML ILD HUB',
    'ES': 'Enterprise SMSC',
    'CV': 'Comviva SMSC',
    'TD': 'Teledna SMSC',
    'VO': 'CMS One97 Voice mail',
    'BS': 'BSMART',
    'NT': 'NT HLR',
    'DS': 'DSR',
    'PC': 'PCC',
    'TA/TS': 'TAS',
    'SU': 'SGU',
    'SD': 'SDC',
    'VM': 'VMS',
    'SP': 'SDP',
    'AR': 'AIR',
    'BC': 'BC',
    'SX': 'SOFTX',
    'TR': 'TEST AIR',
    'TP': 'TEST SDP',
    'EC': 'Ieocn',
    'HB': 'SMSC HUB',
    'PS': 'PRUTECH SERVER',
    'IV': 'IVR',
    'DA': 'DSA Server',
    'IC': 'sICR',
    'WF': 'WIFI Server',
    'SF': 'SS7 FW Node',
    'CS': 'CLI Spoofing IODB'
}


def get_val(circle_card, col):
    
    import sqlite3

    # Connect to your SQLite database
    conn = sqlite3.connect('card_database.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Example: Deleting rows from the 'example' table based on a condition
    cursor.execute("SELECT "+str(col)+" FROM cards WHERE new_column3 = ?", (circle_card,))
    
    val = cursor.fetchall()
    
    res = val[0][0]

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    return res

def create_text_file(new_df, number_of_linksets, DPC, params_df):
    output_file = io.StringIO()
    
    temp = params_df["DPC Name"].astype(str).str.upper().str.strip().str[:3]
    circle = reverse_circle_mapping.get(temp.iloc[0]) if not temp.empty else None

    temp = params_df["LSET_NAME"].astype(str).str.upper().str.strip().str[4:6]
    node = reverse_node_mapping.get(temp.iloc[0]) if not temp.empty else None
    
    sub_heading = "DPC & LSN"
    
    line1 = "ent-dstn:dpcn="+str(DPC)+":clli="+str(params_df["DPC Name"][0])
    line2 = "ent-ls:lst=a:adapter=m3ua:slktps="+str(params_df["TPS"][0])+":lsn="+str(params_df["LSET_NAME"][0])+":apcn="+str(DPC)+":ipsg=yes"
    line3 = "chg-ls:lsn="+str(params_df["LSET_NAME"][0])+":maxslktps=9500"
    line4 = "chg-ls:lsn="+str(params_df["LSET_NAME"][0])+":rcontext="+str(params_df["Routing Context"][0])
    
    output_file.write("------------------------"+sub_heading+"------------------------"+"\n")
    output_file.write("\n")
    output_file.write(line1+"\n")
    output_file.write(line2+"\n")
    output_file.write(line3+"\n")
    output_file.write(line4+"\n")
    output_file.write("\n")
    output_file.write("===========================================================================================" +"\n" )
    output_file.write("\n")
    

    for i in range(0, number_of_linksets):
    
        sub_heading = "IP Route for SLC:"+str(i)
        value1 = "ent-ip-rte:submask=255.255.255.255:loc=" + str(new_df["CARD"][i]) + ":dest=" + str(new_df["REM_IP1"][i]) + ":gtwy=" + str(get_val((str(params_df["Select STP"][0])+str(new_df["CARD"][i])), "GATEWAY_1"))
        value2 = "ent-ip-rte:submask=255.255.255.255:loc=" + str(new_df["CARD"][i]) + ":dest=" + str(new_df["REM_IP2"][i]) + ":gtwy=" + str(get_val((str(params_df["Select STP"][0])+str(new_df["CARD"][i])), "GATEWAY_2"))
        output_file.write("------------------------"+sub_heading+"------------------------"+"\n")
        output_file.write("\n")
        output_file.write(value1+"\n")
        output_file.write(value2+"\n")
        output_file.write("\n")
    

    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")


    for i in range(0, number_of_linksets):
    
        sub_heading = "IP Host for SLC:"+str(i)
        value1 = "ent-ip-host:host="+str(circle_mapping[circle].lower()+"."+node_mapping[node].lower()+"."+str(new_df["REM_IP1"][i]))+":ipaddr="+str(new_df["REM_IP1"][i])+":type=remote"
        value2 = "ent-ip-host:host="+str(circle_mapping[circle].lower()+"."+node_mapping[node].lower()+"."+str(new_df["REM_IP2"][i]))+":ipaddr="+str(new_df["REM_IP2"][i])+":type=remote"
      
        output_file.write("------------------------"+sub_heading+"------------------------"+"\n")
        output_file.write("\n")
        output_file.write(value1+"\n")
        output_file.write(value2+"\n")
        output_file.write("\n")


    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")


    for i in range(0, number_of_linksets):
    
        sub_heading = "Assoc:"+str(i)
        value1 = "ent-assoc:aname="+str(new_df["ASSOC_NAME"][i])+":lhost="+str(get_val((str(params_df["Select STP"][0])+str(new_df["CARD"][i])), "PRIMARY_IP_HOST"))+":rhost="+str(circle_mapping[circle].lower()+"."+node_mapping[node].lower()+"."+str(new_df["REM_IP1"][i]))+":lport="+str(new_df["STP_PORT"][i])+":rport="+str(new_df["REM_PORT"][i])+":adapter=m3ua"
        value2 = "chg-assoc:aname="+str(new_df["ASSOC_NAME"][i])+":alhost="+str(get_val((str(params_df["Select STP"][0])+str(new_df["CARD"][i])), "SECONDARY_IP_HOST"))+""
        value3 = "chg-assoc:aname="+str(new_df["ASSOC_NAME"][i])+":rhosttype=alternate:rhost="+str(circle_mapping[circle].lower()+"."+node_mapping[node].lower()+"."+str(new_df["REM_IP2"][i]))+""
        value4 = "chg-assoc:aname="+str(new_df["ASSOC_NAME"][i])+":rtxthr=65535"

        output_file.write(sub_heading+"\n")
        output_file.write("\n")
        output_file.write(value1+"\n")
        output_file.write(value2+"\n")
        output_file.write(value3+"\n")
        output_file.write(value4+"\n")
        output_file.write("\n")

    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")
        
        
    for i in range(0, number_of_linksets):
    
        sub_heading = "SLk:"+str(i)
        value1 = "ent-slk:loc="+str(new_df["CARD"][i])+":link=A1:aname="+str(new_df["ASSOC_NAME"][i])+":lsn="+str(params_df["LSET_NAME"][0])+":slc="+str(new_df["SLC"][i])+""
        
        output_file.write(sub_heading+"\n")
        output_file.write("\n")
        output_file.write(value1+"\n")
        output_file.write("\n")
    
    
    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")

    sub_heading = "Primary Route"
    value1 = "ent-rte:rc=10:dpcn="+str(DPC)+":lsn="+str(params_df["LSET_NAME"][0])

    output_file.write("------------------------"+sub_heading+"------------------------"+"\n")
    output_file.write("\n")
    output_file.write("\n")
    output_file.write(value1+ "\n")


    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")
   

    sub_heading = "Secondary Route"
    value1 = "ent-rte:rc=20:dpcn="+str(DPC)+":lsn="+str(secondary_route_mapping[str(params_df["Select STP"][0])])


    output_file.write("------------------------"+sub_heading+"------------------------"+"\n")
    output_file.write("\n")
    output_file.write("\n")
    output_file.write(value1+"\n")


    output_file.write("==========================================================================================="+"\n")
    output_file.write("\n")
    
    return output_file.getvalue()