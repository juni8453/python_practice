# end 매개변수로 마지막을 공백말고 다른 것으로 설정할 수 있다.
# default 는 \n
print('집단지성')
print('집단지성', end='')
print('집단지성')
print('집단지성', end="/")
print('')

# Escape code \n (줄바꿈), \t (탭)
print('미운코딩새끼의\n집단지성들')
print('미운코딩새끼의\t집단지성들')
print('미운코딩새끼의\t집단\n지성들')

# 출력 결과
# 집단지성
# 집단지성집단지성
# 집단지성/
# 미운코딩새끼의
# 집단지성들
# 미운코딩새끼의	집단지성들
# 미운코딩새끼의	집단
# 지성들