# """실습 01 기본필수: 학습과 예측 두 문장을 연결합니다."""
# from sklearn.linear_model import LinearRegression

# # X는 한 행이 한 사람이고, 각 행의 숫자는 공부시간입니다. 그래서 [[1], [2], ...]입니다.
# X = [[1], [2], [3], [4], [5]]
# y = [52, 61, 69, 80, 89]  # 같은 순서의 실제 점수
# model = LinearRegression()  # 선을 맞추는 모델을 준비합니다. 아직 학습 전입니다.
# # TODO B01: model을 X, y로 학습하고, [[6]]의 예측을 prediction에 넣으세요.
# # 힌트: fit에는 입력과 정답, predict에는 입력만 전달합니다.
# pass
# prediction = None
# print("기울기:", round(model.coef_[0], 1))
# print("절편:", round(model.intercept_, 1))
# print("6시간 예측:", round(prediction[0], 1))
# # 주의: 6시간은 학습 범위 1~5시간 밖입니다. 수식 확인용이며 실제 점수를 보장하지 않습니다.

"""실습 01 기본필수: 학습과 예측 두 문장을 연결합니다."""
from sklearn.linear_model import LinearRegression

# X는 한 행이 한 사람이고, 각 행의 숫자는 공부시간입니다. 그래서 [[1], [2], ...]입니다.
X = [[1], [2], [3], [4], [5]]
y = [52, 61, 69, 80, 89]  # 같은 순서의 실제 점수
model = LinearRegression()  # 선을 맞추는 모델을 준비합니다. 아직 학습 전입니다.
# TODO B01: model을 X, y로 학습하고, [[6]]의 예측을 prediction에 넣으세요.
# 힌트: fit에는 입력과 정답, predict에는 입력만 전달합니다.
# pass
# prediction = None
"""힌트 윗 줄에 model = LinearRgression()을 받았으니 fit을 입력해서 X값과 y값을 입력해주기
힌트를 보면 예측에 prediction 정답에 predict를 입력하라는 지시가 있어서 prediction = model.predict를 입력해주고, [[6]]의 예측을 입력하라 지시 하였으니([[6]])를 넣기"""
model.fit(X, y)
prediction = model.predict([[6]]) #중괄호 2개를 입력하는거 실수 하지 않도록 확인 잘 하자
print("기울기:", round(model.coef_[0], 1))
print("절편:", round(model.intercept_, 1))
print("6시간 예측:", round(prediction[0], 1))
# 주의: 6시간은 학습 범위 1~5시간 밖입니다. 수식 확인용이며 실제 점수를 보장하지 않습니다.

"""# 출력 결과 값
# 기울기 : 9.3
# 절편 : 42.3
# 6시간 예측 : 98.1 """