import numpy as np

if __name__ == '__main__':
    lines = 'date,price,region\n2015-07-19,1.08,Louisville\n2015-08-16,1.05,RichmondNorfolk\n2015-04-05,1.1,' \
            'Orlando\n2015-07-26,1.12,GrandRapids\n2015-05-31,1.1,Atlanta'
    lines = lines.split()
    prices = list()
    for line in lines:
        if line.find('price') > 0:  # using in operator: 'price' in line
            continue
        price = line.split(',')[1]
        prices.append(float(price))
    print('Min: %.2f' % np.min(prices))
    print('Max: %.2f' % np.max(prices))
    print('Mean: %.3f' % np.mean(prices))
    print('Std: %.4f' % np.std(prices, ddof=1))  # standard deviation based on a sample
