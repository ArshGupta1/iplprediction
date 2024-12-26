import streamlit as st
import pandas as pd
import pickle

teams=[
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities=['hyderabaad','Bangalore','Mumbai','Indore','Kolkata','Delhi','Chandigarh','Jaipur','Chennai','Cape town','port elizabeth','Durban','Centurion','East london','Johannesburg','Kimberley','Bloemfontein','Ahemdabad','Cuttack','Nagpur','Dharamsala',
        'Visakhapatnam','pune','Raipur','Ranchi','Abu Dhabi','Sharjah','Mohali','Bengaluru']

pipe=pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1,col2=st.columns(2)

with col1:
    battingteam=st.selectbox('Select the batting team',sorted(teams))

with col2:
    bowlingteam=st.selectbox('bowling team',sorted(teams))

city=st.selectbox('city',sorted(cities))

target=st.number_input('target')

col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input('scores')

with col4:
    overs=st.number_input('Overs')

with col5:
    wickets=st.number_input('wickets')

if st.button('predict'):

    runs_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wickets
    currentrunrate=score/overs
    requiredrunrate=(runs_left*6)/balls_left

    input_df=pd.DataFrame({'batting_team':[battingteam],'bowling_team':[bowlingteam],'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'curr_run_rate':[currrentrunrate],'req_run_rate':[requiredrunrate]})

    result=pipe.predict_proba(input_df)
    lossprob=result[0][0]
    winprob=result[0][1]

    st.header(battingteam+"- "+str(round(winprob*100))+"%")
    st.header(bowlingteam+"- "+str(round(lossprob*100))+"%")
