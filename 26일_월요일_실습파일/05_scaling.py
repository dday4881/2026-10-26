# """실습 05 기본필수: train에서 정한 기준을 새 입력에도 적용합니다."""
# from sklearn.preprocessing import StandardScaler

# train = [[100], [200], [300]]
# valid = [[400]]
# scaler = StandardScaler()
# scaler.fit(train)  # 제공: 평균과 크기 기준은 train에서만 구합니다.
# # TODO B05: valid를 transform하여 converted에 넣으세요.
# # 힌트: 학습은 이미 끝났으므로 fit_transform이 아니라 transform을 씁니다.
# converted = None
# print("train 기준 평균:", scaler.mean_)
# print("train 변환:", scaler.transform(train).round(3))
# print("valid 변환:", converted.round(3))
# print("변환 후 기준 평균:", scaler.mean_)
# # valid에 다시 fit하지 않습니다. StandardScaler는 자료를 정규분포로 만들지 않습니다.

"""실습 05 기본필수: train에서 정한 기준을 새 입력에도 적용합니다."""
from sklearn.preprocessing import StandardScaler

train = [[100], [200], [300]]
valid = [[400]]
scaler = StandardScaler()
scaler.fit(train)  # 제공: 평균과 크기 기준은 train에서만 구합니다.
# TODO B05: valid를 transform하여 converted에 넣으세요.
# 힌트: 학습은 이미 끝났으므로 fit_transform이 아니라 transform을 씁니다.
converted = scaler.transform(valid) # 이미 학습을 마친 자료를 받았으니 fit_trasnform이 아닌 transform으로 입력
print("train 기준 평균:", scaler.mean_)
print("train 변환:", scaler.transform(train).round(3))
print("valid 변환:", converted.round(3))
print("변환 후 기준 평균:", scaler.mean_)
# valid에 다시 fit하지 않습니다. StandardScaler는 자료를 정규분포로 만들지 않습니다.

""" 출력 결과 값
train 기준 평균 : [200.]
train 변환 : [[-1.225]
[ 0.   ]
[ 1.225]]
valid 변환 : [[2.449]]
변환 후 기준 평균 : [200.] """

""" fit_transfrom 입력시 출력 결과 값
train 기준 평균 : [400.]
train 변환 : [[-300]
[-200.]
[-100.]]
valid 변환 : [[0.]]
변환 후 기준 평균 : [400.] """