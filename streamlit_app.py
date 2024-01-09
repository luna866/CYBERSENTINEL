
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Charger le modèle
id=1
clf = joblib.load('D:\CYBERSENTINEL\ML\LABEL\modelcode.pkl')

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# Charger le modèle
id=1
clf = joblib.load('D:\CYBERSENTINEL\ML\LABEL\modelcode.pkl')

# Définir le titre et la page
st.set_page_config(page_title='CYBERSENTINEL', page_icon='🔒', layout='wide')
st.title("Détecteur d'intrusion")

# Insérer une image
st.image('D:\M2i\RNCP\RNCP_CDC\LogoCybersentinel\logopetit.png')

#  Créer des widgets pour recueillir de nouvelles données
srcip = st.text_input('srcip')
sport = st.number_input('sport', min_value=0)
dstip = st.text_input('dstip')
dsport = st.number_input('dsport')
proto = st.selectbox('proto', ['udp', 'arp', 'tcp', 'ospf', 'icmp', 'igmp', 'sctp', 'udt', 'sep', 'sun-nd', 'swipe', 'mobile', 'pim', 'rtp', 'ipnip', 'ip', 'ggp', 'st2', 'egp', 'cbt', 'emcon', 'nvp', 'igp', 'xnet', 'argus', 'bbn-rcc', 'chaos', 'pup', 'hmp', 'mux', 'dcn', 'prm', 'trunk-1', 'xns-idp', 'trunk-2', 'leaf-1', 'leaf-2', 'irtp', 'rdp', 'iso-tp4', 'netblt', 'mfe-nsp', 'merit-inp', '3pc', 'xtp', 'idpr', 'tp++', 'ddp', 'idpr-cmtp', 'ipv6', 'il', 'idrp', 'ipv6-frag', 'sdrp', 'ipv6-route', 'gre', 'rsvp', 'mhrp', 'bna', 'esp', 'i-nlsp', 'narp', 'ipv6-no', 'tlsp', 'skip', 'ipv6-opts', 'any', 'cftp', 'sat-expak', 'kryptolan', 'rvd', 'ippc', 'sat-mon', 'ipcv', 'visa', 'cpnx', 'cphb', 'wsn', 'pvp', 'br-sat-mon', 'wb-mon', 'wb-expak', 'iso-ip', 'secure-vmtp', 'vmtp', 'vines', 'ttp', 'nsfnet-igp', 'dgp', 'tcf', 'eigrp', 'sprite-rpc', 'larp', 'mtp', 'ax.25', 'ipip', 'micp', 'aes-sp3-d', 'encap', 'etherip', 'pri-enc', 'gmtp', 'pnni', 'ifmp', 'aris', 'qnx', 'a/n', 'scps', 'snp', 'ipcomp', 'compaq-peer', 'ipx-n-ip', 'vrrp', 'zero', 'pgm', 'iatp', 'ddx', 'l2tp', 'srp', 'stp', 'smp', 'uti', 'sm', 'ptp', 'fire', 'crtp', 'isis', 'crudp', 'sccopmce', 'sps', 'pipe', 'iplt', 'unas', 'fc', 'ib'])
state = st.selectbox('state', ['CON', 'INT', 'FIN', 'URH', 'REQ', 'ECO', 'RST', 'CLO', 'TXD', 'URN', 'no', 'ACC', 'PAR', 'MAS', 'TST', 'ECR'])
dur = st.number_input('dur', min_value=0)
dbytes = st.number_input('dbytes')
sttl = st.number_input('sttl')
dttl = st.number_input('dttl')
sloss = st.number_input('sloss')
service = st.selectbox('service', ['-', 'dns', 'http', 'smtp', 'ftp-data', 'ftp', 'ssh', 'pop3', 'snmp', 'ssl', 'irc','radius', 'dhcp'])
sload = st.number_input('sload')
dload = st.number_input('dload')
spkts = st.number_input('spkts')
swin = st.number_input('swin')
stcpb = st.number_input('stcpb')
dtcpb = st.number_input('dtcpb')
smeansz = st.number_input('smeansz')
dmeansz = st.number_input('dmeansz')
trans_depth = st.number_input('trans_depth')
res_bdy_len = st.number_input('res_bdy_len')
sjit = st.number_input('sjit')
djit = st.number_input('djit')
stime = st.number_input('stime')
ltime = st.number_input('ltime')
sintpkt = st.number_input('sintpkt')
dintpkt = st.number_input('dintpkt')
synack = st.number_input('synack')
ackdat = st.number_input('ackdat')
is_sm_ips_ports = st.selectbox('is_sm_ips_ports', [0,1])
ct_state_ttl = st.number_input('ct_state_ttl')
ct_flw_http_mthd = st.number_input('ct_flw_http_mthd')
is_ftp_login = st.number_input('is_ftp_login')
ct_ftp_cmd = st.selectbox('ct_ftp_cmd', [0, 1, 6, 2, 4, 8, 5, 3])
ct_srv_src = st.number_input('ct_srv_src')

