if __name__ == '__main__':
    line = '35 40'
    nums = line.split()
    if nums[0] > nums[1]:
        print('>')
    elif nums[0] < nums[1]:
        print('<')
    else:
        print('=')
