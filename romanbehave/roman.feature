Feature: convert integer to roman numberal

    Scenario Outline: I give an integer
      Given number <number> is entered to the program
      when pass to int_to_roman
      then it should return "<roman>"

    Examples: convert
    | number		   | roman 	    |
    | 1				   | I  		|
    | 3				   | III 		|
    | 5				   | V 		    |
    | 6				   | VI 		|	
    | 8				   | VIII		|	
    | 9				   | IX 		|
    | 13			   | XIII 	    |
    | 16			   | XVI 		|
    | 20			   | XX 		|
    | 19			   | XIX 		|
    | 2013			   | MMXIII	    |