# Créer un dataframe avec les nouvelles données
new_data = pd.DataFrame(
    data=np.array([[srcip, sport, dstip, dsport, proto, state,
       dur, dbytes, sttl, dttl, sloss, service, sload, dload,
       spkts, swin, stcpb, dtcpb, smeansz, dmeansz, trans_depth,
       res_bdy_len, sjit, djit, stime, ltime, sintpkt, dintpkt,
       synack, ackdat, is_sm_ips_ports, ct_state_ttl,
       ct_flw_http_mthd, is_ftp_login, ct_ftp_cmd, ct_srv_src]]),
    columns=['srcip', 'sport', 'dstip', 'dsport', 'proto', 'state',
       'dur', 'dbytes', 'sttl', 'dttl', 'sloss', 'service', 'sload', 'dload',
       'spkts', 'swin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz', 'trans_depth',
       'res_bdy_len', 'sjit', 'djit', 'stime', 'ltime', 'sintpkt', 'dintpkt',
       'synack', 'ackdat', 'is_sm_ips_ports', 'ct_state_ttl',
       'ct_flw_http_mthd', 'is_ftp_login', 'ct_ftp_cmd', 'ct_srv_src'])

# Charger les données d'entraînement
train = pd.read_csv(r'D:\CYBERSENTINEL\ML\reste.csv')

# Sélectionner uniquement les colonnes numériques
numeric_columns = train.select_dtypes(include=[np.number])

# Calculer les valeurs médianes
median_values = numeric_columns.median()

# Créer le bouton
if st.button('Remplir avec les valeurs médianes'):
    sport = st.number_input('sport', value=int(median_values['sport']))
    dur = st.number_input('dur', value=median_values['dur'])
    dbytes = st.number_input('dbytes', value=int(median_values['dbytes']))
    sttl = st.number_input('sttl', value=int(median_values['sttl']))
    dttl = st.number_input('dttl', value=int(median_values['dttl']))
    sloss = st.number_input('sloss', value=int(median_values['sloss']))
    sload = st.number_input('sload', value=median_values['sload'])
    dload = st.number_input('dload', value=median_values['dload'])
    spkts = st.number_input('spkts', value=int(median_values['spkts']))
    swin = st.number_input('swin', value=int(median_values['swin']))
    stcpb = st.number_input('stcpb', value=int(median_values['stcpb']))
    dtcpb = st.number_input('dtcpb', value=int(median_values['dtcpb']))
    smeansz = st.number_input('smeansz', value=int(median_values['smeansz']))
    dmeansz = st.number_input('dmeansz', value=int(median_values['dmeansz']))
    trans_depth = st.number_input('trans_depth', value=int(median_values['trans_depth']))
    res_bdy_len = st.number_input('res_bdy_len', value=int(median_values['res_bdy_len']))
    sjit = st.number_input('sjit', value=median_values['sjit'])
    djit = st.number_input('djit', value=median_values['djit'])
    stime = st.number_input('stime', value=int(median_values['stime']))
    ltime = st.number_input('ltime', value=int(median_values['ltime']))
    sintpkt = st.number_input('sintpkt', value=median_values['sintpkt'])
    dintpkt = st.number_input('dintpkt', value=median_values['dintpkt'])
    synack = st.number_input('synack', value=median_values['synack'])
    ackdat = st.number_input('ackdat', value=median_values['ackdat'])
    is_sm_ips_ports = st.number_input('is_sm_ips_ports', value=int(median_values['is_sm_ips_ports']))
    ct_state_ttl = st.number_input('ct_state_ttl', value=int(median_values['ct_state_ttl']))
    ct_flw_http_mthd = st.number_input('ct_flw_http_mthd', value=int(median_values['ct_flw_http_mthd']))
    is_ftp_login = st.number_input('is_ftp_login', value=int(median_values['is_ftp_login']))
    ct_ftp_cmd = st.number_input('ct_ftp_cmd', value=int(median_values['ct_srv_src']))
    ct_srv_src = st.number_input('ct_srv_src', value=int(median_values['ct_srv_src']))

# Faire une prédiction
if st.button("Predict"):
    prediction = clf.predict(new_data)
    # Afficher la prédiction
    st.write(f'La prédiction est : {prediction}')
