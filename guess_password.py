password = input('請輸入想要設定的密碼：')
i = 3 #剩餘機會
while i >0:
	i = i - 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！')
		break #逃出迴圈
	else:
		if i > 0:
			print('密碼錯誤！你還有', i, '次機會')	
		else:
			break	



