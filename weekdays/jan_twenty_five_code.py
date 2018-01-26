def get_products_of_all_ints_except_at_index(number_list):
	prod_list = []
	if len(number_list) < 2:
		return []
	else:
		for i in range(len(number_list)):
			prod_list_1 = 1
			prod_list_2 = 1

			if i <2:
				pass
			else:
				for number in range(len(number_list[:i])):
					prod_list_1 *= number_list[:i][number]

			for number in range(len(number_list[i+1:])):
				prod_list_2 *= number_list[i+1:][number]

			prod_list.append(prod_list_1*prod_list_2)
	print(prod_list)
	return prod_list  ## a list of integers


get_products_of_all_ints_except_at_index([1,2,3,4,5])
#get_products_of_all_ints_except_at_index([1])
#get_products_of_all_ints_except_at_index([])
#get_products_of_all_ints_except_at_index([0,0,0,0,0])
#get_products_of_all_ints_except_at_index([1,7,3,4])

