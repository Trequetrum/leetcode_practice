def travel(start = 1, step = 1, n = 20, rep_dict = {3:'Fizz', 5:'Buzz'}):

    mod_dict = {k: (k - start % k) % k for k in rep_dict}

    for i in range(start, n+1, step):
        acc = ''
        for k in rep_dict:

            if mod_dict[k] == 0:
                mod_dict[k] = k
                acc = acc + rep_dict[k]

            mod_dict[k] = mod_dict[k] - step
        
            if mod_dict[k] < 0:
                mod_dict[k] = mod_dict[k] + k
        
        if len(acc) < 1:
            acc = str(i)
        
        print(acc)

travel()
