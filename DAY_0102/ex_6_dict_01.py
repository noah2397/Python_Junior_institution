#----------------------------------------------
# [질문] 10명 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
#----------------------------------------------

# # 방법 1) 학생 이름 변수 10개 => stdName1 ~ stdName10
# #        학점 변수 10개     => jumsu1 ~ jumsu10
#
# # 방법 2) 학생 이름 변수 10개 => stdNames=[학생 이름1, 학생이름2, .., 학생 이름10]
# #        학점 변수 10개     => stdJumsus=[점수1, ..., 점수10]
#
# stdNums=['std01','std02','std03','std04','std05']
# stdJumsus=[90,89,100,76,34]
#
# # -> 학번 03번 학생의 학번과 점수를 출력하세요
#
# idx=stdNums.index('std03')
# print(f"{stdNums[idx]}학번 학생의 점수 {stdJumsus[idx]}")
#
# # 방법 3) 학생 이름 변수 5개 => stdNames=[학생 이름1, ..., 학생 이름5]
# #        학점 변수 5개     => stdJumsus=[점수1, ..., 점수5]
# stdNumsJumsu=[['std01',90],['std02',89],['std03',100],['std04',76],['std05',34]]


#------------------------------------------------------
# dict 자료형
# -연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# -형태 => 키 : 데이터 (예 : 주민번호:이름, 학번:전공)
# -조건 => 키가 중복되면 안됨!
# -문법 => {키1:데이터1, 키2:데이터2, ..., 키N:데이터N}
#------------------------------------------------------
stdNumsJumsu={'std01':90,'std02':89,'std03':100,'std04':76,'std05':34}
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개,{type(stdNumsJumsu)}, {stdNumsJumsu}')

# 원소 읽는 방법 => 변수명[키]
print(f'stdNumsJumsu["std03f"] => {stdNumsJumsu["std03"]}')

# 마지막 원소 지정하는 -1 사용 => -1 에 대한 키가 없으면 Error
#print(f'stdNumsJumsu[-1] => {stdNumsJumsu[-1]}') # -1인 키값을 가지는 걸 조회하므로, 에러가 뜬다


#----------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[신규 키] = 새로운 데이터
#----------------------------------------------------------
#학번 10인 학생의 점수 99.8 저장 추가하기
stdNumsJumsu['sud10']=99.8
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개,{type(stdNumsJumsu)}, {stdNumsJumsu}')

#----------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[기존 키] = 새로운 데이터
#----------------------------------------------------------
#학번 10인 학생의 점수 99점으로 변경 추가하기
stdNumsJumsu['sud10']=99
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개,{type(stdNumsJumsu)}, {stdNumsJumsu}')

del stdNumsJumsu['std01']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개,{type(stdNumsJumsu)}, {stdNumsJumsu}')