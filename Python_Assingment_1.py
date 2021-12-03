"""
Q.1 In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical.

Ans.1 Values = 'hello', -87.8, 6
      expressions = -87.6 + 6, -87.6 * 6, 'hello'*6

Q.2 What is the difference between string and variable?
Ans.2.i. A string is a value between quotes - representing text
      ii. A variable is a name that can refer to any value

Q.3 Describe three different data types.
Ans.3 i. Integers = integers are zero, positive or negative whole numbers without a fractional part.
                    Integers can be binary, octal, and hexadecimal values.
                    binary : 0b11011000 = 216
                    Octal :  0o12 = 10
                    hexadecimal : 0x12 = 15
          All integer literals or variables are objects of the int class.

    ii. Float = The float type in Python represents the floating point number. 
        Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts. 
        For example, 97.98, 32.3+e18, -32.54e100 all are floating point numbers.

        Python float values are represented as 64-bit double-precision values. 
        The maximum value any floating-point number can be is approx 1.8 x 10 raise to the power 308

  iii.  Dict = consist of key-value pairs.
               Dictionaries are enclosed by curly braces {} and values can be assigned and accessed using square braces [] 
               Dictionaries have no concept of order among elements.
               They are simply unordered
               
               dct = {'one':1, 2:'two', (3,4,'Five'):('6',7,8)}

Q.4. What is an expression made up of? What do all expressions do?
Ans.4 The evaluation of an expression produces a value, 
      which is why expressions can appear on the right hand side of assignment statements
      expression made up of : intergers, float, string and mathematical operators.
      2 + 5, x+y, if(x>10 and x<20):

Q.5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?
Ans.5 Expression : An expression evaluates to some value
      "Hello World", 1000, 5 + 3, a * 5 > b
      all expressions have types. "Hello World" is a string type, 5 + 7 is an integer type.
      A statement is never part of an expression.
      Expression is 10

      Statement is spam = 10
      Statement : A statement performs some action.
      An expression can be part of a statement.
      print("Hello World"), sleep(1000), return 55, if (done) exit(8)

Q.6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Ans.6 bacon = 23

Q.7. What should the values of the following two terms be?
'spam' + 'spamspam' = spamspamspam
'spam'*3
Ans.7 'spam' + 'spamspam' = spamspamspam
      'spam'*3 = spamspamspam

Q.8. Why is eggs a valid variable name while 100 is invalid?
Ans.8 Because values can't be assigned to literal and variable name shouldn't be an integer.

Q.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?
Ans.9 int() for getting integer version of value
      float() for getting floating-point version of value
       str() for getting string version of value

Q.10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos'
Ans.10 because string and integer values cannot be concatenated together so,
        i have to change datatype of 99 from integer version to string version.
        'I have eaten ' + str(99) + ' burritos.' 

"""