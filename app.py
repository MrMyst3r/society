import streamlit as st

pos = 0
neg = 0
st.markdown(
    f"""
    <style>
        .centered-text {{
            text-align: center;
        }}
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown("<h1 class='centered-text'>개인정보 안전성 검사 사이트</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='centered-text'>창원 중앙고 10921 이현수 개발</h1>", unsafe_allow_html=True)

checkbox_sys = st.checkbox('개인정보 처리 시스템을 운영 중인가요?')	
if checkbox_sys:
    pos += 96.6
else:
    neg += 3.4

checkbox_sec = st.checkbox('개인정보의 안전한 관리를 위해 별도의 안정성 확보조치가 있나요?')	
if checkbox_sec:
    pos += 57.4
else:
    neg += 42.6
    

pos_acc = pos/(pos+neg)*100
neg_acc = neg/(pos+neg)*100 
st.write(f'## **당신의 개인정보는 <span style="color: red;">{pos_acc}%</span>의 확률로 안전하게 이용되고 있으며,**', unsafe_allow_html=True)
st.write(f'## **<span style="color: red;">{neg_acc}%</span>%의 확률로 불안전하게 이용되고 있습니다.**', unsafe_allow_html=True)
st.write('인공지능 모델을 만드려 했지만, 저희 주제가 다루듯이 인공지능 학습용 데이터가 부족하여 모델을 구현하진 못했습니다....ㅠㅠ')
st.write('이 사이트는 파이썬으로 개발되었으며, 위 수치는 현재 개인정보보호에 관한 kosis국가 통계의 정보를 바탕으로 계산된 수치입니다.')

code = '''import streamlit as st

pos = 0
neg = 0
st.markdown(
    f"""
    <style>
        .centered-text {{
            text-align: center;
        }}
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown("<h1 class='centered-text'>개인정보 안전성 검사 사이트</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='centered-text'>창원 중앙고 10921 이현수 개발</h1>", unsafe_allow_html=True)

checkbox_sys = st.checkbox('개인정보 처리 시스템을 운영 중인가요?')	
if checkbox_sys:
    pos += 96.6
else:
    neg += 3.4

checkbox_sec = st.checkbox('개인정보의 안전한 관리를 위해 별도의 안정성 확보조치가 있나요?')	
if checkbox_sec:
    pos += 57.4
else:
    neg += 42.6
    

pos_acc = pos/(pos+neg)*100
neg_acc = neg/(pos+neg)*100 
st.write(f'## **당신의 개인정보는 <span style="color: red;">{pos_acc}%</span>의 확률로 안전하게 이용되고 있으며,**', unsafe_allow_html=True)
st.write(f'## **<span style="color: red;">{neg_acc}%</span>%의 확률로 불안전하게 이용되고 있습니다.**', unsafe_allow_html=True)
st.write('인공지능 모델을 만드려 했지만, 저희 주제가 다루듯이 인공지능 학습용 데이터가 부족하여 모델을 구현하진 못했습니다....ㅠㅠ')
st.write('이 사이트는 파이썬으로 개발되었으며, 위 수치는 현재 개인정보보호에 관한 kosis국가 통계의 정보를 바탕으로 계산된 수치입니다.')
'''
st.code(code, language='python')
