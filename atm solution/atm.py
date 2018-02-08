# allowed papers: 100, 50, 10, 5, 1 and cents

money = 500
request = 5.5
init_money = money

if request == 0:
	print 'can\'t give you 0 money'
else:
	while request != 0:
		if money != 0:
			if request >= 1:
				if request > 5:
					if request > 10:
						if request > 50:
							if request > 100:
								request -= 100
								money -= 100
								print 'give 100'
							else:
								request -= 50
								money -= 50
								print 'give 50'
						else:
							request -= 10
							money -= 10
							print 'give 10'
					else:
						request -= 5
						money -= 5
						print 'give 5'
				else:
					print 'give', 5 - (5 - int(request))
					request -= int(request)
					money -= int(request)
					
			else:
				if request < 0:
					print 'can\'t give you negative money'
					break
				print 'give', request * 100, 'cents'
				request -= request
				money -= money
		else:
			needed = request - money
			print 'not enough money in atm, you got:', init_money, 'and you need:', needed, '$'
			request = 0
