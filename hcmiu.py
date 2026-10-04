print('python')
scores=[1,3,6,8,2]
print("MY SCORES:",scores[2])
print('My total scores:',len(scores))

scores =[8,7,9,6,10]
for score in scores:
    print(score)
    total=0
    total+=1
    average=total/len(scores)
    print(average)
    total=0
    total+=1
    for score in scores:
        average=total/len(scores)
        print(scores[2])

scores=[8,7,9,6,10]

for i in range(1,101):
 if (i%3==0) and (i%5==0):
   print('FizzBuzz')
 elif (i%3==0):
   print('Fizz')
 elif (i%5==0):
   print('Buzz')
 else:
    print(i)

    scores=[8,7,9,6,10,5,7.5,8.5]
    Highest_val=scores[0]
    Smallest_val=scores[0]
    greater_count=0
    num_students=len(scores)
    pass_count=0
    total_scores=0

    for X in scores:
       if X > Highest scores:
          Highest scores=X 
        if X < Smallest scores:
          Smallest scores=X 
        if X >= 8:
          greater_count+=1
          total_scores+=X
        if X>=5:
         pass_count+=1
    Average=total_scores/len(scores)
    pass_rate=(pass_count/len(scores))*100
    print('===STUDENT GRADE ANALYZER===')
    print(f'Number of students:{num_students}')
    print(f'HIGHEST SCORE: {Highest_val}')
    print(f'SMALLEST SCORES: {Smallest_val}')
    print(f'The Average of Scores: {Average}')
    print(f'PASS EXAM:{pass_count}')
    



    x=2,y=3
    print(f'x={x}')
    print('value of',x,"+",x,"is",(x+x))
    print('x=')
    print((x+y),'=',(y+x))