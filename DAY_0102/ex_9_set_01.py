#---------------------------------------------------------
# set 데이터 타입
# - 제일 마지막에 추가된 타입
# - 목적 : 중복 데이터 제거
# - 특징 : 이미 존재하는 데이터는 저장하지 않음!!
# - 문법 : {데이터1, 데이터2, ..., 데이터N}
#---------------------------------------------------------
# 빈 데이터 타입 생성
'''
aList=[]
aTuple=()
aDict={}
aSet=set()
aStr=''

print(f'aList=> {type(aList)}, {len(aList)}개')
print(f'aTuple=> {type(aTuple)}, {len(aTuple)}개')
print(f'aDict=> {type(aDict)}, {len(aDict)}개')
print(f'aSet=> {type(aSet)}, {len(aSet)}개')
print(f'aStr=> {type(aStr)}, {len(aStr)}개\n\n')

#-----------------------------------------
# 생성자 메서드 => 타입이름과 동일한 함수명
# - 힙 영역에 메모리 공간을 잡고, 데이터 초기화 기능 수행
# - 해당 타입의 객체를 생성
aList=list()
aTuple=tuple()
aDict=dict()
aSet=set()
aStr=str()

print(f'aList=> {type(aList)}, {len(aList)}개')
print(f'aTuple=> {type(aTuple)}, {len(aTuple)}개')
print(f'aDict=> {type(aDict)}, {len(aDict)}개')
print(f'aSet=> {type(aSet)}, {len(aSet)}개')
print(f'aStr=> {type(aStr)}, {len(aStr)}개\n\n')


# 매직 메서드 __init__

#----------------------------------------------
set 타입의 데이터 생성
a1={1,1,2,3,4,2,1,5,3,6,4,2,1} # 셋은 중복 데이터는 배제한다
a2=[1,1,2,3,4,2,1,5,3,6,4,2,1] # 리스트는 중복 상관없다
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')
print(f'a2=> {type(a2)}, {len(a2)}개, {a2}\n')

a2=list(set(a2)) # 중복을 제거한 리스트로 변환
print(f'a2=> {type(a2)}, {len(a2)}개, {a2}')


#-------------------------------------------------
# set 타입의 연산 수행
#-------------------------------------------------
a1={1,3,5,1,2}
b1={1,2,3,4,5,6,7,8,9,10}
#print(a1+b1, a1*2) # 셋에서는 덧셈 연산과 곱셈을 지원하지 않는다

# 죽어도 하고 싶으면 형변환 후에 더하면 된다
# 연산 수행 => 형변환 후 수행-------------------------
a1,b1=list(a1), list(b1)
print(a1+b1, a1*2)

#---------------------------------------------------------
# 원소/요소 읽기/수정/삭제/추가 ===> 인덱스x, 키 x ==> 메서드 제공
#---------------------------------------------------------

a1=set()
# 한 개 넣는 건 add, 여러개 넣는 건 update다
# 원소/요소 추가 => 1개 추가 : add()메서드
a1.add(10)
a1.add(10)
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')

a1.add('A')
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')

#여러개의 원소/요소 추가 => update
a1.update([11,22,33,44,55])
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')

a1.update("Good Luck !!")
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')

a1.add("Good Luck!!")
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')


# 원소/요소 삭제 => remove(데이터)
a1.remove('G')
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')
pop_item=a1.pop()
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}, popitem : {pop_item}')
a1.discard('G') # discard는 지울게 없어도 에러를 내뿜지 않는다
print(f'a1=> {type(a1)}, {len(a1)}개, {a1}')

#-----------------------------------------------
# 집합에 관련된 메서드들과 기호 / 연산자
#-----------------------------------------------
# 교집합 =======================================
# - 여러개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호/연산자 : &
# - 메서드 : intersection()
#-----------------------------------------------
a1=set()
a1.update("Happy")
a2=a1.intersection({'a','A','b','B'})
print(f'교집합한 a2 => {a2}', a1 & a2)

# 합집합
# - 여거래의 집합에 중복은 1개만 포함한 모든 원소의 집합
# - 기호 연산자 : |, 연산자
# - 메서드 : union()
a1=set()
a1.update("Happy")
a2=a1.union({'a','A','b','B'})
print(f'합집합한 a2 => {a2}', a1 | a2)

# 차집합 -------------------------------------
a2=a1.difference({'a','A','b','B'}) # 교집함의 데이터를 제외한 나머지 데이터
print(f'차집합한 a2 => {a2}', a1-{'a','A','b','B'})

a3={'a','A','b','B'}.difference(a1)
print(f'a3 => {a3}',{'a','A','b','B'}-a1)
'''

# 정렬 -------------------------------------------------------------------
# => 원소 값을 서로 비교해서 작은 데이터 >> 큰 데이터 순서로 저장 => 오름차순 정렬
# => 원소 값을 서로 비교해서 큰 데이터 >> 작은 데이터 순서로 저장 => 내림차순 정렬
# => set 타입에는 정렬 메서드 없음 =======> 내장함수 sorted()
#------------------------------------------------------------------------
#
a1={'A','B','C','DD','F'}
print(f'a1 => {type(a1)}, {a1}')
a1=sorted(a1)
print(f'a1 => {type(a1)}, {a1}')

















