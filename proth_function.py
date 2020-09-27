def proth_prime_test(proth_number,max_testing_value=1000000):
    """ Description of function:
    This function takes in a proth number and evaluates if it is a proth prime or not using proth theorem which states:

    A proth number 'p' is a proth prime if there exists an integer 'a' for which

        (a^(p-1/2))≡ -1 (mod p)

    which can be given as:

        (a^(p-1/2))+1 must be completely divisible by p
    
                or
    
        (a^(p-1/2))+1 mod p = 0
    
    Parameters:
    proth_number(int): this is the proth number 
    max_testing_value(int): this is the maximum range value for integer 'a' , default value is set at 1000000

    Returns:
    None

    Written by Lawson Adesayo

    """
    
    if proth_number <= 0:
        raise ValueError("proth_number value must be a positive integer.")
    if max_testing_value <= 0:
        raise ValueError("max_testing_value must be a positive integer.")
    
   #Step to determine if number given is a proth number 
    x = proth_number-1
    n = 0
    
    while (x%2)== 0:
        n+=1
        x=x//2
    k=x
    
    if (2**n)< k :
        raise ValueError("value is not a proth number")

    #Step to check if given value is a proth prime
    for a in range(1,(max_testing_value+1)):
        c= (a**((proth_number-1)//2))+1
        if c%proth_number==0:
             print(" This proth number is a proth prime\n","Confirmed at a=",a)
             break
    else:
        print(" This number is not a proth prime \n","There is no integer between 1 and",max_testing_value,"that satisfies the conditions\n","You can try a higher max_testing_value")


    
    
    
