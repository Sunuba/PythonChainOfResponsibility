# Chain of Responsibility Pattern in Python

The intent in this pattern is to decouple sender and receiver. The best way to understand this
example is to code an ATM system where distributes money value into available nominal values and
prints out the number of nominal and nominal values. Then try it in the Chain of Responsibility
Pattern to feel the difference. Now, let's assume that we are writing a software for ATM to handle 
money. For example, a person comes to an ATM and want to get cash amount of 125, currency
is not important at this time. We have the following nominal inside ATM or any other 
exchange types: 

- 100
- 50
- 20
- 10
- 5
- 1

We will apply Strategy Pattern here in order to switch between exchange types without changing 
anything inside Exchange.py file. I mean in Exchange.py file you can use `money = ATM(99)` or 
`money = BankBranch(99)`. You can add your own exchange point with different distribute algorithm
without touching any other Classes, this is cool.

We now will use chain of responsibility to give cash to the client.

First, we will distribute the total amount into pieces. To do this we create an ATM class 
where we will keep all the numbers for each nominal. ATM has a distribute method, 
this method simply divides all amount into possible nominal values. 

 For example:

    money = ATM(199) # We want 99 in cash, so we entered 99 to the ATM
    money.distribute() # We pressed confirm button and ATM distributed the money into nominals
    print(money.__dict__)
Result will be:

    {
    'money': 199, 
    'n100': 1.0, 
    'n50': 1.0, 
    'n20': 2.0, 
    'n10': 0.0, 
    'n5': 1.0, 
    'n1': 4.0
    }
    

1\*50+2\*20+1\*5+4\*1 = 50+40+5+4 = 199. Cool, it works perfectly.

Now, we will try to implement chain of responsibility. For each nominal value, we have a class:

    give100 = Give100()
    give50 = Give50()
    give20 = Give20()
    give10 = Give10()
    give5 = Give5()
    give1 = Give1()

Each class extends CashHandler abstract class. CashHandler class handles the queue.

Now, as we are done with the coding we can get a cash from ATM:

    money = ATM(199) # you can also use money = BankBranch(199) - where 50 nominal values are not available, so outcome will be different.
    money.distribute()
    
    give100 = Give100()
    give50 = Give50()
    give20 = Give20()
    give10 = Give10()
    give5 = Give5()
    give1 = Give1()
    
    # This is where chain is happening
    give100.set_successor(give50)
    give50.set_successor(give20)
    give20.set_successor(give10)
    give10.set_successor(give5)
    give5.set_successor(give1)
    
    
    # This is where the chain is starting
    give100.give(money)

The result will be:

    Give 1.0 100 in cash. 
    Give 1.0 50 in cash. 
    Give 2.0 20 in cash. 
    Give 1.0 5 in cash. 
    Give 4.0 1 in cash. 

Sum is 199

If we request 158:
    
    money = ATM(158);
    ...

The result will be:

    Give 1.0 100 in cash. 
    Give 1.0 50 in cash. 
    Give 1.0 5 in cash. 
    Give 3.0 1 in cash. 
    
Sum is 158

Also, in the future it is possible that a client may want to exchange money from different
sources such as bank branches. May be in the bank branches they do not give 50 nominal value 
(let's assume something like this) or they have a certain pattern for exchange. Then you can
implement your own exchange service by extending ExchangeAbstractClass class. In our example
BankBranch does not give 50 nominal values so when you use it like this: `money = BankBranch(99)`
it will give you money in the following way:

    Give 4.0 20 in cash. 
    Give 1.0 10 in cash. 
    Give 1.0 5 in cash. 
    Give 4.0 1 in cash. 

As we do not have 50 nominal value in the bank, we will get 4 20 nominal values and so on.

In `money = ATM(99);` The result will be the following:

    Give 1.0 50 in cash. 
    Give 2.0 20 in cash. 
    Give 1.0 5 in cash. 
    Give 4.0 1 in cash.

Just extend ExchangeAbstractClass and create your own exchange service.

Thanks.

