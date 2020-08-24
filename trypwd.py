# 密碼重試程式
password = 'a123456'
print ('最多可輸入3次密碼錯誤')
count = 3 #剩餘機會
while count > 0:
	pwd = input ('請輸入密碼: ')
	if pwd == password :
		print ('登入成功!')
		break
	else:
		count = count - 1
		print ('輸入錯誤, 你還有', count, '次機會')