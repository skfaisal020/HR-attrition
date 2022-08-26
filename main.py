import streamlit as st
import numpy as np
import time
import pickle
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

pickle_in = open('employee1.pkl', "rb")
dec_cl = pickle.load(pickle_in)

st.title('HR Attrition')

# adding image
st.image("images (1).png",width = 700)
# adding sidebar


st.header("Know employe attrition")
#Age	EnvironmentSatisfaction	JobInvolvement	MonthlyIncome	NumCompaniesWorked	TotalWorkingYears	YearsAtCompany	Department_Research & Development	Department_Sales	Gender_Male	MaritalStatus_Married	MaritalStatus_Single	JobRole_Human Resources	JobRole_Laboratory Technician	JobRole_Manager	JobRole_Manufacturing Director	JobRole_Research Director	JobRole_Research Scientist	JobRole_Sales Executive	JobRole_Sales Representative
Age = st.slider("enter your age ", 0, 100)
EnvironmentSatisfaction = st.selectbox('EnvironmentSatisfaction', ['1', '2', '3', '4'])
JobInvolvement = st.selectbox('JobInvolvement', ['1', '2', '3', '4'])
MonthlyIncome = st.number_input("Enter your MonthlyIncome", 0.00, 1000000.00, step=2000.0)
NumCompaniesWorked = st.slider("Number of Companies Worked ", 0, 10)
TotalWorkingYears= st.slider("Total Working Years ", 0, 40)
YearsAtCompany = st.slider("YearsAtCompany", 0, 80)

Department = ['Research & Development', 'Sales']
Department1 = st.selectbox('Department', Department)

Gender=['Male','Female']
Gender1=st.selectbox('Gender',Gender)

MaritalStatus = ['Married', 'Single']
MaritalStatus1 = st.selectbox('Marital Status', MaritalStatus)

JobRole = ['Research Scientist','Sales Executive','Laboratory Technician','Manufacturing Director','Healthcare Representative','Manager','Sales Representative','Research Director','Human Resources']
JobRole1=st.selectbox("Job Role",JobRole)





cat_list = ['r_d', 'sales','m','f','mr','s','rs','se','lt','md','hr','mn','sr','rd','hr_h']
for i in cat_list:
    exec("%s = %d" % (i, 0))

r_d=0
sales=0
m=0
f=0
mr=0
s=0
rs=0
se=0
lt=0
md=0
hr=0
mn=0
sr=0
rd=0
hr_h=0




if Department == 'Research & Development':
    r_d= 1
elif Department == 'Sales':
    sales = 1
else:
    pass

if Gender == 'Male':
    m = 1
elif Gender == 'Female':
    m = 0
else:
    pass


if MaritalStatus == 'Married':
    mr = 1
elif MaritalStatus == 'Single':
    s = 1
else:
    pass

if JobRole=='Research Scientist':
    rs=1
elif JobRole== 'Sales Executive':
    se=1
elif JobRole== 'Laboratory Technician':
    lt=1
elif JobRole=='Manufacturing Director':
    md=1
elif JobRole=='Healthcare Representative':
    rs=0
    se=0
    lt=0
    md=0
    mn=0
    sr=0
    rd=0
    hr_h=0
elif JobRole=='Manager':
    mn=1
elif JobRole=='Sales Representative':
    sr=1
elif JobRole=='Research Director':
    rd=1
elif JobRole=='Human Resources':
    hr_h=1
else:
    pass

if st.button("Predict"):
    val = np.asarray(
        [Age,EnvironmentSatisfaction,JobInvolvement,MonthlyIncome,NumCompaniesWorked,TotalWorkingYears,YearsAtCompany,
         r_d,sales,m,mr,s,rs,se,lt,md,mn,sr,rd,hr_h]).reshape(1, -1)
    pred = dec_cl.predict(val)

    progress = st.progress(0)  # this is for progress bar
    for i in range(100):
        time.sleep(0.001)
        progress.progress(i + 1)

    if pred == 0:
        st.write('***The Employee will not Leave The Company***')
    else:
        st.write('***The Employee will Leave The Company***')







