#name your file as GamesSalesAnalytic.py and test your code.
from GamesSalesAnalytic import Analytic
from collections import Counter

dA = {'name': 'Game A', 'platform': 'PS4', 'year_of_release': 2015, 'genre': 'Action', 'publisher': 'Sony', 'global_sales': 3.5, 'critic_score': 85, 'developer': 'DevStudio', 'rating': 'M'}
dB = {'name': 'Game B', 'platform': 'Xbox', 'year_of_release': 2012, 'genre': 'Shooter', 'publisher': 'Microsoft', 'global_sales': 2.7, 'critic_score': 78, 'developer': 'GameMakers', 'rating': 'M'}
dC = {'name': 'Game C', 'platform': 'PC', 'year_of_release': 2010, 'genre': 'Strategy', 'publisher': 'EA', 'global_sales': 1.2, 'critic_score': 90, 'developer': 'ThinkDev', 'rating': 'E'}
dD = {'name': 'Game D', 'platform': 'PS4', 'year_of_release': 2016, 'genre': 'Action', 'publisher': 'Sony', 'global_sales': 5.3, 'critic_score': 88, 'developer': 'NextGen', 'rating': 'M'}
dE = {'name': 'Game E', 'platform': 'Switch', 'year_of_release': 2019, 'genre': 'Adventure', 'publisher': 'Nintendo', 'global_sales': 6.1, 'critic_score': 92, 'developer': 'NintendoDev', 'rating': 'E'}
dF = {'name': 'Game F', 'platform': 'PS4', 'year_of_release': 2011, 'genre': 'Action', 'publisher': 'Sony', 'global_sales': 2.0, 'critic_score': 81, 'developer': 'DevStudio', 'rating': 'M'}
dG = {'name': 'Game G', 'platform': 'Xbox', 'year_of_release': 2014, 'genre': 'Shooter', 'publisher': 'Microsoft', 'global_sales': 2.9, 'critic_score': 80, 'developer': 'GameMakers', 'rating': 'M'}


def cmp(list1, list2):
	list1_as_set = Counter([frozenset(d.items()) for d in list1])
	list2_as_set = Counter([frozenset(d.items()) for d in list2])

	return list1_as_set == list2_as_set


def main():
	analytic = Analytic("GamesSales.csv")
	#return the number of records
	assert analytic.count == 7
	platforms = analytic.get_platforms()
	assert set(platforms) == set(['Xbox', 'Switch', 'PS4', 'PC'])
	genres = analytic.get_genres()
	assert set(genres) == set(['Shooter', 'Adventure', 'Strategy', 'Action'])

	#test for single fields input
	data = analytic.match(name=["Game A"])
	assert cmp(data, [dA]) == True

	data = analytic.match(name=["Game A", "Game B"])
	assert cmp(data, [dA, dB]) == True

	data = analytic.match(platform=["PS4"])
	assert cmp(data, [dA, dD, dF]) == True

	data = analytic.match(platform=["PS4", "Xbox"])
	assert cmp(data, [dA, dB, dD, dF, dG]) == True

	data = analytic.match(year_of_release=[2014, 2015])
	assert cmp(data, [dA, dG]) == True

	data = analytic.match(genre=["Action", "Adventure"])
	assert cmp(data, [dA, dD, dE, dF]) == True

	data = analytic.match(publisher=["Sony", "Microsoft"])
	assert cmp(data, [dA, dB, dD, dF, dG]) == True

	data = analytic.match(global_sales=[2, 3.5])
	assert cmp(data, [dA, dB, dF, dG]) == True

	data = analytic.match(critic_score=[80, 90])
	assert cmp(data, [dA, dC, dD, dF, dG]) == True

	data = analytic.match(developer=["DevStudio", "ThinkDev"])
	assert cmp(data, [dA, dC, dF]) == True

	data = analytic.match(rating=["E", "M"])
	assert cmp(data, [dA, dB, dC, dD, dE, dF, dG]) == True

	#test for two fields input
	data = analytic.match(platform=["PS4", "Xbox"], year_of_release=[2014, 2015])
	assert cmp(data, [dA, dG]) == True

	data = analytic.match(platform=["PS4", "Xbox"], genre=["Action", "Shooter"])
	assert cmp(data, [dA, dB, dD, dF, dG]) == True

	print('passed')

	#add in more test cases on your own....
	#Another set of more comprehensive test cases will be use to mark your code.

	#begin you testing adventure here.....
	#test for three fields input...
	#test for four fields input...


def error_test():
	analytic = Analytic("GamesSales_Errors.csv")
	data = analytic.match(name=["Game A", "Game C", "Game E"])
	assert cmp(data, [dA, dC, dE]) == True


if __name__ == "__main__":
	main()
	error_test()
